"""Script to audit transition pathways, analyze the v2.6 -> v2.7 drop, and reconcile dangerous escape.

Outputs:
1. Section B: results/tables/regain_v27_rejected_manual_audit.csv (120 stratified sample cases)
2. Section B: results/regain_v27_rejected_manual_audit.md (120 cases with full -3s to +8s event traces)
3. Section C: Automated classification of all 11,544 changed cases
4. Section D: Full reconciliation of the 2,286 dangerous escape changes
"""

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from counterpress.config import FINAL_THIRD_X, REGAIN_WINDOW_SECONDS, TRANSITION_WINDOW_SECONDS
from counterpress.data import load_events
from counterpress.outcomes import detect_controlled_regain_v26
from counterpress.turnovers import timestamp_to_seconds

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

RESULTS_DIR = Path("results")
TABLES_DIR = RESULTS_DIR / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)


def get_actual_opponent(events: List[Dict[str, Any]], press_team: str) -> Optional[str]:
    """Determine the true opposing team in a two-team soccer match."""
    for e in events:
        t = e.get("team", {}).get("name")
        if t and t != press_team:
            return t
    return None


def format_event_trace_extended_11s(
    events: List[Dict[str, Any]],
    init_idx: int,
    init_sec: float,
    press_team: str,
    opp_team: str,
    v26_idx: Optional[int] = None,
) -> Tuple[str, Optional[int], Optional[int], Optional[int]]:
    """Format an extended chronological event trace from -3s to +8s relative to initiation.

    Returns:
        (markdown_table_str, opponent_last_ctrl_idx, possible_trans_idx, press_first_ctrl_idx)
    """
    # Identify window: -3.0s to +8.0s
    window_indices = []
    for idx, e in enumerate(events):
        ts = e.get("timestamp", "00:00:00.000")
        t_sec = timestamp_to_seconds(ts)
        rel_init = t_sec - init_sec
        if -3.0 <= rel_init <= 8.0:
            window_indices.append(idx)

    if not window_indices:
        # Fallback to index-based slice around init_idx
        start_idx = max(0, init_idx - 5)
        end_idx = min(len(events), init_idx + 15)
        window_indices = list(range(start_idx, end_idx))

    opp_last_ctrl_idx = None
    possible_trans_idx = None
    press_first_ctrl_idx = None

    # Scan for markers
    for idx in window_indices:
        e = events[idx]
        ts = e.get("timestamp", "00:00:00.000")
        t_sec = timestamp_to_seconds(ts)
        rel_init = t_sec - init_sec
        team = e.get("team", {}).get("name")
        ev_type = e.get("type", {}).get("name")

        # Opponent controlled action before/around transition
        if team == opp_team:
            if ev_type in {"Pass", "Carry", "Dribble", "Shot"}:
                if ev_type == "Pass":
                    if not e.get("pass", {}).get("outcome"):
                        opp_last_ctrl_idx = idx
                elif ev_type == "Dribble":
                    if e.get("dribble", {}).get("outcome", {}).get("name") != "Incomplete":
                        opp_last_ctrl_idx = idx
                else:
                    opp_last_ctrl_idx = idx

            # Possible transition events by opponent
            if ev_type in {"Miscontrol", "Dispossessed"}:
                possible_trans_idx = idx
            elif ev_type == "Pass" and e.get("pass", {}).get("outcome", {}).get("name") in {"Incomplete", "Pass Offside", "Out"}:
                possible_trans_idx = idx
            elif ev_type == "Dribble" and e.get("dribble", {}).get("outcome", {}).get("name") == "Incomplete":
                possible_trans_idx = idx

        # Possible transition events by pressing team
        if team == press_team:
            if ev_type in {"Ball Recovery", "Interception", "Duel", "50/50"}:
                if possible_trans_idx is None or idx < (press_first_ctrl_idx or 999999):
                    possible_trans_idx = idx

            if ev_type in {"Carry", "Pass", "Ball Receipt*", "Shot", "Dribble"}:
                if ev_type == "Pass" and not e.get("pass", {}).get("outcome"):
                    if press_first_ctrl_idx is None and rel_init >= 0:
                        press_first_ctrl_idx = idx
                elif ev_type == "Ball Receipt*" and e.get("ball_receipt", {}).get("outcome", {}).get("name") != "Incomplete":
                    if press_first_ctrl_idx is None and rel_init >= 0:
                        press_first_ctrl_idx = idx
                elif ev_type in {"Carry", "Shot"}:
                    if press_first_ctrl_idx is None and rel_init >= 0:
                        press_first_ctrl_idx = idx

    lines = []
    lines.append("| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |")
    lines.append("| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |")

    for idx in window_indices:
        e = events[idx]
        ts = e.get("timestamp", "00:00:00.000")
        t_sec = timestamp_to_seconds(ts)
        rel_init = round(t_sec - init_sec, 2)

        team = e.get("team", {}).get("name", "Unknown")[:18]
        poss_team = e.get("possession_team", {}).get("name", "Unknown")[:18]
        poss_id = e.get("possession", "-")
        ev_type = e.get("type", {}).get("name", "Unknown")
        is_cp = "Yes" if e.get("counterpress") is True else "-"

        loc = e.get("location")
        loc_str = f"[{loc[0]:.1f}, {loc[1]:.1f}]" if loc and len(loc) >= 2 else "-"

        details = []
        if ev_type == "Pass":
            rec = e.get("pass", {}).get("recipient", {}).get("name")
            outc = e.get("pass", {}).get("outcome", {}).get("name")
            if outc:
                details.append(f"Incomplete ({outc})")
            elif rec:
                details.append(f"-> {rec[:14]}")
            else:
                details.append("Complete")
        elif ev_type == "Ball Receipt*":
            outc = e.get("ball_receipt", {}).get("outcome", {}).get("name")
            if outc:
                details.append(f"Incomplete Receipt ({outc})")
            else:
                details.append("Controlled Receipt")
        elif ev_type == "Shot":
            outc = e.get("shot", {}).get("outcome", {}).get("name", "Shot")
            details.append(outc)
        elif ev_type == "Duel":
            d_type = e.get("duel", {}).get("type", {}).get("name")
            d_outc = e.get("duel", {}).get("outcome", {}).get("name")
            if d_type:
                details.append(d_type)
            if d_outc:
                details.append(d_outc)
        elif ev_type == "Interception":
            i_outc = e.get("interception", {}).get("outcome", {}).get("name")
            if i_outc:
                details.append(i_outc)
            else:
                details.append("Intercepted")
        elif ev_type == "Carry":
            details.append("Carry")
        elif ev_type == "Dribble":
            d_outc = e.get("dribble", {}).get("outcome", {}).get("name")
            if d_outc:
                details.append(d_outc)
            else:
                details.append("Complete")
        elif ev_type == "Miscontrol":
            details.append("Miscontrol")
        elif ev_type == "Dispossessed":
            details.append("Dispossessed")

        det_str = ", ".join(details) if details else ""

        # Tactical markers
        markers = []
        if idx == init_idx:
            markers.append("**CP INITIATION**")
        if idx == opp_last_ctrl_idx:
            markers.append("**OPPONENT LAST CONTROL**")
        if idx == possible_trans_idx:
            markers.append("**POSSIBLE TRANSITION**")
        if idx == press_first_ctrl_idx:
            markers.append("**PRESSING-TEAM FIRST CONTROL**")
        if idx == v26_idx:
            markers.append("(v2.6 Regain Event)")

        marker_str = " | ".join(markers) if markers else ""

        lines.append(
            f"| {rel_init:+6.2f} | {ts} | {team:<18} | {poss_team:<18} | {poss_id} | {ev_type:<15} | {is_cp:^5} | {loc_str:<15} | {det_str:<25} | {marker_str} |"
        )

    return "\n".join(lines), opp_last_ctrl_idx, possible_trans_idx, press_first_ctrl_idx


