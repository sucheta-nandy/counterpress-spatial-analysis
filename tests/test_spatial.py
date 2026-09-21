"""Unit tests for spatial and geometric calculations in StatsBomb 360 analysis."""

import math
import pytest
from shapely.geometry import Point, Polygon, box

from counterpress.spatial import (
    PITCH_AREA,
    PITCH_BOX,
    build_escape_corridor_polygon,
    clip_polygon_to_pitch,
    compute_circle_coverage,
    compute_circle_pitch_area,
    compute_compactness,
    compute_convex_hull_area,
    compute_corridor_coverage,
    compute_mean_pairwise_distance,
    euclidean_distance,
    invert_coordinates,
    invert_polygon,
    point_in_escape_corridor,
)


def test_euclidean_distance():
    assert euclidean_distance((0, 0), (3, 4)) == 5.0
    assert euclidean_distance((10, 20), (10, 20)) == 0.0
    assert euclidean_distance((0, 0), (0, 10)) == 10.0


def test_invert_coordinates_roundtrip():
    """Test coordinate transformation: x_opp = 120 - x, y_opp = 80 - y."""
    x, y = 30.0, 25.0
    inv_x, inv_y = invert_coordinates(x, y)
    assert inv_x == 90.0
    assert inv_y == 55.0

    # Double inversion returns original coordinates exactly
    orig_x, orig_y = invert_coordinates(inv_x, inv_y)
    assert orig_x == pytest.approx(x)
    assert orig_y == pytest.approx(y)

    # Center of pitch is invariant under inversion
    cx, cy = invert_coordinates(60.0, 40.0)
    assert cx == 60.0
    assert cy == 40.0


def test_invert_polygon():
    """Inverting a polygon preserves its area and geometric validity."""
    poly = box(10.0, 10.0, 30.0, 40.0)
    inv_poly = invert_polygon(poly)
    assert inv_poly is not None
    assert inv_poly.is_valid
    assert inv_poly.area == pytest.approx(poly.area)

    # Inverting None returns None
    assert invert_polygon(None) is None


def test_clip_polygon_to_pitch():
    """Visible area polygon must be clipped to legal 120x80 pitch."""
    # Polygon extending outside pitch boundary: [-10, -10] to [130, 90]
    coords = [-10.0, -10.0, 130.0, -10.0, 130.0, 90.0, -10.0, 90.0]
    clipped = clip_polygon_to_pitch(coords)
    assert clipped is not None
    assert clipped.is_valid
    assert clipped.area == pytest.approx(PITCH_AREA)  # Exactly 9600.0

    # Polygon entirely within pitch
    inner_coords = [10.0, 10.0, 30.0, 10.0, 30.0, 40.0, 10.0, 40.0]
    clipped_inner = clip_polygon_to_pitch(inner_coords)
    assert clipped_inner is not None
    assert clipped_inner.area == pytest.approx(600.0)

    # Malformed / empty coordinates
    assert clip_polygon_to_pitch([]) is None
    assert clip_polygon_to_pitch([1.0, 2.0]) is None


def test_circle_clipped_to_pitch_near_touchline():
    """Circle clipped to pitch near touchline must have denominator equal to on-pitch area,
    strictly less than full circle area pi * r^2.
    """
    center_touchline = (60.0, 0.0)
    radius = 10.0

    on_pitch_area = compute_circle_pitch_area(center_touchline, radius)
    full_circle_area = math.pi * (radius ** 2)

    # Semicircle on pitch
    assert on_pitch_area < full_circle_area
    assert on_pitch_area == pytest.approx(full_circle_area / 2.0, rel=1e-2)

    # Corner case: (0, 0) quarter-circle
    corner_area = compute_circle_pitch_area((0.0, 0.0), radius)
    assert corner_area == pytest.approx(full_circle_area / 4.0, rel=1e-2)


def test_circle_coverage_fully_visible():
    """Fully visible circle must have coverage approximately 1.0."""
    center = (60.0, 40.0)
    vis_full = PITCH_BOX

    vis_area, cov = compute_circle_coverage(center, radius=10.0, visible_poly=vis_full)
    assert cov == pytest.approx(1.0, rel=1e-3)
    assert vis_area == pytest.approx(math.pi * 100.0, rel=1e-2)

    # At touchline, if visible polygon covers pitch, coverage is still 1.0
    vis_area_t, cov_t = compute_circle_coverage((60.0, 0.0), radius=10.0, visible_poly=vis_full)
    assert cov_t == pytest.approx(1.0, rel=1e-3)
    assert vis_area_t == pytest.approx((math.pi * 100.0) / 2.0, rel=1e-2)


def test_circle_coverage_partially_visible():
    """Partially visible circle must have coverage between 0 and 1."""
    center = (60.0, 40.0)
    # Visible area covers left half of pitch (x <= 60)
    vis_half = box(0.0, 0.0, 60.0, 80.0)

    vis_area, cov = compute_circle_coverage(center, radius=10.0, visible_poly=vis_half)
    assert 0.0 < cov < 1.0
    assert cov == pytest.approx(0.5, rel=1e-2)


