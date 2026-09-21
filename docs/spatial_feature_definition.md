# Spatial Feature Engineering & Geometric Definitions

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Conferences**: MIT Sloan Sports Analytics Conference (SSAC) & Carnegie Mellon Sports Analytics Conference (CMSAC)  
**Iteration**: 3 — Spatial Feature Engineering and Freeze-Frame Processing  
**Dataset**: Primary Cohort ($N = 21,616$ distinct episodes across 414 matches)

---

## 1. Geometric Foundations & Coordinate Systems

### Coordinate Units & Legal Boundary
- All pitch distances and coordinates are expressed in **StatsBomb coordinate units** ($120 \times 80$). No assumption of physical yards or meters is made without separate calibration.
- **Defending Goal Center**: $(0.0, 40.0)$
- **Attacking Goal Center**: $(120.0, 40.0)$
- **Touchlines**: $y = 0.0$ (top) and $y = 80.0$ (bottom)
- **Legal Pitch Bounding Box**: $\Omega_{\text{pitch}} = [0, 120] \times [0, 80]$, with total pitch area:
  $$\text{Area}(\Omega_{\text{pitch}}) = 120.0 \times 80.0 = 9600.0\,\text{coordinate area units}$$

### Counterpressing Team Perspective (Primary Frame)
- In the primary frame, the counterpressing team attacks from left to right ($x = 0 \to 120$).
- The counterpress initiation event location $(x_0, y_0)$ is the reference point for all local team support and density calculations.

### Opponent-Attack Coordinate System (Inverted Frame)
For transition escape features, all coordinates are transformed into the opponent's attacking frame:
$$x_{\text{opp}} = 120.0 - x, \quad y_{\text{opp}} = 80.0 - y$$
- In this frame, the opponent's transition attack direction is increasing $x_{\text{opp}}$ toward the goal center at $(120.0, 40.0)$.
- The ball origin transforms to $(x_{0, \text{opp}}, y_{0, \text{opp}}) = (120.0 - x_0, 80.0 - y_0)$.

---

## 2. Temporal Leakage Rule & Freeze-Frame Alignment

### Strict Pre-Initiation Information Horizon
Every spatial predictor is derived exclusively from the StatsBomb 360 freeze frame captured at the exact moment of counterpress initiation ($t = t_{\text{init}}$).
- **Prohibited Information**: No future event locations, pass completions, regain timestamps, dangerous escape events, or outcome classes are ever referenced.
- Frozen outcome labels (`regain_5s_controlled`, `dangerous_escape_15s`, `episode_outcome_3class`) are appended only as target variables for downstream modeling.

### Actor Identification and Strict Exclusion
StatsBomb 360 freeze frames mark the event actor with `actor = True`.
- The actor's position in the freeze frame aligns with $(x_0, y_0)$ within floating-point tolerance ($d \le 10^{-5}$ coordinate units in open-play pressure events).
- **Exclusion Rule**: The counterpressing actor is strictly excluded from all teammate-support metrics. For example, `visible_teammates_within_10` measures only **other** teammates.

```text
       StatsBomb 360 Freeze Frame Layout at Initiation
+-------------------------------------------------------------------+ y=80
|                                                                   |
|              [O] Opponent                                         |
|                                                                   |
|                      r=15u     r=10u    r=5u                      |
|                     . - - - - - - - - - .                         |
|                   '        . - - - .      '                       |
|                  '       '   [T]     '     '                      |
|                 (       (     ★       )     )                     |
|                  '       '  Actor    '     '                      |
|                   '        ' - - - '      '                       |
|                     ' - - - - - - - - - '                         |
|                                  [O]                              |
|                                                                   |
+-------------------------------------------------------------------+ y=0
x=0 (Own Goal)                                        x=120 (Attacking Goal)
```

---

## 3. Mathematical Feature Formulations

### A. Camera-Coverage Features ($r \in \{5, 10, 15\}$)
To account for partial broadcast camera visibility, local coverage is measured strictly against the portion of the circle physically lying on the pitch:
$$\Omega_{\text{local}}(r) = \mathcal{B}_r(x_0, y_0) \cap \Omega_{\text{pitch}}$$
$$\text{Area}_{\text{local}}(r) = \text{Area}(\Omega_{\text{local}}(r))$$
$$\text{visible\_local\_area}_r = \text{Area}\left(\Omega_{\text{local}}(r) \cap \mathcal{P}_{\text{visible}}\right)$$
$$\text{coverage}_r = \frac{\text{visible\_local\_area}_r}{\text{Area}_{\text{local}}(r)} \in [0.0, 1.0]$$

