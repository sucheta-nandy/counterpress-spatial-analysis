# Outcome Definitions & Short-Horizon Evaluation Framework

This document outlines the tactical framework and mathematical definitions for the short-horizon outcomes labeled on each counterpress episode.

---

## 1. Dual-Horizon Tactical Framework

Counterpressing is inherently a dual-objective tactical decision:
1. **Immediate Objective (Regain)**: Win the ball back immediately while the opponent is disorganized ($t \le 5.0\,\text{s}$).
2. **Defensive Risk Objective (Transition Prevention)**: Prevent the opponent from bypassing the press and breaking into open space to create a scoring opportunity ($t \le 15.0\,\text{s}$).

Evaluating counterpress success solely by regains ignores transition vulnerability; evaluating solely by transitions ignores the positive utility of turnovers. We therefore formulate a dual-horizon framework.

---

## 2. Outcome 1: Established Possession Regain (Short Horizon)

In Iteration 2.6 and Iteration 2.7, the regain outcome was methodologically refined from a raw StatsBomb `possession_team` annotation to an **evidence-based controlled regain detector** enforcing strict possession-transition verification.

### Multi-Tier Outcome Variable Schema:
- **Primary Research Variable**: `regain_5s_controlled` (aliased to `regain_5s` for primary downstream modeling): requires BOTH verified possession-transition evidence AND confirming on-ball controlled play within 5.000 seconds of counterpress initiation (`confirming_control_dt <= 5.000s`).
- **Audit Variable (v2.6 Baseline)**: `regain_5s_controlled_v26`: preserved for longitudinal auditing to measure the effect of eliminating unverified standalone actions and enforcing conservative control timing.
- **Legacy Annotation Variable**: `regain_5s_possession_annotation`: raw StatsBomb `possession_team` metadata indicator.

### Mathematical Definition (Iteration 2.7 Frozen):
$$\text{regain\_5s\_controlled} = \begin{cases} 1 & \text{if pressing team verifies possession transition AND confirms control within } t_{\text{ctrl}} \le t_{\text{init}} + 5.000\,\text{s} \\ 0 & \text{otherwise} \end{cases}$$

### Strict Evidence-Based Criteria:
A pressing-team regain requires **BOTH**:
1. **Possession-Transition Evidence**:
   - **Pathway A (Defensive Acquisition)**: Pressing-team explicit ball-winning event: `Ball Recovery`, `Interception`, won `Duel` / `50/50`, or `Goal Keeper` collection / claim.
   - **Pathway B (Opponent Turnover)**: Opponent loss in open play: `Dispossessed`, `Miscontrol`, or incomplete pass (`Incomplete`, `Pass Offside`, `Out`).
   - **Pathway C (New Possession Assignment)**: Transition to a new StatsBomb possession ID assigned to the pressing team (`possession != poss_id` and `possession_team == counterpressing_team`).
2. **Confirming Controlled-Possession Evidence**:
   Must derive from an observable on-ball control action performed by the counterpressing team (`team == counterpressing_team`) within the time horizon:
   - `Carry` traveling under player control.
   - Completed `Pass`.
   - Controlled `Ball Receipt*` (outcome not `Incomplete`).
   - Completed `Dribble` (outcome not `Incomplete`).
   - `Shot`.

### Operational Timing & Conservative Definition:
- **`controlled_acquisition_time`**: Elapsed seconds from initiation to the initial ball acquisition or turnover event ($t_{\text{acq}} - t_{\text{init}}$).
- **`controlled_control_time`**: Elapsed seconds from initiation to the confirming on-ball control event ($t_{\text{ctrl}} - t_{\text{init}}$).
- **`controlled_regain_time`**: Operational regain timestamp, set conservatively to **`controlled_control_time`** ($t_{\text{ctrl}} - t_{\text{init}}$).
- If an acquisition occurs at $t = 4.8$s but confirming control occurs at $t = 5.2$s, `regain_5s_controlled` is strictly **0** (while `regain_8s_controlled` is **1**).

### Standalone Actions Explicitly Prohibited Alone:
The following do **NOT** constitute an established regain:
- Standalone `Carry`, `Pass`, `Ball Receipt*`, `Shot`, or `Dribble` events occurring during the opponent's continuous possession sequence without preceding acquisition or turnover evidence (eliminates 1,677 false positives from v2.6).
- `Pressure` alone (no physical ball contact).
- `Block` alone (deflection; opponent frequently retains possession).
- `Foul Committed` alone (dead ball awarded to opponent).
- `Clearance` alone without retained possession.
- `possession_team` field change with no corresponding controlled action by the pressing team (prevents false positives like Case 9).
- Any event where `team != counterpressing_team`.

