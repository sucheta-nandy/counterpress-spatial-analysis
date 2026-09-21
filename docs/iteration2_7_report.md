# Iteration 2.7 Report: Final Outcome Freeze and Scientific Transition Verification

## Executive Summary

In **Iteration 2.7**, we performed the final audit and outcome-label freeze for the counterpress research project (*"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*).

Following the rigorous audit of Iteration 2.6, we enforced the scientific definition of controlled possession regain: **a regain requires BOTH verified possession-transition evidence AND confirming on-ball controlled play within 5.000 seconds of counterpress initiation (`confirming_control_dt <= 5.000s`)**.

### Key Accomplishments & Methodological Refinements:
1. **Strict Transition Verification**: Eliminated the loophole in v2.6 where standalone pressing-team actions (`Carry`, `Pass`, `Ball Receipt*`, `Shot`, `Dribble`) occurring in the opponent's possession sequence without verified transition evidence were erroneously credited as regains.
2. **Conservative Regain Timing Established**: Clarified that the confirming control timestamp (`controlled_control_time`), rather than the initial acquisition timestamp, serves as the operational `controlled_regain_time`. If an acquisition occurs at $4.8$s but confirming control occurs at $5.2$s, `regain_5s_controlled` is strictly $0$ (while `regain_8s_controlled` is $1$).
3. **Longitudinal Variable Preservation**: Preserved `regain_5s_controlled_v26` and `regain_5s_possession_annotation` alongside the primary frozen variable `regain_5s_controlled` (v2.7), enabling complete longitudinal auditing and transparent reporting of definition refinements.
4. **Cohort Stability**: Primary cohort eligibility ($N = 21,616$) remains strictly fixed. No changes were made to episode extraction or cohort definitions.
5. **Terminology Standardized**: Consistently adopted the phrase *"Outcome Labels Methodologically Refined and Automated Sanity-Checked"*, accurately capturing automated verification without unverified claims of human signoff.

---

## 1. Outcome Label Comparison: v2.6 vs v2.7

Across all **29,186 distinct counterpress episodes** and the **21,616 primary cohort episodes**, the 2x2 comparison between the Iteration 2.6 and Iteration 2.7 definitions reveals:

### 2x2 Contingency Matrix (Full Dataset, N = 29,186)
- **v2.6 Positive (`regain_5s_controlled_v26 = 1`)**: 12,869 (44.09%)
- **v2.7 Positive (`regain_5s_controlled = 1`)**: 11,024 (37.77%)
- **Both Positive ($n_{1,1}$)**: 11,024
- **Both Negative ($n_{0,0}$)**: 16,317
- **v2.6 Positive $\to$ v2.7 Negative ($n_{1,0}$)**: 1,845 (suspect standalone actions or control $> 5.0$s)
- **v2.6 Negative $\to$ v2.7 Positive ($n_{0,1}$)**: 0
- **Overall Agreement**: **93.68%** | **Cohen's Kappa ($\kappa$)**: **0.8698**

### 2x2 Contingency Matrix (Primary Cohort, N = 21,616)
- **v2.6 Positive (`regain_5s_controlled_v26 = 1`)**: 8,485 (39.25%)
- **v2.7 Positive (`regain_5s_controlled = 1`)**: 7,491 (34.65%)
- **Both Positive ($n_{1,1}$)**: 7,491
- **Both Negative ($n_{0,0}$)**: 13,131
- **v2.6 Positive $\to$ v2.7 Negative ($n_{1,0}$)**: 994
- **v2.6 Negative $\to$ v2.7 Positive ($n_{0,1}$)**: 0
- **Overall Agreement**: **95.40%** | **Cohen's Kappa ($\kappa$)**: **0.9015**

---

## 2. Audit of Changed Cases and Direct-Control Episodes

### Root-Cause Breakdown of Changed Cases ($n = 1,845$) :
1. **Standalone Action in Opponent Possession Rejected**: 1,677 episodes (90.9%).
   - In these episodes, a pressing-team player executed an on-ball touch (e.g., `Carry` or `Pass`) during the opponent's possession sequence, but with **no preceding turnover, duel win, interception, or ball recovery**. The opponent retained possession immediately afterward.
   - Under v2.6, these were erroneously labeled as regains. In v2.7, they are correctly rejected.
2. **Confirming Control Exceeded 5.0 Seconds**: 168 episodes (9.1%).
   - In these episodes, an explicit ball acquisition occurred within 5.0s (e.g. at $t = 4.8$s), but confirming control was established at $t > 5.0$s (e.g. at $t = 5.2$s).
   - Under v2.6's acquisition-time rule, these were positive for 5s regain. Under v2.7's conservative control-time rule, they are correctly labeled `regain_5s_controlled = 0` and `regain_8s_controlled = 1`.

---

## 3. Stratified Positive Sample Trace Audit (100 Cases)

We extracted a stratified sample of **100 verified positive counterpress regains** (`results/tables/final_regain_trace_audit.csv` and `results/final_regain_trace_audit.md`):
- **25 Ball Recovery + Control**: Verified ball recovery followed immediately by carry, completed pass, or receipt.
- **20 Duel + Control**: Won duel / tackle followed immediately by pressing-team control.
- **15 Interception + Control**: Interception leading directly to pressing-team carry or pass.
- **20 New Possession + Control**: StatsBomb confirmed possession transition to pressing team with subsequent controlled sequence.
- **20 Other / Opponent Turnover + Control**: Opponent miscontrol or dispossessed event immediately followed by pressing-team control.

> [!NOTE]
> In accordance with research integrity protocols, all human verification checkboxes in `final_regain_trace_audit.md` remain strictly unpopulated (`[ ]`), awaiting formal manual reviewer evaluation.

---

## 4. Final Frozen Primary Cohort Outcome Distributions

With the Iteration 2.7 freeze in place, the outcome labels for the primary cohort ($N = 21,616$) are locked for spatial feature engineering (Iteration 3) and predictive modeling (Iteration 4):

| Variable | Primary Cohort ($N = 21,616$) | Full Dataset ($N = 29,186$) | Description |
| :--- | :---: | :---: | :--- |
| `regain_3s_controlled` | **28.50%** (6,161) | **31.20%** (9,107) | Controlled regain within 3.0s |
| `regain_5s_controlled` (Primary) | **34.65%** (7,491) | **37.77%** (11,024) | Controlled regain within 5.0s |
| `regain_8s_controlled` | **41.07%** (8,878) | **44.24%** (12,912) | Controlled regain within 8.0s |
| `dangerous_escape_15s` (Outcome 2) | **22.41%** (4,844) | **21.45%** (6,261) | Opponent shot / attacking final-third entry within 15s |
| `regain_5s_controlled_v26` (Audit) | 39.25% (8,485) | 44.09% (12,869) | Pre-freeze v2.6 outcome |
| `regain_5s_possession_annotation` (Audit) | 43.49% (9,401) | 50.02% (14,598) | Raw StatsBomb possession tag |

### Final Three-State Tactical Outcome Distribution (Primary Cohort, N = 21,616)
1. **`dangerous_escape`**: **22.41%** (4,844 episodes)
2. **`successful_regain`**: **32.27%** (6,976 episodes)
3. **`harmless_escape`**: **45.32%** (9,796 episodes)

---

## 5. Summary and Readiness for Iteration 3

Outcome labeling is now complete, methodologically refined, and frozen. The codebase enforces strict transition verification and conservative confirming-control timing.
The project is fully prepared for **Iteration 3: Spatial Feature Engineering and Freeze Frame Processing**.