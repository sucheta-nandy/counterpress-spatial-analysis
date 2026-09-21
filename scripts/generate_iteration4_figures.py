"""Generate publication-quality figures for Iteration 4 analysis.

Produces:
- Figure 1: Grouped-CV model performance comparison (Context vs Local vs Full Spatial vs GAM vs Gradient Boosting)
- Figure 2: Calibration curve for primary regain model
- Figure 3: Regain probability vs nearest teammate distance (partial effect curve with rug / CI)
- Figure 4: Regain probability vs local numerical advantage (5 & 10 units)
- Figure 5: Dangerous-escape probability vs forward numerical advantage
- Figure 6: Dangerous-escape probability vs escape-corridor advantage
- Figure 7: 2D descriptive pitch map of observed regain rate (with minimum sample count threshold N >= 30)

Outputs saved to: results/figures/
"""

import logging
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import Pitch
from scipy.interpolate import make_interp_spline
from sklearn.calibration import calibration_curve

from counterpress.config import FIGURES_DIR, PROCESSED_DIR, TABLES_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Style parameters
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
plt.rcParams["axes.edgecolor"] = "#CCCCCC"
plt.rcParams["axes.linewidth"] = 0.8


def plot_figure_1_performance():
    perf_path = TABLES_DIR / "model_performance.csv"
    df_perf = pd.read_csv(perf_path)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), dpi=300)

    colors = ["#7f7f7f", "#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd", "#d62728"]
    models_to_plot = [
        "Model 0 (Null)",
        "Model 1 (Context)",
        "Model 2 (Context+Local)",
        "Model 3 (Full Spatial Logistic)",
        "Model 4 (Additive Spline GAM)",
        "Model 5 (Gradient Boosting)",
    ]
    clean_labels = ["Null (Prevalence)", "Model 1: Context", "Model 2: Context+Local", "Model 3: Full Spatial", "Model 4: Additive GAM", "Model 5: Gradient Boost"]

    for ax_idx, (tgt, title) in enumerate([("regain_5s", "Controlled Regain within 5s"), ("danger_15s", "Dangerous Opponent Escape within 15s")]):
        sub = df_perf[df_perf["target"] == tgt].set_index("model").loc[models_to_plot].reset_index()
        ax = axes[ax_idx]

        x_pos = np.arange(len(sub))
        bars = ax.bar(x_pos, sub["roc_auc_mean"], yerr=sub["roc_auc_std"], capsize=4, color=colors, alpha=0.85, edgecolor="#333333", width=0.6)

        ax.set_title(f"{title}\n5-Fold Grouped Cross-Validation (by Match)", fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel("Held-Out ROC-AUC", fontsize=11)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(clean_labels, rotation=35, ha="right", fontsize=9.5)
        ax.set_ylim(0.45, 0.86)
        ax.axhline(0.5, color="red", linestyle="--", alpha=0.5, label="Null Chance (0.50)")
        ax.grid(axis="y", linestyle=":", alpha=0.6)

        # Annotate bars with exact mean ROC-AUC and PR-AUC
        for bar, roc, pr in zip(bars, sub["roc_auc_mean"], sub["pr_auc_mean"]):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.012, f"{roc:.3f}\n(PR:{pr:.3f})", ha="center", va="bottom", fontsize=8.5, fontweight="semibold")

    plt.tight_layout()
    out_file = FIGURES_DIR / "model_performance.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 1 to {out_file}")


