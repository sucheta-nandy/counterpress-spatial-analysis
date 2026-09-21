"""Unit tests for feature engineering pipeline and temporal leakage enforcement."""

import math
import numpy as np
import pytest

from counterpress.features import (
    build_spatial_feature_row,
    compute_k_nearest_distances,
    compute_local_counts,
    extract_frame_players,
)


def test_actor_excluded_from_teammate_count():
    """The counterpressing actor must be strictly excluded from teammate-support calculations."""
    event_loc = (60.0, 40.0)
    freeze_frame = {
        "event_uuid": "ev1",
        "visible_area": [0.0, 0.0, 120.0, 0.0, 120.0, 80.0, 0.0, 80.0],
        "freeze_frame": [
            # Actor at initiation location
            {"teammate": True, "actor": True, "keeper": False, "location": [60.0, 40.0]},
            # Supporting teammate at distance 3.0
            {"teammate": True, "actor": False, "keeper": False, "location": [63.0, 40.0]},
            # Opponent at distance 4.0
            {"teammate": False, "actor": False, "keeper": False, "location": [60.0, 44.0]},
        ],
    }
    parsed = extract_frame_players(freeze_frame, event_loc)
    assert parsed["actor_present"] is True
    assert parsed["actor_distance_from_event"] == pytest.approx(0.0)
    assert parsed["actor_matching_anomalous"] is False

    # Actor is excluded from teammates_excluding_actor
    assert len(parsed["teammates_excluding_actor"]) == 1
    assert parsed["teammates_excluding_actor"][0] == (63.0, 40.0)
    assert len(parsed["teammates_including_actor"]) == 2

    # In row builder:
    episode = {
        "episode_id": "ep1",
        "initiation_event_id": "ev1",
        "initiation_location": [60.0, 40.0],
        "match_id": 12345,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
    }
    row = build_spatial_feature_row(episode, freeze_frame)

    # Actor must not be counted in visible_teammates_within_5
    assert row["visible_teammates_within_5"] == 1
    assert row["visible_opponents_within_5"] == 1
    assert row["numerical_advantage_5"] == 0  # 1 teammate - 1 opponent

    # Nearest teammate distance must measure OTHER teammate (3.0, not 0.0)
    assert row["nearest_teammate_distance"] == pytest.approx(3.0)


def test_teammate_at_exact_radius_included():
    """Teammate at exactly radius 5.0 is included."""
    center = (60.0, 40.0)
    # Point at exactly (60.0, 45.0) -> distance = 5.0
    pts = [(60.0, 45.0)]
    assert compute_local_counts(center, pts, radius=5.0) == 1


def test_player_outside_radius_excluded():
    """Player at distance > 5.0 is strictly excluded from radius 5."""
    center = (60.0, 40.0)
    pts = [(60.0, 45.05)]  # Distance = 5.05
    assert compute_local_counts(center, pts, radius=5.0) == 0
    assert compute_local_counts(center, pts, radius=10.0) == 1


def test_numerical_advantage_calculation():
    """Numerical advantage is teammates - opponents."""
    event_loc = (50.0, 40.0)
    freeze_frame = {
        "freeze_frame": [
            {"teammate": True, "actor": True, "location": [50.0, 40.0]},
            {"teammate": True, "actor": False, "location": [52.0, 40.0]},  # dist 2
            {"teammate": True, "actor": False, "location": [54.0, 40.0]},  # dist 4
            {"teammate": False, "actor": False, "location": [50.0, 43.0]}, # dist 3
        ],
        "visible_area": [0.0, 0.0, 120.0, 0.0, 120.0, 80.0, 0.0, 80.0],
    }
    episode = {"episode_id": "ep1", "initiation_location": [50.0, 40.0]}
    row = build_spatial_feature_row(episode, freeze_frame)

    assert row["visible_teammates_within_5"] == 2
    assert row["visible_opponents_within_5"] == 1
    assert row["numerical_advantage_5"] == 1  # 2 - 1 = +1
    assert row["total_players_within_5"] == 4  # 2 teammates + 1 opponent + 1 actor


def test_nearest_and_second_nearest_distances():
    """Distances are ordered and correct."""
    center = (0.0, 0.0)
    pts = [(0.0, 8.0), (3.0, 4.0), (0.0, 2.0)]  # dists: 8.0, 5.0, 2.0
    dists = compute_k_nearest_distances(center, pts, k=3)
    assert dists[0] == pytest.approx(2.0)
    assert dists[1] == pytest.approx(5.0)
    assert dists[2] == pytest.approx(8.0)


