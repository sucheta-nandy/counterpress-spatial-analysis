"""Visualization module for counterpress actions and StatsBomb 360 freeze frames.

Generates publication-quality pitch visualizations with:
- Visible camera viewport polygon
- Counterpressing players (actor highlighted)
- Opponent players (goalkeepers distinct)
- Local density rings (5, 10, 15 yards)
- Tactical annotations and contextual headers
"""

import logging
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch

from counterpress.config import FIGURES_DIR, PITCH_LENGTH, PITCH_WIDTH, SPATIAL_RADII

logger = logging.getLogger(__name__)


def plot_counterpress_freeze_frame(
    event: Dict[str, Any],
    freeze_frame: Dict[str, Any],
    match_info: Optional[Dict[str, Any]] = None,
    show_density_radii: bool = True,
    save_path: Optional[Union[str, Path]] = None,
    dark_mode: bool = True,
    figsize: Tuple[float, float] = (12, 8),
) -> Tuple[plt.Figure, plt.Axes]:
    """Plot a single counterpress event with its 360 freeze frame and visible area polygon.

    Parameters
    ----------
    event : dict
        StatsBomb event dictionary (e.g. Pressure event).
    freeze_frame : dict
        StatsBomb 360 freeze frame dict containing 'visible_area' and 'freeze_frame' player list.
    match_info : dict, optional
        Metadata about match (teams, date, competition).
    show_density_radii : bool, default True
        Whether to draw 5yd, 10yd, and 15yd concentric circles around the presser.
    save_path : str or Path, optional
        Path to save figure.
    dark_mode : bool, default True
        Dark vs light tactical pitch style.
    figsize : tuple, default (12, 8)
        Figure size in inches.

    Returns
    -------
    fig, ax : matplotlib Figure and Axes
    """
    pitch_color = "#10141a" if dark_mode else "#f8f9fa"
    line_color = "#4a5568" if dark_mode else "#cbd5e1"
    text_color = "#f1f5f9" if dark_mode else "#0f172a"
    subtext_color = "#94a3b8" if dark_mode else "#64748b"

    pitch = Pitch(
        pitch_type="statsbomb",
        pitch_color=pitch_color,
        line_color=line_color,
        linewidth=1.5,
        goal_type="box",
    )

    fig, ax = pitch.draw(figsize=figsize)
    fig.patch.set_facecolor(pitch_color)

    # 1. Draw 360 Visible Area Polygon
    visible_coords = freeze_frame.get("visible_area", [])
    if visible_coords and len(visible_coords) >= 6:
        poly_pts = np.array(visible_coords).reshape(-1, 2)
        poly = patches.Polygon(
            poly_pts,
            closed=True,
            facecolor="#38bdf8" if dark_mode else "#0284c7",
            alpha=0.12,
            edgecolor="#38bdf8" if dark_mode else "#0284c7",
            linestyle="--",
            linewidth=1.2,
            zorder=2,
            label="360 Camera Viewport",
        )
        ax.add_patch(poly)

    # 2. Extract Event Actor details
    ev_loc = event.get("location", [None, None])
    ev_x, ev_y = ev_loc[0], ev_loc[1]
    actor_name = event.get("player", {}).get("name", "Unknown Actor")
    event_team = event.get("team", {}).get("name", "Defending Team")
    event_type = event.get("type", {}).get("name", "Event")

    # 3. Plot Concentric Density Radii around Actor
    if show_density_radii and ev_x is not None and ev_y is not None:
        for r, ls, alpha in zip(SPATIAL_RADII, [":", "--", "-."], [0.5, 0.4, 0.3]):
            circ = patches.Circle(
                (ev_x, ev_y),
                radius=r,
                facecolor="none",
                edgecolor="#fbbf24",
                linestyle=ls,
                linewidth=1.0,
                alpha=alpha,
                zorder=3,
            )
            ax.add_patch(circ)
            ax.text(
                ev_x,
                ev_y - r - 0.5,
                f"{int(r)}y",
                color="#fbbf24",
                fontsize=7,
                ha="center",
                va="top",
                alpha=0.7,
                zorder=4,
            )

    # 4. Plot Freeze-Frame Players
    players = freeze_frame.get("freeze_frame", [])
    teammate_color = "#3b82f6"  # Blue
    opponent_color = "#ef4444"  # Red
    actor_color = "#fbbf24"     # Amber/Gold
    gk_color = "#10b981"        # Emerald Green

    teammates_x, teammates_y = [], []
    opponents_x, opponents_y = [], []
    actor_x, actor_y = None, None

    for p in players:
        loc = p.get("location")
        if not loc or len(loc) < 2:
            continue
        px, py = loc[0], loc[1]
        is_actor = p.get("actor", False)
        is_teammate = p.get("teammate", False)
        is_keeper = p.get("keeper", False)

        if is_actor:
            actor_x, actor_y = px, py
        elif is_teammate:
            teammates_x.append(px)
            teammates_y.append(py)
            if is_keeper:
                ax.scatter(px, py, c=gk_color, s=180, edgecolors=pitch_color, linewidth=1.5, zorder=5)
        else:
            opponents_x.append(px)
            opponents_y.append(py)
            if is_keeper:
                ax.scatter(px, py, c=gk_color, s=180, edgecolors=pitch_color, linewidth=1.5, zorder=5)

    # Draw regular teammates and opponents
    if teammates_x:
        ax.scatter(
            teammates_x,
            teammates_y,
            c=teammate_color,
            s=160,
            edgecolors="#ffffff" if dark_mode else "#1e293b",
            linewidth=1.2,
            zorder=5,
            label=f"Teammates ({event_team})",
        )
    if opponents_x:
        ax.scatter(
            opponents_x,
            opponents_y,
            c=opponent_color,
            s=160,
            edgecolors="#ffffff" if dark_mode else "#1e293b",
            linewidth=1.2,
            zorder=5,
            label="Opponents (Possession Team)",
        )

    # Draw actor distinctly
    act_plot_x = actor_x if actor_x is not None else ev_x
    act_plot_y = actor_y if actor_y is not None else ev_y
    if act_plot_x is not None and act_plot_y is not None:
        ax.scatter(
            act_plot_x,
            act_plot_y,
            c=actor_color,
            s=260,
            marker="*",
            edgecolors="#000000",
            linewidth=1.5,
            zorder=6,
            label=f"Presser: {actor_name}",
        )
        ax.annotate(
            actor_name.split()[-1] if actor_name else "Actor",
            xy=(act_plot_x, act_plot_y),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            va="bottom",
            color=actor_color,
            fontweight="bold",
            fontsize=9,
            zorder=7,
        )

    # 5. Attacking Direction Indicator
    ax.annotate(
        "",
        xy=(80, 77),
        xytext=(40, 77),
        arrowprops=dict(arrowstyle="->", color=subtext_color, lw=1.5),
        zorder=5,
    )
    ax.text(
        60,
        76,
        f"{event_team} Attacking Direction ➔",
        color=subtext_color,
        fontsize=8,
        ha="center",
        va="bottom",
        fontstyle="italic",
        zorder=5,
    )

    # 6. Title and Metadata Headers
    match_str = ""
    if match_info:
        home = match_info.get("home_team_name", "")
        away = match_info.get("away_team_name", "")
        comp = match_info.get("competition_name", "")
        season = match_info.get("season_name", "")
        date = match_info.get("match_date", "")
        match_str = f"{home} vs. {away} | {comp} {season} ({date})\n"

    time_str = f"Period {event.get('period', 1)} - {event.get('minute', 0):02d}:{event.get('second', 0):02d}"
    coord_str = f"Location: ({act_plot_x:.1f}, {act_plot_y:.1f})" if act_plot_x is not None else ""

    title = f"{match_str}Counterpress Action: {event_type} by {actor_name} ({event_team})"
    subtitle = f"{time_str} | {coord_str} | Visible: {len(players)} players ({len(teammates_x) + 1} T, {len(opponents_x)} O)"

    ax.set_title(title, fontsize=12, fontweight="bold", color=text_color, pad=20, loc="left")
    ax.text(
        0,
        -3,
        subtitle,
        fontsize=9,
        color=subtext_color,
        ha="left",
        va="top",
        transform=ax.get_xaxis_transform(),
    )

    # 7. Legend
    leg = ax.legend(
        loc="upper right",
        bbox_to_anchor=(1.0, 1.05),
        facecolor=pitch_color,
        edgecolor=line_color,
        fontsize=8,
        labelcolor=text_color,
        framealpha=0.9,
    )
    leg.set_zorder(10)

    plt.tight_layout()

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
        logger.info(f"Saved figure to {save_path}")

    return fig, ax


