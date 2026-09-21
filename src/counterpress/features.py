"""Feature engineering pipeline for counterpress spatial freeze-frame analysis.

Extracts:
1. Reference location & Actor QA (initiation_x, initiation_y, actor_distance_from_event, anomalous flag)
2. Raw frame & visibility features (player counts, clipped visible area polygon area & pitch fraction)
3. Camera-coverage features at r = 5, 10, 15 (clipped to pitch boundary, denominator physically on pitch)
4. Local team support (visible teammates within 5, 10, 15; nearest 1st, 2nd, 3rd teammate distances - actor EXCLUDED)
5. Local opposition (visible opponents within 5, 10, 15; nearest 1st, 2nd, 3rd opponent distances)
6. Local numerical structure (numerical advantage at 5, 10, 15; total players at 5, 10, 15)
7. Visibility-aware local densities & 80% coverage flags
8. Visible team compactness (x/y std, mean pairwise distance, convex hull area, hull-to-visible ratio)
9. Pitch geometry (touchline distance, goal line distances, lateral centrality, 3-zone, 3x3-zone)
10. Forward escape structure (opponents & defenders ahead of ball, forward numerical advantage, nearest ahead distances)
11. Forward escape corridor (r=20, 30-deg wedge toward goal, corridor advantage, nearest corridor distances, corridor camera coverage)
"""

import logging
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from counterpress.config import PITCH_AREA, PITCH_LENGTH, PITCH_WIDTH, SPATIAL_RADII
from counterpress.spatial import (
    PITCH_BOX,
    build_escape_corridor_polygon,
    clip_polygon_to_pitch,
    compute_circle_coverage,
    compute_compactness,
    compute_corridor_coverage,
    euclidean_distance,
    invert_coordinates,
    invert_polygon,
    point_in_escape_corridor,
)

logger = logging.getLogger(__name__)


def extract_frame_players(
    freeze_frame_data: Optional[Dict[str, Any]],
    event_location: Tuple[float, float],
) -> Dict[str, Any]:
    """Extract and categorize visible players from a 360 freeze frame.

    Identifies the counterpressing actor and strictly excludes the actor from
    teammate support calculations.

    Parameters
    ----------
    freeze_frame_data : dict or None
        StatsBomb 360 freeze frame containing 'freeze_frame' player list and 'visible_area'.
    event_location : tuple of (x, y)
        Initiation event location (x0, y0).

    Returns
    -------
    dict
        Parsed player collections and actor metadata.
    """
    if not freeze_frame_data or "freeze_frame" not in freeze_frame_data:
        return {
            "actor_present": False,
            "actor_loc": None,
            "actor_distance_from_event": np.nan,
            "actor_matching_anomalous": True,
            "teammates_excluding_actor": [],
            "teammates_including_actor": [],
            "opponents": [],
            "goalkeepers": [],
            "frame_player_count": 0,
        }

    players = freeze_frame_data.get("freeze_frame", [])
    actor_candidates = []
    all_teammates = []
    all_opponents = []
    all_keepers = []

    for idx, p in enumerate(players):
        loc = p.get("location")
        if not loc or len(loc) < 2:
            continue
        pt = (float(loc[0]), float(loc[1]))

        if p.get("keeper") is True:
            all_keepers.append(pt)

        if p.get("teammate") is True:
            all_teammates.append((idx, pt, p.get("actor") is True))
        else:
            all_opponents.append(pt)

    # 1. Identify actor
    # Primary: players flagged with actor == True
    flagged_actors = [(idx, pt) for idx, pt, is_actor in all_teammates if is_actor]
    chosen_actor_idx = None
    actor_loc = None
    actor_present = False
    actor_distance = np.nan

    if flagged_actors:
        # Choose the flagged actor closest to event location
        flagged_actors.sort(key=lambda item: euclidean_distance(event_location, item[1]))
        chosen_actor_idx, actor_loc = flagged_actors[0]
        actor_present = True
        actor_distance = euclidean_distance(event_location, actor_loc)
    elif all_teammates:
        # Fallback: find teammate closest to event location
        all_teammates.sort(key=lambda item: euclidean_distance(event_location, item[1]))
        closest_idx, closest_pt, _ = all_teammates[0]
        d = euclidean_distance(event_location, closest_pt)
        if d <= 1.0:
            chosen_actor_idx = closest_idx
            actor_loc = closest_pt
            actor_distance = d
            # actor_present remains False because actor flag was not explicitly present in 360 frame

    # 2. Partition teammates excluding actor
    teammates_excluding_actor = [
        pt for idx, pt, _ in all_teammates if idx != chosen_actor_idx
    ]
    teammates_including_actor = [pt for _, pt, _ in all_teammates]

    # Flag anomalous actor matching (distance > 1.0 or actor completely missing)
    actor_matching_anomalous = bool(
        (not actor_present) or (np.isnan(actor_distance)) or (actor_distance > 1.0)
    )

    return {
        "actor_present": actor_present,
        "actor_loc": actor_loc,
        "actor_distance_from_event": float(actor_distance) if not np.isnan(actor_distance) else np.nan,
        "actor_matching_anomalous": actor_matching_anomalous,
        "teammates_excluding_actor": teammates_excluding_actor,
        "teammates_including_actor": teammates_including_actor,
        "opponents": all_opponents,
        "goalkeepers": all_keepers,
        "frame_player_count": len(players),
    }


