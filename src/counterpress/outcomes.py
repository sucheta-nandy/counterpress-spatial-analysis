"""Outcome labeling engine for counterpress episodes.

Operational Targets:
1. Possession Regain (Outcome 1):
   - Primary: regain_5s_controlled (counterpressing team established controlled possession
     within 5.0s of counterpress initiation). Requires BOTH possession-transition evidence
     and on-ball controlled possession evidence.
   - Sensitivity: regain_3s_controlled, regain_8s_controlled.
   - Auditing: regain_5s_possession_annotation (StatsBomb possession_team annotation).

2. Opponent Transition Risk (Outcome 2):
   - Primary: dangerous_escape_15s (within 15.0s and before any controlled regain, opponent takes
     a shot or enters attacking final third x >= 80.0, provided episode did not initiate in that third).
   - Supporting: shot_15s, final_third_entry_15s, opponent_max_progression_15s, time_to_shot,
     time_to_final_third_entry.

3. Three-State Tactical Outcome:
   - Priority: dangerous_escape > successful_regain > harmless_escape
   - successful_regain: regain_5s_controlled == 1 and dangerous_escape_15s == 0
   - harmless_escape: regain_5s_controlled == 0 and dangerous_escape_15s == 0
   - dangerous_escape: dangerous_escape_15s == 1
"""

import logging
from typing import Any, Dict, List, Optional, Tuple

from counterpress.config import FINAL_THIRD_X, REGAIN_WINDOW_SECONDS, TRANSITION_WINDOW_SECONDS
from counterpress.turnovers import timestamp_to_seconds

logger = logging.getLogger(__name__)


def detect_controlled_regain_v26(
    events: List[Dict[str, Any]],
    init_idx: int,
    init_sec: float,
    init_period: int,
    press_team: str,
    poss_id: int,
    opp_team: str,
) -> Tuple[Optional[float], Optional[str], Optional[str], Optional[str]]:
    """Legacy v2.6 detection logic preserved for longitudinal auditing."""
    controlled_regain_time: Optional[float] = None
    controlled_regain_id: Optional[str] = None
    controlled_regain_type: Optional[str] = None
    controlled_regain_evidence: Optional[str] = None

    for j in range(init_idx + 1, len(events)):
        sub_e = events[j]
        if sub_e.get("period") != init_period:
            break

        sub_sec = timestamp_to_seconds(sub_e.get("timestamp", "00:00:00.000"))
        dt = sub_sec - init_sec

        if dt > TRANSITION_WINDOW_SECONDS:
            break
        if dt < 0:
            continue

        team_name = sub_e.get("team", {}).get("name")
        if team_name != press_team:
            continue

        ev_type = sub_e.get("type", {}).get("name")

        if ev_type in {
            "Pressure",
            "Block",
            "Foul Committed",
            "Bad Behaviour",
            "Injury Stoppage",
            "Clearance",
            "Shield",
            "Error",
        }:
            continue

        if ev_type in {"Ball Recovery", "Interception", "Duel", "50/50"}:
            has_subsequent_control = False
            control_action_name = None

            for k in range(j + 1, min(len(events), j + 12)):
                next_e = events[k]
                if next_e.get("period") != init_period:
                    break
                next_team = next_e.get("team", {}).get("name")
                if next_team != press_team:
                    next_opp_type = next_e.get("type", {}).get("name")
                    if next_opp_type in {"Pass", "Carry", "Ball Receipt*", "Shot", "Dribble"}:
                        break
                    continue

                next_type = next_e.get("type", {}).get("name")
                if next_type in {"Carry", "Pass", "Dribble", "Shot"}:
                    has_subsequent_control = True
                    control_action_name = next_type.lower()
                    break

            if has_subsequent_control:
                controlled_regain_time = dt
                controlled_regain_id = sub_e.get("id")
                controlled_regain_type = ev_type
                if ev_type == "Ball Recovery":
                    controlled_regain_evidence = f"ball_recovery_plus_{control_action_name}"
                elif ev_type == "Interception":
                    controlled_regain_evidence = "interception_plus_control"
                elif ev_type in {"Duel", "50/50"}:
                    controlled_regain_evidence = f"duel_plus_{control_action_name}"
                break
            else:
                continue

        if ev_type == "Carry":
            controlled_regain_time = dt
            controlled_regain_id = sub_e.get("id")
            controlled_regain_type = ev_type
            if sub_e.get("possession") != poss_id:
                controlled_regain_evidence = "new_possession_carry"
            else:
                controlled_regain_evidence = "carry_control"
            break

        if ev_type == "Pass":
            pass_outcome = sub_e.get("pass", {}).get("outcome", {}).get("name")
            if pass_outcome is None:
                controlled_regain_time = dt
                controlled_regain_id = sub_e.get("id")
                controlled_regain_type = ev_type
                if sub_e.get("possession") != poss_id:
                    controlled_regain_evidence = "new_possession_completed_pass"
                else:
                    controlled_regain_evidence = "completed_pass"
                break
            else:
                continue

        if ev_type == "Ball Receipt*":
            rec_outcome = sub_e.get("ball_receipt", {}).get("outcome", {}).get("name")
            if rec_outcome != "Incomplete":
                controlled_regain_time = dt
                controlled_regain_id = sub_e.get("id")
                controlled_regain_type = ev_type
                controlled_regain_evidence = "controlled_ball_receipt"
                break

        if ev_type == "Goal Keeper":
            gk_type = sub_e.get("goalkeeper", {}).get("type", {}).get("name")
            if gk_type in {"Collected", "Keeper Sweeper", "Claim", "Shot Saved"}:
                controlled_regain_time = dt
                controlled_regain_id = sub_e.get("id")
                controlled_regain_type = ev_type
                controlled_regain_evidence = "goalkeeper_control"
                break

        if ev_type in {"Dribble", "Shot"}:
            controlled_regain_time = dt
            controlled_regain_id = sub_e.get("id")
            controlled_regain_type = ev_type
            controlled_regain_evidence = f"{ev_type.lower()}_control"
            break

    return controlled_regain_time, controlled_regain_id, controlled_regain_type, controlled_regain_evidence


