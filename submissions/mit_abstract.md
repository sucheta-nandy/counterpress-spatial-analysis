# MIT Sloan Sports Analytics Conference (SSAC) Research Paper Submission

## Paper Title
**When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer**

## Track
Research Paper Competition — Soccer / Team Tactics

## Authors
Research Team

---

## Extended Abstract

### 1. Motivation & Context
In elite contemporary soccer, counterpressing—the immediate application of defensive pressure by a team upon losing possession—has become an essential tactical pillar. However, counterpressing represents a fundamental tactical trade-off: aggressive forward commitment to recover the ball risks bypassing the initial defensive line, conceding dangerous open transitions to the opponent. While event-level statistics capture when a counterpress action occurs, they cannot explain *why* certain attempts succeed in forcing a turnover while others fail catastrophically.

### 2. Data & Methodology
Using **StatsBomb Open Data** and **StatsBomb 360 freeze frames** across 424 matches (comprising 50,366 raw counterpress actions and 40,054 actions with verified freeze frames across the 2022 FIFA World Cup, UEFA Euro 2020/2024, 2023/24 Bundesliga, La Liga, and Women's World Cup), we aggregate multiple defensive actions within the same post-turnover possession into distinct **counterpress episodes** to eliminate pseudo-replication. We extract raw geometric player configurations at the initiation of each counterpress episode. 

We engineer interpretable spatial predictors:
1. **Local Numerical Superiority & Density**: Teammates minus opponents within concentric Euclidean radii of 5, 10, and 15 StatsBomb coordinate units.
2. **Nearest Player Distances**: Separation to first and second-nearest teammate and opponent.
3. **Unit Compactness**: Longitudinal and lateral spatial spread ($\sigma_x, \sigma_y$) and convex hull areas.
4. **Escape-Space Geometry**: Uncontested forward corridors and opponent numerical advantage between the ball carrier and the defending goal.
5. **Camera Viewport Controls**: Visible polygon area and player counts to control for broadcast frustum censoring.

We evaluate two distinct operational horizons:
- **Possession Regain within 5 Seconds**: Recovering established possession within 5.0 seconds of counterpress initiation.
- **Transition Risk within 15 Seconds**: The opponent escaping pressure to generate a shot or penetrate the attacking final third ($x \ge 80.0$), conditional on not initiating in that zone.

### 3. Validation & Practical Applications
Models are evaluated using Grouped $K$-Fold cross-validation (grouped by `match_id`) and Leave-Competition-Out validation to measure cross-competition generalization. Probability metrics including ROC-AUC, Brier score, and calibration curves are reported. The resulting spatial risk-reward frontier provides actionable tactical guidelines for coaching staffs to optimize trigger thresholds for counterpressing versus immediate defensive rest-defense retreat.