def test_insufficient_players_nan_not_zero():
    """When fewer than k players are visible, remaining distances must be NaN, never zero."""
    center = (0.0, 0.0)
    pts = [(0.0, 3.0)]  # Only 1 player
    dists = compute_k_nearest_distances(center, pts, k=3)
    assert dists[0] == pytest.approx(3.0)
    assert dists[1] is None
    assert dists[2] is None

    # Empty player list -> all None
    dists_empty = compute_k_nearest_distances(center, [], k=3)
    assert dists_empty == [None, None, None]


def test_actor_event_coordinate_alignment_qa():
    """QA fields correctly flag actor-event alignment."""
    # Case 1: Aligned actor (< 0.1)
    ev_loc = (45.0, 35.0)
    ff_aligned = {
        "freeze_frame": [{"teammate": True, "actor": True, "location": [45.0, 35.0]}],
    }
    meta_aligned = extract_frame_players(ff_aligned, ev_loc)
    assert meta_aligned["actor_present"] is True
    assert meta_aligned["actor_distance_from_event"] == pytest.approx(0.0)
    assert meta_aligned["actor_matching_anomalous"] is False

    # Case 2: Anomalous actor (distance > 1.0)
    ff_misaligned = {
        "freeze_frame": [{"teammate": True, "actor": True, "location": [55.0, 35.0]}],  # dist = 10.0
    }
    meta_misaligned = extract_frame_players(ff_misaligned, ev_loc)
    assert meta_misaligned["actor_present"] is True
    assert meta_misaligned["actor_distance_from_event"] == pytest.approx(10.0)
    assert meta_misaligned["actor_matching_anomalous"] is True

    # Case 3: Missing actor flag
    ff_no_actor = {
        "freeze_frame": [{"teammate": False, "actor": False, "location": [50.0, 35.0]}],
    }
    meta_no_actor = extract_frame_players(ff_no_actor, ev_loc)
    assert meta_no_actor["actor_present"] is False
    assert np.isnan(meta_no_actor["actor_distance_from_event"])
    assert meta_no_actor["actor_matching_anomalous"] is True


def test_opponent_ahead_classification():
    """Test classification of opponents and defenders ahead in transition direction."""
    # Initiation at x=80, y=40 in pressing team frame
    # In opponent attack frame: ball is at x_opp = 120 - 80 = 40, y_opp = 80 - 40 = 40
    episode = {"episode_id": "ep1", "initiation_location": [80.0, 40.0]}
    freeze_frame = {
        "visible_area": [0.0, 0.0, 120.0, 0.0, 120.0, 80.0, 0.0, 80.0],
        "freeze_frame": [
            # Actor at (80, 40)
            {"teammate": True, "actor": True, "location": [80.0, 40.0]},
            # Opponent at (70, 40) in pressing frame -> in opp frame: x_opp = 120 - 70 = 50 > 40 (AHEAD!)
            {"teammate": False, "actor": False, "location": [70.0, 40.0]},
            # Opponent at (90, 40) in pressing frame -> in opp frame: x_opp = 120 - 90 = 30 < 40 (BEHIND!)
            {"teammate": False, "actor": False, "location": [90.0, 40.0]},
            # Defender at (75, 40) in pressing frame -> in opp frame: x_opp = 120 - 75 = 45 > 40 (AHEAD!)
            {"teammate": True, "actor": False, "location": [75.0, 40.0]},
        ],
    }
    row = build_spatial_feature_row(episode, freeze_frame)
    assert row["opponents_ahead_of_ball"] == 1
    assert row["defenders_ahead_of_ball"] == 1
    assert row["forward_numerical_advantage"] == 0  # 1 - 1 = 0
    assert row["nearest_opponent_ahead_distance"] == pytest.approx(10.0)
    assert row["nearest_defender_ahead_distance"] == pytest.approx(5.0)