def compute_local_counts(
    center: Tuple[float, float],
    points: List[Tuple[float, float]],
    radius: float,
) -> int:
    """Count how many points fall within a Euclidean radius around center."""
    return sum(1 for p in points if euclidean_distance(center, p) <= radius + 1e-7)


def compute_k_nearest_distances(
    center: Tuple[float, float],
    points: List[Tuple[float, float]],
    k: int = 3,
) -> List[Optional[float]]:
    """Compute Euclidean distances to the k nearest points from center.

    Returns a list of length k. If fewer than k points exist, remaining positions are None (NaN).
    Never substitutes zero for missing distances.
    """
    if not points:
        return [None] * k
    dists = sorted([euclidean_distance(center, p) for p in points])
    res: List[Optional[float]] = [float(d) for d in dists[:k]]
    while len(res) < k:
        res.append(None)
    return res


def compute_pitch_zone(x: float, y: float) -> Tuple[str, str]:
    """Compute categorical 3-zone and 3x3-zone strings from counterpressing perspective."""
    if x < 40.0:
        third = "defensive_third"
    elif x < 80.0:
        third = "middle_third"
    else:
        third = "attacking_third"

    # Lateral lane (80 / 3 = 26.667)
    if y < 80.0 / 3.0:
        lane = "left"
    elif y < 160.0 / 3.0:
        lane = "center"
    else:
        lane = "right"

    zone_3x3 = f"{third}_{lane}"
    return third, zone_3x3