def plot_figure_2_calibration():
    oof_path = PROCESSED_DIR / "oof_predictions.parquet"
    df_oof = pd.read_parquet(oof_path)

    y_true = df_oof["regain_5s_controlled"].values

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), dpi=300, gridspec_kw={"height_ratios": [3, 1]})

    model_cols = [
        ("pred_regain_5s_model_1_context", "Model 1: Context Only", "#1f77b4", ":"),
        ("pred_regain_5s_model_3_full_spatial_logistic", "Model 3: Full Spatial Logistic", "#2ca02c", "-"),
        ("pred_regain_5s_model_4_additive_spline_gam", "Model 4: Additive Spline GAM", "#9467bd", "-."),
        ("pred_regain_5s_model_5_gradient_boosting", "Model 5: Gradient Boosting", "#d62728", "--"),
    ]

    ax1.plot([0, 1], [0, 1], "k--", label="Perfect Calibration", alpha=0.7)

    for col, lbl, color, ls in model_cols:
        y_prob = df_oof[col].values
        prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=10, strategy="quantile")
        ax1.plot(prob_pred, prob_true, marker="o", label=lbl, color=color, linestyle=ls, linewidth=1.8, markersize=5)
        # Histogram of predictions in lower panel
        ax2.hist(y_prob, bins=30, histtype="step", label=lbl, color=color, linestyle=ls, linewidth=1.2, density=True)

    ax1.set_title("Calibration Curve: Primary Regain Model (Y = regain_5s_controlled)\nQuantile Binned Held-Out Predictions Across 5 Grouped Folds", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Mean Predicted Regain Probability", fontsize=10)
    ax1.set_ylabel("Observed Regain Fraction", fontsize=10)
    ax1.set_xlim(-0.02, 1.02)
    ax1.set_ylim(-0.02, 1.02)
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left", fontsize=9)

    ax2.set_title("Distribution of Predicted Probabilities", fontsize=9.5, fontweight="bold")
    ax2.set_xlabel("Predicted Probability", fontsize=9)
    ax2.set_ylabel("Density", fontsize=9)
    ax2.set_xlim(-0.02, 1.02)
    ax2.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    out_file = FIGURES_DIR / "calibration_regain.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 2 to {out_file}")


def plot_figure_3_nearest_teammate():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    df = pd.read_parquet(parquet_path)

    valid_mask = df["nearest_teammate_distance"].notna()
    sub_df = df[valid_mask].copy()

    # Bin nearest teammate distance into fine intervals up to 25 units
    sub_df = sub_df[sub_df["nearest_teammate_distance"] <= 25.0]
    sub_df["dist_bin"] = pd.cut(sub_df["nearest_teammate_distance"], bins=np.linspace(0, 25, 26))

    binned = sub_df.groupby("dist_bin", observed=True).agg(
        mean_dist=("nearest_teammate_distance", "mean"),
        regain_rate=("regain_5s_controlled", "mean"),
        n_obs=("regain_5s_controlled", "count")
    ).dropna()

    # Wilson score / normal approx SE for error bars
    p = binned["regain_rate"].values
    n = binned["n_obs"].values
    se = np.sqrt(p * (1 - p) / n)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), dpi=300, gridspec_kw={"height_ratios": [3, 1]}, sharex=True)

    ax1.errorbar(binned["mean_dist"], p, yerr=1.96 * se, fmt="o", color="#1f77b4", ecolor="#9ecae1", elinewidth=1.5, capsize=3, label="Empirical Rate (95% CI)")

    # Smooth curve
    x_dense = np.linspace(binned["mean_dist"].min(), binned["mean_dist"].max(), 200)
    spl = make_interp_spline(binned["mean_dist"], p, k=3)
    ax1.plot(x_dense, spl(x_dense), color="#08519c", linewidth=2.2, label="Spline Fit")

    ax1.set_title("Controlled Regain Probability vs. Nearest Teammate Distance\nCounterpress Initiation Frame (t <= t_init)", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Regain within 5s Probability", fontsize=10)
    ax1.set_ylim(0.15, 0.70)
    ax1.axhline(0.3465, color="red", linestyle="--", alpha=0.7, label="Cohort Base Rate (34.65%)")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper right", fontsize=9)

    # Rug / observation count histogram
    ax2.bar(binned["mean_dist"], binned["n_obs"], width=0.8, color="#bdbdbd", edgecolor="#737373", alpha=0.8)
    ax2.set_xlabel("Nearest Teammate Distance (StatsBomb Coordinate Units)", fontsize=10)
    ax2.set_ylabel("Episode Count", fontsize=9)
    ax2.grid(axis="y", linestyle=":", alpha=0.6)

    plt.tight_layout()
    out_file = FIGURES_DIR / "regain_nearest_teammate.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 3 to {out_file}")


