"""Statistical and machine learning evaluation metrics and model utilities for counterpress analysis.

Implements:
- Probabilistic evaluation metrics: ROC-AUC, PR-AUC, Brier score, Log Loss.
- Calibration slope, intercept, and reliability curve generation.
- Match-clustered bootstrap confidence intervals for CV performance metrics.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    log_loss,
    roc_auc_score,
)
from sklearn.calibration import calibration_curve
from scipy.special import expit, logit


def evaluate_probability_model(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    compute_calibration_params: bool = True,
) -> Dict[str, float]:
    """Compute comprehensive probabilistic classification metrics:

    - ROC-AUC
    - PR-AUC (Average Precision)
    - Brier score
    - Log loss
    - Calibration slope and intercept (via Platt calibration regression)
    """
    y_true = np.asarray(y_true, dtype=int)
    y_prob = np.asarray(y_prob, dtype=float)

    # Clip probabilities strictly away from 0 and 1 for numerical stability
    eps = 1e-15
    y_prob_clipped = np.clip(y_prob, eps, 1.0 - eps)

    roc_auc = float(roc_auc_score(y_true, y_prob_clipped))
    pr_auc = float(average_precision_score(y_true, y_prob_clipped))
    brier = float(brier_score_loss(y_true, y_prob_clipped))
    ll = float(log_loss(y_true, y_prob_clipped))

    calib_slope = np.nan
    calib_intercept = np.nan

    if compute_calibration_params:
        try:
            # Regress log-odds of predictions onto true binary outcomes:
            # y_true ~ logit(p)
            log_odds = logit(y_prob_clipped).reshape(-1, 1)
            # Use simple logistic regression without regularization
            from sklearn.linear_model import LogisticRegression
            lr = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500)
            lr.fit(log_odds, y_true)
            calib_slope = float(lr.coef_[0][0])
            calib_intercept = float(lr.intercept_[0])
        except Exception:
            calib_slope = np.nan
            calib_intercept = np.nan

    return {
        "roc_auc": round(roc_auc, 4),
        "pr_auc": round(pr_auc, 4),
        "brier_score": round(brier, 4),
        "log_loss": round(ll, 4),
        "calib_slope": round(calib_slope, 4) if not np.isnan(calib_slope) else np.nan,
        "calib_intercept": round(calib_intercept, 4) if not np.isnan(calib_intercept) else np.nan,
    }


def compute_calibration_curve_data(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    n_bins: int = 10,
    strategy: str = "quantile",
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute calibration curve data with empirical bins and observation counts."""
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy=strategy)
    # Bin counts
    if strategy == "quantile":
        quantiles = np.linspace(0, 1, n_bins + 1)
        bin_edges = np.quantile(y_prob, quantiles)
    else:
        bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_counts, _ = np.histogram(y_prob, bins=bin_edges)
    return prob_true, prob_pred, bin_counts


def match_cluster_bootstrap_ci(
    df: pd.DataFrame,
    y_true_col: str,
    y_prob_col: str,
    cluster_col: str = "match_id",
    n_boot: int = 500,
    random_state: int = 42,
) -> Dict[str, Tuple[float, float]]:
    """Compute 95% confidence intervals for evaluation metrics using match-cluster bootstrap."""
    rng = np.random.RandomState(random_state)
    unique_clusters = df[cluster_col].unique()
    n_clusters = len(unique_clusters)

    # Group rows by cluster for fast lookup
    cluster_to_indices = df.groupby(cluster_col).indices

    boot_metrics: Dict[str, List[float]] = {
        "roc_auc": [],
        "pr_auc": [],
        "brier_score": [],
        "log_loss": [],
    }

    y_true_all = df[y_true_col].values
    y_prob_all = df[y_prob_col].values

    for _ in range(n_boot):
        sample_clusters = rng.choice(unique_clusters, size=n_clusters, replace=True)
        sample_indices = np.concatenate([cluster_to_indices[c] for c in sample_clusters])

        y_t = y_true_all[sample_indices]
        y_p = y_prob_all[sample_indices]

        # Check for both classes in sample
        if len(np.unique(y_t)) < 2:
            continue

        res = evaluate_probability_model(y_t, y_p, compute_calibration_params=False)
        for k in boot_metrics:
            boot_metrics[k].append(res[k])

    ci_dict = {}
    for k, vals in boot_metrics.items():
        if len(vals) > 0:
            ci_lower = round(float(np.percentile(vals, 2.5)), 4)
            ci_upper = round(float(np.percentile(vals, 97.5)), 4)
            ci_dict[k] = (ci_lower, ci_upper)
        else:
            ci_dict[k] = (np.nan, np.nan)

    return ci_dict
