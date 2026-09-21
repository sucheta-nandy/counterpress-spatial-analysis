# Full Manuscript Outline

**Working Title**: *When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer*  
**Target Submission**: MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Track  
**Current Milestone**: Iteration 5 Full Paper Architecture  

---

## 1. Introduction

### Argument / Purpose
* Establish counterpressing as a defining strategic concept in contemporary elite soccer, pioneered by high-tempo pressing philosophies to disrupt opponent build-up and capitalize on disorganization.
* Frame the central tactical tension: counterpressing is inherently high-risk, high-reward. Committing players toward the ball risks stranding defenders ahead of play and vacating central space if the initial wave is broken.
* Identify the empirical research gap: existing public analyses evaluate pressing using aggregate count metrics (e.g., PPDA, pressing event totals) without accounting for the spatial configuration of teammates and opponents when pressure is initiated.
* Articulate the core research question: What spatial conditions at counterpress initiation differentiate immediate possession recovery from opponent dangerous escape?

### Quantitative Results to Cite
* Primary cohort scale: 21,616 distinct counterpress episodes across 414 matches in seven elite domestic and international competitions.
* Baseline outcome distribution: 34.65% 5-second controlled regain rate; 22.41% 15-second dangerous-transition rate.

### Figure / Table Candidates
* **Figure 1**: Two contrasting StatsBomb 360 freeze frames at counterpress initiation: (A) compact overload leading to a 5s regain; (B) isolated presser bypassed leading to a dangerous transition.

### Materials Status
* **Available**: Full background context, verified episode counts, and motivating tactical framework.
* **Missing**: Formal external citations for historical tactical evolution.

---

## 2. Related Work

### Argument / Purpose
* Review literature across four relevant streams:
  1. *Tactical Theory of Counterpressing*: Tactical treatises on Gegenpressing, rest-defense, and transition phases.
  2. *Empirical Pressing Metrics*: PPDA, challenge intensity, defensive line height, and aggregate possession turnover statistics.
  3. *Spatial Soccer Analytics*: Pitch control models, voronoi tessellations, pass probability surfaces, and defensive compactness metrics.
  4. *Counterattack & Transition Risk*: Models of transition xG, counterattacking velocity, and space penetration following turnovers.
* Emphasize the methodological gap: previous spatial models rely heavily on either continuous tracking data (rarely open-access or multi-competition) or purely event-based data lacking surrounding player locations.

### Figure / Table Candidates
* **Table 1**: Comparative taxonomy of pressing research (event-only vs. continuous tracking vs. freeze-frame spatial geometry).

### Materials Status
* **Available**: Clear conceptual boundaries and critique of event-only limitations.
* **Missing**: Formal compilation of peer-reviewed citations (tracked in `docs/related_work_todo.md`).

---

## 3. Data and Acquisition

### Argument / Purpose
* Detail the StatsBomb Open Data and StatsBomb 360 Open Data repositories, describing the seven represented competitions: UEFA Euro 2024, FIFA World Cup 2022, UEFA Women's Euro 2022, FIFA Women's World Cup 2023, La Liga, Ligue 1, and 1. Bundesliga.
* Explain the 360 broadcast freeze-frame mechanism: computer-vision extracted player coordinates within the broadcast camera's field of view at the millisecond of specific on-ball events.
* Provide the coverage audit: explain that while broadcast truncation introduces missingness, 95.06% of episodes have $\ge 80\%$ camera coverage within 10 units of the ball.

### Quantitative Results to Cite
* Total matches: 414; total episodes: 21,616.
* Competition distribution: La Liga ($N=1,861$), UEFA Euro ($N=4,764$), Ligue 1 ($N=2,924$), Women's Euro ($N=3,533$), World Cup ($N=2,955$), WWC ($N=3,917$), Bundesliga ($N=1,662$).

### Figure / Table Candidates
* **Table 2**: Competition sample characteristics, match counts, and 360 availability rates.

### Materials Status
* **Available**: Complete data audit in [`docs/data_audit.md`](data_audit.md) and [`results/tables/competition_360_audit.csv`](../results/tables/competition_360_audit.csv).
* **Missing**: None.

---

## 4. Counterpress Episode Definition

### Argument / Purpose
* Formulate the rigorous, deterministic definition of a counterpress episode:
  - Triggered exclusively by open-play turnovers (dispossessions, misplaced passes, failed dribbles, rebounds).
  - Pressing team must exert defensive pressure (tagged `counterpress: true` or immediate pressure/duel/tackle) within 5.0 seconds of turnover.
  - Multi-action collapsing: contiguous defensive actions by the same pressing team within 5.0 seconds collapse into a single episode anchored at the earliest initiation event.