def plot_figure_4_numerical_advantage():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    df = pd.read_parquet(parquet_path)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

    for ax, adv_col, radius, min_val, max_val in [(ax1, "numerical_advantage_5", "5-Unit Radius", -3, 2), (ax2, "numerical_advantage_10", "10-Unit Radius", -4, 3)]:
        sub_df = df.copy()
        sub_df["binned"] = sub_df[adv_col].clip(lower=min_val, upper=max_val)
        grouped = sub_df.groupby("binned").agg(
            regain_rate=("regain_5s_controlled", "mean"),
            n_obs=("regain_5s_controlled", "count")
        ).reset_index()

        p = grouped["regain_rate"].values
        n = grouped["n_obs"].values
        se = np.sqrt(p * (1 - p) / n)

        x_vals = grouped["binned"].values
        bars = ax.bar(x_vals, p, yerr=1.96 * se, capsize=4, color="#3182bd", alpha=0.85, edgecolor="#08519c", width=0.65)

        ax.set_title(f"Regain Rate vs. Numerical Advantage\n({radius})", fontsize=11, fontweight="bold")
        ax.set_xlabel(f"Numerical Advantage: Teammates - Opponents ({adv_col})", fontsize=10)
        ax.set_ylabel("Regain within 5s Rate", fontsize=10)
        ax.set_ylim(0.0, 0.90)
        ax.axhline(0.3465, color="red", linestyle="--", alpha=0.7, label="Base Rate (34.65%)")
        ax.grid(axis="y", linestyle=":", alpha=0.6)

        # Bar value annotations
        for bar, rate, count in zip(bars, p, n):
            ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height() + 0.04, f"{rate*100:.1f}%\n(N={count})", ha="center", va="bottom", fontsize=8)

        ax.legend(loc="upper left", fontsize=8.5)

    plt.tight_layout()
    out_file = FIGURES_DIR / "regain_numerical_advantage.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 4 to {out_file}")


def plot_figure_5_forward_advantage():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    df = pd.read_parquet(parquet_path)

    sub_df = df.copy()
    sub_df["binned"] = sub_df["forward_numerical_advantage"].clip(lower=-4, upper=3)
    grouped = sub_df.groupby("binned").agg(
        danger_rate=("dangerous_escape_15s", "mean"),
        n_obs=("dangerous_escape_15s", "count")
    ).reset_index()

    p = grouped["danger_rate"].values
    n = grouped["n_obs"].values
    se = np.sqrt(p * (1 - p) / n)

    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    bars = ax.bar(grouped["binned"], p, yerr=1.96 * se, capsize=4, color="#e6550d", alpha=0.85, edgecolor="#a63603", width=0.6)

    ax.set_title("Dangerous Opponent Escape Rate vs. Forward Numerical Advantage\nOpponents Ahead - Pressing Defenders Ahead (Opponent Attack Direction)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Forward Numerical Advantage (>0 Opponent Surplus, <0 Pressing Defensive Surplus)", fontsize=10)
    ax.set_ylabel("Dangerous Escape within 15s Rate", fontsize=10)
    ax.set_ylim(0.0, 0.35)
    ax.axhline(0.2241, color="black", linestyle="--", alpha=0.7, label="Base Rate (22.41%)")
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    for bar, rate, count in zip(bars, p, n):
        ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height() + 0.015, f"{rate*100:.1f}%\n(N={count})", ha="center", va="bottom", fontsize=8.5)

    ax.legend(loc="upper right", fontsize=9)
    plt.tight_layout()
    out_file = FIGURES_DIR / "danger_forward_advantage.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 5 to {out_file}")


def plot_figure_6_corridor_advantage():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    df = pd.read_parquet(parquet_path)

    sub_df = df.copy()
    sub_df["binned"] = sub_df["escape_corridor_advantage_20"].clip(lower=-2, upper=2)
    grouped = sub_df.groupby("binned").agg(
        danger_rate=("dangerous_escape_15s", "mean"),
        n_obs=("dangerous_escape_15s", "count")
    ).reset_index()

    p = grouped["danger_rate"].values
    n = grouped["n_obs"].values
    se = np.sqrt(p * (1 - p) / n)

    labels = ["<= -2 (Defensive Surplus)", "-1 (Defensive +1)", "0 (Parity)", "+1 (Opponent +1)", ">= +2 (Opponent Surplus)"]

    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    bars = ax.bar(range(len(labels)), p, yerr=1.96 * se, capsize=4, color="#fd8d3c", alpha=0.85, edgecolor="#d94801", width=0.55)

    ax.set_title("Dangerous Opponent Escape Rate vs. Escape Corridor Advantage\n20-Unit Sector Toward Counterpressing Goal (Opponents - Defenders)", fontsize=11, fontweight="bold")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=9)
    ax.set_ylabel("Dangerous Escape within 15s Rate", fontsize=10)
    ax.set_ylim(0.0, 0.35)
    ax.axhline(0.2241, color="black", linestyle="--", alpha=0.7, label="Base Rate (22.41%)")
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    for bar, rate, count in zip(bars, p, n):
        ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height() + 0.015, f"{rate*100:.1f}%\n(N={count})", ha="center", va="bottom", fontsize=8.5)

    ax.legend(loc="upper right", fontsize=9)
    plt.tight_layout()
    out_file = FIGURES_DIR / "danger_corridor_advantage.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Figure 6 to {out_file}")


