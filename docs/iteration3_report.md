# Iteration 3 Milestone Report: Spatial Feature Engineering and Freeze-Frame Processing

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Date**: September 2026  
**Status**: Completed & Validated (Pre-Modeling Feature Freeze)

---

## 1. Executive Summary

Iteration 3 completes the spatial feature engineering and freeze-frame geometry processing pipeline for all **21,616 distinct counterpress episodes** across **414 matches** in the frozen primary cohort.

### Key Achievements:
1. **Zero Data Loss & Invariant Preservation**:
   - Exactly **21,616 rows** and **84 columns** in [`data/processed/counterpress_features.parquet`](../data/processed/counterpress_features.parquet).
   - Zero episode drops, zero duplications, and exact 1-to-1 correspondence with the canonical cohort manifest ([`results/tables/primary_cohort_episode_ids.csv`](../results/tables/primary_cohort_episode_ids.csv)).
2. **Strict Temporal Leakage Enforcement**:
   - All spatial features are derived strictly and exclusively from the 360 freeze frame captured at the exact moment of counterpress initiation ($t \le t_{\text{init}}$).
   - Post-initiation event sequences ($t > t_{\text{init}}$) were strictly excluded from feature computation.
3. **Rigorous Geometric Formulations**:
   - All spatial coordinates, distances, and areas are strictly measured in **StatsBomb coordinate units** ($120 \times 80$).
   - Camera coverage at 5, 10, and 15 coordinate units is calculated with pitch boundary clipping to ensure the denominator is the exact on-pitch circle area ($\text{Area}(\text{Circle}_r \cap \text{Pitch})$), preventing boundary distortion for touchline presses.
   - Convex hulls strictly require $\ge 3$ non-collinear player locations; frames with fewer players return `NaN` rather than misleading $0.0$ area values.
   - Forward escape corridors are geometrically formulated as a $20$-unit circular sector ($60^\circ$ arc, half-angle $30^\circ$) directed toward the opponent's attacking goal center $(120, 40)$.
4. **Comprehensive Quality Control**:
   - 100% of primary cohort episodes have matching 360 freeze frames and valid pitch-clipped visible polygons.
   - Identified and isolated an actor-perspective orientation edge case (3.64% of episodes, predominantly `Dribbled Past` and defensive duel events) using an explicit boolean QA flag (`actor_matching_anomalous`) without discarding episodes.
   - Built a comprehensive visual QA suite generating 20 stratified freeze-frame diagnostic figures in [`results/figures/qa_spatial/`](../results/figures/qa_spatial/).
   - 69 automated unit and regression tests passing with 100% compliance.

---

## 2. Methodology & Geometric Formulations