* Explain why action-level rows cannot be treated as statistically independent observations.

### Quantitative Results to Cite
* 40,054 raw counterpress actions collapsed into 21,616 distinct episodes.
* Inter-action latency distribution: median delay from turnover to pressure = 1.12 seconds.

### Figure / Table Candidates
* **Figure 2**: Episode extraction workflow diagram showing turnover detection, latency window, and action aggregation.

### Materials Status
* **Available**: Documented in [`docs/episode_definition.md`](episode_definition.md) and locked in [`results/tables/primary_cohort_episode_ids.csv`](../results/tables/primary_cohort_episode_ids.csv).
* **Missing**: None.

---

## 5. Outcome Definitions: Dual-Outcome Framework

### Argument / Purpose
* Establish that counterpressing cannot be evaluated along a single binary dimension. A counterpress can succeed (regain), fail harmlessly (opponent reset), or fail catastrophically (dangerous counterattack).
* Define the two primary binary targets and the three-state mutually exclusive taxonomy:
  1. `regain_5s_controlled`: Possession recovered within 5.000s with verified controlled action (carry, pass, shot, controlled duel/recovery). Defensive actions alone (blocks, pressures) do NOT qualify.
  2. `dangerous_escape_15s`: Opponent generates a shot or enters the defending final third within 15.000s of initiation.
  3. Mutually Exclusive 3-State: Successful Regain (32.27%), Harmless Escape (45.32%), Dangerous Escape (22.41%).

### Quantitative Results to Cite
* Controlled regains: 7,491 / 21,616 = 34.65% (5s horizon); 6,161 (3s, 28.50%); 8,878 (8s, 41.07%).
* Dangerous escapes: 4,844 / 21,616 = 22.41%.

### Figure / Table Candidates
* **Table 3**: Outcome event criteria, transition evidence rules, and baseline prevalence matrix.

### Materials Status
* **Available**: Codified in [`docs/outcome_definition.md`](outcome_definition.md) and passing automated invariant tests.
* **Missing**: None.

---

## 6. StatsBomb 360 Spatial Representation

### Argument / Purpose
* Describe the mathematical extraction of player coordinates from the initiation freeze frame.
* Detail coordinate normalization: standardizing pitch coordinates to $120 \times 80$ coordinate units with attacking direction oriented toward $x = 120$.
* Formulate the visible viewing frustum polygon, explaining how camera field of view is reconstructed and clipped to pitch boundaries.
* Define camera-coverage metrics: `coverage_10` (fraction of 10-unit radius circle visible) and `escape_corridor_coverage_20` (fraction of forward 20-unit wedge visible).

### Quantitative Results to Cite
* Mean visible area: 3,421 square coordinate units (~35.6% of pitch).
* Coverage rates: 95.06% have $\ge 80\%$ visibility at 10 units; 62.04% have $\ge 80\%$ corridor visibility.

### Figure / Table Candidates
* **Figure 3**: Geometric pitch representation illustrating visible viewing polygon, concentric density rings, and forward escape wedge.

### Materials Status
* **Available**: Documented in [`docs/spatial_feature_definition.md`](spatial_feature_definition.md).
* **Missing**: None.

---

## 7. Spatial Feature Engineering

### Argument / Purpose
* Detail the four feature families engineered at counterpress initiation:
  - **Family A (Local Support & Proximity)**: Distance to nearest, second-nearest, and third-nearest teammate/opponent; actor-to-ball distance.
  - **Family B (Local Opposition Density & Numerical Advantage)**: Player counts and numerical differentials (`teammates - opponents`, actor excluded) across 5, 10, and 15 coordinate unit concentric rings.
  - **Family C (Team Compactness & Dispersion)**: Mean pairwise distance, coordinate standard deviations, and convex hull area for teammates and opponents.
  - **Family D (Forward Escape Structure)**: Opponents ahead of ball, defenders ahead of ball, forward numerical advantage (`opponents - defenders`), and 20-unit escape corridor advantage.
* Clarify the strict exclusion of the pressing actor from teammate support metrics to isolate structural support from individual engagement.

### Quantitative Results to Cite
* Feature standard deviations: `initiation_x` ($\sigma = 26.99$), `nearest_teammate_distance` ($\sigma = 8.18$), `numerical_advantage_10` ($\sigma = 1.36$), `forward_numerical_advantage` ($\sigma = 1.73$).