def plot_figure_7_regain_pitch_map():
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    df = pd.read_parquet(parquet_path)

    # 2D binning on 120 x 80 pitch (12 x 8 grid = 10x10 unit cells)
    x_bins = np.linspace(0, 120, 13)
    y_bins = np.linspace(0, 80, 9)

    df["x_bin"] = pd.cut(df["initiation_x"], bins=x_bins, labels=False)
    df["y_bin"] = pd.cut(df["initiation_y"], bins=y_bins, labels=False)

    grid_stats = df.groupby(["x_bin", "y_bin"]).agg(
        n_obs=("regain_5s_controlled", "count"),
        regain_rate=("regain_5s_controlled", "mean")
    ).reset_index()

    # Minimum sample size threshold: N >= 30
    MIN_OBS = 30
    grid_matrix = np.full((len(y_bins) - 1, len(x_bins) - 1), np.nan)
    count_matrix = np.zeros((len(y_bins) - 1, len(x_bins) - 1))

    for _, row in grid_stats.iterrows():
        xb = int(row["x_bin"])
        yb = int(row["y_bin"])
        n = int(row["n_obs"])
        r = float(row["regain_rate"])
        count_matrix[yb, xb] = n
        if n >= MIN_OBS:
            grid_matrix[yb, xb] = r

    # Create pitch visualization using mplsoccer
    pitch = Pitch(
        pitch_type="statsbomb",
        pitch_color="#1a1c23",
        line_color="#c0c0c0",
        line_zorder=2,
    )
    fig, ax = pitch.draw(figsize=(12, 8))

    # Plot 2D heatmap
    x_centers = (x_bins[:-1] + x_bins[1:]) / 2.0
    y_centers = (y_bins[:-1] + y_bins[1:]) / 2.0
    X, Y = np.meshgrid(x_bins, y_bins)

    mesh = ax.pcolormesh(X, Y, grid_matrix, cmap="viridis", vmin=0.15, vmax=0.65, alpha=0.85, zorder=1)

    cbar = plt.colorbar(mesh, ax=ax, orientation="horizontal", fraction=0.046, pad=0.04)
    cbar.set_label("Observed Controlled Regain Rate (5s) [Cells with N >= 30]", color="white", fontsize=10)
    cbar.ax.xaxis.set_tick_params(color="white")
    plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='white')

    # Annotate cell rates
    for i in range(len(y_centers)):
        for j in range(len(x_centers)):
            rate = grid_matrix[i, j]
            count = int(count_matrix[i, j])
            if not np.isnan(rate):
                ax.text(x_centers[j], y_centers[i], f"{rate*100:.0f}%\n(n={count})", ha="center", va="center", color="white", fontsize=7.5, fontweight="bold", zorder=3)

    ax.set_title("Descriptive 2D Pitch Map: Controlled Regain Rate within 5s\nPrimary Cohort (N = 21,616 Episodes, Cell Size: 10x10 Units, Filter: N >= 30)", color="white", fontsize=12, fontweight="bold", pad=12)

    fig.patch.set_facecolor("#1a1c23")
    out_file = FIGURES_DIR / "regain_pitch_map.png"
    plt.savefig(out_file, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    logger.info(f"Saved Figure 7 to {out_file}")


def main():
    plot_figure_1_performance()
    plot_figure_2_calibration()
    plot_figure_3_nearest_teammate()
    plot_figure_4_numerical_advantage()
    plot_figure_5_forward_advantage()
    plot_figure_6_corridor_advantage()
    plot_figure_7_regain_pitch_map()


if __name__ == "__main__":
    main()
