"""Auditing pipeline: computes exact statistics for all StatsBomb competitions with 360 frames.

Produces:
- results/tables/competition_360_audit.csv
- results/tables/competition_360_audit.md
- data/raw/match_manifest.csv
"""

import logging
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from counterpress.config import RAW_DIR, RESULTS_DIR, TABLES_DIR
from counterpress.data import (
    StatsBombDownloader,
    build_match_manifest,
    load_competitions,
    load_events,
    load_matches,
    load_three_sixty,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def process_match(match: Dict[str, Any], downloader: StatsBombDownloader) -> Dict[str, Any]:
    """Process a single match to extract event counts and 360 coverage."""
    match_id = match["match_id"]
    has_360 = match.get("match_status_360") == "available"

    try:
        events = downloader.get_events(match_id)
        if events is None:
            events = []
    except Exception as e:
        logger.error(f"Error fetching events for match {match_id}: {e}")
        events = []

    frames = None
    frame_uuids = set()
    if has_360:
        try:
            frames = downloader.get_three_sixty(match_id)
            if frames:
                frame_uuids = {f["event_uuid"] for f in frames if len(f.get("freeze_frame", [])) > 0}
        except Exception as e:
            logger.error(f"Error fetching 360 for match {match_id}: {e}")

    n_events = len(events)
    n_cp = 0
    n_cp_with_usable_360 = 0

    for e in events:
        if e.get("counterpress") is True:
            n_cp += 1
            if e.get("id") in frame_uuids:
                n_cp_with_usable_360 += 1

    return {
        "match_id": match_id,
        "competition_id": match["competition_id"],
        "season_id": match["season_id"],
        "competition_name": match["competition_name"],
        "season_name": match["season_name"],
        "has_360": has_360,
        "n_events": n_events,
        "n_cp": n_cp,
        "n_cp_with_usable_360": n_cp_with_usable_360,
    }


def main():
    start_time = time.time()
    downloader = StatsBombDownloader()

    logger.info("Loading competitions...")
    comps = load_competitions()

    # Filter to the 12 competitions with 360 data
    c_360 = comps[comps["match_available_360"].notna()].copy()
    logger.info(f"Found {len(c_360)} competitions with 360 flag.")

    all_matches = []
    for _, c in c_360.iterrows():
        cid = c["competition_id"]
        sid = c["season_id"]
        cname = c["competition_name"]
        sname = c["season_name"]
        m_list = downloader.get_matches(cid, sid)
        for m in m_list:
            all_matches.append({
                "match_id": m["match_id"],
                "competition_id": cid,
                "season_id": sid,
                "competition_name": cname,
                "season_name": sname,
                "match_status_360": m.get("match_status_360"),
            })

    logger.info(f"Total matches across 12 competitions: {len(all_matches)}")
    m_with_360 = [m for m in all_matches if m.get("match_status_360") == "available"]
    logger.info(f"Total matches with 360 available: {len(m_with_360)}")

    logger.info("Auditing matches concurrently (max_workers=20)...")
    results = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(process_match, m, downloader): m["match_id"] for m in all_matches}
        done_count = 0
        for fut in as_completed(futures):
            mid = futures[fut]
            try:
                res = fut.result()
                results.append(res)
            except Exception as e:
                logger.error(f"Match {mid} raised exception: {e}")
            done_count += 1
            if done_count % 50 == 0 or done_count == len(all_matches):
                logger.info(f"Processed {done_count}/{len(all_matches)} matches...")

    df_matches = pd.DataFrame(results)

    # Aggregate by competition and season
    summary = []
    for (cid, sid, cname, sname), group in df_matches.groupby(
        ["competition_id", "season_id", "competition_name", "season_name"]
    ):
        match_count = len(group)
        match_count_360 = group["has_360"].sum()
        total_events = group["n_events"].sum()
        total_cp = group["n_cp"].sum()
        total_cp_360 = group["n_cp_with_usable_360"].sum()
        pct_cp_360 = (total_cp_360 / total_cp * 100) if total_cp > 0 else 0.0

        summary.append({
            "competition": cname,
            "season": sname,
            "competition_id": cid,
            "season_id": sid,
            "match_count": int(match_count),
            "match_count_360": int(match_count_360),
            "n_event_records": int(total_events),
            "n_counterpress_events": int(total_cp),
            "n_counterpress_usable_360": int(total_cp_360),
            "pct_counterpress_usable_360": round(pct_cp_360, 2),
        })

    df_summary = pd.DataFrame(summary).sort_values(
        by=["match_count_360", "n_counterpress_usable_360"], ascending=[False, False]
    )

    # Add Total Row
    total_row = pd.DataFrame([{
        "competition": "TOTAL",
        "season": "ALL",
        "competition_id": "-",
        "season_id": "-",
        "match_count": int(df_summary["match_count"].sum()),
        "match_count_360": int(df_summary["match_count_360"].sum()),
        "n_event_records": int(df_summary["n_event_records"].sum()),
        "n_counterpress_events": int(df_summary["n_counterpress_events"].sum()),
        "n_counterpress_usable_360": int(df_summary["n_counterpress_usable_360"].sum()),
        "pct_counterpress_usable_360": round(
            df_summary["n_counterpress_usable_360"].sum() / df_summary["n_counterpress_events"].sum() * 100, 2
        ),
    }])
    df_with_total = pd.concat([df_summary, total_row], ignore_index=True)

    # Save to CSV and Markdown
    csv_path = TABLES_DIR / "competition_360_audit.csv"
    md_path = TABLES_DIR / "competition_360_audit.md"

    df_with_total.to_csv(csv_path, index=False)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# StatsBomb Open Data: 360 Competition Audit\n\n")
        f.write(df_with_total.to_markdown(index=False))
        f.write("\n")

    logger.info(f"Saved audit table to {csv_path} and {md_path}")
    print("\n" + df_with_total.to_markdown(index=False) + "\n")
    logger.info(f"Completed audit pipeline in {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()