def test_forward_escape_corridor_inclusion_and_advantage():
    """Test forward escape corridor counts and advantage."""
    # Ball at center (60, 40) -> in opponent frame (60, 40)
    episode = {"episode_id": "ep1", "initiation_location": [60.0, 40.0]}
    freeze_frame = {
        "visible_area": [0.0, 0.0, 120.0, 0.0, 120.0, 80.0, 0.0, 80.0],
        "freeze_frame": [
            {"teammate": True, "actor": True, "location": [60.0, 40.0]},
            # Opponent at (50, 40) in pressing frame -> in opp frame: (70, 40) -> directly toward goal, dist 10 (IN CORRIDOR)
            {"teammate": False, "actor": False, "location": [50.0, 40.0]},
            # Opponent at (70, 40) in pressing frame -> in opp frame: (50, 40) -> behind ball (OUTSIDE)
            {"teammate": False, "actor": False, "location": [70.0, 40.0]},
            # Teammate at (60, 50) in pressing frame -> in opp frame: (60, 30) -> angle -90 deg (OUTSIDE)
            {"teammate": True, "actor": False, "location": [60.0, 50.0]},
        ],
    }
    row = build_spatial_feature_row(episode, freeze_frame)
    assert row["opponents_in_escape_corridor_20"] == 1
    assert row["defenders_in_escape_corridor_20"] == 0
    assert row["escape_corridor_advantage_20"] == 1  # 1 - 0 = +1
    assert row["nearest_opponent_in_escape_corridor"] == pytest.approx(10.0)
    assert np.isnan(row["nearest_defender_in_escape_corridor"])
    assert 0.0 <= row["escape_corridor_coverage_20"] <= 1.0


def test_temporal_leakage_rule():
    """Verify that feature engineering functions exclusively reference initiation state
    and never depend on post-initiation events or outcome labels.
    """
    # An episode dict containing deceptive outcome values must produce the exact same features
    # regardless of outcome values
    episode_clean = {
        "episode_id": "ep1",
        "initiation_event_id": "ev1",
        "initiation_location": [60.0, 40.0],
        "match_id": 100,
    }
    episode_with_outcomes = {
        **episode_clean,
        "regain_5s_controlled": 1,
        "dangerous_escape_15s": 1,
        "episode_outcome_3class": "dangerous_escape",
        "future_pass_count": 999,
    }
    freeze_frame = {
        "visible_area": [0.0, 0.0, 120.0, 0.0, 120.0, 80.0, 0.0, 80.0],
        "freeze_frame": [
            {"teammate": True, "actor": True, "location": [60.0, 40.0]},
            {"teammate": False, "actor": False, "location": [65.0, 40.0]},
        ],
    }
    row1 = build_spatial_feature_row(episode_clean, freeze_frame)
    row2 = build_spatial_feature_row(episode_with_outcomes, freeze_frame)

    # All spatial features must be identical
    feature_keys = [
        "visible_opponents_within_5",
        "visible_teammates_within_5",
        "numerical_advantage_5",
        "coverage_10",
        "forward_numerical_advantage",
        "escape_corridor_advantage_20",
    ]
    for k in feature_keys:
        assert row1[k] == row2[k]


def test_missing_freeze_frame_retains_row_with_nans():
    """When a freeze frame is missing, the row is retained with valid identifiers,
    pitch geometry features, and explicit missingness/quality flags.
    """
    episode = {
        "episode_id": "ep_missing",
        "initiation_event_id": "ev_miss",
        "initiation_location": [75.0, 25.0],
        "match_id": 999,
        "competition_name": "UEFA Euro",
        "season_name": "2024",
    }
    row = build_spatial_feature_row(episode, freeze_frame=None)

    # Identifiers retained
    assert row["episode_id"] == "ep_missing"
    assert row["match_id"] == 999
    assert row["initiation_x"] == 75.0
    assert row["initiation_y"] == 25.0

    # Pitch geometry computed
    assert row["distance_to_nearest_touchline"] == pytest.approx(25.0)
    assert row["pitch_zone"] == "middle_third"

    # 360 quality flags set
    assert row["actor_present"] is False
    assert np.isnan(row["actor_distance_from_event"])
    assert row["actor_matching_anomalous"] is True
    assert row["polygon_missing"] is True
    assert row["polygon_valid"] is False

    # Spatial features are NaN or 0 as appropriate
    assert row["visible_teammates_within_5"] == 0
    assert np.isnan(row["nearest_teammate_distance"])
    assert np.isnan(row["teammate_density_visible_5"])
    assert row["coverage_5"] == 0.0
