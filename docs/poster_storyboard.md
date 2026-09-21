# Conference Poster Storyboard

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Layout**: Standard 36" x 48" or 48" x 36" Landscape Research Poster  
**Design Philosophy**: Visual-first, scannable architecture; 6 structured blocks with callout metrics, pitch plots, and empirical curves.

---

```
+---------------------------------------------------------------------------------------------------+
|  TITLE: When Does the Counterpress Work? Spatial Predictors of Possession Regain & Transition Risk |
|  AUTHORS: [Author List]  |  INSTITUTION: [Affiliation]  |  GITHUB: [PUBLIC REPOSITORY URL]         |
+------------------------------------+----------------------------------+---------------------------+
| BLOCK 1: THE RESEARCH QUESTION     | BLOCK 3: 360 GEOMETRY AT         | BLOCK 5: WHAT PREDICTS    |
| - Tactical tension: Regain vs Risk |          COUNTERPRESS INITIATION |          DANGEROUS ESCAPE?|
| - Event metrics vs Spatial Reality | - Visible viewing frustum        | - Pitch depth dominance   |
| - Dual-outcome framework           | - Concentric rings & corridors   | - Centrality trade-off    |
|                                    | - Proximity & compactness        | - Non-linear thresholds   |
| [Visual: Dual-outcome diagram]     | [Visual: Annotated 360 pitch]    | [Visual: Danger PDP & map]|
+------------------------------------+----------------------------------+---------------------------+
| BLOCK 2: DATASET & DEFINITIONS     | BLOCK 4: WHAT PREDICTS REGAIN?   | BLOCK 6: TACTICAL RULES & |
| - 21,616 episodes, 414 matches     | - Immediate teammate proximity   |          LIMITATIONS      |
| - 7 elite competitions             | - Broader numerical support      | - Local cue vs macro risk |
| - Strict transition evidence       | - Linear sufficiency (AUC 0.816) | - Central pressing hazard |
|                                    | - +2.3% AUC over context         | - 360 freeze-frame bounds |
| [Visual: Competition breakdown]    | [Visual: Regain proximity curve] | [Visual: Decision matrix] |
+------------------------------------+----------------------------------+---------------------------+
```

---

## Block 1: The Research Question & Tactical Dilemma
* **Headline**: *Counterpressing is high-risk, high-reward: when should teams press vs. drop?*
* **Core Problem**:
  - Teams counterpress to win the ball high or disrupt build-up.
  - When bypassed, defenders are stranded, creating dangerous counter-attacking voids.
  - Existing analytics count pressing actions (PPDA) but ignore the spatial structure present when pressure begins.
* **Dual-Outcome Formulation**:
  - **Success**: Controlled possession regain within 5 seconds (Baseline: **34.65%**).
  - **Failure**: Opponent dangerous transition (shot or final-third entry) within 15 seconds (Baseline: **22.41%**).
* **Recommended Visual**: High-contrast iconographic diagram contrasting a successful turnover recovery with an opponent counterattack exploiting central space.

---

## Block 2: Dataset & Episode Definition
* **Headline**: *21,616 distinct episodes extracted deterministically across 414 professional matches.*
* **Cohort Integrity**:
  - Open-play turnovers only; pressure exerted within 5.0 seconds.
  - Multi-action collapsing: contiguous pressures merged into single distinct episodes.
  - Seven competition groups: UEFA Euro 2024, FIFA World Cup 2022, Ligue 1, La Liga, 1. Bundesliga, Women's Euro, Women's World Cup.
* **Strict Outcome Criteria**: Controlled regains require verifiable transition evidence (carries, completed passes, controlled recoveries); defensive deflections alone do not count.
* **Recommended Visual**: Cohort summary graphic showing the reduction from 40,054 raw actions to 21,616 distinct episodes across 414 matches.

---

## Block 3: StatsBomb 360 Freeze-Frame Geometry
* **Headline**: *Extracting spatial structure at counterpress initiation from broadcast freeze frames.*
* **Geometric Feature Families**:
  - **Local Proximity**: Distance to nearest teammate ($\sigma = 8.2$ units) and opponent.
  - **Numerical Advantage**: Player differentials in concentric 5u, 10u, and 15u rings (actor strictly excluded).
  - **Team Compactness**: Mean pairwise distances, player coordinate standard deviations.
  - **Escape Corridors**: 20-unit forward escape wedge toward goal.
* **Recommended Visual**: **[`results/figures/counterpress_example_1_worldcup.png`](../results/figures/counterpress_example_1_worldcup.png)**:
  - Annotated pitch plot displaying the visible camera polygon, ball position, nearest-teammate distance vector, and concentric support rings.

---