> [!NOTE]
> Near touchlines ($y_0 \approx 0$ or $y_0 \approx 80$) or goal lines ($x_0 \approx 0$ or $x_0 \approx 120$), $\text{Area}_{\text{local}}(r)$ is less than $\pi r^2$ (e.g. $\approx \frac{1}{2}\pi r^2$ along a touchline). Normalizing by the on-pitch area prevents false penalties for out-of-bounds space.

### B. Local Team Support & Opposition
Let $\mathcal{T}$ be visible counterpressing teammates (excluding the actor) and $\mathcal{O}$ be visible opponents:
- **Count within radius $r$**:
  $$\text{visible\_teammates\_within}_r = \sum_{p \in \mathcal{T}} \mathbb{I}(\|p - (x_0, y_0)\| \le r)$$
  $$\text{visible\_opponents\_within}_r = \sum_{p \in \mathcal{O}} \mathbb{I}(\|p - (x_0, y_0)\| \le r)$$
- **Numerical Advantage**:
  $$\text{numerical\_advantage}_r = \text{visible\_teammates\_within}_r - \text{visible\_opponents\_within}_r$$
- **Nearest-Neighbor Distances**:
  Let $d_{(1)}^{\mathcal{T}} \le d_{(2)}^{\mathcal{T}} \le d_{(3)}^{\mathcal{T}}$ be the sorted Euclidean distances to players in $\mathcal{T}$.
  If $|\mathcal{T}| < k$, the $k$-th nearest distance is assigned **NaN** (strictly never imputed as 0.0).

### C. Visibility-Aware Local Densities
$$\text{teammate\_density\_visible}_r = \frac{\text{visible\_teammates\_within}_r}{\text{visible\_local\_area}_r}$$
$$\text{opponent\_density\_visible}_r = \frac{\text{visible\_opponents\_within}_r}{\text{visible\_local\_area}_r}$$
*(Stored as NaN if $\text{visible\_local\_area}_r \le 10^{-4}$).*

### D. Visible Team Compactness & Convex Hulls
- **Standard Deviations**: Population standard deviation ($\text{ddof}=0$) of visible player coordinates:
  $$\sigma_x = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \bar{x})^2}, \quad \sigma_y = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \bar{y})^2}$$
- **Mean Pairwise Distance**:
  $$\bar{d}_{\text{pair}} = \frac{2}{N(N-1)} \sum_{i < j} \|p_i - p_j\| \quad (N \ge 2)$$
- **Convex Hull Area**:
  $$\text{hull\_area} = \text{Area}(\text{ConvexHull}(\{p_1, \dots, p_N\}))$$
  *Rule: Requires $N \ge 3$ non-collinear points. Collinear configurations or $N < 3$ return NaN (never zero).*

---

## 4. Forward Escape Structure & Escape Corridor

### A. Opponents Ahead of the Ball
In opponent-oriented coordinates ($x_{\text{opp}}, y_{\text{opp}}$):
- Escaping players ahead: $p \in \mathcal{O}$ such that $x_{\text{opp}}(p) > x_{0, \text{opp}}$.
- Defending players ahead: $p \in \mathcal{T}$ such that $x_{\text{opp}}(p) > x_{0, \text{opp}}$.
- **Forward Numerical Advantage**:
  $$\text{forward\_numerical\_advantage} = \text{opponents\_ahead\_of\_ball} - \text{defenders\_ahead\_of\_ball}$$

### B. Forward Escape Corridor (20-Unit Wedge)
The escape corridor is defined as an angular wedge originating at $(x_{0, \text{opp}}, y_{0, \text{opp}})$ directed toward the center of the opponent's attacking goal $(120.0, 40.0)$:
- **Radius**: $R = 20.0$ StatsBomb coordinate units
- **Target Direction**: $\theta_{\text{goal}} = \text{atan2}(40.0 - y_{0, \text{opp}}, 120.0 - x_{0, \text{opp}})$
- **Angular Half-Width**: $\Delta\theta = 30^\circ = \frac{\pi}{6}$ radians (full cone angle $60^\circ$)