def build_spatial_feature_row(
    episode: Dict[str, Any],
    freeze_frame: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Construct complete spatial predictor vector for a single counterpress episode.

    Strict Temporal Leakage Rule:
    Every predictor is calculated exclusively from information available at or before
    the counterpress initiation event. No future outcome information is referenced.

    Parameters
    ----------
    episode : dict
        Episode metadata dictionary from primary cohort.
    freeze_frame : dict or None
        360 freeze frame associated with initiation_event_id.

    Returns
    -------
    dict
        Tabular feature row with exactly defined columns.
    """
    # 1. Reference Location (Initiation Event)
    raw_loc = episode.get("initiation_location")
    if isinstance(raw_loc, str):
        try:
            loc = eval(raw_loc)
            x0, y0 = float(loc[0]), float(loc[1])
        except Exception:
            x0, y0 = float(episode.get("initiation_location_x", 60.0)), float(episode.get("initiation_location_y", 40.0))
    elif isinstance(raw_loc, (list, tuple)) and len(raw_loc) >= 2:
        x0, y0 = float(raw_loc[0]), float(raw_loc[1])
    else:
        x0 = float(episode.get("initiation_location_x", 60.0))
        y0 = float(episode.get("initiation_location_y", 40.0))

    center = (x0, y0)

    # Pitch geometry features (independent of 360 tracking)
    dist_touchline = float(min(y0, PITCH_WIDTH - y0))
    dist_own_goal = float(x0)
    dist_opp_goal = float(PITCH_LENGTH - x0)
    lateral_centrality = float(1.0 - abs(y0 - 40.0) / 40.0)
    pitch_zone, pitch_zone_3x3 = compute_pitch_zone(x0, y0)

    # 2. Extract 360 Players & Actor Identification
    players_meta = extract_frame_players(freeze_frame, center)
    actor_present = players_meta["actor_present"]
    actor_dist = players_meta["actor_distance_from_event"]
    actor_anomalous = players_meta["actor_matching_anomalous"]

    teammates = players_meta["teammates_excluding_actor"]
    opponents = players_meta["opponents"]
    goalkeepers = players_meta["goalkeepers"]

    frame_player_count = players_meta["frame_player_count"]
    visible_team_inc_actor = len(players_meta["teammates_including_actor"])
    visible_team_exc_actor = len(teammates)
    visible_opp_count = len(opponents)
    visible_gk_count = len(goalkeepers)

    # 3. Visible Area Polygon & Quality
    visible_poly = None
    polygon_valid = False
    polygon_missing = True
    vis_area = 0.0
    vis_pitch_frac = 0.0

    if freeze_frame and "visible_area" in freeze_frame:
        raw_coords = freeze_frame.get("visible_area", [])
        if raw_coords and len(raw_coords) >= 6:
            polygon_missing = False
            visible_poly = clip_polygon_to_pitch(raw_coords)
            if visible_poly is not None and not visible_poly.is_empty and visible_poly.area > 1e-6:
                polygon_valid = True
                vis_area = float(visible_poly.area)
                vis_pitch_frac = float(vis_area / PITCH_AREA)

    # 4. Camera-Coverage Features (r = 5, 10, 15)
    vis_loc_5, cov_5 = compute_circle_coverage(center, 5.0, visible_poly)
    vis_loc_10, cov_10 = compute_circle_coverage(center, 10.0, visible_poly)
    vis_loc_15, cov_15 = compute_circle_coverage(center, 15.0, visible_poly)

    cov_5_ge_80 = bool(cov_5 >= 0.80)
    cov_10_ge_80 = bool(cov_10 >= 0.80)
    cov_15_ge_80 = bool(cov_15 >= 0.80)

    # 5. Local Team Support (Actor Strictly Excluded)
    team_within_5 = compute_local_counts(center, teammates, 5.0)
    team_within_10 = compute_local_counts(center, teammates, 10.0)
    team_within_15 = compute_local_counts(center, teammates, 15.0)

    team_dists = compute_k_nearest_distances(center, teammates, k=3)
    nearest_team_d = team_dists[0]
    second_team_d = team_dists[1]
    third_team_d = team_dists[2]

    # 6. Local Opposition
    opp_within_5 = compute_local_counts(center, opponents, 5.0)
    opp_within_10 = compute_local_counts(center, opponents, 10.0)
    opp_within_15 = compute_local_counts(center, opponents, 15.0)

    opp_dists = compute_k_nearest_distances(center, opponents, k=3)
    nearest_opp_d = opp_dists[0]
    second_opp_d = opp_dists[1]
    third_opp_d = opp_dists[2]

    # 7. Local Numerical Structure
    num_adv_5 = team_within_5 - opp_within_5
    num_adv_10 = team_within_10 - opp_within_10
    num_adv_15 = team_within_15 - opp_within_15

    # Total players in circle (supporting teammates + opponents + 1 for the actor if present)
    actor_inc = 1 if actor_present else 0
    total_players_5 = team_within_5 + opp_within_5 + actor_inc
    total_players_10 = team_within_10 + opp_within_10 + actor_inc
    total_players_15 = team_within_15 + opp_within_15 + actor_inc

    # 8. Visibility-Aware Local Densities
    team_dens_5 = float(team_within_5 / vis_loc_5) if vis_loc_5 > 1e-4 else np.nan
    team_dens_10 = float(team_within_10 / vis_loc_10) if vis_loc_10 > 1e-4 else np.nan
    team_dens_15 = float(team_within_15 / vis_loc_15) if vis_loc_15 > 1e-4 else np.nan

    opp_dens_5 = float(opp_within_5 / vis_loc_5) if vis_loc_5 > 1e-4 else np.nan
    opp_dens_10 = float(opp_within_10 / vis_loc_10) if vis_loc_10 > 1e-4 else np.nan
    opp_dens_15 = float(opp_within_15 / vis_loc_15) if vis_loc_15 > 1e-4 else np.nan

    # 9. Visible Team Compactness
    poly_area_arg = vis_area if polygon_valid else None
    team_compact = compute_compactness(teammates, visible_polygon_area=poly_area_arg)
    opp_compact = compute_compactness(opponents, visible_polygon_area=poly_area_arg)

    # 10. Opponent-Attack Coordinate System Transformation
    # x_opp = 120 - x, y_opp = 80 - y
    ball_opp = invert_coordinates(x0, y0)
    opponents_opp = [invert_coordinates(p[0], p[1]) for p in opponents]
    defenders_opp = [invert_coordinates(p[0], p[1]) for p in teammates]

    # Invert visible polygon into opponent coordinates
    visible_poly_opp = invert_polygon(visible_poly) if polygon_valid else None

    # 11. Forward Escape Structure (in opponent coordinates)
    # Opponent attack direction is increasing x_opp
    # Opponents = escaping team players (opponents in 360)
    # Defenders = counterpressing teammates (teammates in 360, actor excluded)
    opp_ahead_pts = [p for p in opponents_opp if p[0] > ball_opp[0]]
    def_ahead_pts = [p for p in defenders_opp if p[0] > ball_opp[0]]

    opp_ahead_count = len(opp_ahead_pts)
    def_ahead_count = len(def_ahead_pts)
    forward_num_adv = opp_ahead_count - def_ahead_count

    nearest_def_ahead_d = (
        min([euclidean_distance(ball_opp, p) for p in def_ahead_pts])
        if def_ahead_pts
        else np.nan
    )
    nearest_opp_ahead_d = (
        min([euclidean_distance(ball_opp, p) for p in opp_ahead_pts])
        if opp_ahead_pts
        else np.nan
    )

    # 12. Forward Escape Corridor (r = 20, 30-deg wedge toward goal (120, 40))
    corridor_poly = build_escape_corridor_polygon(ball_opp, goal_opp=(120.0, 40.0), radius=20.0, half_angle_deg=30.0)

    opp_in_corridor_pts = [p for p in opponents_opp if point_in_escape_corridor(p, ball_opp, (120.0, 40.0), 20.0, 30.0)]
    def_in_corridor_pts = [p for p in defenders_opp if point_in_escape_corridor(p, ball_opp, (120.0, 40.0), 20.0, 30.0)]

    opp_in_corridor_cnt = len(opp_in_corridor_pts)
    def_in_corridor_cnt = len(def_in_corridor_pts)
    corridor_adv = opp_in_corridor_cnt - def_in_corridor_cnt

    nearest_def_corridor_d = (
        min([euclidean_distance(ball_opp, p) for p in def_in_corridor_pts])
        if def_in_corridor_pts
        else np.nan
    )
    nearest_opp_corridor_d = (
        min([euclidean_distance(ball_opp, p) for p in opp_in_corridor_pts])
        if opp_in_corridor_pts
        else np.nan
    )

    _, corridor_cov = compute_corridor_coverage(corridor_poly, visible_poly_opp)

    # 13. Assemble Feature Vector
    return {
        # Cohort Identifiers
        "episode_id": episode.get("episode_id"),
        "match_id": int(episode.get("match_id", 0)),
        "competition": episode.get("competition_name", episode.get("competition")),
        "season": episode.get("season_name", episode.get("season")),
        "counterpressing_team": episode.get("counterpressing_team"),
        "opponent_team": episode.get("possession_team", episode.get("opponent_team")),
        "initiation_event_id": episode.get("initiation_event_id"),

        # Reference Location & Actor QA
        "initiation_x": round(x0, 2),
        "initiation_y": round(y0, 2),
        "actor_present": actor_present,
        "actor_distance_from_event": round(actor_dist, 4) if not np.isnan(actor_dist) else np.nan,
        "actor_matching_anomalous": actor_anomalous,

        # Raw Frame / Visibility Features
        "frame_player_count": frame_player_count,
        "visible_teammate_count_including_actor": visible_team_inc_actor,
        "visible_teammate_count_excluding_actor": visible_team_exc_actor,
        "visible_opponent_count": visible_opp_count,
        "visible_goalkeeper_count": visible_gk_count,
        "visible_area_polygon_area": round(vis_area, 2),
        "visible_area_pitch_fraction": round(vis_pitch_frac, 4),
        "polygon_valid": polygon_valid,
        "polygon_missing": polygon_missing,

        # Camera-Coverage Features
        "coverage_5": round(cov_5, 4),
        "coverage_10": round(cov_10, 4),
        "coverage_15": round(cov_15, 4),
        "visible_local_area_5": round(vis_loc_5, 2),
        "visible_local_area_10": round(vis_loc_10, 2),
        "visible_local_area_15": round(vis_loc_15, 2),
        "coverage_5_ge_80pct": cov_5_ge_80,
        "coverage_10_ge_80pct": cov_10_ge_80,
        "coverage_15_ge_80pct": cov_15_ge_80,

        # Local Team Support (Actor Strictly Excluded)
        "visible_teammates_within_5": team_within_5,
        "visible_teammates_within_10": team_within_10,
        "visible_teammates_within_15": team_within_15,
        "nearest_teammate_distance": round(nearest_team_d, 2) if nearest_team_d is not None else np.nan,
        "second_nearest_teammate_distance": round(second_team_d, 2) if second_team_d is not None else np.nan,
        "third_nearest_teammate_distance": round(third_team_d, 2) if third_team_d is not None else np.nan,

        # Local Opposition
        "visible_opponents_within_5": opp_within_5,
        "visible_opponents_within_10": opp_within_10,
        "visible_opponents_within_15": opp_within_15,
        "nearest_opponent_distance": round(nearest_opp_d, 2) if nearest_opp_d is not None else np.nan,
        "second_nearest_opponent_distance": round(second_opp_d, 2) if second_opp_d is not None else np.nan,
        "third_nearest_opponent_distance": round(third_opp_d, 2) if third_opp_d is not None else np.nan,

        # Local Numerical Structure
        "numerical_advantage_5": num_adv_5,
        "numerical_advantage_10": num_adv_10,
        "numerical_advantage_15": num_adv_15,
        "total_players_within_5": total_players_5,
        "total_players_within_10": total_players_10,
        "total_players_within_15": total_players_15,

        # Visibility-Aware Local Density
        "teammate_density_visible_5": round(team_dens_5, 5) if not np.isnan(team_dens_5) else np.nan,
        "teammate_density_visible_10": round(team_dens_10, 5) if not np.isnan(team_dens_10) else np.nan,
        "teammate_density_visible_15": round(team_dens_15, 5) if not np.isnan(team_dens_15) else np.nan,
        "opponent_density_visible_5": round(opp_dens_5, 5) if not np.isnan(opp_dens_5) else np.nan,
        "opponent_density_visible_10": round(opp_dens_10, 5) if not np.isnan(opp_dens_10) else np.nan,
        "opponent_density_visible_15": round(opp_dens_15, 5) if not np.isnan(opp_dens_15) else np.nan,

        # Visible Team Compactness
        "teammate_x_std": round(team_compact["x_std"], 2) if team_compact["x_std"] is not None else np.nan,
        "teammate_y_std": round(team_compact["y_std"], 2) if team_compact["y_std"] is not None else np.nan,
        "opponent_x_std": round(opp_compact["x_std"], 2) if opp_compact["x_std"] is not None else np.nan,
        "opponent_y_std": round(opp_compact["y_std"], 2) if opp_compact["y_std"] is not None else np.nan,
        "teammate_mean_pairwise_distance": round(team_compact["mean_pairwise_distance"], 2) if team_compact["mean_pairwise_distance"] is not None else np.nan,
        "opponent_mean_pairwise_distance": round(opp_compact["mean_pairwise_distance"], 2) if opp_compact["mean_pairwise_distance"] is not None else np.nan,
        "teammate_hull_area": round(team_compact["hull_area"], 2) if team_compact["hull_area"] is not None else np.nan,
        "opponent_hull_area": round(opp_compact["hull_area"], 2) if opp_compact["hull_area"] is not None else np.nan,
        "teammate_hull_visible_area_ratio": round(team_compact["hull_visible_area_ratio"], 4) if team_compact["hull_visible_area_ratio"] is not None else np.nan,
        "opponent_hull_visible_area_ratio": round(opp_compact["hull_visible_area_ratio"], 4) if opp_compact["hull_visible_area_ratio"] is not None else np.nan,

        # Pitch Geometry Features
        "distance_to_nearest_touchline": round(dist_touchline, 2),
        "distance_to_own_goal_line": round(dist_own_goal, 2),
        "distance_to_opponent_goal_line": round(dist_opp_goal, 2),
        "lateral_centrality": round(lateral_centrality, 4),
        "pitch_zone": pitch_zone,
        "pitch_zone_3x3": pitch_zone_3x3,

        # Forward Escape Structure (in opponent coordinates)
        "opponents_ahead_of_ball": opp_ahead_count,
        "defenders_ahead_of_ball": def_ahead_count,
        "forward_numerical_advantage": forward_num_adv,
        "nearest_defender_ahead_distance": round(nearest_def_ahead_d, 2) if not np.isnan(nearest_def_ahead_d) else np.nan,
        "nearest_opponent_ahead_distance": round(nearest_opp_ahead_d, 2) if not np.isnan(nearest_opp_ahead_d) else np.nan,

        # Forward Escape Corridor (r = 20, 30-deg wedge)
        "opponents_in_escape_corridor_20": opp_in_corridor_cnt,
        "defenders_in_escape_corridor_20": def_in_corridor_cnt,
        "escape_corridor_advantage_20": corridor_adv,
        "nearest_defender_in_escape_corridor": round(nearest_def_corridor_d, 2) if not np.isnan(nearest_def_corridor_d) else np.nan,
        "nearest_opponent_in_escape_corridor": round(nearest_opp_corridor_d, 2) if not np.isnan(nearest_opp_corridor_d) else np.nan,
        "escape_corridor_coverage_20": round(corridor_cov, 4),

        # Frozen Outcome Labels (attached for downstream convenience, strictly not used in feature computation)
        "regain_5s_controlled": episode.get("regain_5s_controlled"),
        "dangerous_escape_15s": episode.get("dangerous_escape_15s"),
        "episode_outcome_3class": episode.get("episode_outcome_3class"),
    }
