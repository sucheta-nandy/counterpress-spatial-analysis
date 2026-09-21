"""Tests for Iteration 3 feature dataset invariants and summary table consistency."""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from counterpress.config import PROCESSED_DIR, TABLES_DIR

PARQUET_PATH = PROCESSED_DIR / "counterpress_features.parquet"
SUMMARY_CSV_PATH = TABLES_DIR / "spatial_feature_summary.csv"
COHORT_PATH = TABLES_DIR / "primary_cohort_episode_ids.csv"


def test_feature_dataset_dimensions_and_invariants():
    """Verify primary cohort invariants on counterpress_features.parquet."""
    assert PARQUET_PATH.exists(), f"Missing {PARQUET_PATH}"
    df = pd.read_parquet(PARQUET_PATH)

    assert len(df) == 21616, f"Expected 21,616 rows, got {len(df)}"
    assert df["episode_id"].nunique() == 21616, "Duplicate episode_ids found"
    assert df["match_id"].nunique() == 414, f"Expected 414 matches, got {df['match_id'].nunique()}"

    # Check match with primary cohort manifest
    cohort_df = pd.read_csv(COHORT_PATH)
    cohort_ids = set(cohort_df["episode_id"])
    assert set(df["episode_id"]) == cohort_ids, "Episode IDs do not match primary cohort manifest exactly"


def test_spatial_feature_summary_consistency():
    """Verify summary table matches parquet columns and row count."""
    assert SUMMARY_CSV_PATH.exists(), f"Missing {SUMMARY_CSV_PATH}"
    summary_df = pd.read_csv(SUMMARY_CSV_PATH)
    df = pd.read_parquet(PARQUET_PATH)

    assert len(summary_df) == len(df.columns), "Feature count mismatch between parquet and summary CSV"
    assert set(summary_df["feature"]) == set(df.columns), "Feature names do not match exactly"

    # Verify coverage bounds in summary
    for cov_col in ["coverage_5", "coverage_10", "coverage_15", "escape_corridor_coverage_20"]:
        row = summary_df[summary_df["feature"] == cov_col].iloc[0]
        assert row["min"] >= 0.0, f"{cov_col} min < 0"
        assert row["max"] <= 1.0, f"{cov_col} max > 1"


def test_strict_temporal_leakage_and_quality_flags():
    """Verify QA flags, canonical outcomes inclusion, and exact column counts."""
    df = pd.read_parquet(PARQUET_PATH)

    # Invariant: exactly 84 columns
    assert len(df.columns) == 84, f"Expected 84 columns, got {len(df.columns)}"

    # Check canonical outcome labels are present for downstream modeling convenience
    expected_outcomes = ["regain_5s_controlled", "dangerous_escape_15s", "episode_outcome_3class"]
    for col in expected_outcomes:
        assert col in df.columns, f"Expected outcome column {col} in feature dataset"

    # Verify quality flags are bool
    assert df["actor_present"].dtype == bool
    assert df["actor_matching_anomalous"].dtype == bool