### Figure / Table Candidates
* **Table 4**: Feature dictionary detailing operational definitions, coordinate transformations, and summary statistics.

### Materials Status
* **Available**: Full feature dataset in `counterpress_features.parquet` and documentation in [`docs/spatial_feature_definition.md`](spatial_feature_definition.md).
* **Missing**: None.

---

## 8. Modeling and Validation Methodology

### Argument / Purpose
* Describe the nested modeling hierarchy:
  - Model 0: Null baseline (empirical class prevalence).
  - Model 1: Context baseline (pitch location, event type, period, competition).
  - Model 2: Context + Local density features.
  - Model 3: Full Spatial Logistic Regression (`PRIMARY_INFERENTIAL_MODEL`).
  - Model 4: Additive Spline Generalized Additive Model (GAM).
  - Model 5: HistGradientBoosting Classifier (HGB).
* Validation architecture:
  - 5-fold match-clustered cross-validation (no match split across train and test).
  - Strictly isolated preprocessing (median imputation and $z$-score scaling computed on train folds only).
  - Multi-metric evaluation: ROC-AUC, PR-AUC, Brier score, log loss, calibration curves.
  - Statistical significance via 1,000 match-clustered paired bootstrap resamples.
  - Multivariable inferential GLM with sandwich robust standard errors clustered on `match_id` and Benjamini-Hochberg FDR $q$-values.

### Quantitative Results to Cite
* Calibration slope near unity: Model 3 regain calibration slope = $0.9971$, intercept = $-0.0021$.

### Figure / Table Candidates
* **Figure 4**: Modeling workflow: nested model hierarchy, grouped cross-validation, and paired bootstrap architecture.

### Materials Status
* **Available**: Complete scripts in `src/counterpress/modeling.py`, `scripts/run_iteration4_modeling.py`.
* **Missing**: None.

---

## 9. Results

### 9.1 Controlled Regain Within 5 Seconds
* Multivariable clustered GLM results (`PRIMARY_INFERENTIAL_MODEL`):
  - Immediate teammate proximity: $\beta = -0.2228, \text{OR} = 0.8003$ [95% CI: $0.7294, 0.8781$], $p < 0.0001, q < 0.0001$. Holding covariates fixed, 1 SD closer distance (~8.2 coordinate units) corresponds to +25.0% higher regain odds.
  - Broader numerical advantage: 10-unit $\text{OR} = 1.0705$ [95% CI: $1.0141, 1.1301$], $q = 0.0218$; 15-unit $\text{OR} = 1.1443$ [95% CI: $1.0852, 1.2067$], $q < 0.0001$.
  - Immediate 5-unit advantage non-significant ($\text{OR} = 1.0217, p = 0.3285$) after conditioning on broader rings.
  - Dispersion: opponent dispersion increases regain odds ($\text{OR} = 1.1332, q < 0.0001$).
* Model comparison: Linear sufficiency confirmed; GAM ($\Delta \text{ROC-AUC} = +0.0001$) and HGB ($\Delta \text{ROC-AUC} = -0.0011$) fail to improve out-of-sample discrimination over logistic regression.

### 9.2 Dangerous Transition Within 15 Seconds
* Multivariable clustered GLM results:
  - Longitudinal pitch position dominates: $\beta = -0.9715, \text{OR} = 0.3785$ [95% CI: $0.3591, 0.3990$], $z = -36.07, p < 0.0001$.
  - Descriptive escalation: Defensive-third danger = 31.57% vs. Attacking-third danger = 11.28% (nearly 3x increase).
  - Lateral centrality: distance to touchline $\beta = +0.1981, \text{OR} = 1.2190$ [95% CI: $1.1740, 1.2658$], $p < 0.0001$. Descriptive danger rises from 16.86% (wide) to 25.15% (central).
  - Forward numerical advantage: $\text{OR} = 1.0637$ [95% CI: $1.0147, 1.1150$], $q = 0.0206$.
* Model comparison: Non-linear benefit confirmed; HGB improves precision-recall ($\Delta \text{PR-AUC} = +0.0394$ [95% CI: $+0.0299, +0.0490$]) over spatial logistic, driven by threshold non-linearities at defensive-third boundaries.

