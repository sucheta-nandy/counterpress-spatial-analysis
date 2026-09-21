# Iteration 5: Conference Abstract, Manuscript Story, and Reproducibility Package

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Competition**: MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition  
**Contingency Venue**: Carnegie Mellon Sports Analytics Conference (CMSAC)  
**Status**: **COMPLETE & FULLY VERIFIED** (All 95 unit tests passing)

---

## 1. Executive Summary

Iteration 5 completes the formal conference abstract drafting, title selection, figure evaluation, manuscript architecture, poster storyboard, and open-source repository audit.
- All analytical components from Iterations 1–4.6 remain **permanently frozen**.
- Every quantitative claim originates strictly from [`results/tables/canonical_conference_claims.csv`](../results/tables/canonical_conference_claims.csv) and [`results/tables/canonical_model_specifications.csv`](../results/tables/canonical_model_specifications.csv).
- Automated tests in [`tests/test_abstract_claims.py`](../tests/test_abstract_claims.py) and [`tests/test_claim_consistency.py`](../tests/test_claim_consistency.py) enforce word count limits, exact numeric matches, and terminology constraints.

---

## 2. Title Options and Recommendation

Five title options were formulated across distinct conceptual angles:
1. **Option 1 (Original Working Title)**:  
   *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*
2. **Option 2 (Spatial Geometry Focus)**:  
   *"The Geometry of the Counterpress: Spatial Predictors of Immediate Regain and Transition Danger in Elite Soccer"*
3. **Option 3 (Risk-Reward Dilemma Focus)**:  
   *"Regain or Be Exposed: Modeling Counterpress Success and Transition Risk from 360 Freeze-Frame Geometry"*
4. **Option 4 (Turnover Temporal Focus)**:  
   *"Spatial Structure at Turnover Initiation: Predicting Possession Regain and Transition Danger in Professional Soccer"*
5. **Option 5 (Defensive Exposure Focus)**:  
   *"When Pressure Fails: Spatial Predictors of Possession Regain and Defensive Exposure in Elite Soccer Counterpressing"*

### Recommendation: Option 1
* **Selected Title**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*
* **Rationale**: It directly poses the practical tactical question, establishes the dual-outcome nature of the problem (regain vs. transition risk), avoids sensationalism, and has served as the stable anchor across all project documentation.

---

## 3. Abstract Versions and Word Counts

Both MIT abstracts strictly conform to the five required sections: `TITLE`, `INTRODUCTION`, `METHODS`, `RESULTS`, `CONCLUSION`.

| Abstract Document | Target Word Count | Exact Word Count (with Title) | Primary Focus | Recommendation |
| :--- | :---: | :---: | :--- | :---: |
| **[`docs/ssac27_abstract_version_a.md`](ssac27_abstract_version_a.md)** | 420–450 | **437 words** | Academic, methodological, and statistical rigor | **RECOMMENDED** |
| **[`docs/ssac27_abstract_version_b.md`](ssac27_abstract_version_b.md)** | 420–450 | **439 words** | Tactical decision-making and club analyst utility | Alternative |
| **[`docs/cmsac_poster_abstract_contingency.md`](cmsac_poster_abstract_contingency.md)** | 250–300 | **247 words** (body) / **293 words** (total) | Concise poster summary (Status: Submissions Closed) | Contingency |

### Recommendation Between Versions A and B
* **Version A is recommended** for the official SSAC27 submission because the MIT Sloan research paper competition review panel heavily weights statistical and methodological clarity (match-clustered validation, paired bootstrap inference, FDR corrections, and camera-coverage sensitivity).

---

## 4. Abstract Figure Decision & Strategy

* **Rule**: SSAC permits up to two figures/tables in the abstract submission.
* **Evaluation**: A text-only abstract (Option A) forces reviewers to track two independent spatial mechanisms (regain proximity vs. danger depth) purely from prose. A compact two-panel display (Option B) demonstrates the dual-outcome thesis instantaneously.
* **Recommendation**: **Option B (One compact two-panel figure)**:
  - **Panel A (Regain Proximity)**: Observed 5-second regain rate decaying by nearest-teammate distance quintile (54.31% in Q1 down to 24.44% in Q5) and local numerical advantage (+1 surplus: 56.85% vs. -1 deficit: 31.54%).
  - **Panel B (Transition Danger)**: Observed transition danger escalating by pitch third (Attacking: 11.28%, Middle: 27.41%, Defensive: 31.57%) and lateral zone (Touchline: 16.86% vs. Central: 25.15%).

