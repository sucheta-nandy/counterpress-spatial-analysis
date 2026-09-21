# Iteration 4.6: Canonical Claims and Number Reconciliation Freeze

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Venues**: MIT Sloan Sports Analytics Conference (SSAC 2026) & Carnegie Mellon Sports Analytics Conference (CMSAC 2026)  
**Milestone**: Iteration 4.6 (Final Numerical Consistency Gate Before Abstract Drafting)  
**Status**: **FROZEN & VERIFIED** (All 84 unit tests passing)

---

## Executive Summary

Iteration 4.6 serves as the **final numerical consistency gate** prior to conference abstract drafting. In accordance with strict methodological governance:
- Cohort membership remains strictly frozen at **$N = 21,616$ distinct counterpress episodes across 414 matches**.
- Primary outcome definitions and counts remain strictly frozen at **$\text{regain\_5s\_controlled} = 7,491$ (34.65%)** and **$\text{dangerous\_escape\_15s} = 4,844$ (22.41%)**.
- Spatial features and model architectures were **not altered, retuned, or re-searched**.
- Every quantitative statement intended for conference claims is programmatically generated from canonical result tables via `scripts/build_canonical_claims.py` and locked in [`results/tables/canonical_conference_claims.csv`](../results/tables/canonical_conference_claims.csv).
- Nine automated consistency assertions in [`tests/test_claim_consistency.py`](../tests/test_claim_consistency.py) verify all claims, deltas, recomputed pitch-third rates, and inferential invariants.

---

## 1. Primary Inferential Specification (`PRIMARY_INFERENTIAL_MODEL`)

To ensure that conference and manuscript odds ratios derive from a single, pre-specified regression model, we formally define `PRIMARY_INFERENTIAL_MODEL`. Sensitivity regressions are documented separately and must never replace primary inferential estimates.

The three canonical regression specifications are codified in [`results/tables/canonical_model_specifications.csv`](../results/tables/canonical_model_specifications.csv):

| Specification Name | Model Family | Cluster Variable | Sample $N$ | Feature Set | Primary Output Table |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`PRIMARY_INFERENTIAL_MODEL`** | Binomial GLM (logit link) | `match_id` (414 clusters) | 21,616 | 17 features (15 spatial/frame + 1 QA flag + 1 categorical) | [`logistic_coefficients.csv`](../results/tables/logistic_coefficients.csv) |
| **`HIGH_LOCAL_VISIBILITY_SENSITIVITY`** | Binomial GLM (logit link) | `match_id` (414 clusters) | 20,548 (`coverage_10 >= 0.80`) | 10 features (6 tactical + 4 contextual categoricals) | [`high_coverage_sensitivity_coefficients.csv`](../results/tables/high_coverage_sensitivity_coefficients.csv) |
| **`HIGH_CORRIDOR_VISIBILITY_SENSITIVITY`** | Binomial GLM (logit link) | `match_id` (414 clusters) | 13,411 (`escape_corridor_coverage_20 >= 0.80`) | 10 features (6 tactical + 4 contextual categoricals) | [`high_coverage_sensitivity_coefficients.csv`](../results/tables/high_coverage_sensitivity_coefficients.csv) |

