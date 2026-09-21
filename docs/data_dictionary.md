# Data Dictionary

This document details the variables, data types, and definitions across the raw, interim, and processed data layers of the counterpressing research repository.

---

## 1. Raw Data Layers (StatsBomb)

### Competition Metadata (`competitions.json`)
- `competition_id` (int): Unique identifier for competition.
- `season_id` (int): Unique identifier for season.
- `competition_name` (str): Name of competition (e.g. "FIFA World Cup", "1. Bundesliga").
- `season_name` (str): Name of season (e.g. "2022", "2023/2024").
- `competition_gender` (str): "male" or "female".
- `match_available_360` (str/null): ISO timestamp indicating when 360 data became available.

### Match Metadata (`matches/{competition_id}/{season_id}.json`)
- `match_id` (int): Unique match identifier.
- `match_date` (str): Match date (YYYY-MM-DD).
- `home_team` (dict): `home_team_id`, `home_team_name`.
- `away_team` (dict): `away_team_id`, `away_team_name`.
- `home_score` / `away_score` (int): Final full-time score.
- `match_status_360` (str): Status of 360 frames ("available" or null).

### Event Log (`events/{match_id}.json`)
- `id` (str): UUID for the event.
- `index` (int): Sequential index of the event within the match.
- `period` (int): Match period (1 = 1st half, 2 = 2nd half, 3/4 = extra time, 5 = penalty shootout).
- `timestamp` (str): Elapsed time in period (HH:MM:SS.mmm).
- `minute` (int) / `second` (int): Elapsed clock time.
- `type` (dict): Event type `id` and `name` (e.g. "Pressure", "Pass", "Ball Recovery", "Duel").
- `possession` (int): Sequential possession chain identifier.
- `possession_team` (dict): Team in possession for this chain.
- `team` (dict): Team executing the current event.
- `player` (dict): Player executing the event.
- `location` (list of float): Coordinates `[x, y]` in StatsBomb coordinate units ($x \in [0, 120], y \in [0, 80]$).
- `counterpress` (bool): Flag indicating event is a counterpress action (within 5s of turnover).

### 360 Freeze Frames (`three-sixty/{match_id}.json`)
- `event_uuid` (str): UUID matching the event in `events/{match_id}.json`.
- `visible_area` (list of float): Polygon vertices $[x_0, y_0, x_1, y_1, \dots, x_k, y_k]$ defining the camera viewport.
- `freeze_frame` (list of dict): Detected visible players, each containing:
  - `teammate` (bool): True if on the same team as the event's actor; False if opponent.
  - `actor` (bool): True if this player performed the event.
  - `keeper` (bool): True if player is goalkeeper.
  - `location` (list of float): `[x, y]` coordinates projected onto event team's attacking frame.

---

## 2. Counterpress Episode Dataset Schema (`counterpress_episodes.csv`)

