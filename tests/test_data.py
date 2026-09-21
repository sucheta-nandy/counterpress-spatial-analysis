"""Tests for data download, loading, schema validation, and 360 alignment."""

import pytest
from counterpress.config import PITCH_LENGTH, PITCH_WIDTH
from counterpress.data import StatsBombDownloader, load_competitions


def test_competitions_schema():
    """Verify that competitions load and contain required fields."""
    comps = load_competitions()
    assert not comps.empty
    expected_cols = {"competition_id", "season_id", "competition_name", "season_name"}
    assert expected_cols.issubset(comps.columns)

    # Check that 360 availability flags exist
    has_360 = comps[comps["match_available_360"].notna()]
    assert len(has_360) > 0


def test_pitch_boundary_invariants():
    """Verify coordinate system bounds."""
    assert PITCH_LENGTH == 120.0
    assert PITCH_WIDTH == 80.0