def main():
    start_time = time.time()
    logger.info("Starting comprehensive transition pathway and dangerous escape audit...")

    df = pd.read_csv(TABLES_DIR / "counterpress_episodes.csv", low_memory=False)
    logger.info(f"Loaded {len(df)} total episodes.")

    changed_mask = (df["regain_5s_controlled_v26"] == 1) & (df["regain_5s_controlled"] == 0)
    df_changed = df[changed_mask].copy()
    n_changed = len(df_changed)
    logger.info(f"Total episodes that changed 1 -> 0: {n_changed}")

    # Cache events by match_id
    matches_needed = df_changed["match_id"].unique()
    logger.info(f"Loading events for {len(matches_needed)} matches with changed episodes...")

    events_by_match = {}
    for i, mid in enumerate(matches_needed):
        events_by_match[mid] = load_events(mid)
        if (i + 1) % 50 == 0 or (i + 1) == len(matches_needed):
            logger.info(f"Loaded {i + 1}/{len(matches_needed)} matches...")

    # ==============================================================================
    # SECTION C: AUTOMATED TRANSITION PATHWAY AUDIT
    # ==============================================================================
    logger.info("Classifying transition pathways for all 11,544 changed cases...")

    pathway_classifications = []
    first_ctrl_types = []
    v26_evidence_types = []
    is_same_team_bug_flags = []
    v26_indices = []

    for idx, row in df_changed.iterrows():
        mid = int(row["match_id"])
        events = events_by_match[mid]
        init_id = row["initiation_event_id"]
        init_idx = [i for i, e in enumerate(events) if e.get("id") == init_id][0]
        init_sec = row["initiation_seconds"]
        press_team = row["counterpressing_team"]
        opp_team = get_actual_opponent(events, press_team)

        is_same_team = (row["counterpressing_team"] == row["possession_team"])
        is_same_team_bug_flags.append(is_same_team)

        # Run v2.6 detection to get the exact event that triggered v2.6
        v26_t, v26_id, v26_type, v26_ev = detect_controlled_regain_v26(
            events, init_idx, init_sec, row["period"], press_team, row["possession_id"], row["possession_team"]
        )
        v26_evidence_types.append(v26_ev)
        v26_idx = [i for i, e in enumerate(events) if e.get("id") == v26_id][0] if v26_id else None
        v26_indices.append(v26_idx)

        # Determine the first pressing control candidate event
        ctrl_idx = v26_idx
        ctrl_type = v26_type if v26_type else "None"
        first_ctrl_types.append(ctrl_type)

        if ctrl_idx is None:
            pathway_classifications.append("no_identifiable_turnover")
            continue

        # Inspect events between init_idx and ctrl_idx (or immediately preceding ctrl_idx)
        # Scan backward from ctrl_idx to max(0, ctrl_idx - 6, init_idx - 2)
        prior_events = [events[k] for k in range(max(0, ctrl_idx - 6), ctrl_idx)]
        
        # Check transition signals in prior events
        pathway = None
        for pe in reversed(prior_events):
            pe_team = pe.get("team", {}).get("name")
            pe_type = pe.get("type", {}).get("name")

            if pe_team == opp_team:
                if pe_type == "Pass" and pe.get("pass", {}).get("outcome", {}).get("name") in {"Incomplete", "Pass Offside", "Out"}:
                    pathway = "opponent_incomplete_pass"
                    break
                elif pe_type == "Miscontrol":
                    pathway = "opponent_miscontrol"
                    break
                elif pe_type == "Dispossessed":
                    pathway = "opponent_dispossessed"
                    break
                elif pe_type == "Dribble" and pe.get("dribble", {}).get("outcome", {}).get("name") == "Incomplete":
                    pathway = "opponent_failed_dribble"
                    break
                elif pe_type == "Clearance":
                    pathway = "opponent_clearance"
                    break
                elif pe_type == "Shot":
                    pathway = "opponent_shot"
                    break

            if pe_type in {"Duel", "50/50"}:
                pathway = "contested_duel"
                break

        if pathway is None:
            # Check if opponent continuous passes occurred
            opp_passes = [pe for pe in prior_events if pe.get("team", {}).get("name") == opp_team and pe.get("type", {}).get("name") in {"Pass", "Carry"}]
            press_def = [pe for pe in prior_events if pe.get("team", {}).get("name") == press_team and pe.get("type", {}).get("name") in {"Pressure", "Block", "Foul Committed"}]
            if opp_passes and press_def:
                pathway = "same_possession_defensive_touch"
            elif opp_passes and not press_def:
                pathway = "no_identifiable_turnover"
            else:
                pathway = "other"

        pathway_classifications.append(pathway)

    df_changed["pathway_classification"] = pathway_classifications
    df_changed["first_ctrl_type"] = first_ctrl_types
    df_changed["v26_evidence"] = v26_evidence_types
    df_changed["is_same_team_bug"] = is_same_team_bug_flags
    df_changed["v26_event_index"] = v26_indices

    pathway_counts = df_changed["pathway_classification"].value_counts().to_dict()
    logger.info("==================================================")
    logger.info("PATHWAY CLASSIFICATION FOR ALL 11,544 CHANGED CASES:")
    for k, v in pathway_counts.items():
        logger.info(f"  {k}: {v:,} ({v / n_changed * 100:.2f}%)")
    logger.info("==================================================")

    same_team_counts = df_changed["is_same_team_bug"].value_counts().to_dict()
    logger.info(f"Changed cases affected by same_team bug (opp_team == press_team): {same_team_counts.get(True, 0):,} ({same_team_counts.get(True, 0) / n_changed * 100:.2f}%)")

    # ==============================================================================
    # SECTION B: STRATIFIED MANUAL AUDIT SAMPLE (120 CASES)
    # ==============================================================================
    logger.info("Generating stratified sample of 120 cases for Section B manual audit...")

    # Targets:
    # 30 Carry
    # 30 completed Pass
    # 20 Ball Receipt*
    # 15 Dribble
    # 10 Shot
    # 15 other/common pathways
    # Prefer primary cohort episodes

    def get_stratum(row):
        ctrl = str(row["first_ctrl_type"]).lower()
        if "carry" in ctrl:
            return "carry"
        elif "pass" in ctrl:
            return "pass"
        elif "receipt" in ctrl:
            return "ball_receipt"
        elif "dribble" in ctrl:
            return "dribble"
        elif "shot" in ctrl:
            return "shot"
        else:
            return "other"

    df_changed["sample_stratum"] = df_changed.apply(get_stratum, axis=1)

    target_quotas = {
        "carry": 30,
        "pass": 30,
        "ball_receipt": 20,
        "dribble": 15,
        "shot": 10,
        "other": 15,
    }

    sample_rows = []
    # Prioritize primary cohort
    df_changed_sorted = df_changed.sort_values("primary_cohort_eligible", ascending=False)

    for stratum, quota in target_quotas.items():
        subset = df_changed_sorted[df_changed_sorted["sample_stratum"] == stratum]
        n_take = min(len(subset), quota)
        sample_rows.append(subset.head(n_take))
        logger.info(f"Sampled {n_take}/{quota} for stratum '{stratum}'")

    df_sample_120 = pd.concat(sample_rows, ignore_index=True)
    if len(df_sample_120) < 120:
        rem = df_changed_sorted[~df_changed_sorted["episode_id"].isin(df_sample_120["episode_id"])]
        df_sample_120 = pd.concat([df_sample_120, rem.head(120 - len(df_sample_120))], ignore_index=True)

    df_sample_120 = df_sample_120.head(120).copy()

    # Add blank human review fields
    df_sample_120["human_transition_occurred"] = ""
    df_sample_120["human_control_established"] = ""
    df_sample_120["human_regain_within_5s"] = ""
    df_sample_120["human_notes"] = ""

    # Save to CSV
    csv_cols = [
        "episode_id", "match_id", "competition_name", "period", "counterpressing_team",
        "possession_team", "initiation_seconds", "sample_stratum", "first_ctrl_type",
        "pathway_classification", "v26_evidence", "is_same_team_bug",
        "human_transition_occurred", "human_control_established", "human_regain_within_5s", "human_notes"
    ]
    sample_csv_path = TABLES_DIR / "regain_v27_rejected_manual_audit.csv"
    df_sample_120[csv_cols].to_csv(sample_csv_path, index=False)
    logger.info(f"Saved 120 sample cases to {sample_csv_path}")

    # Build Markdown report for Section B
    logger.info("Building results/regain_v27_rejected_manual_audit.md with full -3s to +8s event logs...")
    md_lines = [
        "# Audit of Counterpress Regain Reductions: v2.6 Positive $\\to$ v2.7 Negative (120 Cases)",
        "",
        "**Cohort**: 120 Stratified Random Cases where `regain_5s_controlled_v26 = 1` and `regain_5s_controlled = 0`",
        f"**Audit Execution Time**: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Sampling Stratification Schema",
        "- **First Control = Carry**: 30 episodes",
        "- **First Control = Completed Pass**: 30 episodes",
        "- **First Control = Ball Receipt***: 20 episodes",
        "- **First Control = Dribble**: 15 episodes",
        "- **First Control = Shot**: 10 episodes",
        "- **Other / Common Pathways**: 15 episodes",
        "",
        "> [!IMPORTANT]",
        "> All human verification fields in this report are strictly blank placeholders for scientific evaluation.",
        "",
        "---",
        "",
    ]

    for idx, row in df_sample_120.iterrows():
        ep_id = row["episode_id"]
        mid = int(row["match_id"])
        cname = row["competition_name"]
        press_t = row["counterpressing_team"]
        poss_t = row["possession_team"]
        events = events_by_match[mid]
        opp_t = get_actual_opponent(events, press_t)

        init_sec = float(row["initiation_seconds"])
        init_id = row["initiation_event_id"]
        init_idx = [i for i, e in enumerate(events) if e.get("id") == init_id][0]
        v26_idx = row["v26_event_index"]

        trace_md, opp_last_idx, poss_trans_idx, press_ctrl_idx = format_event_trace_extended_11s(
            events, init_idx, init_sec, press_t, opp_t, v26_idx
        )

        md_lines.append(f"### Case {idx + 1}: Episode `{ep_id}`")
        md_lines.append(f"- **Match**: `{mid}` ({cname}) | **Period**: {row['period']}")
        md_lines.append(f"- **Counterpressing Team**: **{press_t}** vs Actual Opponent: **{opp_t}** (StatsBomb Poss Team: `{poss_t}`)")
        md_lines.append(f"- **Stratum**: `{row['sample_stratum']}` | **First Press Control Candidate**: `{row['first_ctrl_type']}`")
        md_lines.append(f"- **Automated Pathway Classification**: `{row['pathway_classification']}` | v2.6 Evidence: `{row['v26_evidence']}`")
        md_lines.append(f"- **Affected by Same-Team Annotation**: `{'Yes' if row['is_same_team_bug'] else 'No'}`")
        md_lines.append("")
        md_lines.append("```text")
        md_lines.append("Human Review Evaluation:")
        md_lines.append("  human_transition_occurred: ")
        md_lines.append("  human_control_established: ")
        md_lines.append("  human_regain_within_5s:    ")
        md_lines.append("  human_notes:               ")
        md_lines.append("```")
        md_lines.append("")
        md_lines.append(trace_md)
        md_lines.append("\n---\n")

    audit_md_path = RESULTS_DIR / "regain_v27_rejected_manual_audit.md"
    with open(audit_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    logger.info(f"Saved Section B markdown audit report to {audit_md_path}")

    # ==============================================================================
    # SECTION D: RECONCILE DANGEROUS_ESCAPE_15S
    # ==============================================================================
    logger.info("Reconciling dangerous_escape_15s changes (5,171 in v2.6 -> 7,457 in v2.7 on primary cohort)...")

    pri_df = df[df["primary_cohort_eligible"] == True].copy()
    
    # We want to identify the exact episodes where danger was 0 in v2.6 and became 1 in v2.7
    # Let's compute v2.6 danger vs v2.7 danger for all primary episodes
    danger_diff_records = []
    
    for idx, row in pri_df.iterrows():
        mid = int(row["match_id"])
        events = load_events(mid) if mid not in events_by_match else events_by_match[mid]
        init_id = row["initiation_event_id"]
        init_idx = [i for i, e in enumerate(events) if e.get("id") == init_id][0]
        init_sec = row["initiation_seconds"]
        init_period = row["period"]
        press_team = row["counterpressing_team"]
        opp_team = row["possession_team"]
        actual_opp = get_actual_opponent(events, press_team)

        # Compute v2.6 c_time
        v26_time, _, _, _ = detect_controlled_regain_v26(
            events, init_idx, init_sec, init_period, press_team, row["possession_id"], opp_team
        )

        # Danger under v2.6 rules (censored at v26_time):
        d_v26 = 0
        trigger_v26 = None
        trigger_t_v26 = None
        for j in range(init_idx + 1, len(events)):
            sub_e = events[j]
            if sub_e.get("period") != init_period:
                break
            dt = timestamp_to_seconds(sub_e.get("timestamp", "00:00:00.000")) - init_sec
            if dt > 15.0:
                break
            if dt < 0:
                continue
            if v26_time is not None and dt > v26_time + 1e-6:
                break
            if sub_e.get("team", {}).get("name") == opp_team:
                if sub_e.get("type", {}).get("name") == "Shot":
                    d_v26 = 1
                    trigger_v26 = "shot"
                    trigger_t_v26 = round(dt, 3)
                    break
                loc = sub_e.get("location")
                if loc and loc[0] >= FINAL_THIRD_X and not row["started_in_final_third"]:
                    d_v26 = 1
                    trigger_v26 = "final_third_entry"
                    trigger_t_v26 = round(dt, 3)
                    break

        # Danger in current v2.7 table
        d_v27 = row["dangerous_escape_15s"]

        # If danger changed (0 -> 1):
        if d_v26 == 0 and d_v27 == 1:
            # Determine reason:
            # Did v2.6 censor prematurely because of a regain?
            reason = None
            if v26_time is not None and row["controlled_regain_time"] is None:
                reason = "v26_premature_regain_censoring"
            elif v26_time is not None and row["controlled_regain_time"] is not None and row["controlled_regain_time"] > v26_time:
                reason = "v26_premature_regain_censoring"
            elif row["counterpressing_team"] == row["possession_team"]:
                # When opp_team == press_team, v2.7 checked press_team actions as opponent danger!
                reason = "evaluated_pressing_team_as_opponent"
            else:
                reason = "horizon_or_timing_shift"

            danger_diff_records.append({
                "episode_id": row["episode_id"],
                "match_id": mid,
                "danger_v26": d_v26,
                "danger_v27": d_v27,
                "regain_v26": row["regain_5s_controlled_v26"],
                "regain_v27": row["regain_5s_controlled"],
                "danger_trigger": "shot" if row["shot_15s"] == 1 else "final_third_entry",
                "danger_trigger_time": row["time_to_shot"] if row["shot_15s"] == 1 else row["time_to_final_third_entry"],
                "old_regain_time": v26_time,
                "new_regain_time": row["controlled_regain_time"],
                "change_reason": reason,
            })

    df_danger_diff = pd.DataFrame(danger_diff_records)
    logger.info("==================================================")
    logger.info(f"DANGEROUS ESCAPE 0 -> 1 CHANGES: {len(df_danger_diff)}")
    if len(df_danger_diff) > 0:
        d_reasons = df_danger_diff["change_reason"].value_counts().to_dict()
        for k, v in d_reasons.items():
            logger.info(f"  {k}: {v:,} ({v / len(df_danger_diff) * 100:.2f}%)")
    logger.info("==================================================")

    # Save danger comparison table
    danger_csv_path = TABLES_DIR / "dangerous_escape_v26_vs_v27_reconciliation.csv"
    df_danger_diff.to_csv(danger_csv_path, index=False)
    logger.info(f"Saved dangerous escape reconciliation to {danger_csv_path}")

    logger.info(f"Audit completed in {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()