| Column Name | Type | Description |
| :--- | :---: | :--- |
| `episode_id` | str | Unique deterministic key (`{match_id}_p{possession}_{init_id[:8]}`). |
| `match_id` | int | StatsBomb match identifier. |
| `competition_name` | str | Competition name. |
| `season_name` | str | Season name. |
| `period` | int | Match period (1, 2, 3, etc.). |
| `possession_id` | int | StatsBomb possession chain index. |
| `counterpressing_team` | str | Name of defending team attempting the counterpress. |
| `counterpressing_team_id` | int | Team ID of counterpressing team. |
| `possession_team` | str | Name of opponent team in possession. |
| `possession_team_id` | int | Team ID of opponent team. |
| `play_pattern` | str | Starting play pattern of the possession. |
| `possession_origin_pattern` | str | Raw starting play pattern of the possession (`play_pattern`). |
| `turnover_context` | str | Tactical context of turnover: `open_play`, `immediate_restart_phase`, or `ambiguous`. |
| `is_open_play` | bool | True if turnover occurred in open play (`turnover_context == "open_play"`). |
| `turnover_event_id` | str | UUID of event marking the turnover. |
| `turnover_event_type` | str | Event type of turnover. |
| `turnover_timestamp` | str | Timestamp of turnover (HH:MM:SS.mmm). |
| `turnover_seconds` | float | Elapsed seconds into the period of turnover. |
| `turnover_location` | list | Coordinates `[x, y]` of turnover event. |
| `turnover_link_quality` | str | Quality of turnover-counterpress linkage: `high`, `ambiguous`, `invalid`. |
| `initiation_event_id` | str | UUID of the chronologically first counterpress action. |
| `initiation_event_type` | str | Type of initiation action (`Pressure`, `Duel`, `Block`, etc.). |
| `initiation_timestamp` | str | Timestamp of initiation action. |
| `initiation_seconds` | float | Elapsed seconds into the period of initiation action. |
| `initiation_location` | list | Coordinates `[x, y]` of pressing actor (in pressing team's frame). |
| `initiation_player_id` | int | Player ID of pressing actor. |
| `initiation_player_name` | str | Player name of pressing actor. |
| `delay_seconds` | float | Latency $t_{\text{init}} - t_{\text{turnover}}$ in seconds. |
| `latency_valid` | bool | True if $0 \le \text{delay\_seconds} \le 5.0$ and `turnover_link_quality == "high"`. |
| `num_counterpress_actions` | int | Total count of chained counterpress actions in this episode. |
| `all_counterpress_event_ids` | list | List of all counterpress action UUIDs in this episode. |
| `has_initiation_360` | bool | True if initiation event has a usable 360 freeze frame. |
| `is_primary_cohort` | bool | Sensitivity flag: True if competition is not Major League Soccer 2023. |
| `opponent_team_at_turnover` | str | Explicit name of opponent team at turnover. |
| `possession_team_at_counterpress_initiation` | str | Exact StatsBomb `possession_team` annotated at initiation event. |
| `possession_id_at_counterpress_initiation` | int | Exact possession ID at counterpress initiation event. |
| `regain_5s_controlled` | int | Primary outcome (v2.7 frozen): 1 if pressing team verified transition AND confirmed control within 5.0s, else 0. |
| `regain_3s_controlled` | int | Sensitivity outcome: 1 if verified transition and confirmed control within 3.0s, else 0. |
| `regain_8s_controlled` | int | Sensitivity outcome: 1 if verified transition and confirmed control within 8.0s, else 0. |
| `controlled_acquisition_time` | float | Elapsed seconds from initiation to initial ball acquisition or turnover ($t_{\text{acq}} - t_{\text{init}}$). |
| `controlled_control_time` | float | Elapsed seconds from initiation to confirming on-ball control ($t_{\text{ctrl}} - t_{\text{init}}$). |
| `controlled_regain_time` | float | Elapsed seconds to established controlled regain ($= t_{\text{ctrl}} - t_{\text{init}}$, conservative definition). |
| `controlled_regain_event_id` | str | UUID of the confirming controlled regain event (or null). |
| `controlled_regain_event_type` | str | Event type of the confirming controlled regain action (e.g. `Carry`, `Pass`). |
| `controlled_regain_evidence` | str | Operational evidence classification string (e.g. `ball_recovery_plus_carry`, `duel_plus_pass`). |
| `regain_5s` | int | Standard research variable (aliased to `regain_5s_controlled` for downstream analysis). |
| `regain_3s` | int | Standard research variable (aliased to `regain_3s_controlled`). |
| `regain_8s` | int | Standard research variable (aliased to `regain_8s_controlled`). |
| `seconds_to_regain` | float | Elapsed seconds to established controlled possession regain (or null). |
| `regain_event_id` | str | UUID of the established controlled regain event. |
| `regain_5s_controlled_v26` | int | Longitudinal audit variable: 1 if episode met Iteration 2.6 definition, else 0. |
| `regain_5s_possession_annotation` | int | Auditing variable: 1 if StatsBomb `possession_team` transitioned to pressing team within 5.0s, else 0. |
| `regain_3s_possession_annotation` | int | Auditing variable: 1 if StatsBomb `possession_team` transitioned within 3.0s, else 0. |
| `regain_8s_possession_annotation` | int | Auditing variable: 1 if StatsBomb `possession_team` transitioned within 8.0s, else 0. |
| `seconds_to_regain_annotation` | float | Elapsed seconds to StatsBomb possession_team transition (or null). |
| `regain_event_id_annotation` | str | UUID of event where StatsBomb possession_team transitioned. |
| `dangerous_escape_15s` | int | Primary risk outcome: 1 if opponent shot or entered final third within 15s before controlled regain. |
| `shot_15s` | int | 1 if opponent took a shot within 15s before controlled regain, else 0. |
| `final_third_entry_15s` | int | 1 if opponent entered attacking final third within 15s before controlled regain, else 0. |
| `started_in_final_third` | bool | True if opponent was already in attacking final third at episode start. |
| `opponent_initial_x` | float | Initial x-coordinate of opponent in opponent attacking frame. |
| `opponent_max_progression_15s` | float | Maximum x-coordinate reached by opponent within 15s before controlled regain. |
| `time_to_shot` | float | Elapsed seconds from initiation to opponent shot (or null). |
| `time_to_final_third_entry` | float | Elapsed seconds from initiation to final third entry (or null). |
| `episode_outcome_3class` | str | Primary three-state tactical outcome: `dangerous_escape`, `successful_regain`, `harmless_escape` (danger prioritized, using controlled regain). |
| `episode_outcome_3class_old` | str | Auditing three-state tactical outcome using legacy annotation regain. |

---

## 3. Spatial Feature Matrix Schema (`counterpress_features.parquet`)

Dataset: Primary Cohort ($N = 21,616$ distinct episodes across 414 matches).

| Column Name | Type | Unit / Range | Description |
| :--- | :---: | :---: | :--- |
| **Cohort Identifiers** | | | |
| `episode_id` | str | Deterministic key | Match-possession-UUID identifier (`results/tables/primary_cohort_episode_ids.csv`). |
| `match_id` | int | Integer | StatsBomb match identifier. |
| `competition` | str | String | Competition name. |
| `season` | str | String | Season name. |
| `counterpressing_team` | str | String | Name of counterpressing squad. |
| `opponent_team` | str | String | Name of opponent squad possessing the ball. |
| `initiation_event_id` | str | UUID | UUID of first counterpress action (links to 360 freeze frame). |
| **Reference Location & Actor QA** | | | |
| `initiation_x` | float | $[0.0, 120.0]$ | Reference initiation location x-coordinate (pressing team attacking frame). |
| `initiation_y` | float | $[0.0, 80.0]$ | Reference initiation location y-coordinate. |
| `actor_present` | bool | {True, False} | True if freeze frame explicitly flagged player with `actor == True`. |
| `actor_distance_from_event` | float | $\ge 0.0$ | Euclidean distance between 360 actor position and $(x_0, y_0)$ (NaN if no actor). |
| `actor_matching_anomalous` | bool | {True, False} | True if distance > 1.0 or actor flag missing. |
| **Raw Frame & Visibility** | | | |
| `frame_player_count` | int | $[0, 22]$ | Total players detected in freeze frame. |
| `visible_teammate_count_including_actor` | int | $[0, 11]$ | All players with `teammate == True`. |
| `visible_teammate_count_excluding_actor` | int | $[0, 10]$ | Teammates with actor strictly excluded. |
| `visible_opponent_count` | int | $[0, 11]$ | Players with `teammate == False`. |
| `visible_goalkeeper_count` | int | $[0, 2]$ | Players with `keeper == True`. |
| `visible_area_polygon_area` | float | $[0.0, 9600.0]$ | Area of camera visible polygon clipped to $120 \times 80$ pitch. |
| `visible_area_pitch_fraction` | float | $[0.0, 1.0]$ | Ratio of visible polygon area to total pitch area ($9600.0$). |
| `polygon_valid` | bool | {True, False} | True if visible area polygon is non-empty, valid, and on pitch. |
| `polygon_missing` | bool | {True, False} | True if 360 visible area polygon is missing or malformed. |
| **Camera-Coverage Features** | | | |
| `coverage_5`, `10`, `15` | float | $[0.0, 1.0]$ | Area(Visible $\cap$ Pitch $\cap$ Circle_r) / Area(Pitch $\cap$ Circle_r). |
| `visible_local_area_5`, `10`, `15` | float | $\ge 0.0$ | Square coordinate units of visible area inside local on-pitch circle. |
| `coverage_5_ge_80pct`, `10`, `15` | bool | {True, False} | Sensitivity flag: True if local circle coverage $\ge 80\%$. |
| **Local Team Support (Actor Excluded)** | | | |
| `visible_teammates_within_5`, `10`, `15` | int | $\ge 0$ | Count of visible teammates within radius (actor strictly excluded). |
| `nearest_teammate_distance` | float | $\ge 0.0$ | Euclidean distance to nearest other teammate (NaN if count < 1). |
| `second_nearest_teammate_distance` | float | $\ge 0.0$ | Distance to 2nd nearest other teammate (NaN if count < 2). |
| `third_nearest_teammate_distance` | float | $\ge 0.0$ | Distance to 3rd nearest other teammate (NaN if count < 3). |
| **Local Opposition** | | | |
| `visible_opponents_within_5`, `10`, `15` | int | $\ge 0$ | Count of visible opponents within radius. |
| `nearest_opponent_distance` | float | $\ge 0.0$ | Distance to 1st nearest opponent (NaN if count < 1). |
| `second_nearest_opponent_distance` | float | $\ge 0.0$ | Distance to 2nd nearest opponent (NaN if count < 2). |
| `third_nearest_opponent_distance` | float | $\ge 0.0$ | Distance to 3rd nearest opponent (NaN if count < 3). |
| **Local Numerical Structure** | | | |
| `numerical_advantage_5`, `10`, `15` | int | Integer | Supporting teammates minus opponents within radius. |
| `total_players_within_5`, `10`, `15` | int | $\ge 0$ | Total players within radius (supporting teammates + opponents + actor). |
| **Visibility-Aware Local Density** | | | |
| `teammate_density_visible_5`, `10`, `15` | float | $\ge 0.0$ | Teammates per visible local area unit (NaN if local visible area $\le 10^{-4}$). |
| `opponent_density_visible_5`, `10`, `15` | float | $\ge 0.0$ | Opponents per visible local area unit (NaN if local visible area $\le 10^{-4}$). |
| **Visible Team Compactness** | | | |
| `teammate_x_std`, `y_std` | float | $\ge 0.0$ | Standard deviation ($\text{ddof}=0$) of teammate coordinates (NaN if count < 2). |
| `opponent_x_std`, `y_std` | float | $\ge 0.0$ | Standard deviation ($\text{ddof}=0$) of opponent coordinates (NaN if count < 2). |
| `teammate_mean_pairwise_distance` | float | $\ge 0.0$ | Mean Euclidean distance across teammate pairs (NaN if count < 2). |
| `opponent_mean_pairwise_distance` | float | $\ge 0.0$ | Mean Euclidean distance across opponent pairs (NaN if count < 2). |
| `teammate_hull_area` | float | $\ge 0.0$ | 2D convex hull area for teammates (NaN if count < 3 or collinear). |
| `opponent_hull_area` | float | $\ge 0.0$ | 2D convex hull area for opponents (NaN if count < 3 or collinear). |
| `teammate_hull_visible_area_ratio` | float | $\ge 0.0$ | Ratio of teammate hull area to visible polygon area (NaN if hull NaN). |
| `opponent_hull_visible_area_ratio` | float | $\ge 0.0$ | Ratio of opponent hull area to visible polygon area (NaN if hull NaN). |
| **Pitch Geometry Features** | | | |
| `distance_to_nearest_touchline` | float | $[0.0, 40.0]$ | $\min(y_0, 80 - y_0)$. |
| `distance_to_own_goal_line` | float | $[0.0, 120.0]$ | $x_0$. |
| `distance_to_opponent_goal_line` | float | $[0.0, 120.0]$ | $120.0 - x_0$. |
| `lateral_centrality` | float | $[0.0, 1.0]$ | $1.0 - |y_0 - 40.0| / 40.0$ (1.0 = center, 0.0 = touchline). |
| `pitch_zone` | str | Categorical | `defensive_third` ($x < 40$), `middle_third` ($40 \le x < 80$), `attacking_third` ($x \ge 80$). |
| `pitch_zone_3x3` | str | Categorical | Pitch third crossed with lateral lane (`left`, `center`, `right`). |
| **Forward Escape Structure (Opponent Frame)** | | | |
| `opponents_ahead_of_ball` | int | $\ge 0$ | Escaping players with $x_{\text{opp}} > x_{0, \text{opp}}$ in transition direction. |
| `defenders_ahead_of_ball` | int | $\ge 0$ | Pressing players with $x_{\text{opp}} > x_{0, \text{opp}}$ (actor excluded). |
| `forward_numerical_advantage` | int | Integer | Opponents ahead minus defenders ahead. |
| `nearest_defender_ahead_distance` | float | $\ge 0.0$ | Distance to nearest defending player ahead (NaN if none). |
| `nearest_opponent_ahead_distance` | float | $\ge 0.0$ | Distance to nearest escaping player ahead (NaN if none). |
| **Forward Escape Corridor (20u Wedge)** | | | |
| `opponents_in_escape_corridor_20` | int | $\ge 0$ | Escaping players in $20$u wedge toward goal $(120, 40)$ in opponent frame. |
| `defenders_in_escape_corridor_20` | int | $\ge 0$ | Pressing players in $20$u wedge toward goal. |
| `escape_corridor_advantage_20` | int | Integer | Corridor opponents minus corridor defenders. |
| `nearest_defender_in_escape_corridor` | float | $\ge 0.0$ | Distance to nearest defender in corridor (NaN if none). |
| `nearest_opponent_in_escape_corridor` | float | $\ge 0.0$ | Distance to nearest opponent in corridor (NaN if none). |
| `escape_corridor_coverage_20` | float | $[0.0, 1.0]$ | Camera coverage fraction of escape corridor wedge on pitch. |
| **Frozen Outcome Targets (For Reference)** | | | |
| `regain_5s_controlled` | int | {0, 1} | Primary Outcome 1 (frozen in Pre-Iteration-3 consistency gate). |
| `dangerous_escape_15s` | int | {0, 1} | Primary Outcome 2 (frozen in Pre-Iteration-3 consistency gate). |
| `episode_outcome_3class` | str | Categorical | Three-State Outcome: `dangerous_escape`, `successful_regain`, `harmless_escape`. |

