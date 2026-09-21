"""Generate 20 publication-quality spatial QA visualizations across diverse tactical strata.

Strata covered:
1. Men's World Cup: High Local Support (num_adv_10 >= 2, attacking third, central)
2. Men's World Cup: Low Local Support (num_adv_10 <= -2, middle third)
3. UEFA Euro: High Local Support (middle third, central)
4. UEFA Euro: Low Local Support (defensive third)
5. Women's World Cup: High Camera Coverage (coverage_10 >= 0.95, attacking third)
6. Women's World Cup: Low Camera Coverage & Touchline (coverage_10 <= 0.65, touchline)
7. UEFA Women's Euro: High Forward Advantage (forward_num_adv >= 2)
8. UEFA Women's Euro: Negative Forward Advantage (forward_num_adv <= -2)
9. La Liga: High Escape Corridor Advantage (escape_corridor_advantage_20 >= 2)
10. La Liga: Negative Escape Corridor Advantage (escape_corridor_advantage_20 <= -2)
11. 1. Bundesliga: High Density Congestion (total_players_within_10 >= 6)
12. 1. Bundesliga: Low Density Open Space (total_players_within_10 <= 2)
13. Ligue 1: Left Touchline Press (distance_to_nearest_touchline <= 4.0)
14. Ligue 1: Pitch Center Axis (lateral_centrality >= 0.92)
15. Defensive Third Pressure (pitch_zone == 'defensive_third')
16. Attacking Third High Press (pitch_zone == 'attacking_third')
17. High Team Compactness (teammate_x_std <= 8.0)
18. Low Team Compactness / Dispersed (teammate_x_std >= 18.0)
19. High Corridor Coverage (escape_corridor_coverage_20 >= 0.90)
20. Low Corridor Coverage (escape_corridor_coverage_20 <= 0.50)
"""

import logging
from pathlib import Path
from typing import Any, Dict, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from counterpress.config import FIGURES_DIR, PROCESSED_DIR, TABLES_DIR
from counterpress.data import StatsBombDownloader
from counterpress.visualization import plot_spatial_qa_freeze_frame

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

QA_DIR = FIGURES_DIR / "qa_spatial"
QA_DIR.mkdir(parents=True, exist_ok=True)