def detect_controlled_regain(
    events: List[Dict[str, Any]],
    init_idx: int,
    init_sec: float,
    init_period: int,
    press_team: str,
    poss_id: int,
    opp_team: str,
) -> Tuple[Optional[float], Optional[float], Optional[str], Optional[str], Optional[str]]:
    """Detect established controlled possession regain by the counterpressing team (v2.7).

    Requires BOTH:
    A. Possession-transition evidence:
       - Defensive acquisition by pressing team (Ball Recovery, Interception, won Duel/50-50, Keeper collection).
       - Opponent turnover/loss (Dispossessed, Miscontrol, Incomplete Pass).
       - StatsBomb possession state change to counterpressing team confirmed by subsequent controlled action.
    B. Controlled-possession evidence by pressing team:
       - Carry, completed Pass, controlled Ball Receipt*, Dribble, Shot.

    Confirming control must occur within 0.000 <= t <= TRANSITION_WINDOW_SECONDS of counterpress initiation.
    The confirming control time is returned as ctrl_time.

    Parameters
    ----------
    events : list of dict
        Ordered match event log.
    init_idx : int
        Index of the counterpress initiation event.
    init_sec : float
        Initiation timestamp in seconds.
    init_period : int
        Match period (1, 2, etc.).
    press_team : str
        Name of the counterpressing squad.
    poss_id : int
        Possession ID at initiation.
    opp_team : str
        Opponent squad possessing the ball at initiation.

    Returns
    -------
    tuple
        (acq_time, ctrl_time, ctrl_id, ctrl_type, evidence_string)
    """
    pending_acq: Optional[Dict[str, Any]] = None

    for j in range(init_idx, len(events)):
        sub_e = events[j]
        if sub_e.get("period") != init_period:
            break

        sub_sec = timestamp_to_seconds(sub_e.get("timestamp", "00:00:00.000"))
        dt = sub_sec - init_sec

        if dt > TRANSITION_WINDOW_SECONDS:
            break
        if dt < 0:
            continue

        team_name = sub_e.get("team", {}).get("name")
        ev_type = sub_e.get("type", {}).get("name")
        sub_poss = sub_e.get("possession")
        sub_poss_team = sub_e.get("possession_team", {}).get("name")

        # 1. Check for opponent actions
        if team_name == opp_team:
            # Opponent turnover / dispossession / failed action: establishes transition evidence
            if ev_type in {"Miscontrol", "Dispossessed"}:
                pending_acq = {
                    "acq_time": dt,
                    "acq_id": sub_e.get("id"),
                    "acq_type": ev_type,
                    "pathway": "opponent_turnover",
                }
            elif ev_type == "Pass" and sub_e.get("pass", {}).get("outcome", {}).get("name") in {
                "Incomplete", "Pass Offside", "Out"
            }:
                pending_acq = {
                    "acq_time": dt,
                    "acq_id": sub_e.get("id"),
                    "acq_type": ev_type,
                    "pathway": "opponent_turnover",
                }
            elif ev_type == "Dribble" and sub_e.get("dribble", {}).get("outcome", {}).get("name") == "Incomplete":
                pending_acq = {
                    "acq_time": dt,
                    "acq_id": sub_e.get("id"),
                    "acq_type": ev_type,
                    "pathway": "opponent_turnover",
                }
            elif ev_type == "Clearance":
                pending_acq = {
                    "acq_time": dt,
                    "acq_id": sub_e.get("id"),
                    "acq_type": ev_type,
                    "pathway": "opponent_clearance",
                }
            elif ev_type == "Ball Receipt*":
                rec_outcome = sub_e.get("ball_receipt", {}).get("outcome", {}).get("name")
                if rec_outcome != "Incomplete":
                    # Opponent successfully received the ball -> reset pending acquisition
                    pending_acq = None
            elif ev_type in {"Pass", "Carry", "Shot", "Dribble", "Ball Recovery", "Interception"}:
                # Opponent executed on-ball controlled play; if we had a pending acquisition not confirmed, opponent retained
                pending_acq = None
            continue

        # 2. Check for pressing team actions
        if team_name == press_team:
            # Defensive non-possession actions that break possession or do not establish control
            if ev_type in {"Clearance", "Foul Committed", "Error"}:
                pending_acq = None
                continue

            if ev_type in {
                "Pressure",
                "Block",
                "Bad Behaviour",
                "Injury Stoppage",
                "Shield",
            }:
                continue

            # Defensive ball acquisitions by pressing team
            if ev_type in {"Ball Recovery", "Interception", "Duel", "50/50"}:
                pending_acq = {
                    "acq_time": dt,
                    "acq_id": sub_e.get("id"),
                    "acq_type": ev_type,
                    "pathway": ev_type.lower().replace(" ", "_").replace("/", "_"),
                }
                # Initiation event or acquisition event itself is not confirming control
                continue

            if ev_type == "Goal Keeper":
                gk_type = sub_e.get("goalkeeper", {}).get("type", {}).get("name")
                if gk_type in {"Collected", "Keeper Sweeper", "Claim", "Shot Saved"}:
                    pending_acq = {
                        "acq_time": dt,
                        "acq_id": sub_e.get("id"),
                        "acq_type": ev_type,
                        "pathway": "goalkeeper",
                    }
                continue

            # Initiation event itself at init_idx cannot be confirming control
            if j == init_idx:
                continue

            # Check for confirming control actions
            is_confirming_control = False
            ctrl_name = None

            if ev_type == "Carry":
                is_confirming_control = True
                ctrl_name = "carry"
            elif ev_type == "Pass":
                pass_outcome = sub_e.get("pass", {}).get("outcome", {}).get("name")
                if pass_outcome is None:  # Completed pass
                    is_confirming_control = True
                    ctrl_name = "pass"
            elif ev_type == "Ball Receipt*":
                rec_outcome = sub_e.get("ball_receipt", {}).get("outcome", {}).get("name")
                if rec_outcome != "Incomplete":
                    is_confirming_control = True
                    ctrl_name = "receipt"
            elif ev_type == "Dribble":
                drib_outcome = sub_e.get("dribble", {}).get("outcome", {}).get("name")
                if drib_outcome != "Incomplete":
                    is_confirming_control = True
                    ctrl_name = "dribble"
            elif ev_type == "Shot":
                is_confirming_control = True
                ctrl_name = "shot"

            if is_confirming_control:
                # Require verified transition evidence
                if pending_acq is not None:
                    acq_pathway = pending_acq["pathway"]
                    evidence = f"{acq_pathway}_plus_{ctrl_name}"
                    return pending_acq["acq_time"], dt, sub_e.get("id"), ev_type, evidence

                elif sub_poss != poss_id and sub_poss_team == press_team:
                    if ctrl_name == "pass":
                        evidence = "new_possession_completed_pass"
                    else:
                        evidence = f"new_possession_plus_{ctrl_name}"
                    return dt, dt, sub_e.get("id"), ev_type, evidence

                else:
                    # Standalone action in opponent possession sequence without transition evidence -> REJECT
                    continue

    return None, None, None, None, None


