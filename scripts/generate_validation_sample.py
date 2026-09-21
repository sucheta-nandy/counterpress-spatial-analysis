"""Generate a stratified manual validation sample of 100 counterpress episodes.

Outputs:
- results/tables/manual_episode_validation.csv
- results/manual_validation_report.md
"""

import json
import logging
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from counterpress.config import FIGURES_DIR, RANDOM_SEED, RESULTS_DIR, TABLES_DIR
from counterpress.data import StatsBombDownloader
from counterpress.turnovers import timestamp_to_seconds
from counterpress.visualization import plot_counterpress_freeze_frame

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def build_episode_trace(
    episode: Dict[str, Any],
    events: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Build chronological event trace from 3 seconds before turnover to 20 seconds after initiation."""
    init_sec = episode["initiation_seconds"]
    to_sec = episode["turnover_seconds"]
    init_period = episode["period"]
    press_team = episode["counterpressing_team"]

    start_window = max(0.0, to_sec - 3.0)
    end_window = init_sec + 20.0

    trace = []
    for e in events:
        if e.get("period") != init_period:
            continue
        ts = e.get("timestamp", "00:00:00.000")
        sec = timestamp_to_seconds(ts)
        if start_window <= sec <= end_window:
            rel_to = sec - to_sec
            rel_init = sec - init_sec
            trace.append({
                "index": e.get("index"),
                "timestamp": ts,
                "rel_to_turnover_sec": round(rel_to, 2),
                "rel_to_init_sec": round(rel_init, 2),
                "team": e.get("team", {}).get("name"),
                "possession_team": e.get("possession_team", {}).get("name"),
                "event_type": e.get("type", {}).get("name"),
                "counterpress": e.get("counterpress", False) is True,
                "location": e.get("location"),
                "possession": e.get("possession"),
                "play_pattern": e.get("play_pattern", {}).get("name"),
                "is_initiation": e.get("id") == episode["initiation_event_id"],
                "is_turnover": e.get("id") == episode["turnover_event_id"],
            })

    return trace


def main():
    random.seed(RANDOM_SEED)
    downloader = StatsBombDownloader()

    episodes_csv_path = TABLES_DIR / "counterpress_episodes.csv"
    if not episodes_csv_path.exists():
        raise FileNotFoundError(f"{episodes_csv_path} not found.")

    df_episodes = pd.read_csv(episodes_csv_path)
    logger.info(f"Loaded {len(df_episodes)} total episodes.")

    # Stratify by:
    # 1. Outcome class (successful_regain, harmless_escape, dangerous_escape)
    # 2. Gender / competition group
    # 3. Has 360 frame
    # Target: 100 episodes total
    sample_targets = {
        "successful_regain": 40,
        "harmless_escape": 30,
        "dangerous_escape": 30,
    }

    sampled_rows = []
    for outcome_cls, n_target in sample_targets.items():
        subset = df_episodes[df_episodes["episode_outcome_3class"] == outcome_cls].copy()
        # Stratify further across competitions
        comps = subset["competition_name"].unique()
        per_comp = max(1, n_target // len(comps))
        sampled_comp_groups = []
        for c in comps:
            c_sub = subset[subset["competition_name"] == c]
            n_take = min(len(c_sub), per_comp)
            sampled_comp_groups.append(c_sub.sample(n=n_take, random_state=RANDOM_SEED))

        combined_sub = pd.concat(sampled_comp_groups)
        if len(combined_sub) < n_target:
            remaining = subset[~subset["episode_id"].isin(combined_sub["episode_id"])]
            add_count = min(len(remaining), n_target - len(combined_sub))
            if add_count > 0:
                combined_sub = pd.concat([combined_sub, remaining.sample(n=add_count, random_state=RANDOM_SEED)])
        elif len(combined_sub) > n_target:
            combined_sub = combined_sub.sample(n=n_target, random_state=RANDOM_SEED)

        sampled_rows.append(combined_sub)

    df_sample = pd.concat(sampled_rows).sample(frac=1.0, random_state=RANDOM_SEED).reset_index(drop=True)
    logger.info(f"Generated stratified validation sample of {len(df_sample)} episodes.")

    # Prepare manual validation CSV structure
    validation_records = []
    match_events_cache: Dict[int, List[Dict[str, Any]]] = {}

    report_lines = [
        "# Manual Episode Validation Report",
        "",
        "This report documents a stratified sample of 100 counterpress episodes for manual tactical and chronological verification.",
        "",
        "## Validation Summary Statistics",
        f"- Total Sampled Episodes: {len(df_sample)}",
        f"- Competitions Represented: {df_sample['competition_name'].nunique()} ({', '.join(sorted(df_sample['competition_name'].unique()))})",
        f"- Outcomes in Sample: Successful Regains = {(df_sample['episode_outcome_3class'] == 'successful_regain').sum()}, Harmless Escapes = {(df_sample['episode_outcome_3class'] == 'harmless_escape').sum()}, Dangerous Escapes = {(df_sample['episode_outcome_3class'] == 'dangerous_escape').sum()}",
        f"- Episodes with Usable Initiation 360: {df_sample['has_initiation_360'].sum()} ({df_sample['has_initiation_360'].mean()*100:.1f}%)",
        "",
        "---",
        "",
    ]

    for idx, row in df_sample.iterrows():
        mid = int(row["match_id"])
        if mid not in match_events_cache:
            match_events_cache[mid] = downloader.get_events(mid)
        events = match_events_cache[mid]

        ep_dict = row.to_dict()
        trace = build_episode_trace(ep_dict, events)

        # Build validation note explaining algorithm reasoning
        notes = []
        if row["regain_5s"] == 1:
            notes.append(f"Regained possession at dt={row['seconds_to_regain']}s by {row['counterpressing_team']}.")
        else:
            notes.append(f"No regain within 5.0s (delay={row['delay_seconds']}s).")

        if row["dangerous_escape_15s"] == 1:
            triggers = []
            if row["shot_15s"] == 1:
                triggers.append(f"Shot at dt={row['time_to_shot']}s")
            if row["final_third_entry_15s"] == 1:
                triggers.append(f"Final third entry at dt={row['time_to_final_third_entry']}s (initial x={row['opponent_initial_x']}, max x={row['opponent_max_progression_15s']})")
            notes.append("Dangerous transition triggered by: " + "; ".join(triggers) + ".")
        else:
            notes.append(f"Harmless transition (opp max progression x={row['opponent_max_progression_15s']}).")

        val_note = " ".join(notes)

        validation_records.append({
            "episode_id": row["episode_id"],
            "match_id": mid,
            "competition_name": row["competition_name"],
            "period": row["period"],
            "counterpressing_team": row["counterpressing_team"],
            "possession_team": row["possession_team"],
            "initiation_event_type": row["initiation_event_type"],
            "initiation_player_name": row["initiation_player_name"],
            "delay_seconds": row["delay_seconds"],
            "num_actions": row["num_counterpress_actions"],
            "algorithm_counterpress_valid": 1,
            "human_counterpress_valid": "",  # Blank for manual review
            "algorithm_regain_5s": int(row["regain_5s"]),
            "human_regain_5s": "",           # Blank for manual review
            "algorithm_dangerous_escape_15s": int(row["dangerous_escape_15s"]),
            "human_dangerous_escape_15s": "", # Blank for manual review
            "episode_outcome_3class": row["episode_outcome_3class"],
            "validation_notes": val_note,
        })

        # Append to report
        report_lines.append(f"### Episode {idx + 1}: `{row['episode_id']}`")
        report_lines.append(f"- **Match**: `{mid}` | **Competition**: {row['competition_name']} ({row['season_name']})")
        report_lines.append(f"- **Context**: Period {row['period']}, Pressing Team: **{row['counterpressing_team']}** vs. Possession Team: **{row['possession_team']}**")
        report_lines.append(f"- **Initiation Action**: `{row['initiation_event_type']}` by **{row['initiation_player_name']}** at `{row['initiation_timestamp']}` (Turnover delay: {row['delay_seconds']}s)")
        report_lines.append(f"- **Algorithm Classification**: `{row['episode_outcome_3class']}` (Regain 5s: {row['regain_5s']}, Dangerous Escape 15s: {row['dangerous_escape_15s']})")
        report_lines.append(f"- **Rationale**: {val_note}")
        report_lines.append("")
        report_lines.append("**Chronological Event Sequence:**")
        report_lines.append("")
        report_lines.append("| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |")
        report_lines.append("| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |")

        for tr in trace:
            cp_str = "**YES**" if tr["counterpress"] else "-"
            flag_str = ""
            if tr["is_initiation"]:
                flag_str = "⭐ **CP INITIATION**"
            elif tr["is_turnover"]:
                flag_str = "🔄 **TURNOVER**"
            loc_str = f"[{tr['location'][0]:.1f}, {tr['location'][1]:.1f}]" if tr["location"] else "-"

            report_lines.append(
                f"| {tr['rel_to_turnover_sec']:+.2f} | {tr['rel_to_init_sec']:+.2f} | {tr['timestamp']} | {tr['team']} | {tr['possession_team']} | {tr['event_type']} | {cp_str} | {loc_str} | {flag_str} |"
            )
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    df_val = pd.DataFrame(validation_records)
    val_csv_path = TABLES_DIR / "manual_episode_validation.csv"
    df_val.to_csv(val_csv_path, index=False)
    logger.info(f"Saved manual validation table to {val_csv_path}")

    report_md_path = RESULTS_DIR / "manual_validation_report.md"
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    logger.info(f"Saved manual validation report to {report_md_path}")


if __name__ == "__main__":
    main()