### Specification Details for `PRIMARY_INFERENTIAL_MODEL`
- **Sample**: All $N = 21,616$ primary cohort episodes from 414 matches.
- **Cluster Variable**: `match_id` (sandwich clustered robust standard errors via `cov_type='cluster'`).
- **Standardization Method**: All continuous features are $z$-score standardized ($z = (x - \mu)/\sigma$) using sample mean and sample standard deviation across the full cohort.
- **Imputation**: Missing continuous values are imputed with the feature median prior to scaling.
- **Categorical Handling**: `initiation_event_type` is one-hot encoded with reference class 'Ball Recovery' (`pd.get_dummies(..., drop_first=True, dtype=float)`). The QA flag `actor_matching_anomalous` is cast to float (0.0/1.0). Intercept (`const`) is added.
- **Exact Feature List (17 features)**:
  1. `initiation_x`
  2. `distance_to_nearest_touchline`
  3. `numerical_advantage_5`
  4. `numerical_advantage_10`
  5. `numerical_advantage_15`
  6. `nearest_teammate_distance`
  7. `nearest_opponent_distance`
  8. `teammate_mean_pairwise_distance`
  9. `opponent_mean_pairwise_distance`
  10. `forward_numerical_advantage`
  11. `nearest_defender_ahead_distance`
  12. `nearest_opponent_ahead_distance`
  13. `escape_corridor_advantage_20`
  14. `coverage_10`
  15. `escape_corridor_coverage_20`
  16. `actor_matching_anomalous`
  17. `initiation_event_type` (one-hot: Block, Dribbled Past, Duel, Foul Committed, Interception, Pass, Pressure)

---

## 2. Numerical Reconciliation of Historical Discrepancies

### 2.1 Claim 01 Performance Deltas Reconciled
- **Previous Errant Claim**: $\Delta \text{ROC-AUC} = +0.0251$, $\Delta \text{PR-AUC} = +0.0204$ (reported in early draft audit).
- **Source of Discrepancy**: Traced to an uncalibrated, draft model comparison where context ROC-AUC was entered as $0.5843$ and spatial ROC-AUC as $0.6094$ ($0.6094 - 0.5843 = 0.0251$).
- **Canonical Frozen Result**: Evaluated across 5-fold match-clustered cross-validation ([`results/tables/model_performance.csv`](../results/tables/model_performance.csv) and [`results/tables/model_incremental_value.csv`](../results/tables/model_incremental_value.csv)):
  - **Model 1 (Context)**: $\text{ROC-AUC} = 0.7926 \pm 0.0021$, $\text{PR-AUC} = 0.7393 \pm 0.0088$, $\text{Brier} = 0.1449 \pm 0.0028$.
  - **Model 3 (Full Spatial Logistic)**: $\text{ROC-AUC} = 0.8156 \pm 0.0020$, $\text{PR-AUC} = 0.7770 \pm 0.0065$, $\text{Brier} = 0.1386 \pm 0.0019$.
  - **Incremental Deltas**: **$\Delta \text{ROC-AUC} = +0.0230$**, **$\Delta \text{PR-AUC} = +0.0377$**, **$\Delta \text{Brier} = -0.0063$**, **$\Delta \text{Log Loss} = -0.0187$**.
  - **Paired Match-Clustered Bootstrap (1,000 resamples)**: $\Delta \text{ROC-AUC} = +0.0233$ [95% CI: $+0.0181, +0.0278$]; $\Delta \text{PR-AUC} = +0.0390$ [95% CI: $+0.0330, +0.0448$]. Both strictly exclude zero.

### 2.2 Local Numerical Advantage Odds Ratios Reconciled
- **Previous Errant Claim**: $\text{OR} = 1.074$ (5m) and $\text{OR} = 1.055$ (10m).
- **Source of Discrepancy**: Manual entry in `audit_iteration4_5.py` reflecting an exploratory model that lacked the 15-unit compactness ring.
- **Canonical Frozen Result** ([`results/tables/logistic_coefficients.csv`](../results/tables/logistic_coefficients.csv)):
  - `numerical_advantage_15`: $\beta = +0.1348, z = 4.98, p < 0.0001, q < 0.0001 \implies \mathbf{\text{OR} = 1.1443} \ [1.0852, 1.2067]$.
  - `numerical_advantage_10`: $\beta = +0.0681, z = 2.47, p = 0.0136, q = 0.0218 \implies \mathbf{\text{OR} = 1.0705} \ [1.0141, 1.1301]$.
  - `numerical_advantage_5`: $\beta = +0.0215, z = 0.98, p = 0.3285, q = 0.4380 \implies \mathbf{\text{OR} = 1.0217} \ [0.9786, 1.0667]$ (non-significant in fully adjusted model).
