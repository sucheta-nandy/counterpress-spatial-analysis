"""Spatial and geometric calculations for StatsBomb 360 freeze frames.

Provides robust, vectorized, and Shapely-based geometric operations:
- 2D Euclidean distance and k-nearest neighbor search
- Pitch-clipping for visible area polygons (120 x 80 legal pitch)
- Exact pitch-intersected circle areas and camera coverage fractions
- Coordinate transformation between attacking frames (x_opp = 120 - x, y_opp = 80 - y)
- Forward escape wedge corridors (radius 20, 30 deg half-angle to goal center)
- Convex hull and compactness metrics for partially observed player configurations
"""

import math
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
from shapely.geometry import MultiPoint, Point, Polygon, box
from shapely.geometry.polygon import orient

from counterpress.config import PITCH_LENGTH, PITCH_WIDTH

# Legal pitch bounding box (120 x 80 StatsBomb coordinate units)
PITCH_BOX = box(0.0, 0.0, PITCH_LENGTH, PITCH_WIDTH)
PITCH_AREA = PITCH_LENGTH * PITCH_WIDTH  # 9600.0


def euclidean_distance(p1: Sequence[float], p2: Sequence[float]) -> float:
    """Calculate 2D Euclidean distance between two points in StatsBomb coordinate units."""
    return float(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))


def invert_coordinates(x: float, y: float) -> Tuple[float, float]:
    """Invert pitch coordinates between opposing attacking perspectives.

    In StatsBomb coordinates:
    x_opp = 120.0 - x
    y_opp = 80.0 - y
    """
    return PITCH_LENGTH - float(x), PITCH_WIDTH - float(y)


def invert_polygon(poly: Optional[Polygon]) -> Optional[Polygon]:
    """Invert a Polygon into the opposing attacking coordinate system.

    Maintains valid winding order (CCW).
    """
    if poly is None or poly.is_empty or not poly.is_valid:
        return None
    try:
        inv_coords = [invert_coordinates(x, y) for x, y in poly.exterior.coords]
        inv_poly = orient(Polygon(inv_coords), sign=1.0)
        if not inv_poly.is_valid:
            inv_poly = inv_poly.buffer(0)
        return inv_poly
    except Exception:
        return None


def clip_polygon_to_pitch(visible_coords: Sequence[float]) -> Optional[Polygon]:
    """Clip a flat sequence of visible area polygon coordinates to the legal 120x80 pitch.

    Parameters
    ----------
    visible_coords : sequence of float
        Flat coordinate sequence [x0, y0, x1, y1, ..., xk, yk].

    Returns
    -------
    Polygon or None
        Clipped Shapely Polygon, or None if malformed or degenerate.
    """
    if not visible_coords or len(visible_coords) < 6:
        return None
    try:
        pts = np.array(visible_coords, dtype=float).reshape(-1, 2)
        poly = Polygon(pts)
        if not poly.is_valid:
            poly = poly.buffer(0)
        clipped = poly.intersection(PITCH_BOX)
        if not clipped.is_valid or clipped.is_empty or clipped.area <= 1e-6:
            return None
        return clipped
    except Exception:
        return None


def compute_circle_pitch_area(center: Tuple[float, float], radius: float) -> float:
    """Compute the area of a circle centered at `center` that lies physically on the pitch.

    Parameters
    ----------
    center : tuple of (x, y)
    radius : float

    Returns
    -------
    float
        Area in square StatsBomb coordinate units (clipped to pitch boundary).
    """
    circ = Point(center).buffer(radius, quad_segs=32)
    circ_pitch = circ.intersection(PITCH_BOX)
    return float(circ_pitch.area)


