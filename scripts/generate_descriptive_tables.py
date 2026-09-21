"""Generate interpretable descriptive outcome tables across tactical groups.

Produces binned analysis of:
- Regain 5s rate by:
  - numerical_advantage_5
  - numerical_advantage_10
  - nearest teammate distance quintiles
  - nearest opponent distance quintiles
  - pitch third (defensive, middle, attacking)
  - lateral zone (wide vs central)
- Dangerous escape 15s rate by:
  - forward numerical advantage
  - corridor advantage
  - pitch third
  - touchline distance bins

Saves output to: results/tables/descriptive_outcome_tables.csv
"""

import logging
from pathlib import Path
import numpy as np
import pandas as pd

from counterpress.config import PROCESSED_DIR, TABLES_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def compute_group_stats(df: pd.DataFrame, group_col: str, group_name: str, outcome_col: str, outcome_label: str) -> pd.DataFrame:
    grouped = df.groupby(group_col, observed=True).agg(
        N=(outcome_col, "count"),
        outcome_count=(outcome_col, "sum"),
        outcome_rate=(outcome_col, "mean"),
    ).reset_index()
    grouped.rename(columns={group_col: "bin_or_category"}, inplace=True)
    grouped["grouping_variable"] = group_name
    grouped["outcome"] = outcome_label
    grouped["outcome_rate"] = grouped["outcome_rate"].round(4)
    return grouped[["grouping_variable", "bin_or_category", "outcome", "N", "outcome_count", "outcome_rate"]]


def generate_descriptive_tables():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    out_path = TABLES_DIR / "descriptive_outcome_tables.csv"

    logger.info(f"Loading features from {parquet_path}...")
    df = pd.read_parquet(parquet_path)

    tables = []

    # 1. Regain by numerical_advantage_5 (clamped to [-3, +2] for stability)
    df["num_adv_5_binned"] = df["numerical_advantage_5"].clip(lower=-3, upper=2).astype(str)
    df.loc[df["numerical_advantage_5"] <= -3, "num_adv_5_binned"] = "<= -3"
    df.loc[df["numerical_advantage_5"] >= 2, "num_adv_5_binned"] = ">= +2"
    tables.append(compute_group_stats(df, "num_adv_5_binned", "numerical_advantage_5", "regain_5s_controlled", "regain_5s"))

    # 2. Regain by numerical_advantage_10 (clamped to [-4, +3])
    df["num_adv_10_binned"] = df["numerical_advantage_10"].clip(lower=-4, upper=3).astype(str)
    df.loc[df["numerical_advantage_10"] <= -4, "num_adv_10_binned"] = "<= -4"
    df.loc[df["numerical_advantage_10"] >= 3, "num_adv_10_binned"] = ">= +3"
    tables.append(compute_group_stats(df, "num_adv_10_binned", "numerical_advantage_10", "regain_5s_controlled", "regain_5s"))

    # 3. Regain by nearest teammate distance quintiles
    valid_tm = df["nearest_teammate_distance"].dropna()
    df["teammate_dist_quintile"] = pd.qcut(valid_tm, q=5, labels=["Q1 (Closest)", "Q2", "Q3", "Q4", "Q5 (Furthest)"])
    tables.append(compute_group_stats(df, "teammate_dist_quintile", "nearest_teammate_distance_quintile", "regain_5s_controlled", "regain_5s"))

    # 4. Regain by nearest opponent distance quintiles
    valid_opp = df["nearest_opponent_distance"].dropna()
    df["opponent_dist_quintile"] = pd.qcut(valid_opp, q=5, labels=["Q1 (Closest)", "Q2", "Q3", "Q4", "Q5 (Furthest)"])
    tables.append(compute_group_stats(df, "opponent_dist_quintile", "nearest_opponent_distance_quintile", "regain_5s_controlled", "regain_5s"))

    # 5. Regain by Pitch Third (initiation_x: [0, 40) Def, [40, 80) Mid, [80, 120] Att)
    df["pitch_third"] = pd.cut(df["initiation_x"], bins=[0, 40, 80, 120], labels=["Defensive Third", "Middle Third", "Attacking Third"])
    tables.append(compute_group_stats(df, "pitch_third", "pitch_third", "regain_5s_controlled", "regain_5s"))

    # 6. Regain by Lateral Zone (distance_to_nearest_touchline: [0, 15] Wide, >15 Central)
    df["lateral_zone"] = np.where(df["distance_to_nearest_touchline"] <= 15.0, "Wide (<15u to line)", "Central (>=15u to line)")
    tables.append(compute_group_stats(df, "lateral_zone", "lateral_zone", "regain_5s_controlled", "regain_5s"))

    # 7. Dangerous Escape by Forward Numerical Advantage (clamped to [-4, +3])
    df["fwd_adv_binned"] = df["forward_numerical_advantage"].clip(lower=-4, upper=3).astype(str)
    df.loc[df["forward_numerical_advantage"] <= -4, "fwd_adv_binned"] = "<= -4"
    df.loc[df["forward_numerical_advantage"] >= 3, "fwd_adv_binned"] = ">= +3"
    tables.append(compute_group_stats(df, "fwd_adv_binned", "forward_numerical_advantage", "dangerous_escape_15s", "dangerous_escape_15s"))

    # 8. Dangerous Escape by Escape Corridor Advantage (clamped to [-2, +2])
    # Definition: opponents_in_corridor - defenders_in_corridor
    # Positive = Opponent / Escaping Surplus; Negative = Pressing Defensive Surplus
    df["corridor_adv_binned"] = df["escape_corridor_advantage_20"].clip(lower=-2, upper=2).astype(str)
    df.loc[df["escape_corridor_advantage_20"] <= -2, "corridor_adv_binned"] = "<= -2 (Defensive Surplus)"
    df.loc[df["escape_corridor_advantage_20"] == 0, "corridor_adv_binned"] = "0 (Parity)"
    df.loc[df["escape_corridor_advantage_20"] >= 2, "corridor_adv_binned"] = ">= +2 (Opponent Surplus)"
    tables.append(compute_group_stats(df, "corridor_adv_binned", "escape_corridor_advantage_20", "dangerous_escape_15s", "dangerous_escape_15s"))

    # 9. Dangerous Escape by Pitch Third
    tables.append(compute_group_stats(df, "pitch_third", "pitch_third", "dangerous_escape_15s", "dangerous_escape_15s"))

    # 10. Dangerous Escape by Touchline Distance Bins ([0, 10), [10, 20), [20, 40])
    df["touchline_dist_bin"] = pd.cut(df["distance_to_nearest_touchline"], bins=[0, 10, 20, 40], labels=["Touchline (0-10u)", "Half-Space (10-20u)", "Central (20-40u)"])
    tables.append(compute_group_stats(df, "touchline_dist_bin", "distance_to_nearest_touchline", "dangerous_escape_15s", "dangerous_escape_15s"))

    final_df = pd.concat(tables, ignore_index=True)
    final_df.to_csv(out_path, index=False)
    logger.info(f"Saved descriptive outcome tables to {out_path} ({len(final_df)} rows).")
    print(final_df.to_string(index=False))


if __name__ == "__main__":
    generate_descriptive_tables()
