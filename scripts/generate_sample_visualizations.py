"""Generate sample pitch visualizations and verify individual counterpress sequences.

Verifies:
1. Event ordering
2. Event timestamps and latency
3. Team identities (pressing team vs possession team)
4. Teammate/opponent interpretation in 360 freeze frames
5. Alignment of actor location between event record and 360 freeze frame
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from counterpress.config import FIGURES_DIR
from counterpress.data import StatsBombDownloader
from counterpress.visualization import plot_counterpress_freeze_frame

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def find_and_verify_counterpress_example(
    match_id: int,
    match_desc: str,
    event_idx_hint: int = None,
    save_filename: str = None,
) -> Dict[str, Any]:
    """Inspect and visualize a counterpress event with full verification."""
    dl = StatsBombDownloader()
    events = dl.get_events(match_id)
    frames = dl.get_three_sixty(match_id)

    frames_by_uuid = {f["event_uuid"]: f for f in frames} if frames else {}

    # Find suitable counterpress events
    candidate_indices = []
    for idx, e in enumerate(events):
        if e.get("counterpress") is True and e.get("id") in frames_by_uuid:
            f = frames_by_uuid[e.get("id")]
            if len(f.get("freeze_frame", [])) >= 8:  # Good visibility
                candidate_indices.append(idx)

    if not candidate_indices:
        raise ValueError(f"No suitable 360 counterpress events found in match {match_id}")

    chosen_idx = event_idx_hint if event_idx_hint in candidate_indices else candidate_indices[0]
    cp_event = events[chosen_idx]
    frame = frames_by_uuid[cp_event["id"]]

    # Verification checks
    ev_loc = cp_event.get("location")
    ev_type = cp_event.get("type", {}).get("name")
    ev_team = cp_event.get("team", {}).get("name")
    ev_player = cp_event.get("player", {}).get("name")
    ev_time = cp_event.get("timestamp")
    ev_period = cp_event.get("period")
    ev_poss = cp_event.get("possession")
    ev_possteam = cp_event.get("possession_team", {}).get("name")

    # Find actor in freeze frame
    players = frame.get("freeze_frame", [])
    actors = [p for p in players if p.get("actor")]
    teammates = [p for p in players if p.get("teammate")]
    opponents = [p for p in players if not p.get("teammate")]

    actor_loc = actors[0]["location"] if actors else None

    # Check coordinate alignment
    coord_diff = None
    if ev_loc and actor_loc:
        dx = abs(ev_loc[0] - actor_loc[0])
        dy = abs(ev_loc[1] - actor_loc[1])
        coord_diff = (dx, dy)

    # Preceding event to verify turnover sequence
    preceding_events = events[max(0, chosen_idx - 5) : chosen_idx]
    subsequent_events = events[chosen_idx + 1 : min(len(events), chosen_idx + 6)]

    # Generate figure
    save_path = FIGURES_DIR / save_filename if save_filename else None
    plot_counterpress_freeze_frame(
        event=cp_event,
        freeze_frame=frame,
        match_info={"competition_name": match_desc, "match_date": cp_event.get("timestamp")},
        show_density_radii=True,
        save_path=save_path,
        dark_mode=True,
    )

    return {
        "match_id": match_id,
        "match_desc": match_desc,
        "chosen_index": cp_event.get("index"),
        "period": ev_period,
        "timestamp": ev_time,
        "event_type": ev_type,
        "pressing_team": ev_team,
        "possession_team": ev_possteam,
        "actor_player": ev_player,
        "event_location": ev_loc,
        "freeze_frame_actor_location": actor_loc,
        "coord_difference_dx_dy": coord_diff,
        "total_visible_players": len(players),
        "visible_teammates": len(teammates),
        "visible_opponents": len(opponents),
        "has_actor_flag": len(actors) == 1,
        "figure_saved": str(save_path) if save_path else None,
        "preceding_types": [e.get("type", {}).get("name") for e in preceding_events],
        "subsequent_types": [e.get("type", {}).get("name") for e in subsequent_events],
    }


def main():
    examples = [
        {
            "match_id": 3857276,
            "match_desc": "FIFA World Cup 2022: Canada vs. Morocco",
            "filename": "counterpress_example_1_worldcup.png",
        },
        {
            "match_id": 3895292,
            "match_desc": "1. Bundesliga 2023/2024: Union Berlin vs. Bayer Leverkusen",
            "filename": "counterpress_example_2_bundesliga.png",
        },
        {
            "match_id": 3930163,
            "match_desc": "UEFA Euro 2024: Serbia vs. England",
            "filename": "counterpress_example_3_euro2024.png",
        },
        {
            "match_id": 3773565,
            "match_desc": "La Liga 2020/2021: Granada vs. Barcelona",
            "filename": "counterpress_example_4_laliga.png",
        },
    ]

    verification_reports = []
    for ex in examples:
        logger.info(f"Processing and verifying {ex['match_desc']}...")
        rep = find_and_verify_counterpress_example(
            match_id=ex["match_id"],
            match_desc=ex["match_desc"],
            save_filename=ex["filename"],
        )
        verification_reports.append(rep)

    report_df = pd.DataFrame(verification_reports)
    print("\n=== VERIFICATION SUMMARY TABLE ===")
    cols_to_print = [
        "match_desc",
        "timestamp",
        "event_type",
        "pressing_team",
        "possession_team",
        "actor_player",
        "coord_difference_dx_dy",
        "total_visible_players",
    ]
    print(report_df[cols_to_print].to_markdown(index=False))

    # Save detailed JSON report
    report_json_path = FIGURES_DIR / "verification_examples_report.json"
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(verification_reports, f, indent=2)
    logger.info(f"Saved verification report to {report_json_path}")


if __name__ == "__main__":
    main()
