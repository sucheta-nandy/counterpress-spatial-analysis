"""Modeling pipelines, transformers, and estimators for counterpress predictive analysis.

Enforces:
- Strict cross-validation leakage boundaries (all preprocessing within training folds).
- ColumnTransformer with median imputation, standard scaling, missing indicators for continuous features.
- Categorical one-hot encoding with unknown handling.
- Estimator hierarchy: Null, Context-only, Context+Local, Full Spatial Logistic, Additive Spline (GAM), HistGradientBoosting.
- Clustered inferential logistic regression using statsmodels.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, SplineTransformer, StandardScaler
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import ParameterGrid
import statsmodels.api as sm


class NullPrevalenceClassifier(BaseEstimator, ClassifierMixin):
    """Predicts empirical training-fold class prevalence for every validation observation."""

    def __init__(self):
        self.prevalence_ = 0.5
        self.classes_ = np.array([0, 1])

    def fit(self, X, y):
        self.prevalence_ = float(np.mean(y))
        self.classes_ = np.unique(y)
        return self

    def predict_proba(self, X):
        n = len(X)
        p1 = self.prevalence_
        p0 = 1.0 - p1
        return np.column_stack([np.full(n, p0), np.full(n, p1)])

    def predict(self, X):
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)


def build_preprocessor(
    numeric_cols: List[str],
    categorical_cols: List[str],
    add_missing_indicator: bool = True,
) -> ColumnTransformer:
    """Construct an isolated sklearn ColumnTransformer for numeric and categorical features."""
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median", add_indicator=add_missing_indicator)),
        ("scaler", StandardScaler()),
    ])

    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, numeric_cols),
            ("cat", cat_pipeline, categorical_cols),
        ],
        remainder="drop",
    )
    return preprocessor


def build_model_pipeline(
    model_type: str,
    numeric_cols: List[str],
    categorical_cols: List[str],
    spline_cols: Optional[List[str]] = None,
    C: float = 1.0,
    random_state: int = 42,
    hgb_params: Optional[Dict[str, Any]] = None,
) -> Any:
    """Build complete cross-validation pipeline for a specified model hierarchy tier.

    Model Types:
    - 'null': NullPrevalenceClassifier
    - 'logistic': Preprocessor + L2 LogisticRegression
    - 'gam': Preprocessor with SplineTransformer on continuous spatial features + L2 LogisticRegression
    - 'hgb': Native HistGradientBoostingClassifier (handles missing and categoricals natively or via preprocessor)
    """
    if model_type == "null":
        return NullPrevalenceClassifier()

    if model_type == "logistic":
        preprocessor = build_preprocessor(numeric_cols, categorical_cols)
        clf = LogisticRegression(
            penalty="l2",
            C=C,
            solver="lbfgs",
            max_iter=1000,
            random_state=random_state,
        )
        return Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", clf),
        ])

    if model_type == "gam":
        # Additive Spline model: apply splines to specified continuous spatial columns
        if spline_cols is None:
            spline_cols = [c for c in numeric_cols if "within" not in c and "count" not in c and "advantage" not in c]

        non_spline_num = [c for c in numeric_cols if c not in spline_cols]

        spline_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
            ("spline", SplineTransformer(n_knots=5, degree=3, extrapolation="linear", include_bias=False)),
            ("scaler", StandardScaler()),
        ])

        regular_num_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
            ("scaler", StandardScaler()),
        ])

        cat_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ("spline", spline_pipe, spline_cols),
                ("num", regular_num_pipe, non_spline_num),
                ("cat", cat_pipe, categorical_cols),
            ],
            remainder="drop",
        )

        clf = LogisticRegression(
            penalty="l2",
            C=C,
            solver="lbfgs",
            max_iter=1500,
            random_state=random_state,
        )
        return Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", clf),
        ])

    if model_type == "hgb":
        params = hgb_params or {"learning_rate": 0.05, "max_leaf_nodes": 31, "min_samples_leaf": 30}
        preprocessor = build_preprocessor(numeric_cols, categorical_cols, add_missing_indicator=False)
        clf = HistGradientBoostingClassifier(
            learning_rate=params.get("learning_rate", 0.05),
            max_leaf_nodes=params.get("max_leaf_nodes", 31),
            min_samples_leaf=params.get("min_samples_leaf", 30),
            max_iter=200,
            early_stopping=True,
            validation_fraction=0.15,
            n_iter_no_change=15,
            random_state=random_state,
        )
        return Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", clf),
        ])

    raise ValueError(f"Unknown model_type: {model_type}")


def fit_clustered_logistic_regression(
    df: pd.DataFrame,
    feature_cols: List[str],
    target_col: str,
    cluster_col: str = "match_id",
) -> pd.DataFrame:
    """Fit an inferential logistic regression with standard errors clustered by match_id.

    Returns DataFrame with:
    - feature
    - coef
    - std_err (clustered)
    - z_stat
    - p_val
    - odds_ratio
    - ci_lower_95
    - ci_upper_95
    """
    X_raw = df[feature_cols].copy()
    y = df[target_col].values
    groups = df[cluster_col].values

    # Impute missing with median and standardize continuous features
    for col in feature_cols:
        if pd.api.types.is_numeric_dtype(X_raw[col]):
            med = X_raw[col].median()
            X_raw[col] = X_raw[col].fillna(med)
            std = X_raw[col].std()
            if std > 0:
                X_raw[col] = (X_raw[col] - X_raw[col].mean()) / std
        elif pd.api.types.is_bool_dtype(X_raw[col]):
            X_raw[col] = X_raw[col].astype(float)
        else:
            # Categorical: one-hot
            dummies = pd.get_dummies(X_raw[col], prefix=col, drop_first=True, dtype=float)
            X_raw = pd.concat([X_raw.drop(columns=[col]), dummies], axis=1)

    X_with_const = sm.add_constant(X_raw, prepend=True)

    # Fit GLM Binomial with clustered covariance
    glm_model = sm.GLM(y, X_with_const, family=sm.families.Binomial())
    res = glm_model.fit(cov_type="cluster", cov_kwds={"groups": groups})

    coef_df = pd.DataFrame({
        "feature": res.params.index,
        "coef": res.params.values.round(4),
        "std_err": res.bse.values.round(4),
        "z_stat": res.tvalues.values.round(4),
        "p_val": res.pvalues.values.round(4),
        "odds_ratio": np.exp(res.params.values).round(4),
        "ci_lower_95": np.exp(res.conf_int()[0].values).round(4),
        "ci_upper_95": np.exp(res.conf_int()[1].values).round(4),
    })
    return coef_df
