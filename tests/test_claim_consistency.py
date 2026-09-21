"""tests/test_claim_consistency.py

Automated Consistency and Invariant Tests for Canonical Conference Claims.
Enforces Iteration 4.6 reconciliation gates:
- Assertions A & B: Performance Deltas for Model 1 -> Model 3
- Assertion C: Pitch-Third Danger and Regain Recomputations
- Assertion D: Primary Inferential Odds Ratios == exp(primary coefficient)
- Assertion E: Confidence Intervals Match Source Tables
- Assertion F: No Sensitivity Model Labeled as Primary
- Assertion G: Forward Numerical Advantage Sign Definition (Opponents - Defenders)
- Assertion H: Primary Cohort Invariants (21,616 episodes, 414 matches)
- Assertion I: Primary Outcome Invariants (7,491 regains, 4,844 dangerous escapes)
"""

import math
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TABLES_DIR = PROJECT_ROOT / "results" / "tables"
DATA_DIR = PROJECT_ROOT / "data" / "processed"


@pytest.fixture(scope="module")
def features_df():
    return pd.read_parquet(DATA_DIR / "counterpress_features.parquet")


@pytest.fixture(scope="module")
def claims_df():
    return pd.read_csv(TABLES_DIR / "canonical_conference_claims.csv")


@pytest.fixture(scope="module")
def coefs_df():
    return pd.read_csv(TABLES_DIR / "logistic_coefficients.csv")


@pytest.fixture(scope="module")
def model_perf_df():
    return pd.read_csv(TABLES_DIR / "model_performance.csv")


@pytest.fixture(scope="module")
def model_incr_df():
    return pd.read_csv(TABLES_DIR / "model_incremental_value.csv")


@pytest.fixture(scope="module")
def paired_df():
    return pd.read_csv(TABLES_DIR / "paired_model_comparisons.csv")


@pytest.fixture(scope="module")
def specs_df():
    return pd.read_csv(TABLES_DIR / "canonical_model_specifications.csv")


# ----------------------------------------------------------------------
# Assertion A: Model 1 -> Model 3 Regain Delta ROC-AUC
# ----------------------------------------------------------------------
def test_assertion_a_model1_to_model3_regain_delta_roc_auc(model_perf_df, model_incr_df, claims_df):
    m1 = model_perf_df[(model_perf_df["target"] == "regain_5s") & (model_perf_df["model"] == "Model 1 (Context)")].iloc[0]
    m3 = model_perf_df[(model_perf_df["target"] == "regain_5s") & (model_perf_df["model"] == "Model 3 (Full Spatial Logistic)")].iloc[0]
    incr = model_incr_df[(model_incr_df["target"] == "regain_5s") &
                          (model_incr_df["baseline"] == "Model 1 (Context)") &
                          (model_incr_df["comparison_model"] == "Model 3 (Full Spatial Logistic)")].iloc[0]

    expected_delta_roc = round(m3["roc_auc_mean"] - m1["roc_auc_mean"], 4)
    assert incr["delta_roc_auc"] == expected_delta_roc
    assert incr["delta_roc_auc"] == 0.0230

    claim_01 = claims_df[claims_df["claim_id"] == "CLAIM_01"].iloc[0]
    assert "+0.0230" in claim_01["value"]
    assert "0.7926" in claim_01["claim_text"]
    assert "0.8156" in claim_01["claim_text"]


# ----------------------------------------------------------------------
# Assertion B: Model 1 -> Model 3 Regain Delta PR-AUC
# ----------------------------------------------------------------------
def test_assertion_b_model1_to_model3_regain_delta_pr_auc(model_perf_df, model_incr_df, claims_df):
    m1 = model_perf_df[(model_perf_df["target"] == "regain_5s") & (model_perf_df["model"] == "Model 1 (Context)")].iloc[0]
    m3 = model_perf_df[(model_perf_df["target"] == "regain_5s") & (model_perf_df["model"] == "Model 3 (Full Spatial Logistic)")].iloc[0]
    incr = model_incr_df[(model_incr_df["target"] == "regain_5s") &
                          (model_incr_df["baseline"] == "Model 1 (Context)") &
                          (model_incr_df["comparison_model"] == "Model 3 (Full Spatial Logistic)")].iloc[0]

    expected_delta_pr = round(m3["pr_auc_mean"] - m1["pr_auc_mean"], 4)
    assert incr["delta_pr_auc"] == expected_delta_pr
    assert incr["delta_pr_auc"] == 0.0377

    claim_01 = claims_df[claims_df["claim_id"] == "CLAIM_01"].iloc[0]
    assert "+0.0377" in claim_01["value"]
    assert "0.7393" in claim_01["claim_text"]
    assert "0.7770" in claim_01["claim_text"]


