"""Generate frozen cross-validation fold assignments for Iteration 4 modeling.

Enforces:
- Exact match with canonical primary cohort (21,616 episodes, 414 matches).
- 5-fold GroupKFold strictly grouped by match_id.
- Reproducible random seed (seed=42) for group shuffling.
- Output file: results/tables/model_cv_folds.csv
"""

import logging
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold

from counterpress.config import PROCESSED_DIR, TABLES_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

RANDOM_SEED = 42


def setup_cv_folds():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    cohort_manifest_path = TABLES_DIR / "primary_cohort_episode_ids.csv"
    output_folds_path = TABLES_DIR / "model_cv_folds.csv"

    logger.info(f"Loading primary feature dataset from {parquet_path}...")
    df = pd.read_parquet(parquet_path)

    # Invariant checks
    assert len(df) == 21616, f"Expected 21,616 rows, got {len(df)}"
    assert df["episode_id"].nunique() == 21616, "Duplicate episode_ids found"
    assert df["match_id"].nunique() == 414, f"Expected 414 matches, got {df['match_id'].nunique()}"

    logger.info(f"Loading primary cohort manifest from {cohort_manifest_path}...")
    manifest_df = pd.read_csv(cohort_manifest_path)
    cohort_ids = set(manifest_df["episode_id"])
    assert set(df["episode_id"]) == cohort_ids, "Features episode_ids do not match cohort manifest exactly!"

    logger.info("Setting up 5-fold GroupKFold grouped by match_id with seed 42...")
    # Shuffle match_ids reproducibly with fixed random seed
    unique_matches = df["match_id"].unique()
    rng = np.random.RandomState(RANDOM_SEED)
    shuffled_matches = rng.permutation(unique_matches)

    # Map each match to a fold using GroupKFold
    # GroupKFold balances total observations per fold across groups
    gkf = GroupKFold(n_splits=5)
    
    # Create match-level DataFrame with group counts for optimal GroupKFold balancing
    match_counts = df.groupby("match_id").size().loc[shuffled_matches].reset_index(name="n_episodes")
    
    match_to_fold = {}
    for fold_idx, (_, val_idx) in enumerate(gkf.split(match_counts, groups=match_counts["match_id"])):
        val_matches = match_counts.iloc[val_idx]["match_id"].values
        for m in val_matches:
            match_to_fold[m] = fold_idx

    df["fold"] = df["match_id"].map(match_to_fold)

    # Invariant checks on fold assignments
    assert not df["fold"].isna().any(), "Unassigned fold found!"
    assert df["fold"].nunique() == 5, f"Expected 5 folds, got {df['fold'].nunique()}"

    # Verify no match_id appears in more than one fold
    match_fold_counts = df.groupby("match_id")["fold"].nunique()
    assert (match_fold_counts == 1).all(), "Match ID present in multiple folds! Leakage detected!"

    logger.info("Fold distribution summary:")
    fold_summary = df.groupby("fold").agg(
        n_episodes=("episode_id", "count"),
        n_matches=("match_id", "nunique"),
        regain_5s_rate=("regain_5s_controlled", "mean"),
        danger_15s_rate=("dangerous_escape_15s", "mean"),
    ).reset_index()
    print(fold_summary.to_string(index=False))

    # Save minimal frozen fold assignment table
    folds_df = df[["episode_id", "match_id", "fold"]].copy()
    folds_df.to_csv(output_folds_path, index=False)
    logger.info(f"Saved frozen CV folds to {output_folds_path} ({len(folds_df)} rows).")


if __name__ == "__main__":
    setup_cv_folds()