def plot_spatial_qa_freeze_frame(
    episode: Dict[str, Any],
    freeze_frame: Dict[str, Any],
    feature_row: Dict[str, Any],
    save_path: Optional[Union[str, Path]] = None,
    dark_mode: bool = True,
    figsize: Tuple[float, float] = (12, 8),
) -> Tuple[plt.Figure, plt.Axes]:
    """Generate a spatial QA visualization with complete tactical geometry annotations.

    Displays:
    - Pitch (120 x 80 StatsBomb coordinate units)
    - Initiation location (x0, y0)
    - Counterpressing actor (distinct gold star marker)
    - Visible counterpressing teammates (blue circles)
    - Visible opponents (red circles)
    - Goalkeepers (emerald green markers)
    - 360 camera visible area polygon (shaded light blue)
    - 5, 10, 15 unit concentric circles
    - Opponent transition attack arrow
    - 20-unit forward escape corridor wedge (in pressing team frame: toward defending goal)
    - Boxed tactical metrics annotations
    """
    pitch_color = "#10141a" if dark_mode else "#f8f9fa"
    line_color = "#4a5568" if dark_mode else "#cbd5e1"
    text_color = "#f1f5f9" if dark_mode else "#0f172a"
    subtext_color = "#94a3b8" if dark_mode else "#64748b"

    pitch = Pitch(
        pitch_type="statsbomb",
        pitch_color=pitch_color,
        line_color=line_color,
        linewidth=1.5,
        goal_type="box",
    )

    fig, ax = pitch.draw(figsize=figsize)
    fig.patch.set_facecolor(pitch_color)

    # 1. Visible Area Polygon
    visible_coords = freeze_frame.get("visible_area", [])
    if visible_coords and len(visible_coords) >= 6:
        poly_pts = np.array(visible_coords).reshape(-1, 2)
        poly = patches.Polygon(
            poly_pts,
            closed=True,
            facecolor="#38bdf8" if dark_mode else "#0284c7",
            alpha=0.12,
            edgecolor="#38bdf8" if dark_mode else "#0284c7",
            linestyle="--",
            linewidth=1.2,
            zorder=2,
            label="360 Visible Area",
        )
        ax.add_patch(poly)

    # 2. Initiation Location
    x0 = float(feature_row.get("initiation_x", 60.0))
    y0 = float(feature_row.get("initiation_y", 40.0))

    # 3. Density Circles (5, 10, 15 units)
    for r, ls, col in zip([5.0, 10.0, 15.0], [":", "--", "-."], ["#eab308", "#f59e0b", "#d97706"]):
        circ = patches.Circle(
            (x0, y0),
            radius=r,
            facecolor="none",
            edgecolor=col,
            linestyle=ls,
            linewidth=1.2,
            alpha=0.6,
            zorder=3,
        )
        ax.add_patch(circ)
        ax.text(
            x0,
            y0 - r - 0.6,
            f"{int(r)}u",
            color=col,
            fontsize=7,
            fontweight="bold",
            ha="center",
            va="top",
            zorder=4,
        )

    # 4. Forward Escape Corridor (Radius 20, 30-deg half-angle)
    # Opponent attacks toward defending goal (0.0, 40.0) in pressing team frame
    theta_opp_goal = math.atan2(40.0 - y0, 0.0 - x0)
    half_ang = math.radians(30.0)
    arc_angles = np.linspace(theta_opp_goal - half_ang, theta_opp_goal + half_ang, 32)
    corridor_pts = [(x0, y0)] + [
        (x0 + 20.0 * math.cos(a), y0 + 20.0 * math.sin(a)) for a in arc_angles
    ] + [(x0, y0)]

    corr_poly = patches.Polygon(
        corridor_pts,
        closed=True,
        facecolor="#f97316",
        alpha=0.15,
        edgecolor="#f97316",
        linestyle="--",
        linewidth=1.5,
        zorder=3,
        label="20u Escape Corridor (30°)",
    )
    ax.add_patch(corr_poly)

    # Opponent Attack Direction Arrow
    arrow_len = 12.0
    ax.annotate(
        "",
        xy=(x0 + arrow_len * math.cos(theta_opp_goal), y0 + arrow_len * math.sin(theta_opp_goal)),
        xytext=(x0, y0),
        arrowprops=dict(arrowstyle="->", color="#ef4444", lw=2.0, ls="-"),
        zorder=5,
    )
    ax.text(
        x0 + (arrow_len + 2.0) * math.cos(theta_opp_goal),
        y0 + (arrow_len + 2.0) * math.sin(theta_opp_goal),
        "Opponent Attack",
        color="#ef4444",
        fontsize=8,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=6,
    )

    # 5. Players
    players = freeze_frame.get("freeze_frame", [])
    teammates_x, teammates_y = [], []
    opponents_x, opponents_y = [], []
    actor_x, actor_y = None, None
    keepers_x, keepers_y = [], []

    for p in players:
        loc = p.get("location")
        if not loc or len(loc) < 2:
            continue
        px, py = float(loc[0]), float(loc[1])
        if p.get("actor") is True:
            actor_x, actor_y = px, py
        elif p.get("keeper") is True:
            keepers_x.append(px)
            keepers_y.append(py)
        elif p.get("teammate") is True:
            teammates_x.append(px)
            teammates_y.append(py)
        else:
            opponents_x.append(px)
            opponents_y.append(py)

    if teammates_x:
        ax.scatter(teammates_x, teammates_y, s=80, c="#38bdf8", edgecolors="#0284c7", lw=1.2, zorder=6, label=f"Teammates ({len(teammates_x)})")
    if opponents_x:
        ax.scatter(opponents_x, opponents_y, s=80, c="#f87171", edgecolors="#b91c1c", lw=1.2, zorder=6, label=f"Opponents ({len(opponents_x)})")
    if keepers_x:
        ax.scatter(keepers_x, keepers_y, s=90, marker="s", c="#34d399", edgecolors="#059669", lw=1.2, zorder=6, label=f"Goalkeepers ({len(keepers_x)})")

    # Plot actor
    if actor_x is not None:
        ax.scatter(actor_x, actor_y, s=160, marker="*", c="#facc15", edgecolors="#ca8a04", lw=1.5, zorder=7, label="Counterpress Actor")
    else:
        ax.scatter(x0, y0, s=120, marker="x", c="#facc15", lw=2.0, zorder=7, label="Initiation Location")

    # 6. Title and Metadata
    ep_id = episode.get("episode_id", "Episode")
    comp = episode.get("competition_name", episode.get("competition", ""))
    press_team = episode.get("counterpressing_team", "Pressing Team")
    opp_team = episode.get("possession_team", episode.get("opponent_team", "Opponent Team"))

    title = f"Spatial QA: {press_team} vs {opp_team} | {ep_id}"
    subtitle = f"Comp: {comp} | Zone: {feature_row.get('pitch_zone_3x3')} | Pos: [{x0:.1f}, {y0:.1f}]"

    ax.set_title(title, fontsize=12, fontweight="bold", color=text_color, pad=18, loc="left")
    ax.text(0, -3, subtitle, fontsize=9, color=subtext_color, ha="left", va="top", transform=ax.get_xaxis_transform())

    # 7. Metrics Annotation Box
    num_adv_10 = feature_row.get("numerical_advantage_10", 0)
    cov_10 = feature_row.get("coverage_10", 0.0)
    fwd_adv = feature_row.get("forward_numerical_advantage", 0)
    corr_adv = feature_row.get("escape_corridor_advantage_20", 0)
    corr_cov = feature_row.get("escape_corridor_coverage_20", 0.0)

    metrics_text = (
        f"Tactical QA Metrics:\n"
        f"• numerical_advantage_10: {num_adv_10:+d}\n"
        f"• coverage_10: {cov_10:.1%}\n"
        f"• forward_numerical_advantage: {fwd_adv:+d}\n"
        f"• escape_corridor_advantage_20: {corr_adv:+d}\n"
        f"• escape_corridor_coverage_20: {corr_cov:.1%}"
    )

    ax.text(
        0.02,
        0.04,
        metrics_text,
        transform=ax.transAxes,
        fontsize=8.5,
        fontfamily="monospace",
        color="#f8fafc",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#0f172a", edgecolor="#334155", alpha=0.85),
        zorder=10,
    )

    leg = ax.legend(
        loc="upper right",
        bbox_to_anchor=(1.0, 1.05),
        facecolor=pitch_color,
        edgecolor=line_color,
        fontsize=8,
        labelcolor=text_color,
        framealpha=0.9,
    )
    leg.set_zorder(10)

    plt.tight_layout()

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
        logger.info(f"Saved QA figure to {save_path}")

    return fig, ax