- **Tactical Interpretation**: Tactical numerical support is not confined to the immediate 5-unit radius; robust associations manifest across broader 10-unit and 15-unit rings.

### 2.3 Pitch-Third Danger Numbers Reconciled
- **Previous Errant Claim**: Defensive-third danger = $35.9\%$, attacking-third danger = $11.2\%$.
- **Source of Discrepancy**: Identified as a transcription error where the overall regain prevalence in the FIFA World Cup ($35.91\%$ in [`leave_competition_out.csv`](../results/tables/leave_competition_out.csv)) was inadvertently transcribed into the descriptive pitch-third danger text.
- **Direct Recomputation from `counterpress_features.parquet`** ($x < 40, 40 \le x < 80, x \ge 80$):
  - **Defensive Third ($x < 40$)**: $N = 4,054$, danger = **1,280 (31.57%)**, regain = **2,312 (57.03%)**.
  - **Middle Third ($40 \le x < 80$)**: $N = 9,815$, danger = **2,690 (27.41%)**, regain = **3,327 (33.90%)**.
  - **Attacking Third ($x \ge 80$)**: $N = 7,747$, danger = **874 (11.28%)**, regain = **1,852 (23.91%)**.
  *(Note: Binned descriptive table using right-closed intervals yields 31.60%, 27.37%, 11.25%; both match within 0.03 percentage points).*

### 2.4 Initiation X Odds Ratios Reconciled
Documented in [`results/tables/coefficient_specification_reconciliation.csv`](../results/tables/coefficient_specification_reconciliation.csv):
- **$\text{OR} = 0.3785 \approx 0.379$** [95% CI: $0.3591, 0.3990$]: Canonical **`PRIMARY_INFERENTIAL_MODEL`** ($N = 21,616$, 17 features, match-clustered GLM). **Sole headline value.**
- **$\text{OR} = 0.3738 \approx 0.374$** [95% CI: $0.3393, 0.4118$]: Sensitivity regression on Full Cohort ($N = 21,616$) using 6 tactical features + context categoricals.
- **$\text{OR} = 0.4050 \approx 0.405$** [95% CI: $0.3555, 0.4614$]: High Corridor Visibility sensitivity model ($N = 13,411$, `escape_corridor_coverage_20 >= 0.80`).
- **$\text{OR} = 0.5120 \approx 0.512$** [$\beta = -0.6693$]: Unadjusted historical specification prior to spatial covariate adjustment.

### 2.5 Nearest-Teammate Distance Odds Ratios Reconciled
- **$\text{OR} = 0.8003 \approx 0.800$** [95% CI: $0.7294, 0.8781$, $p < 0.0001, q < 0.0001$]: Canonical **`PRIMARY_INFERENTIAL_MODEL`** ($N = 21,616$, 17 features).
  - Feature standard deviation: **$\sigma = 8.1836$ StatsBomb coordinate units** (~8.2m).
  - Magnitude: 1 SD closer (~8.2 units) is associated with $\exp(+0.2228) = 1.2495 \approx \mathbf{+25.0\%}$ higher odds of controlled regain.
- **Sensitivity Estimates**: $\text{OR} = 0.8662$ (Full Cohort tactical subset), $\text{OR} = 0.8833$ (High Local Visibility subset, $N = 20,548$), $\text{OR} = 0.8962$ (High Corridor Visibility subset, $N = 13,411$).
  - Shift explained: Sensitivity regressions omitted `numerical_advantage_15` and `teammate_mean_pairwise_distance`, distributing part of the compactness signal across other features.

---

## 3. Canonical Conference Claims Table

The 10 conference-safe claims codified in [`results/tables/canonical_conference_claims.csv`](../results/tables/canonical_conference_claims.csv):