## Block 4: What Predicts Controlled Regain? (Local Compactness)
* **Headline**: *Possession regain is a local proximity problem governed by immediate support.*
* **Empirical Highlights**:
  - **Incremental Predictive Value**: Spatial geometry adds statistically reliable information beyond context ($\Delta \text{ROC-AUC} = \mathbf{+0.0230}$, $\Delta \text{PR-AUC} = \mathbf{+0.0377}$, paired bootstrap 95% CI $[+0.0181, +0.0278]$).
  - **Nearest Teammate Distance**: $\mathbf{\text{OR} = 0.800}$ [95% CI: $0.729, 0.878$] per 1 SD (~8.2 coordinate units). Being 1 SD closer corresponds to **+25.0% higher regain odds**.
  - **Numerical Overload**: Significant at 10u ($\mathbf{\text{OR} = 1.071}$) and 15u ($\mathbf{\text{OR} = 1.144}$), but immediate 5u surplus is not independently significant after adjusting for broader support.
  - **Linear Sufficiency**: Flexible non-linear models (GAM $\Delta \text{AUC} = +0.0001$; HGB $\Delta \text{AUC} = -0.0011$) do not improve discrimination over spatial logistic regression.
* **Recommended Visual**: **[`results/figures/regain_nearest_teammate.png`](../results/figures/regain_nearest_teammate.png)**:
  - Bar plot showing observed regain rate decaying monotonically from **54.31%** (Q1, nearest teammate < 4.2 units) down to **24.44%** (Q5, nearest teammate > 12.8 units).

---

## Block 5: What Predicts Dangerous Escape? (Pitch Geography)
* **Headline**: *Transition danger is dominated by pitch depth, centrality, and non-linear thresholding.*
* **Empirical Highlights**:
  - **Longitudinal Depth**: Turnovers in the defensive third yield **31.57%** danger versus **11.28%** in the attacking third ($\mathbf{\text{OR} = 0.379}$ [95% CI: $0.359, 0.399$]).
  - **The Centrality Trade-Off**: Central counterpresses have nearly flat unadjusted regain rates (34.85% vs. 34.30% wide) and modest adjusted regain benefit ($\text{OR} = 1.111$), but expose teams to massive transition danger: **25.15% central vs. 16.86% wide** ($\mathbf{\text{OR} = 1.219}$ [95% CI: $1.174, 1.266$]).
  - **Non-Linear Benefit**: Gradient boosting improves probability ranking and precision-recall ($\mathbf{\Delta \text{PR-AUC} = +0.0394}$ [95% CI: $+0.0299, +0.0490$]) by capturing sharp threshold danger spikes once pressure is breached.
* **Recommended Visual**: **[`results/figures/figure_8_danger_nonlinearity_diagnostics.png`](../results/figures/figure_8_danger_nonlinearity_diagnostics.png)**:
  - Partial dependence curves illustrating the steep drop in transition danger as turnover location moves upfield ($x > 60$) and the steep penalty for central initiation ($y \in [30, 50]$).

---

## Block 6: Tactical Rules & Methodological Limitations
* **Headline**: *Actionable decision heuristics for coaching staffs; rigorous science boundaries.*
* **Three Tactical Heuristics**:
  1. *Condition on Proximity, Not Headcount*: Having a teammate within ~8 StatsBomb units is the primary spatial correlate of regain. If nearest support is distant, pressing rarely succeeds.
  2. *Avoid the Central Trap*: Pressing centrally without overwhelming compact support carries extreme downside (+49% relative danger increase) for marginal regain upside.
  3. *Separate Triggers from Exposure*: Pressing cues must account for defensive depth; attacking-third counterpressing carries minimal danger even when failed.
* **Limitations**:
  - Freeze frames capture geometry at initiation; player velocity/acceleration unobserved.
  - Broadcast camera truncation affects extreme peripheral players (though findings replicate in $\ge 80\%$ visibility subsets).
  - Observational associations, not causal interventions.
* **Recommended Visual**: Two-by-two Tactical Decision Matrix ("Press Immediately" vs. "Delay & Recover") based on teammate proximity and pitch depth.

---

## Recommended 5 Figures for Poster Adaptation

1. **[`counterpress_example_1_worldcup.png`](../results/figures/counterpress_example_1_worldcup.png)**: Visualizing the 360 freeze frame and geometric feature extraction on the pitch.
2. **[`model_performance.png`](../results/figures/model_performance.png)**: Out-of-sample ROC and PR curves demonstrating the +2.3% AUC incremental value of spatial geometry.
3. **[`regain_nearest_teammate.png`](../results/figures/regain_nearest_teammate.png)**: Observed regain rate by teammate proximity quintile (54.3% down to 24.4%).
4. **[`figure_8_danger_nonlinearity_diagnostics.png`](../results/figures/figure_8_danger_nonlinearity_diagnostics.png)**: Partial dependence plots illustrating pitch-depth and centrality threshold effects for transition danger.
5. **[`calibration_regain.png`](../results/figures/calibration_regain.png)**: Out-of-fold calibration curves demonstrating near-unity calibration slope (0.997) for the primary spatial model.
