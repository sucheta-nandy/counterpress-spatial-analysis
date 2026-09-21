"""Unit tests for turnover detection and counterpress episode extraction."""

import pytest
from counterpress.turnovers import (
    extract_counterpress_episodes,
    is_open_play_transition,
    timestamp_to_seconds,
)


def test_timestamp_to_seconds():
    assert timestamp_to_seconds("00:00:00.000") == 0.0
    assert timestamp_to_seconds("00:01:30.500") == 90.5
    assert timestamp_to_seconds("01:15:10.250") == 4510.25
    assert timestamp_to_seconds("") == 0.0


def test_is_open_play_transition():
    assert is_open_play_transition("Regular Play") is True
    assert is_open_play_transition("From Counter") is True
    assert is_open_play_transition("From Keeper") is True
    assert is_open_play_transition("From Corner") is False
    assert is_open_play_transition("From Throw In") is False
    assert is_open_play_transition("From Free Kick") is False
    assert is_open_play_transition("From Goal Kick") is False


def test_multiple_counterpress_actions_collapse_into_one_episode():
    """Verify that multiple CP actions within the same possession collapse to 1 episode

    and the first chronological action is chosen as initiation.
    """
    events = [
        # Turnover occurs: Team A loses ball to Team B
        {
            "id": "e1",
            "index": 1,
            "period": 1,
            "timestamp": "00:01:00.000",
            "possession": 10,
            "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2},
            "type": {"name": "Pass"},
            "play_pattern": {"name": "Regular Play"},
            "location": [40.0, 30.0],
        },
        # First counterpress action by Team A
        {
            "id": "cp1",
            "index": 2,
            "period": 1,
            "timestamp": "00:01:01.500",
            "possession": 10,
            "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1},
            "player": {"name": "Player 1", "id": 101},
            "type": {"name": "Pressure"},
            "counterpress": True,
            "location": [45.0, 32.0],
        },
        # Second counterpress action by Team A in same possession
        {
            "id": "cp2",
            "index": 3,
            "period": 1,
            "timestamp": "00:01:03.000",
            "possession": 10,
            "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1},
            "player": {"name": "Player 2", "id": 102},
            "type": {"name": "Pressure"},
            "counterpress": True,
            "location": [48.0, 35.0],
        },
        # Third counterpress action by Team A in same possession
        {
            "id": "cp3",
            "index": 4,
            "period": 1,
            "timestamp": "00:01:04.200",
            "possession": 10,
            "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1},
            "player": {"name": "Player 3", "id": 103},
            "type": {"name": "Block"},
            "counterpress": True,
            "location": [50.0, 35.0],
        },
    ]

    episodes = extract_counterpress_episodes(events, {"match_id": 99999})

    # Must produce exactly ONE episode
    assert len(episodes) == 1
    ep = episodes[0]

    # Initiation event must be the FIRST chronological action (cp1)
    assert ep["initiation_event_id"] == "cp1"
    assert ep["initiation_event_type"] == "Pressure"
    assert ep["initiation_player_name"] == "Player 1"
    assert ep["num_counterpress_actions"] == 3
    assert ep["all_counterpress_event_ids"] == ["cp1", "cp2", "cp3"]
    assert ep["counterpressing_team"] == "Team A"
    assert ep["possession_team"] == "Team B"
    assert ep["is_open_play"] is True
    assert ep["delay_seconds"] == pytest.approx(1.5, abs=0.01)


def test_unique_episode_ids_and_missing_360_preservation():
    """Verify episode IDs are unique and missing 360 does not drop the episode."""
    events = [
        # Possession 1 with CP
        {
            "id": "e1", "index": 1, "period": 1, "timestamp": "00:02:00.000",
            "possession": 20, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "Regular Play"},
        },
        {
            "id": "cp_p20", "index": 2, "period": 1, "timestamp": "00:02:02.000",
            "possession": 20, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Pressure"},
            "counterpress": True, "location": [60.0, 40.0],
        },
        # Possession 2 with CP
        {
            "id": "e3", "index": 3, "period": 1, "timestamp": "00:05:00.000",
            "possession": 25, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "From Corner"},
        },
        {
            "id": "cp_p25", "index": 4, "period": 1, "timestamp": "00:05:03.000",
            "possession": 25, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Duel"},
            "counterpress": True, "location": [70.0, 30.0],
        },
    ]

    # Only cp_p20 has 360; cp_p25 does not
    usable_360 = {"cp_p20"}

    episodes = extract_counterpress_episodes(events, {"match_id": 12345}, usable_360_uuids=usable_360)

    assert len(episodes) == 2
    # Unique IDs
    ids = [e["episode_id"] for e in episodes]
    assert len(set(ids)) == len(ids)

    # 360 flags preserved correctly
    assert episodes[0]["has_initiation_360"] is True
    assert episodes[1]["has_initiation_360"] is False

    # Play patterns flagged
    assert episodes[0]["is_open_play"] is True
    assert episodes[1]["is_open_play"] is False


