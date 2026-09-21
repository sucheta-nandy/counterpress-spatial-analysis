"""Define and document pre-specified feature families for Iteration 4 modeling.

Enforces:
- Separation into 5 explicit families (A: Context, B: Local Pressure, C: Compactness, D: Forward Structure, E: Observability Controls).
- Elimination of redundant or raw intermediate columns.
- Clear specification of column roles and transformations.
- Output: results/tables/model_feature_sets.csv
"""

import pandas as pd
from counterpress.config import TABLES_DIR

FEATURE_FAMILIES_DEF = [
    # Family A: Context / Location Baseline
    {"feature": "initiation_x", "family": "A_context", "type": "continuous", "role": "predictor", "description": "X coordinate of initiation location on 120x80 pitch"},
    {"feature": "initiation_y", "family": "A_context", "type": "continuous", "role": "predictor", "description": "Y coordinate of initiation location on 120x80 pitch"},
    {"feature": "distance_to_nearest_touchline", "family": "A_context", "type": "continuous", "role": "predictor", "description": "Distance to closest touchline (min(y, 80-y))"},
    {"feature": "lateral_centrality", "family": "A_context", "type": "continuous", "role": "predictor", "description": "Distance from pitch center line (abs(y - 40))"},
    {"feature": "pitch_zone_3x3", "family": "A_context", "type": "categorical", "role": "predictor", "description": "3x3 spatial pitch zone (e.g. attacking_third_center)"},
    {"feature": "initiation_event_type", "family": "A_context", "type": "categorical", "role": "predictor", "description": "Event type initiating counterpress (e.g. Pressure, Duel)"},
    {"feature": "competition", "family": "A_context", "type": "categorical", "role": "predictor", "description": "Competition name (e.g. FIFA World Cup)"},
    {"feature": "period", "family": "A_context", "type": "categorical", "role": "predictor", "description": "Match period (1, 2, 3, 4)"},

    # Family B: Local Pressure Geometry
    {"feature": "visible_teammates_within_5", "family": "B_local_pressure", "type": "count", "role": "predictor", "description": "Visible teammates within 5 units (excluding actor)"},
    {"feature": "visible_opponents_within_5", "family": "B_local_pressure", "type": "count", "role": "predictor", "description": "Visible opponents within 5 units"},
    {"feature": "numerical_advantage_5", "family": "B_local_pressure", "type": "integer", "role": "predictor", "description": "Local numerical advantage at 5 units (teammates - opponents)"},
    {"feature": "visible_teammates_within_10", "family": "B_local_pressure", "type": "count", "role": "predictor", "description": "Visible teammates within 10 units (excluding actor)"},
    {"feature": "visible_opponents_within_10", "family": "B_local_pressure", "type": "count", "role": "predictor", "description": "Visible opponents within 10 units"},
    {"feature": "numerical_advantage_10", "family": "B_local_pressure", "type": "integer", "role": "predictor", "description": "Local numerical advantage at 10 units (teammates - opponents)"},
    {"feature": "nearest_teammate_distance", "family": "B_local_pressure", "type": "continuous", "role": "predictor", "description": "Euclidean distance to closest teammate (excluding actor)"},
    {"feature": "second_nearest_teammate_distance", "family": "B_local_pressure", "type": "continuous", "role": "predictor", "description": "Euclidean distance to 2nd closest teammate"},
    {"feature": "nearest_opponent_distance", "family": "B_local_pressure", "type": "continuous", "role": "predictor", "description": "Euclidean distance to closest opponent"},
    {"feature": "second_nearest_opponent_distance", "family": "B_local_pressure", "type": "continuous", "role": "predictor", "description": "Euclidean distance to 2nd closest opponent"},

    # Family C: Broader Compactness
    {"feature": "numerical_advantage_15", "family": "C_compactness", "type": "integer", "role": "predictor", "description": "Local numerical advantage at 15 units (teammates - opponents)"},
    {"feature": "teammate_mean_pairwise_distance", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Mean pairwise distance between teammates (dispersion)"},
    {"feature": "opponent_mean_pairwise_distance", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Mean pairwise distance between opponents"},
    {"feature": "teammate_hull_area", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Convex hull area of teammates (NaN if <3 players)"},
    {"feature": "opponent_hull_area", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Convex hull area of opponents (NaN if <3 players)"},
    {"feature": "teammate_x_std", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Standard deviation of teammate X coordinates"},
    {"feature": "teammate_y_std", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Standard deviation of teammate Y coordinates"},
    {"feature": "opponent_x_std", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Standard deviation of opponent X coordinates"},
    {"feature": "opponent_y_std", "family": "C_compactness", "type": "continuous", "role": "predictor", "description": "Standard deviation of opponent Y coordinates"},

    # Family D: Forward Escape Structure
    {"feature": "opponents_ahead_of_ball", "family": "D_forward_structure", "type": "count", "role": "predictor", "description": "Opponents positioned ahead of ball toward their attack goal"},
    {"feature": "defenders_ahead_of_ball", "family": "D_forward_structure", "type": "count", "role": "predictor", "description": "Defenders (pressing teammates) positioned behind ball defending own goal"},
    {"feature": "forward_numerical_advantage", "family": "D_forward_structure", "type": "integer", "role": "predictor", "description": "Forward advantage (defenders ahead - opponents ahead)"},
    {"feature": "nearest_defender_ahead_distance", "family": "D_forward_structure", "type": "continuous", "role": "predictor", "description": "Distance to nearest defender ahead of ball"},
    {"feature": "nearest_opponent_ahead_distance", "family": "D_forward_structure", "type": "continuous", "role": "predictor", "description": "Distance to nearest opponent ahead of ball"},
    {"feature": "opponents_in_escape_corridor_20", "family": "D_forward_structure", "type": "count", "role": "predictor", "description": "Opponents in 20-unit forward escape corridor"},
    {"feature": "defenders_in_escape_corridor_20", "family": "D_forward_structure", "type": "count", "role": "predictor", "description": "Defenders in 20-unit forward escape corridor"},
    {"feature": "escape_corridor_advantage_20", "family": "D_forward_structure", "type": "integer", "role": "predictor", "description": "Corridor advantage (defenders - opponents in corridor)"},

    # Family E: Observability Controls
    {"feature": "coverage_5", "family": "E_observability", "type": "continuous", "role": "control", "description": "Fraction of 5-unit on-pitch circle inside 360 visible polygon"},
    {"feature": "coverage_10", "family": "E_observability", "type": "continuous", "role": "control", "description": "Fraction of 10-unit on-pitch circle inside 360 visible polygon"},
    {"feature": "coverage_15", "family": "E_observability", "type": "continuous", "role": "control", "description": "Fraction of 15-unit on-pitch circle inside 360 visible polygon"},
    {"feature": "escape_corridor_coverage_20", "family": "E_observability", "type": "continuous", "role": "control", "description": "Fraction of 20-unit corridor inside 360 visible polygon"},
    {"feature": "visible_area_pitch_fraction", "family": "E_observability", "type": "continuous", "role": "control", "description": "Fraction of entire pitch visible in 360 polygon"},
    {"feature": "frame_player_count", "family": "E_observability", "type": "count", "role": "control", "description": "Total players detected in freeze frame"},
    {"feature": "actor_matching_anomalous", "family": "E_observability", "type": "boolean", "role": "control", "description": "Actor-event location discrepancy flag (robustness control)"},
]


def setup_feature_sets():
    df_sets = pd.DataFrame(FEATURE_FAMILIES_DEF)
    out_path = TABLES_DIR / "model_feature_sets.csv"
    df_sets.to_csv(out_path, index=False)
    print(f"Saved feature sets definition to {out_path} ({len(df_sets)} features across {df_sets['family'].nunique()} families).")
    print(df_sets["family"].value_counts().sort_index())


if __name__ == "__main__":
    setup_feature_sets()
