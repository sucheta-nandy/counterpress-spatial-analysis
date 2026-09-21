"""Unit tests for outcome labeling logic (controlled regain, dangerous escape, 3-class)."""

import pytest
from counterpress.outcomes import compute_episode_outcomes


def test_regain_within_exact_5_seconds():
    """Regain at exactly 5.0s is positive for regain_5s; regain at 5.1s is negative."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }

    # Case 1: Regain at exactly 65.0s (dt = 5.0s) with controlled pass by Team A
    events_at_5s = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "e_regain", "period": 1, "timestamp": "00:01:05.000", "possession": 11, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out_5s = compute_episode_outcomes(episode, events_at_5s)
    assert out_5s["regain_5s_controlled"] == 1
    assert out_5s["regain_5s"] == 1
    assert out_5s["seconds_to_regain"] == pytest.approx(5.0)
    assert out_5s["episode_outcome_3class"] == "successful_regain"

    # Case 2: Regain at 65.1s (dt = 5.1s) -> regain_5s must be 0, but regain_8s must be 1
    events_at_5_1s = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "e_regain", "period": 1, "timestamp": "00:01:05.100", "possession": 11, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out_5_1s = compute_episode_outcomes(episode, events_at_5_1s)
    assert out_5_1s["regain_5s_controlled"] == 0
    assert out_5_1s["regain_5s"] == 0
    assert out_5_1s["regain_8s_controlled"] == 1
    assert out_5_1s["seconds_to_regain"] == pytest.approx(5.1)
    assert out_5_1s["episode_outcome_3class"] == "harmless_escape"


def test_defensive_action_does_not_equal_regain():
    """A defensive action (Pressure/Tackle/Foul) by pressing team while opponent retains
    possession MUST NOT be counted as established possession regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        # Team A performs a Pressure at 62.0s, but Team B remains possession_team
        {"id": "cp2", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        # Team A commits a Foul at 63.5s, but Team B remains possession_team
        {"id": "foul", "period": 1, "timestamp": "00:01:03.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Foul Committed"}},
        # Team B plays a pass at 64.0s
        {"id": "pass", "period": 1, "timestamp": "00:01:04.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["regain_5s"] == 0
    assert out["seconds_to_regain"] is None
    assert out["episode_outcome_3class"] == "harmless_escape"


def test_possession_team_changes_but_opponent_continues_play_no_regain():
    """If StatsBomb's possession_team changes to pressing team, but opponent continues
    passing/carrying with no pressing team controlled action, it must NOT count as regain.
    (Case 9 scenario).
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        # StatsBomb annotates possession_team as Team A, but event is played by Team B!
        {"id": "opp_pass", "period": 1, "timestamp": "00:01:01.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
        {"id": "opp_carry", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team B"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_possession_annotation"] == 1  # Old flawed variable triggered
    assert out["regain_5s_controlled"] == 0              # New robust variable correctly rejects!
    assert out["episode_outcome_3class"] == "harmless_escape"


def test_block_alone_no_regain():
    """A Block by pressing team alone must not count as a regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "blk", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Block"}},
        {"id": "opp_rec", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Ball Receipt*"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0


def test_pressure_alone_no_regain():
    """Pressure alone without ball control does not equal regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "press2", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0


def test_duel_followed_by_pressing_carry_regain():
    """Duel followed by pressing team Carry counts as a controlled regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "duel", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Duel"}},
        {"id": "carry", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_evidence"] == "duel_plus_carry"
    assert out["seconds_to_regain"] == pytest.approx(2.0)


def test_interception_followed_by_opponent_control_no_regain():
    """Interception that immediately deflects to opponent control does not count."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "intc", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Interception"}},
        # Opponent controls immediately
        {"id": "opp_pass", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0


def test_interception_followed_by_pressing_carry_pass_regain():
    """Interception followed by pressing team Carry/Pass counts as controlled regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "intc", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Interception"}},
        {"id": "pass", "period": 1, "timestamp": "00:01:03.000", "possession": 11, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_evidence"] in {"interception_plus_pass", "interception_plus_control"}


def test_opponent_miscontrol_followed_by_recovery_carry_regain():
    """Opponent Miscontrol followed by pressing team Ball Recovery + Carry is a valid regain.
    (Case 18 scenario).
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "misc", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Miscontrol"}},
        # Note: StatsBomb possession_team may still say Team B!
        {"id": "rec", "period": 1, "timestamp": "00:01:03.800", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Ball Recovery"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:03.800", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_evidence"] == "ball_recovery_plus_carry"
    assert out["seconds_to_regain"] == pytest.approx(3.8)


def test_completed_pass_in_new_possession_regain():
    """Completed pass in new possession ID constitutes a controlled regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "pass", "period": 1, "timestamp": "00:01:03.000", "possession": 11, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_evidence"] == "new_possession_completed_pass"


def test_opponent_shot_within_and_after_window():
    """Opponent shot within 15.0s is dangerous; shot after 15.0s is not dangerous."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }

    # Shot at 72.0s (dt = 12.0s <= 15.0s) -> dangerous escape
    events_shot_12s = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "shot", "period": 1, "timestamp": "00:01:12.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Shot"}, "location": [105.0, 40.0]},
    ]
    out_12s = compute_episode_outcomes(episode, events_shot_12s)
    assert out_12s["dangerous_escape_15s"] == 1
    assert out_12s["shot_15s"] == 1
    assert out_12s["time_to_shot"] == pytest.approx(12.0)
    assert out_12s["episode_outcome_3class"] == "dangerous_escape"

    # Shot at 76.0s (dt = 16.0s > 15.0s) -> window expired, harmless
    events_shot_16s = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "shot", "period": 1, "timestamp": "00:01:16.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Shot"}, "location": [105.0, 40.0]},
    ]
    out_16s = compute_episode_outcomes(episode, events_shot_16s)
    assert out_16s["dangerous_escape_15s"] == 0
    assert out_16s["shot_15s"] == 0
    assert out_16s["episode_outcome_3class"] == "harmless_escape"


def test_final_third_entry_and_already_in_final_third():
    """Final third entry is detected if opponent enters x >= 80.0, but NOT if opponent
    already started in the attacking final third.
    """
    episode_mid = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events_entry = [
        {"id": "turnover", "period": 1, "timestamp": "00:00:58.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}, "location": [60.0, 40.0]},
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "advance", "period": 1, "timestamp": "00:01:08.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Carry"}, "location": [85.0, 30.0]},
    ]
    out_entry = compute_episode_outcomes(episode_mid, events_entry)
    assert out_entry["started_in_final_third"] is False
    assert out_entry["final_third_entry_15s"] == 1
    assert out_entry["dangerous_escape_15s"] == 1
    assert out_entry["time_to_final_third_entry"] == pytest.approx(8.0)

    # Case 2: Already started in final third (x = 88.0)
    events_already_in = [
        {"id": "turnover", "period": 1, "timestamp": "00:00:58.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}, "location": [88.0, 40.0]},
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "pass2", "period": 1, "timestamp": "00:01:08.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}, "location": [92.0, 30.0]},
    ]
    out_already = compute_episode_outcomes(episode_mid, events_already_in)
    assert out_already["started_in_final_third"] is True
    assert out_already["final_third_entry_15s"] == 0
    assert out_already["dangerous_escape_15s"] == 0
    assert out_already["episode_outcome_3class"] == "harmless_escape"


def test_period_boundary_handling():
    """Events in the subsequent period must not be evaluated."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 2700.0,  # 45th minute
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 50,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:45:00.000", "possession": 50, "possession_team": {"name": "Team B"}},
        {"id": "p2_kickoff", "period": 2, "timestamp": "00:00:02.000", "possession": 51, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["regain_5s"] == 0
    assert out["seconds_to_regain"] is None
    assert out["episode_outcome_3class"] == "harmless_escape"


def test_dangerous_event_before_regain_gets_dangerous_outcome():
    """Verify that when a dangerous event (shot/entry) occurs BEFORE a 5s regain,
    danger takes priority and episode_outcome_3class is 'dangerous_escape'.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 60,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 60, "possession_team": {"name": "Team B"}},
        # Opponent takes a Shot at 62.0s (dt = 2.0s)
        {"id": "shot", "period": 1, "timestamp": "00:01:02.000", "possession": 60, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Shot"}, "location": [108.0, 40.0]},
        # Pressing team regains possession at 64.0s (dt = 4.0s <= 5.0s)
        {"id": "regain", "period": 1, "timestamp": "00:01:04.000", "possession": 61, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["dangerous_escape_15s"] == 1
    assert out["shot_15s"] == 1
    assert out["regain_5s_controlled"] == 1
    assert out["seconds_to_regain"] == pytest.approx(4.0)
    assert out["episode_outcome_3class"] == "dangerous_escape"


def test_regain_before_dangerous_event_not_dangerous():
    """Verify that events occurring AFTER established regain do not create dangerous escape."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 70,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 70, "possession_team": {"name": "Team B"}},
        # Pressing team regains possession at 62.5s (dt = 2.5s)
        {"id": "regain", "period": 1, "timestamp": "00:01:02.500", "possession": 71, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
        # Team B later shoots at 68.0s (dt = 8.0s) in a new sequence
        {"id": "late_shot", "period": 1, "timestamp": "00:01:08.000", "possession": 72, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Shot"}, "location": [105.0, 40.0]},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["dangerous_escape_15s"] == 0
    assert out["episode_outcome_3class"] == "successful_regain"


def test_simultaneous_shot_and_regain_edge_case():
    """Verify that simultaneous timestamp between dangerous entry and regain prioritizes danger."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 80,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 80, "possession_team": {"name": "Team B"}},
        # Team B carries into attacking final third at 63.0s
        {"id": "entry", "period": 1, "timestamp": "00:01:03.000", "possession": 80, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Carry"}, "location": [85.0, 40.0]},
        # At exact same second 63.0s, Team A tackles and establishes possession
        {"id": "regain", "period": 1, "timestamp": "00:01:03.000", "possession": 81, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["dangerous_escape_15s"] == 1
    assert out["final_third_entry_15s"] == 1
    assert out["regain_5s_controlled"] == 1
    assert out["episode_outcome_3class"] == "dangerous_escape"


# ==============================================================================
# ITERATION 2.7 SPECIFIC UNIT TESTS (TRANSITION VERIFICATION & CONTROL TIMING)
# ==============================================================================


def test_pressing_carry_without_transition_no_regain():
    """Test 1: Pressing-team Carry within opponent possession sequence without
    intervening turnover or acquisition must NOT count as a regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "c1", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
        {"id": "p1", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["controlled_regain_time"] is None
    assert out["episode_outcome_3class"] == "harmless_escape"


def test_pressing_pass_without_transition_no_regain():
    """Test 2: Pressing-team Pass within opponent possession sequence without
    intervening turnover or acquisition must NOT count as a regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "p_press", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
        {"id": "p_opp", "period": 1, "timestamp": "00:01:03.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["controlled_regain_time"] is None


def test_controlled_ball_receipt_without_transition_no_regain():
    """Test 3: Pressing-team Ball Receipt within opponent possession sequence
    without transition must NOT count as a regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "rec_press", "period": 1, "timestamp": "00:01:01.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Ball Receipt*"}},
        {"id": "p_opp", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["controlled_regain_time"] is None


def test_opponent_miscontrol_recovery_carry_all_under_5s_regain():
    """Test 4: Opponent Miscontrol -> Ball Recovery -> Carry all <= 5s is a confirmed regain."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "misc", "period": 1, "timestamp": "00:01:01.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Miscontrol"}},
        {"id": "rec", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Ball Recovery"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_acquisition_time"] == pytest.approx(2.5)
    assert out["controlled_control_time"] == pytest.approx(3.0)
    assert out["controlled_regain_time"] == pytest.approx(3.0)
    assert out["controlled_regain_evidence"] == "ball_recovery_plus_carry"
    assert out["episode_outcome_3class"] == "successful_regain"


def test_ball_recovery_4_8s_carry_5_2s_no_5s_regain():
    """Test 5: Ball Recovery at 4.8s followed by confirming Carry at 5.2s:
    Confirming control occurs at 5.2s > 5.0s, so regain_5s_controlled MUST BE 0,
    while regain_8s_controlled is 1. (Conservative definition requirement).
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "rec", "period": 1, "timestamp": "00:01:04.800", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Ball Recovery"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:05.200", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["regain_8s_controlled"] == 1
    assert out["controlled_acquisition_time"] == pytest.approx(4.8)
    assert out["controlled_control_time"] == pytest.approx(5.2)
    assert out["controlled_regain_time"] == pytest.approx(5.2)
    assert out["regain_5s_controlled_v26"] == 1  # Note: v2.6 would have marked this positive at acq time!
    assert out["episode_outcome_3class"] == "harmless_escape"


def test_ball_recovery_4_8s_carry_exact_5s_regain():
    """Test 6: Ball Recovery at 4.8s followed by confirming Carry at exactly 5.0s:
    Confirming control occurs at exactly 5.000s <= 5.000s, so regain_5s_controlled is 1.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "rec", "period": 1, "timestamp": "00:01:04.800", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Ball Recovery"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:05.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_acquisition_time"] == pytest.approx(4.8)
    assert out["controlled_control_time"] == pytest.approx(5.0)
    assert out["controlled_regain_time"] == pytest.approx(5.0)
    assert out["episode_outcome_3class"] == "successful_regain"


def test_duel_followed_by_opponent_carry_no_regain():
    """Test 7: Pressing team Duel at 2.0s followed by opponent Carry:
    Opponent retains/regains control, so pressing team did NOT establish possession.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "duel", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Duel"}},
        {"id": "opp_cry", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["controlled_regain_time"] is None


def test_interception_at_3s_pressing_carry_3_5s_regain():
    """Test 8: Pressing team Interception at 3.0s followed by pressing Carry at 3.5s:
    Confirms controlled regain at 3.5s.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "intc", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Interception"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:03.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_acquisition_time"] == pytest.approx(3.0)
    assert out["controlled_control_time"] == pytest.approx(3.5)
    assert out["controlled_regain_time"] == pytest.approx(3.5)
    assert out["controlled_regain_evidence"] == "interception_plus_carry"


def test_same_timestamp_acquisition_and_carry_regain():
    """Test 9: Same-timestamp acquisition (Duel) and Carry by pressing team."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "duel", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Duel"}},
        {"id": "cry", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_acquisition_time"] == pytest.approx(2.0)
    assert out["controlled_control_time"] == pytest.approx(2.0)
    assert out["controlled_regain_time"] == pytest.approx(2.0)
    assert out["controlled_regain_evidence"] == "duel_plus_carry"


def test_block_followed_by_opponent_pass_no_regain():
    """Test 10: Block by pressing team followed by opponent Pass:
    Block is defensive deflection, not possession acquisition. No regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}},
        {"id": "blk", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Block"}},
        {"id": "p_opp", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 0
    assert out["controlled_regain_time"] is None


def test_possession_team_equals_counterpressing_team_regain():
    """Test 11: When episode possession_team == counterpressing_team (due to origin tagging),
    the algorithm correctly recognizes Team B as the opponent, detects Team B's incomplete pass,
    and detects Team A's controlled pass as a regain.
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team A",  # Same-team tagging from possession origin
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        {"id": "opp_inc_pass", "period": 1, "timestamp": "00:01:01.500", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}, "pass": {"outcome": {"name": "Incomplete"}}},
        {"id": "press_pass", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_time"] == pytest.approx(3.0)
    assert out["controlled_regain_evidence"] == "opponent_turnover_plus_pass"
    assert out["dangerous_escape_15s"] == 0


def test_pressing_team_shot_not_counted_as_opponent_danger():
    """Test 12: When possession_team == counterpressing_team, Team A attacking into
    the final third and taking a shot MUST NOT trigger dangerous_escape_15s!
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team A",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        # Opponent Team B is present in match
        {"id": "opp_touch", "period": 1, "timestamp": "00:01:00.500", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team B"}, "type": {"name": "Miscontrol"}},
        # Team A penetrates and shoots
        {"id": "press_carry", "period": 1, "timestamp": "00:01:02.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}, "location": [85.0, 40.0]},
        {"id": "press_shot", "period": 1, "timestamp": "00:01:04.000", "possession": 10, "possession_team": {"name": "Team A"}, "team": {"name": "Team A"}, "type": {"name": "Shot"}, "location": [105.0, 40.0]},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["dangerous_escape_15s"] == 0
    assert out["shot_15s"] == 0
    assert out["final_third_entry_15s"] == 0
    assert out["episode_outcome_3class"] == "successful_regain"


def test_opponent_failed_dribble_followed_by_pass():
    """Test 13: Opponent failed Dribble (Incomplete) followed by pressing-team completed pass."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        {"id": "opp_drib", "period": 1, "timestamp": "00:01:01.200", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Dribble"}, "dribble": {"outcome": {"name": "Incomplete"}}},
        {"id": "press_pass", "period": 1, "timestamp": "00:01:02.800", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pass"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_time"] == pytest.approx(2.8)
    assert out["controlled_regain_evidence"] == "opponent_turnover_plus_pass"


def test_opponent_clearance_followed_by_carry():
    """Test 14: Opponent Clearance followed by pressing-team Carry."""
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        {"id": "opp_clr", "period": 1, "timestamp": "00:01:01.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Clearance"}},
        {"id": "press_cry", "period": 1, "timestamp": "00:01:02.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_time"] == pytest.approx(2.5)
    assert out["controlled_regain_evidence"] == "opponent_clearance_plus_carry"


def test_opponent_incomplete_receipt_does_not_clear_pending_turnover():
    """Test 15: Opponent incomplete pass -> opponent intended recipient incomplete Ball Receipt* ->
    pressing-team Carry within 5s correctly establishes regain!
    """
    episode = {
        "initiation_event_id": "cp1",
        "initiation_seconds": 60.0,
        "period": 1,
        "counterpressing_team": "Team A",
        "possession_team": "Team B",
        "possession_id": 10,
    }
    events = [
        {"id": "cp1", "period": 1, "timestamp": "00:01:00.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Pressure"}},
        {"id": "opp_pass", "period": 1, "timestamp": "00:01:01.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Pass"}, "pass": {"outcome": {"name": "Incomplete"}}},
        {"id": "opp_rec", "period": 1, "timestamp": "00:01:01.500", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team B"}, "type": {"name": "Ball Receipt*"}, "ball_receipt": {"outcome": {"name": "Incomplete"}}},
        {"id": "press_cry", "period": 1, "timestamp": "00:01:03.000", "possession": 10, "possession_team": {"name": "Team B"}, "team": {"name": "Team A"}, "type": {"name": "Carry"}},
    ]
    out = compute_episode_outcomes(episode, events)
    assert out["regain_5s_controlled"] == 1
    assert out["controlled_regain_time"] == pytest.approx(3.0)
    assert out["controlled_regain_evidence"] == "opponent_turnover_plus_carry"