### Empirical Regain Rates ($N = 29,186$ Distinct Episodes):
- **Legacy Annotation (`regain_5s_possession_annotation`)**: **50.02%** (14,598 episodes)
- **Iteration 2.6 Controlled Baseline (`regain_5s_controlled_v26`)**: **44.09%** (12,869 episodes)
- **Iteration 2.7 Frozen Controlled (`regain_5s_controlled`)**: **37.77%** (11,024 episodes)
- **Primary Cohort ($N = 21,616$) Frozen Rate**: **34.65%** (7,491 episodes)
- **Sensitivity Horizons (Primary Cohort)**:
  - `regain_3s_controlled`: **28.50%** (6,161 episodes)
  - `regain_5s_controlled`: **34.65%** (7,491 episodes)
  - `regain_8s_controlled`: **41.07%** (8,878 episodes)

---

## 3. Outcome 2: Opponent Dangerous Escape (15-Second Horizon)

### Primary Label: `dangerous_escape_15s`
$$\text{dangerous\_escape\_15s} = \begin{cases} 1 & \text{if opponent creates shot or final-third entry within } t \le t_{\text{init}} + 15.0\,\text{s} \text{ (before controlled regain)} \\ 0 & \text{otherwise} \end{cases}$$

### Trigger Conditions:
1. **Opponent Shot (`shot_15s`)**:
   The opponent in possession takes an event of type `Shot` within 15.0 seconds of counterpress initiation, before any controlled regain by the pressing team.
2. **Opponent Final-Third Penetration (`final_third_entry_15s`)**:
   The opponent advances the ball into its attacking final third ($x \ge 80.0$ in the opponent's attacking coordinate system), **PROVIDED** the episode did not already initiate with the opponent in that attacking final third ($x_{\text{start}} < 80.0$).

### Temporal Precedence:
Opponent transition events are valid **only if they occur before controlled possession is established** (`dt < controlled_regain_time`). Once the pressing team establishes controlled possession, the opponent's transition sequence is terminated.

### Starting in Final Third Exclusion:
If the turnover occurred deep in the defending team's defensive third ($x \le 40$ in defending frame, which translates to $x \ge 80$ in opponent frame), the opponent was ALREADY in its attacking final third at episode start.
- In this scenario, `started_in_final_third = True`.
- Simply retaining the ball at $x \ge 80$ does NOT constitute a "final-third entry".
- The opponent can only trigger `dangerous_escape_15s = 1` by taking a `Shot`.

---

## 4. Three-State Tactical Outcome (`episode_outcome_3class`)

To evaluate the full tactical trade-off, each episode is partitioned into one of three mutually exclusive and exhaustive categories. **Tactical transition danger takes strict priority** over eventual short-horizon recovery:

$$\text{episode\_outcome\_3class} = \begin{cases} 
\text{"dangerous\_escape"} & \text{if } \text{dangerous\_escape\_15s} = 1 \\
\text{"successful\_regain"} & \text{if } \text{dangerous\_escape\_15s} = 0 \land \text{regain\_5s\_controlled} = 1 \\
\text{"harmless\_escape"} & \text{if } \text{dangerous\_escape\_15s} = 0 \land \text{regain\_5s\_controlled} = 0 
\end{cases}$$

### Empirical Breakdown (Primary Cohort, $N = 21,616$ Distinct Episodes):
1. **`dangerous_escape`**: **4,844 episodes (22.41%)**
2. **`successful_regain`**: **6,976 episodes (32.27%)** (Note: 515 episodes had regains preceded by earlier transition danger and are strictly assigned to `dangerous_escape`)
3. **`harmless_escape`**: **9,796 episodes (45.32%)**
- Overlap between classes: **0 episodes** (100% mutually exclusive and exhaustive).
- Auditing counterpart: `episode_outcome_3class_old` is preserved for historical auditing.

---

## 5. Edge Case & Boundary Handling

1. **Period Boundaries**:
   - Episodes occurring near the end of a half cannot cross into the next half ($t_{\text{period}} \to t_{\text{period+1}}$).
   - If the referee blows the half-time or full-time whistle before 5.0s or 15.0s elapse, the episode is evaluated strictly on the observable window prior to the whistle.
2. **Stoppages & Fouls**:
   - Defensive foul by pressing team: Opponent retains possession; regain cannot occur.
   - Offensive foul or turnover by opponent: Pressing team regains possession upon restart.
3. **Simultaneous Timestamps**:
   - Sub-second microsecond ordering (`index`) ensures chronological precedence when multiple events share identical second timestamps.