def compute_circle_coverage(
    center: Tuple[float, float],
    radius: float,
    visible_poly: Optional[Polygon],
) -> Tuple[float, float]:
    """Compute visible local area and camera coverage fraction for a circle around center.

    Coverage is defined as:
    Area(VisiblePolygon ∩ Pitch ∩ Circle_r) / Area(Pitch ∩ Circle_r)

    The denominator is strictly the portion of the circle physically on the pitch,
    ensuring touchline and goal-line circles are not penalized for out-of-bounds space.

    Parameters
    ----------
    center : tuple of (x, y)
    radius : float
    visible_poly : Polygon or None
        Clipped visible area polygon.

    Returns
    -------
    tuple of (visible_local_area, coverage_fraction)
        Both bounded and >= 0.0, coverage in [0.0, 1.0].
    """
    circ = Point(center).buffer(radius, quad_segs=32)
    local_pitch_circ = circ.intersection(PITCH_BOX)
    local_pitch_area = float(local_pitch_circ.area)

    if local_pitch_area <= 1e-6:
        return 0.0, 0.0

    if visible_poly is None or visible_poly.is_empty or not visible_poly.is_valid or visible_poly.area <= 1e-6:
        return 0.0, 0.0

    vis_local = local_pitch_circ.intersection(visible_poly)
    vis_area = float(vis_local.area)
    cov = float(min(1.0, max(0.0, vis_area / local_pitch_area)))
    return vis_area, cov


def compute_convex_hull_area(points: List[Tuple[float, float]]) -> Optional[float]:
    """Compute area of the 2D convex hull formed by a set of points.

    Rule: Requires at least 3 non-collinear points. Otherwise returns None (NaN).
    Never returns an arbitrary zero for an undefined hull.

    Parameters
    ----------
    points : list of tuple of (x, y)

    Returns
    -------
    float or None
    """
    if not points or len(points) < 3:
        return None
    try:
        hull = MultiPoint(points).convex_hull
        if isinstance(hull, Polygon) and hull.area > 1e-6:
            return float(hull.area)
        return None
    except Exception:
        return None


def compute_mean_pairwise_distance(points: List[Tuple[float, float]]) -> Optional[float]:
    """Compute average Euclidean distance between all distinct pairs of points.

    Requires at least 2 points; returns None otherwise.
    """
    if not points or len(points) < 2:
        return None
    n = len(points)
    total_dist = 0.0
    count = 0
    for i in range(n):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]
            total_dist += math.hypot(p1[0] - p2[0], p1[1] - p2[1])
            count += 1
    return float(total_dist / count) if count > 0 else None


def compute_compactness(
    points: List[Tuple[float, float]],
    visible_polygon_area: Optional[float] = None,
) -> Dict[str, Optional[float]]:
    """Compute visible compactness metrics for a group of players.

    Returns
    -------
    dict with keys:
        x_std, y_std, mean_pairwise_distance, hull_area, hull_visible_area_ratio
    """
    if not points or len(points) < 2:
        return {
            "x_std": None,
            "y_std": None,
            "mean_pairwise_distance": None,
            "hull_area": None,
            "hull_visible_area_ratio": None,
        }

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    # Population standard deviation (ddof=0)
    x_std = float(np.std(xs, ddof=0))
    y_std = float(np.std(ys, ddof=0))

    mean_pair = compute_mean_pairwise_distance(points)
    hull_a = compute_convex_hull_area(points)

    ratio = None
    if hull_a is not None and visible_polygon_area is not None and visible_polygon_area > 1e-6:
        ratio = float(hull_a / visible_polygon_area)

    return {
        "x_std": x_std,
        "y_std": y_std,
        "mean_pairwise_distance": mean_pair,
        "hull_area": hull_a,
        "hull_visible_area_ratio": ratio,
    }