---

## 5. Summary of Prioritized Quantitative Claims

Every quantitative claim in the abstract matches canonical result tables:
1. **Sample Scale**: 21,616 distinct counterpress episodes, 414 matches, seven competitions.
2. **Outcome Baseline**: 34.65% 5-second controlled regain; 22.41% 15-second dangerous transition.
3. **Incremental Value of 360 Geometry**: Model 1 Context ROC-AUC = 0.7926 vs. Model 3 Full Spatial Logistic ROC-AUC = 0.8156 ($\Delta \text{ROC-AUC} = \mathbf{+0.0230}$, $\Delta \text{PR-AUC} = \mathbf{+0.0377}$, paired bootstrap 95% CI $[\mathbf{+0.0181, +0.0278}]$).
4. **Immediate Teammate Proximity**: $\mathbf{\text{OR} = 0.800}$ [95% CI: $0.729, 0.878$] per 1 SD (8.2 StatsBomb coordinate units). Shorter distance corresponds to **+25.0% higher regain odds**.
5. **Broader Numerical Overload**: 10-unit $\mathbf{\text{OR} = 1.071}$ [95% CI: $1.014, 1.130$]; 15-unit $\mathbf{\text{OR} = 1.144}$ [95% CI: $1.085, 1.207$]; immediate 5-unit surplus non-significant ($\text{OR} = 1.022, p = 0.3285$) after conditioning on broader rings.
6. **Pitch-Third Danger Dominance**: Defensive third = **31.57%** vs. Attacking third = **11.28%** ($\mathbf{\text{OR} = 0.379}$ [95% CI: $0.359, 0.399$]).
7. **Centrality Danger Escalation**: Touchline = **16.86%** vs. Central = **25.15%** ($\mathbf{\text{OR} = 1.219}$ [95% CI: $1.174, 1.266$]).
8. **Danger Non-Linear Gain**: HistGradientBoosting achieves superior probability ranking over spatial logistic ($\mathbf{\Delta \text{PR-AUC} = +0.0394}$ [95% CI: $\mathbf{+0.0299, +0.0490}$]), driven by threshold non-linearities at defensive-third boundaries.

---

## 6. Deliverable Artifacts Directory

| Artifact Document | Purpose |
| :--- | :--- |
| [`docs/ssac27_abstract_version_a.md`](ssac27_abstract_version_a.md) | Official SSAC27 abstract draft (437 words, methodological focus) |
| [`docs/ssac27_abstract_version_b.md`](ssac27_abstract_version_b.md) | Alternative SSAC27 abstract draft (439 words, practitioner focus) |
| [`docs/cmsac_poster_abstract_contingency.md`](cmsac_poster_abstract_contingency.md) | Contingency CMSAC poster draft (247 body words / 293 total) |
| [`docs/manuscript_outline.md`](manuscript_outline.md) | Complete 12-section full paper architecture |
| [`docs/related_work_todo.md`](related_work_todo.md) | Literature checklist of external citations requiring verification |
| [`docs/poster_storyboard.md`](poster_storyboard.md) | 6-block visual poster storyboard with 5 recommended figures |
| [`docs/ssac_repository_checklist.md`](ssac_repository_checklist.md) | Open-source public repository audit and checklist |
| [`tests/test_abstract_claims.py`](../tests/test_abstract_claims.py) | Automated abstract claim validation and word count test suite |

---

## 7. Verification Test Suite Status

```bash
$ ./.venv/bin/pytest tests/ -v
============================== 95 passed in 3.30s ==============================
```
- `tests/test_abstract_claims.py`: 11 passed (word counts, numbers, terminology).
- `tests/test_claim_consistency.py`: 9 passed (canonical deltas, recomputed rates, invariants).
- Entire codebase: 95 automated unit tests passing.