```text
       Forward Escape Corridor in Opponent Attacking Coordinates
                                                          Goal (120, 40)
                                                                 |
               \                                                |
                \  +30°                                         v
                 \                                       [---+---]
                  \-----_                             ===|   |   |===
                   \     \                           /   |   |   |
                    \     \                         /    [---+---]
  Ball (x0, y0) -----\=====\---------------------> /
                    /     /                         \
                   /     /                           \
                  /----~                              ===
                 / -30°
                /
               /
```

- **Inclusion Criteria**: A player at $p = (x, y)$ is inside the corridor if:
  1. $\|p - (x_{0, \text{opp}}, y_{0, \text{opp}})\| \le 20.0$
  2. $|\text{atan2}(y - y_{0, \text{opp}}, x - x_{0, \text{opp}}) - \theta_{\text{goal}}| \le 30^\circ$ (with circular normalization)
- **Escape Corridor Advantage**:
  $$\text{escape\_corridor\_advantage\_20} = \text{opponents\_in\_escape\_corridor\_20} - \text{defenders\_in\_escape\_corridor\_20}$$
- **Escape Corridor Visibility**:
  $$\text{escape\_corridor\_coverage\_20} = \frac{\text{Area}(\mathcal{W}_{\text{corridor}} \cap \mathcal{P}_{\text{visible, opp}} \cap \Omega_{\text{pitch}})}{\text{Area}(\mathcal{W}_{\text{corridor}} \cap \Omega_{\text{pitch}})} \in [0.0, 1.0]$$

---

## 5. Summary Table of Engineered Spatial Features

