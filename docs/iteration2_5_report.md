# Iteration 2.5 Report: Counterpress Episode Validation, Edge-Case Resolution, and Primary Cohort Locking

**Project Title**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Conferences**: MIT Sloan Sports Analytics Conference (SSAC) & Carnegie Mellon Sports Analytics Conference (CMSAC)  
**Date**: September 2026  
**Status**: Iteration 2.5 Complete — Primary Modeling Cohort Locked  

---

## 1. Executive Summary of Methodological Resolutions

Iteration 2.5 resolves all critical methodological issues uncovered following the initial episode extraction in Iteration 2:
1. **Terminology Standardized**: Replaced "statistically independent counterpress episodes" with **"distinct counterpress episodes"**. Added formal notes indicating that predictive evaluation will group by `match_id` and inferential models require clustered/multilevel treatment.
2. **Investigation of Delays > 5.0s**: Audited all **2,376 episodes (8.14%)** with delay > 5.0s. Categorized causes (A through E). Implemented deterministic improvements in `identify_turnover_event()`. Added `turnover_link_quality` (`high`, `ambiguous`, `invalid`) and `latency_valid` flags.
3. **Open-Play vs. Set-Piece Classification**: Audited restart possessions. Formulated and documented `possession_origin_pattern` vs `turnover_context` in `docs/open_play_definition.md`. Established that restart possessions establishing >= 2 passes and lasting >= 5.0s transition to genuine `open_play` turnovers.
4. **Regain / Dangerous Escape Overlap Resolved**: Analyzed all **192 overlap cases**. Revised the tactical 3-class outcome (`episode_outcome_3class`) so that transition danger takes priority over eventual recovery (`dangerous_escape` > `successful_regain` > `harmless_escape`). Verified mutual exclusivity and exhaustiveness.
5. **Priority Manual Validation Sample Created**: Selected **40 priority review cases** across all outcome and delay categories into `results/tables/manual_validation_priority.csv` with human-review fields left strictly unpopulated. Rephrased past claims to "automated sanity-checked".
6. **Primary Modeling Cohort Locked**: Formally locked `primary_cohort_eligible` (**21,616 distinct episodes** across 414 matches) via `results/tables/cohort_flow.csv`.

---

## 2. Initiation Delay (> 5s) Audit Summary

- **Total Episodes Analyzed**: 29,186
- **Episodes with Delay > 5.0s Before Correction**: 2,376 (8.14%)
- **Distribution of Delays > 5.0s**:
  * 5.0 – 6.0s: **748** (31.5%)
  * 6.0 – 8.0s: **1,628** (68.5%)
  * 8.0 – 10.0s: **0** (0.0%)
  * > 10.0s: **0** (0.0%)

### Breakdown by Operational Audit Categories (Algorithmically Classified, Not Proven Causes):
- **Category A (Turnover Detector Linkage)**: 142 episodes
- **Category B (Possession Indexing Delayed)**: 18 episodes
- **Category C (Multiple Contested Events / Duels)**: 325 episodes
- **Category D (Ambiguous Timestamp / Ordering)**: 1,180 episodes
- **Category E (Cannot Link Within 5s - Sustained Buildup)**: 711 episodes

All episodes with delay > 5.0s are flagged with `latency_valid = False` and excluded from the primary cohort. Full chronological traces are published in `results/delay_over_5_validation_report.md`.

---

## 3. Open-Play vs. Restart Classification Audit

- **Total Episodes Originating from Dead-Ball Restarts**: 4,831
- **Episodes Developing into Genuine Open Play** (>= 2 passes, >= 5.0s): 2,917
- **Immediate Restart Phase Turnovers** (cleared corner, intercepted throw-in): 1,069
- **Ambiguous Restart Turnovers**: 845

Full methodology is documented in `docs/open_play_definition.md` and sample traces in `results/tables/restart_context_audit.csv`.

---

## 4. Regain / Dangerous Escape Overlap Resolution

- **Exact Overlapping Episodes**: **192 episodes**
- **Ordering Breakdown**:
  * Final-Third Penetration before Regain: **122**
  * Shot before Regain: **18**
  * Both before Regain: **11**
  * Simultaneous Timestamp Edge Cases: **41**
- **Tactical Priority Rule**: Because tactical danger occurred before recovery, all 192 episodes are classified as `dangerous_escape` in `episode_outcome_3class`.
- **Revised 3-Class Distribution**:
  * `successful_regain`: **14,406** (49.36%)
  * `harmless_escape`: **9,945** (34.07%)
  * `dangerous_escape`: **4,835** (16.57%)

---

## 5. Primary Modeling Cohort Locking

### Cohort Flow Table (`results/tables/cohort_flow.csv`):
|   step_number | filter_stage                                         |   episodes_retained |   episodes_dropped |   retention_pct |
|--------------:|:-----------------------------------------------------|--------------------:|-------------------:|----------------:|
|             1 | Raw Counterpress Actions                             |               45389 |                  0 |          100    |
|             2 | Distinct Counterpress Episodes                       |               29186 |              16203 |           64.3  |
|             3 | Valid Turnover Linkage                               |               26375 |               2811 |           90.37 |
|             4 | Open-Play Turnover Context                           |               24610 |               1765 |           93.31 |
|             5 | Usable Initiation 360 Freeze Frame                   |               21782 |               2828 |           88.51 |
|             6 | Competition Exclusions (MLS 2023 Sensitivity Cohort) |               21616 |                166 |           99.24 |
|             7 | Final Locked Primary Modeling Cohort                 |               21616 |                  0 |           74.06 |

### Primary Cohort Characteristics ($N = 21,616$):
- **Matches**: 414 across 7 clean competition-seasons
- **Unique Teams**: 147
- **Regain (5s) Rate**: 43.49% (vs 68.65% in excluded; Cohen's d = -0.524)
- **Dangerous Escape (15s) Rate**: 19.02% (vs 9.55% in excluded; Cohen's d = 0.273)
- **Median Initiation Delay**: 1.463 seconds
- **Mean Initiation Pitch Coordinates**: (x = 67.1 +/- 26.99, y = 40.41 +/- 22.45) StatsBomb coordinate units

> [!NOTE]
> **Representativeness Statement**:
> The locked primary modeling cohort represents high-quality, observable counterpress situations from selected elite European leagues and major international tournaments. We do **not** claim this sample is representative of all professional soccer worldwide.

---

## 6. Manual Review Priority

A priority validation subset of **40 unique episodes** is generated in `results/tables/manual_validation_priority.csv` with accompanying traces in `results/manual_validation_priority_report.md`. All human review fields remain unpopulated pending human judgment.
