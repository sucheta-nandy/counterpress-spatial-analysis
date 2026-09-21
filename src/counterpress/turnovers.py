"""Turnover detection and counterpress episode extraction.

Operational Definitions:
- Counterpress Action: A single defensive action (Pressure, Block, Duel, etc.)
  tagged with counterpress=True by StatsBomb (occurring within 5 seconds of an open-play turnover).
- Counterpress Episode: The aggregated sequence of all counterpress actions executed by the
  dispossessed team during a single post-turnover opposition possession.
- Episode Initiation: The chronologically first valid counterpress-tagged action by the pressing team.
"""

import logging
from typing import Any, Dict, List, Optional, Set, Tuple

import pandas as pd

from counterpress.config import COUNTERPRESS_WINDOW_SECONDS

logger = logging.getLogger(__name__)

# StatsBomb play patterns representing open play vs dead-ball set piece restarts
SET_PIECE_PATTERNS = {
    "From Free Kick",
    "From Corner",
    "From Throw In",
    "From Goal Kick",
    "From Kick Off",
    "Other",
}

OPEN_PLAY_PATTERNS = {
    "Regular Play",
    "From Counter",
    "From Keeper",
}


def timestamp_to_seconds(ts: str) -> float:
    """Convert 'HH:MM:SS.mmm' string to total seconds within the period."""
    if not ts or not isinstance(ts, str):
        return 0.0
    parts = ts.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    return float(ts)


def is_open_play_transition(play_pattern: Optional[str]) -> bool:
    """Determine whether a possession transition occurred in open play."""
    if not play_pattern:
        return True
    return play_pattern in OPEN_PLAY_PATTERNS


def classify_turnover_context(
    origin_pattern: Optional[str],
    elapsed_seconds: float,
    successful_passes: int,
    is_restart_event: bool = False,
) -> str:
    """Classify the tactical context of the turnover.

    Distinguishes genuine open-play transitions from immediate dead-ball restart phases.

    Returns
    -------
    str
        'open_play', 'immediate_restart_phase', or 'ambiguous'
    """
    if not origin_pattern or origin_pattern in OPEN_PLAY_PATTERNS:
        return "open_play"

    # Possession originated from a set-piece restart
    if is_restart_event or successful_passes == 0 or elapsed_seconds < 3.0:
        return "immediate_restart_phase"
    elif successful_passes >= 2 and elapsed_seconds >= 5.0:
        return "open_play"
    else:
        return "ambiguous"


