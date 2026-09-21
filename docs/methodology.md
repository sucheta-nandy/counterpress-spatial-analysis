# Research Methodology

**Working Title**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Conferences**: MIT Sloan Sports Analytics Conference (SSAC) & Carnegie Mellon Sports Analytics Conference (CMSAC)  

---

## 1. Research Questions & Hypotheses

### Primary Research Questions
1. **Regain Predictors (RQ1)**: Among counterpressing attempts, which spatial characteristics at the moment of initiation are most strongly associated with regaining possession within 5 seconds?
   - *Hypothesis 1*: Immediate numerical superiority within a 5-yard radius and compactness of the pressing unit will be the strongest positive predictors of rapid regain.
2. **Transition Risk (RQ2)**: Which spatial characteristics are associated with the opponent successfully bypassing the counterpress and generating a dangerous attacking transition (final third entry or shot within 15 seconds)?
   - *Hypothesis 2*: Opponents with unimpeded forward escape corridors (nearest defender distance ahead $> 15$ yards) and an imbalanced pressing structure (large distance between pressing actor and second-nearest teammate) will dramatically elevate transition risk.
3. **Generalizability (RQ3)**: Do these spatial relationships generalize across diverse domestic leagues, international tournaments, and women's competitions?
   - *Hypothesis 3*: While baseline regain probabilities vary by league pace and pressing intensity, the marginal spatial effects (e.g. odds ratio per additional opponent within 5 yards) remain stable across competitions.

---

## 2. Mathematical Framework & Spatial Definitions

### Pitch Coordinate Representation
Let $\mathcal{P} = [0, 120] \times [0, 80]$ represent the StatsBomb pitch in StatsBomb coordinate units.
For a counterpress initiation event $e_i$ defining episode $i$ at initiation timestamp $t_i$:
- Location of the pressing actor: $\mathbf{x}_{\text{actor}} = (x_0, y_0) \in \mathcal{P}$.
- Visible teammates: $\mathcal{T} = \{\mathbf{x}_{T, 1}, \mathbf{x}_{T, 2}, \dots, \mathbf{x}_{T, N_T}\}$.
- Visible opponents: $\mathcal{O} = \{\mathbf{x}_{O, 1}, \mathbf{x}_{O, 2}, \dots, \mathbf{x}_{O, N_O}\}$.
- Camera viewport polygon: $\mathcal{V} \subset \mathcal{P}$.

### Spatial Feature Formulations

1. **Local Density at Radius $R \in \{5, 10, 15\}$ StatsBomb coordinate units**:
   $$D_T(R) = \sum_{\mathbf{x} \in \mathcal{T}} \mathbb{I}(\|\mathbf{x} - \mathbf{x}_{\text{actor}}\|_2 \le R)$$
   $$D_O(R) = \sum_{\mathbf{x} \in \mathcal{O}} \mathbb{I}(\|\mathbf{x} - \mathbf{x}_{\text{actor}}\|_2 \le R)$$

2. **Numerical Superiority**:
   $$S(R) = D_T(R) - D_O(R)$$

3. **Nearest Player Distances**:
   $$d_{T, (k)} = k\text{-th smallest } \{\|\mathbf{x} - \mathbf{x}_{\text{actor}}\|_2 : \mathbf{x} \in \mathcal{T}\}$$
   $$d_{O, (k)} = k\text{-th smallest } \{\|\mathbf{x} - \mathbf{x}_{\text{actor}}\|_2 : \mathbf{x} \in \mathcal{O}\}$$

4. **Local Compactness (Spread & Convex Hull)**:
   $$\sigma_{x, T}^2 = \frac{1}{|\mathcal{T}|}\sum_{\mathbf{x} \in \mathcal{T}} (x - \bar{x}_T)^2, \quad \sigma_{y, T}^2 = \frac{1}{|\mathcal{T}|}\sum_{\mathbf{x} \in \mathcal{T}} (y - \bar{y}_T)^2$$
   $$\text{Area}(\text{ConvexHull}(\mathcal{T}_{\text{local}}))$$

5. **Pitch Location & Centrality**:
   $$\text{Centrality} = 40.0 - |y_0 - 40.0|$$
   $$\text{DistTouchline} = \min(y_0, 80.0 - y_0)$$
   $$\text{DistAttackingGoal} = \sqrt{(120.0 - x_0)^2 + (40.0 - y_0)^2}$$

6. **Forward Escape Space & Corridors**:
   Let the opponent's attacking direction be toward $x = 0$ (defending team goal).
   $$\mathcal{O}_{\text{ahead}} = \{\mathbf{x} \in \mathcal{O} : x < x_0\}$$
   $$\mathcal{T}_{\text{behind}} = \{\mathbf{x} \in \mathcal{T} : x < x_0\}$$
   Forward numerical advantage of opponent: $|\mathcal{O}_{\text{ahead}}| - |\mathcal{T}_{\text{behind}}|$.

7. **Camera Visibility Controls**:
   $$A_{\text{vis}} = \text{Area}(\mathcal{V}), \quad N_{\text{vis}} = N_T + N_O$$

---

## 3. Modeling Strategy

### Model Architectures
1. **Baseline**: L2-regularized Logistic Regression with standardized continuous features and splines for non-linear coordinates.
2. **Nonlinear Benchmark**: Histogram Gradient Boosting Classifier (`HistGradientBoostingClassifier`), capable of learning complex spatial interactions between density and pitch zones.
3. **Interpretable Additive Model**: Generalized Additive Model (GAM) with spline basis functions to isolate non-linear effects of distance and density.

### Evaluation Protocol
- **Grouped Cross-Validation**: To prevent match-level leakage and tactical autocorrelation, validation folds are strictly grouped by `match_id` ($K=5$ GroupKFold).
- **Leave-Competition-Out (LCO)**: To evaluate cross-competition generalization (RQ3), models trained on domestic leagues (e.g. Bundesliga, La Liga, Ligue 1) will be evaluated out-of-sample on international tournaments (World Cup, Euro).
- **Probability Metrics**:
  - ROC-AUC
  - Precision-Recall AUC (PR-AUC)
  - Brier Score
  - Log Loss / Binary Cross-Entropy
  - Calibration curves (Hosmer-Lemeshow / Brier decomposition)