def test_circle_coverage_bounds():
    """Coverage fraction must always be strictly within [0.0, 1.0]."""
    center = (20.0, 20.0)
    # None polygon -> 0 coverage
    assert compute_circle_coverage(center, 10.0, None) == (0.0, 0.0)

    # Empty polygon -> 0 coverage
    assert compute_circle_coverage(center, 10.0, Polygon()) == (0.0, 0.0)

    # Tiny overlap
    tiny_vis = box(25.0, 20.0, 26.0, 21.0)
    _, cov = compute_circle_coverage(center, 10.0, tiny_vis)
    assert 0.0 <= cov <= 1.0


def test_convex_hull_less_than_3_points_nan():
    """Convex hull with <3 points must return None (NaN), never zero."""
    assert compute_convex_hull_area([]) is None
    assert compute_convex_hull_area([(10.0, 20.0)]) is None
    assert compute_convex_hull_area([(10.0, 20.0), (30.0, 40.0)]) is None


def test_convex_hull_collinear_points_nan():
    """Collinear points cannot form a valid 2D hull and must return None (NaN)."""
    collinear = [(10.0, 10.0), (20.0, 20.0), (30.0, 30.0), (40.0, 40.0)]
    assert compute_convex_hull_area(collinear) is None


def test_known_triangle_convex_hull_area():
    """Known right triangle with vertices (0,0), (10,0), (0,10) has area 50.0."""
    pts = [(0.0, 0.0), (10.0, 0.0), (0.0, 10.0)]
    hull_area = compute_convex_hull_area(pts)
    assert hull_area == pytest.approx(50.0)

    # Square with vertices (0,0), (10,0), (10,10), (0,10) has area 100.0
    square_pts = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0), (5.0, 5.0)]
    assert compute_convex_hull_area(square_pts) == pytest.approx(100.0)


def test_mean_pairwise_distance():
    """Test mean pairwise distance on known coordinates."""
    # 3-4-5 triangle: (0,0), (3,0), (0,4)
    # Pairs: (0,0)-(3,0) = 3; (0,0)-(0,4) = 4; (3,0)-(0,4) = 5. Mean = 12 / 3 = 4.0
    pts = [(0.0, 0.0), (3.0, 0.0), (0.0, 4.0)]
    assert compute_mean_pairwise_distance(pts) == pytest.approx(4.0)

    # Fewer than 2 points returns None
    assert compute_mean_pairwise_distance([]) is None
    assert compute_mean_pairwise_distance([(1.0, 1.0)]) is None


def test_escape_corridor_inclusion_and_geometry():
    """Test forward escape corridor wedge polygon construction and point inclusion."""
    ball_opp = (60.0, 40.0)  # Center of pitch in opponent frame
    # Goal center is at (120.0, 40.0)
    corridor = build_escape_corridor_polygon(ball_opp, goal_opp=(120.0, 40.0), radius=20.0, half_angle_deg=30.0)
    assert corridor.is_valid

    # Theoretical wedge area: (60 / 360) * pi * 20^2 = (1/6) * pi * 400 approx 209.44
    expected_area = (60.0 / 360.0) * math.pi * (20.0 ** 2)
    assert corridor.area == pytest.approx(expected_area, rel=1e-2)

    # Point directly ahead toward goal at distance 10 (inside)
    assert point_in_escape_corridor((70.0, 40.0), ball_opp) is True

    # Point at 25 degrees angle within 20 distance (inside)
    pt_25deg = (60.0 + 10.0 * math.cos(math.radians(25.0)), 40.0 + 10.0 * math.sin(math.radians(25.0)))
    assert point_in_escape_corridor(pt_25deg, ball_opp) is True

    # Point at 35 degrees angle (outside angular corridor)
    pt_35deg = (60.0 + 10.0 * math.cos(math.radians(35.0)), 40.0 + 10.0 * math.sin(math.radians(35.0)))
    assert point_in_escape_corridor(pt_35deg, ball_opp) is False

    # Point in direction of goal but distance 25 > 20 (outside radius)
    assert point_in_escape_corridor((85.0, 40.0), ball_opp) is False

    # Point behind the ball (outside)
    assert point_in_escape_corridor((50.0, 40.0), ball_opp) is False


def test_escape_corridor_coverage_bounds():
    """Corridor camera coverage must be strictly within [0.0, 1.0]."""
    ball_opp = (60.0, 40.0)
    corridor = build_escape_corridor_polygon(ball_opp)

    # Fully visible
    vis_full = PITCH_BOX
    _, cov_full = compute_corridor_coverage(corridor, vis_full)
    assert cov_full == pytest.approx(1.0, rel=1e-2)

    # Half visible
    vis_half = box(0.0, 0.0, 70.0, 80.0)  # Covers x in [60, 70]
    _, cov_half = compute_corridor_coverage(corridor, vis_half)
    assert 0.0 < cov_half < 1.0

    # No visible polygon
    assert compute_corridor_coverage(corridor, None) == (0.0, 0.0)
