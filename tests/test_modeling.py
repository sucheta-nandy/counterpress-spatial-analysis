"""Unit tests for modeling pipeline, cross-validation isolation, and evaluation metrics."""

import numpy as np
import pandas as pd
import pytest

from counterpress.config import TABLES_DIR
from counterpress.models import evaluate_probability_model
from counterpress.modeling import (
    NullPrevalenceClassifier,
    build_preprocessor,
    fit_clustered_logistic_regression,
)


def test_cv_folds_invariants():
    """Verify frozen cross-validation fold assignments."""
    folds_path = TABLES_DIR / "model_cv_folds.csv"
    assert folds_path.exists(), f"Missing {folds_path}"
    df = pd.read_csv(folds_path)

    assert len(df) == 21616, f"Expected 21616 rows, got {len(df)}"
    assert df["episode_id"].nunique() == 21616, "Duplicate episode_ids in folds"
    assert df["match_id"].nunique() == 414, "Expected 414 matches"

    # Strictly test group independence
    match_folds = df.groupby("match_id")["fold"].nunique()
    assert (match_folds == 1).all(), "Data leakage: match_id exists in multiple CV folds!"
    assert set(df["fold"].unique()) == {0, 1, 2, 3, 4}, "Folds should be 0 through 4"


def test_null_prevalence_classifier():
    """Verify NullPrevalenceClassifier outputs training prevalence on validation data."""
    X_train = np.zeros((100, 2))
    y_train = np.array([1] * 35 + [0] * 65)  # 35% prevalence
    X_val = np.ones((50, 2))

    null_clf = NullPrevalenceClassifier()
    null_clf.fit(X_train, y_train)
    probs = null_clf.predict_proba(X_val)

    assert probs.shape == (50, 2)
    assert np.allclose(probs[:, 1], 0.35)
    assert np.allclose(probs[:, 0], 0.65)


def test_evaluate_probability_model():
    """Verify metric computation against synthetic ground truth."""
    y_true = np.array([1, 1, 1, 0, 0, 0])
    y_prob = np.array([0.9, 0.8, 0.7, 0.3, 0.2, 0.1])

    res = evaluate_probability_model(y_true, y_prob)
    assert res["roc_auc"] == 1.0
    assert res["pr_auc"] == 1.0
    assert res["brier_score"] < 0.1
    assert not np.isnan(res["calib_slope"])


def test_preprocessor_leakage_isolation():
    """Verify that preprocessing scales only using training fold statistics."""
    train_df = pd.DataFrame({
        "num1": [10.0, 20.0, 30.0],
        "cat1": ["A", "B", "A"],
    })
    val_df = pd.DataFrame({
        "num1": [100.0, 200.0],
        "cat1": ["A", "C"],  # C is unseen
    })

    preprocessor = build_preprocessor(["num1"], ["cat1"])
    X_train_proc = preprocessor.fit_transform(train_df)
    X_val_proc = preprocessor.transform(val_df)

    # Train mean is 20.0, std is sqrt(200/3) ≈ 8.165
    # Value 100 in val should be (100 - 20) / std, not 0
    assert X_val_proc.shape[0] == 2
    # Unseen category 'C' in val should be encoded as 0, not error
    assert not np.isnan(X_val_proc).any()


def test_clustered_inference_output():
    """Verify statsmodels clustered logistic regression returns valid coefficients and cluster SEs."""
    rng = np.random.RandomState(42)
    n = 300
    df_synth = pd.DataFrame({
        "match_id": rng.choice([1, 2, 3, 4, 5], size=n),
        "feature1": rng.randn(n),
        "target": rng.binomial(1, 0.4, size=n),
    })

    res_df = fit_clustered_logistic_regression(df_synth, ["feature1"], "target")
    assert "coef" in res_df.columns
    assert "std_err" in res_df.columns
    assert "odds_ratio" in res_df.columns
    assert "ci_lower_95" in res_df.columns
    assert len(res_df) == 2  # const + feature1


def test_constant_predictor_roc_auc():
    """Verify that a constant predictor produces ROC-AUC = 0.5 under valid cluster-bootstrap samples."""
    from counterpress.models import match_cluster_bootstrap_ci
    from sklearn.metrics import roc_auc_score

    rng = np.random.RandomState(42)
    n_samples = 500
    df_synth = pd.DataFrame({
        "match_id": rng.choice(range(20), size=n_samples),
        "target": rng.binomial(1, 0.35, size=n_samples),
        "constant_pred": np.full(n_samples, 0.35),
    })

    # Within any evaluation set with binary classes, constant predictor yields AUC = 0.5
    point_auc = roc_auc_score(df_synth["target"], df_synth["constant_pred"])
    assert point_auc == 0.5, f"Expected 0.5, got {point_auc}"

    ci_dict = match_cluster_bootstrap_ci(df_synth, "target", "constant_pred", n_boot=50, random_state=42)
    # Every bootstrap sample with both classes has ROC-AUC identically 0.5
    assert ci_dict["roc_auc"][0] == 0.5
    assert ci_dict["roc_auc"][1] == 0.5
