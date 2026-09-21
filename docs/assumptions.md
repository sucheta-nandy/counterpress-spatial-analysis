# Operational Definitions & Methodological Assumptions

This document records the exact operational definitions, mathematical assumptions, coordinate conventions, and exclusions governing our research on soccer counterpressing.

---

## 1. Counterpressing Operational Definition: Actions vs. Episodes

### StatsBomb Action-Level Specification
StatsBomb defines a counterpressing action via the boolean flag `counterpress: true`.
Authoritative definition:
> *"A pressing action occurring within 5 seconds of an open play turnover."*

In the StatsBomb Open Data schema, `counterpress: true` is predominantly attached to:
- `Pressure`: A player actively reducing time/space on the opponent on the ball.
- `Foul Committed`: A defensive foul committed during an immediate pressing attempt.
- `Duel` (Tackle / Aerial): An immediate physical contest for the ball.
- `Interception`: An attempt to intercept an immediate outlet pass.
- `Block`: An immediate block of a pass or clearance.
- `Dribbled Past`: A pressing player bypassed by the ball carrier.

### Unit of Analysis: Distinct Counterpress Episodes
Multiple counterpress-tagged defensive actions may occur during the same post-turnover opposition possession. **These action-level events must NOT be treated as distinct counterpress attempts.**

> [!NOTE]
> **Clustering and Non-Independence**:
> Counterpress episodes are clustered within matches, teams, and competitions and must **not** be described as statistically independent. Later predictive evaluation will strictly group by `match_id` (e.g., grouped cross-validation), and inferential models may require clustered standard errors or multilevel treatment.

We define **ONE distinct counterpress episode per relevant post-turnover possession**:
1. When Team A loses possession to Team B in open play, inspect the resulting Team B possession.
2. If Team A executes one or more `counterpress: true` actions belonging to the post-turnover window, define exactly **one counterpress episode**.
3. **Episode Initiation**: The *chronologically first* valid counterpress action by Team A defines the episode initiation event ($e_{\text{init}}$).
4. All subsequent counterpress actions by Team A within that same post-turnover sequence are associated with this episode rather than treated as new attempts.

---

## 2. Outcome Definitions

### Outcome 1: Controlled Possession Regain within 5 Seconds (Primary)
- **Definition**: The counterpressing team establishes controlled possession within **5.0 seconds** after counterpress initiation.
- **Operational Implementation (Iteration 2.7 Frozen)**:
  - Requires **BOTH** verified possession-transition evidence (defensive acquisition, opponent turnover, or new possession assignment) and confirming controlled-possession evidence by the pressing team (`Carry`, completed `Pass`, controlled `Ball Receipt*`, completed `Dribble`, `Shot`).
  - **Conservative Control Timing**: The operational regain time (`controlled_regain_time`) is defined by the confirming control timestamp ($t_{\text{ctrl}} - t_{\text{init}}$). Both transition and confirming control must occur within $0.000 \le t \le 5.000$s. If acquisition occurs at $4.8$s but control at $5.2$s, `regain_5s_controlled = 0` and `regain_8s_controlled = 1`.
  - Standalone pressing-team actions occurring within the opponent's possession sequence without verified transition evidence are strictly rejected.
  - Multi-tier auditing variables are preserved: `regain_5s_controlled_v26` (Iteration 2.6 baseline) and `regain_5s_possession_annotation` (StatsBomb annotation).
- **Sensitivity Horizons**: `regain_3s_controlled` (3.0 seconds) and `regain_8s_controlled` (8.0 seconds).
- **Target**: $Y_{\text{regain\_5s\_controlled}} \in \{0, 1\}$.