# ----------------------------------------------------------------------
# Assertion C: Pitch-Third Danger Rates Match Direct Recomputation
# ----------------------------------------------------------------------
def test_assertion_c_pitch_third_danger_rates_direct_recomputation(features_df, claims_df):
    def_mask = features_df["initiation_x"] < 40
    mid_mask = (features_df["initiation_x"] >= 40) & (features_df["initiation_x"] < 80)
    att_mask = features_df["initiation_x"] >= 80

    n_def = def_mask.sum()
    n_mid = mid_mask.sum()
    n_att = att_mask.sum()
    assert n_def + n_mid + n_att == len(features_df)

    def_danger_cnt = features_df.loc[def_mask, "dangerous_escape_15s"].sum()
    mid_danger_cnt = features_df.loc[mid_mask, "dangerous_escape_15s"].sum()
    att_danger_cnt = features_df.loc[att_mask, "dangerous_escape_15s"].sum()

    assert def_danger_cnt == 1280
    assert mid_danger_cnt == 2690
    assert att_danger_cnt == 874

    def_danger_rate = def_danger_cnt / n_def
    mid_danger_rate = mid_danger_cnt / n_mid
    att_danger_rate = att_danger_cnt / n_att

    assert round(def_danger_rate * 100, 2) == 31.57
    assert round(mid_danger_rate * 100, 2) == 27.41
    assert round(att_danger_rate * 100, 2) == 11.28

    claim_04 = claims_df[claims_df["claim_id"] == "CLAIM_04"].iloc[0]
    assert "31.57%" in claim_04["claim_text"]
    assert "27.41%" in claim_04["claim_text"]
    assert "11.28%" in claim_04["claim_text"]
    assert "35.9%" not in claim_04["claim_text"]


# ----------------------------------------------------------------------
# Assertion D: Primary Inferential ORs Equal exp(primary coefficient)
# ----------------------------------------------------------------------
def test_assertion_d_primary_inferential_odds_ratios_equal_exp_coef(coefs_df, claims_df):
    primary_claims = claims_df[claims_df["model_specification"] == "PRIMARY_INFERENTIAL_MODEL"]
    assert len(primary_claims) >= 4

    for _, row in coefs_df.iterrows():
        expected_or = round(math.exp(row["coef"]), 4)
        assert abs(row["odds_ratio"] - expected_or) <= 0.0002, (
            f"Feature {row['feature']} OR {row['odds_ratio']} != exp({row['coef']})={expected_or}"
        )

    # Verify specific primary claims
    tm_row = coefs_df[(coefs_df["target"] == "regain_5s") & (coefs_df["feature"] == "nearest_teammate_distance")].iloc[0]
    assert tm_row["odds_ratio"] == 0.8003
    assert round(math.exp(tm_row["coef"]), 4) == 0.8003

    init_x_row = coefs_df[(coefs_df["target"] == "danger_15s") & (coefs_df["feature"] == "initiation_x")].iloc[0]
    assert init_x_row["odds_ratio"] == 0.3785
    assert round(math.exp(init_x_row["coef"]), 4) == 0.3785

    touch_reg = coefs_df[(coefs_df["target"] == "regain_5s") & (coefs_df["feature"] == "distance_to_nearest_touchline")].iloc[0]
    assert touch_reg["odds_ratio"] == 1.1113

    touch_dan = coefs_df[(coefs_df["target"] == "danger_15s") & (coefs_df["feature"] == "distance_to_nearest_touchline")].iloc[0]
    assert touch_dan["odds_ratio"] == 1.2190