def identify_turnover_event(
    events: List[Dict[str, Any]],
    first_cp_event: Dict[str, Any],
    max_search_seconds: float = 8.0,
) -> Tuple[Optional[Dict[str, Any]], float, str]:
    """Find the specific event marking the change of possession prior to the counterpress action.

    Searches backward from the first counterpress event to locate where the pressing team
    lost possession or the opponent established control.

    Returns
    -------
    turnover_event : dict or None
    latency_seconds : float
    turnover_link_quality : str
        'high', 'ambiguous', or 'invalid'
    """
    cp_per = first_cp_event.get("period", 1)
    cp_time = timestamp_to_seconds(first_cp_event.get("timestamp", "00:00:00.000"))
    cp_team = first_cp_event.get("team", {}).get("name")

    # Find the index of first_cp_event in events list
    target_pos = None
    for idx, e in enumerate(events):
        if e.get("id") == first_cp_event.get("id"):
            target_pos = idx
            break

    if target_pos is None or target_pos == 0:
        return None, 0.0, "invalid"

    opp_events = []
    cp_dispossessed_event = None
    first_opp_event = None

    for i in range(target_pos - 1, -1, -1):
        prev = events[i]
        if prev.get("period") != cp_per:
            break
        prev_time = timestamp_to_seconds(prev.get("timestamp", "00:00:00.000"))
        dt = cp_time - prev_time
        if dt > max_search_seconds:
            break

        p_team = prev.get("team", {}).get("name")
        p_type = prev.get("type", {}).get("name")

        if p_team != cp_team:
            opp_events.append((i, prev, dt))
        else:
            if opp_events:
                cp_dispossessed_event = prev
                first_opp_event = opp_events[-1][1]
                break
            else:
                if p_type in {"Pass", "Miscontrol", "Dispossessed", "Dribble", "Shot", "Clearance"}:
                    cp_dispossessed_event = prev
                    break

    if first_opp_event is not None:
        to_ev = first_opp_event
        latency = cp_time - timestamp_to_seconds(to_ev.get("timestamp", "00:00:00.000"))
        if latency <= 5.0:
            quality = "high"
        elif latency <= 6.0:
            quality = "ambiguous"
        else:
            quality = "invalid"
        return to_ev, max(0.0, latency), quality
    elif cp_dispossessed_event is not None:
        to_ev = cp_dispossessed_event
        latency = cp_time - timestamp_to_seconds(to_ev.get("timestamp", "00:00:00.000"))
        if latency <= 5.0:
            quality = "high"
        elif latency <= 6.0:
            quality = "ambiguous"
        else:
            quality = "invalid"
        return to_ev, max(0.0, latency), quality
    elif opp_events:
        to_ev = opp_events[-1][1]
        latency = cp_time - timestamp_to_seconds(to_ev.get("timestamp", "00:00:00.000"))
        quality = "invalid" if latency > 5.0 else "ambiguous"
        return to_ev, max(0.0, latency), quality
    else:
        return None, 0.0, "invalid"