def test_latency_over_5s_marked_invalid():
    """Verify that an episode with delay > 5.0s is flagged latency_valid=False and link_quality='invalid'."""
    events = [
        # Opponent started possession 10 seconds ago
        {
            "id": "e_old", "index": 1, "period": 1, "timestamp": "00:01:00.000",
            "possession": 30, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "Regular Play"},
        },
        {
            "id": "e_mid", "index": 2, "period": 1, "timestamp": "00:01:03.000",
            "possession": 30, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "Regular Play"},
        },
        # CP occurs 9 seconds after first pass, and 6.5s after second pass
        {
            "id": "cp_delayed", "index": 3, "period": 1, "timestamp": "00:01:09.500",
            "possession": 30, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Pressure"},
            "counterpress": True, "location": [50.0, 30.0],
        },
    ]
    episodes = extract_counterpress_episodes(events, {"match_id": 88888})
    assert len(episodes) == 1
    ep = episodes[0]
    assert ep["delay_seconds"] > 5.0
    assert ep["latency_valid"] is False
    assert ep["turnover_link_quality"] in {"invalid", "ambiguous"}


def test_open_play_after_restart_possession():
    """Verify that a possession starting from a throw-in but completing multiple passes

    over >5 seconds is retained as open_play turnover context.
    """
    events = [
        # Throw in restart at 00:01:00.000
        {
            "id": "ti", "index": 1, "period": 1, "timestamp": "00:01:00.000",
            "possession": 40, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "From Throw In"},
        },
        # Pass 1 completed at 00:01:03.000
        {
            "id": "p1", "index": 2, "period": 1, "timestamp": "00:01:03.000",
            "possession": 40, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "From Throw In"},
        },
        # Pass 2 completed at 00:01:07.000
        {
            "id": "p2", "index": 3, "period": 1, "timestamp": "00:01:07.000",
            "possession": 40, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "From Throw In"},
        },
        # Turnover occurs at 00:01:10.000 (10s after throw-in)
        {
            "id": "to", "index": 4, "period": 1, "timestamp": "00:01:10.000",
            "possession": 40, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Dispossessed"},
            "play_pattern": {"name": "From Throw In"},
        },
        # Counterpress initiated at 00:01:11.500 (delay = 1.5s)
        {
            "id": "cp_open", "index": 5, "period": 1, "timestamp": "00:01:11.500",
            "possession": 40, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Pressure"},
            "counterpress": True, "location": [60.0, 40.0],
        },
    ]
    episodes = extract_counterpress_episodes(events, {"match_id": 77777})
    assert len(episodes) == 1
    ep = episodes[0]
    assert ep["possession_origin_pattern"] == "From Throw In"
    assert ep["turnover_context"] == "open_play"
    assert ep["is_open_play"] is True
    assert ep["latency_valid"] is True
    assert ep["turnover_link_quality"] == "high"


def test_immediate_set_piece_turnover_classified():
    """Verify that a corner cleared on first delivery is classified as immediate_restart_phase."""
    events = [
        # Corner kick at 00:02:00.000
        {
            "id": "corner", "index": 1, "period": 1, "timestamp": "00:02:00.000",
            "possession": 50, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team B", "id": 2}, "type": {"name": "Pass"},
            "play_pattern": {"name": "From Corner"},
        },
        # Defending team heads it away at 00:02:01.000 (turnover on delivery)
        {
            "id": "clearance", "index": 2, "period": 1, "timestamp": "00:02:01.000",
            "possession": 50, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Clearance"},
            "play_pattern": {"name": "From Corner"},
        },
        # Counterpress action at 00:02:02.000
        {
            "id": "cp_corner", "index": 3, "period": 1, "timestamp": "00:02:02.000",
            "possession": 50, "possession_team": {"name": "Team B", "id": 2},
            "team": {"name": "Team A", "id": 1}, "type": {"name": "Pressure"},
            "counterpress": True, "location": [95.0, 40.0],
        },
    ]
    episodes = extract_counterpress_episodes(events, {"match_id": 66666})
    assert len(episodes) == 1
    ep = episodes[0]
    assert ep["possession_origin_pattern"] == "From Corner"
    assert ep["turnover_context"] == "immediate_restart_phase"
    assert ep["is_open_play"] is False
