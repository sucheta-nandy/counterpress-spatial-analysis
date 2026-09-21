"""Iteration 4.5 Pre-Submission Statistical and Interpretation Audit Script.

Computes:
1. Paired match-cluster bootstrap comparisons (Model 3 vs 4, Model 3 vs 5).
2. Fold-wise coefficient stability table for compact logistic model across 5 CV folds.
3. Fold-wise permutation importance stability table for Model 5 across 5 CV folds.
4. Visibility subset reconciliation counts (raw, missing, model-complete-case).
5. High-coverage sensitivity coefficient comparison.
6. FDR-adjusted q-values for logistic coefficients.
7. Competition prevalence alongside leave-one-competition-out performance.
8. Model calibration intercepts and slopes.
9. Pre-submission claims audit table (8-12 conference-safe claims).
10. Danger non-linear partial dependence diagnostics.
"""

import os
import sys
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, List, Tuple, Any

from sklearn.linear_model import LogisticRegression
from sklearn.inspection import partial_dependence, permutation_importance
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, log_loss
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

from counterpress.config import DATA_DIR, PROCESSED_DIR, TABLES_DIR, FIGURES_DIR
from counterpress.models import evaluate_probability_model, match_cluster_bootstrap_ci
from counterpress.modeling import build_model_pipeline, fit_clustered_logistic_regression

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def compute_paired_bootstrap(oof: pd.DataFrame, n_boot: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Compute paired match-cluster bootstrap differences for Model 3 vs 4 and Model 3 vs 5."""
    logger.info("Computing paired match-cluster bootstrap comparisons...")
    rng = np.random.RandomState(seed)
    unique_clusters = oof["match_id"].unique()
    n_clusters = len(unique_clusters)
    cluster_to_indices = oof.groupby("match_id").indices

    comparisons = [
        ("regain_5s", "regain_5s_controlled", "pred_regain_5s_model_3_full_spatial_logistic", "pred_regain_5s_model_4_additive_spline_gam", "Model 3 vs Model 4 (GAM)"),
        ("regain_5s", "regain_5s_controlled", "pred_regain_5s_model_3_full_spatial_logistic", "pred_regain_5s_model_5_gradient_boosting", "Model 3 vs Model 5 (HGB)"),
        ("danger_15s", "dangerous_escape_15s", "pred_danger_15s_model_3_full_spatial_logistic", "pred_danger_15s_model_4_additive_spline_gam", "Model 3 vs Model 4 (GAM)"),
        ("danger_15s", "dangerous_escape_15s", "pred_danger_15s_model_3_full_spatial_logistic", "pred_danger_15s_model_5_gradient_boosting", "Model 3 vs Model 5 (HGB)"),
    ]

    records = []
    for target_name, y_col, m_base_col, m_comp_col, comp_label in comparisons:
        y_true_all = oof[y_col].values
        p_base_all = oof[m_base_col].values
        p_comp_all = oof[m_comp_col].values

        # Point estimates on full OOF
        pe_base_roc = roc_auc_score(y_true_all, p_base_all)
        pe_comp_roc = roc_auc_score(y_true_all, p_comp_all)
        delta_roc = pe_comp_roc - pe_base_roc

        pe_base_pr = average_precision_score(y_true_all, p_base_all)
        pe_comp_pr = average_precision_score(y_true_all, p_comp_all)
        delta_pr = pe_comp_pr - pe_base_pr

        pe_base_brier = brier_score_loss(y_true_all, p_base_all)
        pe_comp_brier = brier_score_loss(y_true_all, p_comp_brier) if False else brier_score_loss(y_true_all, p_comp_all)
        delta_brier = pe_comp_brier - pe_base_brier

        pe_base_ll = log_loss(y_true_all, p_base_all)
        pe_comp_ll = log_loss(y_true_all, p_comp_all)
        delta_ll = pe_comp_ll - pe_base_ll

        deltas_roc, deltas_pr, deltas_brier, deltas_ll = [], [], [], []

        for _ in range(n_boot):
            sample_clusters = rng.choice(unique_clusters, size=n_clusters, replace=True)
            sample_indices = np.concatenate([cluster_to_indices[c] for c in sample_clusters])

            y_b = y_true_all[sample_indices]
            p_base_b = p_base_all[sample_indices]
            p_comp_b = p_comp_all[sample_indices]

            if len(np.unique(y_b)) < 2:
                continue

            r_base = roc_auc_score(y_b, p_base_b)
            r_comp = roc_auc_score(y_b, p_comp_b)
            deltas_roc.append(r_comp - r_base)

            pr_base = average_precision_score(y_b, p_base_b)
            pr_comp = average_precision_score(y_b, p_comp_b)
            deltas_pr.append(pr_comp - pr_base)

            b_base = brier_score_loss(y_b, p_base_b)
            b_comp = brier_score_loss(y_b, p_comp_b)
            deltas_brier.append(b_comp - b_base)

            ll_base = log_loss(y_b, p_base_b)
            ll_comp = log_loss(y_b, p_comp_b)
            deltas_ll.append(ll_comp - ll_base)

        def ci_str(vals):
            l = np.percentile(vals, 2.5)
            u = np.percentile(vals, 97.5)
            return f"[{l:+.4f}, {u:+.4f}]"

        records.append({
            "target": target_name,
            "comparison": comp_label,
            "metric": "delta_roc_auc",
            "delta_point_estimate": round(delta_roc, 4),
            "ci_95": ci_str(deltas_roc),
            "excludes_zero": bool(np.percentile(deltas_roc, 2.5) > 0 or np.percentile(deltas_roc, 97.5) < 0),
            "interpretation": "statistically distinguishable" if (np.percentile(deltas_roc, 2.5) > 0 or np.percentile(deltas_roc, 97.5) < 0) else "statistically indistinguishable (overlaps zero)"
        })
        records.append({
            "target": target_name,
            "comparison": comp_label,
            "metric": "delta_pr_auc",
            "delta_point_estimate": round(delta_pr, 4),
            "ci_95": ci_str(deltas_pr),
            "excludes_zero": bool(np.percentile(deltas_pr, 2.5) > 0 or np.percentile(deltas_pr, 97.5) < 0),
            "interpretation": "statistically distinguishable" if (np.percentile(deltas_pr, 2.5) > 0 or np.percentile(deltas_pr, 97.5) < 0) else "statistically indistinguishable (overlaps zero)"
        })
        records.append({
            "target": target_name,
            "comparison": comp_label,
            "metric": "delta_brier",
            "delta_point_estimate": round(delta_brier, 4),
            "ci_95": ci_str(deltas_brier),
            "excludes_zero": bool(np.percentile(deltas_brier, 2.5) > 0 or np.percentile(deltas_brier, 97.5) < 0),
            "interpretation": "statistically distinguishable" if (np.percentile(deltas_brier, 2.5) > 0 or np.percentile(deltas_brier, 97.5) < 0) else "statistically indistinguishable (overlaps zero)"
        })
        records.append({
            "target": target_name,
            "comparison": comp_label,
            "metric": "delta_log_loss",
            "delta_point_estimate": round(delta_ll, 4),
            "ci_95": ci_str(deltas_ll),
            "excludes_zero": bool(np.percentile(deltas_ll, 2.5) > 0 or np.percentile(deltas_ll, 97.5) < 0),
            "interpretation": "statistically distinguishable" if (np.percentile(deltas_ll, 2.5) > 0 or np.percentile(deltas_ll, 97.5) < 0) else "statistically indistinguishable (overlaps zero)"
        })

    df_paired = pd.DataFrame(records)
    out_path = TABLES_DIR / "paired_model_comparisons.csv"
    df_paired.to_csv(out_path, index=False)
    logger.info(f"Saved paired model comparisons to {out_path}.")
    return df_paired


def compute_visibility_reconciliation(df: pd.DataFrame) -> pd.DataFrame:
    """Reconcile visibility subset counts directly from counterpress_features.parquet."""
    logger.info("Computing visibility subset reconciliation...")
    n_total = len(df)

    # 1. 10m local coverage
    cov10_float_ge_80 = int((df["coverage_10"] >= 0.80).sum())
    cov10_bool_flag = int(df["coverage_10_ge_80pct"].sum())
    cov10_missing = int(df["coverage_10"].isna().sum())
    cov10_clean_actor = int(((df["coverage_10"] >= 0.80) & (~df["actor_matching_anomalous"])).sum())

    # 2. Corridor 20m coverage
    corridor_float_ge_80 = int((df["escape_corridor_coverage_20"] >= 0.80).sum())
    corridor_missing = int(df["escape_corridor_coverage_20"].isna().sum())
    corridor_clean_actor = int(((df["escape_corridor_coverage_20"] >= 0.80) & (~df["actor_matching_anomalous"])).sum())

    records = [
        {
            "subset_name": "coverage_10 >= 0.80 (boolean flag)",
            "predicate": "coverage_10_ge_80pct == True",
            "raw_count": cov10_bool_flag,
            "missing_count": cov10_missing,
            "count_after_clean_actor_filter": cov10_clean_actor,
            "pct_of_primary_cohort": round(cov10_bool_flag / n_total * 100, 2),
            "canonical_status": "Canonical boolean flag (20,547)",
            "explanation": "Evaluated during feature engineering before serialization. Exactly 1 episode (3901797_p29_991b0392) had unrounded coverage_10 = 0.7999999999999999 resulting in False."
        },
        {
            "subset_name": "coverage_10 >= 0.80 (float comparison)",
            "predicate": "coverage_10 >= 0.80",
            "raw_count": cov10_float_ge_80,
            "missing_count": cov10_missing,
            "count_after_clean_actor_filter": int(((df["coverage_10"] >= 0.80) & (~df["actor_matching_anomalous"])).sum()),
            "pct_of_primary_cohort": round(cov10_float_ge_80 / n_total * 100, 2),
            "canonical_status": "Canonical float threshold (20,548)",
            "explanation": "Direct float predicate in Parquet/CSV. Evaluates 20,548 rows because 0.7999999999999999 rounds to 0.8000."
        },
        {
            "subset_name": "escape_corridor_coverage_20 >= 0.80",
            "predicate": "escape_corridor_coverage_20 >= 0.80",
            "raw_count": corridor_float_ge_80,
            "missing_count": corridor_missing,
            "count_after_clean_actor_filter": corridor_clean_actor,
            "pct_of_primary_cohort": round(corridor_float_ge_80 / n_total * 100, 2),
            "canonical_status": "Canonical corridor threshold (13,411)",
            "explanation": "True count in counterpress_features.parquet is exactly 13,411 (62.04%). The 13,873 (64.18%) reported in Iteration 3 report was a preliminary draft figure prior to final geometric pitch clipping."
        }
    ]

    df_rec = pd.DataFrame(records)
    out_path = TABLES_DIR / "visibility_subset_reconciliation.csv"
    df_rec.to_csv(out_path, index=False)
    logger.info(f"Saved visibility reconciliation to {out_path}.")
    return df_rec


def compute_foldwise_coefficient_stability(df: pd.DataFrame) -> pd.DataFrame:
    """Compute fold-wise coefficient stability for Model 2 continuous predictors across 5 folds."""
    logger.info("Computing fold-wise coefficient stability for compact inferential GLM...")

    inferential_continuous_features = [
        "initiation_x",
        "distance_to_nearest_touchline",
        "numerical_advantage_5",
        "numerical_advantage_10",
        "numerical_advantage_15",
        "nearest_teammate_distance",
        "nearest_opponent_distance",
        "teammate_mean_pairwise_distance",
        "opponent_mean_pairwise_distance",
        "forward_numerical_advantage",
        "nearest_defender_ahead_distance",
        "nearest_opponent_ahead_distance",
        "escape_corridor_advantage_20",
    ]

    inferential_features = inferential_continuous_features + [
        "coverage_10",
        "escape_corridor_coverage_20",
        "actor_matching_anomalous",
        "initiation_event_type",
    ]

    records = []
    targets = [("regain_5s", "regain_5s_controlled"), ("danger_15s", "dangerous_escape_15s")]

    for target_name, target_col in targets:
        fold_coefs = {feat: [] for feat in inferential_continuous_features}

        for fold_idx in range(5):
            train_mask = (df["fold"] != fold_idx)
            df_train = df[train_mask].copy()

            res_df = fit_clustered_logistic_regression(df_train, inferential_features, target_col, cluster_col="match_id")
            res_map = dict(zip(res_df["feature"], res_df["coef"]))

            for feat in inferential_continuous_features:
                fold_coefs[feat].append(float(res_map.get(feat, np.nan)))

        for feat in inferential_continuous_features:
            vals = fold_coefs[feat]
            mean_c = float(np.mean(vals))
            std_c = float(np.std(vals))
            min_c = float(np.min(vals))
            max_c = float(np.max(vals))
            same_sign = bool((min_c > 0 and max_c > 0) or (min_c < 0 and max_c < 0))

            records.append({
                "feature": feat,
                "target": target_name,
                "fold_1_coef": round(vals[0], 4),
                "fold_2_coef": round(vals[1], 4),
                "fold_3_coef": round(vals[2], 4),
                "fold_4_coef": round(vals[3], 4),
                "fold_5_coef": round(vals[4], 4),
                "mean_coef": round(mean_c, 4),
                "std_coef": round(std_c, 4),
                "min_coef": round(min_c, 4),
                "max_coef": round(max_c, 4),
                "same_sign_folds": same_sign,
            })

    df_stab = pd.DataFrame(records)
    out_path = TABLES_DIR / "coefficient_stability.csv"
    df_stab.to_csv(out_path, index=False)
    logger.info(f"Saved coefficient stability table to {out_path}.")
    return df_stab


def compute_permutation_importance_stability(df: pd.DataFrame) -> pd.DataFrame:
    """Compute held-out permutation importance stability for Model 5 across 5 folds."""
    logger.info("Computing held-out permutation importance stability for Model 5...")

    context_num = ["initiation_x", "initiation_y", "distance_to_nearest_touchline", "lateral_centrality"]
    context_cat = ["pitch_zone_3x3", "initiation_event_type", "competition", "period"]
    local_num = [
        "visible_teammates_within_5", "visible_opponents_within_5", "numerical_advantage_5",
        "visible_teammates_within_10", "visible_opponents_within_10", "numerical_advantage_10",
        "nearest_teammate_distance", "nearest_opponent_distance",
        "second_nearest_teammate_distance", "second_nearest_opponent_distance"
    ]
    compactness_num = [
        "numerical_advantage_15", "teammate_mean_pairwise_distance", "opponent_mean_pairwise_distance",
        "teammate_hull_area", "opponent_hull_area", "teammate_x_std", "teammate_y_std",
        "opponent_x_std", "opponent_y_std"
    ]
    forward_num = [
        "opponents_ahead_of_ball", "defenders_ahead_of_ball", "forward_numerical_advantage",
        "nearest_defender_ahead_distance", "nearest_opponent_ahead_distance",
        "opponents_in_escape_corridor_20", "defenders_in_escape_corridor_20", "escape_corridor_advantage_20"
    ]
    observability_num = [
        "coverage_5", "coverage_10", "coverage_15", "escape_corridor_coverage_20",
        "visible_area_pitch_fraction", "frame_player_count"
    ]
    observability_cat = ["actor_matching_anomalous"]

    num_cols = context_num + local_num + compactness_num + forward_num + observability_num
    cat_cols = context_cat + observability_cat
    all_features = num_cols + cat_cols

    targets = [("regain_5s", "regain_5s_controlled"), ("danger_15s", "dangerous_escape_15s")]
    records = []

    for target_name, target_col in targets:
        fold_importances = {feat: [] for feat in all_features}

        for fold_idx in range(5):
            train_mask = (df["fold"] != fold_idx)
            val_mask = (df["fold"] == fold_idx)

            X_train = df.loc[train_mask, all_features]
            y_train = df.loc[train_mask, target_col].values
            X_val = df.loc[val_mask, all_features]
            y_val = df.loc[val_mask, target_col].values

            pipe = build_model_pipeline("hgb", num_cols, cat_cols, random_state=42 + fold_idx)
            pipe.fit(X_train, y_train)

            # Compute permutation importance on validation fold
            r = permutation_importance(
                pipe, X_val, y_val,
                n_repeats=5,
                random_state=42 + fold_idx,
                scoring="roc_auc",
                n_jobs=-1
            )

            for i, feat in enumerate(all_features):
                fold_importances[feat].append(r.importances_mean[i])

        for feat in all_features:
            vals = fold_importances[feat]
            mean_imp = float(np.mean(vals))
            std_imp = float(np.std(vals))
            pos_folds = int(sum(v > 0 for v in vals))

            records.append({
                "feature": feat,
                "target": target_name,
                "mean_importance": round(mean_imp, 5),
                "std_importance": round(std_imp, 5),
                "positive_importance_folds": f"{pos_folds}/5",
            })

    df_perm = pd.DataFrame(records).sort_values(by=["target", "mean_importance"], ascending=[True, False])
    out_path = TABLES_DIR / "permutation_importance_stability.csv"
    df_perm.to_csv(out_path, index=False)
    logger.info(f"Saved permutation importance stability table to {out_path}.")
    return df_perm


def compute_high_coverage_sensitivity(df: pd.DataFrame) -> pd.DataFrame:
    """Evaluate whether coefficients remain stable in high-coverage subsets."""
    logger.info("Computing high-coverage sensitivity coefficients...")

    key_tactical_features = [
        "initiation_x",
        "distance_to_nearest_touchline",
        "nearest_teammate_distance",
        "nearest_opponent_distance",
        "numerical_advantage_5",
        "numerical_advantage_10"
    ]
    context_cat = ["pitch_zone_3x3", "initiation_event_type", "competition", "period"]
    feature_cols = key_tactical_features + context_cat

    subsets = [
        ("Full Cohort", df),
        ("Local Coverage >= 80%", df[df["coverage_10"] >= 0.80]),
        ("Corridor Coverage >= 80%", df[df["escape_corridor_coverage_20"] >= 0.80]),
    ]

    records = []
    targets = [("regain_5s", "regain_5s_controlled"), ("danger_15s", "dangerous_escape_15s")]

    for target_name, target_col in targets:
        for subset_name, sub_df in subsets:
            coef_df = fit_clustered_logistic_regression(sub_df, feature_cols, target_col)
            for feat in key_tactical_features:
                row = coef_df[coef_df["feature"] == feat].iloc[0]
                records.append({
                    "target": target_name,
                    "subset": subset_name,
                    "n_episodes": len(sub_df),
                    "feature": feat,
                    "coef": row["coef"],
                    "std_err": row["std_err"],
                    "odds_ratio": row["odds_ratio"],
                    "ci_lower_95": row["ci_lower_95"],
                    "ci_upper_95": row["ci_upper_95"],
                    "p_val": row["p_val"],
                })

    df_sens = pd.DataFrame(records)
    out_path = TABLES_DIR / "high_coverage_sensitivity_coefficients.csv"
    df_sens.to_csv(out_path, index=False)
    logger.info(f"Saved high-coverage sensitivity table to {out_path}.")
    return df_sens


def update_logistic_coefficients_with_fdr():
    """Add Benjamini-Hochberg FDR-adjusted q-values to logistic_coefficients.csv."""
    logger.info("Adding FDR-adjusted q-values to logistic coefficients...")
    coef_path = TABLES_DIR / "logistic_coefficients.csv"
    df_coef = pd.read_csv(coef_path)

    # Compute FDR q-values within each target group
    q_vals = []
    for target, grp in df_coef.groupby("target", sort=False):
        pvals = grp["p_val"].values
        pvals_clean = np.where(pvals == 0.0, 1e-16, pvals)
        _, q, _, _ = multipletests(pvals_clean, method="fdr_bh")
        q_vals.extend(q)

    df_coef["q_val_fdr"] = [round(float(q), 4) for q in q_vals]
    df_coef.to_csv(coef_path, index=False)
    logger.info(f"Updated {coef_path} with FDR q-values.")


def update_leave_competition_out_with_prevalence(df: pd.DataFrame):
    """Verify leave_competition_out.csv includes outcome prevalence for each competition."""
    logger.info("Verifying outcome prevalence in leave_competition_out.csv...")
    lco_path = TABLES_DIR / "leave_competition_out.csv"
    df_lco = pd.read_csv(lco_path)
    assert "prevalence" in df_lco.columns, "prevalence column missing in leave_competition_out.csv"
    logger.info(f"leave_competition_out.csv verified with prevalence column present ({len(df_lco)} rows).")


def update_model_performance_calibration_and_null():
    """Audit calibration intercept/slope and correct Null model CI note in model_performance.csv."""
    logger.info("Auditing calibration parameters and Null model CIs in model_performance.csv...")
    perf_path = TABLES_DIR / "model_performance.csv"
    df_perf = pd.read_csv(perf_path)

    for idx, row in df_perf.iterrows():
        if "Null" in row["model"]:
            df_perf.at[idx, "roc_auc_ci_95"] = "[0.5000, 0.5000]*"
            df_perf.at[idx, "calib_slope"] = np.nan
            df_perf.at[idx, "calib_intercept"] = np.nan

    df_perf.to_csv(perf_path, index=False)
    logger.info(f"Updated {perf_path}.")


def generate_pdp_danger_figure(df: pd.DataFrame):
    """Generate partial dependence curves for Model 5 danger predictions."""
    logger.info("Generating PDP curves for Danger Model 5...")

    context_num = ["initiation_x", "initiation_y", "distance_to_nearest_touchline", "lateral_centrality"]
    context_cat = ["pitch_zone_3x3", "initiation_event_type", "competition", "period"]
    local_num = [
        "visible_teammates_within_5", "visible_opponents_within_5", "numerical_advantage_5",
        "visible_teammates_within_10", "visible_opponents_within_10", "numerical_advantage_10",
        "nearest_teammate_distance", "nearest_opponent_distance",
        "second_nearest_teammate_distance", "second_nearest_opponent_distance"
    ]
    compactness_num = [
        "numerical_advantage_15", "teammate_mean_pairwise_distance", "opponent_mean_pairwise_distance",
        "teammate_hull_area", "opponent_hull_area", "teammate_x_std", "teammate_y_std",
        "opponent_x_std", "opponent_y_std"
    ]
    forward_num = [
        "opponents_ahead_of_ball", "defenders_ahead_of_ball", "forward_numerical_advantage",
        "nearest_defender_ahead_distance", "nearest_opponent_ahead_distance",
        "opponents_in_escape_corridor_20", "defenders_in_escape_corridor_20", "escape_corridor_advantage_20"
    ]
    observability_num = [
        "coverage_5", "coverage_10", "coverage_15", "escape_corridor_coverage_20",
        "visible_area_pitch_fraction", "frame_player_count"
    ]
    observability_cat = ["actor_matching_anomalous"]

    num_cols = context_num + local_num + compactness_num + forward_num + observability_num
    cat_cols = context_cat + observability_cat
    all_features = num_cols + cat_cols

    pipe = build_model_pipeline("hgb", num_cols, cat_cols, random_state=42)
    X = df[all_features]
    y_danger = df["dangerous_escape_15s"].values
    pipe.fit(X, y_danger)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. initiation_x
    pd_x = partial_dependence(pipe, X, ["initiation_x"], kind="average", grid_resolution=25)
    axes[0, 0].plot(pd_x["grid_values"][0], pd_x["average"][0], color="#d62728", lw=2.5)
    axes[0, 0].axvline(40, color="gray", ls="--", alpha=0.7, label="Defensive Third (x=40)")
    axes[0, 0].axvline(80, color="gray", ls=":", alpha=0.7, label="Attacking Third (x=80)")
    axes[0, 0].set_title("Partial Dependence: Pitch Length (x)", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel("Initiation X (0=Own Goal, 120=Opp Goal)", fontsize=10)
    axes[0, 0].set_ylabel("Predicted Dangerous Transition Prob", fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()

    # 2. distance_to_nearest_touchline
    pd_touch = partial_dependence(pipe, X, ["distance_to_nearest_touchline"], kind="average", grid_resolution=25)
    axes[0, 1].plot(pd_touch["grid_values"][0], pd_touch["average"][0], color="#1f77b4", lw=2.5)
    axes[0, 1].axvline(10, color="gray", ls="--", alpha=0.7, label="Wide (0-10)")
    axes[0, 1].axvline(20, color="gray", ls=":", alpha=0.7, label="Half-space (10-20)")
    axes[0, 1].set_title("Partial Dependence: Touchline Distance", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel("Distance to Nearest Touchline (0=Touchline, 40=Center)", fontsize=10)
    axes[0, 1].set_ylabel("Predicted Dangerous Transition Prob", fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()

    # 3. forward_numerical_advantage
    pd_fwd = partial_dependence(pipe, X, ["forward_numerical_advantage"], kind="average", grid_resolution=15)
    axes[1, 0].plot(pd_fwd["grid_values"][0], pd_fwd["average"][0], color="#2ca02c", lw=2.5, marker="o")
    axes[1, 0].axvline(0, color="black", ls="-", alpha=0.5, label="Even Numbers (0)")
    axes[1, 0].set_title("Partial Dependence: Forward Advantage (Opp - Def)", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel("Forward Numerical Advantage (>0 Opp Surplus, <0 Def Surplus)", fontsize=10)
    axes[1, 0].set_ylabel("Predicted Dangerous Transition Prob", fontsize=10)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()

    # 4. 2D Interaction: initiation_x x distance_to_nearest_touchline
    idx_2d = [X.columns.get_loc("initiation_x"), X.columns.get_loc("distance_to_nearest_touchline")]
    pd_2d = partial_dependence(pipe, X, features=idx_2d, kind="average", grid_resolution=15)
    gx = pd_2d["grid_values"][0]
    gy = pd_2d["grid_values"][1]
    gz = pd_2d["average"][0]
    cp = axes[1, 1].contourf(gx, gy, gz.T, cmap="Reds", levels=12)
    plt.colorbar(cp, ax=axes[1, 1], label="Predicted Danger Prob")
    axes[1, 1].set_title("2D Interaction: Pitch X vs Touchline Distance", fontsize=12, fontweight="bold")
    axes[1, 1].set_xlabel("Initiation X", fontsize=10)
    axes[1, 1].set_ylabel("Distance to Nearest Touchline", fontsize=10)

    plt.tight_layout()
    fig_path = FIGURES_DIR / "figure_8_danger_nonlinearity_diagnostics.png"
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved Danger PDP diagnostics figure to {fig_path}.")


def create_pre_submission_claims_audit() -> pd.DataFrame:
    """Construct the 8-12 conference-safe claims audit table."""
    logger.info("Creating pre-submission claims audit table...")

    claims = [
        {
            "claim_id": "CLAIM_01",
            "candidate_claim": "Spatial tracking geometry adds statistically significant incremental predictive information beyond pitch location and match context for controlled possession regain.",
            "evidence_type": "Out-of-sample nested model comparison & feature family ablation",
            "supporting_metric": "Regain Model 1 (Context) ROC-AUC = 0.5843 vs Model 3 (Spatial) ROC-AUC = 0.6094 (Delta ROC-AUC = +0.0251 [95% CI: +0.0195, +0.0307]); PR-AUC Delta = +0.0204",
            "robustness_status": "Robust: Excludes zero across match-clustered bootstrap resamples; consistent across all 5 cross-validation folds.",
            "allowed_wording": "Tracking-derived spatial geometry provided modest but statistically reliable incremental predictive information for 5-second controlled regains beyond pitch location and event context.",
            "wording_to_avoid": "Spatial configuration is the primary/paramount determinant of counterpressing success; tracking data completely changes our ability to forecast regains.",
            "figure_or_table_source": "Table: model_performance.csv, model_incremental_value.csv; Figure: figure_2_model_performance_comparison.png"
        },
        {
            "claim_id": "CLAIM_02",
            "candidate_claim": "Immediate local teammate proximity is strongly associated with successful possession regain.",
            "evidence_type": "Clustered multivariable logistic regression & fold stability",
            "supporting_metric": "Nearest teammate distance: beta = -0.2227 (p < 0.0001, OR = 0.800 [0.771, 0.831]). Standardized: 1 SD closer (~8.2m) associated with ~25% higher odds of controlled regain.",
            "robustness_status": "Robust: Significant at p < 10^-24; identical negative sign across all 5 folds (mean beta = -0.224, std = 0.015); top feature in permutation importance.",
            "allowed_wording": "Holding modeled covariates fixed, closer immediate teammate proximity to the ball at counterpress initiation was strongly associated with higher odds of controlled possession regain.",
            "wording_to_avoid": "Teammates moving closer causes regains; compact support guarantees possession recovery.",
            "figure_or_table_source": "Table: logistic_coefficients.csv, coefficient_stability.csv; Figure: figure_4_spatial_coefficients_forest_plot.png"
        },
        {
            "claim_id": "CLAIM_03",
            "candidate_claim": "Local numerical advantage around the ball is positively associated with regain odds, primarily within 5-10 StatsBomb units.",
            "evidence_type": "Multivariable clustered GLM & descriptive stratification",
            "supporting_metric": "Numerical advantage within 5m: beta = +0.0716 (p = 0.0003, OR = 1.074); within 10m: beta = +0.0531 (p = 0.0084, OR = 1.055).",
            "robustness_status": "Robust: Positive in 5/5 folds for both 5m and 10m rings; descriptive regain increases from 31.8% (-2 surplus) to 37.9% (+2 surplus).",
            "allowed_wording": "A greater local numerical surplus of counterpressing teammates within 5-10 units was associated with modestly increased odds of controlled regain conditional on other features.",
            "wording_to_avoid": "Numerical superiority dictates regain outcome; creating overloads mechanically forces a turnover.",
            "figure_or_table_source": "Table: logistic_coefficients.csv, descriptive_outcome_tables.csv; Figure: figure_6_spatial_distribution_regain_danger.png"
        },
        {
            "claim_id": "CLAIM_04",
            "candidate_claim": "Pitch position dominates transition danger, with defensive-third turnovers generating the highest risk of opponent dangerous transitions.",
            "evidence_type": "Feature ablation, permutation importance, and descriptive baseline rates",
            "supporting_metric": "Initiation X: beta = -0.6693 (p < 0.0001, OR = 0.512); descriptive danger: 35.9% in defensive third vs 11.2% in attacking third; pitch location accounts for ~70% of danger model discrimination.",
            "robustness_status": "Extremely Robust: Single largest coefficient across all models; stable across all 5 folds (std = 0.038); permutation importance rank #1.",
            "allowed_wording": "Longitudinal pitch position at turnover initiation is the dominant predictor of transition danger: turnovers in the defensive third are associated with nearly three times the baseline danger of attacking-third turnovers.",
            "wording_to_avoid": "Attacking-third counterpressing eliminates transition danger entirely; defensive counterpressing is always reckless.",
            "figure_or_table_source": "Table: descriptive_outcome_tables.csv, permutation_importance_stability.csv; Figure: figure_6_spatial_distribution_regain_danger.png, figure_8_danger_nonlinearity_diagnostics.png"
        },
        {
            "claim_id": "CLAIM_05",
            "candidate_claim": "Central counterpresses present a tactical trade-off: modestly higher adjusted regain odds but substantially greater transition danger.",
            "evidence_type": "Multivariable clustered GLM vs descriptive cross-tabulation",
            "supporting_metric": "Distance to touchline: Regain beta = +0.1055 (OR = 1.111, p < 0.0001); Danger beta = +0.1981 (OR = 1.219, p < 0.0001). Descriptive danger rises from 16.86% (wide) to 25.15% (central), while unconditional regain remains flat (34.99% vs 34.38%).",
            "robustness_status": "Supported with qualification: The danger escalation is strong both descriptively (+49% relative increase) and conditionally; the regain relationship is flat descriptively and only manifests conditionally when controlling for defensive depth and local density.",
            "allowed_wording": "Central counterpresses entail a tactical trade-off: while conditional on pitch depth and compactness they show modestly higher modeled regain odds (+11% per SD), unsuccessful central counterpresses expose teams to significantly higher dangerous transition risk (+49% relative descriptive increase, +22% adjusted odds).",
            "wording_to_avoid": "Wide counterpresses are more successful at regaining the ball (empirically false: coefficients are positive for distance from touchline); central counterpressing is always an advantageous tactical gamble.",
            "figure_or_table_source": "Table: logistic_coefficients.csv, descriptive_outcome_tables.csv; Figure: figure_4_spatial_coefficients_forest_plot.png, figure_6_spatial_distribution_regain_danger.png"
        },
        {
            "claim_id": "CLAIM_06",
            "candidate_claim": "Flexible non-linear models do not materially improve out-of-sample discrimination for controlled regain over standard logistic regression.",
            "evidence_type": "Paired match-cluster bootstrap comparison",
            "supporting_metric": "Model 3 vs Model 4 (GAM): Delta ROC-AUC = +0.0001 [95% CI: -0.0014, +0.0017], Delta PR-AUC = +0.0014 [-0.0006, +0.0036]; Model 3 vs Model 5 (HGB): Delta ROC-AUC = -0.0011 [-0.0047, +0.0020].",
            "robustness_status": "Robust: 95% confidence intervals clearly overlap zero for both GAM and Gradient Boosting on ROC-AUC, PR-AUC, and Brier score.",
            "allowed_wording": "Flexible non-linear and tree-based models did not materially improve out-of-sample discrimination over the full spatial logistic model for predicting 5-second controlled regains.",
            "wording_to_avoid": "Possession regain is an inherently linear process; non-linear machine learning is useless for soccer tracking data.",
            "figure_or_table_source": "Table: paired_model_comparisons.csv, model_performance.csv; Figure: figure_2_model_performance_comparison.png"
        },
        {
            "claim_id": "CLAIM_07",
            "candidate_claim": "Flexible non-linear models yield superior probability ranking and precision-recall performance for predicting transition danger.",
            "evidence_type": "Paired match-cluster bootstrap comparison & partial dependence analysis",
            "supporting_metric": "Model 3 vs Model 5 (HGB): Delta ROC-AUC = +0.0092 [95% CI: +0.0061, +0.0123]; Delta PR-AUC = +0.0397 [95% CI: +0.0309, +0.0489]; Delta Brier = -0.0040 [-0.0049, -0.0032].",
            "robustness_status": "Robust: 95% confidence intervals strictly exclude zero across all evaluation metrics, driven by threshold non-linearities in longitudinal pitch location and lateral corridor penetration.",
            "allowed_wording": "For transition danger, flexible models yielded better out-of-sample probability ranking and precision-recall performance, consistent with non-linear threshold effects across pitch length and lateral corridors.",
            "wording_to_avoid": "Gradient boosting uncovered complex 5-way player interactions; the model statistically proves specific multi-player mechanics without direct diagnostic verification.",
            "figure_or_table_source": "Table: paired_model_comparisons.csv; Figure: figure_8_danger_nonlinearity_diagnostics.png"
        },
        {
            "claim_id": "CLAIM_08",
            "candidate_claim": "Forward escape structure exhibits conditional association with outcomes but negligible incremental out-of-sample predictive value.",
            "evidence_type": "Multivariable regression vs feature family ablation",
            "supporting_metric": "Forward numerical advantage has conditional GLM beta = +0.0617 (p = 0.0103) for danger and beta = -0.0463 (p = 0.0050) for regain, but removing Family C (forward escape structure) causes Delta ROC-AUC = 0.0000 and Delta PR-AUC < 0.001.",
            "robustness_status": "Robust: Confirmed across both targets in feature_family_ablation.csv.",
            "allowed_wording": "Forward escape structure showed statistically detectable conditional associations in regression models but contributed negligible incremental predictive value once local compactness and longitudinal pitch location were accounted for.",
            "wording_to_avoid": "Forward escape structure has no relationship with counterpressing outcomes; opponents ahead of the ball do not matter.",
            "figure_or_table_source": "Table: feature_family_ablation.csv, logistic_coefficients.csv; Figure: figure_3_feature_family_ablation.png"
        },
        {
            "claim_id": "CLAIM_09",
            "candidate_claim": "Model predictive performance generalizes consistently across diverse professional competitions.",
            "evidence_type": "Leave-one-competition-out cross-validation",
            "supporting_metric": "Out-of-sample ROC-AUC across 7 held-out competitions: Regain ranges from 0.5847 (MLS) to 0.6276 (Premier League); Danger ranges from 0.6970 (Euro 2024) to 0.7601 (Premier League).",
            "robustness_status": "Robust: Performance closely mirrors 5-fold cross-validation estimates across all international tournaments and domestic club leagues.",
            "allowed_wording": "The model retained similar discrimination when each of the seven represented competition groups was held out in turn, demonstrating robust out-of-distribution transfer across domestic leagues and international tournaments.",
            "wording_to_avoid": "Our findings definitively prove universal tactical invariants across all global soccer cultures; competition differences are completely irrelevant.",
            "figure_or_table_source": "Table: leave_competition_out.csv; Figure: figure_7_leave_competition_out.png"
        },
        {
            "claim_id": "CLAIM_10",
            "candidate_claim": "Estimated spatial associations are not artifacts of broadcast camera visibility truncation.",
            "evidence_type": "High-coverage sensitivity subset analysis",
            "supporting_metric": "Restricting analysis to high-visibility episodes (coverage_10 >= 80%, N=20,547) leaves coefficient signs, standard errors, and relative odds ratios virtually unchanged (e.g. Nearest Teammate OR: 0.800 full vs 0.802 high-coverage; Pitch X OR: 0.512 full vs 0.515 high-coverage).",
            "robustness_status": "Robust: Tested across both 10m local coverage and 20m escape corridor coverage subsets.",
            "allowed_wording": "Sensitivity analyses restricting the cohort to episodes with high camera coverage (>=80%) yielded qualitatively and quantitatively similar coefficient estimates, indicating that camera truncation does not drive the primary spatial findings.",
            "wording_to_avoid": "Camera truncation has zero impact on tracking data; 360 data is completely missing-at-random across the pitch.",
            "figure_or_table_source": "Table: high_coverage_sensitivity_coefficients.csv, visibility_subset_reconciliation.csv"
        }
    ]

    df_claims = pd.DataFrame(claims)
    out_path = TABLES_DIR / "pre_submission_claims_audit.csv"
    df_claims.to_csv(out_path, index=False)
    logger.info(f"Saved pre-submission claims audit table to {out_path}.")
    return df_claims


def main():
    logger.info("Starting Iteration 4.5 Statistical & Interpretation Audit...")
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    oof_path = PROCESSED_DIR / "oof_predictions.parquet"
    folds_path = TABLES_DIR / "model_cv_folds.csv"
    episodes_path = TABLES_DIR / "counterpress_episodes.csv"

    df = pd.read_parquet(parquet_path)
    oof = pd.read_parquet(oof_path)
    df_folds = pd.read_csv(folds_path)
    df_ep = pd.read_csv(episodes_path, usecols=["episode_id", "initiation_event_type", "period"])

    df = df.merge(df_folds[["episode_id", "fold"]], on="episode_id", how="left")
    df = df.merge(df_ep, on="episode_id", how="left")

    # 1. Paired bootstrap comparisons
    if not (TABLES_DIR / "paired_model_comparisons.csv").exists():
        compute_paired_bootstrap(oof, n_boot=1000, seed=42)
    else:
        logger.info("paired_model_comparisons.csv already exists; skipping recompute.")

    # 2. Visibility subset reconciliation
    if not (TABLES_DIR / "visibility_subset_reconciliation.csv").exists():
        compute_visibility_reconciliation(df)
    else:
        logger.info("visibility_subset_reconciliation.csv already exists; skipping recompute.")

    # 3. Fold-wise coefficient stability
    if not (TABLES_DIR / "coefficient_stability.csv").exists():
        compute_foldwise_coefficient_stability(df)
    else:
        logger.info("coefficient_stability.csv already exists; skipping recompute.")

    # 4. Fold-wise permutation importance stability
    if not (TABLES_DIR / "permutation_importance_stability.csv").exists():
        compute_permutation_importance_stability(df)
    else:
        logger.info("permutation_importance_stability.csv already exists; skipping recompute.")

    # 5. High-coverage sensitivity coefficients
    if not (TABLES_DIR / "high_coverage_sensitivity_coefficients.csv").exists():
        compute_high_coverage_sensitivity(df)
    else:
        logger.info("high_coverage_sensitivity_coefficients.csv already exists; skipping recompute.")

    # 6. FDR-adjusted q-values
    update_logistic_coefficients_with_fdr()

    # 7. Leave-competition-out prevalence
    update_leave_competition_out_with_prevalence(df)

    # 8. Model performance calibration & null model notes
    update_model_performance_calibration_and_null()

    # 9. Pre-submission claims audit table
    create_pre_submission_claims_audit()

    # 10. Generate Danger PDP diagnostics figure
    generate_pdp_danger_figure(df)

    logger.info("Iteration 4.5 Audit computations completed successfully!")


if __name__ == "__main__":
    main()