def extract_counterpress_episodes(
    events: List[Dict[str, Any]],
    match_info: Optional[Dict[str, Any]] = None,
    usable_360_uuids: Optional[Set[str]] = None,
) -> List[Dict[str, Any]]:
    """Extract validated episode-level counterpress events from an ordered event log.

    Parameters
    ----------
    events : list of dict
        Ordered match events.
    match_info : dict, optional
        Metadata about the match (match_id, competition, season, etc.).
    usable_360_uuids : set of str, optional
        Set of event UUIDs that have usable 360 freeze frames.

    Returns
    -------
    list of dict
        List of extracted counterpress episodes with initiation events and turnover references.
    """
    if usable_360_uuids is None:
        usable_360_uuids = set()

    match_id = match_info.get("match_id") if match_info else events[0].get("match_id", 0)
    comp_name = match_info.get("competition_name", "Unknown") if match_info else ""
    season_name = match_info.get("season_name", "Unknown") if match_info else ""

    # Ensure deterministic sort: period, timestamp, index
    sorted_events = sorted(
        events,
        key=lambda e: (
            e.get("period", 1),
            timestamp_to_seconds(e.get("timestamp", "00:00:00.000")),
            e.get("index", 0),
        ),
    )

    # Group events by possession identifier
    possessions: Dict[int, List[Dict[str, Any]]] = {}
    for e in sorted_events:
        p = e.get("possession")
        if p is not None:
            if p not in possessions:
                possessions[p] = []
            possessions[p].append(e)

    episodes = []
    p_ids = sorted(list(possessions.keys()))

    for p_id in p_ids:
        p_events = possessions[p_id]
        if not p_events:
            continue

        p_team = p_events[0].get("possession_team", {}).get("name")
        p_team_id = p_events[0].get("possession_team", {}).get("id")
        p_per = p_events[0].get("period", 1)
        play_pattern = p_events[0].get("play_pattern", {}).get("name")
        p_start_ev = p_events[0]
        p_start_time = timestamp_to_seconds(p_start_ev.get("timestamp", "00:00:00.000"))
        p_start_idx = p_start_ev.get("index", 0)

        # Collect all counterpress-tagged actions in this possession
        cp_actions = [e for e in p_events if e.get("counterpress") is True]
        if not cp_actions:
            continue

        # Group by pressing team (in nearly all cases, exactly one defending team presses)
        pressing_teams = sorted(list(set(e.get("team", {}).get("name") for e in cp_actions)))

        for press_team in pressing_teams:
            team_cps = [e for e in cp_actions if e.get("team", {}).get("name") == press_team]
            if not team_cps:
                continue

            # Initiation event is the first chronological counterpress action
            init_event = team_cps[0]
            init_id = init_event.get("id")
            init_ts = init_event.get("timestamp")
            init_sec = timestamp_to_seconds(init_ts)
            init_loc = init_event.get("location")
            init_actor = init_event.get("player", {})
            init_type = init_event.get("type", {}).get("name")

            # Identify turnover event
            turnover_ev, delay, link_quality = identify_turnover_event(sorted_events, init_event)
            if turnover_ev is None:
                # Fall back to first event of the possession for reporting
                turnover_ev = p_events[0]
                delay = max(0.0, init_sec - timestamp_to_seconds(turnover_ev.get("timestamp", "00:00:00.000")))
                link_quality = "invalid"

            to_id = turnover_ev.get("id")
            to_ts = turnover_ev.get("timestamp")
            to_sec = timestamp_to_seconds(to_ts)
            to_type = turnover_ev.get("type", {}).get("name")
            to_loc = turnover_ev.get("location")
            to_idx = turnover_ev.get("index", 0)

            # Classify turnover context (open play vs immediate restart phase)
            intervening = [e for e in p_events if p_start_idx <= e.get("index", 0) <= to_idx]
            passes = [e for e in intervening if e.get("type", {}).get("name") == "Pass"]
            succ_passes = [e for e in passes if not e.get("pass", {}).get("outcome") and e.get("index", 0) < to_idx]
            elapsed_from_restart = max(0.0, to_sec - p_start_time)
            is_restart_ev = (to_idx == p_start_idx)

            turnover_context = classify_turnover_context(
                origin_pattern=play_pattern,
                elapsed_seconds=elapsed_from_restart,
                successful_passes=len(succ_passes),
                is_restart_event=is_restart_ev,
            )
            is_open_play = (turnover_context == "open_play")

            # Latency valid flag: defensible link producing 0 <= delay <= 5.0
            latency_valid = bool(0.0 <= delay <= 5.0 and link_quality == "high")

            # Unique deterministic episode ID
            episode_id = f"{match_id}_p{p_id}_{init_id[:8]}"

            episodes.append({
                "episode_id": episode_id,
                "match_id": match_id,
                "competition_name": comp_name,
                "season_name": season_name,
                "period": p_per,
                "possession_id": p_id,
                "counterpressing_team": press_team,
                "counterpressing_team_id": init_event.get("team", {}).get("id"),
                "possession_team": p_team,
                "possession_team_id": p_team_id,
                "possession_origin_pattern": play_pattern,
                "play_pattern": play_pattern,
                "turnover_context": turnover_context,
                "is_open_play": is_open_play,
                "turnover_event_id": to_id,
                "turnover_event_type": to_type,
                "turnover_timestamp": to_ts,
                "turnover_seconds": to_sec,
                "turnover_location": to_loc,
                "turnover_link_quality": link_quality,
                "initiation_event_id": init_id,
                "initiation_event_type": init_type,
                "initiation_timestamp": init_ts,
                "initiation_seconds": init_sec,
                "initiation_location": init_loc,
                "initiation_player_id": init_actor.get("id"),
                "initiation_player_name": init_actor.get("name"),
                "delay_seconds": round(delay, 3),
                "latency_valid": latency_valid,
                "num_counterpress_actions": len(team_cps),
                "all_counterpress_event_ids": [e.get("id") for e in team_cps],
                "has_initiation_360": init_id in usable_360_uuids,
                "opponent_team_at_turnover": turnover_ev.get("team", {}).get("name"),
                "possession_team_at_counterpress_initiation": init_event.get("possession_team", {}).get("name"),
                "possession_id_at_counterpress_initiation": init_event.get("possession"),
            })

    return episodes