### 9.3 Incremental Predictive Value of 360 Geometry
* Model 1 (Context: $0.7926$) vs. Model 3 (Full Spatial Logistic: $0.8156$): $\Delta \text{ROC-AUC} = +0.0230$, $\Delta \text{PR-AUC} = +0.0377$, $\Delta \text{Brier} = -0.0063$.
* Paired cluster bootstrap strictly excludes zero: $\Delta \text{ROC-AUC} = +0.0233$ [95% CI: $+0.0181, +0.0278$].
* Feature family ablation: Removing Family B (local numerical advantage) drops regain ROC-AUC by $-0.0067$; removing Family A (proximity) drops regain ROC-AUC by $-0.0042$. Forward structure (Family D) yields conditional associations but negligible incremental predictive discrimination ($\Delta \text{ROC-AUC} = 0.0000$).

### 9.4 Robustness and Generalizability
* Leave-One-Competition-Out (LOCO): Out-of-distribution transfer confirmed across all 7 competitions (Regain ROC-AUC: 0.7873 in Bundesliga to 0.8466 in Ligue 1; Danger ROC-AUC: 0.7532 to 0.7919).
* Broadcast Visibility Sensitivity: Restricting to episodes with $\ge 80\%$ camera coverage ($N = 20,548$) preserves coefficient signs, relative magnitudes, and overlapping confidence intervals (e.g., Nearest Teammate $\text{OR} = 0.8833$ vs. $0.8662$ full-cohort sensitivity; Initiation X $\text{OR} = 0.3810$ vs. $0.3738$).

### Figure / Table Candidates
* **Figure 5**: Forest plot of odds ratios from `PRIMARY_INFERENTIAL_MODEL` for Regain vs. Danger.
* **Figure 6**: Spatial distribution maps: (A) Regain rate by teammate proximity and numerical advantage; (B) Danger rate across pitch grid.
* **Figure 7**: Out-of-sample ROC and PR curves across Models 1–5.
* **Figure 8**: Partial dependence plots for transition danger non-linearities.
* **Table 5**: Canonical model performance metrics across 5-fold cross-validation.
* **Table 6**: Clustered logistic regression coefficients, standard errors, odds ratios, and FDR $q$-values.

### Materials Status
* **Available**: All tables, metrics, bootstrap intervals, and figures generated and verified.
* **Missing**: None.

---

## 10. Tactical Interpretation

### Argument / Purpose
* Synthesize the dual-outcome findings into concrete tactical principles:
  1. *Two Distinct Spatial Problems*: Winning the ball back is a local problem (support within 10–15 units); conceding danger is a global pitch problem (turnover depth and centrality).
  2. *The Centrality Trade-Off*: Unadjusted regain rates are flat across pitch width (34.30% wide vs. 34.85% central), but after adjustment central pressing has modestly higher regain odds ($\text{OR} = 1.111$). However, central counterpresses carry substantially higher transition danger (25.15% vs. 16.86%, $\text{OR} = 1.219$). Central pressing without overwhelming local compactness represents a hazardous gamble.
  3. *Coaching Decision Heuristic*: Pressing cues should be conditioned on local teammate proximity (is a teammate within 8 StatsBomb units?) rather than raw player counts. If immediate compact support is lacking, particularly in central areas, defensive units should delay and drop.

### Materials Status
* **Available**: Verified findings, cautious phrasing guidelines locked in `docs/iteration4_6_claims_freeze.md`.
* **Missing**: None.

---

## 11. Limitations

### Argument / Purpose
* Transparently delineate methodological boundaries:
  1. *Event-Level Freeze Frames*: Freeze frames capture spatial geometry at initiation only; player velocities, accelerations, and orientations are unobserved in broadcast freeze frames.
  2. *Broadcast Camera Truncation*: Players located outside the broadcast camera view are unobserved. While sensitivity models confirm that primary associations are stable in high-visibility subsets, extreme wide players may be missing.
  3. *Observational Data*: Findings represent associative conditional relationships, not causal treatment effects. Tactical selection bias may influence when teams choose to press.
  4. *Human Adjudication Scope*: While outcome algorithms are internally consistent and statistically audited, human adjudication of full video traces remains an ongoing validation objective.

### Materials Status
* **Available**: Comprehensive limitations framework.
* **Missing**: None.

---

## 12. Conclusion

### Argument / Purpose
* Summarize core findings: StatsBomb 360 freeze frames provide reliable predictive value beyond event data; local proximity governs regains, while pitch geography governs danger.
* State final implication: Moving beyond aggregate pressing counts toward spatial freeze-frame evaluation provides clubs with objective criteria to optimize pressing triggers and manage transition exposure.

### Materials Status
* **Available**: Complete.
* **Missing**: None.