### 2.1 Coordinate Conventions and Frame Inversion
StatsBomb 360 freeze frames store player coordinates and the visible camera polygon in the coordinate frame of the event. In approximately 3.64% of events (e.g., when the initiation event is logged as `Dribbled Past` or from an opponent's duel perspective), coordinates are oriented from the opponent's attacking direction.
- **Inversion Transformation**:
  $$\begin{aligned}
  x_{\text{opp}} &= 120.0 - x \\
  y_{\text{opp}} &= 80.0 - y
  \end{aligned}$$
- When transforming visible area polygons, vertex order is reversed to maintain standard counter-clockwise (CCW) polygon orientation required by planar geometry engines.
- **Actor Identification**: The counterpressing actor is identified by matching `actor == True` in the 360 freeze frame. The actor is strictly excluded from teammate counts to avoid auto-inflating pressing team local support.
- **QA Metrics**: `actor_distance_from_event` tracks the Euclidean distance between the initiation event coordinate and the matched actor. When distance exceeds $1.0$ unit, `actor_matching_anomalous` is set to `True`.

### 2.2 Camera Viewport and Pitch Clipping
- The visible viewport is represented by a Shapely polygon clipped to the pitch boundary $[0, 120] \times [0, 80]$ (total pitch area $9,600.0$ units):
  $$P_{\text{visible}} = P_{\text{raw}} \cap [0, 120] \times [0, 80]$$
- Visible pitch fraction is computed as $\text{Area}(P_{\text{visible}}) / 9600.0$.

### 2.3 Boundary-Aware Camera Coverage
Around initiation location $(x_0, y_0)$, local observation rings of radii $r \in \{5, 10, 15\}$ are clipped to the pitch:
$$C_{r, \text{pitch}} = \text{Circle}( (x_0, y_0), r ) \cap \text{Pitch}$$
The camera coverage within radius $r$ is:
$$\text{Coverage}_r = \frac{\text{Area}(C_{r, \text{pitch}} \cap P_{\text{visible}})}{\text{Area}(C_{r, \text{pitch}})}$$
This guarantees $\text{Coverage}_r \in [0.0, 1.0]$. A boolean flag `coverage_{r}_ge_80pct` identifies frames with $\ge 80\%$ visual coverage suitable for unconfounded spatial density analysis.

### 2.4 Forward Escape Corridor
The forward escape corridor models the opponent's immediate passing and ball-carrying lane toward the counterpressing team's goal $(120, 40)$:
- Radius $R = 20.0$ coordinate units.
- Central axis vector directed from $(x_0, y_0)$ to $(120.0, 40.0)$.
- Angle range $[\theta_0 - 30^\circ, \theta_0 + 30^\circ]$ ($60^\circ$ total arc).
- Theoretical sector area:
  $$A_{\text{corridor}} = \frac{60^\circ}{360^\circ} \pi (20)^2 = \frac{400\pi}{6} \approx 209.44 \text{ units}^2$$
- Corridor coverage is defined as:
  $$\text{Coverage}_{\text{corridor}} = \frac{\text{Area}(W_{\text{corridor}} \cap \text{Pitch} \cap P_{\text{visible}})}{\text{Area}(W_{\text{corridor}} \cap \text{Pitch})}$$

### 2.5 Dispersion and Compactness Metrics
- **Convex Hull Area**: Evaluated separately for visible teammates (excluding actor) and visible opponents. Formally requires $\ge 3$ non-collinear coordinates. When $< 3$ players are visible, the hull is mathematically undefined and strictly returned as `NaN` (never $0.0$).
- **Mean Pairwise Distance**: For a group of $N$ players ($N \ge 2$):
  $$\bar{d} = \frac{2}{N(N-1)} \sum_{i < j} d(p_i, p_j)$$
  Returned as `NaN` if $N < 2$.

---

## 3. Spatial Feature Summary and Distributions

The complete feature summary across all 21,616 primary cohort episodes is saved in [`results/tables/spatial_feature_summary.csv`](../results/tables/spatial_feature_summary.csv).

### Table 3.1: Camera Coverage & Viewport Completeness
| Feature Name | Valid Obs | Valid % | Mean | Std | 25% | Median | 75% | Coverage $\ge 80\%$ Count (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `coverage_5` | 21,616 | 100.0% | 0.969 | 0.125 | 1.000 | 1.000 | 1.000 | 20,882 (96.60%) |
| `coverage_10` | 21,616 | 100.0% | 0.956 | 0.134 | 1.000 | 1.000 | 1.000 | 20,547 (95.05%) |
| `coverage_15` | 21,616 | 100.0% | 0.919 | 0.155 | 0.902 | 0.984 | 1.000 | 19,535 (90.37%) |
| `escape_corridor_coverage_20` | 21,616 | 100.0% | 0.778 | 0.278 | 0.613 | 0.924 | 1.000 | 13,873 (64.18%) |
| `visible_area_pitch_fraction` | 21,616 | 100.0% | 0.366 | 0.108 | 0.288 | 0.354 | 0.434 | — |

*Observation*: Camera coverage within immediate pressing proximity (5 and 10 units) is exceptionally high ($>95\%$ of episodes have $\ge 80\%$ coverage). Coverage diminishes slightly for the 20-unit forward escape corridor (mean 77.82%) as forward passes often point toward off-screen pitch areas.

---

### Table 3.2: Visible Player Counts & Frame Composition
| Feature Name | Valid Obs | Mean | Std | Min | 25% | Median | 75% | Max |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `frame_player_count` | 21,616 | 15.48 | 3.05 | 3 | 14 | 16 | 18 | 22 |
| `visible_teammate_count_excluding_actor` | 21,616 | 6.54 | 1.89 | 0 | 5 | 7 | 8 | 10 |
| `visible_opponent_count` | 21,616 | 7.95 | 1.85 | 1 | 7 | 8 | 9 | 11 |
| `visible_goalkeeper_count` | 21,616 | 0.35 | 0.48 | 0 | 0 | 0 | 1 | 1 |

*Observation*: On average, 15.48 of the 22 players on the pitch are captured in the 360 freeze frame at counterpress initiation. Teammate support averages 6.54 players (excluding the actor), while opponent presence averages 7.95 players.

---

### Table 3.3: Local Numerical Advantage & Opposition
| Feature Name | Valid Obs | Mean | Std | Min | 25% | Median | 75% | Max |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `visible_teammates_within_5` | 21,616 | 0.40 | 0.65 | 0 | 0 | 0 | 1 | 4 |
| `visible_opponents_within_5` | 21,616 | 1.30 | 0.65 | 0 | 1 | 1 | 2 | 7 |
| `numerical_advantage_5` | 21,616 | -0.90 | 0.80 | -7 | -1 | -1 | 0 | +3 |
| `visible_teammates_within_10` | 21,616 | 1.54 | 1.25 | 0 | 1 | 1 | 2 | 7 |
| `visible_opponents_within_10` | 21,616 | 2.47 | 1.27 | 0 | 2 | 2 | 3 | 8 |
| `numerical_advantage_10` | 21,616 | -0.93 | 1.36 | -7 | -2 | -1 | 0 | +5 |
| `visible_teammates_within_15` | 21,616 | 3.01 | 1.70 | 0 | 2 | 3 | 4 | 9 |
| `visible_opponents_within_15` | 21,616 | 3.98 | 1.75 | 0 | 3 | 4 | 5 | 10 |
| `numerical_advantage_15` | 21,616 | -0.97 | 1.72 | -8 | -2 | -1 | 0 | +5 |

*Tactical Insight*: Across all local radii (5, 10, and 15 units), the counterpressing team is at an average numerical deficit of approximately -0.90 to -0.97 players relative to the opponent. Because the counterpressing team has just turned the ball over, the recovering opponent naturally clusters near the ball, requiring pressing actors to challenge under local numerical inferiority.

---

### Table 3.4: Forward Escape Structure and Corridor Metrics
| Feature Name | Valid Obs | Mean | Std | Min | 25% | Median | 75% | Max |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `opponents_ahead_of_ball` | 21,616 | 3.09 | 2.10 | 0 | 1 | 3 | 4 | 11 |
| `defenders_ahead_of_ball` | 21,616 | 3.55 | 2.01 | 0 | 2 | 3 | 5 | 10 |
| `forward_numerical_advantage` | 21,616 | -0.46 | 1.73 | -7 | -2 | -1 | 1 | +6 |
| `opponents_in_escape_corridor_20` | 21,616 | 0.62 | 0.76 | 0 | 0 | 0 | 1 | 6 |
| `defenders_in_escape_corridor_20` | 21,616 | 0.84 | 0.86 | 0 | 0 | 1 | 1 | 6 |
| `escape_corridor_advantage_20` | 21,616 | -0.22 | 0.90 | -6 | -1 | 0 | 0 | +5 |

*Tactical Insight*: In the forward corridor directed toward the counterpressing team's goal, the pressing team typically positions slightly more defending players than opponent targets (0.84 defenders vs 0.62 opponents), providing a defensive buffer against direct vertical escape passes.

---

### Table 3.5: Proximity, Dispersion, and Compactness
| Feature Name | Valid Obs | Valid % | Mean | Std | 25% | Median | 75% |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `nearest_teammate_distance` | 21,584 | 99.85% | 8.86 | 6.01 | 4.67 | 7.30 | 11.23 |
| `second_nearest_teammate_distance`| 21,401 | 98.98% | 12.96 | 7.42 | 7.74 | 10.98 | 16.03 |
| `nearest_opponent_distance` | 21,616 | 100.0% | 3.86 | 4.88 | 1.25 | 2.23 | 4.38 |
| `second_nearest_opponent_distance`| 21,610 | 99.97% | 9.38 | 6.30 | 5.09 | 7.48 | 11.75 |
| `teammate_mean_pairwise_distance`| 21,401 | 98.98% | 21.94 | 5.37 | 18.23 | 21.83 | 25.56 |
| `opponent_mean_pairwise_distance`| 21,610 | 99.97% | 20.70 | 4.54 | 17.65 | 20.55 | 23.63 |
| `teammate_hull_area` | 20,989 | 97.10% | 553.99 | 291.68 | 344.97 | 509.79 | 719.12 |
| `opponent_hull_area` | 21,532 | 99.61% | 590.67 | 277.56 | 390.43 | 545.75 | 743.08 |

*Missingness Note*: Convex hull areas and pairwise distances are strictly `NaN` when fewer than 3 or 2 players are visible, respectively. No artificial zeros were imputed.

---

## 4. Visual Quality Assurance Gallery

Twenty publication-grade diagnostic freeze frames were generated across stratified tactical contexts (high vs. low density, high vs. low coverage, touchline vs. central, positive vs. negative numerical advantage). All 20 plots are stored in [`results/figures/qa_spatial/`](../results/figures/qa_spatial/).

### Key Visual Diagnostic Features:
1. **Pitch Geometry**: Full $120 \times 80$ pitch with penalty boxes, center circle, and goal areas.
2. **Camera Viewport**: Shaded 360 visible area polygon.
3. **Player Markers**:
   - Counterpress Actor: Gold star.
   - Teammates: Sky-blue circles.
   - Opponents: Coral-red circles (goalkeepers distinct).
4. **Tactical Rings**: Concentric circles at 5, 10, and 15 StatsBomb coordinate units.
5. **Escape Wedge**: 20-unit circular sector ($60^\circ$ arc) pointing directly toward the opponent's attacking goal center $(120, 40)$.
6. **Tactical Header & Metric Overlay**: Real-time display of local numerical advantage, camera coverage, and corridor advantage.

Below is a reference visual QA plot:
- [`qa_spatial_01_3857258_p43_4b80fdea.png`](../results/figures/qa_spatial/qa_spatial_01_3857258_p43_4b80fdea.png)

---

## 5. Verification of Cohort & Outcome Invariants

The primary cohort membership and canonical outcome distribution established in Iterations 2.5–2.7 remain completely preserved and uncorrupted:

| Metric | Canonical Target | Parquet Actual | Match Status |
| :--- | :---: | :---: | :---: |
| **Total Episodes** | 21,616 | 21,616 | **EXACT MATCH** |
| **Unique Matches** | 414 | 414 | **EXACT MATCH** |
| **Duplicate Episode IDs** | 0 | 0 | **EXACT MATCH** |
| **regain_5s_controlled = 1** | 7,491 (34.65%) | 7,491 (34.65%) | **EXACT MATCH** |
| **dangerous_escape_15s = 1** | 4,844 (22.41%) | 4,844 (22.41%) | **EXACT MATCH** |
| **successful_regain** | 6,976 (32.27%) | 6,976 (32.27%) | **EXACT MATCH** |
| **harmless_escape** | 9,796 (45.32%) | 9,796 (45.32%) | **EXACT MATCH** |
| **dangerous_escape** | 4,844 (22.41%) | 4,844 (22.41%) | **EXACT MATCH** |

---

## 6. Recommendations for Iteration 4 (Predictive Modeling)

1. **Match-Clustered Cross-Validation**:
   - Episodes within the same match are tactically and statistically interdependent.
   - All cross-validation splits and holdout test sets in Iteration 4 MUST be grouped by `match_id` (e.g., `GroupKFold(groups=df['match_id'])`).
2. **Camera Coverage Gating & Sensitivity Analysis**:
   - Primary modeling should evaluate both:
     - The complete cohort ($N = 21,616$) with missing indicators / coverage covariates.
     - The high-coverage subset (`coverage_10_ge_80pct == True`, $N = 20,547$, 95.05%) to demonstrate that camera unobservability does not bias spatial effect estimates.
3. **Addressing Actor Perspective Anomalies**:
   - Filter or include `actor_matching_anomalous` as a covariate / sensitivity check ($N = 787$, 3.64%) to ensure opponent-oriented frames do not introduce structural noise into spatial coefficients.
4. **Nonlinear & Multilevel Architecture**:
   - Logistic regression baselines with clustered standard errors.
   - Generalized Additive Models (GAMs) and gradient-boosted trees (XGBoost / LightGBM) to capture non-linear relationships between spatial distance, numerical density, and regain probability.
   - Separate modeling pathways for the binary outcomes (`regain_5s_controlled`, `dangerous_escape_15s`) and the multinomial three-state outcome.