| Claim ID | Theme | Analysis Type / Specification | Primary Metric & Value | Confidence Interval | Allowed Wording |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CLAIM_01** | Incremental Value of 360 Geometry | 5-Fold Match-Clustered CV (Model 1 vs Model 3) | $\Delta \text{ROC-AUC} = +0.0230$, $\Delta \text{PR-AUC} = +0.0377$, $\Delta \text{Brier} = -0.0063$ | ROC: $[+0.0181, +0.0278]$, PR: $[+0.0330, +0.0448]$ | StatsBomb 360 freeze-frame spatial geometry provided modest but statistically reliable incremental predictive information for 5-second controlled regains beyond pitch location and event context. |
| **CLAIM_02** | Nearest Teammate Proximity and Regain | `PRIMARY_INFERENTIAL_MODEL` | $\beta = -0.2228, \text{OR} = 0.8003$ per 8.2 units | $[0.7294, 0.8781]$ | Holding modeled covariates fixed, closer immediate teammate proximity to the ball at counterpress initiation was strongly associated with higher odds of controlled possession regain (OR = 0.800 per 8.2 units distance). |
| **CLAIM_03** | Broader Local Numerical Support | `PRIMARY_INFERENTIAL_MODEL` | 10u $\text{OR} = 1.0705$; 15u $\text{OR} = 1.1443$; 5u $\text{OR} = 1.0217$ (n.s.) | 10u: $[1.0141, 1.1301]$, 15u: $[1.0852, 1.2067]$ | A greater local numerical surplus within 10 to 15 coordinate units was associated with increased odds of controlled regain conditional on other features, while immediate 5-unit surplus was not independently significant. |
| **CLAIM_04** | Longitudinal Pitch Position and Danger | `PRIMARY_INFERENTIAL_MODEL` & Descriptive Stratification | $\beta = -0.9715, \text{OR} = 0.3785$; Def Danger = 31.57%, Att Danger = 11.28% | $[0.3591, 0.3990]$ | Longitudinal pitch position at turnover initiation is the dominant predictor of transition danger: turnovers in the defensive third are associated with nearly three times the baseline danger of attacking-third turnovers (31.57% vs 11.28%). |
| **CLAIM_05** | Centrality and Transition Danger | `PRIMARY_INFERENTIAL_MODEL` & Descriptive Stratification | $\beta = +0.1981, \text{OR} = 1.2190$; Wide = 16.86%, Central = 25.15% | $[1.1740, 1.2658]$ | Counterpress episodes initiated farther from the touchline were associated with significantly greater transition danger, with descriptive danger rising from 16.86% in wide areas to 25.15% in central areas, consistent with greater access to central counter-attacking space. |
| **CLAIM_06** | Centrality Trade-Off (Cautiously Phrased) | `PRIMARY_INFERENTIAL_MODEL` Regain vs Danger Contrast | Regain $\text{OR} = 1.1113$, Danger $\text{OR} = 1.2190$; Regain flat unadjusted (34.30% vs 34.85%) | Regain: $[1.0712, 1.1529]$, Danger: $[1.1740, 1.2658]$ | Unadjusted regain rates were nearly flat across pitch width, but after adjustment greater centrality was associated with modestly higher regain odds. Central counterpress episodes were also associated with substantially greater dangerous-transition risk. |
| **CLAIM_07** | Limited Nonlinear Gain for Regain | Paired Clustered Bootstrap (Model 3 vs Models 4 & 5) | GAM $\Delta \text{ROC-AUC} = +0.0001$; HGB $\Delta \text{ROC-AUC} = -0.0011$ | GAM: $[-0.0014, +0.0018]$, HGB: $[-0.0042, +0.0022]$ | Flexible non-linear and tree-based models did not materially improve out-of-sample discrimination over the full spatial logistic model for predicting 5-second controlled regains. |
| **CLAIM_08** | Nonlinear Gain for Transition Danger | Paired Clustered Bootstrap (Model 3 vs Model 5 HGB) | $\Delta \text{ROC-AUC} = +0.0091$, $\Delta \text{PR-AUC} = +0.0394$, $\Delta \text{Brier} = -0.0040$ | ROC: $[+0.0059, +0.0125]$, PR: $[+0.0299, +0.0490]$ | For transition danger, flexible models yielded better out-of-sample probability ranking and precision-recall performance, consistent with non-linear threshold effects across pitch length and lateral corridors. |
| **CLAIM_09** | Competition Holdout Robustness | Leave-One-Competition-Out (7 competition partitions) | Regain ROC: $[0.7873, 0.8466]$; Danger ROC: $[0.7532, 0.7919]$ | 7 partitions: La Liga, Euro, Ligue 1, Women's Euro, World Cup, WWC, Bundesliga | The model retained similar discrimination when each of the seven represented competition groups was held out in turn, demonstrating robust out-of-distribution transfer across domestic leagues and international tournaments. |
| **CLAIM_10** | Visibility Robustness | Sensitivity Subsets (Local Coverage $\ge 80\%$, $N = 20,548$) | Nearest Teammate $\text{OR} = 0.8833$; Initiation X $\text{OR} = 0.3810$ | Teammate: $[0.8445, 0.9240]$, Pitch X: $[0.3445, 0.4214]$ | Sensitivity analyses restricting the cohort to episodes with high camera coverage (>=80%) yielded qualitatively and quantitatively similar coefficient estimates, indicating that camera truncation does not drive the primary spatial findings. |

