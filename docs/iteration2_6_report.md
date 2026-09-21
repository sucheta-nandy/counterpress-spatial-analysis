# Iteration 2.6 Report: Established-Possession Regain Definition and Human Trace Validation

**Project Title**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Conferences**: MIT Sloan Sports Analytics Conference (SSAC) & Carnegie Mellon Sports Analytics Conference (CMSAC)  
**Date**: September 2026  
**Status**: Iteration 2.6 Complete — Outcome Labels Methodologically Refined and Automated Sanity-Checked  

---

## 1. Executive Summary & Core Results

Iteration 2.6 resolved critical validity problems in possession regain labeling identified during human trace review of the Iteration 2.5 priority sample. Specifically, relying purely on StatsBomb `possession_team` annotations produced both false positives (when opponents continued passing while possession_team remained attributed to the pressing team) and false negatives (when the pressing team recovered and carried the ball, but possession_team was not updated).

We implemented an evidence-based controlled regain detector requiring BOTH:
1. **Possession-transition evidence** (new possession ID or clear opponent turnover).
2. **Controlled-possession evidence** by the pressing team (`Carry`, completed `Pass`, `Ball Recovery` + control, `Duel` + control, `Interception` + control, `Goalkeeper` control, or controlled `Ball Receipt*`).

Standalone defensive events (`Pressure`, `Block`, `Foul Committed`, uncompleted `Clearance`) and opponent actions are strictly prohibited from counting as regains.

### Summary Metrics Across Full Dataset ($N = 29,186$ Distinct Episodes):
- **Old Possession-Annotation Regain Rate**: **50.02%** (14,598 episodes)
- **New Controlled Regain Rate**: **44.09%** (12,869 episodes)
- **Overall Agreement Rate**: **90.27%** (26,347 / 29,186 episodes)
- **Cohen's Kappa ($\kappa$)**: **0.8055**
- **False-Positive Candidates (`Annotation=1, Controlled=0`)**: **2,284** (7.83%)
- **False-Negative Candidates (`Annotation=0, Controlled=1`)**: **555** (1.90%)
- **Total Episodes Changing 3-Class Outcome**: **2,213** (7.58%)

---

## 2. 2x2 Contingency Table: Annotation vs. Controlled Regain

```text
                                Controlled Regain (5s)
                                  0                 1              Total
Annotation (5s)   0           14033               555             14588
                  1            2284             12314             14598
Total                         16317             12869             29186
```

- **Agreement**: 26,347 episodes (90.27%)
- **Cohen's Kappa**: 0.8055

---

## 3. Re-evaluation of Investigated Priority Cases

| Case | Episode ID | Old Regain | New Controlled Regain | New Evidence | Tactical 3-Class Outcome | Status & Empirical Finding |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **Case 9** | `3788766_p107_15ad5bb1` | 1 (dt=0.25s) | **0** (dt=7.33s) | `ball_recovery_plus_carry` (>5s) | `harmless_escape` | **False Positive Resolved**: Italy had only Pressure; Wales continued passing; Italy controlled ball only at 7.33s |
| **Case 18** | `3857276_p12_fcc6b2e3` | 0 (dt=None) | **1** (dt=3.89s) | `ball_recovery_plus_carry` | `successful_regain` | **False Negative Resolved**: Morocco recovered and carried at 3.89s; StatsBomb had un-incremented `possession_team` |
| **Case 37** | `3802805_p92_835a9886` | 1 (dt=4.97s) | **1** (dt=4.97s) | `ball_recovery_plus_carry` | `dangerous_escape` | **Danger Priority & Extended Trace**: Nice recovered ball at 4.97s, but PSG entered final third at dt=0.002s before regain |
| **Case 40** | `3895180_p19_f72281df` | 1 (dt=3.28s) | **1** (dt=3.28s) | `ball_recovery_plus_carry` | `dangerous_escape` | **Extended Trace Visibility**: Leverkusen controlled at 3.28s; Frankfurt entered final third at dt=1.29s before regain |

---

## 4. Revised Three-Class Tactical Outcome Distribution

### Full Dataset ($N = 29,186$):
| Outcome Class | Old Count (Annotation) | Old Pct | New Count (Controlled) | New Pct | Net Change |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`successful_regain`** | 12,801 | 43.86% | 11,420 | 39.13% | -1,381 |
| **`harmless_escape`** | 10,029 | 34.36% | 11,410 | 39.09% | +1,381 |
| **`dangerous_escape`** | 6,356 | 21.78% | 6,356 | 21.78% | +0 |

---

## 5. Primary Modeling Cohort ($N = 21,616$) Outcomes

The primary modeling cohort eligibility criteria established in Iteration 2.5 remain identical (valid turnover link, open play, usable initiation 360, non-MLS clean competitions):

| Metric | Old Annotation Value | New Controlled Value | Absolute Shift |
| :--- | :---: | :---: | :---: |
| **Primary Cohort Episodes ($N$)** | **21,616** | **21,616** | 0 |
| **Regain (5s) Rate** | 43.49% (9,401) | **39.25% (8,485)** | -4.24% |
| **Dangerous Escape (15s) Rate** | 23.92% (5,171) | **23.92% (5,171)** | 0.00% |
| **Successful Regain (3-Class)** | 37.53% | **34.31%** | -3.22% |
| **Harmless Escape (3-Class)** | 38.55% | **41.77%** | +3.22% |
| **Dangerous Escape (3-Class)** | 23.92% | **23.92%** | 0.00% |

---

## 6. Generated Reports & Artifacts
- `results/tables/regain_label_comparison.csv`: Stratified 2x2 comparison across all dimensions.
- `results/regain_disagreement_validation_report.md`: 100 extended chronological traces for disagreement cases.
- `results/tables/manual_validation_priority_v2.csv`: 40 priority review cases with side-by-side labels and strictly unpopulated human columns.
- `results/manual_validation_priority_v2_report.md`: Priority report with full $\ge 8$s visibility and explicit case analyses.
