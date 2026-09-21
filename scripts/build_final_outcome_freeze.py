"""Generate final outcome freeze summary table and frozen primary cohort episode manifest.

Outputs:
1. results/tables/final_outcome_freeze_summary.csv
2. results/tables/primary_cohort_episode_ids.csv
"""

import json
import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

RESULTS_DIR = Path("results")
TABLES_DIR = RESULTS_DIR / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)


def main():
    episodes_path = TABLES_DIR / "counterpress_episodes.csv"
    if not episodes_path.exists():
        raise FileNotFoundError(f"Episodes file {episodes_path} not found.")

    logger.info(f"Loading episodes from {episodes_path}...")
    df = pd.read_csv(episodes_path, low_memory=False)

    total_episodes = len(df)
    total_actions = int(df["num_counterpress_actions"].sum())

    # Primary cohort
    primary = df[df["primary_cohort_eligible"]].copy()
    n_primary = len(primary)
    n_primary_matches = primary["match_id"].nunique()

    logger.info(f"Full dataset: {total_episodes} episodes, {total_actions} actions.")
    logger.info(f"Primary cohort: {n_primary} episodes across {n_primary_matches} unique matches.")

    # 1. Generate frozen primary cohort manifest
    manifest_df = primary[["episode_id", "match_id", "competition_name", "season_name"]].copy()
    manifest_df.rename(columns={"competition_name": "competition", "season_name": "season"}, inplace=True)
    manifest_path = TABLES_DIR / "primary_cohort_episode_ids.csv"
    manifest_df.to_csv(manifest_path, index=False)
    logger.info(f"Saved frozen primary cohort manifest to {manifest_path} ({len(manifest_df)} rows).")

    # 2. Compute canonical freeze values
    r3_cnt = int(primary["regain_3s_controlled"].sum())
    r3_pct = round(float(primary["regain_3s_controlled"].mean() * 100), 2)

    r5_cnt = int(primary["regain_5s_controlled"].sum())
    r5_pct = round(float(primary["regain_5s_controlled"].mean() * 100), 2)

    r8_cnt = int(primary["regain_8s_controlled"].sum())
    r8_pct = round(float(primary["regain_8s_controlled"].mean() * 100), 2)

    de15_cnt = int(primary["dangerous_escape_15s"].sum())
    de15_pct = round(float(primary["dangerous_escape_15s"].mean() * 100), 2)

    sr_cnt = int((primary["episode_outcome_3class"] == "successful_regain").sum())
    sr_pct = round(float(sr_cnt / n_primary * 100), 2)

    he_cnt = int((primary["episode_outcome_3class"] == "harmless_escape").sum())
    he_pct = round(float(he_cnt / n_primary * 100), 2)

    de_cnt = int((primary["episode_outcome_3class"] == "dangerous_escape").sum())
    de_pct = round(float(de_cnt / n_primary * 100), 2)

    freeze_rows = [
        {
            "Metric": "raw_counterpress_actions",
            "Final_Value": f"{total_actions:,}",
            "Definition": "Event records in StatsBomb Open Data with counterpress=True across 424 audited matches",
            "Version_Source": "StatsBomb Open Data / Iteration 2.7 Freeze",
        },
        {
            "Metric": "distinct_episodes",
            "Final_Value": f"{total_episodes:,}",
            "Definition": "Chained counterpress actions collapsed into distinct temporal episodes (open play and restarts)",
            "Version_Source": "Extraction Pipeline / Iteration 2.7 Freeze",
        },
        {
            "Metric": "primary_cohort_episodes",
            "Final_Value": f"{n_primary:,}",
            "Definition": "Open-play, valid turnover delay (0-5s), high linkage quality, usable 360 freeze frame, non-MLS",
            "Version_Source": "Cohort Filter / Iteration 2.7 Freeze",
        },
        {
            "Metric": "primary_cohort_matches",
            "Final_Value": f"{n_primary_matches}",
            "Definition": "Unique match IDs containing at least one primary cohort counterpress episode",
            "Version_Source": "Cohort Filter / Iteration 2.7 Freeze",
        },
        {
            "Metric": "regain_3s_controlled",
            "Final_Value": f"{r3_pct:.2f}% ({r3_cnt:,})",
            "Definition": "Established controlled possession (carry, completed pass, dribble, shot, receipt) within 3.0s following turnover/acquisition",
            "Version_Source": "Methodologically Refined Engine (Fixed opp_team)",
        },
        {
            "Metric": "regain_5s_controlled",
            "Final_Value": f"{r5_pct:.2f}% ({r5_cnt:,})",
            "Definition": "Primary Outcome 1: Established controlled possession within 5.0s following turnover/acquisition evidence",
            "Version_Source": "Methodologically Refined Engine (Fixed opp_team)",
        },
        {
            "Metric": "regain_8s_controlled",
            "Final_Value": f"{r8_pct:.2f}% ({r8_cnt:,})",
            "Definition": "Established controlled possession within 8.0s following turnover/acquisition evidence (sensitivity target)",
            "Version_Source": "Methodologically Refined Engine (Fixed opp_team)",
        },
        {
            "Metric": "dangerous_escape_15s",
            "Final_Value": f"{de15_pct:.2f}% ({de15_cnt:,})",
            "Definition": "Primary Outcome 2: Opponent shot or attacking final-third entry (x >= 80.0) within 15.0s before pressing regain",
            "Version_Source": "Methodologically Refined Engine (Fixed opp_team)",
        },
        {
            "Metric": "successful_regain",
            "Final_Value": f"{sr_pct:.2f}% ({sr_cnt:,})",
            "Definition": "Three-State Class 1: regain_5s_controlled == 1 and dangerous_escape_15s == 0",
            "Version_Source": "Canonical Three-State Partition",
        },
        {
            "Metric": "harmless_escape",
            "Final_Value": f"{he_pct:.2f}% ({he_cnt:,})",
            "Definition": "Three-State Class 2: regain_5s_controlled == 0 and dangerous_escape_15s == 0",
            "Version_Source": "Canonical Three-State Partition",
        },
        {
            "Metric": "dangerous_escape",
            "Final_Value": f"{de_pct:.2f}% ({de_cnt:,})",
            "Definition": "Three-State Class 3: dangerous_escape_15s == 1 (takes hierarchical precedence over regain)",
            "Version_Source": "Canonical Three-State Partition",
        },
    ]

    freeze_df = pd.DataFrame(freeze_rows)
    summary_path = TABLES_DIR / "final_outcome_freeze_summary.csv"
    freeze_df.to_csv(summary_path, index=False)
    logger.info(f"Saved authoritative summary table to {summary_path}")
    print(freeze_df.to_string(index=False))


if __name__ == "__main__":
    main()