---

## 4. Terminology and Verification Guidelines

1. **Data Description**:
   - **Mandatory Terminology**: *"StatsBomb 360 freeze-frame spatial geometry"* or *"event-level 360 freeze-frame spatial geometry"*.
   - **Prohibited Terminology**: *"continuous tracking data"*, *"tracking-derived spatial geometry"*.
2. **Causal Attribution**:
   - **Prohibited**: *"due to direct central counter-attacking access"*, *"compact support guarantees possession recovery"*, *"numerical superiority mechanically dictates turnover outcome"*.
   - **Approved**: *"consistent with greater access to central counter-attacking space"*, *"holding modeled covariates fixed, closer proximity is associated with higher odds"*.
3. **Centrality Formulation**:
   - **Approved Wording**: *"Unadjusted regain rates were nearly flat across pitch width, but after adjustment greater centrality was associated with modestly higher regain odds. Central counterpress episodes were also associated with substantially greater dangerous-transition risk."*
   - Do NOT say "unsuccessful counterpresses" unless restricted explicitly to episodes without controlled regain.
4. **Validation Language**:
   - **Prohibited**: *"100% verified"*, *"ground-truth validated"*, *"fully human validated"*.
   - **Approved**: *"statistically audited"*, *"automated sanity-checked"*, *"internally consistent"*, *"reproducible"*.

---

## 5. Test Suite Verification

The test suite enforces all canonical invariants across 84 automated unit tests:
```bash
$ ./.venv/bin/pytest tests/ -v
============================== 84 passed in 2.41s ==============================
```
Specific consistency assertions in `tests/test_claim_consistency.py`:
- `test_assertion_a_model1_to_model3_regain_delta_roc_auc`: PASSED
- `test_assertion_b_model1_to_model3_regain_delta_pr_auc`: PASSED
- `test_assertion_c_pitch_third_danger_rates_direct_recomputation`: PASSED
- `test_assertion_d_primary_inferential_odds_ratios_equal_exp_coef`: PASSED
- `test_assertion_e_confidence_intervals_match_source_table`: PASSED
- `test_assertion_f_no_sensitivity_model_labeled_as_primary`: PASSED
- `test_assertion_g_forward_numerical_advantage_sign_definition`: PASSED
- `test_assertion_h_primary_cohort_invariants`: PASSED
- `test_assertion_i_primary_outcomes_invariants`: PASSED

---

## 6. Readiness Assessment

With all historical numerical discrepancies resolved, canonical model specifications formally established, claims table programmatically generated, and 84/84 tests passing:
- **Conference Abstract Drafting Status**: **APPROVED TO PROCEED**.