| Feature Name | Type | Valid Range | Missingness Rule | Description |
| :--- | :---: | :---: | :---: | :--- |
| `initiation_x` | float | $[0.0, 120.0]$ | Never null | Event x-coordinate in pressing team frame |
| `initiation_y` | float | $[0.0, 80.0]$ | Never null | Event y-coordinate in pressing team frame |
| `actor_present` | bool | {True, False} | Never null | True if freeze frame explicitly flagged actor |
| `actor_distance_from_event` | float | $\ge 0.0$ | NaN if missing actor | Euclidean distance between actor and event |
| `actor_matching_anomalous` | bool | {True, False} | Never null | True if distance > 1.0 or actor missing |
| `frame_player_count` | int | $[0, 22]$ | Never null | Total visible players detected in 360 frame |
| `visible_teammate_count_excluding_actor` | int | $[0, 10]$ | Never null | Visible pressing teammates (excluding actor) |
| `visible_opponent_count` | int | $[0, 11]$ | Never null | Visible opponent players |
| `visible_goalkeeper_count` | int | $[0, 2]$ | Never null | Visible goalkeepers |
| `visible_area_polygon_area` | float | $[0.0, 9600.0]$ | 0.0 if missing | Clipped camera viewport area on pitch |
| `visible_area_pitch_fraction` | float | $[0.0, 1.0]$ | 0.0 if missing | Visible area divided by pitch area (9600) |
| `coverage_5`, `10`, `15` | float | $[0.0, 1.0]$ | 0.0 if missing | Camera coverage fraction of local on-pitch circle |
| `visible_local_area_5`, `10`, `15` | float | $\ge 0.0$ | 0.0 if missing | Visible area inside on-pitch circle |
| `coverage_5_ge_80pct`, `10`, `15` | bool | {True, False} | False if missing | Sensitivity flag: coverage $\ge 80\%$ |
| `visible_teammates_within_5`, `10`, `15` | int | $\ge 0$ | Never null | Teammates within radius (actor excluded) |
| `nearest_teammate_distance` | float | $\ge 0.0$ | NaN if count < 1 | Distance to 1st nearest teammate |
| `second_nearest_teammate_distance` | float | $\ge 0.0$ | NaN if count < 2 | Distance to 2nd nearest teammate |
| `third_nearest_teammate_distance` | float | $\ge 0.0$ | NaN if count < 3 | Distance to 3rd nearest teammate |
| `visible_opponents_within_5`, `10`, `15` | int | $\ge 0$ | Never null | Opponents within radius |
| `nearest_opponent_distance` | float | $\ge 0.0$ | NaN if count < 1 | Distance to 1st nearest opponent |
| `second_nearest_opponent_distance` | float | $\ge 0.0$ | NaN if count < 2 | Distance to 2nd nearest opponent |
| `third_nearest_opponent_distance` | float | $\ge 0.0$ | NaN if count < 3 | Distance to 3rd nearest opponent |
| `numerical_advantage_5`, `10`, `15` | int | Integer | Never null | Teammates minus opponents within radius |
| `total_players_within_5`, `10`, `15` | int | $\ge 0$ | Never null | Teammates + opponents + actor |
| `teammate_density_visible_5`, `10`, `15` | float | $\ge 0.0$ | NaN if area $\le 10^{-4}$ | Teammates per visible local square unit |
| `opponent_density_visible_5`, `10`, `15` | float | $\ge 0.0$ | NaN if area $\le 10^{-4}$ | Opponents per visible local square unit |
| `teammate_x_std`, `y_std` | float | $\ge 0.0$ | NaN if teammates < 2 | Visible teammate spatial spread |
| `opponent_x_std`, `y_std` | float | $\ge 0.0$ | NaN if opponents < 2 | Visible opponent spatial spread |
| `teammate_mean_pairwise_distance` | float | $\ge 0.0$ | NaN if teammates < 2 | Mean distance between teammate pairs |
| `opponent_mean_pairwise_distance` | float | $\ge 0.0$ | NaN if opponents < 2 | Mean distance between opponent pairs |
| `teammate_hull_area` | float | $\ge 0.0$ | NaN if teammates < 3 | 2D convex hull area (non-collinear) |
| `opponent_hull_area` | float | $\ge 0.0$ | NaN if opponents < 3 | 2D convex hull area (non-collinear) |
| `teammate_hull_visible_area_ratio` | float | $\ge 0.0$ | NaN if hull is NaN | Hull area / visible area |
| `opponent_hull_visible_area_ratio` | float | $\ge 0.0$ | NaN if hull is NaN | Hull area / visible area |
| `distance_to_nearest_touchline` | float | $[0.0, 40.0]$ | Never null | $\min(y_0, 80 - y_0)$ |
| `distance_to_own_goal_line` | float | $[0.0, 120.0]$ | Never null | $x_0$ |
| `distance_to_opponent_goal_line` | float | $[0.0, 120.0]$ | Never null | $120 - x_0$ |
| `lateral_centrality` | float | $[0.0, 1.0]$ | Never null | $1 - |y_0 - 40| / 40$ |
| `pitch_zone` | str | Categorical | Never null | defensive, middle, or attacking third |
| `pitch_zone_3x3` | str | Categorical | Never null | Third crossed with left, center, right |
| `opponents_ahead_of_ball` | int | $\ge 0$ | Never null | Escaping players with $x_{\text{opp}} > x_{0, \text{opp}}$ |
| `defenders_ahead_of_ball` | int | $\ge 0$ | Never null | Pressing players with $x_{\text{opp}} > x_{0, \text{opp}}$ |
| `forward_numerical_advantage` | int | Integer | Never null | Opponents ahead minus defenders ahead |
| `nearest_defender_ahead_distance` | float | $\ge 0.0$ | NaN if defenders ahead = 0 | Distance to nearest defending player ahead |
| `nearest_opponent_ahead_distance` | float | $\ge 0.0$ | NaN if opponents ahead = 0 | Distance to nearest escaping player ahead |
| `opponents_in_escape_corridor_20` | int | $\ge 0$ | Never null | Escaping players in $20$u wedge |
| `defenders_in_escape_corridor_20` | int | $\ge 0$ | Never null | Pressing players in $20$u wedge |
| `escape_corridor_advantage_20` | int | Integer | Never null | Corridor opponents minus corridor defenders |
| `nearest_defender_in_escape_corridor` | float | $\ge 0.0$ | NaN if no defender | Distance to nearest defender in wedge |
| `nearest_opponent_in_escape_corridor` | float | $\ge 0.0$ | NaN if no opponent | Distance to nearest opponent in wedge |
| `escape_corridor_coverage_20` | float | $[0.0, 1.0]$ | 0.0 if missing | Camera coverage fraction of escape wedge |