def select_stratified_sample(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """Select 20 diverse episodes meeting distinct tactical and observational strata."""
    selected_indices = []

    def get_candidate(query_str: str, fallback_query: str = "") -> int:
        subset = df.query(query_str)
        for idx in subset.index:
            if idx not in selected_indices:
                return idx
        if fallback_query:
            sub_fallback = df.query(fallback_query)
            for idx in sub_fallback.index:
                if idx not in selected_indices:
                    return idx
        # Fallback to any remaining
        for idx in df.index:
            if idx not in selected_indices:
                return idx
        return df.index[0]

    criteria = [
        # 1. Men's World Cup, High Support
        ("competition == 'FIFA World Cup' and numerical_advantage_10 >= 2 and pitch_zone == 'attacking_third'", "competition == 'FIFA World Cup' and numerical_advantage_10 >= 1"),
        # 2. Men's World Cup, Low Support
        ("competition == 'FIFA World Cup' and numerical_advantage_10 <= -2 and pitch_zone == 'middle_third'", "competition == 'FIFA World Cup' and numerical_advantage_10 <= -1"),
        # 3. UEFA Euro, High Support, Central
        ("competition == 'UEFA Euro' and numerical_advantage_10 >= 2 and lateral_centrality >= 0.80", "competition == 'UEFA Euro' and numerical_advantage_10 >= 1"),
        # 4. UEFA Euro, Low Support, Defensive Third
        ("competition == 'UEFA Euro' and numerical_advantage_10 <= -1 and pitch_zone == 'defensive_third'", "competition == 'UEFA Euro' and pitch_zone == 'defensive_third'"),
        # 5. Women's World Cup, High Coverage
        ("competition == \"Women's World Cup\" and coverage_10 >= 0.95 and pitch_zone == 'attacking_third'", "competition == \"Women's World Cup\" and coverage_10 >= 0.90"),
        # 6. Women's World Cup, Low Coverage & Touchline
        ("competition == \"Women's World Cup\" and coverage_10 <= 0.65 and distance_to_nearest_touchline <= 6.0", "competition == \"Women's World Cup\" and distance_to_nearest_touchline <= 5.0"),
        # 7. UEFA Women's Euro, High Forward Advantage
        ("competition == \"UEFA Women's Euro\" and forward_numerical_advantage >= 2", "competition == \"UEFA Women's Euro\" and forward_numerical_advantage >= 1"),
        # 8. UEFA Women's Euro, Negative Forward Advantage
        ("competition == \"UEFA Women's Euro\" and forward_numerical_advantage <= -2", "competition == \"UEFA Women's Euro\" and forward_numerical_advantage <= -1"),
        # 9. La Liga, High Corridor Advantage
        ("competition == 'La Liga' and escape_corridor_advantage_20 >= 2", "competition == 'La Liga' and escape_corridor_advantage_20 >= 1"),
        # 10. La Liga, Negative Corridor Advantage
        ("competition == 'La Liga' and escape_corridor_advantage_20 <= -2", "competition == 'La Liga' and escape_corridor_advantage_20 <= -1"),
        # 11. 1. Bundesliga, High Density
        ("competition == '1. Bundesliga' and total_players_within_10 >= 6", "competition == '1. Bundesliga' and total_players_within_10 >= 5"),
        # 12. 1. Bundesliga, Low Density
        ("competition == '1. Bundesliga' and total_players_within_10 <= 2 and actor_present == True", "competition == '1. Bundesliga' and total_players_within_10 <= 3"),
        # 13. Ligue 1, Touchline
        ("competition == 'Ligue 1' and distance_to_nearest_touchline <= 4.0", "competition == 'Ligue 1' and distance_to_nearest_touchline <= 8.0"),
        # 14. Ligue 1, Central
        ("competition == 'Ligue 1' and lateral_centrality >= 0.92", "competition == 'Ligue 1' and lateral_centrality >= 0.85"),
        # 15. Defensive Third Pressure
        ("pitch_zone == 'defensive_third' and coverage_10 >= 0.80", "pitch_zone == 'defensive_third'"),
        # 16. Attacking Third High Press
        ("pitch_zone == 'attacking_third' and numerical_advantage_10 >= 1", "pitch_zone == 'attacking_third'"),
        # 17. High Team Compactness
        ("teammate_x_std <= 8.0 and visible_teammate_count_excluding_actor >= 3", "teammate_x_std <= 10.0"),
        # 18. Low Team Compactness
        ("teammate_x_std >= 18.0 and visible_teammate_count_excluding_actor >= 3", "teammate_x_std >= 15.0"),
        # 19. High Corridor Coverage
        ("escape_corridor_coverage_20 >= 0.90 and pitch_zone == 'middle_third'", "escape_corridor_coverage_20 >= 0.80"),
        # 20. Low Corridor Coverage
        ("escape_corridor_coverage_20 <= 0.50 and distance_to_nearest_touchline <= 8.0", "escape_corridor_coverage_20 <= 0.60"),
    ]

    for q, fb in criteria:
        idx = get_candidate(q, fb)
        selected_indices.append(idx)

    selected_rows = [df.loc[idx].to_dict() for idx in selected_indices]
    return selected_rows


def main():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    if not parquet_path.exists():
        raise FileNotFoundError(f"Feature dataset {parquet_path} not found.")

    logger.info(f"Loading features from {parquet_path}...")
    df = pd.read_parquet(parquet_path)

    episodes_csv = TABLES_DIR / "counterpress_episodes.csv"
    df_ep = pd.read_csv(episodes_csv, low_memory=False)
    ep_dict_map = {row["episode_id"]: row.to_dict() for _, row in df_ep.iterrows()}

    downloader = StatsBombDownloader()

    logger.info("Selecting 20 stratified QA sample episodes...")
    sample_rows = select_stratified_sample(df)
    logger.info(f"Selected {len(sample_rows)} episodes for visual QA generation.")

    # Cache frames by match
    match_ids = set(r["match_id"] for r in sample_rows)
    match_frames = {}
    for mid in match_ids:
        frames = downloader.get_three_sixty(mid)
        match_frames[mid] = {f["event_uuid"]: f for f in frames if "event_uuid" in f}

    for idx, row in enumerate(sample_rows, 1):
        ep_id = row["episode_id"]
        mid = row["match_id"]
        init_id = row["initiation_event_id"]

        ep_meta = ep_dict_map.get(ep_id, row)
        f = match_frames.get(mid, {}).get(init_id, {})

        filename = f"qa_spatial_{idx:02d}_{ep_id}.png"
        save_file = QA_DIR / filename

        fig, _ = plot_spatial_qa_freeze_frame(
            episode=ep_meta,
            freeze_frame=f,
            feature_row=row,
            save_path=save_file,
            dark_mode=True,
        )
        plt.close(fig)
        logger.info(f"Generated QA visual [{idx:02d}/20]: {filename}")

    logger.info(f"All 20 Visual QA figures saved to {QA_DIR}")


if __name__ == "__main__":
    main()
