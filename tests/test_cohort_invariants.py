"""Cohort invariant test to ensure no future cohort drift in feature engineering or modeling."""

from pathlib import Path
import pandas as pd
import pytest


def test_primary_cohort_invariants():
    """Assert that the primary cohort manifest exists, contains exactly 21,616 distinct episodes,
    spans exactly 414 matches, has no duplicates, and matches the live counterpress_episodes.csv.
    """
    manifest_path = Path("results/tables/primary_cohort_episode_ids.csv")
    assert manifest_path.exists(), f"Primary cohort manifest {manifest_path} must exist!"

    manifest = pd.read_csv(manifest_path)

    # 1. Exact count invariant
    assert len(manifest) == 21616, f"Expected exactly 21,616 primary episodes, found {len(manifest)}"

    # 2. No duplicates
    assert manifest["episode_id"].nunique() == 21616, "Found duplicate episode IDs in primary cohort manifest!"

    # 3. Exact match count invariant
    assert manifest["match_id"].nunique() == 414, f"Expected exactly 414 unique matches, found {manifest['match_id'].nunique()}"

    # 4. Required columns
    expected_cols = {"episode_id", "match_id", "competition", "season"}
    assert set(expected_cols).issubset(set(manifest.columns)), f"Missing required columns in manifest: {expected_cols - set(manifest.columns)}"

    # 5. Live dataset alignment (if counterpress_episodes.csv is present)
    episodes_path = Path("results/tables/counterpress_episodes.csv")
    if episodes_path.exists():
        episodes_df = pd.read_csv(episodes_path, low_memory=False)
        pri_live = episodes_df[episodes_df["primary_cohort_eligible"]]

        assert len(pri_live) == 21616, f"Live primary cohort length {len(pri_live)} != 21616"
        assert set(pri_live["episode_id"]) == set(manifest["episode_id"]), "Live primary cohort episode IDs do not match frozen manifest!"