def build_escape_corridor_polygon(
    ball_opp: Tuple[float, float],
    goal_opp: Tuple[float, float] = (120.0, 40.0),
    radius: float = 20.0,
    half_angle_deg: float = 30.0,
    num_arc_pts: int = 32,
) -> Polygon:
    """Construct forward escape corridor wedge originating from the ball toward goal center.

    In opponent-oriented coordinates:
    - Origin: ball location (x0_opp, y0_opp)
    - Direction: toward opponent attacking goal center (120.0, 40.0)
    - Radius: 20 StatsBomb coordinate units
    - Angular half-width: 30 degrees (full cone angle 60 degrees)

    Parameters
    ----------
    ball_opp : tuple of (x, y)
        Ball position in opponent-oriented coordinates.
    goal_opp : tuple of (x, y), default (120.0, 40.0)
    radius : float, default 20.0
    half_angle_deg : float, default 30.0
    num_arc_pts : int, default 32

    Returns
    -------
    Polygon
        Closed wedge polygon in opponent-oriented coordinates.
    """
    x0, y0 = ball_opp
    gx, gy = goal_opp
    theta_goal = math.atan2(gy - y0, gx - x0)
    half_angle_rad = math.radians(half_angle_deg)

    start_ang = theta_goal - half_angle_rad
    end_ang = theta_goal + half_angle_rad

    arc_pts = []
    for i in range(num_arc_pts):
        ang = start_ang + (end_ang - start_ang) * (i / (num_arc_pts - 1))
        arc_pts.append((x0 + radius * math.cos(ang), y0 + radius * math.sin(ang)))

    poly_pts = [(x0, y0)] + arc_pts + [(x0, y0)]
    poly = orient(Polygon(poly_pts), sign=1.0)
    if not poly.is_valid:
        poly = poly.buffer(0)
    return poly


def point_in_escape_corridor(
    pt_opp: Tuple[float, float],
    ball_opp: Tuple[float, float],
    goal_opp: Tuple[float, float] = (120.0, 40.0),
    radius: float = 20.0,
    half_angle_deg: float = 30.0,
) -> bool:
    """Test whether a player location in opponent-oriented coordinates falls inside the forward escape wedge.

    Uses exact distance and angular sector checking with boundary inclusion.
    """
    x0, y0 = ball_opp
    px, py = pt_opp
    gx, gy = goal_opp

    dist = math.hypot(px - x0, py - y0)
    if dist > radius + 1e-7:
        return False
    if dist <= 1e-7:
        return True

    theta_goal = math.atan2(gy - y0, gx - x0)
    theta_pt = math.atan2(py - y0, px - x0)

    diff = (theta_pt - theta_goal + math.pi) % (2.0 * math.pi) - math.pi
    return bool(abs(diff) <= math.radians(half_angle_deg) + 1e-7)


def compute_corridor_coverage(
    corridor_poly: Polygon,
    visible_poly_opp: Optional[Polygon],
) -> Tuple[float, float]:
    """Compute camera visibility coverage of the forward escape corridor on the pitch.

    Coverage is defined as:
    Area(EscapeCorridor ∩ VisiblePolygon_opp ∩ Pitch) / Area(EscapeCorridor ∩ Pitch)

    Parameters
    ----------
    corridor_poly : Polygon
        Escape corridor wedge polygon in opponent coordinates.
    visible_poly_opp : Polygon or None
        Visible area polygon inverted into opponent coordinates.

    Returns
    -------
    tuple of (visible_corridor_area, coverage_fraction)
        Both bounded and >= 0.0, coverage in [0.0, 1.0].
    """
    corridor_pitch = corridor_poly.intersection(PITCH_BOX)
    corridor_pitch_area = float(corridor_pitch.area)

    if corridor_pitch_area <= 1e-6:
        return 0.0, 0.0

    if visible_poly_opp is None or visible_poly_opp.is_empty or not visible_poly_opp.is_valid or visible_poly_opp.area <= 1e-6:
        return 0.0, 0.0

    vis_corridor = corridor_pitch.intersection(visible_poly_opp)
    vis_area = float(vis_corridor.area)
    cov = float(min(1.0, max(0.0, vis_area / corridor_pitch_area)))
    return vis_area, cov
