# Counterpress Episode Definition & Operationalization

This document details the mathematical and computational operationalization of the **Counterpress Episode**, establishing it as the fundamental unit of analysis for our research on soccer counterpressing.

---

## 1. Tactical Motivation: Actions vs. Episodes

In soccer analytics, event logs capture discrete, granular actions performed by individual players. StatsBomb Open Data flags defensive actions occurring within 5 seconds of an open-play turnover with the boolean tag `counterpress: true`.

However, treating every individual counterpress action as an independent observation introduces **severe pseudo-replication and statistical confounding**:
- An initial pressure action by a winger may immediately be followed 1.2 seconds later by a second pressure action from a central midfielder and a tackle attempt by a full-back—all contesting the same possession phase.
- Across our dataset of 424 matches, **38.3% of counterpressing possessions contain multiple chained counterpress actions** (up to 9 actions in a single possession), with an average of **1.555 counterpress actions per sequence**.
- Treating each action as an independent trial falsely inflates sample size and conflates initial spatial triggers with subsequent secondary adjustments.

**Methodological Solution**: We define **one distinct Counterpress Episode per relevant post-turnover opposition possession**.

> [!NOTE]
> **Clustering and Non-Independence**:
> Distinct counterpress episodes are clustered within matches, teams, and competitions and must not be described as statistically independent. Later predictive evaluation will strictly group by `match_id` (e.g., grouped cross-validation), and inferential models may require clustered standard errors or multilevel treatment.

---

## 2. Computational Workflow for Episode Construction

The extraction pipeline in `src/counterpress/turnovers.py` follows a deterministic sequential process:

### Step 1: Deterministic Event Sorting
Events within each match are ordered chronologically by `(period, timestamp, index)`, where `timestamp` is parsed to sub-second precision ($t = \text{hours} \times 3600 + \text{minutes} \times 60 + \text{seconds}$).

### Step 2: Possession Chain Partitioning
Events are grouped by the official StatsBomb `possession` identifier. Every possession chain in StatsBomb belongs to exactly one `possession_team`.

### Step 3: Turnover Identification
A turnover represents a change of possession from Team A (previous possession team) to Team B (new possession team). 
- We prefer StatsBomb's possession transition semantics over fragile, hard-coded lists of event types.
- The turnover event is identified by searching backward from the first counterpress event to determine the exact transition event (e.g. Incomplete Pass, Miscontrol, Dispossessed, Ball Recovery, or initial Pass of the new possession).
- The turnover timestamp ($t_{\text{turnover}}$) marks the start of the post-turnover window.

### Step 4: Detection of Counterpress Actions
Within the resulting Team B possession, all events where `team == Team A` and `counterpress == True` are extracted.
If one or more such actions exist, exactly **ONE counterpress episode** is instantiated.

### Step 5: Episode Initiation
The **chronologically first** valid counterpress action by Team A defines the **Episode Initiation Event** ($e_{\text{init}}$).
- Its timestamp ($t_{\text{init}}$) establishes the baseline for all subsequent outcome evaluations.
- Its location ($\mathbf{x}_{\text{init}}$) and associated 360 freeze frame provide the spatial state at the moment the defending team committed to counterpressing.

### Step 6: Sequence Aggregation
All subsequent `counterpress == True` actions by Team A within that same post-turnover possession are linked as attributes (`num_counterpress_actions`, `all_counterpress_event_ids`) rather than treated as new episodes.

---

## 3. Open-Play Transitions vs. Set-Piece Restarts

StatsBomb flags `play_pattern` on every possession chain.
- **Open-Play Transitions**:
  - `Regular Play`
  - `From Counter`
  - `From Keeper`
- **Set-Piece Restarts**:
  - `From Throw In`
  - `From Corner`
  - `From Free Kick`
  - `From Goal Kick`
  - `From Kick Off`
  - `Other`

### Primary Cohort Rule:
Episodes originating from dead-ball restarts represent distinct tactical situations (defending established set pieces or throw-in structures) and are flagged via `is_open_play: bool`. In our dataset:
- **Open-Play Episodes**: **24,355 episodes** (83.45% of all episodes).
- **Set-Piece Restart Episodes**: **4,831 episodes** (16.55% of all episodes).
Set-piece transitions are preserved in the dataset with `is_open_play = False` to enable sensitivity comparisons but are excluded from primary open-play tactical models.

---

## 4. Episode Schema & Identifiers

Each episode in `results/tables/counterpress_episodes.csv` contains:
- `episode_id` (str): Unique deterministic key (`{match_id}_p{possession_id}_{init_id[:8]}`).
- `match_id` (int): Match identifier.
- `period` (int): Match half / extra time period.
- `possession_id` (int): StatsBomb possession chain index.
- `counterpressing_team` (str): Team attempting the counterpress.
- `possession_team` (str): Opponent team in possession.
- `play_pattern` (str): Play pattern of the possession.
- `is_open_play` (bool): True if open-play turnover; False if set-piece restart.
- `turnover_event_id` / `turnover_event_type` / `turnover_timestamp` / `turnover_seconds` / `turnover_location`.
- `initiation_event_id` / `initiation_event_type` / `initiation_timestamp` / `initiation_seconds` / `initiation_location` / `initiation_player_name`.
- `delay_seconds` (float): Elapsed latency $t_{\text{init}} - t_{\text{turnover}}$ (median = 1.69s).
- `num_counterpress_actions` (int): Count of chained counterpress actions in this episode.
- `has_initiation_360` (bool): True if the initiation event has a usable 360 freeze frame.
- `is_primary_cohort` (bool): True if competition is among the 10 clean 360 competitions (excludes MLS 2023 and AFCON).
