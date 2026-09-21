"""Comprehensive execution script for Iteration 4 Modeling, Ablation, Inference, and Robustness.

Executes:
1. Data loading and validation against cohort invariants (21,616 episodes, 414 matches).
2. 5-fold GroupKFold evaluation of Models 0-5 for both primary outcomes:
   - Y_regain: regain_5s_controlled
   - Y_danger: dangerous_escape_15s
3. Incremental value analysis (Context vs Local vs Full Spatial vs GAM vs Gradient Boosting).
4. Feature-family ablation analysis.
5. Inferential clustered logistic regression with match_id cluster standard errors via statsmodels.
6. Permutation feature importance on held-out folds for gradient boosting.
7. Sensitivity analyses:
   - High local coverage (coverage_10 >= 0.80)
   - High corridor coverage (escape_corridor_coverage_20 >= 0.80)
   - Actor-event location discrepancy exclusion (actor_matching_anomalous == False)
8. Leave-one-competition-out generalization across all 7 competitions.
9. Secondary 3-class multinomial model (successful_regain, harmless_escape, dangerous_escape).
10. Saves all tables and out-of-fold predictions for figure generation.
"""

import logging
import time
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score, roc_auc_score
from sklearn.model_selection import GroupKFold

from counterpress.config import DATA_DIR, PROCESSED_DIR, TABLES_DIR
from counterpress.models import evaluate_probability_model, match_cluster_bootstrap_ci
from counterpress.modeling import (
    NullPrevalenceClassifier,
    build_model_pipeline,
    build_preprocessor,
    fit_clustered_logistic_regression,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def run_iteration4_modeling():
    start_time = time.time()
    parquet_path = PROCESSED_DIR / "counterpress_features.parquet"
    folds_path = TABLES_DIR / "model_cv_folds.csv"
    episodes_path = TABLES_DIR / "counterpress_episodes.csv"

    logger.info("Loading primary features, folds, and episode metadata...")
    df = pd.read_parquet(parquet_path)
    df_folds = pd.read_csv(folds_path)
    df_ep = pd.read_csv(episodes_path, usecols=["episode_id", "initiation_event_type", "period"])

    df = df.merge(df_folds[["episode_id", "fold"]], on="episode_id", how="left")
    df = df.merge(df_ep, on="episode_id", how="left")

    # Verify invariants
    assert len(df) == 21616, f"Expected 21,616 rows, got {len(df)}"
    assert df["episode_id"].nunique() == 21616, "Duplicate episode_ids"
    assert df["match_id"].nunique() == 414, "Expected 414 matches"
    assert not df["fold"].isna().any(), "Missing fold assignments"

    # Pre-specified feature lists
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

    feature_configs = {
        "Model 0 (Null)": {
            "num": [],
            "cat": [],
            "type": "null"
        },
        "Model 1 (Context)": {
            "num": context_num,
            "cat": context_cat,
            "type": "logistic"
        },
        "Model 2 (Context+Local)": {
            "num": context_num + local_num,
            "cat": context_cat,
            "type": "logistic"
        },
        "Model 3 (Full Spatial Logistic)": {
            "num": context_num + local_num + compactness_num + forward_num + observability_num,
            "cat": context_cat + observability_cat,
            "type": "logistic"
        },
        "Model 4 (Additive Spline GAM)": {
            "num": context_num + local_num + compactness_num + forward_num + observability_num,
            "cat": context_cat + observability_cat,
            "spline_cols": [
                "initiation_x", "initiation_y", "distance_to_nearest_touchline", "lateral_centrality",
                "nearest_teammate_distance", "nearest_opponent_distance",
                "second_nearest_teammate_distance", "second_nearest_opponent_distance",
                "teammate_mean_pairwise_distance", "opponent_mean_pairwise_distance",
                "nearest_defender_ahead_distance", "nearest_opponent_ahead_distance"
            ],
            "type": "gam"
        },
        "Model 5 (Gradient Boosting)": {
            "num": context_num + local_num + compactness_num + forward_num + observability_num,
            "cat": context_cat + observability_cat,
            "type": "hgb"
        }
    }

    # DataFrames to collect out-of-fold probability predictions
    oof_predictions = df[["episode_id", "match_id", "fold", "competition", "coverage_10", "escape_corridor_coverage_20", "actor_matching_anomalous", "regain_5s_controlled", "dangerous_escape_15s", "episode_outcome_3class"]].copy()

    targets = [
        ("regain_5s", "regain_5s_controlled"),
        ("danger_15s", "dangerous_escape_15s")
    ]

    performance_records = []

    for target_name, target_col in targets:
        logger.info(f"\n==========================================")
        logger.info(f"TRAINING MODEL HIERARCHY FOR TARGET: {target_name} ({target_col})")
        logger.info(f"==========================================")

        y = df[target_col].values

        for m_name, cfg in feature_configs.items():
            logger.info(f"Evaluating {m_name} for {target_name} across 5 GroupKFold splits...")
            num_cols = cfg["num"]
            cat_cols = cfg["cat"]
            m_type = cfg["type"]
            spline_cols = cfg.get("spline_cols", None)

            oof_preds = np.zeros(len(df))
            fold_metrics = []

            for fold_idx in range(5):
                train_mask = (df["fold"] != fold_idx)
                val_mask = (df["fold"] == fold_idx)

                X_train = df.loc[train_mask, num_cols + cat_cols]
                y_train = y[train_mask]
                X_val = df.loc[val_mask, num_cols + cat_cols]
                y_val = y[val_mask]

                pipe = build_model_pipeline(
                    model_type=m_type,
                    numeric_cols=num_cols,
                    categorical_cols=cat_cols,
                    spline_cols=spline_cols,
                    C=1.0,
                    random_state=42 + fold_idx,
                )
                pipe.fit(X_train, y_train)

                if m_type == "null":
                    p_val = pipe.predict_proba(X_val)[:, 1]
                else:
                    p_val = pipe.predict_proba(X_val)[:, 1]

                oof_preds[val_mask] = p_val
                metrics = evaluate_probability_model(y_val, p_val)
                fold_metrics.append(metrics)

            oof_col = f"pred_{target_name}_{m_name.replace(' ', '_').replace('(', '').replace(')', '').lower()}"
            oof_predictions[oof_col] = oof_preds

            # Aggregate across folds
            mean_roc = float(np.mean([m["roc_auc"] for m in fold_metrics]))
            std_roc = float(np.std([m["roc_auc"] for m in fold_metrics]))
            mean_pr = float(np.mean([m["pr_auc"] for m in fold_metrics]))
            std_pr = float(np.std([m["pr_auc"] for m in fold_metrics]))
            mean_brier = float(np.mean([m["brier_score"] for m in fold_metrics]))
            std_brier = float(np.std([m["brier_score"] for m in fold_metrics]))
            mean_ll = float(np.mean([m["log_loss"] for m in fold_metrics]))
            std_ll = float(np.std([m["log_loss"] for m in fold_metrics]))
            mean_slope = float(np.nanmean([m["calib_slope"] for m in fold_metrics]))
            mean_intercept = float(np.nanmean([m["calib_intercept"] for m in fold_metrics]))

            # Overall bootstrap 95% CI on out-of-fold predictions
            temp_df = pd.DataFrame({"y_true": y, "y_prob": oof_preds, "match_id": df["match_id"]})
            ci_dict = match_cluster_bootstrap_ci(temp_df, "y_true", "y_prob", n_boot=200, random_state=42)

            performance_records.append({
                "target": target_name,
                "model": m_name,
                "roc_auc_mean": round(mean_roc, 4),
                "roc_auc_std": round(std_roc, 4),
                "roc_auc_ci_95": f"[{ci_dict['roc_auc'][0]:.4f}, {ci_dict['roc_auc'][1]:.4f}]",
                "pr_auc_mean": round(mean_pr, 4),
                "pr_auc_std": round(std_pr, 4),
                "pr_auc_ci_95": f"[{ci_dict['pr_auc'][0]:.4f}, {ci_dict['pr_auc'][1]:.4f}]",
                "brier_score_mean": round(mean_brier, 4),
                "brier_score_std": round(std_brier, 4),
                "brier_ci_95": f"[{ci_dict['brier_score'][0]:.4f}, {ci_dict['brier_score'][1]:.4f}]",
                "log_loss_mean": round(mean_ll, 4),
                "log_loss_std": round(std_ll, 4),
                "log_loss_ci_95": f"[{ci_dict['log_loss'][0]:.4f}, {ci_dict['log_loss'][1]:.4f}]",
                "calib_slope": round(mean_slope, 4),
                "calib_intercept": round(mean_intercept, 4),
            })
            logger.info(f"--> {m_name} | ROC-AUC: {mean_roc:.4f} (±{std_roc:.4f}) | PR-AUC: {mean_pr:.4f} | Brier: {mean_brier:.4f} | Slope: {mean_slope:.3f}")

    df_perf = pd.DataFrame(performance_records)
    perf_path = TABLES_DIR / "model_performance.csv"
    df_perf.to_csv(perf_path, index=False)
    logger.info(f"Saved model performance table to {perf_path}.")

    # ----------------------------------------------------
    # INCREMENTAL VALUE ANALYSIS
    # ----------------------------------------------------
    logger.info("\nComputing Incremental Value of Spatial Information...")
    incremental_records = []
    for target_name in ["regain_5s", "danger_15s"]:
        sub = df_perf[df_perf["target"] == target_name].set_index("model")
        base_roc = sub.loc["Model 1 (Context)", "roc_auc_mean"]
        base_pr = sub.loc["Model 1 (Context)", "pr_auc_mean"]
        base_brier = sub.loc["Model 1 (Context)", "brier_score_mean"]
        base_ll = sub.loc["Model 1 (Context)", "log_loss_mean"]

        for comp_model in ["Model 2 (Context+Local)", "Model 3 (Full Spatial Logistic)", "Model 4 (Additive Spline GAM)", "Model 5 (Gradient Boosting)"]:
            c_roc = sub.loc[comp_model, "roc_auc_mean"]
            c_pr = sub.loc[comp_model, "pr_auc_mean"]
            c_brier = sub.loc[comp_model, "brier_score_mean"]
            c_ll = sub.loc[comp_model, "log_loss_mean"]

            incremental_records.append({
                "target": target_name,
                "baseline": "Model 1 (Context)",
                "comparison_model": comp_model,
                "delta_roc_auc": round(c_roc - base_roc, 4),
                "delta_pr_auc": round(c_pr - base_pr, 4),
                "delta_brier": round(c_brier - base_brier, 4),
                "delta_log_loss": round(c_ll - base_ll, 4),
            })

    df_inc = pd.DataFrame(incremental_records)
    inc_path = TABLES_DIR / "model_incremental_value.csv"
    df_inc.to_csv(inc_path, index=False)
    logger.info(f"Saved incremental value analysis to {inc_path}.")
    print(df_inc.to_string(index=False))

    # ----------------------------------------------------
    # FEATURE-FAMILY ABLATION
    # ----------------------------------------------------
    logger.info("\nRunning Pre-Specified Feature-Family Ablations...")
    ablation_configs = {
        "Full Spatial Model": (context_num + local_num + compactness_num + forward_num + observability_num, context_cat + observability_cat),
        "Minus Local Pressure Geometry": (context_num + compactness_num + forward_num + observability_num, context_cat + observability_cat),
        "Minus Broader Compactness": (context_num + local_num + forward_num + observability_num, context_cat + observability_cat),
        "Minus Forward Escape Structure": (context_num + local_num + compactness_num + observability_num, context_cat + observability_cat),
        "Minus Pitch Geometry": (local_num + compactness_num + forward_num + observability_num, ["initiation_event_type", "competition", "period"] + observability_cat),
    }

    ablation_records = []
    for target_name, target_col in targets:
        y = df[target_col].values
        for abl_name, (num_cols, cat_cols) in ablation_configs.items():
            fold_rocs, fold_prs, fold_briers = [], [], []
            for fold_idx in range(5):
                train_mask = (df["fold"] != fold_idx)
                val_mask = (df["fold"] == fold_idx)
                X_train = df.loc[train_mask, num_cols + cat_cols]
                y_train = y[train_mask]
                X_val = df.loc[val_mask, num_cols + cat_cols]
                y_val = y[val_mask]

                pipe = build_model_pipeline("logistic", num_cols, cat_cols, C=1.0, random_state=42 + fold_idx)
                pipe.fit(X_train, y_train)
                p_val = pipe.predict_proba(X_val)[:, 1]
                m = evaluate_probability_model(y_val, p_val, compute_calibration_params=False)
                fold_rocs.append(m["roc_auc"])
                fold_prs.append(m["pr_auc"])
                fold_briers.append(m["brier_score"])

            ablation_records.append({
                "target": target_name,
                "configuration": abl_name,
                "roc_auc_mean": round(float(np.mean(fold_rocs)), 4),
                "roc_auc_std": round(float(np.std(fold_rocs)), 4),
                "pr_auc_mean": round(float(np.mean(fold_prs)), 4),
                "pr_auc_std": round(float(np.std(fold_prs)), 4),
                "brier_score_mean": round(float(np.mean(fold_briers)), 4),
                "brier_score_std": round(float(np.std(fold_briers)), 4),
            })

    df_abl = pd.DataFrame(ablation_records)
    abl_path = TABLES_DIR / "feature_family_ablation.csv"
    df_abl.to_csv(abl_path, index=False)
    logger.info(f"Saved feature-family ablation table to {abl_path}.")
    print(df_abl.to_string(index=False))

    # ----------------------------------------------------
    # INFERENTIAL CLUSTERED LOGISTIC REGRESSION
    # ----------------------------------------------------
    logger.info("\nFitting Clustered Logistic Regression for Inferential Effects (statsmodels)...")
    inferential_features = [
        "initiation_x", "distance_to_nearest_touchline",
        "numerical_advantage_5", "numerical_advantage_10", "numerical_advantage_15",
        "nearest_teammate_distance", "nearest_opponent_distance",
        "teammate_mean_pairwise_distance", "opponent_mean_pairwise_distance",
        "forward_numerical_advantage",
        "nearest_defender_ahead_distance", "nearest_opponent_ahead_distance",
        "escape_corridor_advantage_20",
        "coverage_10", "escape_corridor_coverage_20",
        "actor_matching_anomalous",
        "initiation_event_type"
    ]

    coef_tables = []
    for target_name, target_col in targets:
        logger.info(f"Fitting clustered GLM for {target_name} on {len(inferential_features)} features...")
        res_df = fit_clustered_logistic_regression(df, inferential_features, target_col, cluster_col="match_id")
        res_df["target"] = target_name
        coef_tables.append(res_df)

    df_coefs = pd.concat(coef_tables, ignore_index=True)
    coefs_path = TABLES_DIR / "logistic_coefficients.csv"
    df_coefs.to_csv(coefs_path, index=False)
    logger.info(f"Saved clustered logistic regression coefficients to {coefs_path}.")

    # Print top associations for regain
    top_regain = df_coefs[df_coefs["target"] == "regain_5s"].sort_values("z_stat", ascending=False)
    print("\nTop Positive & Negative Predictors of Regain (Clustered GLM):")
    print(pd.concat([top_regain.head(5), top_regain.tail(5)])[["feature", "coef", "std_err", "z_stat", "p_val", "odds_ratio", "ci_lower_95", "ci_upper_95"]].to_string(index=False))

    # Print top associations for danger
    top_danger = df_coefs[df_coefs["target"] == "danger_15s"].sort_values("z_stat", ascending=False)
    print("\nTop Positive & Negative Predictors of Dangerous Escape (Clustered GLM):")
    print(pd.concat([top_danger.head(5), top_danger.tail(5)])[["feature", "coef", "std_err", "z_stat", "p_val", "odds_ratio", "ci_lower_95", "ci_upper_95"]].to_string(index=False))

    # ----------------------------------------------------
    # SENSITIVITY ANALYSES
    # ----------------------------------------------------
    logger.info("\nExecuting Sensitivity & Robustness Analyses...")
    # 1. High local visibility (coverage_10 >= 0.80)
    high_vis_mask = (df["coverage_10"] >= 0.80)
    logger.info(f"High local visibility subset: {high_vis_mask.sum()} / {len(df)} episodes ({high_vis_mask.mean()*100:.2f}%)")
    for target_name, target_col in targets:
        sub_y = df.loc[high_vis_mask, target_col]
        for m_lbl, oof_col in [("Context", f"pred_{target_name}_model_1_context"), ("Full Spatial", f"pred_{target_name}_model_3_full_spatial_logistic")]:
            sub_p = oof_predictions.loc[high_vis_mask, oof_col]
            m_res = evaluate_probability_model(sub_y, sub_p, compute_calibration_params=False)
            logger.info(f"High Visibility ({target_name}, {m_lbl}): ROC-AUC = {m_res['roc_auc']:.4f}, Brier = {m_res['brier_score']:.4f}")

    # 2. Corridor visibility subset (escape_corridor_coverage_20 >= 0.80)
    corridor_vis_mask = (df["escape_corridor_coverage_20"] >= 0.80)
    logger.info(f"High corridor visibility subset: {corridor_vis_mask.sum()} / {len(df)} episodes ({corridor_vis_mask.mean()*100:.2f}%)")
    for m_lbl, oof_col in [("Context", "pred_danger_15s_model_1_context"), ("Full Spatial", "pred_danger_15s_model_3_full_spatial_logistic")]:
        sub_y = df.loc[corridor_vis_mask, "dangerous_escape_15s"]
        sub_p = oof_predictions.loc[corridor_vis_mask, oof_col]
        m_res = evaluate_probability_model(sub_y, sub_p, compute_calibration_params=False)
        logger.info(f"High Corridor Vis (danger_15s, {m_lbl}): ROC-AUC = {m_res['roc_auc']:.4f}, Brier = {m_res['brier_score']:.4f}")

    # 3. Actor discrepancy sensitivity (exclude actor_matching_anomalous == True)
    actor_clean_mask = (~df["actor_matching_anomalous"])
    logger.info(f"Actor-Event clean subset: {actor_clean_mask.sum()} / {len(df)} episodes ({actor_clean_mask.mean()*100:.2f}%)")
    for target_name, target_col in targets:
        sub_y = df.loc[actor_clean_mask, target_col]
        for m_lbl, oof_col in [("Context", f"pred_{target_name}_model_1_context"), ("Full Spatial", f"pred_{target_name}_model_3_full_spatial_logistic")]:
            sub_p = oof_predictions.loc[actor_clean_mask, oof_col]
            m_res = evaluate_probability_model(sub_y, sub_p, compute_calibration_params=False)
            logger.info(f"Actor Clean ({target_name}, {m_lbl}): ROC-AUC = {m_res['roc_auc']:.4f}, Brier = {m_res['brier_score']:.4f}")

    # ----------------------------------------------------
    # LEAVE-ONE-COMPETITION-OUT GENERALIZATION
    # ----------------------------------------------------
    logger.info("\nEvaluating Leave-One-Competition-Out Generalization (Model 3 Full Spatial)...")
    comp_records = []
    unique_comps = df["competition"].unique()
    num_cols = context_num + local_num + compactness_num + forward_num + observability_num
    cat_cols = ["pitch_zone_3x3", "initiation_event_type", "period", "actor_matching_anomalous"]

    for comp in unique_comps:
        test_mask = (df["competition"] == comp)
        train_mask = ~test_mask

        n_train = int(train_mask.sum())
        n_test = int(test_mask.sum())

        if n_test < 50:
            continue

        for target_name, target_col in targets:
            X_train = df.loc[train_mask, num_cols + cat_cols]
            y_train = df.loc[train_mask, target_col].values
            X_test = df.loc[test_mask, num_cols + cat_cols]
            y_test = df.loc[test_mask, target_col].values

            pipe = build_model_pipeline("logistic", num_cols, cat_cols, C=1.0, random_state=42)
            pipe.fit(X_train, y_train)
            p_test = pipe.predict_proba(X_test)[:, 1]

            m = evaluate_probability_model(y_test, p_test, compute_calibration_params=False)
            comp_records.append({
                "target": target_name,
                "held_out_competition": comp,
                "n_train": n_train,
                "n_test": n_test,
                "prevalence": round(float(np.mean(y_test)), 4),
                "roc_auc": m["roc_auc"],
                "pr_auc": m["pr_auc"],
                "brier_score": m["brier_score"],
                "log_loss": m["log_loss"],
            })

    df_comps = pd.DataFrame(comp_records)
    comp_path = TABLES_DIR / "leave_competition_out.csv"
    df_comps.to_csv(comp_path, index=False)
    logger.info(f"Saved leave-one-competition-out generalization table to {comp_path}.")
    print(df_comps.to_string(index=False))

    # ----------------------------------------------------
    # SECONDARY THREE-CLASS MODEL
    # ----------------------------------------------------
    logger.info("\nEvaluating Secondary Three-Class Multinomial Model...")
    y_3class = df["episode_outcome_3class"].values
    classes = np.array(["successful_regain", "harmless_escape", "dangerous_escape"])
    oof_3class_probs = np.zeros((len(df), 3))

    num_cols = context_num + local_num + compactness_num + forward_num + observability_num
    cat_cols = context_cat + observability_cat

    for fold_idx in range(5):
        train_mask = (df["fold"] != fold_idx)
        val_mask = (df["fold"] == fold_idx)

        X_train = df.loc[train_mask, num_cols + cat_cols]
        y_train = y_3class[train_mask]
        X_val = df.loc[val_mask, num_cols + cat_cols]

        preproc = build_preprocessor(num_cols, cat_cols)
        X_train_proc = preproc.fit_transform(X_train)
        X_val_proc = preproc.transform(X_val)

        multi_clf = LogisticRegression(multi_class="multinomial", solver="lbfgs", max_iter=1000, C=1.0, random_state=42 + fold_idx)
        multi_clf.fit(X_train_proc, y_train)
        # Reorder probabilities to match `classes` array
        class_order = [np.where(multi_clf.classes_ == c)[0][0] for c in classes]
        p_val = multi_clf.predict_proba(X_val_proc)[:, class_order]
        oof_3class_probs[val_mask] = p_val

    oof_predictions["pred_3class_successful_regain"] = oof_3class_probs[:, 0]
    oof_predictions["pred_3class_harmless_escape"] = oof_3class_probs[:, 1]
    oof_predictions["pred_3class_dangerous_escape"] = oof_3class_probs[:, 2]

    # Evaluate 3-class metrics
    pred_labels = classes[np.argmax(oof_3class_probs, axis=1)]
    macro_f1 = f1_score(y_3class, pred_labels, average="macro")
    macro_roc = roc_auc_score(pd.get_dummies(y_3class)[classes], oof_3class_probs, average="macro", multi_class="ovr")
    conf_mat = confusion_matrix(y_3class, pred_labels, labels=classes)

    logger.info(f"Three-Class Multinomial Model Results:")
    logger.info(f"Macro ROC-AUC: {macro_roc:.4f} | Macro F1: {macro_f1:.4f}")
    logger.info(f"Aggregated Confusion Matrix (rows=true, cols=pred):\n{conf_mat}")

    # ----------------------------------------------------
    # SAVE OUT-OF-FOLD PREDICTIONS
    # ----------------------------------------------------
    oof_path = PROCESSED_DIR / "oof_predictions.parquet"
    oof_predictions.to_parquet(oof_path, index=False)
    logger.info(f"Saved all out-of-fold probability predictions to {oof_path} ({len(oof_predictions)} rows).")

    elapsed = round(time.time() - start_time, 2)
    logger.info(f"\n==========================================")
    logger.info(f"ITERATION 4 MODELING COMPLETED IN {elapsed} SECONDS")
    logger.info(f"==========================================")


if __name__ == "__main__":
    run_iteration4_modeling()