# ----------------------------------------------------------------------
# Assertion E: Confidence Intervals Match Source Table
# ----------------------------------------------------------------------
def test_assertion_e_confidence_intervals_match_source_table(claims_df, coefs_df, paired_df):
    # Claim 02: nearest_teammate_distance
    c2 = claims_df[claims_df["claim_id"] == "CLAIM_02"].iloc[0]
    tm_row = coefs_df[(coefs_df["target"] == "regain_5s") & (coefs_df["feature"] == "nearest_teammate_distance")].iloc[0]
    assert f"[{tm_row['ci_lower_95']:.4f}, {tm_row['ci_upper_95']:.4f}]" == c2["CI"]

    # Claim 04: initiation_x
    c4 = claims_df[claims_df["claim_id"] == "CLAIM_04"].iloc[0]
    x_row = coefs_df[(coefs_df["target"] == "danger_15s") & (coefs_df["feature"] == "initiation_x")].iloc[0]
    assert f"[{x_row['ci_lower_95']:.4f}, {x_row['ci_upper_95']:.4f}]" == c4["CI"]

    # Claim 07: GAM & HGB for regain
    c7 = claims_df[claims_df["claim_id"] == "CLAIM_07"].iloc[0]
    p_gam = paired_df[(paired_df["target"] == "regain_5s") &
                      (paired_df["comparison"] == "Model 3 vs Model 4 (GAM)") &
                      (paired_df["metric"] == "delta_roc_auc")].iloc[0]
    assert p_gam["ci_95"] in c7["CI"]


# ----------------------------------------------------------------------
# Assertion F: No Sensitivity Model Labeled as Primary
# ----------------------------------------------------------------------
def test_assertion_f_no_sensitivity_model_labeled_as_primary(claims_df, specs_df):
    # In canonical claims:
    claim_10 = claims_df[claims_df["claim_id"] == "CLAIM_10"].iloc[0]
    assert "PRIMARY_INFERENTIAL_MODEL" not in claim_10["model_specification"]
    assert "SENSITIVITY" in claim_10["model_specification"]

    # In canonical specs:
    assert len(specs_df) == 3
    primary_row = specs_df[specs_df["specification_name"] == "PRIMARY_INFERENTIAL_MODEL"].iloc[0]
    assert primary_row["sample_n"] == 21616
    assert "PRIMARY" in primary_row["specification_name"]

    sens_local = specs_df[specs_df["specification_name"] == "HIGH_LOCAL_VISIBILITY_SENSITIVITY"].iloc[0]
    assert sens_local["sample_n"] == 20548
    assert "SENSITIVITY" in sens_local["specification_name"]

    sens_corr = specs_df[specs_df["specification_name"] == "HIGH_CORRIDOR_VISIBILITY_SENSITIVITY"].iloc[0]
    assert sens_corr["sample_n"] == 13411
    assert "SENSITIVITY" in sens_corr["specification_name"]


# ----------------------------------------------------------------------
# Assertion G: Forward Numerical Advantage Sign Definition
# ----------------------------------------------------------------------
def test_assertion_g_forward_numerical_advantage_sign_definition(features_df):
    non_null = features_df[features_df["forward_numerical_advantage"].notna()]
    assert len(non_null) == len(features_df)

    diff = non_null["opponents_ahead_of_ball"] - non_null["defenders_ahead_of_ball"]
    assert (non_null["forward_numerical_advantage"] == diff).all(), (
        "forward_numerical_advantage must equal opponents_ahead_of_ball - defenders_ahead_of_ball"
    )


# ----------------------------------------------------------------------
# Assertion H: Primary Cohort Invariants
# ----------------------------------------------------------------------
def test_assertion_h_primary_cohort_invariants(features_df):
    cohort_ids = pd.read_csv(TABLES_DIR / "primary_cohort_episode_ids.csv")
    assert len(cohort_ids) == 21616
    assert len(features_df) == 21616
    assert features_df["match_id"].nunique() == 414
    assert set(features_df["episode_id"]) == set(cohort_ids["episode_id"])


# ----------------------------------------------------------------------
# Assertion I: Primary Outcomes Invariants
# ----------------------------------------------------------------------
def test_assertion_i_primary_outcomes_invariants(features_df):
    regain_count = features_df["regain_5s_controlled"].sum()
    danger_count = features_df["dangerous_escape_15s"].sum()

    assert regain_count == 7491
    assert danger_count == 4844
    assert round(regain_count / len(features_df) * 100, 2) == 34.65
    assert round(danger_count / len(features_df) * 100, 2) == 22.41