### Outcome 2: Opponent Dangerous Escape within 15 Seconds
- **Definition**: Prior to the counterpressing team establishing controlled possession, and within **15.0 seconds** of counterpress initiation, the opponent creates a dangerous transition.
- **Operational Criteria**:
  1. **Shot**: The opponent registers a `Shot` event within $t \le t_{\text{init}} + 15.0\,\text{s}$ before controlled regain.
  2. **Final-Third Penetration**: The opponent advances the ball into its attacking final third ($x \ge 80.0$ in the opponent's attacking coordinate frame), **PROVIDED** the episode did not already initiate with the opponent in that attacking final third ($x_{\text{start}} < 80.0$).
- **Supporting Continuous Variables**: `opponent_max_progression_15s`, `time_to_shot`, `time_to_final_third_entry`.
- **Target**: $Y_{\text{dangerous\_escape\_15s}} \in \{0, 1\}$.

### Three-State Tactical Outcome (`episode_outcome_3class`)
To capture the full tactical trade-off, each episode is categorized into one of three mutually exclusive and exhaustive states, prioritizing transition danger:
1. `dangerous_escape`: $Y_{\text{dangerous\_escape\_15s}} = 1$.
2. `successful_regain`: $Y_{\text{dangerous\_escape\_15s}} = 0 \land Y_{\text{regain\_5s\_controlled}} = 1$.
3. `harmless_escape`: $Y_{\text{dangerous\_escape\_15s}} = 0 \land Y_{\text{regain\_5s\_controlled}} = 0$.

---

## 3. Coordinate System Conventions & Inversions

### StatsBomb Pitch System
- Dimensions: $120 \times 80$ StatsBomb coordinate units.
- Origin $(0, 0)$ is the top-left corner.
- Attacking direction: In StatsBomb event logs, the acting team always attacks left-to-right (toward $x = 120$). Defending goal is at $(0, 40)$, attacking goal is at $(120, 40)$.

### 360 Freeze-Frame Perspective
- A 360 freeze frame is linked to an event via `event_uuid`.
- Coordinate Alignment: The freeze-frame player coordinates are recorded in the coordinate frame of the **event's acting team**.
- For a counterpress event executed by Team A:
  - Team A's goal is at $x = 0$.
  - Opponent's goal is at $x = 120$.
  - `teammate: true` denotes Team A players (counterpressers).
  - `teammate: false` denotes Team B players (opponent in possession).
  - `actor: true` denotes the individual executing the counterpress action.

### Cross-Event Coordinate Inversion
When comparing an event by Team B (the opponent in possession) with an event by Team A (the counterpressing team):
$$\begin{aligned}
x_A &= 120.0 - x_B \\
y_A &= 80.0 - y_B
\end{aligned}$$
For opponent on-ball progression, evaluating against $x \ge 80.0$ in Team B's own attacking coordinates directly identifies penetration into Team B's attacking final third.

---

## 4. Partial Visibility & Observational Missingness

### StatsBomb 360 Constraints
StatsBomb 360 tracking is derived from broadcast footage and represents **event-level freeze frames of visible players**, not continuous optical tracking of all 22 players.

### Observational Missingness Controls
1. **Visible Area ($A_{\text{vis}}$)**: Area in square coordinate units of the `visible_area` polygon.
2. **Total Visible Players ($N_{\text{vis}}$)**: Total players captured in the frame.
3. **Investigation of Missingness**: We test whether 360 availability is associated with observable event and match characteristics (e.g. pitch coordinates, period, minute, event type). Missing-at-random (MAR) assumptions cannot be proven from observational data alone.

---

## 5. Exclusions & Data Sanitation Rules

1. **Set-Piece Restart Exclusions**: Transitions originating from dead-ball restarts (Goal Kick, Throw In, Corner, Free Kick, Kick Off, Penalty) are excluded from the primary open-play counterpress episode cohort.
2. **Period Boundary Handling**: Episodes cannot cross period boundaries. If a half ends before the outcome horizon (5s or 15s) expires without a regain or transition event, the outcome is evaluated strictly on the observable window prior to the final whistle.
3. **Cohort Eligibility**:
   - Primary modeling cohort includes the 10 clean 360 competition-seasons.
   - AFCON 2023 is excluded due to missing upstream 360 files.
   - UEFA Women's Euro 2022 excludes corrupted match `3845506` (preserving the other 30 matches).
   - MLS 2023 is excluded from primary models due to lower 360 event-level coverage and preserved for sensitivity analysis.
4. **Grouped Cross-Validation**: All model validation must strictly group by `match_id` (GroupKFold) to prevent within-match tactical autocorrelation and data leakage.