def compute_episode_outcomes(
    episode: Dict[str, Any],
    events: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Compute controlled regain, annotation regain, 15s transition risk, and 3-class outcomes.

    Parameters
    ----------
    episode : dict
        Counterpress episode dictionary containing initiation_event_id, initiation_seconds,
        period, counterpressing_team, possession_team, etc.
    events : list of dict
        Ordered event log of the entire match.

    Returns
    -------
    dict
        Dictionary containing all labeled outcome variables.
    """
    init_id = episode["initiation_event_id"]
    init_sec = episode["initiation_seconds"]
    init_period = episode["period"]
    press_team = episode["counterpressing_team"]
    poss_id = episode["possession_id"]

    # In soccer, a match consists of two competing teams.
    # The opponent team is the squad playing against the counterpressing team.
    opp_team = None
    for e in events:
        t = e.get("team", {}).get("name")
        if t and t != press_team:
            opp_team = t
            break

    if opp_team is None:
        # Fallback for synthetic single-team event fixtures in unit tests
        poss_team = episode.get("possession_team")
        opp_team = poss_team if (poss_team and poss_team != press_team) else "Opponent"

    # Locate the initiation event in the event list
    init_idx = None
    for idx, e in enumerate(events):
        if e.get("id") == init_id:
            init_idx = idx
            break

    if init_idx is None:
        raise ValueError(f"Initiation event {init_id} not found in event sequence.")

    # 1. Determine whether the opponent was ALREADY in its attacking final third at episode start
    opp_initial_x = None
    for i in range(init_idx, -1, -1):
        prev = events[i]
        if prev.get("period") != init_period or prev.get("possession") != poss_id:
            break
        if prev.get("team", {}).get("name") == opp_team and prev.get("location"):
            opp_initial_x = prev["location"][0]
            for j in range(i, -1, -1):
                p2 = events[j]
                if p2.get("period") != init_period or p2.get("possession") != poss_id:
                    break
                if p2.get("team", {}).get("name") == opp_team and p2.get("location"):
                    opp_initial_x = p2["location"][0]
            break

    started_in_final_third = opp_initial_x is not None and opp_initial_x >= FINAL_THIRD_X

    # 2. Track old annotation-based regain (for auditing and comparison)
    regain_time_annot: Optional[float] = None
    regain_event_id_annot: Optional[str] = None
    regain_3s_annot = 0
    regain_5s_annot = 0
    regain_8s_annot = 0

    for j in range(init_idx + 1, len(events)):
        sub_e = events[j]
        if sub_e.get("period") != init_period:
            break
        sub_sec = timestamp_to_seconds(sub_e.get("timestamp", "00:00:00.000"))
        dt = sub_sec - init_sec
        if dt > TRANSITION_WINDOW_SECONDS:
            break
        if dt < 0:
            continue

        sub_poss_team = sub_e.get("possession_team", {}).get("name")
        if sub_poss_team == press_team and regain_time_annot is None:
            regain_time_annot = dt
            regain_event_id_annot = sub_e.get("id")
            if dt <= 3.0 + 1e-6:
                regain_3s_annot = 1
            if dt <= REGAIN_WINDOW_SECONDS + 1e-6:
                regain_5s_annot = 1
            if dt <= 8.0 + 1e-6:
                regain_8s_annot = 1

    # 3. Detect evidence-based controlled regain (v2.7) and legacy v2.6 for auditing
    v26_time, _, _, _ = detect_controlled_regain_v26(
        events, init_idx, init_sec, init_period, press_team, poss_id, opp_team
    )
    regain_5s_controlled_v26 = 1 if (v26_time is not None and v26_time <= REGAIN_WINDOW_SECONDS + 1e-6) else 0

    acq_time, ctrl_time, c_id, c_type, c_evidence = detect_controlled_regain(
        events, init_idx, init_sec, init_period, press_team, poss_id, opp_team
    )

    # Primary conservative definition: confirming control time is controlled_regain_time
    c_regain_time = ctrl_time

    regain_3s_controlled = 1 if (c_regain_time is not None and c_regain_time <= 3.0 + 1e-6) else 0
    regain_5s_controlled = 1 if (c_regain_time is not None and c_regain_time <= REGAIN_WINDOW_SECONDS + 1e-6) else 0
    regain_8s_controlled = 1 if (c_regain_time is not None and c_regain_time <= 8.0 + 1e-6) else 0

    # 4. Check for Opponent Transition: valid BEFORE controlled regain occurs
    shot_15s = 0
    final_third_entry_15s = 0
    time_to_shot: Optional[float] = None
    time_to_final_third_entry: Optional[float] = None
    opp_max_progression: float = opp_initial_x if opp_initial_x is not None else 0.0

    for j in range(init_idx + 1, len(events)):
        sub_e = events[j]
        if sub_e.get("period") != init_period:
            break

        sub_sec = timestamp_to_seconds(sub_e.get("timestamp", "00:00:00.000"))
        dt = sub_sec - init_sec

        if dt > TRANSITION_WINDOW_SECONDS:
            break
        if dt < 0:
            continue

        # Transition danger must occur BEFORE pressing team establishes controlled possession
        if c_regain_time is not None and dt > c_regain_time + 1e-6:
            break

        if sub_e.get("team", {}).get("name") == opp_team:
            ev_type = sub_e.get("type", {}).get("name")

            # Opponent shot
            if ev_type == "Shot" and shot_15s == 0:
                shot_15s = 1
                time_to_shot = round(dt, 3)

            # Opponent attacking final third penetration
            loc = sub_e.get("location")
            if loc and len(loc) >= 1:
                x_coord = loc[0]
                opp_max_progression = max(opp_max_progression, x_coord)
                if x_coord >= FINAL_THIRD_X and not started_in_final_third and final_third_entry_15s == 0:
                    final_third_entry_15s = 1
                    time_to_final_third_entry = round(dt, 3)

    dangerous_escape_15s = 1 if (shot_15s == 1 or final_third_entry_15s == 1) else 0

    # 5. Formulate Three-State Tactical Outcomes
    # New outcome (using v2.7 controlled regain)
    if dangerous_escape_15s == 1:
        outcome_3class = "dangerous_escape"
    elif regain_5s_controlled == 1:
        outcome_3class = "successful_regain"
    else:
        outcome_3class = "harmless_escape"

    # Old outcome (using annotation regain)
    if dangerous_escape_15s == 1:
        outcome_3class_old = "dangerous_escape"
    elif regain_5s_annot == 1:
        outcome_3class_old = "successful_regain"
    else:
        outcome_3class_old = "harmless_escape"

    return {
        # Primary controlled regain variables (v2.7)
        "regain_5s_controlled": regain_5s_controlled,
        "regain_3s_controlled": regain_3s_controlled,
        "regain_8s_controlled": regain_8s_controlled,
        "controlled_acquisition_time": round(acq_time, 3) if acq_time is not None else None,
        "controlled_control_time": round(ctrl_time, 3) if ctrl_time is not None else None,
        "controlled_regain_time": round(c_regain_time, 3) if c_regain_time is not None else None,
        "controlled_regain_event_id": c_id,
        "controlled_regain_event_type": c_type,
        "controlled_regain_evidence": c_evidence,
        # Standard primary variables (aliased to controlled for downstream use)
        "regain_5s": regain_5s_controlled,
        "regain_3s": regain_3s_controlled,
        "regain_8s": regain_8s_controlled,
        "seconds_to_regain": round(c_regain_time, 3) if c_regain_time is not None else None,
        "regain_event_id": c_id,
        # Longitudinal auditing variables
        "regain_5s_controlled_v26": regain_5s_controlled_v26,
        "regain_5s_possession_annotation": regain_5s_annot,
        "regain_3s_possession_annotation": regain_3s_annot,
        "regain_8s_possession_annotation": regain_8s_annot,
        "seconds_to_regain_annotation": round(regain_time_annot, 3) if regain_time_annot is not None else None,
        "regain_event_id_annotation": regain_event_id_annot,
        # Opponent transition risk variables
        "dangerous_escape_15s": dangerous_escape_15s,
        "shot_15s": shot_15s,
        "final_third_entry_15s": final_third_entry_15s,
        "started_in_final_third": started_in_final_third,
        "opponent_initial_x": round(opp_initial_x, 2) if opp_initial_x is not None else None,
        "opponent_max_progression_15s": round(opp_max_progression, 2),
        "time_to_shot": time_to_shot,
        "time_to_final_third_entry": time_to_final_third_entry,
        # 3-class outcomes
        "episode_outcome_3class": outcome_3class,
        "episode_outcome_3class_old": outcome_3class_old,
    }


def label_all_episodes(
    episodes: List[Dict[str, Any]],
    events: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Compute and attach outcome labels to all episodes in a match."""
    sorted_events = sorted(
        events,
        key=lambda e: (
            e.get("period", 1),
            timestamp_to_seconds(e.get("timestamp", "00:00:00.000")),
            e.get("index", 0),
        ),
    )

    labeled = []
    for ep in episodes:
        outcomes = compute_episode_outcomes(ep, sorted_events)
        merged = {**ep, **outcomes}
        labeled.append(merged)

    return labeled
