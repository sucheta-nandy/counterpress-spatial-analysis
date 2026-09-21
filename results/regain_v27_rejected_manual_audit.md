# Audit of Counterpress Regain Reductions: v2.6 Positive $\to$ v2.7 Negative (120 Cases)

**Cohort**: 120 Stratified Random Cases where `regain_5s_controlled_v26 = 1` and `regain_5s_controlled = 0`
**Audit Execution Time**: 2026-09-18 16:14:35

## Sampling Stratification Schema
- **First Control = Carry**: 30 episodes
- **First Control = Completed Pass**: 30 episodes
- **First Control = Ball Receipt***: 20 episodes
- **First Control = Dribble**: 15 episodes
- **First Control = Shot**: 10 episodes
- **Other / Common Pathways**: 15 episodes

> [!IMPORTANT]
> All human verification fields in this report are strictly blank placeholders for scientific evaluation.

---

### Case 1: Episode `3794686_p43_39539e6f`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.17 | 00:22:58.653 | Spain              | Spain              | 42 | Ball Receipt*   |   -   | [67.5, 41.1]    | Controlled Receipt        |  |
|  -2.17 | 00:22:58.653 | Spain              | Spain              | 42 | Carry           |   -   | [67.5, 41.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.93 | 00:22:59.886 | Spain              | Spain              | 42 | Pass            |   -   | [70.0, 45.6]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:23:00.820 | Spain              | Spain              | 42 | Ball Receipt*   |   -   | [77.9, 59.7]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:23:00.820 | Croatia            | Croatia            | 43 | Interception    |  Yes  | [43.4, 24.0]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:23:00.820 | Croatia            | Croatia            | 43 | Carry           |   -   | [43.4, 24.0]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.62 | 00:23:03.437 | Croatia            | Croatia            | 43 | Pass            |   -   | [61.9, 21.3]    | -> Ante Rebić             |  |
|  +3.82 | 00:23:04.635 | Croatia            | Croatia            | 43 | Ball Receipt*   |   -   | [75.0, 6.3]     | Controlled Receipt        |  |
|  +3.82 | 00:23:04.635 | Croatia            | Croatia            | 43 | Carry           |   -   | [75.0, 6.3]     | Carry                     |  |
|  +7.19 | 00:23:08.013 | Spain              | Croatia            | 43 | Pressure        |   -   | [32.9, 66.9]    |                           |  |
|  +7.46 | 00:23:08.278 | Croatia            | Croatia            | 43 | Pass            |   -   | [85.4, 12.0]    | -> Mateo Kovačić          |  |
|  -2.84 | 00:22:57.983 | Croatia            | Croatia            | 133 | Pass            |   -   | [28.7, 40.1]    | -> Domagoj Vida           |  |
|  -1.41 | 00:22:59.409 | Croatia            | Croatia            | 133 | Ball Receipt*   |   -   | [39.4, 64.1]    | Controlled Receipt        |  |
|  -1.41 | 00:22:59.409 | Croatia            | Croatia            | 133 | Carry           |   -   | [39.4, 64.1]    | Carry                     |  |
|  +1.16 | 00:23:01.984 | Croatia            | Croatia            | 133 | Pass            |   -   | [39.4, 64.1]    | -> Duje Ćaleta-Ca         |  |
|  +2.89 | 00:23:03.713 | Croatia            | Croatia            | 133 | Ball Receipt*   |   -   | [29.4, 28.8]    | Controlled Receipt        |  |
|  +2.89 | 00:23:03.713 | Croatia            | Croatia            | 133 | Carry           |   -   | [29.4, 28.8]    | Carry                     |  |
|  +5.04 | 00:23:05.864 | Croatia            | Croatia            | 133 | Pass            |   -   | [33.1, 25.7]    | -> Joško Gvardiol         |  |
|  +6.81 | 00:23:07.625 | Croatia            | Croatia            | 133 | Ball Receipt*   |   -   | [43.1, 3.1]     | Controlled Receipt        |  |
|  +6.81 | 00:23:07.625 | Croatia            | Croatia            | 133 | Carry           |   -   | [43.1, 3.1]     | Carry                     |  |

---

### Case 2: Episode `3794686_p90_53eeeb3b`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +6.65 | 00:00:23.881 | Croatia            | Croatia            | 3 | Pass            |   -   | [25.5, 0.1]     | -> Bruno Petković         | **PRESSING-TEAM FIRST CONTROL** |
|  +7.74 | 00:00:24.971 | Spain              | Croatia            | 3 | Pressure        |   -   | [75.5, 74.1]    |                           |  |
|  +7.94 | 00:00:25.169 | Croatia            | Croatia            | 3 | Ball Receipt*   |   -   | [45.6, 6.0]     | Controlled Receipt        |  |
|  +7.94 | 00:00:25.169 | Croatia            | Croatia            | 3 | Carry           |   -   | [45.6, 6.0]     | Carry                     |  |
|  -2.69 | 00:00:14.544 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [89.4, 30.1]    | Controlled Receipt        |  |
|  -2.69 | 00:00:14.544 | Spain              | Spain              | 89 | Pass            |   -   | [88.7, 26.0]    | -> Sergio Busquet         |  |
|  -1.18 | 00:00:16.055 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [79.4, 48.0]    | Controlled Receipt        |  |
|  -1.18 | 00:00:16.055 | Spain              | Spain              | 89 | Pass            |   -   | [79.4, 48.0]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:00:17.233 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [94.0, 58.5]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:00:17.233 | Croatia            | Croatia            | 90 | Interception    |  Yes  | [27.7, 22.7]    | Won                       | **CP INITIATION** |
|  +0.00 | 00:00:17.233 | Croatia            | Croatia            | 90 | Carry           |   -   | [27.7, 22.7]    | Carry                     | (v2.6 Regain Event) |
|  +0.46 | 00:00:17.691 | Spain              | Croatia            | 90 | Pressure        |  Yes  | [90.0, 49.6]    |                           |  |
|  +1.10 | 00:00:18.332 | Croatia            | Croatia            | 90 | Pass            |   -   | [30.1, 24.9]    | -> Mateo Kovačić          |  |
|  +1.89 | 00:00:19.126 | Croatia            | Croatia            | 90 | Ball Receipt*   |   -   | [39.4, 17.5]    | Controlled Receipt        |  |
|  +1.89 | 00:00:19.126 | Croatia            | Croatia            | 90 | Carry           |   -   | [39.4, 17.5]    | Carry                     |  |
|  -2.34 | 00:00:14.890 | Croatia            | Spain              | 179 | Pressure        |   -   | [62.0, 70.7]    |                           |  |
|  -2.09 | 00:00:15.148 | Spain              | Spain              | 179 | Pass            |   -   | [58.9, 9.1]     | -> Daniel Olmo Ca         |  |
|  -1.02 | 00:00:16.210 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [64.7, 1.6]     | Controlled Receipt        |  |
|  -1.02 | 00:00:16.210 | Spain              | Spain              | 179 | Carry           |   -   | [64.7, 1.6]     | Carry                     |  |
|  -0.27 | 00:00:16.963 | Croatia            | Spain              | 179 | Pressure        |   -   | [55.4, 77.1]    |                           |  |
|  -0.08 | 00:00:17.149 | Spain              | Spain              | 179 | Pass            |   -   | [63.4, 3.8]     | -> Pau Francisco          |  |
|  +2.08 | 00:00:19.312 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [41.4, 3.1]     | Controlled Receipt        |  |
|  +2.08 | 00:00:19.312 | Spain              | Spain              | 179 | Carry           |   -   | [41.4, 3.1]     | Carry                     |  |
|  +3.02 | 00:00:20.248 | Spain              | Spain              | 179 | Pass            |   -   | [41.8, 3.6]     | -> Unai Simón Men         |  |
|  +5.14 | 00:00:22.371 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [17.9, 25.2]    | Controlled Receipt        |  |
|  +5.14 | 00:00:22.371 | Spain              | Spain              | 179 | Carry           |   -   | [17.9, 25.2]    | Carry                     |  |
|  +6.05 | 00:00:23.284 | Spain              | Spain              | 179 | Pass            |   -   | [17.2, 25.2]    | -> Aymeric Laport         |  |
|  +7.98 | 00:00:25.210 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [26.4, 48.9]    | Controlled Receipt        |  |
|  +7.98 | 00:00:25.210 | Spain              | Spain              | 179 | Carry           |   -   | [26.4, 48.9]    | Carry                     |  |
|  -2.05 | 00:00:15.184 | Spain              | Spain              | 204 | Pass            |   -   | [71.5, 24.3]    | -> Fabián Ruiz Pe         |  |
|  -1.02 | 00:00:16.214 | Spain              | Spain              | 204 | Ball Receipt*   |   -   | [65.2, 42.6]    | Controlled Receipt        |  |
|  -1.02 | 00:00:16.214 | Spain              | Spain              | 204 | Carry           |   -   | [65.2, 42.6]    | Carry                     |  |
|  +0.98 | 00:00:18.209 | Spain              | Spain              | 204 | Pass            |   -   | [65.0, 50.7]    | -> César Azpilicu         |  |
|  +2.27 | 00:00:19.507 | Spain              | Spain              | 204 | Ball Receipt*   |   -   | [50.3, 64.0]    | Controlled Receipt        |  |
|  +2.27 | 00:00:19.507 | Spain              | Spain              | 204 | Carry           |   -   | [50.3, 64.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +2.68 | 00:00:19.909 | Spain              | Spain              | 204 | Pass            |   -   | [50.3, 64.0]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +5.85 | 00:00:23.081 | Croatia            | Croatia            | 205 | Pass            |   -   | [44.7, 25.7]    | -> Mislav Oršić           |  |
|  +7.40 | 00:00:24.632 | Croatia            | Croatia            | 205 | Ball Receipt*   |   -   | [69.5, 8.3]     | Controlled Receipt        |  |
|  +7.40 | 00:00:24.632 | Croatia            | Croatia            | 205 | Carry           |   -   | [69.5, 8.3]     | Carry                     |  |
|  +7.45 | 00:00:24.688 | Croatia            | Croatia            | 205 | Pass            |   -   | [69.5, 8.3]     | -> Mario Pašalić          |  |

---

### Case 3: Episode `3794686_p100_5de42a88`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +5.70 | 00:05:11.482 | Spain              | Spain              | 11 | Pass            |   -   | [82.4, 56.6]    | -> Ferrán Torres          | **PRESSING-TEAM FIRST CONTROL** |
|  +6.85 | 00:05:12.631 | Spain              | Spain              | 11 | Ball Receipt*   |   -   | [104.7, 45.3]   | Controlled Receipt        |  |
|  +6.86 | 00:05:12.644 | Croatia            | Spain              | 11 | Duel            |   -   | [15.4, 34.8]    | Aerial Lost               |  |
|  +6.86 | 00:05:12.644 | Spain              | Spain              | 11 | Miscontrol      |   -   | [104.7, 45.3]   | Miscontrol                |  |
|  -1.69 | 00:05:04.089 | Croatia            | Croatia            | 99 | Pass            |   -   | [63.2, 55.0]    | -> Andrej Kramari         |  |
|  -0.63 | 00:05:05.154 | Spain              | Croatia            | 99 | Pressure        |   -   | [66.7, 44.5]    |                           |  |
|  -0.59 | 00:05:05.198 | Croatia            | Croatia            | 99 | Ball Receipt*   |   -   | [54.3, 38.6]    | Controlled Receipt        |  |
|  -0.59 | 00:05:05.198 | Croatia            | Croatia            | 99 | Carry           |   -   | [54.3, 38.6]    | Carry                     |  |
|  +0.00 | 00:05:05.783 | Croatia            | Croatia            | 99 | Dispossessed    |   -   | [54.1, 38.8]    | Dispossessed              |  |
|  +0.00 | 00:05:05.783 | Spain              | Spain              | 100 | Duel            |  Yes  | [66.0, 41.3]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:05:05.783 | Spain              | Spain              | 100 | Carry           |   -   | [66.0, 41.3]    | Carry                     | (v2.6 Regain Event) |
|  +1.88 | 00:05:07.661 | Spain              | Spain              | 100 | Pass            |   -   | [58.6, 38.9]    | -> Sergio Busquet         |  |
|  +2.64 | 00:05:08.422 | Spain              | Spain              | 100 | Ball Receipt*   |   -   | [51.9, 32.1]    | Controlled Receipt        |  |
|  +2.64 | 00:05:08.422 | Spain              | Spain              | 100 | Carry           |   -   | [51.9, 32.1]    | Carry                     |  |
|  +4.53 | 00:05:10.311 | Spain              | Spain              | 100 | Pass            |   -   | [51.9, 33.0]    | -> Aymeric Laport         |  |
|  +5.19 | 00:05:10.969 | Spain              | Spain              | 100 | Ball Receipt*   |   -   | [46.2, 32.3]    | Controlled Receipt        |  |
|  +5.19 | 00:05:10.969 | Spain              | Spain              | 100 | Carry           |   -   | [46.2, 32.3]    | Carry                     |  |
|  -1.18 | 00:05:04.601 | Croatia            | Croatia            | 187 | Pass            |   -   | [83.3, 14.5]    | -> Mislav Oršić           |  |
|  +0.91 | 00:05:06.690 | Croatia            | Croatia            | 187 | Ball Receipt*   |   -   | [101.2, 7.6]    | Controlled Receipt        |  |
|  +0.91 | 00:05:06.690 | Croatia            | Croatia            | 187 | Carry           |   -   | [101.2, 7.6]    | Carry                     |  |
|  +3.75 | 00:05:09.533 | Spain              | Croatia            | 187 | Pressure        |   -   | [6.1, 57.8]     |                           |  |
|  +5.25 | 00:05:11.032 | Croatia            | Croatia            | 187 | Pass            |   -   | [116.9, 24.1]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +5.85 | 00:05:11.629 | Croatia            | Croatia            | 187 | Ball Receipt*   |   -   | [114.0, 44.1]   | Incomplete Receipt (Incomplete) |  |
|  +5.85 | 00:05:11.629 | Spain              | Croatia            | 187 | Clearance       |   -   | [4.7, 38.3]     |                           |  |
|  +6.40 | 00:05:12.185 | Croatia            | Croatia            | 187 | Pass            |   -   | [112.3, 38.1]   | -> Andrej Kramari         |  |
|  +7.65 | 00:05:13.430 | Croatia            | Croatia            | 187 | Ball Receipt*   |   -   | [112.2, 41.8]   | Controlled Receipt        |  |
|  +7.67 | 00:05:13.453 | Croatia            | Croatia            | 187 | Shot            |   -   | [112.1, 40.5]   | Saved                     | **OPPONENT LAST CONTROL** |
|  +7.92 | 00:05:13.701 | Spain              | Croatia            | 187 | Goal Keeper     |   -   | [1.4, 40.6]     |                           |  |
|  +0.18 | 00:05:05.966 | Spain              | Spain              | 213 | Pass            |   -   | [11.5, 33.9]    | -> Rodrigo Hernán         |  |
|  +1.20 | 00:05:06.987 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [21.8, 24.3]    | Controlled Receipt        |  |
|  +1.20 | 00:05:06.987 | Spain              | Spain              | 213 | Carry           |   -   | [21.8, 24.3]    | Carry                     |  |
|  +2.02 | 00:05:07.808 | Spain              | Spain              | 213 | Pass            |   -   | [21.8, 24.3]    | -> Jordi Alba Ram         |  |
|  +2.97 | 00:05:08.753 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [22.9, 7.2]     | Controlled Receipt        |  |
|  +2.97 | 00:05:08.753 | Spain              | Spain              | 213 | Carry           |   -   | [22.9, 7.2]     | Carry                     |  |
|  +4.01 | 00:05:09.791 | Spain              | Spain              | 213 | Pass            |   -   | [22.9, 7.2]     | Incomplete (Out)          |  |

---

### Case 4: Episode `3794686_p114_e0634cba`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.14 | 00:14:03.296 | Spain              | Croatia            | 113 | Pressure        |   -   | [37.5, 11.2]    |                           |  |
|  -1.69 | 00:14:03.746 | Croatia            | Croatia            | 113 | Pass            |   -   | [83.9, 73.7]    | -> Andrej Kramari         |  |
|  -0.99 | 00:14:04.451 | Croatia            | Croatia            | 113 | Ball Receipt*   |   -   | [86.8, 60.9]    | Controlled Receipt        |  |
|  -0.99 | 00:14:04.451 | Croatia            | Croatia            | 113 | Carry           |   -   | [86.8, 60.9]    | Carry                     |  |
|  -0.82 | 00:14:04.615 | Spain              | Croatia            | 113 | Pressure        |   -   | [33.3, 12.9]    |                           |  |
|  +0.00 | 00:14:05.439 | Croatia            | Croatia            | 113 | Dispossessed    |   -   | [86.8, 64.4]    | Dispossessed              |  |
|  +0.00 | 00:14:05.439 | Spain              | Spain              | 114 | Duel            |  Yes  | [33.3, 15.7]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:14:05.439 | Spain              | Spain              | 114 | Carry           |   -   | [33.3, 15.7]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.98 | 00:14:06.415 | Croatia            | Spain              | 114 | Pressure        |  Yes  | [84.8, 60.2]    |                           |  |
|  +2.54 | 00:14:07.982 | Croatia            | Spain              | 114 | Pressure        |  Yes  | [84.4, 58.2]    |                           |  |
|  +2.90 | 00:14:08.342 | Spain              | Spain              | 114 | Pass            |   -   | [33.8, 26.0]    | -> Sergio Busquet         |  |
|  +3.74 | 00:14:09.181 | Spain              | Spain              | 114 | Ball Receipt*   |   -   | [40.1, 37.6]    | Controlled Receipt        |  |
|  +3.74 | 00:14:09.181 | Spain              | Spain              | 114 | Pass            |   -   | [40.1, 37.6]    | -> Pedro González         |  |
|  +4.73 | 00:14:10.169 | Spain              | Spain              | 114 | Ball Receipt*   |   -   | [40.3, 28.8]    | Controlled Receipt        |  |
|  +4.73 | 00:14:10.169 | Spain              | Spain              | 114 | Carry           |   -   | [40.3, 28.8]    | Carry                     |  |
|  +5.53 | 00:14:10.973 | Spain              | Spain              | 114 | Pass            |   -   | [37.5, 29.9]    | -> Unai Simón Men         |  |
|  +7.86 | 00:14:13.298 | Spain              | Spain              | 114 | Ball Receipt*   |   -   | [10.4, 37.3]    | Controlled Receipt        |  |
|  +7.86 | 00:14:13.298 | Spain              | Spain              | 114 | Carry           |   -   | [10.4, 37.3]    | Carry                     |  |
|  +0.17 | 00:14:05.613 | Croatia            | Croatia            | 200 | Pass            |   -   | [61.0, 40.1]    | -> Luka Modrić            |  |
|  +1.42 | 00:14:06.863 | Croatia            | Croatia            | 200 | Ball Receipt*   |   -   | [53.9, 47.6]    | Controlled Receipt        |  |
|  +1.42 | 00:14:06.863 | Croatia            | Croatia            | 200 | Carry           |   -   | [53.9, 47.6]    | Carry                     |  |
|  +2.35 | 00:14:07.788 | Croatia            | Croatia            | 200 | Pass            |   -   | [53.3, 47.4]    | -> Marcelo Brozov         |  |
|  +3.30 | 00:14:08.741 | Croatia            | Croatia            | 200 | Ball Receipt*   |   -   | [52.2, 38.7]    | Controlled Receipt        |  |
|  +3.30 | 00:14:08.741 | Croatia            | Croatia            | 200 | Carry           |   -   | [52.2, 38.7]    | Carry                     |  |
|  +4.98 | 00:14:10.422 | Croatia            | Croatia            | 200 | Pass            |   -   | [49.8, 33.4]    | -> Joško Gvardiol         |  |
|  +6.31 | 00:14:11.753 | Croatia            | Croatia            | 200 | Ball Receipt*   |   -   | [48.9, 16.5]    | Controlled Receipt        |  |
|  +6.31 | 00:14:11.753 | Croatia            | Croatia            | 200 | Carry           |   -   | [48.9, 16.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +1.50 | 00:14:06.935 | Spain              | Spain              | 222 | Pass            |   -   | [75.0, 62.6]    | -> Daniel Olmo Ca         |  |
|  +2.98 | 00:14:08.423 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [77.8, 77.0]    | Controlled Receipt        |  |
|  +2.98 | 00:14:08.423 | Spain              | Spain              | 222 | Carry           |   -   | [77.8, 77.0]    | Carry                     |  |
|  +3.90 | 00:14:09.336 | Spain              | Spain              | 222 | Pass            |   -   | [77.8, 77.0]    | -> Rodrigo Hernán         |  |
|  +5.20 | 00:14:10.638 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [68.4, 73.6]    | Controlled Receipt        |  |
|  +5.20 | 00:14:10.638 | Spain              | Spain              | 222 | Carry           |   -   | [68.4, 73.6]    | Carry                     |  |
|  +5.38 | 00:14:10.820 | Croatia            | Spain              | 222 | Pressure        |   -   | [49.5, 11.1]    |                           |  |
|  +5.56 | 00:14:10.999 | Spain              | Spain              | 222 | Pass            |   -   | [68.0, 73.6]    | -> Mikel Oyarzaba         |  |
|  +6.47 | 00:14:11.907 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [76.3, 67.0]    | Controlled Receipt        |  |
|  +6.47 | 00:14:11.907 | Spain              | Spain              | 222 | Carry           |   -   | [76.3, 67.0]    | Carry                     |  |
|  +7.13 | 00:14:12.574 | Spain              | Spain              | 222 | Pass            |   -   | [71.3, 66.8]    | -> Aymeric Laport         |  |

---

### Case 5: Episode `3788764_p138_757110b4`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.05 | 00:36:52.444 | Germany            | Germany            | 69 | Ball Receipt*   |   -   | [78.9, 2.8]     | Controlled Receipt        |  |
|  -2.05 | 00:36:52.444 | Germany            | Germany            | 69 | Carry           |   -   | [78.9, 2.8]     | Carry                     |  |
|  -1.76 | 00:36:52.740 | Portugal           | Germany            | 69 | Pressure        |   -   | [35.3, 77.9]    |                           |  |
|  -1.30 | 00:36:53.196 | Germany            | Germany            | 69 | Pass            |   -   | [76.3, 3.0]     | -> Antonio Rüdige         |  |
|  +0.33 | 00:36:54.827 | Germany            | Germany            | 69 | Ball Receipt*   |   -   | [64.9, 3.8]     | Controlled Receipt        |  |
|  +0.33 | 00:36:54.827 | Germany            | Germany            | 69 | Carry           |   -   | [64.9, 3.8]     | Carry                     |  |
|  +1.42 | 00:36:55.918 | Germany            | Germany            | 69 | Pass            |   -   | [64.6, 9.6]     | -> Toni Kroos             |  |
|  +2.57 | 00:36:57.066 | Germany            | Germany            | 69 | Ball Receipt*   |   -   | [60.3, 15.9]    | Controlled Receipt        |  |
|  +2.57 | 00:36:57.066 | Germany            | Germany            | 69 | Carry           |   -   | [60.3, 15.9]    | Carry                     |  |
|  +4.09 | 00:36:58.584 | Germany            | Germany            | 69 | Pass            |   -   | [61.5, 23.4]    | Incomplete (Out)          |  |
|  +7.94 | 00:37:02.441 | Germany            | Germany            | 69 | Ball Receipt*   |   -   | [113.9, 72.8]   | Incomplete Receipt (Incomplete) |  |
|  -1.67 | 00:36:52.831 | Portugal           | Portugal           | 138 | Pressure        |   -   | [90.2, 49.2]    |                           |  |
|  -0.83 | 00:36:53.663 | Portugal           | Portugal           | 138 | Ball Receipt*   |   -   | [91.9, 49.9]    | Incomplete Receipt (Incomplete) |  |
|  -0.83 | 00:36:53.663 | Germany            | Portugal           | 138 | Ball Recovery   |   -   | [26.6, 27.7]    |                           |  |
|  -0.83 | 00:36:53.663 | Germany            | Portugal           | 138 | Carry           |   -   | [26.6, 27.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:36:54.497 | Germany            | Portugal           | 138 | Dispossessed    |   -   | [21.9, 28.9]    | Dispossessed              |  |
|  +0.00 | 00:36:54.497 | Portugal           | Portugal           | 138 | Duel            |  Yes  | [98.2, 51.2]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:36:54.497 | Portugal           | Portugal           | 138 | Carry           |   -   | [98.2, 51.2]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +5.36 | 00:36:59.860 | Portugal           | Portugal           | 138 | Pass            |   -   | [91.3, 53.4]    | -> João Filipe Ir         |  |
|  +6.66 | 00:37:01.153 | Portugal           | Portugal           | 138 | Ball Receipt*   |   -   | [78.6, 49.6]    | Controlled Receipt        |  |
|  +6.66 | 00:37:01.153 | Portugal           | Portugal           | 138 | Carry           |   -   | [78.6, 49.6]    | Carry                     |  |
|  +7.45 | 00:37:01.947 | Germany            | Portugal           | 138 | Pressure        |   -   | [40.3, 36.6]    |                           |  |
|  +7.62 | 00:37:02.122 | Portugal           | Portugal           | 138 | Pass            |   -   | [80.3, 51.4]    | -> Renato Júnior          |  |

---

### Case 6: Episode `3788764_p89_ef63dacd`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.58 | 00:02:27.536 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [23.8, 16.6]    | Controlled Receipt        |  |
|  -2.58 | 00:02:27.536 | Germany            | Germany            | 5 | Carry           |   -   | [23.8, 16.6]    | Carry                     |  |
|  -2.44 | 00:02:27.681 | Portugal           | Germany            | 5 | Pressure        |   -   | [97.3, 74.2]    |                           |  |
|  -1.33 | 00:02:28.785 | Germany            | Germany            | 5 | Pass            |   -   | [27.9, 18.3]    | -> Serge Gnabry           |  |
|  +0.02 | 00:02:30.141 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [51.1, 27.9]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.02 | 00:02:30.141 | Germany            | Germany            | 5 | Carry           |   -   | [51.1, 27.9]    | Carry                     |  |
|  +2.25 | 00:02:32.366 | Germany            | Germany            | 5 | Pass            |   -   | [51.1, 23.4]    | -> Kai Havertz            |  |
|  +3.09 | 00:02:33.208 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [50.5, 11.6]    | Controlled Receipt        |  |
|  +3.09 | 00:02:33.208 | Germany            | Germany            | 5 | Carry           |   -   | [50.5, 11.6]    | Carry                     |  |
|  +3.21 | 00:02:33.328 | Germany            | Germany            | 5 | Pass            |   -   | [56.0, 6.1]     | -> İlkay Gündoğan         |  |
|  +4.62 | 00:02:34.741 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [47.9, 15.2]    | Controlled Receipt        |  |
|  +4.62 | 00:02:34.741 | Germany            | Germany            | 5 | Carry           |   -   | [47.9, 15.2]    | Carry                     |  |
|  -2.66 | 00:02:27.462 | Portugal           | Portugal           | 88 | Pass            |   -   | [114.2, 80.0]   | -> Renato Júnior          |  |
|  -1.81 | 00:02:28.305 | Portugal           | Portugal           | 88 | Ball Receipt*   |   -   | [113.7, 72.5]   | Controlled Receipt        |  |
|  -1.81 | 00:02:28.305 | Portugal           | Portugal           | 88 | Carry           |   -   | [113.7, 72.5]   | Carry                     |  |
|  -1.79 | 00:02:28.330 | Germany            | Portugal           | 88 | Pressure        |   -   | [6.4, 7.6]      |                           |  |
|  -0.95 | 00:02:29.168 | Portugal           | Portugal           | 88 | Pass            |   -   | [113.7, 72.5]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.13 | 00:02:29.984 | Portugal           | Portugal           | 88 | Pressure        |   -   | [108.9, 75.5]   |                           |  |
|  +0.00 | 00:02:30.118 | Portugal           | Portugal           | 88 | Ball Receipt*   |   -   | [109.8, 75.5]   | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:02:30.118 | Germany            | Germany            | 89 | Interception    |  Yes  | [9.0, 6.1]      | Won                       | **CP INITIATION** |
|  +0.00 | 00:02:30.118 | Germany            | Germany            | 89 | Carry           |   -   | [9.0, 6.1]      | Carry                     | (v2.6 Regain Event) |
|  +0.77 | 00:02:30.889 | Germany            | Germany            | 89 | Pass            |   -   | [14.5, 7.6]     | -> Thomas Müller          |  |
|  +1.34 | 00:02:31.455 | Germany            | Germany            | 89 | Ball Receipt*   |   -   | [25.8, 8.0]     | Controlled Receipt        |  |
|  +1.34 | 00:02:31.455 | Germany            | Germany            | 89 | Carry           |   -   | [25.8, 8.0]     | Carry                     |  |
|  +1.38 | 00:02:31.495 | Germany            | Germany            | 89 | Pass            |   -   | [25.8, 8.0]     | -> Serge Gnabry           |  |
|  +4.36 | 00:02:34.476 | Germany            | Germany            | 89 | Ball Receipt*   |   -   | [2.9, 13.7]     | Controlled Receipt        |  |
|  +4.36 | 00:02:34.476 | Germany            | Germany            | 89 | Carry           |   -   | [2.9, 13.7]     | Carry                     |  |
|  +5.25 | 00:02:35.373 | Portugal           | Germany            | 89 | Pressure        |   -   | [113.0, 63.1]   |                           |  |
|  +6.48 | 00:02:36.593 | Germany            | Germany            | 89 | Pass            |   -   | [6.2, 13.5]     | Incomplete (Incomplete)   |  |
|  +7.54 | 00:02:37.655 | Germany            | Germany            | 89 | Ball Receipt*   |   -   | [30.5, 11.5]    | Incomplete Receipt (Incomplete) |  |
|  +7.54 | 00:02:37.655 | Portugal           | Portugal           | 90 | Pass            |  Yes  | [92.4, 61.2]    | -> Nélson Cabral          | **OPPONENT LAST CONTROL** |

---

### Case 7: Episode `3794686_p124_87a4502a`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.16 | 00:20:04.786 | Spain              | Spain              | 123 | Ball Receipt*   |   -   | [48.8, 66.6]    | Controlled Receipt        |  |
|  -2.16 | 00:20:04.786 | Spain              | Spain              | 123 | Carry           |   -   | [48.8, 66.6]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.44 | 00:20:05.505 | Spain              | Spain              | 123 | Pass            |   -   | [48.8, 66.6]    | Incomplete (Incomplete)   |  |
|  -0.42 | 00:20:06.529 | Spain              | Spain              | 123 | Pressure        |   -   | [57.3, 57.2]    |                           |  |
|  +0.00 | 00:20:06.947 | Croatia            | Croatia            | 124 | Interception    |  Yes  | [56.9, 24.0]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:20:06.947 | Croatia            | Croatia            | 124 | Carry           |   -   | [56.9, 24.0]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.04 | 00:20:06.986 | Croatia            | Croatia            | 124 | Dispossessed    |   -   | [57.8, 22.9]    | Dispossessed              |  |
|  +0.04 | 00:20:06.986 | Spain              | Croatia            | 124 | Duel            |  Yes  | [62.3, 57.2]    | Tackle, Lost In Play      |  |
|  +1.65 | 00:20:08.596 | Croatia            | Croatia            | 124 | Ball Recovery   |   -   | [46.4, 26.4]    |                           |  |
|  +1.65 | 00:20:08.596 | Croatia            | Croatia            | 124 | Carry           |   -   | [46.4, 26.4]    | Carry                     |  |
|  +2.96 | 00:20:09.910 | Croatia            | Croatia            | 124 | Pass            |   -   | [46.4, 26.4]    | -> Ante Rebić             |  |
|  +5.07 | 00:20:12.012 | Croatia            | Croatia            | 124 | Ball Receipt*   |   -   | [78.3, 2.0]     | Controlled Receipt        |  |
|  +5.07 | 00:20:12.012 | Croatia            | Croatia            | 124 | Carry           |   -   | [78.3, 2.0]     | Carry                     |  |

---

### Case 8: Episode `3794686_p137_418595ae`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.69 | 00:27:07.940 | Spain              | Croatia            | 50 | Clearance       |   -   | [38.7, 62.5]    |                           |  |
|  +5.00 | 00:27:12.246 | Croatia            | Croatia            | 51 | Pass            |   -   | [75.6, 0.1]     | -> Ante Rebić             |  |
|  +6.18 | 00:27:13.431 | Spain              | Croatia            | 51 | Pressure        |   -   | [25.4, 70.5]    |                           |  |
|  +6.54 | 00:27:13.791 | Croatia            | Croatia            | 51 | Ball Receipt*   |   -   | [94.7, 9.6]     | Controlled Receipt        |  |
|  +6.54 | 00:27:13.791 | Croatia            | Croatia            | 51 | Carry           |   -   | [94.7, 9.6]     | Carry                     |  |
|  +6.69 | 00:27:13.932 | Croatia            | Croatia            | 51 | Miscontrol      |   -   | [94.7, 9.6]     | Miscontrol                |  |
|  +7.56 | 00:27:14.803 | Croatia            | Croatia            | 51 | Pressure        |   -   | [93.1, 7.9]     |                           |  |
|  +7.82 | 00:27:15.064 | Spain              | Spain              | 52 | Pass            |   -   | [28.9, 73.5]    | -> César Azpilicu         | **PRESSING-TEAM FIRST CONTROL** |
|  -1.88 | 00:27:05.367 | Croatia            | Croatia            | 136 | Ball Receipt*   |   -   | [105.3, 11.3]   | Controlled Receipt        |  |
|  -1.88 | 00:27:05.367 | Croatia            | Croatia            | 136 | Carry           |   -   | [105.3, 11.3]   | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.80 | 00:27:06.446 | Spain              | Croatia            | 136 | Pressure        |   -   | [16.1, 58.9]    |                           |  |
|  +0.00 | 00:27:07.246 | Croatia            | Croatia            | 136 | Dispossessed    |   -   | [106.6, 20.5]   | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:27:07.246 | Spain              | Spain              | 137 | Duel            |  Yes  | [13.5, 59.6]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:27:07.246 | Spain              | Spain              | 137 | Carry           |   -   | [13.5, 59.6]    | Carry                     | (v2.6 Regain Event) |
|  +2.93 | 00:27:10.174 | Croatia            | Spain              | 137 | Foul Committed  |  Yes  | [107.1, 22.7]   |                           |  |
|  +2.93 | 00:27:10.174 | Spain              | Spain              | 137 | Foul Won        |   -   | [13.0, 57.4]    |                           |  |
|  +3.89 | 00:27:11.141 | Spain              | Spain              | 137 | Tactical Shift  |   -   | -               |                           |  |

---

### Case 9: Episode `3794686_p163_1bb72b50`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.06 | 00:42:56.033 | Croatia            | Croatia            | 80 | Ball Receipt*   |   -   | [56.7, 57.4]    | Controlled Receipt        |  |
|  -2.06 | 00:42:56.033 | Croatia            | Croatia            | 80 | Carry           |   -   | [56.7, 57.4]    | Carry                     |  |
|  +0.88 | 00:42:58.969 | Spain              | Croatia            | 80 | Pressure        |   -   | [64.0, 24.5]    |                           |  |
|  +1.16 | 00:42:59.252 | Croatia            | Croatia            | 80 | Pass            |   -   | [56.1, 52.4]    | -> Nikola Vlašić          | **PRESSING-TEAM FIRST CONTROL** |
|  +1.84 | 00:42:59.932 | Spain              | Croatia            | 80 | Pressure        |   -   | [49.2, 28.5]    |                           |  |
|  +2.07 | 00:43:00.162 | Croatia            | Croatia            | 80 | Ball Receipt*   |   -   | [70.9, 51.6]    | Controlled Receipt        |  |
|  +2.07 | 00:43:00.162 | Croatia            | Croatia            | 80 | Carry           |   -   | [70.9, 51.6]    | Carry                     |  |
|  +5.15 | 00:43:03.241 | Croatia            | Croatia            | 80 | Pass            |   -   | [78.3, 73.5]    | -> Josip Juranovi         |  |
|  +6.56 | 00:43:04.646 | Croatia            | Croatia            | 80 | Ball Receipt*   |   -   | [91.1, 78.2]    | Controlled Receipt        |  |
|  +6.56 | 00:43:04.646 | Croatia            | Croatia            | 80 | Carry           |   -   | [91.1, 78.2]    | Carry                     |  |
|  -2.95 | 00:42:55.135 | Croatia            | Spain              | 162 | Pressure        |   -   | [21.1, 19.0]    |                           |  |
|  -2.20 | 00:42:55.891 | Spain              | Spain              | 162 | Ball Receipt*   |   -   | [95.5, 61.8]    | Controlled Receipt        |  |
|  -2.20 | 00:42:55.891 | Spain              | Spain              | 162 | Carry           |   -   | [95.5, 61.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:42:58.090 | Spain              | Spain              | 162 | Dispossessed    |   -   | [93.8, 70.3]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:42:58.090 | Croatia            | Croatia            | 163 | Duel            |  Yes  | [26.3, 9.8]     | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:42:58.090 | Croatia            | Croatia            | 163 | Carry           |   -   | [26.3, 9.8]     | Carry                     | (v2.6 Regain Event) |
|  +1.42 | 00:42:59.514 | Spain              | Croatia            | 163 | Pressure        |  Yes  | [90.3, 71.6]    |                           |  |
|  +4.52 | 00:43:02.612 | Croatia            | Croatia            | 163 | Pass            |   -   | [57.5, 7.4]     | -> Mislav Oršić           |  |
|  +5.82 | 00:43:03.906 | Croatia            | Croatia            | 163 | Ball Receipt*   |   -   | [66.7, 2.8]     | Controlled Receipt        |  |
|  +5.82 | 00:43:03.906 | Croatia            | Croatia            | 163 | Carry           |   -   | [66.7, 2.8]     | Carry                     |  |
|  +6.30 | 00:43:04.385 | Spain              | Croatia            | 163 | Pressure        |   -   | [48.0, 78.8]    |                           |  |
|  +6.86 | 00:43:04.945 | Croatia            | Croatia            | 163 | Dispossessed    |   -   | [69.0, 0.7]     | Dispossessed              |  |
|  +6.86 | 00:43:04.945 | Spain              | Croatia            | 163 | Duel            |   -   | [51.1, 79.4]    | Tackle, Lost Out          |  |

---

### Case 10: Episode `3788762_p153_6baa23d9`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.97 | 00:44:58.924 | Poland             | Poland             | 74 | Ball Receipt*   |   -   | [78.1, 71.8]    | Incomplete Receipt (Incomplete) |  |
|  -2.97 | 00:44:58.924 | Spain              | Spain              | 75 | Pass            |   -   | [44.6, 16.6]    | -> Álvaro Borja M         |  |
|  -1.20 | 00:45:00.701 | Poland             | Spain              | 75 | Pressure        |  Yes  | [52.7, 72.0]    |                           |  |
|  -0.56 | 00:45:01.338 | Spain              | Spain              | 75 | Ball Receipt*   |   -   | [66.8, 10.8]    | Controlled Receipt        |  |
|  -0.56 | 00:45:01.338 | Spain              | Spain              | 75 | Carry           |   -   | [66.8, 10.8]    | Carry                     |  |
|  -0.55 | 00:45:01.342 | Spain              | Spain              | 75 | Pass            |   -   | [66.4, 9.1]     | -> Daniel Olmo Ca         |  |
|  +0.28 | 00:45:02.179 | Spain              | Spain              | 75 | Ball Receipt*   |   -   | [59.1, 10.4]    | Controlled Receipt        |  |
|  +0.28 | 00:45:02.179 | Spain              | Spain              | 75 | Carry           |   -   | [59.1, 10.4]    | Carry                     |  |
|  +0.56 | 00:45:02.457 | Spain              | Spain              | 75 | Pass            |   -   | [59.1, 10.4]    | -> Álvaro Borja M         |  |
|  +1.80 | 00:45:03.694 | Poland             | Spain              | 75 | Pressure        |  Yes  | [56.7, 64.6]    |                           |  |
|  +2.94 | 00:45:04.837 | Spain              | Spain              | 75 | Ball Receipt*   |   -   | [64.2, 14.1]    | Controlled Receipt        |  |
|  +2.94 | 00:45:04.837 | Spain              | Spain              | 75 | Carry           |   -   | [64.2, 14.1]    | Carry                     |  |
|  +5.22 | 00:45:07.118 | Spain              | Spain              | 75 | Pass            |   -   | [63.4, 16.6]    | -> Rodrigo Hernán         |  |
|  +5.84 | 00:45:07.735 | Spain              | Spain              | 75 | Ball Receipt*   |   -   | [53.5, 16.6]    | Controlled Receipt        |  |
|  +5.84 | 00:45:07.735 | Spain              | Spain              | 75 | Carry           |   -   | [53.5, 16.6]    | Carry                     |  |
|  +6.27 | 00:45:08.165 | Poland             | Spain              | 75 | Pressure        |   -   | [67.4, 61.6]    |                           |  |
|  +7.10 | 00:45:08.996 | Spain              | Spain              | 75 | Pass            |   -   | [50.1, 15.1]    | -> Aymeric Laport         |  |
|  -2.61 | 00:44:59.291 | Poland             | Spain              | 152 | Pressure        |   -   | [79.3, 16.1]    |                           |  |
|  -2.38 | 00:44:59.518 | Spain              | Spain              | 152 | Pass            |   -   | [40.8, 68.1]    | -> Pablo Sarabia          |  |
|  -0.95 | 00:45:00.942 | Spain              | Spain              | 152 | Ball Receipt*   |   -   | [53.8, 46.1]    | Controlled Receipt        |  |
|  -0.95 | 00:45:00.942 | Spain              | Spain              | 152 | Carry           |   -   | [53.8, 46.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.47 | 00:45:01.432 | Poland             | Spain              | 152 | Pressure        |   -   | [65.3, 37.1]    |                           |  |
|  +0.00 | 00:45:01.897 | Spain              | Spain              | 152 | Dribble         |   -   | [55.0, 43.2]    | Incomplete                |  |
|  +0.00 | 00:45:01.897 | Poland             | Poland             | 153 | Duel            |  Yes  | [65.1, 36.9]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:45:01.897 | Poland             | Poland             | 153 | Carry           |   -   | [65.1, 36.9]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.49 | 00:45:03.391 | Spain              | Poland             | 153 | Pressure        |  Yes  | [56.7, 44.9]    |                           |  |
|  +1.99 | 00:45:03.887 | Poland             | Poland             | 153 | Pass            |   -   | [61.9, 31.8]    | -> Bartosz Beresz         |  |
|  +2.80 | 00:45:04.700 | Poland             | Poland             | 153 | Ball Receipt*   |   -   | [55.2, 39.0]    | Controlled Receipt        |  |
|  +2.80 | 00:45:04.700 | Poland             | Poland             | 153 | Pass            |   -   | [55.2, 39.0]    | -> Kamil Glik             |  |
|  +4.04 | 00:45:05.933 | Poland             | Poland             | 153 | Ball Receipt*   |   -   | [46.2, 31.6]    | Controlled Receipt        |  |
|  +4.04 | 00:45:05.933 | Poland             | Poland             | 153 | Pass            |   -   | [47.0, 31.6]    | -> Tymoteusz Puch         |  |
|  +5.46 | 00:45:07.354 | Poland             | Poland             | 153 | Ball Receipt*   |   -   | [50.8, 7.7]     | Controlled Receipt        |  |
|  +5.46 | 00:45:07.354 | Poland             | Poland             | 153 | Carry           |   -   | [50.8, 7.7]     | Carry                     |  |
|  +6.30 | 00:45:08.198 | Spain              | Poland             | 153 | Pressure        |   -   | [64.7, 71.5]    |                           |  |
|  +7.58 | 00:45:09.473 | Poland             | Poland             | 153 | Pass            |   -   | [55.2, 2.8]     | Incomplete (Incomplete)   |  |
|  +7.83 | 00:45:09.726 | Spain              | Poland             | 153 | Block           |   -   | [63.2, 76.5]    |                           |  |

---

### Case 11: Episode `3788762_p162_591673eb`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.92 | 00:48:52.017 | Spain              | Spain              | 161 | Pass            |   -   | [105.5, 72.4]   | -> Pablo Sarabia          |  |
|  -1.29 | 00:48:52.647 | Spain              | Spain              | 161 | Ball Receipt*   |   -   | [102.1, 55.5]   | Controlled Receipt        |  |
|  -1.29 | 00:48:52.647 | Spain              | Spain              | 161 | Carry           |   -   | [102.1, 55.5]   | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.53 | 00:48:53.402 | Poland             | Spain              | 161 | Pressure        |   -   | [20.7, 26.7]    |                           |  |
|  +0.00 | 00:48:53.934 | Spain              | Spain              | 161 | Dribble         |   -   | [100.4, 56.0]   | Incomplete                |  |
|  +0.00 | 00:48:53.934 | Poland             | Poland             | 162 | Duel            |  Yes  | [19.7, 24.1]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:48:53.934 | Poland             | Poland             | 162 | Carry           |   -   | [19.7, 24.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.05 | 00:48:55.987 | Spain              | Poland             | 162 | Pressure        |  Yes  | [92.4, 54.6]    |                           |  |
|  +2.90 | 00:48:56.837 | Spain              | Poland             | 162 | Foul Committed  |  Yes  | [86.9, 56.0]    |                           |  |
|  +2.90 | 00:48:56.837 | Poland             | Poland             | 162 | Foul Won        |   -   | [33.2, 24.1]    |                           |  |

---

### Case 12: Episode `3788762_p64_c67f351f`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.85 | 00:40:13.258 | Poland             | Spain              | 64 | Ball Receipt*   |   -   | [40.9, 36.5]    | Controlled Receipt        |  |
|  -1.85 | 00:40:13.258 | Poland             | Spain              | 64 | Carry           |   -   | [40.9, 36.5]    | Carry                     |  |
|  -0.88 | 00:40:14.230 | Poland             | Spain              | 64 | Pass            |   -   | [41.1, 38.0]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:40:15.108 | Poland             | Spain              | 64 | Ball Receipt*   |   -   | [29.1, 32.5]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:40:15.108 | Spain              | Spain              | 64 | Interception    |  Yes  | [88.2, 45.7]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:40:15.108 | Spain              | Spain              | 64 | Carry           |   -   | [88.2, 45.7]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.38 | 00:40:15.486 | Spain              | Spain              | 64 | Dribble         |   -   | [91.0, 45.9]    | Incomplete                |  |
|  +0.38 | 00:40:15.486 | Poland             | Poland             | 65 | Duel            |  Yes  | [29.1, 34.2]    | Tackle, Success In Play   |  |
|  +2.56 | 00:40:17.673 | Spain              | Poland             | 65 | Pressure        |  Yes  | [105.9, 32.9]   |                           |  |
|  +3.59 | 00:40:18.693 | Poland             | Poland             | 65 | Ball Recovery   |   -   | [11.4, 52.8]    |                           |  |
|  +3.59 | 00:40:18.693 | Poland             | Poland             | 65 | Carry           |   -   | [11.4, 52.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.34 | 00:40:15.447 | Poland             | Poland             | 140 | Pressure        |   -   | [79.3, 54.2]    |                           |  |
|  +1.20 | 00:40:16.312 | Spain              | Spain              | 141 | Pass            |   -   | [38.9, 28.0]    | -> Unai Simón Men         |  |
|  +3.54 | 00:40:18.650 | Spain              | Spain              | 141 | Ball Receipt*   |   -   | [6.8, 40.8]     | Controlled Receipt        |  |
|  +3.54 | 00:40:18.650 | Spain              | Spain              | 141 | Carry           |   -   | [6.8, 40.8]     | Carry                     |  |
|  +4.65 | 00:40:19.756 | Spain              | Spain              | 141 | Pass            |   -   | [6.8, 40.8]     | -> Aymeric Laport         |  |
|  +6.41 | 00:40:21.522 | Spain              | Spain              | 141 | Ball Receipt*   |   -   | [16.7, 48.3]    | Controlled Receipt        |  |
|  +6.41 | 00:40:21.522 | Spain              | Spain              | 141 | Carry           |   -   | [16.7, 48.3]    | Carry                     |  |

---

### Case 13: Episode `3788762_p56_7b2c46ca`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.38 | 00:34:22.077 | Spain              | Spain              | 55 | Pass            |   -   | [67.7, 20.9]    | -> Daniel Olmo Ca         |  |
|  -1.83 | 00:34:22.620 | Spain              | Spain              | 55 | Ball Receipt*   |   -   | [69.8, 13.4]    | Controlled Receipt        |  |
|  -1.83 | 00:34:22.620 | Spain              | Spain              | 55 | Carry           |   -   | [69.8, 13.4]    | Carry                     |  |
|  -1.03 | 00:34:23.423 | Spain              | Spain              | 55 | Pass            |   -   | [70.2, 17.0]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:34:24.454 | Spain              | Spain              | 55 | Ball Receipt*   |   -   | [70.0, 3.4]     | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:34:24.454 | Poland             | Poland             | 56 | Interception    |  Yes  | [49.9, 73.1]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:34:24.454 | Poland             | Poland             | 56 | Carry           |   -   | [49.9, 73.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.53 | 00:34:24.985 | Spain              | Poland             | 56 | Pressure        |  Yes  | [71.3, 5.9]     |                           |  |
|  +5.99 | 00:34:30.441 | Poland             | Poland             | 56 | Pass            |   -   | [79.4, 61.8]    | -> Robert Lewando         |  |
|  +7.42 | 00:34:31.874 | Poland             | Poland             | 56 | Ball Receipt*   |   -   | [105.1, 60.7]   | Controlled Receipt        |  |
|  +7.42 | 00:34:31.874 | Poland             | Poland             | 56 | Carry           |   -   | [105.1, 60.7]   | Carry                     |  |
|  -1.98 | 00:34:22.472 | Poland             | Poland             | 132 | Pass            |   -   | [8.8, 43.1]     | Incomplete (Incomplete)   |  |
|  -0.89 | 00:34:23.564 | Spain              | Spain              | 133 | Ball Recovery   |   -   | [70.2, 75.1]    |                           |  |
|  +2.03 | 00:34:26.488 | Spain              | Spain              | 133 | Pass            |   -   | [69.3, 76.1]    | -> Pablo Sarabia          |  |
|  +2.68 | 00:34:27.130 | Poland             | Spain              | 133 | Pressure        |   -   | [40.7, 14.9]    |                           |  |
|  +2.76 | 00:34:27.210 | Spain              | Spain              | 133 | Ball Receipt*   |   -   | [77.2, 72.4]    | Controlled Receipt        |  |
|  +2.76 | 00:34:27.210 | Spain              | Spain              | 133 | Carry           |   -   | [77.2, 72.4]    | Carry                     |  |
|  +2.86 | 00:34:27.318 | Spain              | Spain              | 133 | Pass            |   -   | [76.5, 65.4]    | -> Rodrigo Hernán         |  |
|  +3.99 | 00:34:28.443 | Spain              | Spain              | 133 | Ball Receipt*   |   -   | [70.5, 71.2]    | Controlled Receipt        |  |
|  +3.99 | 00:34:28.443 | Spain              | Spain              | 133 | Carry           |   -   | [70.5, 71.2]    | Carry                     |  |
|  +4.62 | 00:34:29.075 | Spain              | Spain              | 133 | Pass            |   -   | [70.5, 71.2]    | -> Marcos Llorent         |  |
|  +5.65 | 00:34:30.108 | Spain              | Spain              | 133 | Ball Receipt*   |   -   | [84.5, 76.1]    | Controlled Receipt        |  |
|  +5.65 | 00:34:30.108 | Spain              | Spain              | 133 | Carry           |   -   | [84.5, 76.1]    | Carry                     |  |
|  +6.88 | 00:34:31.329 | Spain              | Spain              | 133 | Pass            |   -   | [84.5, 76.3]    | -> Pablo Sarabia          | **OPPONENT LAST CONTROL** |

---

### Case 14: Episode `3788762_p24_9186bcb7`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.92 | 00:10:43.405 | Poland             | Poland             | 23 | Block           |   -   | [65.3, 69.3]    |                           |  |
|  -1.90 | 00:10:44.422 | Spain              | Poland             | 23 | Pressure        |   -   | [55.2, 12.6]    |                           |  |
|  -1.53 | 00:10:44.799 | Poland             | Poland             | 23 | Pass            |   -   | [65.3, 69.3]    | -> Bartosz Beresz         |  |
|  -0.48 | 00:10:45.843 | Poland             | Poland             | 23 | Ball Receipt*   |   -   | [62.9, 74.6]    | Controlled Receipt        |  |
|  -0.48 | 00:10:45.843 | Poland             | Poland             | 23 | Carry           |   -   | [62.9, 74.6]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.34 | 00:10:45.983 | Poland             | Poland             | 23 | Pass            |   -   | [62.9, 74.6]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:10:46.325 | Poland             | Poland             | 23 | Ball Receipt*   |   -   | [73.6, 75.0]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:10:46.325 | Spain              | Spain              | 24 | Interception    |  Yes  | [51.2, 4.4]     | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:10:46.325 | Spain              | Spain              | 24 | Carry           |   -   | [51.2, 4.4]     | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.14 | 00:10:47.470 | Spain              | Spain              | 24 | Pass            |   -   | [54.0, 3.4]     | -> Álvaro Borja M         |  |
|  +2.29 | 00:10:48.613 | Spain              | Spain              | 24 | Ball Receipt*   |   -   | [68.3, 11.3]    | Controlled Receipt        |  |
|  +2.29 | 00:10:48.613 | Spain              | Spain              | 24 | Carry           |   -   | [68.3, 11.3]    | Carry                     |  |
|  +2.66 | 00:10:48.990 | Poland             | Spain              | 24 | Pressure        |  Yes  | [49.7, 66.3]    |                           |  |
|  +3.62 | 00:10:49.945 | Poland             | Spain              | 24 | Pressure        |  Yes  | [54.2, 68.2]    |                           |  |
|  +4.05 | 00:10:50.373 | Spain              | Spain              | 24 | Pass            |   -   | [65.7, 7.6]     | -> Pedro González         |  |
|  +4.61 | 00:10:50.934 | Spain              | Spain              | 24 | Ball Receipt*   |   -   | [62.1, 11.5]    | Controlled Receipt        |  |
|  +4.61 | 00:10:50.934 | Spain              | Spain              | 24 | Carry           |   -   | [62.1, 11.5]    | Carry                     |  |
|  +5.05 | 00:10:51.377 | Poland             | Spain              | 24 | Pressure        |   -   | [56.1, 70.3]    |                           |  |
|  +5.61 | 00:10:51.936 | Poland             | Spain              | 24 | Foul Committed  |   -   | [59.1, 68.8]    |                           |  |
|  +5.61 | 00:10:51.936 | Spain              | Spain              | 24 | Foul Won        |   -   | [61.0, 11.3]    |                           |  |

---

### Case 15: Episode `3788762_p14_9bab7759`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.13 | 00:04:43.773 | Poland             | Poland             | 14 | Ball Receipt*   |   -   | [64.0, 11.9]    | Controlled Receipt        |  |
|  -2.13 | 00:04:43.773 | Poland             | Poland             | 14 | Carry           |   -   | [64.0, 11.9]    | Carry                     |  |
|  -1.71 | 00:04:44.192 | Spain              | Poland             | 14 | Pressure        |   -   | [53.7, 68.2]    |                           |  |
|  -1.12 | 00:04:44.782 | Poland             | Poland             | 14 | Dribble         |   -   | [66.1, 10.6]    | Incomplete                |  |
|  -1.12 | 00:04:44.782 | Spain              | Poland             | 14 | Duel            |   -   | [54.0, 69.5]    | Tackle, Won               |  |
|  -1.12 | 00:04:44.782 | Spain              | Poland             | 14 | Carry           |   -   | [54.0, 69.5]    | Carry                     |  |
|  +0.00 | 00:04:45.901 | Spain              | Poland             | 14 | Dispossessed    |   -   | [51.4, 68.4]    | Dispossessed              |  |
|  +0.00 | 00:04:45.901 | Poland             | Poland             | 14 | Duel            |  Yes  | [68.7, 11.7]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:04:45.901 | Poland             | Poland             | 14 | Carry           |   -   | [68.7, 11.7]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.95 | 00:04:46.851 | Spain              | Poland             | 14 | Foul Committed  |   -   | [51.4, 68.4]    |                           |  |
|  +0.95 | 00:04:46.851 | Poland             | Poland             | 14 | Foul Won        |   -   | [68.7, 11.7]    |                           |  |
|  -2.96 | 00:04:42.941 | Poland             | Spain              | 89 | Pressure        |  Yes  | [112.6, 46.3]   |                           |  |
|  -2.12 | 00:04:43.776 | Spain              | Spain              | 89 | Pass            |   -   | [8.7, 41.1]     | -> Jorge Resurrec         |  |
|  -1.32 | 00:04:44.585 | Poland             | Spain              | 89 | Pressure        |   -   | [99.1, 37.1]    |                           |  |
|  -1.13 | 00:04:44.773 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [21.0, 39.9]    | Controlled Receipt        |  |
|  -1.13 | 00:04:44.773 | Spain              | Spain              | 89 | Carry           |   -   | [21.0, 39.9]    | Carry                     |  |
|  -1.01 | 00:04:44.893 | Spain              | Spain              | 89 | Pass            |   -   | [21.7, 39.4]    | -> Pau Francisco          |  |
|  +0.91 | 00:04:46.813 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [14.0, 22.2]    | Controlled Receipt        |  |
|  +0.91 | 00:04:46.813 | Spain              | Spain              | 89 | Carry           |   -   | [14.0, 22.2]    | Carry                     |  |
|  +0.95 | 00:04:46.853 | Poland             | Spain              | 89 | Foul Committed  |   -   | [99.6, 39.3]    |                           |  |
|  +0.95 | 00:04:46.853 | Spain              | Spain              | 89 | Foul Won        |   -   | [20.5, 40.8]    |                           |  |
|  +1.01 | 00:04:46.907 | Spain              | Spain              | 89 | Pass            |   -   | [14.5, 24.7]    | -> Álvaro Borja M         |  |
|  +3.61 | 00:04:49.514 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [41.8, 50.0]    | Controlled Receipt        |  |
|  +3.61 | 00:04:49.514 | Spain              | Spain              | 89 | Carry           |   -   | [41.8, 50.0]    | Carry                     |  |
|  +3.66 | 00:04:49.558 | Spain              | Spain              | 89 | Pass            |   -   | [43.2, 47.3]    | -> Marcos Llorent         |  |
|  +5.15 | 00:04:51.056 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [35.5, 73.2]    | Controlled Receipt        |  |
|  +5.15 | 00:04:51.056 | Spain              | Spain              | 89 | Carry           |   -   | [35.5, 73.2]    | Carry                     |  |
|  +6.89 | 00:04:52.790 | Spain              | Spain              | 89 | Pass            |   -   | [35.5, 73.2]    | -> Jorge Resurrec         |  |
|  +7.62 | 00:04:53.520 | Poland             | Spain              | 89 | Pressure        |   -   | [72.3, 11.0]    |                           |  |
|  +7.96 | 00:04:53.863 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [46.1, 70.3]    | Controlled Receipt        |  |
|  +7.96 | 00:04:53.863 | Spain              | Spain              | 89 | Carry           |   -   | [46.1, 70.3]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 16: Episode `3794686_p215_349e1bc4`
- **Match**: `3794686` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.27 | 00:05:37.654 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [25.1, 44.9]    | Controlled Receipt        |  |
|  -1.27 | 00:05:37.654 | Spain              | Spain              | 188 | Carry           |   -   | [25.1, 44.9]    | Carry                     |  |
|  -0.23 | 00:05:38.695 | Spain              | Spain              | 188 | Pass            |   -   | [25.1, 45.3]    | -> Fabián Ruiz Pe         |  |
|  +1.35 | 00:05:40.272 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [49.2, 50.3]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +1.35 | 00:05:40.272 | Spain              | Spain              | 188 | Carry           |   -   | [49.2, 50.3]    | Carry                     |  |
|  +3.53 | 00:05:42.454 | Spain              | Spain              | 188 | Pass            |   -   | [49.2, 50.3]    | -> Mikel Oyarzaba         |  |
|  +4.82 | 00:05:43.749 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [62.6, 72.0]    | Controlled Receipt        |  |
|  +4.82 | 00:05:43.749 | Spain              | Spain              | 188 | Carry           |   -   | [62.6, 72.0]    | Carry                     |  |
|  +5.54 | 00:05:44.466 | Spain              | Spain              | 188 | Pass            |   -   | [62.6, 72.0]    | -> César Azpilicu         |  |
|  +6.79 | 00:05:45.718 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [50.3, 66.9]    | Controlled Receipt        |  |
|  +6.79 | 00:05:45.718 | Spain              | Spain              | 188 | Carry           |   -   | [50.3, 66.9]    | Carry                     |  |
|  -1.50 | 00:05:37.425 | Croatia            | Spain              | 215 | Interception    |   -   | [86.1, 68.5]    | Won                       |  |
|  -1.50 | 00:05:37.425 | Croatia            | Spain              | 215 | Carry           |   -   | [86.1, 68.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:05:38.925 | Croatia            | Spain              | 215 | Dispossessed    |   -   | [95.5, 56.9]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:05:38.925 | Spain              | Spain              | 215 | Duel            |  Yes  | [24.6, 23.2]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:05:38.925 | Spain              | Spain              | 215 | Carry           |   -   | [24.6, 23.2]    | Carry                     | (v2.6 Regain Event) |
|  +2.48 | 00:05:41.401 | Spain              | Spain              | 215 | Pass            |   -   | [35.7, 20.3]    | -> Pedro González         |  |
|  +3.44 | 00:05:42.362 | Croatia            | Spain              | 215 | Pressure        |   -   | [83.5, 44.5]    |                           |  |
|  +3.46 | 00:05:42.389 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [39.2, 34.3]    | Controlled Receipt        |  |
|  +3.46 | 00:05:42.389 | Spain              | Spain              | 215 | Carry           |   -   | [39.2, 34.3]    | Carry                     |  |
|  +5.20 | 00:05:44.124 | Spain              | Spain              | 215 | Pass            |   -   | [41.2, 40.2]    | -> Daniel Olmo Ca         |  |
|  +7.19 | 00:05:46.113 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [55.6, 61.1]    | Controlled Receipt        |  |
|  +7.19 | 00:05:46.113 | Spain              | Spain              | 215 | Carry           |   -   | [55.6, 61.1]    | Carry                     |  |

---

### Case 17: Episode `3794686_p202_6764851d`
- **Match**: `3794686` (UEFA Euro) | **Period**: 3
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.92 | 00:15:05.574 | Spain              | Spain              | 27 | Ball Recovery   |   -   | [69.8, 13.3]    |                           |  |
|  -0.92 | 00:15:05.574 | Spain              | Spain              | 27 | Carry           |   -   | [69.8, 13.3]    | Carry                     |  |
|  +5.20 | 00:15:11.690 | Spain              | Spain              | 27 | Pass            |   -   | [70.1, 13.3]    | -> Sergio Busquet         |  |
|  +5.98 | 00:15:12.467 | Spain              | Spain              | 27 | Ball Receipt*   |   -   | [73.4, 22.5]    | Controlled Receipt        |  |
|  +5.98 | 00:15:12.467 | Spain              | Spain              | 27 | Pass            |   -   | [73.4, 22.5]    | -> Pedro González         |  |
|  +7.14 | 00:15:13.628 | Spain              | Spain              | 27 | Ball Receipt*   |   -   | [85.7, 12.4]    | Controlled Receipt        |  |
|  +7.14 | 00:15:13.628 | Spain              | Spain              | 27 | Carry           |   -   | [85.7, 12.4]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.09 | 00:15:09.580 | Croatia            | Croatia            | 116 | Pass            |   -   | [67.1, 0.1]     | -> Duje Ćaleta-Ca         | **PRESSING-TEAM FIRST CONTROL** |
|  +4.90 | 00:15:11.392 | Croatia            | Croatia            | 116 | Ball Receipt*   |   -   | [35.3, 4.4]     | Controlled Receipt        |  |
|  +4.90 | 00:15:11.392 | Croatia            | Croatia            | 116 | Carry           |   -   | [35.3, 4.4]     | Carry                     |  |
|  +5.76 | 00:15:12.257 | Croatia            | Croatia            | 116 | Pass            |   -   | [35.3, 4.4]     | -> Domagoj Vida           |  |
|  -0.50 | 00:15:05.997 | Croatia            | Spain              | 201 | Pressure        |   -   | [14.2, 29.5]    |                           |  |
|  +0.00 | 00:15:06.492 | Spain              | Spain              | 201 | Dribble         |   -   | [107.8, 50.6]   | Incomplete                | **POSSIBLE TRANSITION** |
|  +0.00 | 00:15:06.492 | Croatia            | Croatia            | 202 | Duel            |  Yes  | [12.3, 29.5]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:15:06.492 | Croatia            | Croatia            | 202 | Carry           |   -   | [12.3, 29.5]    | Carry                     | (v2.6 Regain Event) |
|  +0.48 | 00:15:06.969 | Spain              | Croatia            | 202 | Pressure        |  Yes  | [110.4, 47.0]   |                           |  |
|  +1.17 | 00:15:07.662 | Croatia            | Croatia            | 202 | Pass            |   -   | [6.9, 32.1]     | -> Joško Gvardiol         |  |
|  +4.23 | 00:15:10.726 | Croatia            | Croatia            | 202 | Ball Receipt*   |   -   | [2.8, 56.6]     | Controlled Receipt        |  |
|  +4.23 | 00:15:10.726 | Croatia            | Croatia            | 202 | Carry           |   -   | [2.8, 56.6]     | Carry                     |  |
|  +6.15 | 00:15:12.646 | Croatia            | Croatia            | 202 | Pass            |   -   | [7.2, 68.1]     | -> Josip Brekalo          |  |
|  -2.90 | 00:15:03.588 | Croatia            | Croatia            | 223 | Pass            |   -   | [29.4, 18.3]    | -> Duje Ćaleta-Ca         |  |
|  -1.81 | 00:15:04.677 | Croatia            | Croatia            | 223 | Ball Receipt*   |   -   | [20.9, 35.6]    | Controlled Receipt        |  |
|  -1.81 | 00:15:04.677 | Croatia            | Croatia            | 223 | Carry           |   -   | [20.9, 35.6]    | Carry                     |  |
|  -1.01 | 00:15:05.479 | Croatia            | Croatia            | 223 | Pass            |   -   | [21.5, 29.7]    | -> Joško Gvardiol         |  |
|  +0.05 | 00:15:06.538 | Croatia            | Croatia            | 223 | Ball Receipt*   |   -   | [25.3, 19.0]    | Controlled Receipt        |  |
|  +0.05 | 00:15:06.538 | Croatia            | Croatia            | 223 | Carry           |   -   | [25.3, 19.0]    | Carry                     |  |
|  +1.90 | 00:15:08.392 | Croatia            | Croatia            | 223 | Pass            |   -   | [26.8, 21.8]    | -> Marcelo Brozov         |  |
|  +3.38 | 00:15:09.873 | Croatia            | Croatia            | 223 | Ball Receipt*   |   -   | [29.8, 10.9]    | Controlled Receipt        |  |
|  +3.38 | 00:15:09.873 | Croatia            | Croatia            | 223 | Pass            |   -   | [29.8, 10.9]    | -> Duje Ćaleta-Ca         |  |
|  +5.31 | 00:15:11.803 | Croatia            | Croatia            | 223 | Ball Receipt*   |   -   | [23.9, 35.3]    | Controlled Receipt        |  |
|  +5.31 | 00:15:11.803 | Croatia            | Croatia            | 223 | Carry           |   -   | [23.9, 35.3]    | Carry                     |  |
|  +6.81 | 00:15:13.300 | Croatia            | Croatia            | 223 | Pass            |   -   | [24.6, 35.3]    | -> Luka Ivanušec          |  |

---

### Case 18: Episode `3795506_p210_ebedc5a5`
- **Match**: `3795506` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Italy** vs Actual Opponent: **England** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_miscontrol` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.96 | 00:16:36.775 | Italy              | Italy              | 113 | Pass            |   -   | [87.0, 0.1]     | -> Jorge Luiz Fre         |  |
|  -0.34 | 00:16:38.394 | Italy              | Italy              | 113 | Ball Receipt*   |   -   | [78.7, 24.3]    | Controlled Receipt        |  |
|  -0.31 | 00:16:38.422 | Italy              | Italy              | 113 | Pass            |   -   | [78.7, 24.3]    | -> Leonardo Bonuc         |  |
|  +1.13 | 00:16:39.863 | Italy              | Italy              | 113 | Ball Receipt*   |   -   | [60.4, 25.2]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +1.13 | 00:16:39.863 | Italy              | Italy              | 113 | Carry           |   -   | [60.4, 25.2]    | Carry                     |  |
|  +2.60 | 00:16:41.337 | Italy              | Italy              | 113 | Pass            |   -   | [60.4, 25.2]    | -> Marco Verratti         |  |
|  +4.22 | 00:16:42.957 | Italy              | Italy              | 113 | Ball Receipt*   |   -   | [68.0, 21.4]    | Controlled Receipt        |  |
|  +4.22 | 00:16:42.957 | Italy              | Italy              | 113 | Carry           |   -   | [68.0, 21.4]    | Carry                     |  |
|  +7.35 | 00:16:46.085 | Italy              | Italy              | 113 | Pass            |   -   | [83.3, 20.3]    | -> Lorenzo Insign         |  |
|  -2.64 | 00:16:36.099 | England            | England            | 209 | Ball Receipt*   |   -   | [55.7, 60.7]    | Controlled Receipt        |  |
|  -2.64 | 00:16:36.099 | England            | England            | 209 | Carry           |   -   | [55.7, 60.7]    | Carry                     |  |
|  -2.34 | 00:16:36.399 | England            | England            | 209 | Pass            |   -   | [56.6, 62.1]    | -> Jadon Sancho           |  |
|  -1.96 | 00:16:36.773 | England            | England            | 209 | Ball Receipt*   |   -   | [59.2, 68.6]    | Controlled Receipt        |  |
|  -1.96 | 00:16:36.773 | England            | England            | 209 | Carry           |   -   | [59.2, 68.6]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.64 | 00:16:37.096 | Italy              | England            | 209 | Pressure        |   -   | [59.2, 15.4]    |                           |  |
|  -1.40 | 00:16:37.334 | England            | England            | 209 | Miscontrol      |   -   | [58.6, 68.3]    | Miscontrol                | **POSSIBLE TRANSITION** |
|  -0.02 | 00:16:38.710 | England            | England            | 209 | Pressure        |  Yes  | [65.8, 65.3]    |                           |  |
|  +0.00 | 00:16:38.735 | Italy              | Italy              | 210 | Interception    |  Yes  | [57.2, 16.5]    | Won                       | **CP INITIATION** |
|  +0.00 | 00:16:38.735 | Italy              | Italy              | 210 | Carry           |   -   | [57.2, 16.5]    | Carry                     | (v2.6 Regain Event) |
|  +0.41 | 00:16:39.143 | Italy              | Italy              | 210 | Pass            |   -   | [57.2, 16.5]    | -> Alessandro Flo         |  |
|  +0.96 | 00:16:39.697 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [60.7, 9.2]     | Controlled Receipt        |  |
|  +0.96 | 00:16:39.697 | Italy              | Italy              | 210 | Carry           |   -   | [60.7, 9.2]     | Carry                     |  |
|  +1.07 | 00:16:39.805 | Italy              | Italy              | 210 | Pass            |   -   | [60.7, 9.2]     | -> Jorge Luiz Fre         |  |
|  +1.73 | 00:16:40.460 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [63.2, 16.3]    | Controlled Receipt        |  |
|  +1.73 | 00:16:40.460 | Italy              | Italy              | 210 | Carry           |   -   | [63.2, 16.3]    | Carry                     |  |
|  +2.31 | 00:16:41.043 | England            | Italy              | 210 | Pressure        |  Yes  | [52.8, 61.5]    |                           |  |
|  +2.60 | 00:16:41.333 | Italy              | Italy              | 210 | Pass            |   -   | [63.8, 18.0]    | -> Manuel Locatel         |  |
|  +3.34 | 00:16:42.072 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [67.7, 26.3]    | Controlled Receipt        |  |
|  +3.34 | 00:16:42.072 | Italy              | Italy              | 210 | Carry           |   -   | [67.7, 26.3]    | Carry                     |  |
|  +3.46 | 00:16:42.199 | England            | Italy              | 210 | Pressure        |  Yes  | [51.8, 55.8]    |                           |  |
|  +5.03 | 00:16:43.769 | Italy              | Italy              | 210 | Pass            |   -   | [65.8, 29.2]    | -> Giovanni Di Lo         |  |
|  +6.79 | 00:16:45.527 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [54.3, 44.0]    | Controlled Receipt        |  |
|  +6.79 | 00:16:45.527 | Italy              | Italy              | 210 | Carry           |   -   | [54.3, 44.0]    | Carry                     |  |

---

### Case 19: Episode `3795506_p200_3f2c0c2f`
- **Match**: `3795506` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Italy** vs Actual Opponent: **England** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.95 | 00:07:11.636 | Italy              | England            | 98 | Pressure        |   -   | [70.0, 19.4]    |                           |  |
|  -1.77 | 00:07:11.811 | England            | England            | 98 | Ball Receipt*   |   -   | [48.3, 61.5]    | Controlled Receipt        |  |
|  -1.77 | 00:07:11.811 | England            | England            | 98 | Carry           |   -   | [48.3, 61.5]    | Carry                     |  |
|  -1.16 | 00:07:12.425 | England            | England            | 98 | Miscontrol      |   -   | [47.5, 61.3]    | Miscontrol                |  |
|  -0.31 | 00:07:13.274 | Italy              | Italy              | 99 | Ball Recovery   |   -   | [78.1, 16.5]    |                           |  |
|  -0.31 | 00:07:13.274 | Italy              | Italy              | 99 | Carry           |   -   | [78.1, 16.5]    | Carry                     |  |
|  +2.48 | 00:07:16.061 | Italy              | Italy              | 99 | Pass            |   -   | [85.6, 22.3]    | -> Ciro Immobile          | **PRESSING-TEAM FIRST CONTROL** |
|  +3.16 | 00:07:16.740 | Italy              | Italy              | 99 | Ball Receipt*   |   -   | [93.8, 27.2]    | Controlled Receipt        |  |
|  +3.16 | 00:07:16.740 | Italy              | Italy              | 99 | Carry           |   -   | [93.8, 27.2]    | Carry                     |  |
|  +3.70 | 00:07:17.287 | England            | Italy              | 99 | Pressure        |  Yes  | [29.2, 49.5]    |                           |  |
|  +6.50 | 00:07:20.089 | England            | Italy              | 99 | Pressure        |   -   | [38.3, 41.0]    |                           |  |
|  +7.29 | 00:07:20.876 | Italy              | Italy              | 99 | Pass            |   -   | [79.8, 40.9]    | -> Leonardo Bonuc         |  |
|  -1.73 | 00:07:11.854 | England            | England            | 172 | Ball Receipt*   |   -   | [79.7, 6.8]     | Incomplete Receipt (Incomplete) |  |
|  +7.73 | 00:07:21.310 | Italy              | Italy              | 173 | Pass            |   -   | [47.2, 80.0]    | -> Domenico Berar         |  |
|  -2.09 | 00:07:11.495 | England            | England            | 199 | Pass            |   -   | [77.5, 67.9]    | -> Raheem Sterlin         |  |
|  -1.05 | 00:07:12.535 | England            | England            | 199 | Ball Receipt*   |   -   | [93.3, 56.9]    | Controlled Receipt        |  |
|  -1.05 | 00:07:12.535 | England            | England            | 199 | Carry           |   -   | [93.3, 56.9]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.98 | 00:07:12.607 | Italy              | England            | 199 | Pressure        |   -   | [24.6, 22.3]    |                           |  |
|  +0.00 | 00:07:13.584 | England            | England            | 199 | Dispossessed    |   -   | [92.1, 56.1]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:07:13.584 | Italy              | Italy              | 200 | Duel            |  Yes  | [28.0, 24.0]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:07:13.584 | Italy              | Italy              | 200 | Carry           |   -   | [28.0, 24.0]    | Carry                     | (v2.6 Regain Event) |
|  +0.33 | 00:07:13.915 | Italy              | Italy              | 200 | Pass            |   -   | [28.0, 24.0]    | Incomplete (Incomplete)   |  |
|  +2.10 | 00:07:15.682 | Italy              | Italy              | 200 | Pressure        |  Yes  | [36.6, 28.3]    |                           |  |
|  +2.73 | 00:07:16.317 | Italy              | Italy              | 200 | Ball Receipt*   |   -   | [33.7, 25.2]    | Incomplete Receipt (Incomplete) |  |
|  +2.73 | 00:07:16.317 | Italy              | Italy              | 200 | Foul Committed  |  Yes  | [38.9, 32.6]    |                           |  |
|  +2.73 | 00:07:16.317 | England            | Italy              | 200 | Foul Won        |   -   | [81.2, 47.5]    |                           |  |

---

### Case 20: Episode `3795506_p195_232ce3d4`
- **Match**: `3795506` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Italy** vs Actual Opponent: **England** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.03 | 00:02:48.303 | Italy              | Italy              | 92 | Pass            |   -   | [33.7, 33.7]    | -> Jorge Luiz Fre         |  |
|  +0.87 | 00:02:49.208 | Italy              | Italy              | 92 | Ball Receipt*   |   -   | [33.7, 48.3]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +2.57 | 00:02:50.902 | Italy              | Italy              | 92 | Pass            |   -   | [34.6, 52.4]    | -> Giovanni Di Lo         |  |
|  +4.44 | 00:02:52.774 | Italy              | Italy              | 92 | Ball Receipt*   |   -   | [41.2, 72.1]    | Controlled Receipt        |  |
|  +4.44 | 00:02:52.774 | Italy              | Italy              | 92 | Carry           |   -   | [41.2, 72.1]    | Carry                     |  |
|  +5.86 | 00:02:54.196 | Italy              | Italy              | 92 | Pass            |   -   | [48.6, 78.3]    | -> Nicolò Barella         |  |
|  +6.36 | 00:02:54.694 | England            | Italy              | 92 | Pressure        |   -   | [61.5, 10.3]    |                           |  |
|  +6.50 | 00:02:54.835 | Italy              | Italy              | 92 | Ball Receipt*   |   -   | [56.6, 70.7]    | Controlled Receipt        |  |
|  +6.50 | 00:02:54.835 | Italy              | Italy              | 92 | Carry           |   -   | [56.6, 70.7]    | Carry                     |  |
|  +6.54 | 00:02:54.875 | Italy              | Italy              | 92 | Pass            |   -   | [55.8, 69.8]    | -> Jorge Luiz Fre         |  |
|  +7.20 | 00:02:55.538 | Italy              | Italy              | 92 | Ball Receipt*   |   -   | [47.1, 64.9]    | Controlled Receipt        |  |
|  +7.20 | 00:02:55.538 | Italy              | Italy              | 92 | Pass            |   -   | [47.1, 64.9]    | -> Leonardo Bonuc         |  |
|  -2.43 | 00:02:45.900 | England            | England            | 165 | Ball Receipt*   |   -   | [29.5, 76.1]    | Controlled Receipt        |  |
|  -2.43 | 00:02:45.900 | England            | England            | 165 | Carry           |   -   | [29.5, 76.1]    | Carry                     |  |
|  -2.35 | 00:02:45.980 | England            | England            | 165 | Pass            |   -   | [29.5, 75.5]    | -> John Stones            |  |
|  -1.35 | 00:02:46.980 | England            | England            | 165 | Ball Receipt*   |   -   | [21.7, 60.7]    | Controlled Receipt        |  |
|  -1.35 | 00:02:46.980 | England            | England            | 165 | Carry           |   -   | [21.7, 60.7]    | Carry                     |  |
|  +1.29 | 00:02:49.625 | England            | England            | 165 | Pass            |   -   | [22.7, 56.5]    | -> Harry Maguire          |  |
|  +2.66 | 00:02:50.993 | England            | England            | 165 | Ball Receipt*   |   -   | [21.7, 31.7]    | Controlled Receipt        |  |
|  +2.66 | 00:02:50.993 | England            | England            | 165 | Carry           |   -   | [21.7, 31.7]    | Carry                     |  |
|  +5.87 | 00:02:54.205 | England            | England            | 165 | Pass            |   -   | [41.6, 24.2]    | -> Mason Mount            |  |
|  +6.83 | 00:02:55.168 | England            | England            | 165 | Ball Receipt*   |   -   | [58.2, 17.1]    | Controlled Receipt        |  |
|  +6.83 | 00:02:55.168 | England            | England            | 165 | Carry           |   -   | [58.2, 17.1]    | Carry                     |  |
|  -2.26 | 00:02:46.072 | England            | England            | 194 | Dribbled Past   |  Yes  | [89.5, 76.7]    |                           |  |
|  -2.26 | 00:02:46.072 | Italy              | England            | 194 | Dribble         |   -   | [30.6, 3.4]     | Incomplete                |  |
|  -0.91 | 00:02:47.422 | Italy              | England            | 194 | Pressure        |   -   | [35.5, 14.2]    |                           |  |
|  -0.26 | 00:02:48.076 | England            | England            | 194 | Ball Recovery   |   -   | [83.2, 61.3]    |                           |  |
|  -0.26 | 00:02:48.076 | England            | England            | 194 | Carry           |   -   | [83.2, 61.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:02:48.334 | England            | England            | 194 | Dispossessed    |   -   | [86.1, 60.1]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:02:48.334 | Italy              | Italy              | 195 | Duel            |  Yes  | [34.0, 20.0]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:02:48.334 | Italy              | Italy              | 195 | Carry           |   -   | [34.0, 20.0]    | Carry                     | (v2.6 Regain Event) |
|  +0.66 | 00:02:48.997 | England            | Italy              | 195 | Pressure        |  Yes  | [86.4, 56.4]    |                           |  |
|  +1.54 | 00:02:49.872 | England            | Italy              | 195 | Pressure        |  Yes  | [86.9, 51.2]    |                           |  |
|  +2.02 | 00:02:50.353 | England            | Italy              | 195 | Foul Committed  |  Yes  | [88.4, 53.5]    |                           |  |
|  +2.02 | 00:02:50.353 | Italy              | Italy              | 195 | Foul Won        |   -   | [31.7, 26.6]    |                           |  |
|  +2.02 | 00:02:50.353 | Italy              | Italy              | 195 | Carry           |   -   | [31.7, 26.6]    | Carry                     |  |
|  +2.07 | 00:02:50.406 | Italy              | Italy              | 195 | Dispossessed    |   -   | [31.7, 26.6]    | Dispossessed              |  |
|  +2.07 | 00:02:50.406 | England            | Italy              | 195 | Duel            |  Yes  | [88.4, 53.5]    | Tackle, Lost In Play      |  |
|  +4.06 | 00:02:52.395 | Italy              | Italy              | 195 | Pass            |   -   | [18.9, 28.3]    | -> Leonardo Bonuc         |  |
|  +5.22 | 00:02:53.559 | Italy              | Italy              | 195 | Ball Receipt*   |   -   | [18.6, 39.4]    | Controlled Receipt        |  |
|  +5.22 | 00:02:53.559 | Italy              | Italy              | 195 | Carry           |   -   | [18.6, 39.4]    | Carry                     |  |
|  +5.58 | 00:02:53.917 | England            | Italy              | 195 | Pressure        |   -   | [96.6, 41.8]    |                           |  |
|  +6.16 | 00:02:54.491 | Italy              | Italy              | 195 | Pass            |   -   | [22.1, 42.0]    | -> Manuel Locatel         |  |
|  +7.71 | 00:02:56.045 | Italy              | Italy              | 195 | Ball Receipt*   |   -   | [52.9, 28.6]    | Controlled Receipt        |  |
|  +7.71 | 00:02:56.045 | Italy              | Italy              | 195 | Carry           |   -   | [52.9, 28.6]    | Carry                     |  |

---

### Case 21: Episode `3794692_p86_8aa13bbc`
- **Match**: `3794692` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.11 | 00:09:00.592 | Ukraine            | Sweden             | 85 | Pressure        |   -   | [45.9, 2.1]     |                           |  |
|  -1.40 | 00:09:01.309 | Sweden             | Sweden             | 85 | Pass            |   -   | [73.5, 79.0]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:09:02.705 | Ukraine            | Ukraine            | 86 | Interception    |  Yes  | [32.5, 18.4]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:09:02.705 | Ukraine            | Ukraine            | 86 | Carry           |   -   | [32.5, 18.4]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.69 | 00:09:03.399 | Sweden             | Ukraine            | 86 | Pressure        |  Yes  | [88.0, 59.9]    |                           |  |
|  +3.33 | 00:09:06.036 | Ukraine            | Ukraine            | 86 | Pass            |   -   | [38.6, 29.1]    | -> Oleksandr Kara         |  |
|  +5.09 | 00:09:07.794 | Ukraine            | Ukraine            | 86 | Ball Receipt*   |   -   | [36.6, 58.8]    | Controlled Receipt        |  |
|  +5.09 | 00:09:07.794 | Ukraine            | Ukraine            | 86 | Carry           |   -   | [36.6, 58.8]    | Carry                     |  |
|  +6.40 | 00:09:09.110 | Ukraine            | Ukraine            | 86 | Pass            |   -   | [36.2, 61.3]    | -> Serhii Sydorch         |  |
|  +7.41 | 00:09:10.115 | Ukraine            | Ukraine            | 86 | Ball Receipt*   |   -   | [37.3, 47.7]    | Controlled Receipt        |  |
|  +7.41 | 00:09:10.115 | Ukraine            | Ukraine            | 86 | Carry           |   -   | [37.3, 47.7]    | Carry                     |  |

---

### Case 22: Episode `3794692_p97_c6b5e57f`
- **Match**: `3794692` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Sweden** vs Actual Opponent: **Ukraine** (StatsBomb Poss Team: `Sweden`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.18 | 00:16:08.274 | Sweden             | Sweden             | 22 | Pass            |   -   | [43.0, 36.0]    | -> Mikael Lustig          | **PRESSING-TEAM FIRST CONTROL** |
|  +1.95 | 00:16:10.037 | Sweden             | Sweden             | 22 | Ball Receipt*   |   -   | [49.1, 59.8]    | Controlled Receipt        |  |
|  +1.95 | 00:16:10.037 | Sweden             | Sweden             | 22 | Carry           |   -   | [49.1, 59.8]    | Carry                     |  |
|  +2.67 | 00:16:10.757 | Sweden             | Sweden             | 22 | Pass            |   -   | [49.4, 64.4]    | -> Kristoffer Ols         |  |
|  +3.88 | 00:16:11.968 | Sweden             | Sweden             | 22 | Ball Receipt*   |   -   | [48.5, 53.6]    | Controlled Receipt        |  |
|  +3.88 | 00:16:11.968 | Sweden             | Sweden             | 22 | Carry           |   -   | [48.5, 53.6]    | Carry                     |  |
|  +7.07 | 00:16:15.160 | Sweden             | Sweden             | 22 | Pass            |   -   | [48.5, 53.6]    | -> Albin Ekdal            |  |
|  -2.98 | 00:16:05.109 | Ukraine            | Ukraine            | 96 | Ball Receipt*   |   -   | [70.7, 22.0]    | Controlled Receipt        |  |
|  -2.98 | 00:16:05.109 | Ukraine            | Ukraine            | 96 | Carry           |   -   | [70.7, 22.0]    | Carry                     |  |
|  -2.65 | 00:16:05.440 | Ukraine            | Ukraine            | 96 | Pass            |   -   | [72.0, 22.4]    | -> Ruslan Malinov         |  |
|  -2.13 | 00:16:05.956 | Sweden             | Ukraine            | 96 | Pressure        |   -   | [37.5, 60.3]    |                           |  |
|  -2.03 | 00:16:06.063 | Ukraine            | Ukraine            | 96 | Ball Receipt*   |   -   | [82.1, 19.4]    | Controlled Receipt        |  |
|  -2.03 | 00:16:06.063 | Ukraine            | Ukraine            | 96 | Carry           |   -   | [82.1, 19.4]    | Carry                     |  |
|  -2.00 | 00:16:06.094 | Sweden             | Ukraine            | 96 | Dribbled Past   |   -   | [37.6, 62.3]    |                           |  |
|  -2.00 | 00:16:06.094 | Ukraine            | Ukraine            | 96 | Dribble         |   -   | [82.5, 17.8]    | Complete                  |  |
|  -2.00 | 00:16:06.094 | Ukraine            | Ukraine            | 96 | Carry           |   -   | [82.5, 17.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.62 | 00:16:07.473 | Sweden             | Ukraine            | 96 | Pressure        |   -   | [37.6, 73.4]    |                           |  |
|  +0.00 | 00:16:08.091 | Ukraine            | Ukraine            | 96 | Dispossessed    |   -   | [83.6, 5.9]     | Dispossessed              |  |
|  +0.00 | 00:16:08.091 | Sweden             | Sweden             | 97 | Duel            |  Yes  | [36.5, 74.2]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:16:08.091 | Sweden             | Sweden             | 97 | Carry           |   -   | [36.5, 74.2]    | Carry                     | (v2.6 Regain Event) |
|  +2.17 | 00:16:10.257 | Sweden             | Sweden             | 97 | Pass            |   -   | [43.1, 74.2]    | -> Kristoffer Ols         |  |
|  +2.84 | 00:16:10.926 | Sweden             | Sweden             | 97 | Ball Receipt*   |   -   | [38.5, 62.7]    | Controlled Receipt        |  |
|  +2.84 | 00:16:10.926 | Sweden             | Sweden             | 97 | Carry           |   -   | [38.5, 62.7]    | Carry                     |  |
|  +5.04 | 00:16:13.127 | Sweden             | Sweden             | 97 | Pass            |   -   | [47.6, 61.7]    | -> Alexander Isak         |  |
|  +5.85 | 00:16:13.940 | Sweden             | Sweden             | 97 | Ball Receipt*   |   -   | [59.8, 73.8]    | Controlled Receipt        |  |
|  +5.85 | 00:16:13.940 | Sweden             | Sweden             | 97 | Carry           |   -   | [59.8, 73.8]    | Carry                     |  |
|  +7.45 | 00:16:15.537 | Ukraine            | Sweden             | 97 | Pressure        |   -   | [62.7, 7.6]     |                           |  |
|  +7.85 | 00:16:15.942 | Sweden             | Sweden             | 97 | Dispossessed    |   -   | [56.4, 71.5]    | Dispossessed              |  |
|  +7.85 | 00:16:15.942 | Ukraine            | Sweden             | 97 | Duel            |   -   | [63.7, 8.6]     | Tackle, Lost In Play      |  |
|  +1.31 | 00:16:09.400 | Ukraine            | Ukraine            | 141 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +2.19 | 00:16:10.286 | Sweden             | Ukraine            | 141 | Block           |   -   | [6.9, 51.2]     |                           |  |

---

### Case 23: Episode `3794692_p108_df1cddf8`
- **Match**: `3794692` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.73 | 00:23:30.726 | Sweden             | Sweden             | 36 | Pass            |   -   | [54.7, 61.3]    | -> Sebastian Lars         |  |
|  -0.29 | 00:23:32.163 | Sweden             | Sweden             | 36 | Ball Receipt*   |   -   | [56.5, 70.0]    | Controlled Receipt        |  |
|  -0.29 | 00:23:32.163 | Sweden             | Sweden             | 36 | Carry           |   -   | [56.5, 70.0]    | Carry                     |  |
|  +1.31 | 00:23:33.764 | Sweden             | Sweden             | 36 | Pass            |   -   | [42.6, 65.1]    | -> Robin Olsen            |  |
|  +4.60 | 00:23:37.054 | Sweden             | Sweden             | 36 | Ball Receipt*   |   -   | [12.4, 45.0]    | Controlled Receipt        |  |
|  +4.60 | 00:23:37.054 | Sweden             | Sweden             | 36 | Carry           |   -   | [12.4, 45.0]    | Carry                     |  |
|  +6.28 | 00:23:38.736 | Sweden             | Sweden             | 36 | Pass            |   -   | [12.4, 45.0]    | -> Victor Nilsson         |  |
|  +7.44 | 00:23:39.897 | Sweden             | Sweden             | 36 | Ball Receipt*   |   -   | [22.9, 55.2]    | Controlled Receipt        |  |
|  +7.44 | 00:23:39.897 | Sweden             | Sweden             | 36 | Carry           |   -   | [22.9, 55.2]    | Carry                     |  |
|  -1.90 | 00:23:30.551 | Sweden             | Sweden             | 107 | Pass            |   -   | [111.1, 67.3]   | -> Dejan Kulusevs         |  |
|  -1.23 | 00:23:31.220 | Sweden             | Sweden             | 107 | Ball Receipt*   |   -   | [105.2, 58.5]   | Controlled Receipt        |  |
|  -1.23 | 00:23:31.220 | Sweden             | Sweden             | 107 | Carry           |   -   | [105.2, 58.5]   | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.39 | 00:23:32.065 | Ukraine            | Sweden             | 107 | Pressure        |   -   | [11.2, 17.6]    |                           |  |
|  +0.00 | 00:23:32.454 | Sweden             | Sweden             | 107 | Dispossessed    |   -   | [107.6, 63.9]   | Dispossessed              |  |
|  +0.00 | 00:23:32.454 | Ukraine            | Ukraine            | 108 | Duel            |  Yes  | [12.5, 16.2]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:23:32.454 | Ukraine            | Ukraine            | 108 | Carry           |   -   | [12.5, 16.2]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.91 | 00:23:33.367 | Sweden             | Ukraine            | 108 | Pressure        |  Yes  | [103.1, 68.7]   |                           |  |
|  +1.77 | 00:23:34.220 | Sweden             | Ukraine            | 108 | Foul Committed  |  Yes  | [101.3, 69.1]   |                           |  |
|  +1.77 | 00:23:34.220 | Ukraine            | Ukraine            | 108 | Foul Won        |   -   | [18.8, 11.0]    |                           |  |

---

### Case 24: Episode `3794692_p132_66cd77e5`
- **Match**: `3794692` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Sweden** vs Actual Opponent: **Ukraine** (StatsBomb Poss Team: `Sweden`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.18 | 00:46:20.026 | Ukraine            | Sweden             | 132 | Pass            |   -   | [31.6, 65.2]    | Incomplete (Incomplete)   |  |
|  -1.91 | 00:46:20.298 | Ukraine            | Sweden             | 132 | Ball Receipt*   |   -   | [36.9, 56.0]    | Incomplete Receipt (Incomplete) |  |
|  -1.91 | 00:46:20.298 | Sweden             | Sweden             | 132 | Interception    |   -   | [84.6, 19.6]    | Lost In Play              |  |
|  -0.44 | 00:46:21.775 | Sweden             | Sweden             | 132 | Pressure        |   -   | [76.1, 16.3]    |                           |  |
|  -0.13 | 00:46:22.085 | Ukraine            | Sweden             | 132 | Ball Recovery   |   -   | [44.2, 63.8]    |                           |  |
|  -0.13 | 00:46:22.085 | Ukraine            | Sweden             | 132 | Carry           |   -   | [44.2, 63.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:46:22.211 | Ukraine            | Sweden             | 132 | Dribble         |   -   | [46.2, 63.7]    | Incomplete                |  |
|  +0.00 | 00:46:22.211 | Sweden             | Sweden             | 132 | Duel            |  Yes  | [73.9, 16.4]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:46:22.211 | Sweden             | Sweden             | 132 | Carry           |   -   | [73.9, 16.4]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.68 | 00:46:24.886 | Sweden             | Sweden             | 132 | Pass            |   -   | [61.4, 7.6]     | -> Robin Olsen            |  |
|  +5.25 | 00:46:27.465 | Sweden             | Sweden             | 132 | Ball Receipt*   |   -   | [32.8, 30.7]    | Controlled Receipt        |  |
|  +5.25 | 00:46:27.465 | Sweden             | Sweden             | 132 | Carry           |   -   | [32.8, 30.7]    | Carry                     |  |
|  +7.06 | 00:46:29.269 | Sweden             | Sweden             | 132 | Pass            |   -   | [37.6, 38.0]    | -> Emil Krafth            |  |

---

### Case 25: Episode `3788765_p9_4bc1bb1d`
- **Match**: `3788765` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.12 | 00:03:13.286 | Turkey             | Switzerland        | 8 | Pressure        |   -   | [92.5, 35.4]    |                           |  |
|  -1.62 | 00:03:13.779 | Switzerland        | Switzerland        | 8 | Pass            |   -   | [24.2, 39.3]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:03:15.402 | Switzerland        | Switzerland        | 8 | Ball Receipt*   |   -   | [50.7, 30.3]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:03:15.402 | Turkey             | Turkey             | 9 | Interception    |  Yes  | [70.9, 48.5]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:03:15.402 | Turkey             | Turkey             | 9 | Carry           |   -   | [70.9, 48.5]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.44 | 00:03:16.844 | Turkey             | Turkey             | 9 | Pass            |   -   | [72.8, 41.9]    | -> Burak Yılmaz           |  |
|  +2.06 | 00:03:17.462 | Turkey             | Turkey             | 9 | Ball Receipt*   |   -   | [80.5, 40.1]    | Controlled Receipt        |  |
|  +2.06 | 00:03:17.462 | Turkey             | Turkey             | 9 | Carry           |   -   | [80.5, 40.1]    | Carry                     |  |
|  +3.11 | 00:03:18.514 | Switzerland        | Turkey             | 9 | Pressure        |  Yes  | [35.8, 45.3]    |                           |  |
|  +4.48 | 00:03:19.881 | Turkey             | Turkey             | 9 | Dispossessed    |   -   | [88.4, 38.2]    | Dispossessed              |  |
|  +4.48 | 00:03:19.881 | Switzerland        | Turkey             | 9 | Duel            |  Yes  | [31.7, 41.9]    | Tackle, Success In Play   |  |
|  +4.85 | 00:03:20.251 | Switzerland        | Turkey             | 9 | Ball Recovery   |   -   | [30.2, 37.0]    |                           |  |
|  +5.95 | 00:03:21.352 | Turkey             | Turkey             | 9 | Ball Recovery   |   -   | [91.0, 52.8]    |                           |  |
|  +5.95 | 00:03:21.352 | Turkey             | Turkey             | 9 | Carry           |   -   | [91.0, 52.8]    | Carry                     |  |
|  +7.35 | 00:03:22.756 | Turkey             | Turkey             | 9 | Pass            |   -   | [94.6, 50.8]    | -> Cengiz Ünder           |  |
|  -2.38 | 00:03:13.020 | Switzerland        | Switzerland        | 98 | Ball Receipt*   |   -   | [85.5, 28.8]    | Controlled Receipt        |  |
|  -2.38 | 00:03:13.020 | Switzerland        | Switzerland        | 98 | Carry           |   -   | [85.5, 28.8]    | Carry                     |  |
|  -0.90 | 00:03:14.506 | Switzerland        | Switzerland        | 98 | Pass            |   -   | [88.7, 26.7]    | -> Steven Zuber           |  |
|  +0.82 | 00:03:16.225 | Switzerland        | Switzerland        | 98 | Ball Receipt*   |   -   | [106.0, 23.5]   | Controlled Receipt        |  |
|  +0.82 | 00:03:16.225 | Switzerland        | Switzerland        | 98 | Carry           |   -   | [106.0, 23.5]   | Carry                     |  |
|  +1.62 | 00:03:17.025 | Switzerland        | Switzerland        | 98 | Shot            |   -   | [109.4, 24.2]   | Saved                     | **OPPONENT LAST CONTROL** |
|  +2.31 | 00:03:17.710 | Turkey             | Turkey             | 99 | Goal Keeper     |   -   | [2.0, 43.5]     |                           |  |
|  +6.52 | 00:03:21.921 | Turkey             | Turkey             | 100 | Pass            |   -   | [9.7, 37.7]     | -> Mert Müldür            |  |
|  +7.64 | 00:03:23.046 | Turkey             | Turkey             | 100 | Ball Receipt*   |   -   | [14.9, 24.1]    | Controlled Receipt        |  |
|  +7.64 | 00:03:23.046 | Turkey             | Turkey             | 100 | Carry           |   -   | [14.9, 24.1]    | Carry                     |  |

---

### Case 26: Episode `3794692_p154_2d00b8fb`
- **Match**: `3794692` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.29 | 00:02:54.127 | Sweden             | Sweden             | 5 | Pass            |   -   | [82.7, 28.0]    | -> Mikael Lustig          |  |
|  +2.76 | 00:02:56.593 | Sweden             | Sweden             | 5 | Ball Receipt*   |   -   | [82.7, 49.8]    | Controlled Receipt        |  |
|  +2.76 | 00:02:56.593 | Sweden             | Sweden             | 5 | Carry           |   -   | [82.7, 49.8]    | Carry                     |  |
|  +4.16 | 00:02:58.003 | Sweden             | Sweden             | 5 | Pass            |   -   | [89.9, 55.3]    | Incomplete (Incomplete)   |  |
|  +6.16 | 00:02:59.996 | Sweden             | Sweden             | 5 | Ball Receipt*   |   -   | [107.2, 30.7]   | Incomplete Receipt (Incomplete) |  |
|  +6.16 | 00:02:59.996 | Ukraine            | Sweden             | 5 | Goal Keeper     |   -   | [9.0, 48.3]     |                           |  |
|  +7.11 | 00:03:00.950 | Ukraine            | Sweden             | 5 | Clearance       |   -   | [12.0, 53.0]    |                           |  |
|  -1.35 | 00:02:52.484 | Ukraine            | Sweden             | 74 | Pressure        |   -   | [9.6, 58.8]     |                           |  |
|  -1.20 | 00:02:52.638 | Ukraine            | Sweden             | 74 | Dribbled Past   |   -   | [8.6, 58.8]     |                           |  |
|  -1.20 | 00:02:52.638 | Sweden             | Sweden             | 74 | Dribble         |   -   | [111.5, 21.3]   | Complete                  |  |
|  -1.20 | 00:02:52.638 | Sweden             | Sweden             | 74 | Carry           |   -   | [111.5, 21.3]   | Carry                     |  |
|  -0.76 | 00:02:53.080 | Ukraine            | Sweden             | 74 | Pressure        |   -   | [9.6, 57.2]     |                           |  |
|  -0.61 | 00:02:53.230 | Sweden             | Sweden             | 74 | Dribble         |   -   | [110.5, 22.9]   | Incomplete                |  |
|  -0.61 | 00:02:53.230 | Ukraine            | Ukraine            | 75 | Duel            |  Yes  | [9.6, 57.2]     | Tackle, Success In Play   |  |
|  +1.02 | 00:02:54.862 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [9.4, 60.2]     | Incomplete (Incomplete)   |  |
|  +3.23 | 00:02:57.068 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [46.2, 57.4]    | Incomplete Receipt (Incomplete) |  |
|  +3.23 | 00:02:57.068 | Sweden             | Ukraine            | 75 | Interception    |  Yes  | [74.7, 23.3]    | Lost In Play              |  |
|  +3.55 | 00:02:57.385 | Ukraine            | Ukraine            | 75 | Block           |   -   | [46.0, 57.2]    |                           |  |
|  +4.43 | 00:02:58.272 | Sweden             | Ukraine            | 75 | Pressure        |   -   | [78.6, 21.7]    |                           |  |
|  +4.57 | 00:02:58.404 | Sweden             | Ukraine            | 75 | Pressure        |   -   | [79.7, 22.0]    |                           |  |
|  +4.92 | 00:02:58.757 | Ukraine            | Ukraine            | 75 | Ball Recovery   |   -   | [40.8, 57.8]    |                           |  |
|  +4.92 | 00:02:58.757 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [40.8, 57.8]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +5.62 | 00:02:59.454 | Ukraine            | Ukraine            | 75 | Dispossessed    |   -   | [39.0, 56.8]    | Dispossessed              |  |
|  +5.62 | 00:02:59.454 | Sweden             | Ukraine            | 75 | Duel            |   -   | [81.1, 23.3]    | Tackle, Lost In Play      |  |
|  +6.96 | 00:03:00.797 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [37.3, 51.9]    | -> Oleksandr Zinc         |  |
|  -2.44 | 00:02:51.398 | Ukraine            | Ukraine            | 134 | Pass            |   -   | [70.0, 71.2]    | -> Oleksandr Kara         |  |
|  -1.08 | 00:02:52.758 | Ukraine            | Ukraine            | 134 | Ball Receipt*   |   -   | [78.4, 76.8]    | Controlled Receipt        |  |
|  -1.08 | 00:02:52.758 | Ukraine            | Ukraine            | 134 | Carry           |   -   | [78.4, 76.8]    | Carry                     |  |
|  -0.16 | 00:02:53.677 | Ukraine            | Ukraine            | 134 | Pass            |   -   | [78.4, 76.8]    | -> Ruslan Malinov         |  |
|  +0.70 | 00:02:54.542 | Ukraine            | Ukraine            | 134 | Ball Receipt*   |   -   | [75.3, 67.8]    | Controlled Receipt        |  |
|  +0.70 | 00:02:54.542 | Ukraine            | Ukraine            | 134 | Carry           |   -   | [75.3, 67.8]    | Carry                     |  |
|  +2.37 | 00:02:56.205 | Ukraine            | Ukraine            | 134 | Pass            |   -   | [71.3, 63.2]    | -> Oleksandr Zinc         |  |
|  +5.51 | 00:02:59.344 | Ukraine            | Ukraine            | 134 | Ball Receipt*   |   -   | [98.1, 20.0]    | Controlled Receipt        |  |
|  +5.51 | 00:02:59.344 | Ukraine            | Ukraine            | 134 | Carry           |   -   | [98.1, 20.0]    | Carry                     |  |
|  -2.05 | 00:02:51.785 | Ukraine            | Sweden             | 153 | Ball Receipt*   |   -   | [77.7, 64.4]    | Incomplete Receipt (Incomplete) |  |
|  -2.05 | 00:02:51.785 | Sweden             | Sweden             | 153 | Pass            |   -   | [45.7, 14.9]    | -> Robin Quaison          |  |
|  -0.43 | 00:02:53.406 | Ukraine            | Sweden             | 153 | Pressure        |   -   | [56.3, 75.9]    |                           |  |
|  -0.35 | 00:02:53.490 | Sweden             | Sweden             | 153 | Ball Receipt*   |   -   | [64.3, 2.4]     | Controlled Receipt        |  |
|  -0.35 | 00:02:53.490 | Sweden             | Sweden             | 153 | Carry           |   -   | [64.3, 2.4]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:02:53.838 | Sweden             | Sweden             | 153 | Dispossessed    |   -   | [63.3, 3.9]     | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:02:53.838 | Ukraine            | Ukraine            | 154 | Duel            |  Yes  | [56.8, 76.2]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:02:53.838 | Ukraine            | Ukraine            | 154 | Carry           |   -   | [56.8, 76.2]    | Carry                     | (v2.6 Regain Event) |
|  +0.80 | 00:02:54.633 | Sweden             | Ukraine            | 154 | Pressure        |  Yes  | [62.0, 3.2]     |                           |  |
|  +1.18 | 00:02:55.020 | Ukraine            | Ukraine            | 154 | Pass            |   -   | [58.9, 76.9]    | -> Oleksandr Kara         |  |
|  +1.88 | 00:02:55.719 | Ukraine            | Ukraine            | 154 | Ball Receipt*   |   -   | [62.7, 76.2]    | Controlled Receipt        |  |
|  +1.88 | 00:02:55.719 | Ukraine            | Ukraine            | 154 | Carry           |   -   | [62.7, 76.2]    | Carry                     |  |
|  +2.17 | 00:02:56.005 | Sweden             | Ukraine            | 154 | Pressure        |  Yes  | [56.4, 3.9]     |                           |  |
|  +2.94 | 00:02:56.777 | Sweden             | Ukraine            | 154 | Foul Committed  |  Yes  | [53.2, 3.9]     |                           |  |
|  +2.94 | 00:02:56.777 | Ukraine            | Ukraine            | 154 | Foul Won        |   -   | [66.9, 76.2]    |                           |  |

---

### Case 27: Episode `3794692_p160_ccf69029`
- **Match**: `3794692` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.77 | 00:06:19.306 | Ukraine            | Sweden             | 77 | Ball Receipt*   |   -   | [79.0, 24.0]    | Incomplete Receipt (Incomplete) |  |
|  -2.77 | 00:06:19.306 | Sweden             | Sweden             | 77 | Goal Keeper     |   -   | [36.1, 56.7]    |                           |  |
|  +6.54 | 00:06:28.615 | Ukraine            | Ukraine            | 78 | Pass            |   -   | [64.7, 0.1]     | -> Taras Stepanen         | **PRESSING-TEAM FIRST CONTROL** |
|  +7.76 | 00:06:29.836 | Ukraine            | Ukraine            | 78 | Ball Receipt*   |   -   | [56.7, 9.3]     | Controlled Receipt        |  |
|  -2.71 | 00:06:19.370 | Sweden             | Sweden             | 159 | Ball Receipt*   |   -   | [114.5, 77.6]   | Controlled Receipt        |  |
|  -2.71 | 00:06:19.370 | Sweden             | Sweden             | 159 | Carry           |   -   | [114.5, 77.6]   | Carry                     |  |
|  -1.63 | 00:06:20.448 | Ukraine            | Sweden             | 159 | Pressure        |   -   | [3.5, 2.3]      |                           |  |
|  +0.00 | 00:06:22.079 | Sweden             | Sweden             | 159 | Dispossessed    |   -   | [117.1, 78.1]   | Dispossessed              |  |
|  +0.00 | 00:06:22.079 | Ukraine            | Ukraine            | 160 | Duel            |  Yes  | [3.0, 2.0]      | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:06:22.079 | Ukraine            | Ukraine            | 160 | Carry           |   -   | [3.0, 2.0]      | Carry                     | (v2.6 Regain Event) |
|  +1.35 | 00:06:23.426 | Ukraine            | Ukraine            | 160 | Pass            |   -   | [5.6, 2.8]      | -> Evgeny Makaren         |  |
|  +1.92 | 00:06:23.995 | Sweden             | Ukraine            | 160 | Pressure        |  Yes  | [110.3, 72.9]   |                           |  |
|  +2.13 | 00:06:24.207 | Ukraine            | Ukraine            | 160 | Ball Receipt*   |   -   | [9.0, 8.7]      | Controlled Receipt        |  |
|  +2.13 | 00:06:24.207 | Ukraine            | Ukraine            | 160 | Carry           |   -   | [9.0, 8.7]      | Carry                     |  |
|  +2.71 | 00:06:24.785 | Ukraine            | Ukraine            | 160 | Pass            |   -   | [11.6, 11.9]    | -> Oleksandr Zinc         |  |
|  +3.38 | 00:06:25.462 | Ukraine            | Ukraine            | 160 | Ball Receipt*   |   -   | [18.7, 5.1]     | Controlled Receipt        |  |
|  +3.38 | 00:06:25.462 | Ukraine            | Ukraine            | 160 | Carry           |   -   | [18.7, 5.1]     | Carry                     |  |
|  +3.86 | 00:06:25.937 | Sweden             | Ukraine            | 160 | Pressure        |  Yes  | [98.6, 76.0]    |                           |  |
|  +4.43 | 00:06:26.513 | Ukraine            | Ukraine            | 160 | Pass            |   -   | [21.6, 4.1]     | Incomplete (Incomplete)   |  |
|  +4.49 | 00:06:26.572 | Ukraine            | Ukraine            | 160 | Ball Receipt*   |   -   | [22.9, 1.3]     | Incomplete Receipt (Incomplete) |  |
|  +4.49 | 00:06:26.572 | Sweden             | Ukraine            | 160 | Block           |  Yes  | [97.2, 76.7]    |                           |  |
|  +5.25 | 00:06:27.333 | Sweden             | Ukraine            | 160 | Ball Recovery   |   -   | [97.1, 75.7]    |                           |  |
|  +5.25 | 00:06:27.333 | Sweden             | Ukraine            | 160 | Carry           |   -   | [97.1, 75.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +5.35 | 00:06:27.431 | Ukraine            | Ukraine            | 160 | Pressure        |  Yes  | [22.3, 3.9]     |                           |  |
|  +6.32 | 00:06:28.396 | Ukraine            | Ukraine            | 160 | Dribbled Past   |  Yes  | [22.3, 4.4]     |                           |  |
|  +6.32 | 00:06:28.396 | Sweden             | Ukraine            | 160 | Dribble         |   -   | [97.8, 75.7]    | Incomplete                | **POSSIBLE TRANSITION** |
|  +6.39 | 00:06:28.467 | Ukraine            | Ukraine            | 160 | Pressure        |  Yes  | [20.6, 4.5]     |                           |  |
|  +6.53 | 00:06:28.611 | Sweden             | Ukraine            | 160 | Pressure        |   -   | [99.0, 75.7]    |                           |  |
|  +7.08 | 00:06:29.159 | Ukraine            | Ukraine            | 160 | Pass            |   -   | [21.5, 4.4]     | -> Evgeny Makaren         |  |
|  +7.68 | 00:06:29.758 | Ukraine            | Ukraine            | 160 | Ball Receipt*   |   -   | [19.2, 11.0]    | Controlled Receipt        |  |
|  +7.68 | 00:06:29.758 | Ukraine            | Ukraine            | 160 | Carry           |   -   | [19.2, 11.0]    | Carry                     |  |

---

### Case 28: Episode `3795107_p139_ba902b68`
- **Match**: `3795107` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Belgium** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Belgium`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.54 | 00:41:40.481 | Belgium            | Belgium            | 72 | Pass            |   -   | [23.6, 35.4]    | -> Jan Vertonghen         |  |
|  -1.37 | 00:41:41.648 | Belgium            | Belgium            | 72 | Ball Receipt*   |   -   | [21.5, 8.3]     | Controlled Receipt        |  |
|  -1.37 | 00:41:41.648 | Belgium            | Belgium            | 72 | Carry           |   -   | [21.5, 8.3]     | Carry                     |  |
|  +0.49 | 00:41:43.506 | Belgium            | Belgium            | 72 | Pass            |   -   | [27.0, 1.6]     | Incomplete (Incomplete)   |  |
|  +3.06 | 00:41:46.075 | Belgium            | Belgium            | 72 | Ball Receipt*   |   -   | [77.7, 2.1]     | Incomplete Receipt (Incomplete) |  |
|  +3.06 | 00:41:46.075 | Italy              | Italy              | 73 | Pass            |   -   | [44.7, 75.5]    | -> Jorge Luiz Fre         |  |
|  +4.16 | 00:41:47.182 | Italy              | Italy              | 73 | Ball Receipt*   |   -   | [54.2, 75.7]    | Controlled Receipt        |  |
|  +4.16 | 00:41:47.182 | Italy              | Italy              | 73 | Pass            |   -   | [53.1, 75.9]    | -> Nicolò Barella         |  |
|  +5.46 | 00:41:48.479 | Italy              | Italy              | 73 | Ball Receipt*   |   -   | [63.1, 71.8]    | Controlled Receipt        |  |
|  +5.46 | 00:41:48.479 | Italy              | Italy              | 73 | Carry           |   -   | [63.1, 71.8]    | Carry                     |  |
|  +6.03 | 00:41:49.048 | Italy              | Italy              | 73 | Pass            |   -   | [59.7, 71.6]    | Incomplete (Incomplete)   |  |
|  +6.48 | 00:41:49.494 | Italy              | Italy              | 73 | Ball Receipt*   |   -   | [54.8, 66.3]    | Incomplete Receipt (Incomplete) |  |
|  +6.48 | 00:41:49.494 | Belgium            | Italy              | 73 | Interception    |  Yes  | [64.0, 9.8]     | Lost In Play              |  |
|  +6.98 | 00:41:49.996 | Belgium            | Italy              | 73 | Pressure        |  Yes  | [66.4, 13.4]    |                           |  |
|  +7.30 | 00:41:50.318 | Italy              | Italy              | 73 | Ball Recovery   |   -   | [55.0, 65.2]    |                           |  |
|  +7.30 | 00:41:50.318 | Italy              | Italy              | 73 | Carry           |   -   | [55.0, 65.2]    | Carry                     |  |
|  +7.44 | 00:41:50.455 | Italy              | Italy              | 73 | Dribble         |   -   | [54.8, 66.0]    | Incomplete                |  |
|  +7.44 | 00:41:50.455 | Belgium            | Italy              | 73 | Duel            |  Yes  | [65.3, 14.1]    | Tackle, Won               |  |
|  +7.44 | 00:41:50.455 | Belgium            | Italy              | 73 | Carry           |   -   | [65.3, 14.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  -1.33 | 00:41:41.687 | Italy              | Italy              | 138 | Ball Receipt*   |   -   | [91.6, 16.9]    | Controlled Receipt        |  |
|  -1.33 | 00:41:41.687 | Italy              | Italy              | 138 | Carry           |   -   | [91.6, 16.9]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.10 | 00:41:41.916 | Belgium            | Italy              | 138 | Pressure        |   -   | [22.3, 62.7]    |                           |  |
|  +0.00 | 00:41:43.017 | Italy              | Italy              | 138 | Dispossessed    |   -   | [94.5, 22.9]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:41:43.017 | Belgium            | Belgium            | 139 | Duel            |  Yes  | [25.6, 57.2]    | Tackle, Won               | **CP INITIATION** |
|  +0.00 | 00:41:43.017 | Belgium            | Belgium            | 139 | Carry           |   -   | [25.6, 57.2]    | Carry                     | (v2.6 Regain Event) |
|  +1.95 | 00:41:44.962 | Italy              | Belgium            | 139 | Pressure        |  Yes  | [107.2, 12.2]   |                           |  |
|  +3.66 | 00:41:46.681 | Italy              | Belgium            | 139 | Foul Committed  |  Yes  | [111.0, 7.9]    |                           |  |
|  +3.66 | 00:41:46.681 | Belgium            | Belgium            | 139 | Foul Won        |   -   | [9.1, 72.2]     |                           |  |

---

### Case 29: Episode `3795107_p129_1dec4643`
- **Match**: `3795107` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Italy** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +1.02 | 00:36:18.780 | Belgium            | Belgium            | 67 | Pass            |   -   | [8.4, 34.2]     | -> Jan Vertonghen         |  |
|  +2.37 | 00:36:20.129 | Belgium            | Belgium            | 67 | Ball Receipt*   |   -   | [11.8, 26.2]    | Controlled Receipt        |  |
|  +2.37 | 00:36:20.129 | Belgium            | Belgium            | 67 | Carry           |   -   | [11.8, 26.2]    | Carry                     |  |
|  -1.92 | 00:36:15.841 | Belgium            | Belgium            | 128 | Ball Receipt*   |   -   | [97.8, 77.1]    | Controlled Receipt        |  |
|  -1.92 | 00:36:15.841 | Belgium            | Belgium            | 128 | Carry           |   -   | [97.8, 77.1]    | Carry                     |  |
|  -1.64 | 00:36:16.117 | Belgium            | Belgium            | 128 | Pass            |   -   | [97.8, 77.1]    | -> Kevin De Bruyn         |  |
|  -1.48 | 00:36:16.276 | Italy              | Belgium            | 128 | Pressure        |   -   | [20.0, 15.2]    |                           |  |
|  -1.19 | 00:36:16.570 | Belgium            | Belgium            | 128 | Ball Receipt*   |   -   | [95.4, 64.0]    | Controlled Receipt        |  |
|  -1.19 | 00:36:16.570 | Belgium            | Belgium            | 128 | Carry           |   -   | [95.4, 64.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.15 | 00:36:16.610 | Belgium            | Belgium            | 128 | Pass            |   -   | [96.1, 65.9]    | Incomplete (Incomplete)   |  |
|  -0.07 | 00:36:17.690 | Belgium            | Belgium            | 128 | Pressure        |   -   | [103.4, 67.7]   |                           |  |
|  +0.00 | 00:36:17.757 | Belgium            | Belgium            | 128 | Ball Receipt*   |   -   | [102.8, 71.6]   | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:36:17.757 | Italy              | Italy              | 129 | Interception    |  Yes  | [14.6, 12.4]    | Won                       | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:36:17.757 | Italy              | Italy              | 129 | Carry           |   -   | [14.6, 12.4]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.87 | 00:36:18.624 | Belgium            | Italy              | 129 | Foul Committed  |  Yes  | [104.5, 57.7]   |                           |  |
|  +0.87 | 00:36:18.624 | Italy              | Italy              | 129 | Foul Won        |   -   | [15.6, 22.4]    |                           |  |

---

### Case 30: Episode `3795107_p116_3764f723`
- **Match**: `3795107` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Italy** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `carry` | **First Press Control Candidate**: `Carry`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `carry_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.53 | 00:21:10.412 | Belgium            | Belgium            | 40 | Ball Receipt*   |   -   | [57.2, 8.8]     | Incomplete Receipt (Incomplete) |  |
|  -0.53 | 00:21:10.412 | Italy              | Belgium            | 40 | Clearance       |   -   | [62.6, 67.8]    |                           |  |
|  +2.24 | 00:21:13.185 | Belgium            | Belgium            | 40 | Ball Recovery   |   -   | [30.6, 17.2]    |                           |  |
|  +2.24 | 00:21:13.185 | Belgium            | Belgium            | 40 | Carry           |   -   | [30.6, 17.2]    | Carry                     |  |
|  +3.23 | 00:21:14.169 | Belgium            | Belgium            | 40 | Pass            |   -   | [22.7, 16.0]    | -> Thibaut Courto         |  |
|  +5.46 | 00:21:16.398 | Belgium            | Belgium            | 40 | Ball Receipt*   |   -   | [3.3, 32.9]     | Controlled Receipt        |  |
|  +5.46 | 00:21:16.398 | Belgium            | Belgium            | 40 | Carry           |   -   | [3.3, 32.9]     | Carry                     |  |
|  +6.78 | 00:21:17.716 | Belgium            | Belgium            | 40 | Pass            |   -   | [3.5, 35.4]     | -> Toby Alderweir         |  |
|  +7.59 | 00:21:18.526 | Belgium            | Belgium            | 40 | Ball Receipt*   |   -   | [10.3, 45.5]    | Controlled Receipt        |  |
|  +7.59 | 00:21:18.526 | Belgium            | Belgium            | 40 | Carry           |   -   | [10.3, 45.5]    | Carry                     |  |
|  -2.76 | 00:21:08.180 | Italy              | Italy              | 116 | Ball Receipt*   |   -   | [102.0, 27.1]   | Incomplete Receipt (Incomplete) |  |
|  -2.76 | 00:21:08.180 | Belgium            | Italy              | 116 | Interception    |   -   | [20.6, 53.5]    | Won                       |  |
|  -2.76 | 00:21:08.180 | Belgium            | Italy              | 116 | Carry           |   -   | [20.6, 53.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:21:10.940 | Belgium            | Italy              | 116 | Dribble         |   -   | [32.6, 71.4]    | Incomplete                |  |
|  +0.00 | 00:21:10.940 | Italy              | Italy              | 116 | Duel            |  Yes  | [87.5, 8.7]     | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.00 | 00:21:10.940 | Italy              | Italy              | 116 | Carry           |   -   | [87.5, 8.7]     | Carry                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.37 | 00:21:13.312 | Belgium            | Italy              | 116 | Pressure        |   -   | [33.8, 75.9]    |                           |  |
|  +3.29 | 00:21:14.227 | Belgium            | Italy              | 116 | Foul Committed  |   -   | [28.5, 78.1]    |                           |  |
|  +3.29 | 00:21:14.227 | Italy              | Italy              | 116 | Foul Won        |   -   | [91.6, 2.0]     |                           |  |

---

### Case 31: Episode `3794686_p69_33576c99`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.91 | 00:35:20.167 | Croatia            | Croatia            | 68 | Ball Receipt*   |   -   | [45.4, 67.9]    | Controlled Receipt        |  |
|  -1.91 | 00:35:20.167 | Croatia            | Croatia            | 68 | Carry           |   -   | [45.4, 67.9]    | Carry                     |  |
|  -0.86 | 00:35:21.217 | Spain              | Croatia            | 68 | Pressure        |   -   | [74.0, 12.2]    |                           |  |
|  +0.00 | 00:35:22.078 | Croatia            | Croatia            | 68 | Dispossessed    |   -   | [46.1, 67.9]    | Dispossessed              |  |
|  +0.00 | 00:35:22.078 | Spain              | Spain              | 69 | Duel            |  Yes  | [74.0, 12.2]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.24 | 00:35:23.313 | Spain              | Spain              | 69 | Pass            |   -   | [68.9, 5.6]     | -> Jorge Resurrec         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.97 | 00:35:24.047 | Spain              | Spain              | 69 | Ball Receipt*   |   -   | [68.9, 10.2]    | Controlled Receipt        |  |
|  +1.97 | 00:35:24.047 | Spain              | Spain              | 69 | Carry           |   -   | [68.9, 10.2]    | Carry                     |  |
|  +4.28 | 00:35:26.358 | Spain              | Spain              | 69 | Pass            |   -   | [64.8, 8.8]     | -> José Luis Gayà         |  |
|  +5.62 | 00:35:27.698 | Spain              | Spain              | 69 | Ball Receipt*   |   -   | [70.9, 2.8]     | Controlled Receipt        |  |
|  +5.62 | 00:35:27.698 | Spain              | Spain              | 69 | Carry           |   -   | [70.9, 2.8]     | Carry                     |  |
|  +5.64 | 00:35:27.714 | Croatia            | Spain              | 69 | Pressure        |   -   | [49.2, 76.3]    |                           |  |
|  +7.22 | 00:35:29.300 | Spain              | Spain              | 69 | Pass            |   -   | [70.9, 3.8]     | -> Jorge Resurrec         |  |
|  -2.35 | 00:35:19.724 | Croatia            | Croatia            | 146 | Ball Receipt*   |   -   | [31.8, 29.0]    | Controlled Receipt        |  |
|  -2.35 | 00:35:19.724 | Croatia            | Croatia            | 146 | Carry           |   -   | [31.8, 29.0]    | Carry                     |  |
|  +0.26 | 00:35:22.333 | Croatia            | Croatia            | 146 | Pass            |   -   | [33.8, 26.6]    | -> Joško Gvardiol         |  |
|  +1.26 | 00:35:23.336 | Croatia            | Croatia            | 146 | Ball Receipt*   |   -   | [34.0, 12.4]    | Controlled Receipt        |  |
|  +1.26 | 00:35:23.336 | Croatia            | Croatia            | 146 | Carry           |   -   | [34.0, 12.4]    | Carry                     |  |
|  +2.40 | 00:35:24.481 | Croatia            | Croatia            | 146 | Pass            |   -   | [34.0, 12.4]    | -> Ante Budimir           |  |
|  +4.31 | 00:35:26.387 | Croatia            | Croatia            | 146 | Ball Receipt*   |   -   | [74.6, 19.8]    | Controlled Receipt        |  |
|  +4.31 | 00:35:26.387 | Croatia            | Croatia            | 146 | Carry           |   -   | [74.6, 19.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +4.35 | 00:35:26.427 | Croatia            | Croatia            | 146 | Pass            |   -   | [73.7, 19.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +5.50 | 00:35:27.574 | Croatia            | Croatia            | 146 | Pressure        |   -   | [73.9, 7.4]     |                           |  |
|  +5.79 | 00:35:27.868 | Croatia            | Croatia            | 146 | Ball Receipt*   |   -   | [74.3, 7.2]     | Incomplete Receipt (Incomplete) |  |
|  +5.79 | 00:35:27.868 | Spain              | Croatia            | 146 | Clearance       |   -   | [44.0, 72.9]    |                           |  |

---

### Case 32: Episode `3794686_p13_cb293cfb`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_miscontrol` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.73 | 00:07:24.150 | Spain              | Croatia            | 13 | Ball Recovery   |   -   | [62.7, 27.4]    |                           |  |
|  -1.73 | 00:07:24.150 | Spain              | Croatia            | 13 | Carry           |   -   | [62.7, 27.4]    | Carry                     |  |
|  +0.00 | 00:07:25.880 | Croatia            | Croatia            | 13 | Pressure        |  Yes  | [44.1, 61.9]    |                           | **CP INITIATION** |
|  +0.51 | 00:07:26.394 | Spain              | Croatia            | 13 | Miscontrol      |   -   | [76.8, 15.8]    | Miscontrol                |  |
|  +1.20 | 00:07:27.077 | Spain              | Croatia            | 13 | Pressure        |   -   | [82.4, 11.1]    |                           |  |
|  +1.45 | 00:07:27.332 | Croatia            | Croatia            | 13 | Pass            |   -   | [36.4, 70.8]    | -> Nikola Vlašić          | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +3.45 | 00:07:29.332 | Croatia            | Croatia            | 13 | Ball Receipt*   |   -   | [50.6, 77.3]    | Controlled Receipt        |  |
|  +3.45 | 00:07:29.332 | Croatia            | Croatia            | 13 | Carry           |   -   | [50.6, 77.3]    | Carry                     |  |
|  +3.58 | 00:07:29.465 | Spain              | Croatia            | 13 | Pressure        |   -   | [67.2, 2.4]     |                           |  |
|  +3.99 | 00:07:29.872 | Croatia            | Croatia            | 13 | Dribble         |   -   | [52.9, 77.7]    | Incomplete                |  |
|  +3.99 | 00:07:29.872 | Spain              | Spain              | 14 | Duel            |  Yes  | [67.2, 2.4]     | Tackle, Success In Play   |  |
|  +5.08 | 00:07:30.957 | Spain              | Spain              | 14 | Pass            |   -   | [69.5, 3.0]     | -> José Luis Gayà         |  |
|  +6.58 | 00:07:32.457 | Spain              | Spain              | 14 | Ball Receipt*   |   -   | [72.7, 2.5]     | Controlled Receipt        |  |
|  +6.58 | 00:07:32.457 | Spain              | Spain              | 14 | Carry           |   -   | [72.7, 2.5]     | Carry                     |  |
|  -2.72 | 00:07:23.157 | Spain              | Spain              | 103 | Dribble         |   -   | [45.3, 76.6]    | Incomplete                | **POSSIBLE TRANSITION** |
|  -2.72 | 00:07:23.157 | Croatia            | Spain              | 103 | Duel            |   -   | [74.8, 3.5]     | Tackle, Won               |  |
|  -2.72 | 00:07:23.157 | Croatia            | Spain              | 103 | Carry           |   -   | [74.8, 3.5]     | Carry                     |  |
|  -0.54 | 00:07:25.336 | Croatia            | Spain              | 103 | Pass            |   -   | [70.4, 4.4]     | Incomplete (Incomplete)   |  |
|  +1.79 | 00:07:27.670 | Croatia            | Spain              | 103 | Ball Receipt*   |   -   | [99.2, 23.6]    | Incomplete Receipt (Incomplete) |  |
|  +1.79 | 00:07:27.670 | Spain              | Spain              | 103 | Ball Recovery   |   -   | [15.4, 54.8]    |                           |  |
|  +1.79 | 00:07:27.670 | Spain              | Spain              | 103 | Carry           |   -   | [15.4, 54.8]    | Carry                     |  |
|  +5.14 | 00:07:31.024 | Spain              | Spain              | 103 | Pass            |   -   | [14.8, 49.3]    | -> Aymeric Laport         |  |
|  +6.71 | 00:07:32.592 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [26.1, 33.4]    | Controlled Receipt        |  |
|  +6.71 | 00:07:32.592 | Spain              | Spain              | 103 | Carry           |   -   | [26.1, 33.4]    | Carry                     |  |
|  -2.19 | 00:07:23.694 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [32.0, 10.7]    | Controlled Receipt        |  |
|  -2.19 | 00:07:23.694 | Spain              | Spain              | 215 | Pass            |   -   | [32.0, 10.7]    | -> Fabián Ruiz Pe         |  |
|  -0.78 | 00:07:25.098 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [39.9, 10.7]    | Controlled Receipt        |  |
|  -0.78 | 00:07:25.098 | Spain              | Spain              | 215 | Carry           |   -   | [39.9, 10.7]    | Carry                     |  |
|  +0.22 | 00:07:26.097 | Croatia            | Spain              | 215 | Pressure        |   -   | [82.6, 69.8]    |                           |  |
|  +2.62 | 00:07:28.505 | Spain              | Spain              | 215 | Pass            |   -   | [42.9, 8.5]     | -> Jordi Alba Ram         |  |
|  +3.46 | 00:07:29.337 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [34.8, 8.5]     | Controlled Receipt        |  |
|  +3.46 | 00:07:29.337 | Spain              | Spain              | 215 | Carry           |   -   | [34.8, 8.5]     | Carry                     |  |
|  +5.23 | 00:07:31.107 | Spain              | Spain              | 215 | Pass            |   -   | [34.8, 8.5]     | -> Pau Francisco          |  |
|  +7.10 | 00:07:32.979 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [14.1, 18.1]    | Controlled Receipt        |  |
|  +7.10 | 00:07:32.979 | Spain              | Spain              | 215 | Carry           |   -   | [14.1, 18.1]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 33: Episode `3794686_p14_94dd9018`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.80 | 00:07:27.077 | Spain              | Croatia            | 13 | Pressure        |   -   | [82.4, 11.1]    |                           |  |
|  -2.54 | 00:07:27.332 | Croatia            | Croatia            | 13 | Pass            |   -   | [36.4, 70.8]    | -> Nikola Vlašić          |  |
|  -0.54 | 00:07:29.332 | Croatia            | Croatia            | 13 | Ball Receipt*   |   -   | [50.6, 77.3]    | Controlled Receipt        |  |
|  -0.54 | 00:07:29.332 | Croatia            | Croatia            | 13 | Carry           |   -   | [50.6, 77.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.41 | 00:07:29.465 | Spain              | Croatia            | 13 | Pressure        |   -   | [67.2, 2.4]     |                           |  |
|  +0.00 | 00:07:29.872 | Croatia            | Croatia            | 13 | Dribble         |   -   | [52.9, 77.7]    | Incomplete                |  |
|  +0.00 | 00:07:29.872 | Spain              | Spain              | 14 | Duel            |  Yes  | [67.2, 2.4]     | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +1.08 | 00:07:30.957 | Spain              | Spain              | 14 | Pass            |   -   | [69.5, 3.0]     | -> José Luis Gayà         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.58 | 00:07:32.457 | Spain              | Spain              | 14 | Ball Receipt*   |   -   | [72.7, 2.5]     | Controlled Receipt        |  |
|  +2.58 | 00:07:32.457 | Spain              | Spain              | 14 | Carry           |   -   | [72.7, 2.5]     | Carry                     |  |
|  +4.31 | 00:07:34.179 | Spain              | Spain              | 14 | Pass            |   -   | [81.9, 1.7]     | -> Álvaro Borja M         |  |
|  +5.43 | 00:07:35.304 | Spain              | Spain              | 14 | Ball Receipt*   |   -   | [76.0, 16.5]    | Controlled Receipt        |  |
|  +5.43 | 00:07:35.304 | Spain              | Spain              | 14 | Carry           |   -   | [76.0, 16.5]    | Carry                     |  |
|  +6.04 | 00:07:35.911 | Spain              | Spain              | 14 | Pass            |   -   | [76.0, 16.5]    | -> Jorge Resurrec         |  |
|  +6.90 | 00:07:36.773 | Spain              | Spain              | 14 | Ball Receipt*   |   -   | [72.4, 37.3]    | Controlled Receipt        |  |
|  +6.90 | 00:07:36.773 | Spain              | Spain              | 14 | Pass            |   -   | [72.4, 37.3]    | -> Sergio Busquet         |  |
|  +7.74 | 00:07:37.614 | Spain              | Spain              | 14 | Ball Receipt*   |   -   | [69.9, 28.5]    | Controlled Receipt        |  |
|  +7.74 | 00:07:37.614 | Spain              | Spain              | 14 | Carry           |   -   | [69.9, 28.5]    | Carry                     |  |
|  -2.20 | 00:07:27.670 | Croatia            | Spain              | 103 | Ball Receipt*   |   -   | [99.2, 23.6]    | Incomplete Receipt (Incomplete) |  |
|  -2.20 | 00:07:27.670 | Spain              | Spain              | 103 | Ball Recovery   |   -   | [15.4, 54.8]    |                           |  |
|  -2.20 | 00:07:27.670 | Spain              | Spain              | 103 | Carry           |   -   | [15.4, 54.8]    | Carry                     |  |
|  +1.15 | 00:07:31.024 | Spain              | Spain              | 103 | Pass            |   -   | [14.8, 49.3]    | -> Aymeric Laport         |  |
|  +2.72 | 00:07:32.592 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [26.1, 33.4]    | Controlled Receipt        |  |
|  +2.72 | 00:07:32.592 | Spain              | Spain              | 103 | Carry           |   -   | [26.1, 33.4]    | Carry                     |  |
|  +4.54 | 00:07:34.410 | Spain              | Spain              | 192 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete)   |  |
|  +5.63 | 00:07:35.502 | Croatia            | Spain              | 192 | Clearance       |   -   | [5.6, 51.8]     |                           |  |
|  +7.81 | 00:07:37.684 | Spain              | Spain              | 192 | Pass            |   -   | [92.2, 26.1]    | -> Jordi Alba Ram         |  |
|  -1.37 | 00:07:28.505 | Spain              | Spain              | 215 | Pass            |   -   | [42.9, 8.5]     | -> Jordi Alba Ram         |  |
|  -0.54 | 00:07:29.337 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [34.8, 8.5]     | Controlled Receipt        |  |
|  -0.54 | 00:07:29.337 | Spain              | Spain              | 215 | Carry           |   -   | [34.8, 8.5]     | Carry                     |  |
|  +1.23 | 00:07:31.107 | Spain              | Spain              | 215 | Pass            |   -   | [34.8, 8.5]     | -> Pau Francisco          |  |
|  +3.11 | 00:07:32.979 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [14.1, 18.1]    | Controlled Receipt        |  |
|  +3.11 | 00:07:32.979 | Spain              | Spain              | 215 | Carry           |   -   | [14.1, 18.1]    | Carry                     |  |
|  +4.45 | 00:07:34.318 | Spain              | Spain              | 215 | Pass            |   -   | [9.8, 24.3]     | -> Unai Simón Men         |  |
|  +6.03 | 00:07:35.905 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [8.7, 43.0]     | Controlled Receipt        |  |
|  +6.03 | 00:07:35.905 | Spain              | Spain              | 215 | Carry           |   -   | [8.7, 43.0]     | Carry                     |  |
|  +7.32 | 00:07:37.191 | Croatia            | Spain              | 215 | Pressure        |   -   | [110.6, 33.4]   |                           |  |
|  +7.72 | 00:07:37.592 | Spain              | Spain              | 215 | Pass            |   -   | [9.5, 40.8]     | -> Pau Francisco          |  |

---

### Case 34: Episode `3794686_p102_c353f151`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.58 | 00:06:37.529 | Spain              | Spain              | 12 | Ball Receipt*   |   -   | [8.5, 18.1]     | Controlled Receipt        |  |
|  -1.58 | 00:06:37.529 | Spain              | Spain              | 12 | Carry           |   -   | [8.5, 18.1]     | Carry                     |  |
|  +0.67 | 00:06:39.787 | Spain              | Spain              | 12 | Pass            |   -   | [10.1, 23.3]    | -> Eric García Ma         |  |
|  +2.49 | 00:06:41.601 | Spain              | Spain              | 12 | Ball Receipt*   |   -   | [21.6, 51.1]    | Controlled Receipt        |  |
|  +2.49 | 00:06:41.601 | Spain              | Spain              | 12 | Carry           |   -   | [21.6, 51.1]    | Carry                     |  |
|  +5.34 | 00:06:44.452 | Spain              | Spain              | 12 | Pass            |   -   | [27.1, 50.5]    | -> Aymeric Laport         |  |
|  +6.92 | 00:06:46.030 | Spain              | Spain              | 12 | Ball Receipt*   |   -   | [35.0, 30.1]    | Controlled Receipt        |  |
|  +6.92 | 00:06:46.030 | Spain              | Spain              | 12 | Carry           |   -   | [35.0, 30.1]    | Carry                     |  |
|  -2.74 | 00:06:36.371 | Croatia            | Croatia            | 102 | Pass            |   -   | [61.3, 9.6]     | -> Ante Rebić             |  |
|  -1.75 | 00:06:37.359 | Croatia            | Croatia            | 102 | Ball Receipt*   |   -   | [65.8, 3.9]     | Controlled Receipt        |  |
|  -1.75 | 00:06:37.359 | Croatia            | Croatia            | 102 | Carry           |   -   | [65.8, 3.9]     | Carry                     |  |
|  -1.52 | 00:06:37.595 | Croatia            | Croatia            | 102 | Dribble         |   -   | [68.7, 3.5]     | Incomplete                |  |
|  -1.52 | 00:06:37.595 | Spain              | Croatia            | 102 | Duel            |   -   | [51.4, 76.6]    | Tackle, Won               |  |
|  -1.52 | 00:06:37.595 | Spain              | Croatia            | 102 | Carry           |   -   | [51.4, 76.6]    | Carry                     |  |
|  +0.00 | 00:06:39.114 | Croatia            | Croatia            | 102 | Pressure        |  Yes  | [64.1, 4.1]     |                           | **CP INITIATION** |
|  +0.23 | 00:06:39.347 | Spain              | Croatia            | 102 | Pass            |   -   | [55.4, 77.9]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +2.96 | 00:06:42.069 | Spain              | Croatia            | 102 | Pressure        |   -   | [68.7, 73.3]    |                           |  |
|  +3.05 | 00:06:42.163 | Croatia            | Croatia            | 102 | Pass            |   -   | [54.7, 8.5]     | -> Marcelo Brozov         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +5.55 | 00:06:44.663 | Croatia            | Croatia            | 102 | Ball Receipt*   |   -   | [49.0, 19.6]    | Controlled Receipt        |  |
|  +5.55 | 00:06:44.663 | Croatia            | Croatia            | 102 | Pass            |   -   | [49.0, 19.6]    | -> Josip Juranovi         |  |
|  +8.00 | 00:06:47.111 | Croatia            | Croatia            | 102 | Ball Receipt*   |   -   | [73.5, 70.7]    | Controlled Receipt        |  |
|  +8.00 | 00:06:47.111 | Croatia            | Croatia            | 102 | Carry           |   -   | [73.5, 70.7]    | Carry                     |  |
|  +6.21 | 00:06:45.322 | Spain              | Spain              | 191 | Pass            |   -   | [112.0, 22.8]   | -> Daniel Olmo Ca         |  |
|  +7.51 | 00:06:46.622 | Spain              | Spain              | 191 | Ball Receipt*   |   -   | [105.4, 25.3]   | Controlled Receipt        |  |
|  +7.51 | 00:06:46.624 | Spain              | Spain              | 191 | Shot            |   -   | [106.6, 29.7]   | Blocked                   |  |
|  +7.84 | 00:06:46.949 | Croatia            | Spain              | 191 | Block           |   -   | [6.2, 46.5]     |                           |  |
|  +7.88 | 00:06:46.989 | Croatia            | Spain              | 191 | Goal Keeper     |   -   | [4.2, 44.2]     |                           |  |
|  -2.31 | 00:06:36.804 | Spain              | Spain              | 215 | Pass            |   -   | [73.7, 74.6]    | -> Pedro González         |  |
|  -1.39 | 00:06:37.723 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [78.5, 60.5]    | Controlled Receipt        |  |
|  -1.39 | 00:06:37.723 | Spain              | Spain              | 215 | Carry           |   -   | [78.5, 60.5]    | Carry                     |  |
|  -0.05 | 00:06:39.064 | Spain              | Spain              | 215 | Pass            |   -   | [78.5, 56.3]    | -> Fabián Ruiz Pe         |  |
|  +1.51 | 00:06:40.627 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [71.7, 28.2]    | Controlled Receipt        |  |
|  +1.51 | 00:06:40.627 | Spain              | Spain              | 215 | Carry           |   -   | [71.7, 28.2]    | Carry                     |  |
|  +2.33 | 00:06:41.445 | Spain              | Spain              | 215 | Pass            |   -   | [71.7, 28.2]    | -> Jordi Alba Ram         |  |
|  +3.51 | 00:06:42.627 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [77.2, 11.8]    | Controlled Receipt        |  |
|  +3.51 | 00:06:42.627 | Spain              | Spain              | 215 | Pass            |   -   | [77.2, 11.8]    | -> Fabián Ruiz Pe         |  |
|  +5.09 | 00:06:44.200 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [74.1, 20.5]    | Controlled Receipt        |  |
|  +5.09 | 00:06:44.200 | Spain              | Spain              | 215 | Pass            |   -   | [74.3, 20.3]    | -> Jordi Alba Ram         |  |
|  +5.97 | 00:06:45.088 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [74.6, 10.7]    | Controlled Receipt        |  |
|  +5.97 | 00:06:45.088 | Spain              | Spain              | 215 | Carry           |   -   | [74.6, 10.7]    | Carry                     |  |
|  +6.92 | 00:06:46.031 | Spain              | Spain              | 215 | Pass            |   -   | [74.6, 10.7]    | -> Pau Francisco          | **OPPONENT LAST CONTROL** |

---

### Case 35: Episode `3788764_p62_5659784e`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.65 | 00:30:50.594 | Germany            | Germany            | 62 | Pass            |   -   | [34.4, 56.2]    | -> Kai Havertz            |  |
|  -0.06 | 00:30:52.179 | Germany            | Germany            | 62 | Ball Receipt*   |   -   | [55.0, 46.3]    | Controlled Receipt        |  |
|  -0.06 | 00:30:52.179 | Germany            | Germany            | 62 | Carry           |   -   | [55.0, 46.3]    | Carry                     |  |
|  -0.04 | 00:30:52.197 | Germany            | Germany            | 62 | Pass            |   -   | [55.2, 46.3]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:30:52.241 | Germany            | Germany            | 62 | Ball Receipt*   |   -   | [62.3, 50.1]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:30:52.241 | Portugal           | Germany            | 62 | Block           |  Yes  | [62.5, 33.0]    |                           | **CP INITIATION** |
|  +1.29 | 00:30:53.534 | Germany            | Germany            | 62 | Pass            |   -   | [49.2, 51.8]    | -> Thomas Müller          |  |
|  +2.36 | 00:30:54.596 | Germany            | Germany            | 62 | Ball Receipt*   |   -   | [72.5, 55.2]    | Controlled Receipt        |  |
|  +2.36 | 00:30:54.596 | Germany            | Germany            | 62 | Carry           |   -   | [72.5, 55.2]    | Carry                     |  |
|  +2.39 | 00:30:54.636 | Germany            | Germany            | 62 | Pass            |   -   | [72.5, 55.2]    | Incomplete (Incomplete)   |  |
|  +3.83 | 00:30:56.069 | Germany            | Germany            | 62 | Ball Receipt*   |   -   | [82.6, 48.7]    | Incomplete Receipt (Incomplete) |  |
|  +3.83 | 00:30:56.069 | Portugal           | Germany            | 62 | Pass            |   -   | [33.3, 30.9]    | -> Raphaël Adelin         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +4.96 | 00:30:57.206 | Portugal           | Germany            | 62 | Ball Receipt*   |   -   | [35.5, 12.1]    | Controlled Receipt        |  |
|  +4.96 | 00:30:57.206 | Portugal           | Germany            | 62 | Carry           |   -   | [35.5, 12.1]    | Carry                     |  |
|  +6.61 | 00:30:58.853 | Portugal           | Germany            | 62 | Pass            |   -   | [41.6, 3.3]     | Incomplete (Incomplete)   |  |
|  +7.87 | 00:31:00.109 | Portugal           | Germany            | 62 | Ball Receipt*   |   -   | [66.1, 19.0]    | Incomplete Receipt (Incomplete) |  |
|  +7.87 | 00:31:00.109 | Germany            | Germany            | 62 | Interception    |  Yes  | [57.4, 60.5]    | Won                       |  |
|  -2.67 | 00:30:49.575 | Germany            | Germany            | 129 | Ball Receipt*   |   -   | [54.4, 38.5]    | Controlled Receipt        |  |
|  -2.67 | 00:30:49.575 | Germany            | Germany            | 129 | Carry           |   -   | [54.4, 38.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.28 | 00:30:51.960 | Portugal           | Germany            | 129 | Pressure        |   -   | [48.3, 51.8]    |                           |  |
|  +0.91 | 00:30:53.149 | Germany            | Germany            | 129 | Pass            |   -   | [76.7, 27.7]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +2.85 | 00:30:55.093 | Germany            | Germany            | 129 | Pressure        |   -   | [99.3, 17.9]    |                           |  |
|  +3.53 | 00:30:55.769 | Germany            | Germany            | 129 | Ball Receipt*   |   -   | [111.1, 16.2]   | Incomplete Receipt (Incomplete) |  |
|  +3.53 | 00:30:55.769 | Portugal           | Portugal           | 130 | Ball Recovery   |   -   | [5.1, 63.7]     |                           |  |
|  +3.53 | 00:30:55.769 | Portugal           | Portugal           | 130 | Carry           |   -   | [5.1, 63.7]     | Carry                     |  |
|  +7.01 | 00:30:59.246 | Portugal           | Portugal           | 130 | Pass            |   -   | [2.3, 67.4]     | -> Renato Júnior          |  |

---

### Case 36: Episode `3788764_p100_51a86eae`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.64 | 00:09:28.140 | Portugal           | Portugal           | 16 | Pass            |   -   | [27.0, 27.4]    | -> Cristiano Rona         |  |
|  -1.93 | 00:09:28.851 | Germany            | Portugal           | 16 | Pressure        |  Yes  | [76.2, 58.2]    |                           |  |
|  -1.79 | 00:09:28.990 | Portugal           | Portugal           | 16 | Ball Receipt*   |   -   | [40.2, 21.9]    | Controlled Receipt        |  |
|  -1.79 | 00:09:28.990 | Portugal           | Portugal           | 16 | Carry           |   -   | [40.2, 21.9]    | Carry                     |  |
|  -1.34 | 00:09:29.444 | Germany            | Portugal           | 16 | Foul Committed  |  Yes  | [79.2, 58.2]    |                           |  |
|  -1.34 | 00:09:29.444 | Portugal           | Portugal           | 16 | Foul Won        |   -   | [40.9, 21.9]    |                           |  |
|  -1.29 | 00:09:29.494 | Portugal           | Portugal           | 99 | Pass            |   -   | [53.9, 80.0]    | -> Cristiano Rona         |  |
|  -0.64 | 00:09:30.140 | Germany            | Portugal           | 99 | Pressure        |   -   | [57.1, 9.8]     |                           |  |
|  -0.63 | 00:09:30.157 | Portugal           | Portugal           | 99 | Ball Receipt*   |   -   | [63.8, 67.6]    | Controlled Receipt        |  |
|  -0.63 | 00:09:30.157 | Portugal           | Portugal           | 99 | Carry           |   -   | [63.8, 67.6]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:09:30.785 | Portugal           | Portugal           | 99 | Dribble         |   -   | [63.0, 70.3]    | Incomplete                |  |
|  +0.00 | 00:09:30.785 | Germany            | Germany            | 100 | Duel            |  Yes  | [57.1, 9.8]     | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.56 | 00:09:31.340 | Portugal           | Germany            | 100 | Pressure        |  Yes  | [63.0, 70.3]    |                           |  |
|  +1.18 | 00:09:31.961 | Germany            | Germany            | 100 | Pass            |   -   | [57.5, 8.3]     | -> Toni Kroos             | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.37 | 00:09:32.159 | Portugal           | Germany            | 100 | Pressure        |  Yes  | [57.2, 66.4]    |                           |  |
|  +1.67 | 00:09:32.451 | Germany            | Germany            | 100 | Ball Receipt*   |   -   | [62.9, 13.7]    | Controlled Receipt        |  |
|  +1.67 | 00:09:32.451 | Germany            | Germany            | 100 | Carry           |   -   | [62.9, 13.7]    | Carry                     |  |
|  +1.71 | 00:09:32.491 | Germany            | Germany            | 100 | Pass            |   -   | [63.5, 14.8]    | -> İlkay Gündoğan         |  |
|  +2.57 | 00:09:33.354 | Germany            | Germany            | 100 | Ball Receipt*   |   -   | [55.8, 18.7]    | Controlled Receipt        |  |
|  +2.57 | 00:09:33.354 | Germany            | Germany            | 100 | Carry           |   -   | [55.8, 18.7]    | Carry                     |  |
|  +3.35 | 00:09:34.135 | Germany            | Germany            | 100 | Pass            |   -   | [57.2, 23.3]    | -> Matthias Ginte         |  |
|  +4.60 | 00:09:35.384 | Germany            | Germany            | 100 | Ball Receipt*   |   -   | [42.3, 36.1]    | Controlled Receipt        |  |
|  +4.60 | 00:09:35.384 | Germany            | Germany            | 100 | Carry           |   -   | [42.3, 36.1]    | Carry                     |  |
|  +5.80 | 00:09:36.585 | Germany            | Germany            | 100 | Pass            |   -   | [41.0, 37.1]    | -> Manuel Neuer           |  |

---

### Case 37: Episode `3794686_p182_206d419e`
- **Match**: `3794686` (UEFA Euro) | **Period**: 3
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_miscontrol` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.86 | 00:02:07.241 | Spain              | Spain              | 6 | Pass            |   -   | [11.9, 32.5]    | -> Eric García Ma         |  |
|  -1.14 | 00:02:08.958 | Spain              | Spain              | 6 | Ball Receipt*   |   -   | [19.7, 44.0]    | Controlled Receipt        |  |
|  -1.14 | 00:02:08.958 | Spain              | Spain              | 6 | Carry           |   -   | [19.7, 44.0]    | Carry                     |  |
|  +4.27 | 00:02:14.369 | Spain              | Spain              | 6 | Pass            |   -   | [36.7, 44.2]    | -> Aymeric Laport         | **PRESSING-TEAM FIRST CONTROL** |
|  +5.95 | 00:02:16.048 | Spain              | Spain              | 6 | Ball Receipt*   |   -   | [38.6, 27.1]    | Controlled Receipt        |  |
|  +5.95 | 00:02:16.048 | Spain              | Spain              | 6 | Carry           |   -   | [38.6, 27.1]    | Carry                     |  |
|  -1.66 | 00:02:08.441 | Spain              | Spain              | 182 | Ball Receipt*   |   -   | [76.5, 49.5]    | Incomplete Receipt (Incomplete) |  |
|  -1.66 | 00:02:08.441 | Croatia            | Spain              | 182 | Pass            |   -   | [38.7, 32.4]    | -> Marcelo Brozov         |  |
|  +0.00 | 00:02:10.096 | Spain              | Spain              | 182 | Pressure        |  Yes  | [68.1, 54.1]    |                           | **CP INITIATION** |
|  +0.12 | 00:02:10.221 | Croatia            | Spain              | 182 | Ball Receipt*   |   -   | [50.9, 26.6]    | Controlled Receipt        |  |
|  +0.12 | 00:02:10.221 | Croatia            | Spain              | 182 | Carry           |   -   | [50.9, 26.6]    | Carry                     |  |
|  +0.38 | 00:02:10.480 | Croatia            | Spain              | 182 | Miscontrol      |   -   | [53.7, 23.5]    | Miscontrol                |  |
|  +0.97 | 00:02:11.066 | Spain              | Spain              | 182 | Pass            |   -   | [67.9, 64.4]    | -> Álvaro Borja M         | (v2.6 Regain Event) |
|  +2.28 | 00:02:12.373 | Spain              | Spain              | 182 | Ball Receipt*   |   -   | [77.0, 50.3]    | Controlled Receipt        |  |
|  +2.28 | 00:02:12.373 | Spain              | Spain              | 182 | Carry           |   -   | [77.0, 50.3]    | Carry                     |  |
|  +2.63 | 00:02:12.730 | Croatia            | Spain              | 182 | Pressure        |   -   | [43.1, 29.8]    |                           |  |
|  +5.15 | 00:02:15.244 | Croatia            | Spain              | 182 | Pressure        |   -   | [41.7, 18.1]    |                           |  |
|  +5.23 | 00:02:15.328 | Spain              | Spain              | 182 | Miscontrol      |   -   | [78.4, 66.4]    | Miscontrol                |  |
|  +7.12 | 00:02:17.217 | Croatia            | Croatia            | 183 | Ball Recovery   |   -   | [40.4, 6.0]     |                           |  |
|  +7.12 | 00:02:17.217 | Croatia            | Croatia            | 183 | Carry           |   -   | [40.4, 6.0]     | Carry                     |  |
|  -1.03 | 00:02:09.068 | Spain              | Spain              | 209 | Pass            |   -   | [97.4, 59.8]    | Incomplete (Incomplete)   |  |
|  -0.12 | 00:02:09.972 | Spain              | Spain              | 209 | Pressure        |   -   | [104.9, 63.9]   |                           |  |
|  +0.26 | 00:02:10.352 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [105.7, 63.1]   | Incomplete Receipt (Incomplete) |  |
|  +0.26 | 00:02:10.352 | Croatia            | Spain              | 209 | Interception    |   -   | [13.7, 19.4]    | Won                       |  |
|  +0.26 | 00:02:10.352 | Croatia            | Spain              | 209 | Carry           |   -   | [13.7, 19.4]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.48 | 00:02:10.573 | Croatia            | Spain              | 209 | Dispossessed    |   -   | [15.7, 17.3]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.48 | 00:02:10.573 | Spain              | Spain              | 209 | Duel            |  Yes  | [104.4, 62.8]   | Tackle, Success In Play   |  |
|  +1.51 | 00:02:11.611 | Spain              | Spain              | 209 | Ball Recovery   |   -   | [95.9, 60.6]    |                           |  |
|  +1.51 | 00:02:11.611 | Spain              | Spain              | 209 | Carry           |   -   | [95.9, 60.6]    | Carry                     |  |
|  +2.56 | 00:02:12.661 | Croatia            | Spain              | 209 | Pressure        |   -   | [22.3, 18.6]    |                           |  |
|  +3.02 | 00:02:13.113 | Spain              | Spain              | 209 | Pass            |   -   | [93.5, 60.1]    | -> Rodrigo Hernán         |  |
|  +4.26 | 00:02:14.357 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [84.6, 63.3]    | Controlled Receipt        |  |
|  +4.26 | 00:02:14.357 | Spain              | Spain              | 209 | Pass            |   -   | [84.6, 63.3]    | -> Daniel Olmo Ca         |  |
|  +5.55 | 00:02:15.645 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [100.4, 70.6]   | Controlled Receipt        |  |
|  +5.55 | 00:02:15.645 | Spain              | Spain              | 209 | Carry           |   -   | [100.4, 70.6]   | Carry                     |  |
|  +7.83 | 00:02:17.929 | Spain              | Spain              | 209 | Pass            |   -   | [101.6, 75.5]   | -> Rodrigo Hernán         |  |

---

### Case 38: Episode `3788766_p17_f26809c0`
- **Match**: `3788766` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Wales** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Wales`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.71 | 00:08:40.495 | Wales              | Italy              | 16 | Pressure        |   -   | [42.8, 74.6]    |                           |  |
|  -2.13 | 00:08:41.075 | Italy              | Italy              | 16 | Pass            |   -   | [74.8, 6.6]     | -> Andrea Belotti         |  |
|  -1.48 | 00:08:41.725 | Italy              | Italy              | 16 | Ball Receipt*   |   -   | [79.4, 14.8]    | Controlled Receipt        |  |
|  -1.48 | 00:08:41.725 | Italy              | Italy              | 16 | Carry           |   -   | [79.4, 14.8]    | Carry                     |  |
|  -0.47 | 00:08:42.731 | Wales              | Italy              | 16 | Pressure        |   -   | [38.1, 58.7]    |                           |  |
|  +0.00 | 00:08:43.205 | Italy              | Italy              | 16 | Dispossessed    |   -   | [86.0, 22.9]    | Dispossessed              |  |
|  +0.00 | 00:08:43.205 | Wales              | Wales              | 17 | Duel            |  Yes  | [34.1, 57.2]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.26 | 00:08:44.470 | Wales              | Wales              | 17 | Pass            |   -   | [25.3, 54.8]    | -> Aaron Ramsey           | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.11 | 00:08:45.311 | Italy              | Wales              | 17 | Pressure        |  Yes  | [83.5, 25.1]    |                           |  |
|  +2.11 | 00:08:45.314 | Wales              | Wales              | 17 | Ball Receipt*   |   -   | [35.7, 51.8]    | Controlled Receipt        |  |
|  +2.11 | 00:08:45.314 | Wales              | Wales              | 17 | Carry           |   -   | [35.7, 51.8]    | Carry                     |  |
|  +2.40 | 00:08:45.608 | Wales              | Wales              | 17 | Pass            |   -   | [33.9, 55.8]    | -> Joe Allen              |  |
|  +3.90 | 00:08:47.110 | Italy              | Wales              | 17 | Pressure        |  Yes  | [75.1, 33.6]    |                           |  |
|  +4.54 | 00:08:47.748 | Wales              | Wales              | 17 | Ball Receipt*   |   -   | [47.0, 42.4]    | Controlled Receipt        |  |
|  +4.54 | 00:08:47.748 | Wales              | Wales              | 17 | Carry           |   -   | [47.0, 42.4]    | Carry                     |  |
|  +6.45 | 00:08:49.656 | Italy              | Wales              | 17 | Foul Committed  |   -   | [63.4, 41.6]    |                           |  |
|  +6.45 | 00:08:49.656 | Wales              | Wales              | 17 | Foul Won        |   -   | [56.7, 38.5]    |                           |  |
|  -1.51 | 00:08:41.693 | Italy              | Italy              | 108 | Pass            |   -   | [97.1, 80.0]    | -> Matteo Pessina         |  |
|  -0.43 | 00:08:42.776 | Wales              | Italy              | 108 | Pressure        |   -   | [18.4, 8.0]     |                           |  |
|  -0.39 | 00:08:42.814 | Italy              | Italy              | 108 | Ball Receipt*   |   -   | [100.6, 71.6]   | Controlled Receipt        |  |
|  -0.39 | 00:08:42.814 | Italy              | Italy              | 108 | Carry           |   -   | [100.6, 71.6]   | Carry                     |  |
|  -0.20 | 00:08:43.008 | Italy              | Italy              | 108 | Pass            |   -   | [101.0, 72.5]   | -> Federico Chies         |  |
|  +0.77 | 00:08:43.980 | Wales              | Italy              | 108 | Pressure        |   -   | [22.8, 4.2]     |                           |  |
|  +1.08 | 00:08:44.282 | Italy              | Italy              | 108 | Ball Receipt*   |   -   | [98.0, 77.1]    | Controlled Receipt        |  |
|  +1.08 | 00:08:44.282 | Italy              | Italy              | 108 | Carry           |   -   | [98.0, 77.1]    | Carry                     |  |
|  +2.54 | 00:08:45.741 | Wales              | Italy              | 108 | Pressure        |   -   | [22.9, 24.1]    |                           |  |
|  +2.88 | 00:08:46.083 | Italy              | Italy              | 108 | Pass            |   -   | [97.1, 59.1]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +3.77 | 00:08:46.972 | Italy              | Italy              | 108 | Ball Receipt*   |   -   | [103.7, 40.7]   | Incomplete Receipt (Incomplete) |  |
|  +3.77 | 00:08:46.972 | Wales              | Italy              | 108 | Clearance       |   -   | [17.7, 36.7]    |                           |  |
|  +5.75 | 00:08:48.953 | Italy              | Italy              | 108 | Pass            |   -   | [68.3, 71.1]    | -> Rafael Tolói           |  |
|  +7.65 | 00:08:50.858 | Italy              | Italy              | 108 | Ball Receipt*   |   -   | [76.9, 72.9]    | Controlled Receipt        |  |
|  +7.65 | 00:08:50.858 | Italy              | Italy              | 108 | Carry           |   -   | [76.9, 72.9]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 39: Episode `3788766_p31_d2bd5681`
- **Match**: `3788766` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Wales** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Wales`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.93 | 00:15:18.678 | Wales              | Italy              | 30 | Pressure        |   -   | [42.3, 62.7]    |                           |  |
|  -2.57 | 00:15:19.037 | Italy              | Italy              | 30 | Ball Receipt*   |   -   | [75.9, 19.6]    | Controlled Receipt        |  |
|  -2.57 | 00:15:19.037 | Italy              | Italy              | 30 | Carry           |   -   | [75.9, 19.6]    | Carry                     |  |
|  -2.53 | 00:15:19.077 | Italy              | Italy              | 30 | Pass            |   -   | [75.6, 19.6]    | -> Federico Berna         |  |
|  -1.59 | 00:15:20.014 | Wales              | Italy              | 30 | Pressure        |   -   | [32.4, 63.0]    |                           |  |
|  -1.50 | 00:15:20.107 | Italy              | Italy              | 30 | Ball Receipt*   |   -   | [85.0, 13.2]    | Controlled Receipt        |  |
|  -1.50 | 00:15:20.107 | Italy              | Italy              | 30 | Carry           |   -   | [85.0, 13.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.72 | 00:15:20.884 | Wales              | Italy              | 30 | Pressure        |   -   | [37.1, 60.2]    |                           |  |
|  +0.00 | 00:15:21.607 | Italy              | Italy              | 30 | Dispossessed    |   -   | [85.0, 19.4]    | Dispossessed              |  |
|  +0.00 | 00:15:21.607 | Wales              | Wales              | 31 | Duel            |  Yes  | [35.1, 60.7]    | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.75 | 00:15:22.356 | Wales              | Wales              | 31 | Pass            |   -   | [30.0, 56.7]    | -> Connor Roberts         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.01 | 00:15:23.617 | Wales              | Wales              | 31 | Ball Receipt*   |   -   | [22.5, 61.4]    | Controlled Receipt        |  |
|  +2.01 | 00:15:23.617 | Wales              | Wales              | 31 | Carry           |   -   | [22.5, 61.4]    | Carry                     |  |
|  +3.01 | 00:15:24.618 | Italy              | Wales              | 31 | Pressure        |  Yes  | [94.6, 18.2]    |                           |  |
|  +4.38 | 00:15:25.985 | Wales              | Wales              | 31 | Pass            |   -   | [22.2, 61.4]    | -> Danny Ward             |  |
|  +5.86 | 00:15:27.468 | Wales              | Wales              | 31 | Ball Receipt*   |   -   | [9.6, 48.9]     | Controlled Receipt        |  |
|  +5.86 | 00:15:27.468 | Wales              | Wales              | 31 | Pass            |   -   | [9.6, 48.9]     | Incomplete (Incomplete)   |  |

---

### Case 40: Episode `3794692_p140_42a963e2`
- **Match**: `3794692` (UEFA Euro) | **Period**: 3
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.31 | 00:14:05.328 | Ukraine            | Ukraine            | 19 | Pass            |   -   | [94.1, 13.5]    | -> Mykola Matvien         |  |
|  +0.09 | 00:14:06.727 | Ukraine            | Ukraine            | 19 | Ball Receipt*   |   -   | [72.2, 14.4]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.09 | 00:14:06.727 | Ukraine            | Ukraine            | 19 | Carry           |   -   | [72.2, 14.4]    | Carry                     |  |
|  +0.13 | 00:14:06.767 | Ukraine            | Ukraine            | 19 | Pass            |   -   | [72.2, 14.4]    | -> Mykola Shapare         |  |
|  +1.05 | 00:14:07.683 | Ukraine            | Ukraine            | 19 | Ball Receipt*   |   -   | [82.7, 13.5]    | Controlled Receipt        |  |
|  +1.05 | 00:14:07.683 | Ukraine            | Ukraine            | 19 | Carry           |   -   | [82.7, 13.5]    | Carry                     |  |
|  +2.75 | 00:14:09.386 | Ukraine            | Ukraine            | 19 | Pass            |   -   | [71.0, 13.5]    | -> Mykola Matvien         |  |
|  +4.29 | 00:14:10.924 | Ukraine            | Ukraine            | 19 | Ball Receipt*   |   -   | [56.5, 15.7]    | Controlled Receipt        |  |
|  +4.29 | 00:14:10.924 | Ukraine            | Ukraine            | 19 | Carry           |   -   | [56.5, 15.7]    | Carry                     |  |
|  +4.83 | 00:14:11.465 | Ukraine            | Ukraine            | 19 | Pass            |   -   | [52.5, 17.8]    | -> Serhiy Kryvtso         |  |
|  +6.18 | 00:14:12.815 | Ukraine            | Ukraine            | 19 | Ball Receipt*   |   -   | [43.5, 29.2]    | Controlled Receipt        |  |
|  +6.18 | 00:14:12.815 | Ukraine            | Ukraine            | 19 | Carry           |   -   | [43.5, 29.2]    | Carry                     |  |
|  +7.91 | 00:14:14.544 | Ukraine            | Ukraine            | 19 | Pass            |   -   | [48.1, 38.5]    | -> Illia Zabarnyi         |  |
|  +2.04 | 00:14:08.680 | Sweden             | Sweden             | 95 | Pass            |   -   | [85.2, 80.0]    | -> Victor Nilsson         |  |
|  +4.00 | 00:14:10.633 | Sweden             | Sweden             | 95 | Ball Receipt*   |   -   | [61.6, 77.3]    | Controlled Receipt        |  |
|  +4.00 | 00:14:10.633 | Sweden             | Sweden             | 95 | Carry           |   -   | [61.6, 77.3]    | Carry                     |  |
|  +5.54 | 00:14:12.174 | Sweden             | Sweden             | 95 | Pass            |   -   | [61.6, 77.3]    | -> Albin Ekdal            |  |
|  +6.54 | 00:14:13.178 | Sweden             | Sweden             | 95 | Ball Receipt*   |   -   | [64.0, 58.9]    | Controlled Receipt        |  |
|  +6.54 | 00:14:13.178 | Sweden             | Sweden             | 95 | Carry           |   -   | [64.0, 58.9]    | Carry                     |  |
|  -2.59 | 00:14:04.048 | Ukraine            | Ukraine            | 140 | Dispossessed    |   -   | [82.7, 36.3]    | Dispossessed              |  |
|  -2.59 | 00:14:04.048 | Sweden             | Ukraine            | 140 | Duel            |   -   | [37.4, 43.8]    | Tackle, Lost In Play      |  |
|  -1.22 | 00:14:05.415 | Sweden             | Ukraine            | 140 | Ball Recovery   |   -   | [37.4, 43.8]    |                           |  |
|  -0.49 | 00:14:06.145 | Sweden             | Ukraine            | 140 | Pressure        |   -   | [37.4, 39.1]    |                           |  |
|  -0.24 | 00:14:06.396 | Ukraine            | Ukraine            | 140 | Pressure        |   -   | [82.7, 41.0]    |                           |  |
|  -0.08 | 00:14:06.559 | Sweden             | Ukraine            | 140 | Ball Recovery   |   -   | [37.4, 39.1]    |                           |  |
|  -0.08 | 00:14:06.559 | Sweden             | Ukraine            | 140 | Carry           |   -   | [37.4, 39.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:14:06.636 | Sweden             | Ukraine            | 140 | Dispossessed    |   -   | [37.4, 39.1]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:14:06.636 | Ukraine            | Ukraine            | 140 | Duel            |  Yes  | [82.7, 41.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.45 | 00:14:08.082 | Ukraine            | Ukraine            | 140 | Pass            |   -   | [77.5, 24.9]    | -> Oleksandr Zinc         | (v2.6 Regain Event) |
|  +2.96 | 00:14:09.591 | Ukraine            | Ukraine            | 140 | Ball Receipt*   |   -   | [95.3, 7.9]     | Controlled Receipt        |  |
|  +2.96 | 00:14:09.591 | Ukraine            | Ukraine            | 140 | Carry           |   -   | [95.3, 7.9]     | Carry                     |  |
|  +4.90 | 00:14:11.533 | Ukraine            | Ukraine            | 140 | Pass            |   -   | [96.9, 7.9]     | Incomplete (Incomplete)   |  |
|  +4.98 | 00:14:11.615 | Ukraine            | Ukraine            | 140 | Ball Receipt*   |   -   | [107.4, 40.4]   | Incomplete Receipt (Incomplete) |  |
|  +4.98 | 00:14:11.615 | Sweden             | Ukraine            | 140 | Block           |   -   | [16.4, 65.1]    |                           |  |

---

### Case 41: Episode `3794692_p59_c841f46f`
- **Match**: `3794692` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Sweden** vs Actual Opponent: **Ukraine** (StatsBomb Poss Team: `Sweden`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.83 | 00:39:00.204 | Sweden             | Sweden             | 59 | Ball Receipt*   |   -   | [91.4, 70.0]    | Controlled Receipt        |  |
|  -2.83 | 00:39:00.204 | Sweden             | Sweden             | 59 | Pass            |   -   | [91.4, 70.0]    | -> Sebastian Lars         |  |
|  -1.88 | 00:39:01.153 | Ukraine            | Sweden             | 59 | Pressure        |   -   | [22.5, 23.4]    |                           |  |
|  -1.06 | 00:39:01.974 | Sweden             | Sweden             | 59 | Ball Receipt*   |   -   | [97.6, 56.7]    | Controlled Receipt        |  |
|  -1.06 | 00:39:01.974 | Sweden             | Sweden             | 59 | Pass            |   -   | [98.5, 57.0]    | Incomplete (Incomplete)   |  |
|  -0.94 | 00:39:02.088 | Sweden             | Sweden             | 59 | Ball Receipt*   |   -   | [100.4, 51.2]   | Incomplete Receipt (Incomplete) |  |
|  -0.94 | 00:39:02.088 | Ukraine            | Sweden             | 59 | Block           |   -   | [20.4, 25.5]    |                           |  |
|  -0.20 | 00:39:02.826 | Ukraine            | Sweden             | 59 | Ball Recovery   |   -   | [22.2, 28.3]    |                           |  |
|  -0.20 | 00:39:02.826 | Ukraine            | Sweden             | 59 | Carry           |   -   | [22.2, 28.3]    | Carry                     |  |
|  +0.00 | 00:39:03.030 | Sweden             | Sweden             | 59 | Pressure        |  Yes  | [97.6, 51.8]    |                           | **CP INITIATION** |
|  +2.05 | 00:39:05.079 | Sweden             | Sweden             | 59 | Dribbled Past   |  Yes  | [96.3, 44.4]    |                           |  |
|  +2.05 | 00:39:05.079 | Ukraine            | Sweden             | 59 | Dribble         |   -   | [23.8, 35.7]    | Complete                  |  |
|  +2.05 | 00:39:05.079 | Ukraine            | Sweden             | 59 | Carry           |   -   | [23.8, 35.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +2.60 | 00:39:05.630 | Ukraine            | Sweden             | 59 | Pass            |   -   | [23.8, 35.4]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +2.71 | 00:39:05.737 | Ukraine            | Sweden             | 59 | Ball Receipt*   |   -   | [27.5, 39.7]    | Incomplete Receipt (Incomplete) |  |
|  +2.71 | 00:39:05.737 | Sweden             | Sweden             | 59 | Block           |  Yes  | [96.7, 41.3]    |                           |  |
|  +4.38 | 00:39:07.409 | Sweden             | Sweden             | 59 | Pass            |   -   | [95.4, 46.5]    | -> Victor Nilsson         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +5.78 | 00:39:08.814 | Sweden             | Sweden             | 59 | Ball Receipt*   |   -   | [79.4, 47.5]    | Controlled Receipt        |  |
|  +5.78 | 00:39:08.814 | Sweden             | Sweden             | 59 | Pass            |   -   | [79.4, 47.5]    | -> Albin Ekdal            |  |
|  +7.01 | 00:39:10.036 | Sweden             | Sweden             | 59 | Ball Receipt*   |   -   | [82.2, 44.4]    | Controlled Receipt        |  |
|  +7.01 | 00:39:10.036 | Sweden             | Sweden             | 59 | Carry           |   -   | [82.2, 44.4]    | Carry                     |  |
|  -2.94 | 00:39:00.094 | Sweden             | Sweden             | 124 | Pass            |   -   | [36.9, 28.2]    | -> Victor Nilsson         |  |
|  -1.69 | 00:39:01.344 | Sweden             | Sweden             | 124 | Ball Receipt*   |   -   | [33.7, 41.8]    | Controlled Receipt        |  |
|  -1.69 | 00:39:01.344 | Sweden             | Sweden             | 124 | Carry           |   -   | [33.7, 41.8]    | Carry                     |  |
|  +0.27 | 00:39:03.304 | Sweden             | Sweden             | 124 | Pass            |   -   | [37.9, 46.0]    | -> Kristoffer Ols         |  |
|  +1.17 | 00:39:04.205 | Sweden             | Sweden             | 124 | Ball Receipt*   |   -   | [44.8, 57.1]    | Controlled Receipt        |  |
|  +1.17 | 00:39:04.205 | Sweden             | Sweden             | 124 | Carry           |   -   | [44.8, 57.1]    | Carry                     |  |

---

### Case 42: Episode `3794692_p6_00199cb2`
- **Match**: `3794692` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.64 | 00:04:07.850 | Sweden             | Ukraine            | 6 | Pass            |   -   | [70.6, 14.7]    | -> Alexander Isak         |  |
|  +0.00 | 00:04:08.487 | Ukraine            | Ukraine            | 6 | Pressure        |  Yes  | [38.8, 63.7]    |                           | **CP INITIATION** |
|  +0.27 | 00:04:08.753 | Sweden             | Ukraine            | 6 | Ball Receipt*   |   -   | [81.3, 16.4]    | Controlled Receipt        |  |
|  +0.27 | 00:04:08.753 | Sweden             | Ukraine            | 6 | Pass            |   -   | [81.3, 16.4]    | Incomplete (Incomplete)   |  |
|  +2.56 | 00:04:11.045 | Sweden             | Ukraine            | 6 | Ball Receipt*   |   -   | [85.5, 12.0]    | Incomplete Receipt (Incomplete) |  |
|  +2.56 | 00:04:11.045 | Ukraine            | Ukraine            | 6 | Pass            |   -   | [29.1, 70.9]    | -> Andriy Yarmole         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +3.58 | 00:04:12.065 | Ukraine            | Ukraine            | 6 | Ball Receipt*   |   -   | [46.8, 76.1]    | Controlled Receipt        |  |
|  +3.58 | 00:04:12.065 | Ukraine            | Ukraine            | 6 | Carry           |   -   | [46.8, 76.1]    | Carry                     |  |
|  +5.19 | 00:04:13.680 | Ukraine            | Ukraine            | 6 | Pass            |   -   | [46.8, 76.1]    | Incomplete (Incomplete)   |  |
|  +5.27 | 00:04:13.752 | Ukraine            | Ukraine            | 6 | Ball Receipt*   |   -   | [56.7, 71.7]    | Incomplete Receipt (Incomplete) |  |
|  +5.27 | 00:04:13.752 | Sweden             | Ukraine            | 6 | Block           |   -   | [71.7, 3.7]     |                           |  |
|  +5.90 | 00:04:14.391 | Ukraine            | Ukraine            | 6 | Pass            |   -   | [49.3, 77.5]    | Incomplete (Incomplete)   |  |
|  +7.31 | 00:04:15.801 | Ukraine            | Ukraine            | 6 | Ball Receipt*   |   -   | [44.3, 71.4]    | Incomplete Receipt (Incomplete) |  |
|  +7.31 | 00:04:15.801 | Sweden             | Ukraine            | 6 | Pass            |   -   | [75.5, 4.8]     | -> Emil Peter For         |  |
|  +7.85 | 00:04:16.341 | Sweden             | Ukraine            | 6 | Ball Receipt*   |   -   | [78.8, 11.1]    | Controlled Receipt        |  |
|  +7.85 | 00:04:16.341 | Sweden             | Ukraine            | 6 | Carry           |   -   | [78.8, 11.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.89 | 00:04:16.381 | Sweden             | Ukraine            | 6 | Pass            |   -   | [78.8, 11.1]    | Incomplete (Out)          | **POSSIBLE TRANSITION** |
|  -1.06 | 00:04:07.431 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [65.5, 62.0]    | -> Taras Stepanen         |  |
|  -0.04 | 00:04:08.445 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [63.7, 47.7]    | Controlled Receipt        |  |
|  -0.04 | 00:04:08.445 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [63.7, 47.7]    | Carry                     |  |
|  +2.00 | 00:04:10.489 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [57.5, 39.6]    | -> Mykola Matvien         |  |
|  +3.53 | 00:04:12.021 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [59.5, 7.7]     | Controlled Receipt        |  |
|  +3.53 | 00:04:12.021 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [59.5, 7.7]     | Carry                     |  |
|  +6.25 | 00:04:14.736 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [73.2, 6.5]     | -> Roman Yaremchu         |  |
|  +7.33 | 00:04:15.819 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [90.9, 14.3]    | Controlled Receipt        |  |
|  +7.33 | 00:04:15.819 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [90.9, 14.3]    | Carry                     |  |
|  +7.55 | 00:04:16.040 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [91.5, 14.3]    | -> Oleksandr Zinc         |  |
|  -1.04 | 00:04:07.448 | Ukraine            | Ukraine            | 157 | Ball Receipt*   |   -   | [104.4, 12.9]   | Controlled Receipt        |  |
|  -1.04 | 00:04:07.448 | Ukraine            | Ukraine            | 157 | Carry           |   -   | [104.4, 12.9]   | Carry                     |  |
|  +1.36 | 00:04:09.848 | Ukraine            | Ukraine            | 157 | Pass            |   -   | [104.4, 10.0]   | -> Evgeny Makaren         |  |
|  +2.51 | 00:04:10.993 | Ukraine            | Ukraine            | 157 | Ball Receipt*   |   -   | [90.5, 18.1]    | Controlled Receipt        |  |
|  +2.51 | 00:04:10.993 | Ukraine            | Ukraine            | 157 | Carry           |   -   | [90.5, 18.1]    | Carry                     |  |
|  +3.20 | 00:04:11.685 | Ukraine            | Ukraine            | 157 | Pass            |   -   | [89.1, 18.0]    | -> Mykola Matvien         |  |
|  +4.67 | 00:04:13.153 | Ukraine            | Ukraine            | 157 | Ball Receipt*   |   -   | [92.5, 5.9]     | Controlled Receipt        |  |
|  +4.67 | 00:04:13.153 | Ukraine            | Ukraine            | 157 | Carry           |   -   | [92.5, 5.9]     | Carry                     |  |
|  +5.78 | 00:04:14.268 | Ukraine            | Ukraine            | 157 | Pass            |   -   | [93.0, 5.8]     | -> Oleksandr Zinc         |  |
|  +6.55 | 00:04:15.036 | Ukraine            | Ukraine            | 157 | Ball Receipt*   |   -   | [101.6, 2.5]    | Controlled Receipt        |  |
|  +6.55 | 00:04:15.036 | Ukraine            | Ukraine            | 157 | Carry           |   -   | [101.6, 2.5]    | Carry                     |  |
|  +7.74 | 00:04:16.223 | Ukraine            | Ukraine            | 157 | Pass            |   -   | [101.3, 2.7]    | -> Evgeny Makaren         |  |

---

### Case 43: Episode `3795107_p98_e3e10312`
- **Match**: `3795107` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Italy** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.71 | 00:11:54.477 | Italy              | Italy              | 25 | Ball Receipt*   |   -   | [76.6, 69.9]    | Controlled Receipt        |  |
|  -1.71 | 00:11:54.477 | Italy              | Italy              | 25 | Carry           |   -   | [76.6, 69.9]    | Carry                     |  |
|  +0.10 | 00:11:56.290 | Belgium            | Italy              | 25 | Pressure        |   -   | [38.3, 5.1]     |                           |  |
|  +0.41 | 00:11:56.598 | Belgium            | Italy              | 25 | Foul Committed  |   -   | [36.6, 3.6]     |                           |  |
|  +0.41 | 00:11:56.598 | Italy              | Italy              | 25 | Foul Won        |   -   | [83.5, 76.5]    |                           |  |
|  +0.00 | 00:11:56.191 | Italy              | Italy              | 98 | Pressure        |  Yes  | [98.7, 72.5]    |                           | **CP INITIATION** |
|  +0.49 | 00:11:56.680 | Belgium            | Italy              | 98 | Pass            |   -   | [15.9, 5.4]     | Incomplete (Incomplete)   |  |
|  +1.75 | 00:11:57.936 | Italy              | Italy              | 98 | Pass            |   -   | [75.9, 54.3]    | -> Jorge Luiz Fre         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.91 | 00:11:59.099 | Italy              | Italy              | 98 | Ball Receipt*   |   -   | [84.8, 65.5]    | Controlled Receipt        |  |
|  +2.91 | 00:11:59.099 | Italy              | Italy              | 98 | Carry           |   -   | [84.8, 65.5]    | Carry                     |  |
|  +3.50 | 00:11:59.693 | Belgium            | Italy              | 98 | Pressure        |   -   | [33.1, 10.8]    |                           |  |
|  +4.51 | 00:12:00.704 | Italy              | Italy              | 98 | Dispossessed    |   -   | [85.8, 64.5]    | Dispossessed              |  |
|  +4.51 | 00:12:00.704 | Belgium            | Belgium            | 99 | Duel            |  Yes  | [34.3, 15.6]    | Tackle, Success In Play   |  |
|  +5.75 | 00:12:01.944 | Belgium            | Belgium            | 99 | Pass            |   -   | [43.3, 13.6]    | -> Jeremy Doku            |  |
|  +6.26 | 00:12:02.449 | Italy              | Belgium            | 99 | Pressure        |  Yes  | [71.6, 69.8]    |                           |  |
|  +6.48 | 00:12:02.674 | Belgium            | Belgium            | 99 | Ball Receipt*   |   -   | [49.3, 7.1]     | Controlled Receipt        |  |
|  +6.48 | 00:12:02.674 | Belgium            | Belgium            | 99 | Carry           |   -   | [49.3, 7.1]     | Carry                     |  |
|  +7.12 | 00:12:03.307 | Italy              | Belgium            | 99 | Dribbled Past   |  Yes  | [71.1, 72.3]    |                           |  |
|  +7.12 | 00:12:03.307 | Belgium            | Belgium            | 99 | Dribble         |   -   | [49.0, 7.8]     | Complete                  |  |
|  +7.12 | 00:12:03.307 | Belgium            | Belgium            | 99 | Carry           |   -   | [49.0, 7.8]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.40 | 00:12:03.594 | Italy              | Belgium            | 99 | Pressure        |  Yes  | [64.4, 70.3]    |                           |  |
|  +7.92 | 00:12:04.114 | Belgium            | Belgium            | 99 | Miscontrol      |   -   | [56.7, 5.2]     | Miscontrol                | **POSSIBLE TRANSITION** |

---

### Case 44: Episode `3795107_p21_ad729421`
- **Match**: `3795107` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Italy** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.86 | 00:09:19.924 | Italy              | Italy              | 21 | Pass            |   -   | [83.5, 53.9]    | -> Marco Verratti         |  |
|  -2.00 | 00:09:20.788 | Italy              | Italy              | 21 | Ball Receipt*   |   -   | [77.5, 47.9]    | Controlled Receipt        |  |
|  -2.00 | 00:09:20.788 | Italy              | Italy              | 21 | Carry           |   -   | [77.5, 47.9]    | Carry                     |  |
|  -1.96 | 00:09:20.828 | Italy              | Italy              | 21 | Pass            |   -   | [77.5, 47.9]    | Incomplete (Incomplete)   |  |
|  -0.38 | 00:09:22.405 | Italy              | Italy              | 21 | Ball Receipt*   |   -   | [86.9, 18.6]    | Incomplete Receipt (Incomplete) |  |
|  -0.38 | 00:09:22.405 | Belgium            | Italy              | 21 | Interception    |   -   | [30.9, 55.3]    | Won                       |  |
|  -0.38 | 00:09:22.405 | Belgium            | Italy              | 21 | Carry           |   -   | [30.9, 55.3]    | Carry                     |  |
|  +0.00 | 00:09:22.785 | Italy              | Italy              | 21 | Pressure        |  Yes  | [83.0, 24.1]    |                           | **CP INITIATION** |
|  +0.62 | 00:09:23.407 | Belgium            | Italy              | 21 | Pass            |   -   | [36.2, 56.0]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +2.78 | 00:09:25.566 | Belgium            | Italy              | 21 | Ball Receipt*   |   -   | [56.1, 51.5]    | Incomplete Receipt (Incomplete) |  |
|  +2.78 | 00:09:25.566 | Belgium            | Italy              | 21 | Duel            |   -   | [56.3, 49.6]    | Aerial Lost               |  |
|  +2.78 | 00:09:25.566 | Italy              | Italy              | 21 | Pass            |   -   | [63.8, 30.5]    | -> Leonardo Spina         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +4.64 | 00:09:27.426 | Italy              | Italy              | 21 | Ball Receipt*   |   -   | [70.0, 11.1]    | Controlled Receipt        |  |
|  +4.64 | 00:09:27.426 | Italy              | Italy              | 21 | Carry           |   -   | [70.0, 11.1]    | Carry                     |  |
|  +7.09 | 00:09:29.872 | Italy              | Italy              | 21 | Pass            |   -   | [70.2, 11.1]    | -> Marco Verratti         |  |
|  -1.95 | 00:09:20.838 | Belgium            | Belgium            | 94 | Pass            |   -   | [94.4, 12.9]    | -> Youri Tieleman         |  |
|  -1.04 | 00:09:21.743 | Belgium            | Belgium            | 94 | Ball Receipt*   |   -   | [80.7, 30.6]    | Controlled Receipt        |  |
|  -1.04 | 00:09:21.743 | Belgium            | Belgium            | 94 | Carry           |   -   | [80.7, 30.6]    | Carry                     |  |
|  -0.94 | 00:09:21.848 | Belgium            | Belgium            | 94 | Pass            |   -   | [80.7, 30.6]    | -> Axel Witsel            |  |
|  -0.03 | 00:09:22.752 | Belgium            | Belgium            | 94 | Ball Receipt*   |   -   | [75.2, 17.9]    | Controlled Receipt        |  |
|  -0.03 | 00:09:22.752 | Belgium            | Belgium            | 94 | Carry           |   -   | [75.2, 17.9]    | Carry                     |  |
|  +1.08 | 00:09:23.868 | Belgium            | Belgium            | 94 | Pass            |   -   | [78.1, 20.8]    | -> Toby Alderweir         |  |
|  +2.51 | 00:09:25.295 | Belgium            | Belgium            | 94 | Ball Receipt*   |   -   | [72.7, 56.7]    | Controlled Receipt        |  |
|  +2.51 | 00:09:25.295 | Belgium            | Belgium            | 94 | Carry           |   -   | [72.7, 56.7]    | Carry                     |  |
|  +4.54 | 00:09:27.329 | Belgium            | Belgium            | 94 | Pass            |   -   | [80.4, 59.0]    | -> Youri Tieleman         |  |
|  +4.83 | 00:09:27.611 | Italy              | Belgium            | 94 | Pressure        |   -   | [32.7, 25.1]    |                           |  |
|  +5.30 | 00:09:28.081 | Belgium            | Belgium            | 94 | Ball Receipt*   |   -   | [90.6, 56.4]    | Controlled Receipt        |  |
|  +5.30 | 00:09:28.081 | Belgium            | Belgium            | 94 | Carry           |   -   | [90.6, 56.4]    | Carry                     |  |
|  +6.23 | 00:09:29.012 | Italy              | Belgium            | 94 | Dribbled Past   |   -   | [27.2, 21.1]    |                           |  |
|  +6.23 | 00:09:29.012 | Belgium            | Belgium            | 94 | Dribble         |   -   | [92.9, 59.0]    | Complete                  |  |
|  +6.23 | 00:09:29.012 | Belgium            | Belgium            | 94 | Carry           |   -   | [92.9, 59.0]    | Carry                     |  |
|  +7.43 | 00:09:30.219 | Belgium            | Belgium            | 94 | Pass            |   -   | [95.1, 63.9]    | -> Thomas Meunier         | **OPPONENT LAST CONTROL** |

---

### Case 45: Episode `3795107_p17_cd94a01c`
- **Match**: `3795107` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Belgium** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Belgium`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.02 | 00:07:02.907 | Belgium            | Italy              | 16 | Pressure        |   -   | [35.4, 41.9]    |                           |  |
|  -1.84 | 00:07:03.084 | Belgium            | Italy              | 16 | Ball Receipt*   |   -   | [35.6, 41.0]    | Incomplete Receipt (Incomplete) |  |
|  -1.84 | 00:07:03.084 | Italy              | Italy              | 16 | Interception    |   -   | [82.8, 38.5]    | Won                       |  |
|  -1.84 | 00:07:03.084 | Italy              | Italy              | 16 | Carry           |   -   | [82.8, 38.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:07:04.928 | Italy              | Italy              | 16 | Dribble         |   -   | [85.4, 35.0]    | Incomplete                |  |
|  +0.00 | 00:07:04.928 | Belgium            | Belgium            | 17 | Duel            |  Yes  | [34.7, 45.1]    | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.84 | 00:07:05.770 | Belgium            | Belgium            | 17 | Pass            |   -   | [26.6, 51.9]    | -> Romelu Lukaku          | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.93 | 00:07:06.860 | Italy              | Belgium            | 17 | Pressure        |  Yes  | [68.1, 24.3]    |                           |  |
|  +2.09 | 00:07:07.019 | Belgium            | Belgium            | 17 | Ball Receipt*   |   -   | [49.7, 57.9]    | Controlled Receipt        |  |
|  +2.09 | 00:07:07.019 | Belgium            | Belgium            | 17 | Carry           |   -   | [49.7, 57.9]    | Carry                     |  |
|  +3.51 | 00:07:08.442 | Italy              | Belgium            | 17 | Foul Committed  |  Yes  | [69.8, 23.1]    |                           |  |
|  +3.51 | 00:07:08.442 | Belgium            | Belgium            | 17 | Foul Won        |   -   | [50.3, 57.0]    |                           |  |
|  +3.51 | 00:07:08.442 | Belgium            | Belgium            | 17 | Carry           |   -   | [50.3, 57.0]    | Carry                     |  |
|  +4.31 | 00:07:09.236 | Belgium            | Belgium            | 17 | Pass            |   -   | [50.3, 56.6]    | -> Thomas Meunier         |  |
|  +5.64 | 00:07:10.565 | Belgium            | Belgium            | 17 | Ball Receipt*   |   -   | [49.5, 73.1]    | Controlled Receipt        |  |
|  +5.64 | 00:07:10.565 | Belgium            | Belgium            | 17 | Carry           |   -   | [49.5, 73.1]    | Carry                     |  |
|  +5.68 | 00:07:10.605 | Belgium            | Belgium            | 17 | Pass            |   -   | [49.5, 73.1]    | Incomplete (Incomplete)   |  |
|  -1.82 | 00:07:03.103 | Belgium            | Belgium            | 91 | Pass            |   -   | [32.6, 73.2]    | -> Thomas Vermael         |  |
|  -0.31 | 00:07:04.618 | Belgium            | Belgium            | 91 | Ball Receipt*   |   -   | [27.8, 62.7]    | Controlled Receipt        |  |
|  +0.51 | 00:07:05.443 | Belgium            | Belgium            | 91 | Pass            |   -   | [22.4, 57.9]    | -> Jan Vertonghen         |  |
|  +2.40 | 00:07:07.332 | Belgium            | Belgium            | 91 | Ball Receipt*   |   -   | [28.8, 19.8]    | Controlled Receipt        |  |
|  +4.19 | 00:07:09.115 | Belgium            | Belgium            | 91 | Pass            |   -   | [36.0, 17.8]    | -> Thorgan Hazard         |  |
|  +5.50 | 00:07:10.428 | Belgium            | Belgium            | 91 | Ball Receipt*   |   -   | [63.4, 6.4]     | Controlled Receipt        |  |
|  +5.50 | 00:07:10.428 | Belgium            | Belgium            | 91 | Carry           |   -   | [63.4, 6.4]     | Carry                     |  |
|  +7.81 | 00:07:12.742 | Belgium            | Belgium            | 91 | Pass            |   -   | [63.4, 7.1]     | -> Jan Vertonghen         |  |

---

### Case 46: Episode `3795107_p11_536c4bf1`
- **Match**: `3795107` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Italy** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.58 | 00:03:23.424 | Belgium            | Belgium            | 10 | Ball Recovery   |   -   | [83.3, 1.2]     |                           |  |
|  -2.58 | 00:03:23.424 | Belgium            | Belgium            | 10 | Carry           |   -   | [83.3, 1.2]     | Carry                     |  |
|  -2.44 | 00:03:23.563 | Italy              | Belgium            | 10 | Pressure        |   -   | [34.3, 78.9]    |                           |  |
|  -1.73 | 00:03:24.274 | Italy              | Belgium            | 10 | Dribbled Past   |   -   | [34.9, 79.5]    |                           |  |
|  -1.73 | 00:03:24.274 | Belgium            | Belgium            | 10 | Dribble         |   -   | [85.2, 0.6]     | Complete                  |  |
|  -1.73 | 00:03:24.274 | Belgium            | Belgium            | 10 | Carry           |   -   | [85.2, 0.6]     | Carry                     |  |
|  -1.06 | 00:03:24.940 | Italy              | Belgium            | 10 | Pressure        |   -   | [33.8, 78.2]    |                           |  |
|  +0.00 | 00:03:26.001 | Belgium            | Belgium            | 10 | Dispossessed    |   -   | [92.5, 2.5]     | Dispossessed              |  |
|  +0.00 | 00:03:26.001 | Italy              | Italy              | 11 | Duel            |  Yes  | [27.6, 77.6]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.44 | 00:03:26.444 | Italy              | Italy              | 11 | Pass            |   -   | [26.1, 74.0]    | -> Marco Verratti         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.53 | 00:03:27.530 | Italy              | Italy              | 11 | Ball Receipt*   |   -   | [29.6, 77.0]    | Controlled Receipt        |  |
|  +1.53 | 00:03:27.530 | Italy              | Italy              | 11 | Carry           |   -   | [29.6, 77.0]    | Carry                     |  |
|  +1.92 | 00:03:27.918 | Italy              | Italy              | 11 | Pass            |   -   | [30.2, 75.7]    | -> Federico Chies         |  |
|  +3.17 | 00:03:29.168 | Italy              | Italy              | 11 | Ball Receipt*   |   -   | [48.6, 77.6]    | Controlled Receipt        |  |
|  +3.17 | 00:03:29.168 | Italy              | Italy              | 11 | Carry           |   -   | [48.6, 77.6]    | Carry                     |  |
|  +3.38 | 00:03:29.378 | Belgium            | Italy              | 11 | Pressure        |  Yes  | [64.9, 2.5]     |                           |  |
|  +3.86 | 00:03:29.860 | Italy              | Italy              | 11 | Dribble         |   -   | [51.6, 78.5]    | Incomplete                |  |
|  +3.86 | 00:03:29.860 | Belgium            | Italy              | 11 | Duel            |  Yes  | [68.5, 1.6]     | Tackle, Success Out       |  |
|  -2.94 | 00:03:23.059 | Belgium            | Belgium            | 84 | Pass            |   -   | [9.2, 51.7]     | -> Thomas Meunier         |  |
|  -1.16 | 00:03:24.843 | Belgium            | Belgium            | 84 | Ball Receipt*   |   -   | [25.1, 76.4]    | Controlled Receipt        |  |
|  -1.16 | 00:03:24.843 | Belgium            | Belgium            | 84 | Carry           |   -   | [25.1, 76.4]    | Carry                     |  |
|  -0.44 | 00:03:25.557 | Belgium            | Belgium            | 84 | Pass            |   -   | [25.3, 77.4]    | -> Romelu Lukaku          |  |
|  +0.73 | 00:03:26.733 | Italy              | Belgium            | 84 | Pressure        |   -   | [56.1, 3.0]     |                           |  |
|  +1.33 | 00:03:27.332 | Belgium            | Belgium            | 84 | Ball Receipt*   |   -   | [63.4, 75.7]    | Controlled Receipt        |  |
|  +1.33 | 00:03:27.332 | Belgium            | Belgium            | 84 | Carry           |   -   | [63.4, 75.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +1.37 | 00:03:27.372 | Belgium            | Belgium            | 84 | Miscontrol      |   -   | [61.2, 77.6]    | Miscontrol                | **POSSIBLE TRANSITION** |
|  +3.16 | 00:03:29.166 | Italy              | Italy              | 85 | Pass            |   -   | [64.9, 5.4]     | -> Marco Verratti         |  |
|  +3.86 | 00:03:29.865 | Italy              | Italy              | 85 | Ball Receipt*   |   -   | [72.8, 4.9]     | Controlled Receipt        |  |
|  +3.86 | 00:03:29.865 | Italy              | Italy              | 85 | Carry           |   -   | [72.8, 4.9]     | Carry                     |  |
|  +5.94 | 00:03:31.937 | Italy              | Italy              | 85 | Pass            |   -   | [73.8, 7.5]     | -> Lorenzo Insign         |  |
|  +6.52 | 00:03:32.522 | Italy              | Italy              | 85 | Ball Receipt*   |   -   | [84.5, 2.7]     | Controlled Receipt        |  |
|  +6.52 | 00:03:32.522 | Italy              | Italy              | 85 | Carry           |   -   | [84.5, 2.7]     | Carry                     |  |
|  +6.56 | 00:03:32.562 | Italy              | Italy              | 85 | Pass            |   -   | [81.8, 4.9]     | -> Marco Verratti         |  |
|  +7.31 | 00:03:33.307 | Italy              | Italy              | 85 | Ball Receipt*   |   -   | [77.0, 1.5]     | Controlled Receipt        |  |
|  +7.31 | 00:03:33.307 | Italy              | Italy              | 85 | Carry           |   -   | [77.0, 1.5]     | Carry                     |  |
|  +7.35 | 00:03:33.347 | Italy              | Italy              | 85 | Pass            |   -   | [77.0, 1.5]     | -> Lorenzo Insign         |  |
|  +7.83 | 00:03:33.827 | Italy              | Italy              | 85 | Ball Receipt*   |   -   | [76.4, 8.0]     | Controlled Receipt        |  |
|  +7.83 | 00:03:33.827 | Italy              | Italy              | 85 | Carry           |   -   | [76.4, 8.0]     | Carry                     |  |

---

### Case 47: Episode `3788765_p17_d24e1957`
- **Match**: `3788765` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.89 | 00:09:19.050 | Switzerland        | Switzerland        | 16 | Ball Receipt*   |   -   | [77.7, 76.7]    | Controlled Receipt        |  |
|  -1.89 | 00:09:19.050 | Switzerland        | Switzerland        | 16 | Carry           |   -   | [77.7, 76.7]    | Carry                     |  |
|  -1.40 | 00:09:19.536 | Switzerland        | Switzerland        | 16 | Pass            |   -   | [77.7, 76.7]    | -> Remo Freuler           |  |
|  -0.75 | 00:09:20.189 | Turkey             | Switzerland        | 16 | Pressure        |   -   | [37.1, 11.3]    |                           |  |
|  -0.61 | 00:09:20.329 | Switzerland        | Switzerland        | 16 | Ball Receipt*   |   -   | [83.2, 72.0]    | Controlled Receipt        |  |
|  -0.61 | 00:09:20.329 | Switzerland        | Switzerland        | 16 | Carry           |   -   | [83.2, 72.0]    | Carry                     |  |
|  +0.00 | 00:09:20.937 | Switzerland        | Switzerland        | 16 | Dispossessed    |   -   | [84.3, 72.0]    | Dispossessed              |  |
|  +0.00 | 00:09:20.937 | Turkey             | Turkey             | 17 | Duel            |  Yes  | [35.8, 8.1]     | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.36 | 00:09:21.294 | Switzerland        | Turkey             | 17 | Pressure        |  Yes  | [84.3, 72.0]    |                           |  |
|  +1.32 | 00:09:22.253 | Turkey             | Turkey             | 17 | Pass            |   -   | [42.0, 5.9]     | -> İrfan Can Kahv         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.78 | 00:09:22.716 | Turkey             | Turkey             | 17 | Ball Receipt*   |   -   | [39.8, 9.8]     | Controlled Receipt        |  |
|  +1.78 | 00:09:22.716 | Turkey             | Turkey             | 17 | Carry           |   -   | [39.8, 9.8]     | Carry                     |  |
|  +1.87 | 00:09:22.809 | Switzerland        | Turkey             | 17 | Pressure        |  Yes  | [79.6, 74.2]    |                           |  |
|  +2.76 | 00:09:23.697 | Turkey             | Turkey             | 17 | Dispossessed    |   -   | [44.4, 10.4]    | Dispossessed              |  |
|  +2.76 | 00:09:23.697 | Switzerland        | Turkey             | 17 | Duel            |  Yes  | [75.7, 69.7]    | Tackle, Lost In Play      |  |
|  +4.56 | 00:09:25.497 | Turkey             | Turkey             | 17 | Pass            |   -   | [42.0, 17.3]    | -> Mert Müldür            |  |
|  +6.22 | 00:09:27.152 | Turkey             | Turkey             | 17 | Ball Receipt*   |   -   | [34.9, 3.6]     | Controlled Receipt        |  |
|  +6.22 | 00:09:27.152 | Turkey             | Turkey             | 17 | Carry           |   -   | [34.9, 3.6]     | Carry                     |  |
|  +6.56 | 00:09:27.493 | Turkey             | Turkey             | 17 | Pass            |   -   | [34.9, 3.6]     | -> Caglar Söyüncü         |  |
|  +7.72 | 00:09:28.655 | Switzerland        | Turkey             | 17 | Pressure        |   -   | [91.6, 61.1]    |                           |  |
|  +7.85 | 00:09:28.789 | Turkey             | Turkey             | 17 | Ball Receipt*   |   -   | [26.2, 13.6]    | Controlled Receipt        |  |
|  +7.85 | 00:09:28.789 | Turkey             | Turkey             | 17 | Carry           |   -   | [26.2, 13.6]    | Carry                     |  |
|  -1.97 | 00:09:18.969 | Switzerland        | Switzerland        | 111 | Ball Receipt*   |   -   | [89.5, 7.2]     | Controlled Receipt        |  |
|  -1.97 | 00:09:18.969 | Switzerland        | Switzerland        | 111 | Carry           |   -   | [89.5, 7.2]     | Carry                     |  |
|  +0.25 | 00:09:21.184 | Switzerland        | Switzerland        | 111 | Pass            |   -   | [90.4, 7.2]     | -> Ricardo Iván R         |  |
|  +1.39 | 00:09:22.326 | Switzerland        | Switzerland        | 111 | Ball Receipt*   |   -   | [80.8, 8.1]     | Controlled Receipt        |  |
|  +1.39 | 00:09:22.326 | Switzerland        | Switzerland        | 111 | Carry           |   -   | [80.8, 8.1]     | Carry                     |  |
|  +2.45 | 00:09:23.391 | Switzerland        | Switzerland        | 111 | Pass            |   -   | [80.2, 8.9]     | -> Granit Xhaka           |  |
|  +3.33 | 00:09:24.269 | Switzerland        | Switzerland        | 111 | Ball Receipt*   |   -   | [75.6, 17.7]    | Controlled Receipt        |  |
|  +3.33 | 00:09:24.269 | Switzerland        | Switzerland        | 111 | Pass            |   -   | [75.6, 17.7]    | -> Ricardo Iván R         |  |
|  +4.35 | 00:09:25.286 | Switzerland        | Switzerland        | 111 | Ball Receipt*   |   -   | [70.7, 10.4]    | Controlled Receipt        |  |
|  +4.35 | 00:09:25.286 | Switzerland        | Switzerland        | 111 | Carry           |   -   | [70.7, 10.4]    | Carry                     |  |
|  +6.84 | 00:09:27.778 | Switzerland        | Switzerland        | 111 | Pass            |   -   | [63.9, 20.6]    | -> Granit Xhaka           |  |
|  +7.60 | 00:09:28.538 | Switzerland        | Switzerland        | 111 | Ball Receipt*   |   -   | [69.7, 19.1]    | Controlled Receipt        |  |
|  +7.60 | 00:09:28.538 | Switzerland        | Switzerland        | 111 | Carry           |   -   | [69.7, 19.1]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 48: Episode `3788765_p128_0ad91d2e`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +1.48 | 00:18:28.026 | Turkey             | Turkey             | 42 | Pass            |   -   | [84.6, 55.5]    | Incomplete (Incomplete)   |  |
|  +3.18 | 00:18:29.724 | Turkey             | Turkey             | 42 | Ball Receipt*   |   -   | [87.3, 15.3]    | Incomplete Receipt (Incomplete) |  |
|  +3.18 | 00:18:29.724 | Switzerland        | Switzerland        | 43 | Interception    |   -   | [33.2, 58.1]    | Won                       |  |
|  +3.18 | 00:18:29.724 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [33.2, 58.1]    | Carry                     |  |
|  +5.38 | 00:18:31.919 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [26.4, 55.4]    | -> Nico Elvedi            |  |
|  +6.11 | 00:18:32.655 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [18.4, 53.4]    | Controlled Receipt        |  |
|  +6.11 | 00:18:32.655 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [18.4, 53.4]    | Carry                     |  |
|  +7.36 | 00:18:33.901 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [19.3, 53.0]    | -> Granit Xhaka           |  |
|  -2.55 | 00:18:23.995 | Turkey             | Switzerland        | 127 | Pressure        |   -   | [14.3, 70.2]    |                           |  |
|  -1.05 | 00:18:25.496 | Turkey             | Switzerland        | 127 | Dribbled Past   |   -   | [5.9, 62.4]     |                           |  |
|  -1.05 | 00:18:25.496 | Switzerland        | Switzerland        | 127 | Dribble         |   -   | [114.2, 17.7]   | Complete                  |  |
|  -1.05 | 00:18:25.496 | Switzerland        | Switzerland        | 127 | Carry           |   -   | [114.2, 17.7]   | Carry                     |  |
|  -0.71 | 00:18:25.832 | Turkey             | Switzerland        | 127 | Pressure        |   -   | [9.2, 63.0]     |                           |  |
|  +0.00 | 00:18:26.543 | Switzerland        | Switzerland        | 127 | Dispossessed    |   -   | [115.0, 23.2]   | Dispossessed              |  |
|  +0.00 | 00:18:26.543 | Turkey             | Turkey             | 128 | Duel            |  Yes  | [5.1, 56.9]     | Tackle, Success In Play   | **CP INITIATION** |
|  +0.63 | 00:18:27.177 | Turkey             | Turkey             | 128 | Pass            |   -   | [11.7, 56.3]    | -> İrfan Can Kahv         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.51 | 00:18:28.051 | Turkey             | Turkey             | 128 | Ball Receipt*   |   -   | [14.1, 54.2]    | Controlled Receipt        |  |
|  +1.51 | 00:18:28.051 | Turkey             | Turkey             | 128 | Carry           |   -   | [14.1, 54.2]    | Carry                     |  |
|  +1.53 | 00:18:28.070 | Switzerland        | Turkey             | 128 | Pressure        |  Yes  | [102.0, 26.4]   |                           |  |
|  +1.79 | 00:18:28.331 | Turkey             | Turkey             | 128 | Pass            |   -   | [14.3, 54.2]    | -> Okay Yokuşlu           |  |
|  +2.13 | 00:18:28.674 | Turkey             | Turkey             | 128 | Ball Receipt*   |   -   | [16.4, 56.0]    | Controlled Receipt        |  |
|  +2.13 | 00:18:28.674 | Turkey             | Turkey             | 128 | Carry           |   -   | [16.4, 56.0]    | Carry                     |  |
|  +2.32 | 00:18:28.864 | Turkey             | Turkey             | 128 | Dribble         |   -   | [16.6, 55.2]    | Incomplete                |  |
|  +2.32 | 00:18:28.864 | Switzerland        | Switzerland        | 129 | Duel            |  Yes  | [103.5, 24.9]   | Tackle, Won               |  |
|  +2.32 | 00:18:28.864 | Switzerland        | Switzerland        | 129 | Carry           |   -   | [103.5, 24.9]   | Carry                     |  |
|  +2.62 | 00:18:29.165 | Turkey             | Switzerland        | 129 | Pressure        |  Yes  | [12.3, 59.8]    |                           |  |
|  +3.17 | 00:18:29.710 | Turkey             | Switzerland        | 129 | Dribbled Past   |  Yes  | [13.5, 58.3]    |                           |  |
|  +3.17 | 00:18:29.710 | Switzerland        | Switzerland        | 129 | Dribble         |   -   | [106.6, 21.8]   | Complete                  |  |
|  +3.17 | 00:18:29.710 | Switzerland        | Switzerland        | 129 | Carry           |   -   | [106.6, 21.8]   | Carry                     |  |
|  +3.25 | 00:18:29.791 | Turkey             | Switzerland        | 129 | Pressure        |  Yes  | [11.4, 55.2]    |                           |  |
|  +3.94 | 00:18:30.483 | Turkey             | Switzerland        | 129 | Dribbled Past   |  Yes  | [14.1, 58.1]    |                           |  |
|  +3.94 | 00:18:30.483 | Switzerland        | Switzerland        | 129 | Dribble         |   -   | [106.0, 22.0]   | Complete                  |  |
|  +3.94 | 00:18:30.483 | Switzerland        | Switzerland        | 129 | Carry           |   -   | [106.0, 22.0]   | Carry                     | **OPPONENT LAST CONTROL** |
|  +4.64 | 00:18:31.187 | Turkey             | Switzerland        | 129 | Pressure        |  Yes  | [9.4, 61.6]     |                           |  |
|  +5.86 | 00:18:32.407 | Turkey             | Switzerland        | 129 | Pressure        |  Yes  | [10.8, 66.2]    |                           |  |
|  +6.31 | 00:18:32.851 | Switzerland        | Switzerland        | 129 | Pass            |   -   | [114.5, 8.1]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +6.79 | 00:18:33.336 | Turkey             | Switzerland        | 129 | Interception    |  Yes  | [12.5, 71.4]    | Lost Out                  |  |

---

### Case 49: Episode `3788765_p109_0088df76`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Switzerland** vs Actual Opponent: **Turkey** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.62 | 00:07:57.060 | Switzerland        | Switzerland        | 15 | Ball Receipt*   |   -   | [25.1, 58.1]    | Controlled Receipt        |  |
|  -2.62 | 00:07:57.060 | Switzerland        | Switzerland        | 15 | Carry           |   -   | [25.1, 58.1]    | Carry                     |  |
|  -1.66 | 00:07:58.022 | Switzerland        | Switzerland        | 15 | Pass            |   -   | [25.1, 58.1]    | -> Remo Freuler           |  |
|  -0.97 | 00:07:58.719 | Switzerland        | Switzerland        | 15 | Ball Receipt*   |   -   | [32.6, 57.5]    | Controlled Receipt        |  |
|  -0.97 | 00:07:58.719 | Switzerland        | Switzerland        | 15 | Pass            |   -   | [32.6, 57.5]    | -> Nico Elvedi            |  |
|  -0.26 | 00:07:59.421 | Turkey             | Switzerland        | 15 | Pressure        |   -   | [91.8, 22.4]    |                           |  |
|  -0.08 | 00:07:59.603 | Switzerland        | Switzerland        | 15 | Ball Receipt*   |   -   | [22.7, 58.6]    | Controlled Receipt        |  |
|  -0.08 | 00:07:59.603 | Switzerland        | Switzerland        | 15 | Carry           |   -   | [22.7, 58.6]    | Carry                     |  |
|  +1.41 | 00:08:01.098 | Switzerland        | Switzerland        | 15 | Pass            |   -   | [26.4, 64.1]    | -> Breel-Donald E         | **PRESSING-TEAM FIRST CONTROL** |
|  +2.03 | 00:08:01.715 | Turkey             | Switzerland        | 15 | Pressure        |   -   | [70.6, 16.0]    |                           |  |
|  +2.57 | 00:08:02.259 | Switzerland        | Switzerland        | 15 | Ball Receipt*   |   -   | [44.7, 62.8]    | Controlled Receipt        |  |
|  +2.57 | 00:08:02.259 | Switzerland        | Switzerland        | 15 | Carry           |   -   | [44.7, 62.8]    | Carry                     |  |
|  +3.52 | 00:08:03.210 | Switzerland        | Switzerland        | 15 | Pass            |   -   | [42.4, 60.1]    | -> Granit Xhaka           |  |
|  +4.46 | 00:08:04.147 | Switzerland        | Switzerland        | 15 | Ball Receipt*   |   -   | [38.3, 37.6]    | Controlled Receipt        |  |
|  +4.46 | 00:08:04.147 | Switzerland        | Switzerland        | 15 | Carry           |   -   | [38.3, 37.6]    | Carry                     |  |
|  +4.80 | 00:08:04.481 | Turkey             | Switzerland        | 15 | Pressure        |   -   | [79.4, 36.5]    |                           |  |
|  +6.09 | 00:08:05.772 | Switzerland        | Switzerland        | 15 | Pass            |   -   | [42.8, 32.5]    | -> Ricardo Iván R         |  |
|  -1.58 | 00:07:58.102 | Turkey             | Switzerland        | 109 | Pass            |   -   | [28.5, 25.2]    | -> Cengiz Ünder           |  |
|  +0.00 | 00:07:59.685 | Switzerland        | Switzerland        | 109 | Pressure        |  Yes  | [75.2, 62.4]    |                           | **CP INITIATION** |
|  +0.59 | 00:08:00.271 | Turkey             | Switzerland        | 109 | Ball Receipt*   |   -   | [44.9, 13.3]    | Controlled Receipt        |  |
|  +0.59 | 00:08:00.271 | Turkey             | Switzerland        | 109 | Carry           |   -   | [44.9, 13.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.75 | 00:08:00.439 | Turkey             | Switzerland        | 109 | Pass            |   -   | [45.1, 11.6]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +1.95 | 00:08:01.631 | Turkey             | Switzerland        | 109 | Ball Receipt*   |   -   | [54.4, 14.8]    | Incomplete Receipt (Incomplete) |  |
|  +1.95 | 00:08:01.631 | Switzerland        | Switzerland        | 109 | Pass            |   -   | [73.5, 59.2]    | -> Nico Elvedi            | (v2.6 Regain Event) |
|  +3.02 | 00:08:02.710 | Switzerland        | Switzerland        | 109 | Ball Receipt*   |   -   | [56.1, 57.5]    | Controlled Receipt        |  |
|  +3.02 | 00:08:02.710 | Switzerland        | Switzerland        | 109 | Carry           |   -   | [56.1, 57.5]    | Carry                     |  |
|  +4.43 | 00:08:04.113 | Switzerland        | Switzerland        | 109 | Pass            |   -   | [61.0, 56.0]    | -> Granit Xhaka           |  |
|  +5.43 | 00:08:05.118 | Switzerland        | Switzerland        | 109 | Ball Receipt*   |   -   | [61.0, 47.0]    | Controlled Receipt        |  |
|  +5.43 | 00:08:05.118 | Switzerland        | Switzerland        | 109 | Carry           |   -   | [61.0, 47.0]    | Carry                     |  |

---

### Case 50: Episode `3788765_p100_108f557a`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.21 | 00:03:39.842 | Turkey             | Turkey             | 9 | Ball Receipt*   |   -   | [93.1, 40.1]    | Controlled Receipt        |  |
|  -2.05 | 00:03:40.002 | Turkey             | Turkey             | 9 | Shot            |   -   | [94.1, 46.0]    | Off T                     |  |
|  -0.41 | 00:03:41.643 | Switzerland        | Turkey             | 9 | Goal Keeper     |   -   | [1.9, 39.3]     |                           |  |
|  -1.84 | 00:03:40.212 | Switzerland        | Turkey             | 100 | Pressure        |   -   | [36.9, 8.9]     |                           |  |
|  -1.23 | 00:03:40.818 | Turkey             | Turkey             | 100 | Pass            |   -   | [88.1, 71.4]    | Incomplete (Incomplete)   |  |
|  -0.90 | 00:03:41.157 | Turkey             | Turkey             | 100 | Pressure        |   -   | [91.3, 58.9]    |                           |  |
|  -0.52 | 00:03:41.532 | Turkey             | Turkey             | 100 | Ball Receipt*   |   -   | [92.7, 59.8]    | Incomplete Receipt (Incomplete) |  |
|  -0.52 | 00:03:41.532 | Switzerland        | Turkey             | 100 | Ball Recovery   |   -   | [27.0, 19.4]    |                           |  |
|  -0.52 | 00:03:41.532 | Switzerland        | Turkey             | 100 | Carry           |   -   | [27.0, 19.4]    | Carry                     |  |
|  +0.00 | 00:03:42.052 | Turkey             | Turkey             | 100 | Dribbled Past   |  Yes  | [92.2, 60.4]    |                           | **CP INITIATION** |
|  +0.00 | 00:03:42.052 | Switzerland        | Turkey             | 100 | Dribble         |   -   | [27.9, 19.7]    | Complete                  |  |
|  +0.00 | 00:03:42.052 | Switzerland        | Turkey             | 100 | Carry           |   -   | [27.9, 19.7]    | Carry                     |  |
|  +1.33 | 00:03:43.384 | Switzerland        | Turkey             | 100 | Pass            |   -   | [31.4, 24.7]    | -> Haris Seferovi         | **OPPONENT LAST CONTROL** |
|  +2.73 | 00:03:44.781 | Turkey             | Turkey             | 100 | Pressure        |  Yes  | [62.9, 44.7]    |                           |  |
|  +2.98 | 00:03:45.036 | Switzerland        | Turkey             | 100 | Ball Receipt*   |   -   | [52.0, 35.7]    | Controlled Receipt        |  |
|  +2.98 | 00:03:45.036 | Switzerland        | Turkey             | 100 | Pass            |   -   | [51.8, 36.6]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +4.35 | 00:03:46.399 | Turkey             | Turkey             | 100 | Pass            |   -   | [63.7, 51.9]    | -> Caglar Söyüncü         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +5.84 | 00:03:47.889 | Turkey             | Turkey             | 100 | Ball Receipt*   |   -   | [56.8, 38.8]    | Controlled Receipt        |  |
|  +5.84 | 00:03:47.889 | Turkey             | Turkey             | 100 | Carry           |   -   | [56.8, 38.8]    | Carry                     |  |
|  +5.92 | 00:03:47.973 | Turkey             | Turkey             | 100 | Pass            |   -   | [55.6, 38.8]    | -> Kaan Ayhan             |  |
|  +7.05 | 00:03:49.101 | Turkey             | Turkey             | 100 | Ball Receipt*   |   -   | [55.8, 45.0]    | Controlled Receipt        |  |
|  +7.05 | 00:03:49.101 | Turkey             | Turkey             | 100 | Carry           |   -   | [55.8, 45.0]    | Carry                     |  |

---

### Case 51: Episode `3788765_p96_f1fec877`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +4.26 | 00:02:22.167 | Turkey             | Turkey             | 7 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete)   |  |
|  +5.60 | 00:02:23.510 | Turkey             | Turkey             | 7 | Ball Receipt*   |   -   | [112.6, 36.7]   | Incomplete Receipt (Incomplete) |  |
|  +5.60 | 00:02:23.510 | Turkey             | Turkey             | 7 | Duel            |   -   | [114.1, 36.1]   | Aerial Lost               |  |
|  +5.60 | 00:02:23.510 | Switzerland        | Turkey             | 7 | Clearance       |   -   | [6.0, 44.0]     |                           |  |
|  -1.73 | 00:02:16.177 | Turkey             | Turkey             | 95 | Ball Receipt*   |   -   | [90.8, 58.1]    | Incomplete Receipt (Incomplete) |  |
|  -1.73 | 00:02:16.177 | Switzerland        | Switzerland        | 96 | Pass            |  Yes  | [36.4, 17.7]    | -> Remo Freuler           |  |
|  +0.00 | 00:02:17.907 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [41.0, 27.3]    | Controlled Receipt        |  |
|  +0.00 | 00:02:17.907 | Turkey             | Switzerland        | 96 | Duel            |  Yes  | [79.1, 52.8]    | Aerial Lost               | **CP INITIATION** |
|  +0.00 | 00:02:17.907 | Switzerland        | Switzerland        | 96 | Pass            |   -   | [41.0, 27.3]    | -> Ricardo Iván R         |  |
|  +1.94 | 00:02:19.844 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [36.0, 20.8]    | Controlled Receipt        |  |
|  +1.94 | 00:02:19.844 | Switzerland        | Switzerland        | 96 | Pass            |   -   | [36.0, 20.8]    | Incomplete (Incomplete)   |  |
|  +3.27 | 00:02:21.174 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [43.6, 20.3]    | Incomplete Receipt (Incomplete) |  |
|  +3.27 | 00:02:21.174 | Turkey             | Switzerland        | 96 | Pass            |   -   | [73.8, 59.8]    | -> Mehmet Zeki Çe         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +3.65 | 00:02:21.554 | Switzerland        | Switzerland        | 96 | Pressure        |  Yes  | [56.7, 12.4]    |                           |  |
|  +4.58 | 00:02:22.491 | Turkey             | Switzerland        | 96 | Ball Receipt*   |   -   | [64.0, 63.2]    | Controlled Receipt        |  |
|  +4.58 | 00:02:22.491 | Turkey             | Switzerland        | 96 | Carry           |   -   | [64.0, 63.2]    | Carry                     |  |
|  +4.73 | 00:02:22.642 | Turkey             | Switzerland        | 96 | Miscontrol      |   -   | [64.0, 62.4]    | Miscontrol                |  |
|  +6.78 | 00:02:24.686 | Switzerland        | Switzerland        | 96 | Ball Recovery   |   -   | [48.3, 3.8]     |                           |  |
|  +6.78 | 00:02:24.686 | Switzerland        | Switzerland        | 96 | Carry           |   -   | [48.3, 3.8]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.05 | 00:02:24.953 | Turkey             | Switzerland        | 96 | Pressure        |   -   | [67.2, 70.0]    |                           |  |
|  +7.84 | 00:02:25.747 | Switzerland        | Switzerland        | 96 | Pass            |   -   | [50.6, 2.0]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +7.92 | 00:02:25.823 | Turkey             | Switzerland        | 96 | Block           |   -   | [67.5, 76.9]    |                           |  |

---

### Case 52: Episode `3788765_p43_dc378187`
- **Match**: `3788765` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Switzerland** vs Actual Opponent: **Turkey** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.40 | 00:19:07.865 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [68.9, 71.6]    | Incomplete Receipt (Incomplete) |  |
|  -1.40 | 00:19:07.865 | Turkey             | Switzerland        | 43 | Pass            |   -   | [49.5, 10.0]    | -> Kaan Ayhan             | **OPPONENT LAST CONTROL** |
|  -0.06 | 00:19:09.203 | Turkey             | Switzerland        | 43 | Ball Receipt*   |   -   | [57.8, 8.7]     | Controlled Receipt        |  |
|  -0.02 | 00:19:09.243 | Turkey             | Switzerland        | 43 | Pass            |   -   | [57.4, 8.7]     | Incomplete (Incomplete)   |  |
|  +0.00 | 00:19:09.262 | Switzerland        | Switzerland        | 43 | Block           |  Yes  | [59.9, 71.2]    |                           | **CP INITIATION** |
|  +1.02 | 00:19:10.278 | Switzerland        | Switzerland        | 43 | Clearance       |   -   | [52.9, 72.3]    |                           |  |
|  +2.39 | 00:19:11.656 | Turkey             | Switzerland        | 43 | Pass            |   -   | [64.0, 10.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +3.13 | 00:19:12.389 | Turkey             | Switzerland        | 43 | Pressure        |   -   | [76.9, 13.4]    |                           |  |
|  +3.79 | 00:19:13.055 | Turkey             | Switzerland        | 43 | Ball Receipt*   |   -   | [78.3, 16.2]    | Incomplete Receipt (Incomplete) |  |
|  +3.79 | 00:19:13.055 | Switzerland        | Switzerland        | 43 | Pass            |  Yes  | [41.8, 61.3]    | -> Granit Xhaka           | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +4.46 | 00:19:13.723 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [47.7, 56.2]    | Controlled Receipt        |  |
|  +4.46 | 00:19:13.723 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [47.7, 56.2]    | Carry                     |  |
|  +5.01 | 00:19:14.271 | Turkey             | Switzerland        | 43 | Pressure        |   -   | [77.3, 22.0]    |                           |  |
|  +5.16 | 00:19:14.425 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [43.9, 55.6]    | -> Manuel Obafemi         |  |
|  +6.37 | 00:19:15.630 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [30.6, 51.9]    | Controlled Receipt        |  |
|  +6.37 | 00:19:15.630 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [30.6, 51.9]    | Carry                     |  |

---

### Case 53: Episode `3788765_p25_39415b22`
- **Match**: `3788765` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Switzerland** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.71 | 00:12:14.355 | Turkey             | Turkey             | 25 | Pass            |   -   | [55.7, 71.2]    | -> Cengiz Ünder           |  |
|  -2.43 | 00:12:14.637 | Switzerland        | Turkey             | 25 | Pressure        |   -   | [53.7, 7.0]     |                           |  |
|  -2.10 | 00:12:14.965 | Turkey             | Turkey             | 25 | Ball Receipt*   |   -   | [62.3, 73.7]    | Controlled Receipt        |  |
|  -2.10 | 00:12:14.965 | Turkey             | Turkey             | 25 | Carry           |   -   | [62.3, 73.7]    | Carry                     |  |
|  -1.94 | 00:12:15.125 | Turkey             | Turkey             | 25 | Miscontrol      |   -   | [64.0, 73.7]    | Miscontrol                |  |
|  -0.73 | 00:12:16.331 | Switzerland        | Turkey             | 25 | Pass            |   -   | [57.6, 9.8]     | -> Steven Zuber           |  |
|  -0.07 | 00:12:16.989 | Switzerland        | Turkey             | 25 | Ball Receipt*   |   -   | [64.6, 7.9]     | Controlled Receipt        |  |
|  -0.07 | 00:12:16.989 | Switzerland        | Turkey             | 25 | Carry           |   -   | [64.6, 7.9]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:12:17.064 | Turkey             | Turkey             | 25 | Pressure        |  Yes  | [50.3, 72.4]    |                           | **CP INITIATION** |
|  +0.44 | 00:12:17.500 | Switzerland        | Turkey             | 25 | Pass            |   -   | [64.4, 8.3]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +1.25 | 00:12:18.318 | Turkey             | Turkey             | 25 | Pass            |   -   | [53.7, 63.5]    | -> Ozan Tufan             | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.58 | 00:12:18.645 | Turkey             | Turkey             | 25 | Ball Receipt*   |   -   | [55.0, 70.1]    | Controlled Receipt        |  |
|  +1.58 | 00:12:18.645 | Turkey             | Turkey             | 25 | Carry           |   -   | [55.0, 70.1]    | Carry                     |  |
|  +1.90 | 00:12:18.964 | Switzerland        | Turkey             | 25 | Pressure        |   -   | [60.8, 9.2]     |                           |  |
|  +2.32 | 00:12:19.385 | Switzerland        | Turkey             | 25 | Pressure        |   -   | [65.3, 16.6]    |                           |  |
|  +2.82 | 00:12:19.882 | Switzerland        | Turkey             | 25 | Foul Committed  |   -   | [68.5, 14.1]    |                           |  |
|  +2.82 | 00:12:19.882 | Turkey             | Turkey             | 25 | Foul Won        |   -   | [51.6, 66.0]    |                           |  |

---

### Case 54: Episode `3788766_p49_c725799d`
- **Match**: `3788766` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Wales** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Wales`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_miscontrol` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.70 | 00:17:23.385 | Wales              | Wales              | 49 | Ball Receipt*   |   -   | [53.3, 76.5]    | Incomplete Receipt (Incomplete) |  |
|  -2.70 | 00:17:23.385 | Italy              | Wales              | 49 | Interception    |  Yes  | [72.0, 9.9]     | Won                       |  |
|  -2.70 | 00:17:23.385 | Italy              | Wales              | 49 | Carry           |   -   | [72.0, 9.9]     | Carry                     |  |
|  +0.00 | 00:17:26.084 | Wales              | Wales              | 49 | Pressure        |  Yes  | [39.0, 68.0]    |                           | **CP INITIATION** |
|  +0.21 | 00:17:26.290 | Wales              | Wales              | 49 | Pressure        |  Yes  | [34.6, 64.4]    |                           |  |
|  +0.88 | 00:17:26.962 | Italy              | Wales              | 49 | Miscontrol      |   -   | [83.5, 15.7]    | Miscontrol                | **POSSIBLE TRANSITION** |
|  +1.48 | 00:17:27.563 | Wales              | Wales              | 49 | Pass            |   -   | [28.5, 63.0]    | -> Joe Rodon              | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.83 | 00:17:28.917 | Wales              | Wales              | 49 | Ball Receipt*   |   -   | [22.8, 64.4]    | Controlled Receipt        |  |
|  +2.83 | 00:17:28.917 | Wales              | Wales              | 49 | Pass            |   -   | [22.8, 64.4]    | -> Joseff Morrell         |  |
|  +3.81 | 00:17:29.893 | Wales              | Wales              | 49 | Ball Receipt*   |   -   | [32.2, 69.1]    | Controlled Receipt        |  |
|  +3.81 | 00:17:29.893 | Wales              | Wales              | 49 | Carry           |   -   | [32.2, 69.1]    | Carry                     |  |
|  +4.90 | 00:17:30.984 | Wales              | Wales              | 49 | Pass            |   -   | [32.2, 69.1]    | -> Aaron Ramsey           |  |
|  +5.78 | 00:17:31.869 | Wales              | Wales              | 49 | Ball Receipt*   |   -   | [42.0, 76.9]    | Controlled Receipt        |  |
|  +5.78 | 00:17:31.869 | Wales              | Wales              | 49 | Carry           |   -   | [42.0, 76.9]    | Carry                     |  |
|  +6.00 | 00:17:32.089 | Italy              | Wales              | 49 | Pressure        |   -   | [76.1, 4.4]     |                           |  |
|  +7.77 | 00:17:33.858 | Italy              | Wales              | 49 | Foul Committed  |   -   | [83.5, 3.4]     |                           |  |
|  +7.77 | 00:17:33.858 | Wales              | Wales              | 49 | Foul Won        |   -   | [36.6, 76.7]    |                           |  |
|  -2.14 | 00:17:23.946 | Italy              | Italy              | 121 | Pass            |   -   | [51.3, 28.2]    | -> Alessandro Bas         |  |
|  -1.41 | 00:17:24.670 | Italy              | Italy              | 121 | Ball Receipt*   |   -   | [53.5, 20.7]    | Controlled Receipt        |  |
|  -1.41 | 00:17:24.670 | Italy              | Italy              | 121 | Carry           |   -   | [53.5, 20.7]    | Carry                     |  |
|  -0.58 | 00:17:25.501 | Italy              | Italy              | 121 | Pass            |   -   | [51.3, 19.6]    | -> Gianluigi Donn         |  |
|  +2.56 | 00:17:28.647 | Italy              | Italy              | 121 | Ball Receipt*   |   -   | [27.6, 46.5]    | Controlled Receipt        |  |
|  +2.56 | 00:17:28.647 | Italy              | Italy              | 121 | Pass            |   -   | [28.1, 46.8]    | -> Francesco Acer         |  |
|  +3.94 | 00:17:30.027 | Italy              | Italy              | 121 | Ball Receipt*   |   -   | [35.8, 57.0]    | Controlled Receipt        |  |
|  +3.94 | 00:17:30.027 | Italy              | Italy              | 121 | Carry           |   -   | [35.8, 57.0]    | Carry                     |  |
|  +5.13 | 00:17:31.219 | Italy              | Italy              | 121 | Pass            |   -   | [37.5, 61.5]    | -> Rafael Tolói           |  |
|  +6.66 | 00:17:32.744 | Italy              | Italy              | 121 | Ball Receipt*   |   -   | [46.4, 76.7]    | Controlled Receipt        |  |
|  +6.66 | 00:17:32.744 | Italy              | Italy              | 121 | Carry           |   -   | [46.4, 76.7]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 55: Episode `3788769_p21_5202b9ee`
- **Match**: `3788769` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Denmark** vs Actual Opponent: **Russia** (StatsBomb Poss Team: `Denmark`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.64 | 00:07:19.118 | Denmark            | Denmark            | 21 | Ball Receipt*   |   -   | [76.6, 53.8]    | Incomplete Receipt (Incomplete) |  |
|  -1.64 | 00:07:19.118 | Russia             | Denmark            | 21 | Pass            |   -   | [37.5, 24.5]    | -> Magomed Ozdoev         |  |
|  -0.00 | 00:07:20.760 | Russia             | Denmark            | 21 | Ball Receipt*   |   -   | [48.7, 46.7]    | Controlled Receipt        |  |
|  -0.00 | 00:07:20.760 | Russia             | Denmark            | 21 | Carry           |   -   | [48.7, 46.7]    | Carry                     |  |
|  +0.00 | 00:07:20.763 | Denmark            | Denmark            | 21 | Pressure        |  Yes  | [71.8, 33.6]    |                           | **CP INITIATION** |
|  +0.96 | 00:07:21.721 | Russia             | Denmark            | 21 | Pass            |   -   | [53.3, 37.8]    | Incomplete (Incomplete)   |  |
|  +2.32 | 00:07:23.086 | Russia             | Denmark            | 21 | Ball Receipt*   |   -   | [72.3, 58.2]    | Incomplete Receipt (Incomplete) |  |
|  +2.32 | 00:07:23.086 | Denmark            | Denmark            | 21 | Pass            |  Yes  | [48.5, 26.0]    | -> Pierre-Emile H         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +3.22 | 00:07:23.983 | Denmark            | Denmark            | 21 | Ball Receipt*   |   -   | [58.5, 27.0]    | Controlled Receipt        |  |
|  +3.22 | 00:07:23.983 | Denmark            | Denmark            | 21 | Carry           |   -   | [58.5, 27.0]    | Carry                     |  |
|  +4.23 | 00:07:24.993 | Denmark            | Denmark            | 21 | Pass            |   -   | [63.1, 23.5]    | -> Joakim Mæhle           |  |
|  +5.33 | 00:07:26.097 | Denmark            | Denmark            | 21 | Ball Receipt*   |   -   | [58.1, 10.0]    | Controlled Receipt        |  |
|  +5.33 | 00:07:26.097 | Denmark            | Denmark            | 21 | Carry           |   -   | [58.1, 10.0]    | Carry                     |  |
|  +6.61 | 00:07:27.368 | Denmark            | Denmark            | 21 | Pass            |   -   | [66.8, 5.4]     | Incomplete (Unknown)      |  |
|  +6.74 | 00:07:27.507 | Denmark            | Denmark            | 21 | Ball Receipt*   |   -   | [72.7, 16.4]    | Incomplete Receipt (Incomplete) |  |
|  +6.92 | 00:07:27.687 | Russia             | Denmark            | 21 | Foul Committed  |   -   | [50.3, 70.3]    |                           |  |
|  -2.63 | 00:07:18.135 | Russia             | Russia             | 100 | Ball Receipt*   |   -   | [44.8, 65.1]    | Controlled Receipt        |  |
|  -2.63 | 00:07:18.135 | Russia             | Russia             | 100 | Carry           |   -   | [44.8, 65.1]    | Carry                     |  |
|  -1.66 | 00:07:19.105 | Russia             | Russia             | 100 | Pass            |   -   | [42.6, 65.1]    | -> Matvey Safonov         |  |
|  +0.86 | 00:07:21.627 | Russia             | Russia             | 100 | Ball Receipt*   |   -   | [15.6, 45.2]    | Controlled Receipt        |  |
|  +0.86 | 00:07:21.627 | Russia             | Russia             | 100 | Carry           |   -   | [15.6, 45.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.17 | 00:07:23.931 | Russia             | Russia             | 100 | Pass            |   -   | [18.7, 44.9]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +6.18 | 00:07:26.940 | Russia             | Russia             | 100 | Ball Receipt*   |   -   | [73.6, 53.1]    | Incomplete Receipt (Incomplete) |  |
|  +6.18 | 00:07:26.940 | Denmark            | Denmark            | 101 | Pass            |   -   | [49.8, 28.3]    | -> Yussuf Yurary          |  |
|  +7.29 | 00:07:28.056 | Denmark            | Denmark            | 101 | Ball Receipt*   |   -   | [68.6, 25.5]    | Controlled Receipt        |  |
|  +7.29 | 00:07:28.056 | Denmark            | Denmark            | 101 | Carry           |   -   | [68.6, 25.5]    | Carry                     |  |
|  +7.96 | 00:07:28.721 | Russia             | Denmark            | 101 | Pressure        |  Yes  | [48.3, 55.6]    |                           |  |

---

### Case 56: Episode `3788769_p40_01a87028`
- **Match**: `3788769` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Russia** vs Actual Opponent: **Denmark** (StatsBomb Poss Team: `Russia`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.66 | 00:16:59.044 | Russia             | Denmark            | 39 | Pressure        |   -   | [50.8, 52.2]    |                           |  |
|  +0.00 | 00:16:59.701 | Denmark            | Denmark            | 39 | Dribble         |   -   | [68.6, 31.1]    | Incomplete                |  |
|  +0.00 | 00:16:59.701 | Russia             | Russia             | 40 | Duel            |  Yes  | [51.5, 49.0]    | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +1.05 | 00:17:00.747 | Denmark            | Russia             | 40 | Pressure        |  Yes  | [64.0, 38.2]    |                           |  |
|  +1.52 | 00:17:01.217 | Russia             | Russia             | 40 | Pass            |   -   | [53.1, 40.8]    | -> Aleksandr Golo         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.49 | 00:17:02.195 | Russia             | Russia             | 40 | Ball Receipt*   |   -   | [61.1, 32.3]    | Controlled Receipt        |  |
|  +2.49 | 00:17:02.195 | Russia             | Russia             | 40 | Carry           |   -   | [61.1, 32.3]    | Carry                     |  |
|  -2.33 | 00:16:57.368 | Russia             | Russia             | 120 | Pass            |   -   | [53.3, 32.4]    | Incomplete (Incomplete)   |  |
|  -0.42 | 00:16:59.283 | Russia             | Russia             | 120 | Ball Receipt*   |   -   | [73.1, 40.4]    | Incomplete Receipt (Incomplete) |  |
|  -0.42 | 00:16:59.283 | Denmark            | Denmark            | 121 | Ball Recovery   |   -   | [51.1, 32.4]    |                           |  |
|  -0.42 | 00:16:59.283 | Denmark            | Denmark            | 121 | Carry           |   -   | [51.1, 32.4]    | Carry                     |  |
|  +1.92 | 00:17:01.622 | Denmark            | Denmark            | 121 | Pass            |   -   | [56.2, 24.4]    | -> Joakim Mæhle           |  |
|  +3.55 | 00:17:03.251 | Denmark            | Denmark            | 121 | Ball Receipt*   |   -   | [63.1, 11.4]    | Controlled Receipt        |  |
|  +3.55 | 00:17:03.251 | Denmark            | Denmark            | 121 | Carry           |   -   | [63.1, 11.4]    | Carry                     |  |
|  +5.11 | 00:17:04.812 | Denmark            | Denmark            | 121 | Pass            |   -   | [69.5, 14.2]    | -> Martin Braithw         |  |
|  +5.84 | 00:17:05.539 | Denmark            | Denmark            | 121 | Ball Receipt*   |   -   | [70.6, 24.1]    | Controlled Receipt        |  |
|  +5.84 | 00:17:05.539 | Denmark            | Denmark            | 121 | Carry           |   -   | [70.6, 24.1]    | Carry                     |  |
|  +5.88 | 00:17:05.579 | Denmark            | Denmark            | 121 | Pass            |   -   | [70.6, 24.1]    | -> Pierre-Emile H         |  |
|  +6.88 | 00:17:06.577 | Denmark            | Denmark            | 121 | Ball Receipt*   |   -   | [59.5, 17.4]    | Controlled Receipt        |  |
|  +6.88 | 00:17:06.577 | Denmark            | Denmark            | 121 | Carry           |   -   | [59.5, 17.4]    | Carry                     |  |
|  +6.92 | 00:17:06.617 | Denmark            | Denmark            | 121 | Pass            |   -   | [59.5, 17.4]    | -> Thomas Delaney         |  |
|  +7.94 | 00:17:07.642 | Denmark            | Denmark            | 121 | Ball Receipt*   |   -   | [62.0, 28.3]    | Controlled Receipt        |  |
|  +7.94 | 00:17:07.642 | Denmark            | Denmark            | 121 | Carry           |   -   | [62.0, 28.3]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 57: Episode `3788769_p123_852f2f78`
- **Match**: `3788769` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Denmark** vs Actual Opponent: **Russia** (StatsBomb Poss Team: `Denmark`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +7.90 | 00:17:29.089 | Denmark            | Denmark            | 41 | Pass            |   -   | [7.0, 36.1]     | -> Joakim Mæhle           | **PRESSING-TEAM FIRST CONTROL** |
|  -2.68 | 00:17:18.505 | Russia             | Russia             | 122 | Ball Receipt*   |   -   | [39.8, 41.0]    | Controlled Receipt        |  |
|  -2.68 | 00:17:18.505 | Russia             | Russia             | 122 | Carry           |   -   | [39.8, 41.0]    | Carry                     |  |
|  -1.64 | 00:17:19.544 | Russia             | Russia             | 122 | Pass            |   -   | [44.0, 40.4]    | -> Artem Dzyuba           |  |
|  -0.73 | 00:17:20.459 | Denmark            | Russia             | 122 | Pressure        |   -   | [62.0, 33.3]    |                           |  |
|  -0.08 | 00:17:21.104 | Russia             | Russia             | 122 | Ball Receipt*   |   -   | [55.9, 46.5]    | Controlled Receipt        |  |
|  -0.08 | 00:17:21.104 | Russia             | Russia             | 122 | Carry           |   -   | [55.9, 46.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:17:21.187 | Russia             | Russia             | 122 | Dispossessed    |   -   | [55.9, 47.1]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:17:21.187 | Denmark            | Denmark            | 123 | Duel            |  Yes  | [64.2, 33.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.32 | 00:17:22.511 | Denmark            | Denmark            | 123 | Pass            |   -   | [61.4, 31.7]    | -> Jannik Vesterg         | (v2.6 Regain Event) |
|  +1.98 | 00:17:23.162 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [64.2, 34.9]    | Controlled Receipt        |  |
|  +1.98 | 00:17:23.162 | Denmark            | Denmark            | 123 | Carry           |   -   | [64.2, 34.9]    | Carry                     |  |
|  +2.54 | 00:17:23.723 | Denmark            | Denmark            | 123 | Pass            |   -   | [64.0, 34.9]    | -> Thomas Delaney         |  |
|  +4.28 | 00:17:25.464 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [64.0, 42.8]    | Controlled Receipt        |  |
|  +4.28 | 00:17:25.464 | Denmark            | Denmark            | 123 | Carry           |   -   | [64.0, 42.8]    | Carry                     |  |
|  +4.32 | 00:17:25.504 | Denmark            | Denmark            | 123 | Pass            |   -   | [64.0, 42.8]    | -> Mikkel Damsgaa         |  |
|  +5.07 | 00:17:26.259 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [70.1, 54.1]    | Controlled Receipt        |  |
|  +5.07 | 00:17:26.259 | Denmark            | Denmark            | 123 | Carry           |   -   | [70.1, 54.1]    | Carry                     |  |
|  +7.78 | 00:17:28.968 | Denmark            | Denmark            | 123 | Pass            |   -   | [80.0, 54.9]    | -> Kasper Dolberg         |  |

---

### Case 58: Episode `3788747_p174_e1be0dd6`
- **Match**: `3788747` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **North Macedonia** vs Actual Opponent: **Austria** (StatsBomb Poss Team: `North Macedonia`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.91 | 00:37:44.609 | North Macedonia    | North Macedonia    | 83 | Pass            |   -   | [76.8, 7.7]     | Incomplete (Incomplete)   |  |
|  -2.86 | 00:37:44.658 | Austria            | North Macedonia    | 83 | Block           |   -   | [43.3, 72.4]    |                           |  |
|  -1.99 | 00:37:45.531 | North Macedonia    | North Macedonia    | 83 | Pressure        |   -   | [77.0, 7.9]     |                           |  |
|  -1.53 | 00:37:45.991 | Austria            | North Macedonia    | 83 | Pass            |   -   | [41.4, 70.5]    | Incomplete (Incomplete)   |  |
|  -1.33 | 00:37:46.191 | Austria            | North Macedonia    | 83 | Block           |   -   | [36.0, 69.3]    |                           |  |
|  -0.45 | 00:37:47.072 | Austria            | North Macedonia    | 83 | Pressure        |   -   | [27.0, 68.4]    |                           |  |
|  +0.50 | 00:37:48.026 | North Macedonia    | North Macedonia    | 83 | Ball Recovery   |   -   | [94.7, 10.8]    |                           |  |
|  +0.50 | 00:37:48.026 | North Macedonia    | North Macedonia    | 83 | Carry           |   -   | [94.7, 10.8]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +4.75 | 00:37:52.267 | Austria            | North Macedonia    | 83 | Pressure        |   -   | [26.6, 69.1]    |                           |  |
|  +5.20 | 00:37:52.725 | Austria            | North Macedonia    | 83 | Dribbled Past   |   -   | [34.5, 70.9]    |                           |  |
|  +5.20 | 00:37:52.725 | North Macedonia    | North Macedonia    | 83 | Dribble         |   -   | [85.6, 9.2]     | Complete                  |  |
|  +5.20 | 00:37:52.725 | North Macedonia    | North Macedonia    | 83 | Carry           |   -   | [85.6, 9.2]     | Carry                     |  |
|  +7.63 | 00:37:55.156 | North Macedonia    | North Macedonia    | 83 | Dispossessed    |   -   | [80.8, 9.6]     | Dispossessed              |  |
|  +7.63 | 00:37:55.156 | Austria            | Austria            | 84 | Duel            |   -   | [39.3, 70.5]    | Tackle, Success In Play   |  |
|  -1.88 | 00:37:45.637 | North Macedonia    | Austria            | 173 | Pressure        |   -   | [55.3, 29.5]    |                           |  |
|  -1.78 | 00:37:45.743 | Austria            | Austria            | 173 | Ball Recovery   |   -   | [66.8, 49.6]    |                           |  |
|  -1.78 | 00:37:45.743 | Austria            | Austria            | 173 | Carry           |   -   | [66.8, 49.6]    | Carry                     |  |
|  -1.33 | 00:37:46.188 | North Macedonia    | Austria            | 173 | Dribbled Past   |   -   | [55.3, 29.7]    |                           |  |
|  -1.33 | 00:37:46.188 | Austria            | Austria            | 173 | Dribble         |   -   | [64.8, 50.4]    | Complete                  |  |
|  -1.33 | 00:37:46.188 | Austria            | Austria            | 173 | Carry           |   -   | [64.8, 50.4]    | Carry                     |  |
|  -0.58 | 00:37:46.938 | North Macedonia    | Austria            | 173 | Pressure        |   -   | [55.6, 32.2]    |                           |  |
|  +0.00 | 00:37:47.521 | Austria            | Austria            | 173 | Dispossessed    |   -   | [63.3, 46.2]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:37:47.521 | North Macedonia    | North Macedonia    | 174 | Duel            |  Yes  | [56.8, 33.9]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.27 | 00:37:48.792 | North Macedonia    | North Macedonia    | 174 | Pass            |   -   | [68.5, 32.0]    | -> Goran Pandev           | (v2.6 Regain Event) |
|  +1.60 | 00:37:49.118 | North Macedonia    | North Macedonia    | 174 | Ball Receipt*   |   -   | [68.5, 38.2]    | Controlled Receipt        |  |
|  +1.60 | 00:37:49.118 | North Macedonia    | North Macedonia    | 174 | Carry           |   -   | [68.5, 38.2]    | Carry                     |  |
|  +1.81 | 00:37:49.333 | North Macedonia    | North Macedonia    | 174 | Pass            |   -   | [68.1, 38.4]    | -> Eljif Elmas            |  |
|  +3.40 | 00:37:50.923 | North Macedonia    | North Macedonia    | 174 | Ball Receipt*   |   -   | [70.4, 29.5]    | Controlled Receipt        |  |
|  +3.40 | 00:37:50.923 | North Macedonia    | North Macedonia    | 174 | Carry           |   -   | [70.4, 29.5]    | Carry                     |  |
|  +3.74 | 00:37:51.257 | North Macedonia    | North Macedonia    | 174 | Pass            |   -   | [76.8, 25.9]    | -> Ezgjan Alioski         |  |
|  +5.76 | 00:37:53.277 | Austria            | North Macedonia    | 174 | Pressure        |   -   | [23.1, 63.1]    |                           |  |
|  +6.12 | 00:37:53.643 | North Macedonia    | North Macedonia    | 174 | Ball Receipt*   |   -   | [93.0, 14.9]    | Controlled Receipt        |  |
|  +6.12 | 00:37:53.643 | North Macedonia    | North Macedonia    | 174 | Carry           |   -   | [93.0, 14.9]    | Carry                     |  |
|  +6.28 | 00:37:53.802 | North Macedonia    | North Macedonia    | 174 | Dribble         |   -   | [102.2, 14.1]   | Incomplete                |  |
|  +6.28 | 00:37:53.802 | Austria            | Austria            | 175 | Duel            |  Yes  | [17.9, 66.0]    | Tackle, Won               |  |
|  +6.28 | 00:37:53.802 | Austria            | Austria            | 175 | Carry           |   -   | [17.9, 66.0]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 59: Episode `3788747_p148_01e2f8ec`
- **Match**: `3788747` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Austria** vs Actual Opponent: **North Macedonia** (StatsBomb Poss Team: `Austria`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +5.34 | 00:25:25.311 | North Macedonia    | North Macedonia    | 59 | Pass            |   -   | [92.5, 75.1]    | Incomplete (Unknown)      |  |
|  +6.98 | 00:25:26.954 | North Macedonia    | North Macedonia    | 59 | Pressure        |   -   | [109.1, 32.3]   |                           |  |
|  +7.13 | 00:25:27.108 | North Macedonia    | North Macedonia    | 59 | Ball Receipt*   |   -   | [112.2, 31.4]   | Incomplete Receipt (Incomplete) |  |
|  +7.26 | 00:25:27.230 | North Macedonia    | North Macedonia    | 59 | Foul Committed  |   -   | [108.5, 39.0]   |                           |  |
|  +7.26 | 00:25:27.230 | Austria            | North Macedonia    | 59 | Foul Won        |   -   | [11.6, 41.1]    |                           |  |
|  -2.86 | 00:25:17.118 | North Macedonia    | North Macedonia    | 147 | Ball Receipt*   |   -   | [82.4, 63.2]    | Controlled Receipt        |  |
|  -2.86 | 00:25:17.118 | North Macedonia    | North Macedonia    | 147 | Carry           |   -   | [82.4, 63.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -2.53 | 00:25:17.444 | Austria            | North Macedonia    | 147 | Pressure        |   -   | [31.6, 14.8]    |                           |  |
|  -0.93 | 00:25:19.044 | Austria            | North Macedonia    | 147 | Pressure        |   -   | [27.3, 12.5]    |                           |  |
|  +0.00 | 00:25:19.975 | North Macedonia    | North Macedonia    | 147 | Dispossessed    |   -   | [93.3, 68.6]    | Dispossessed              |  |
|  +0.00 | 00:25:19.975 | Austria            | Austria            | 148 | Duel            |  Yes  | [26.8, 11.5]    | Tackle, Success In Play   | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +1.35 | 00:25:21.323 | Austria            | Austria            | 148 | Pass            |   -   | [26.6, 12.3]    | -> Xaver Schlager         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.42 | 00:25:22.397 | Austria            | Austria            | 148 | Ball Receipt*   |   -   | [28.3, 21.5]    | Controlled Receipt        |  |
|  +2.42 | 00:25:22.397 | Austria            | Austria            | 148 | Pass            |   -   | [28.3, 21.5]    | -> David Olatukun         |  |
|  +3.25 | 00:25:23.229 | Austria            | Austria            | 148 | Ball Receipt*   |   -   | [21.0, 20.8]    | Controlled Receipt        |  |
|  +3.25 | 00:25:23.229 | Austria            | Austria            | 148 | Carry           |   -   | [21.0, 20.8]    | Carry                     |  |
|  +4.72 | 00:25:24.699 | Austria            | Austria            | 148 | Pass            |   -   | [22.0, 19.6]    | -> Xaver Schlager         |  |
|  +5.71 | 00:25:25.688 | Austria            | Austria            | 148 | Ball Receipt*   |   -   | [31.4, 27.3]    | Controlled Receipt        |  |
|  +5.71 | 00:25:25.688 | Austria            | Austria            | 148 | Carry           |   -   | [31.4, 27.3]    | Carry                     |  |

---

### Case 60: Episode `3788747_p68_0f9d0863`
- **Match**: `3788747` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Austria** vs Actual Opponent: **North Macedonia** (StatsBomb Poss Team: `North Macedonia`)
- **Stratum**: `pass` | **First Press Control Candidate**: `Pass`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `completed_pass`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.00 | 00:30:27.607 | Austria            | North Macedonia    | 68 | Pressure        |  Yes  | [116.0, 64.9]   |                           | **CP INITIATION** |
|  +2.15 | 00:30:29.761 | North Macedonia    | North Macedonia    | 68 | Pass            |   -   | [3.7, 14.0]     | -> Ezgjan Alioski         |  |
|  +2.91 | 00:30:30.517 | North Macedonia    | North Macedonia    | 68 | Ball Receipt*   |   -   | [20.4, 10.4]    | Controlled Receipt        |  |
|  +2.91 | 00:30:30.517 | North Macedonia    | North Macedonia    | 68 | Pass            |   -   | [20.4, 10.4]    | -> Arijan Ademi           |  |
|  +3.47 | 00:30:31.077 | North Macedonia    | North Macedonia    | 68 | Ball Receipt*   |   -   | [13.9, 15.2]    | Controlled Receipt        |  |
|  +3.47 | 00:30:31.077 | North Macedonia    | North Macedonia    | 68 | Carry           |   -   | [13.9, 15.2]    | Carry                     |  |
|  +3.51 | 00:30:31.117 | North Macedonia    | North Macedonia    | 68 | Pass            |   -   | [11.6, 14.6]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +4.61 | 00:30:32.212 | North Macedonia    | North Macedonia    | 68 | Ball Receipt*   |   -   | [31.0, 10.8]    | Incomplete Receipt (Incomplete) |  |
|  +4.61 | 00:30:32.212 | Austria            | North Macedonia    | 68 | Pass            |   -   | [90.3, 67.0]    | -> Sasa Kalajdzic         | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +6.12 | 00:30:33.724 | Austria            | North Macedonia    | 68 | Ball Receipt*   |   -   | [111.4, 62.4]   | Controlled Receipt        |  |
|  +6.12 | 00:30:33.724 | Austria            | North Macedonia    | 68 | Carry           |   -   | [111.4, 62.4]   | Carry                     |  |
|  +6.47 | 00:30:34.076 | Austria            | North Macedonia    | 68 | Miscontrol      |   -   | [111.4, 64.1]   | Miscontrol                |  |
|  +7.15 | 00:30:34.760 | North Macedonia    | North Macedonia    | 68 | Ball Recovery   |   -   | [8.7, 16.0]     |                           |  |
|  +7.15 | 00:30:34.760 | North Macedonia    | North Macedonia    | 68 | Carry           |   -   | [8.7, 16.0]     | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 61: Episode `3794686_p31_bdbb6189`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.68 | 00:16:41.373 | Spain              | Croatia            | 30 | Pressure        |   -   | [66.1, 70.8]    |                           |  |
|  -1.65 | 00:16:42.407 | Croatia            | Croatia            | 30 | Pass            |   -   | [54.0, 9.3]     | -> Joško Gvardiol         |  |
|  -1.05 | 00:16:43.002 | Croatia            | Croatia            | 30 | Ball Receipt*   |   -   | [60.4, 4.0]     | Controlled Receipt        |  |
|  -1.05 | 00:16:43.002 | Croatia            | Croatia            | 30 | Carry           |   -   | [60.4, 4.0]     | Carry                     |  |
|  -0.41 | 00:16:43.640 | Croatia            | Croatia            | 30 | Pass            |   -   | [59.8, 3.7]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:16:44.054 | Croatia            | Croatia            | 30 | Ball Receipt*   |   -   | [57.8, 13.8]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:16:44.054 | Spain              | Spain              | 31 | Pass            |  Yes  | [62.3, 69.9]    | -> Álvaro Borja M         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.18 | 00:16:44.237 | Croatia            | Spain              | 31 | Pressure        |  Yes  | [55.9, 7.6]     |                           |  |
|  +0.46 | 00:16:44.513 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [65.0, 71.7]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.46 | 00:16:44.513 | Spain              | Spain              | 31 | Carry           |   -   | [65.0, 71.7]    | Carry                     |  |
|  +1.28 | 00:16:45.335 | Spain              | Spain              | 31 | Pass            |   -   | [64.0, 72.0]    | -> Sergio Busquet         |  |
|  +1.74 | 00:16:45.792 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [62.3, 69.5]    | Controlled Receipt        |  |
|  +1.74 | 00:16:45.792 | Spain              | Spain              | 31 | Pass            |   -   | [62.3, 69.9]    | -> Ferrán Torres          |  |
|  +2.71 | 00:16:46.761 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [60.7, 74.7]    | Controlled Receipt        |  |
|  +2.71 | 00:16:46.761 | Spain              | Spain              | 31 | Carry           |   -   | [60.7, 74.7]    | Carry                     |  |
|  +2.93 | 00:16:46.987 | Croatia            | Spain              | 31 | Pressure        |  Yes  | [58.6, 5.7]     |                           |  |
|  +3.96 | 00:16:48.012 | Spain              | Spain              | 31 | Pass            |   -   | [62.6, 76.3]    | -> Álvaro Borja M         |  |
|  +4.22 | 00:16:48.273 | Croatia            | Spain              | 31 | Pressure        |  Yes  | [53.4, 4.3]     |                           |  |
|  +4.44 | 00:16:48.497 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [66.4, 75.8]    | Controlled Receipt        |  |
|  +4.44 | 00:16:48.497 | Spain              | Spain              | 31 | Carry           |   -   | [66.4, 75.8]    | Carry                     |  |
|  +5.55 | 00:16:49.606 | Spain              | Spain              | 31 | Pass            |   -   | [66.7, 75.8]    | -> Pedro González         |  |
|  +7.15 | 00:16:51.202 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [71.2, 58.6]    | Controlled Receipt        |  |
|  +7.15 | 00:16:51.202 | Spain              | Spain              | 31 | Carry           |   -   | [71.2, 58.6]    | Carry                     |  |
|  +7.19 | 00:16:51.242 | Spain              | Spain              | 31 | Pass            |   -   | [71.2, 58.6]    | -> Jorge Resurrec         |  |
|  +0.11 | 00:16:44.160 | Croatia            | Croatia            | 119 | Pass            |   -   | [45.8, 64.8]    | -> Dominik Livako         |  |
|  +3.07 | 00:16:47.125 | Croatia            | Croatia            | 119 | Ball Receipt*   |   -   | [18.7, 47.3]    | Controlled Receipt        |  |
|  +3.07 | 00:16:47.125 | Croatia            | Croatia            | 119 | Carry           |   -   | [18.7, 47.3]    | Carry                     |  |
|  +4.62 | 00:16:48.670 | Croatia            | Croatia            | 119 | Pass            |   -   | [19.4, 47.1]    | -> Joško Gvardiol         |  |
|  +7.16 | 00:16:51.211 | Croatia            | Croatia            | 119 | Ball Receipt*   |   -   | [46.2, 5.9]     | Controlled Receipt        |  |
|  +7.16 | 00:16:51.211 | Croatia            | Croatia            | 119 | Pass            |   -   | [46.2, 5.9]     | -> Ante Rebić             | **OPPONENT LAST CONTROL** |

---

### Case 62: Episode `3794686_p67_9670e0af`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.52 | 00:34:39.482 | Spain              | Spain              | 66 | Pass            |   -   | [61.4, 29.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.19 | 00:34:41.818 | Spain              | Spain              | 66 | Pressure        |   -   | [88.9, 14.7]    |                           |  |
|  +0.00 | 00:34:42.006 | Spain              | Spain              | 66 | Ball Receipt*   |   -   | [88.6, 15.0]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:34:42.006 | Croatia            | Croatia            | 67 | Pass            |  Yes  | [32.0, 62.9]    | -> Dominik Livako         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +2.59 | 00:34:44.598 | Croatia            | Croatia            | 67 | Ball Receipt*   |   -   | [6.4, 45.7]     | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.59 | 00:34:44.598 | Croatia            | Croatia            | 67 | Carry           |   -   | [6.4, 45.7]     | Carry                     |  |
|  +3.31 | 00:34:45.317 | Croatia            | Croatia            | 67 | Pass            |   -   | [5.6, 44.1]     | -> Josip Juranovi         |  |
|  +4.91 | 00:34:46.915 | Croatia            | Croatia            | 67 | Ball Receipt*   |   -   | [10.1, 76.8]    | Controlled Receipt        |  |
|  +4.91 | 00:34:46.915 | Croatia            | Croatia            | 67 | Carry           |   -   | [10.1, 76.8]    | Carry                     |  |
|  +7.90 | 00:34:49.906 | Spain              | Croatia            | 67 | Pressure        |   -   | [91.4, 3.6]     |                           |  |

---

### Case 63: Episode `3788764_p90_02f79b97`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.91 | 00:02:34.741 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [47.9, 15.2]    | Controlled Receipt        |  |
|  -2.91 | 00:02:34.741 | Germany            | Germany            | 5 | Carry           |   -   | [47.9, 15.2]    | Carry                     |  |
|  +0.52 | 00:02:38.178 | Germany            | Germany            | 5 | Pass            |   -   | [63.8, 14.5]    | -> Toni Kroos             |  |
|  +1.29 | 00:02:38.945 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [62.7, 5.0]     | Controlled Receipt        |  |
|  +1.29 | 00:02:38.945 | Germany            | Germany            | 5 | Carry           |   -   | [62.7, 5.0]     | Carry                     |  |
|  +2.64 | 00:02:40.298 | Germany            | Germany            | 5 | Pass            |   -   | [62.0, 10.3]    | -> Mats Hummels           |  |
|  +4.09 | 00:02:41.743 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [51.4, 40.5]    | Controlled Receipt        |  |
|  +4.09 | 00:02:41.743 | Germany            | Germany            | 5 | Carry           |   -   | [51.4, 40.5]    | Carry                     |  |
|  +6.92 | 00:02:44.573 | Germany            | Germany            | 5 | Pass            |   -   | [56.7, 52.5]    | -> Matthias Ginte         | **OPPONENT LAST CONTROL** |
|  -2.28 | 00:02:35.373 | Portugal           | Germany            | 89 | Pressure        |   -   | [113.0, 63.1]   |                           |  |
|  -1.06 | 00:02:36.593 | Germany            | Germany            | 89 | Pass            |   -   | [6.2, 13.5]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:02:37.655 | Germany            | Germany            | 89 | Ball Receipt*   |   -   | [30.5, 11.5]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:02:37.655 | Portugal           | Portugal           | 90 | Pass            |  Yes  | [92.4, 61.2]    | -> Nélson Cabral          | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.92 | 00:02:38.580 | Germany            | Portugal           | 90 | Pressure        |  Yes  | [22.1, 7.9]     |                           |  |
|  +0.95 | 00:02:38.608 | Portugal           | Portugal           | 90 | Ball Receipt*   |   -   | [97.7, 75.7]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.95 | 00:02:38.608 | Portugal           | Portugal           | 90 | Carry           |   -   | [97.7, 75.7]    | Carry                     |  |
|  +1.27 | 00:02:38.929 | Portugal           | Portugal           | 90 | Pass            |   -   | [97.4, 72.2]    | -> Renato Júnior          |  |
|  +2.06 | 00:02:39.710 | Portugal           | Portugal           | 90 | Ball Receipt*   |   -   | [109.3, 71.6]   | Controlled Receipt        |  |
|  +2.06 | 00:02:39.710 | Portugal           | Portugal           | 90 | Carry           |   -   | [109.3, 71.6]   | Carry                     |  |
|  +2.78 | 00:02:40.433 | Germany            | Portugal           | 90 | Pressure        |  Yes  | [10.8, 9.0]     |                           |  |
|  +2.97 | 00:02:40.626 | Portugal           | Portugal           | 90 | Pass            |   -   | [109.0, 71.1]   | -> Bruno Miguel B         |  |
|  +3.55 | 00:02:41.208 | Portugal           | Portugal           | 90 | Ball Receipt*   |   -   | [109.0, 66.9]   | Controlled Receipt        |  |
|  +3.55 | 00:02:41.208 | Portugal           | Portugal           | 90 | Carry           |   -   | [109.0, 66.9]   | Carry                     |  |
|  +6.01 | 00:02:43.668 | Portugal           | Portugal           | 90 | Pass            |   -   | [106.7, 64.7]   | Incomplete (Unknown)      |  |
|  +7.46 | 00:02:45.115 | Portugal           | Portugal           | 90 | Foul Committed  |   -   | [109.5, 33.0]   |                           |  |
|  +7.46 | 00:02:45.115 | Germany            | Portugal           | 90 | Foul Won        |   -   | [10.6, 47.1]    |                           |  |

---

### Case 64: Episode `3788762_p78_da8daf2d`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.50 | 00:00:02.447 | Poland             | Poland             | 2 | Pass            |   -   | [53.3, 42.9]    | Incomplete (Incomplete)   |  |
|  +0.79 | 00:00:05.742 | Poland             | Poland             | 2 | Pressure        |   -   | [98.0, 76.7]    |                           |  |
|  +2.14 | 00:00:07.084 | Poland             | Poland             | 2 | Ball Receipt*   |   -   | [93.1, 73.1]    | Incomplete Receipt (Incomplete) |  |
|  +2.14 | 00:00:07.084 | Spain              | Poland             | 2 | Ball Recovery   |   -   | [18.9, 3.4]     |                           |  |
|  -2.53 | 00:00:02.416 | Spain              | Spain              | 77 | Ball Receipt*   |   -   | [33.3, 26.3]    | Controlled Receipt        |  |
|  -2.53 | 00:00:02.416 | Spain              | Spain              | 77 | Carry           |   -   | [33.3, 26.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.08 | 00:00:03.872 | Spain              | Spain              | 77 | Pass            |   -   | [34.7, 26.3]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:00:04.948 | Poland             | Poland             | 78 | Pass            |  Yes  | [56.3, 32.5]    | -> Mateusz Andrze         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +2.67 | 00:00:07.621 | Spain              | Poland             | 78 | Pressure        |  Yes  | [78.4, 44.4]    |                           |  |
|  +2.98 | 00:00:07.927 | Poland             | Poland             | 78 | Ball Receipt*   |   -   | [41.7, 39.8]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.98 | 00:00:07.927 | Poland             | Poland             | 78 | Carry           |   -   | [41.7, 39.8]    | Carry                     |  |
|  +3.83 | 00:00:08.775 | Poland             | Poland             | 78 | Pass            |   -   | [41.9, 43.1]    | -> Bartosz Beresz         |  |
|  +5.06 | 00:00:10.013 | Poland             | Poland             | 78 | Ball Receipt*   |   -   | [36.6, 69.4]    | Controlled Receipt        |  |
|  +5.06 | 00:00:10.013 | Poland             | Poland             | 78 | Carry           |   -   | [36.6, 69.4]    | Carry                     |  |
|  +6.86 | 00:00:11.810 | Poland             | Poland             | 78 | Pass            |   -   | [35.6, 72.2]    | Incomplete (Incomplete)   |  |
|  +7.08 | 00:00:12.031 | Poland             | Poland             | 78 | Ball Receipt*   |   -   | [54.6, 74.2]    | Incomplete Receipt (Incomplete) |  |
|  +7.08 | 00:00:12.031 | Spain              | Poland             | 78 | Block           |   -   | [78.3, 6.4]     |                           |  |

---

### Case 65: Episode `3788762_p30_6276c390`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.72 | 00:14:36.714 | Poland             | Spain              | 29 | Pressure        |   -   | [21.2, 67.3]    |                           |  |
|  -0.95 | 00:14:37.483 | Spain              | Spain              | 29 | Pass            |   -   | [98.0, 9.1]     | Incomplete (Incomplete)   |  |
|  +0.00 | 00:14:38.433 | Spain              | Spain              | 29 | Ball Receipt*   |   -   | [104.2, 25.0]   | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:14:38.433 | Poland             | Poland             | 30 | Pass            |  Yes  | [20.1, 56.9]    | -> Mateusz Andrze         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.61 | 00:14:39.046 | Poland             | Poland             | 30 | Ball Receipt*   |   -   | [28.5, 57.9]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.61 | 00:14:39.046 | Poland             | Poland             | 30 | Carry           |   -   | [28.5, 57.9]    | Carry                     |  |
|  +2.70 | 00:14:41.133 | Spain              | Poland             | 30 | Pressure        |  Yes  | [86.3, 24.7]    |                           |  |
|  +3.56 | 00:14:41.996 | Poland             | Poland             | 30 | Pass            |   -   | [35.3, 51.9]    | -> Jakub Moder            |  |
|  +4.13 | 00:14:42.561 | Spain              | Poland             | 30 | Pressure        |  Yes  | [81.1, 46.8]    |                           |  |
|  +4.25 | 00:14:42.679 | Poland             | Poland             | 30 | Ball Receipt*   |   -   | [35.8, 36.5]    | Controlled Receipt        |  |
|  +4.25 | 00:14:42.679 | Poland             | Poland             | 30 | Carry           |   -   | [35.8, 36.5]    | Carry                     |  |
|  +5.38 | 00:14:43.818 | Spain              | Poland             | 30 | Dribbled Past   |   -   | [78.3, 45.9]    |                           |  |
|  +5.38 | 00:14:43.818 | Poland             | Poland             | 30 | Dribble         |   -   | [41.8, 34.2]    | Complete                  |  |
|  +5.38 | 00:14:43.818 | Poland             | Poland             | 30 | Carry           |   -   | [41.8, 34.2]    | Carry                     |  |
|  +7.03 | 00:14:45.461 | Spain              | Poland             | 30 | Pressure        |   -   | [65.3, 50.8]    |                           |  |
|  +7.32 | 00:14:45.753 | Poland             | Poland             | 30 | Dribble         |   -   | [55.0, 26.3]    | Incomplete                |  |
|  +7.32 | 00:14:45.753 | Spain              | Spain              | 31 | Duel            |  Yes  | [65.1, 53.8]    | Tackle, Success In Play   |  |
|  +7.51 | 00:14:45.946 | Spain              | Spain              | 31 | Block           |  Yes  | [67.0, 54.9]    |                           |  |
|  -1.82 | 00:14:36.617 | Spain              | Spain              | 101 | Pressure        |  Yes  | [107.6, 9.9]    |                           |  |
|  -1.44 | 00:14:36.995 | Poland             | Spain              | 101 | Pass            |   -   | [8.6, 71.6]     | Incomplete (Incomplete)   |  |
|  +0.51 | 00:14:38.944 | Spain              | Spain              | 101 | Pass            |   -   | [75.3, 15.0]    | -> Rodrigo Hernán         |  |
|  +1.34 | 00:14:39.773 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [78.9, 25.1]    | Controlled Receipt        |  |
|  +1.34 | 00:14:39.773 | Spain              | Spain              | 101 | Carry           |   -   | [78.9, 25.1]    | Carry                     |  |
|  +2.17 | 00:14:40.599 | Spain              | Spain              | 101 | Pass            |   -   | [78.0, 24.7]    | -> Marcos Llorent         |  |
|  +3.76 | 00:14:42.189 | Poland             | Spain              | 101 | Pressure        |   -   | [32.7, 29.6]    |                           |  |
|  +3.84 | 00:14:42.274 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [84.0, 50.0]    | Controlled Receipt        |  |
|  +3.84 | 00:14:42.274 | Spain              | Spain              | 101 | Carry           |   -   | [84.0, 50.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.88 | 00:14:42.314 | Spain              | Spain              | 101 | Pass            |   -   | [84.2, 50.5]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +6.57 | 00:14:45.002 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [107.2, 59.4]   | Incomplete Receipt (Incomplete) |  |
|  +6.57 | 00:14:45.002 | Poland             | Poland             | 102 | Ball Recovery   |   -   | [5.7, 31.8]     |                           |  |
|  +6.57 | 00:14:45.002 | Poland             | Poland             | 102 | Carry           |   -   | [5.7, 31.8]     | Carry                     |  |

---

### Case 66: Episode `3794692_p111_66c40651`
- **Match**: `3794692` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.47 | 00:25:33.859 | Sweden             | Sweden             | 40 | Pass            |   -   | [63.9, 34.2]    | -> Kristoffer Ols         |  |
|  -1.23 | 00:25:35.105 | Sweden             | Sweden             | 40 | Ball Receipt*   |   -   | [64.6, 43.8]    | Controlled Receipt        |  |
|  -1.23 | 00:25:35.105 | Sweden             | Sweden             | 40 | Carry           |   -   | [64.6, 43.8]    | Carry                     |  |
|  +2.29 | 00:25:38.624 | Sweden             | Sweden             | 40 | Pass            |   -   | [63.0, 37.9]    | -> Marcus Andreas         |  |
|  +3.98 | 00:25:40.317 | Sweden             | Sweden             | 40 | Ball Receipt*   |   -   | [63.3, 7.6]     | Controlled Receipt        |  |
|  +3.98 | 00:25:40.317 | Sweden             | Sweden             | 40 | Carry           |   -   | [63.3, 7.6]     | Carry                     |  |
|  +4.06 | 00:25:40.397 | Sweden             | Sweden             | 40 | Pass            |   -   | [63.3, 7.6]     | -> Emil Peter For         |  |
|  +5.49 | 00:25:41.824 | Sweden             | Sweden             | 40 | Ball Receipt*   |   -   | [76.6, 6.1]     | Controlled Receipt        |  |
|  +5.49 | 00:25:41.824 | Sweden             | Sweden             | 40 | Carry           |   -   | [76.6, 6.1]     | Carry                     |  |
|  +5.83 | 00:25:42.159 | Sweden             | Sweden             | 40 | Pass            |   -   | [76.6, 6.1]     | -> Ludwig Augusti         | **OPPONENT LAST CONTROL** |
|  -1.51 | 00:25:34.828 | Sweden             | Sweden             | 110 | Pass            |   -   | [100.6, 78.7]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:25:36.333 | Sweden             | Sweden             | 110 | Ball Receipt*   |   -   | [90.4, 77.3]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:25:36.333 | Ukraine            | Ukraine            | 111 | Pass            |  Yes  | [25.8, 4.5]     | -> Ruslan Malinov         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.76 | 00:25:37.092 | Ukraine            | Ukraine            | 111 | Ball Receipt*   |   -   | [19.8, 2.0]     | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.76 | 00:25:37.092 | Ukraine            | Ukraine            | 111 | Pass            |   -   | [20.2, 2.0]     | -> Oleksandr Zinc         |  |
|  +2.84 | 00:25:39.175 | Ukraine            | Ukraine            | 111 | Ball Receipt*   |   -   | [9.6, 17.4]     | Controlled Receipt        |  |
|  +2.84 | 00:25:39.175 | Ukraine            | Ukraine            | 111 | Carry           |   -   | [9.6, 17.4]     | Carry                     |  |
|  +3.66 | 00:25:39.990 | Ukraine            | Ukraine            | 111 | Pass            |   -   | [9.0, 18.4]     | -> Heorhii Bushch         |  |
|  +5.13 | 00:25:41.468 | Ukraine            | Ukraine            | 111 | Ball Receipt*   |   -   | [7.4, 39.7]     | Controlled Receipt        |  |
|  +5.13 | 00:25:41.468 | Ukraine            | Ukraine            | 111 | Pass            |   -   | [7.7, 40.3]     | Incomplete (Incomplete)   |  |

---

### Case 67: Episode `3794692_p136_46e2607c`
- **Match**: `3794692` (UEFA Euro) | **Period**: 3
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.07 | 00:05:21.344 | Sweden             | Sweden             | 8 | Pass            |   -   | [36.1, 37.6]    | -> Kristoffer Ols         |  |
|  -0.64 | 00:05:21.779 | Ukraine            | Sweden             | 8 | Pressure        |   -   | [72.4, 43.3]    |                           |  |
|  -0.38 | 00:05:22.041 | Sweden             | Sweden             | 8 | Ball Receipt*   |   -   | [47.7, 36.8]    | Controlled Receipt        |  |
|  -0.38 | 00:05:22.041 | Sweden             | Sweden             | 8 | Carry           |   -   | [47.7, 36.8]    | Carry                     |  |
|  +0.77 | 00:05:23.185 | Sweden             | Sweden             | 8 | Pass            |   -   | [43.3, 31.3]    | -> Marcus Andreas         |  |
|  +2.39 | 00:05:24.806 | Sweden             | Sweden             | 8 | Ball Receipt*   |   -   | [47.1, 11.4]    | Controlled Receipt        |  |
|  +2.39 | 00:05:24.806 | Sweden             | Sweden             | 8 | Carry           |   -   | [47.1, 11.4]    | Carry                     |  |
|  +5.78 | 00:05:28.193 | Sweden             | Sweden             | 8 | Pass            |   -   | [67.0, 6.2]     | -> Alexander Isak         |  |
|  +6.95 | 00:05:29.368 | Ukraine            | Sweden             | 8 | Pressure        |   -   | [25.8, 74.7]    |                           |  |
|  +7.21 | 00:05:29.626 | Sweden             | Sweden             | 8 | Ball Receipt*   |   -   | [94.3, 5.4]     | Controlled Receipt        |  |
|  +7.21 | 00:05:29.626 | Sweden             | Sweden             | 8 | Carry           |   -   | [94.3, 5.4]     | Carry                     |  |
|  +7.75 | 00:05:30.170 | Sweden             | Sweden             | 8 | Dispossessed    |   -   | [96.5, 5.4]     | Dispossessed              |  |
|  +7.75 | 00:05:30.170 | Ukraine            | Sweden             | 8 | Duel            |   -   | [23.6, 74.7]    | Tackle, Lost Out          |  |
|  -2.44 | 00:05:19.973 | Ukraine            | Sweden             | 76 | Miscontrol      |   -   | [37.6, 44.3]    | Miscontrol                |  |
|  -1.97 | 00:05:20.442 | Ukraine            | Sweden             | 76 | Pressure        |   -   | [39.6, 44.3]    |                           |  |
|  -1.71 | 00:05:20.703 | Sweden             | Sweden             | 76 | Pass            |   -   | [79.1, 35.3]    | -> Emil Peter For         |  |
|  -0.71 | 00:05:21.704 | Sweden             | Sweden             | 76 | Ball Receipt*   |   -   | [76.5, 20.6]    | Controlled Receipt        |  |
|  -0.71 | 00:05:21.704 | Sweden             | Sweden             | 76 | Carry           |   -   | [76.5, 20.6]    | Carry                     |  |
|  +1.61 | 00:05:24.025 | Sweden             | Sweden             | 76 | Pass            |   -   | [80.7, 32.7]    | -> Mikael Lustig          |  |
|  +3.30 | 00:05:25.717 | Sweden             | Sweden             | 76 | Ball Receipt*   |   -   | [81.8, 63.0]    | Controlled Receipt        |  |
|  +3.30 | 00:05:25.717 | Sweden             | Sweden             | 76 | Carry           |   -   | [81.8, 63.0]    | Carry                     |  |
|  +4.39 | 00:05:26.806 | Sweden             | Sweden             | 76 | Pass            |   -   | [88.8, 60.3]    | -> Dejan Kulusevs         |  |
|  +5.65 | 00:05:28.062 | Sweden             | Sweden             | 76 | Ball Receipt*   |   -   | [101.7, 78.7]   | Controlled Receipt        |  |
|  +5.65 | 00:05:28.062 | Sweden             | Sweden             | 76 | Carry           |   -   | [101.7, 78.7]   | Carry                     |  |
|  +7.67 | 00:05:30.087 | Sweden             | Sweden             | 76 | Pass            |   -   | [98.8, 77.6]    | Incomplete (Incomplete)   |  |
|  +7.76 | 00:05:30.181 | Ukraine            | Sweden             | 76 | Block           |   -   | [19.7, 4.9]     |                           |  |
|  -2.99 | 00:05:19.423 | Sweden             | Sweden             | 135 | Block           |   -   | [88.3, 71.2]    |                           |  |
|  -2.83 | 00:05:19.581 | Sweden             | Sweden             | 135 | Ball Recovery   |   -   | [88.3, 73.1]    |                           |  |
|  -2.83 | 00:05:19.581 | Sweden             | Sweden             | 135 | Carry           |   -   | [88.3, 73.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.94 | 00:05:20.479 | Ukraine            | Sweden             | 135 | Pressure        |   -   | [32.1, 7.0]     |                           |  |
|  -1.11 | 00:05:21.303 | Sweden             | Sweden             | 135 | Pass            |   -   | [89.6, 73.1]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:05:22.416 | Sweden             | Sweden             | 135 | Ball Receipt*   |   -   | [98.2, 49.6]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:05:22.416 | Ukraine            | Ukraine            | 136 | Pass            |  Yes  | [21.3, 26.5]    | -> Evgeny Makaren         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.71 | 00:05:23.123 | Ukraine            | Ukraine            | 136 | Ball Receipt*   |   -   | [25.9, 24.6]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.71 | 00:05:23.123 | Ukraine            | Ukraine            | 136 | Carry           |   -   | [25.9, 24.6]    | Carry                     |  |
|  +2.34 | 00:05:24.760 | Ukraine            | Ukraine            | 136 | Pass            |   -   | [20.0, 16.3]    | -> Artem Besedin          |  |
|  +4.10 | 00:05:26.511 | Ukraine            | Ukraine            | 136 | Ball Receipt*   |   -   | [47.5, 12.9]    | Controlled Receipt        |  |
|  +4.10 | 00:05:26.511 | Ukraine            | Ukraine            | 136 | Carry           |   -   | [47.5, 12.9]    | Carry                     |  |
|  +4.53 | 00:05:26.945 | Sweden             | Ukraine            | 136 | Pressure        |  Yes  | [72.6, 67.2]    |                           |  |
|  +4.94 | 00:05:27.358 | Ukraine            | Ukraine            | 136 | Pass            |   -   | [47.5, 12.9]    | -> Oleksandr Zinc         |  |
|  +6.02 | 00:05:28.441 | Sweden             | Ukraine            | 136 | Pressure        |   -   | [80.3, 70.9]    |                           |  |
|  +6.21 | 00:05:28.627 | Ukraine            | Ukraine            | 136 | Ball Receipt*   |   -   | [39.8, 9.2]     | Controlled Receipt        |  |
|  +6.21 | 00:05:28.627 | Ukraine            | Ukraine            | 136 | Carry           |   -   | [39.8, 9.2]     | Carry                     |  |
|  +6.90 | 00:05:29.313 | Ukraine            | Ukraine            | 136 | Dispossessed    |   -   | [39.8, 8.9]     | Dispossessed              |  |
|  +6.90 | 00:05:29.313 | Sweden             | Ukraine            | 136 | Duel            |   -   | [80.3, 71.2]    | Tackle, Lost Out          |  |

---

### Case 68: Episode `3794692_p151_060a9107`
- **Match**: `3794692` (UEFA Euro) | **Period**: 4
- **Counterpressing Team**: **Ukraine** vs Actual Opponent: **Sweden** (StatsBomb Poss Team: `Ukraine`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.80 | 00:01:43.818 | Ukraine            | Ukraine            | 3 | Pass            |   -   | [55.6, 0.1]     | -> Serhiy Kryvtso         | **PRESSING-TEAM FIRST CONTROL** |
|  +2.30 | 00:01:45.318 | Ukraine            | Ukraine            | 3 | Ball Receipt*   |   -   | [35.5, 26.8]    | Controlled Receipt        |  |
|  +2.71 | 00:01:45.729 | Ukraine            | Ukraine            | 3 | Pass            |   -   | [36.3, 36.1]    | -> Illia Zabarnyi         |  |
|  +4.25 | 00:01:47.269 | Ukraine            | Ukraine            | 3 | Ball Receipt*   |   -   | [42.9, 66.2]    | Controlled Receipt        |  |
|  +5.96 | 00:01:48.979 | Ukraine            | Ukraine            | 3 | Pass            |   -   | [48.4, 67.8]    | -> Andriy Yarmole         |  |
|  +6.58 | 00:01:49.595 | Ukraine            | Ukraine            | 3 | Ball Receipt*   |   -   | [56.7, 67.0]    | Controlled Receipt        |  |
|  +6.58 | 00:01:49.595 | Ukraine            | Ukraine            | 3 | Carry           |   -   | [56.7, 67.0]    | Carry                     |  |
|  +7.75 | 00:01:50.769 | Ukraine            | Ukraine            | 3 | Pass            |   -   | [56.7, 67.0]    | -> Illia Zabarnyi         |  |
|  +0.11 | 00:01:43.127 | Sweden             | Sweden             | 74 | Pass            |   -   | [80.1, 80.0]    | -> Victor Nilsson         |  |
|  +2.15 | 00:01:45.163 | Sweden             | Sweden             | 74 | Ball Receipt*   |   -   | [53.3, 75.0]    | Controlled Receipt        |  |
|  +2.15 | 00:01:45.163 | Sweden             | Sweden             | 74 | Carry           |   -   | [53.3, 75.0]    | Carry                     |  |
|  +3.54 | 00:01:46.553 | Sweden             | Sweden             | 74 | Pass            |   -   | [55.2, 72.0]    | -> Kristoffer Ols         |  |
|  +4.60 | 00:01:47.611 | Sweden             | Sweden             | 74 | Ball Receipt*   |   -   | [62.0, 55.1]    | Controlled Receipt        |  |
|  +4.60 | 00:01:47.611 | Sweden             | Sweden             | 74 | Carry           |   -   | [62.0, 55.1]    | Carry                     |  |
|  +7.28 | 00:01:50.295 | Sweden             | Sweden             | 74 | Pass            |   -   | [61.2, 57.1]    | -> Emil Peter For         | **OPPONENT LAST CONTROL** |
|  -2.54 | 00:01:40.478 | Ukraine            | Ukraine            | 134 | Ball Receipt*   |   -   | [67.3, 73.1]    | Controlled Receipt        |  |
|  -2.54 | 00:01:40.478 | Ukraine            | Ukraine            | 134 | Carry           |   -   | [67.3, 73.1]    | Carry                     |  |
|  -2.60 | 00:01:40.412 | Sweden             | Sweden             | 150 | Pass            |   -   | [74.9, 4.8]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.22 | 00:01:42.797 | Sweden             | Sweden             | 150 | Pressure        |   -   | [98.2, 10.2]    |                           |  |
|  +0.00 | 00:01:43.015 | Sweden             | Sweden             | 150 | Ball Receipt*   |   -   | [98.5, 11.1]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:01:43.015 | Ukraine            | Ukraine            | 151 | Pass            |  Yes  | [22.5, 70.9]    | -> Illia Zabarnyi         | **CP INITIATION** |
|  +2.33 | 00:01:45.347 | Ukraine            | Ukraine            | 151 | Ball Receipt*   |   -   | [8.8, 64.7]     | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.33 | 00:01:45.347 | Ukraine            | Ukraine            | 151 | Carry           |   -   | [8.8, 64.7]     | Carry                     |  |
|  +3.01 | 00:01:46.027 | Sweden             | Ukraine            | 151 | Pressure        |  Yes  | [113.1, 16.0]   |                           |  |
|  +4.04 | 00:01:47.053 | Sweden             | Ukraine            | 151 | Foul Committed  |  Yes  | [114.5, 18.1]   |                           |  |
|  +4.04 | 00:01:47.053 | Ukraine            | Ukraine            | 151 | Foul Won        |   -   | [5.6, 62.0]     |                           |  |

---

### Case 69: Episode `3794692_p53_328aaa85`
- **Match**: `3794692` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Sweden** vs Actual Opponent: **Ukraine** (StatsBomb Poss Team: `Sweden`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.87 | 00:35:10.176 | Ukraine            | Ukraine            | 52 | Ball Receipt*   |   -   | [34.9, 8.6]     | Controlled Receipt        |  |
|  -2.87 | 00:35:10.176 | Ukraine            | Ukraine            | 52 | Pass            |   -   | [34.9, 8.6]     | -> Oleksandr Zinc         |  |
|  -1.98 | 00:35:11.069 | Ukraine            | Ukraine            | 52 | Ball Receipt*   |   -   | [30.8, 7.0]     | Controlled Receipt        |  |
|  -1.98 | 00:35:11.069 | Ukraine            | Ukraine            | 52 | Pass            |   -   | [30.8, 7.0]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:35:13.045 | Ukraine            | Ukraine            | 52 | Ball Receipt*   |   -   | [54.9, 28.9]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:35:13.045 | Sweden             | Sweden             | 53 | Pass            |  Yes  | [69.5, 52.4]    | -> Emil Peter For         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +2.33 | 00:35:15.374 | Sweden             | Sweden             | 53 | Ball Receipt*   |   -   | [88.3, 25.2]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.33 | 00:35:15.374 | Sweden             | Sweden             | 53 | Carry           |   -   | [88.3, 25.2]    | Carry                     |  |
|  +4.58 | 00:35:17.626 | Sweden             | Sweden             | 53 | Pass            |   -   | [86.8, 24.6]    | -> Kristoffer Ols         |  |
|  +5.04 | 00:35:18.083 | Sweden             | Sweden             | 53 | Ball Receipt*   |   -   | [85.5, 28.9]    | Controlled Receipt        |  |
|  +5.04 | 00:35:18.083 | Sweden             | Sweden             | 53 | Carry           |   -   | [85.5, 28.9]    | Carry                     |  |
|  -2.03 | 00:35:11.020 | Ukraine            | Ukraine            | 121 | Pass            |   -   | [46.2, 40.1]    | -> Mykola Matvien         |  |
|  -0.44 | 00:35:12.602 | Ukraine            | Ukraine            | 121 | Ball Receipt*   |   -   | [46.2, 10.1]    | Controlled Receipt        |  |
|  -0.44 | 00:35:12.602 | Ukraine            | Ukraine            | 121 | Carry           |   -   | [46.2, 10.1]    | Carry                     |  |
|  +1.80 | 00:35:14.843 | Ukraine            | Ukraine            | 121 | Pass            |   -   | [49.4, 14.2]    | -> Serhiy Kryvtso         |  |
|  +3.27 | 00:35:16.316 | Ukraine            | Ukraine            | 121 | Ball Receipt*   |   -   | [42.4, 28.5]    | Controlled Receipt        |  |
|  +3.27 | 00:35:16.316 | Ukraine            | Ukraine            | 121 | Carry           |   -   | [42.4, 28.5]    | Carry                     |  |
|  +4.73 | 00:35:17.779 | Ukraine            | Ukraine            | 121 | Pass            |   -   | [45.9, 33.1]    | -> Serhii Sydorch         |  |
|  +6.42 | 00:35:19.466 | Ukraine            | Ukraine            | 121 | Ball Receipt*   |   -   | [55.7, 65.5]    | Controlled Receipt        |  |
|  +6.42 | 00:35:19.466 | Ukraine            | Ukraine            | 121 | Carry           |   -   | [55.7, 65.5]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 70: Episode `3795107_p74_565273f4`
- **Match**: `3795107` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Belgium** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Belgium`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.84 | 00:44:39.504 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [98.2, 72.0]    | Incomplete Receipt (Incomplete) |  |
|  -2.84 | 00:44:39.504 | Italy              | Belgium            | 74 | Pass            |   -   | [16.9, 6.8]     | -> Giorgio Chiell         |  |
|  -1.94 | 00:44:40.404 | Italy              | Belgium            | 74 | Ball Receipt*   |   -   | [20.4, 19.8]    | Controlled Receipt        |  |
|  -1.94 | 00:44:40.404 | Italy              | Belgium            | 74 | Carry           |   -   | [20.4, 19.8]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.92 | 00:44:40.428 | Italy              | Belgium            | 74 | Pass            |   -   | [21.4, 21.3]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.21 | 00:44:42.134 | Italy              | Belgium            | 74 | Pressure        |   -   | [49.7, 16.9]    |                           |  |
|  +0.00 | 00:44:42.348 | Italy              | Belgium            | 74 | Ball Receipt*   |   -   | [49.7, 16.2]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:44:42.348 | Belgium            | Belgium            | 74 | Pass            |  Yes  | [69.2, 66.0]    | -> Youri Tieleman         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +1.04 | 00:44:43.386 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [85.0, 58.8]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +1.04 | 00:44:43.386 | Belgium            | Belgium            | 74 | Carry           |   -   | [85.0, 58.8]    | Carry                     |  |
|  +1.86 | 00:44:44.209 | Belgium            | Belgium            | 74 | Pass            |   -   | [84.8, 58.1]    | -> Thorgan Hazard         |  |
|  +2.72 | 00:44:45.069 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [86.9, 38.6]    | Controlled Receipt        |  |
|  +2.72 | 00:44:45.069 | Belgium            | Belgium            | 74 | Carry           |   -   | [86.9, 38.6]    | Carry                     |  |
|  +2.80 | 00:44:45.149 | Belgium            | Belgium            | 74 | Pass            |   -   | [86.7, 39.3]    | -> Youri Tieleman         |  |
|  +3.51 | 00:44:45.853 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [84.8, 47.4]    | Controlled Receipt        |  |
|  +3.51 | 00:44:45.853 | Belgium            | Belgium            | 74 | Carry           |   -   | [84.8, 47.4]    | Carry                     |  |
|  +3.62 | 00:44:45.970 | Belgium            | Belgium            | 74 | Pass            |   -   | [84.8, 47.4]    | -> Axel Witsel            |  |
|  +5.32 | 00:44:47.670 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [82.0, 28.0]    | Controlled Receipt        |  |
|  +5.32 | 00:44:47.670 | Belgium            | Belgium            | 74 | Carry           |   -   | [82.0, 28.0]    | Carry                     |  |
|  +5.36 | 00:44:47.710 | Belgium            | Belgium            | 74 | Pass            |   -   | [83.1, 26.7]    | -> Jeremy Doku            |  |
|  +6.80 | 00:44:49.153 | Belgium            | Belgium            | 74 | Ball Receipt*   |   -   | [95.0, 13.2]    | Controlled Receipt        |  |
|  +6.80 | 00:44:49.153 | Belgium            | Belgium            | 74 | Carry           |   -   | [95.0, 13.2]    | Carry                     |  |

---

### Case 71: Episode `3795107_p44_34f7b3d5`
- **Match**: `3795107` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Belgium** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Belgium`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.54 | 00:24:55.143 | Italy              | Italy              | 43 | Pass            |   -   | [105.9, 8.5]    | -> Ciro Immobile          |  |
|  -1.79 | 00:24:55.891 | Italy              | Italy              | 43 | Ball Receipt*   |   -   | [104.9, 37.4]   | Controlled Receipt        |  |
|  -1.79 | 00:24:55.891 | Italy              | Italy              | 43 | Carry           |   -   | [104.9, 37.4]   | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.16 | 00:24:56.518 | Belgium            | Italy              | 43 | Pressure        |   -   | [11.4, 42.3]    |                           |  |
|  -0.75 | 00:24:56.934 | Italy              | Italy              | 43 | Pass            |   -   | [107.0, 38.5]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:24:57.680 | Italy              | Italy              | 43 | Ball Receipt*   |   -   | [99.7, 42.1]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:24:57.680 | Belgium            | Belgium            | 44 | Pass            |  Yes  | [18.2, 38.6]    | -> Kevin De Bruyn         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.55 | 00:24:58.233 | Belgium            | Belgium            | 44 | Ball Receipt*   |   -   | [23.8, 47.2]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.55 | 00:24:58.233 | Belgium            | Belgium            | 44 | Carry           |   -   | [23.8, 47.2]    | Carry                     |  |
|  +1.17 | 00:24:58.848 | Italy              | Belgium            | 44 | Pressure        |  Yes  | [91.6, 33.1]    |                           |  |
|  +1.24 | 00:24:58.919 | Italy              | Belgium            | 44 | Dribbled Past   |  Yes  | [91.6, 36.5]    |                           |  |
|  +1.24 | 00:24:58.919 | Belgium            | Belgium            | 44 | Dribble         |   -   | [28.5, 43.6]    | Complete                  |  |
|  +1.24 | 00:24:58.919 | Belgium            | Belgium            | 44 | Carry           |   -   | [28.5, 43.6]    | Carry                     |  |
|  +5.55 | 00:25:03.232 | Belgium            | Belgium            | 44 | Pass            |   -   | [64.4, 42.3]    | -> Romelu Lukaku          |  |
|  +7.38 | 00:25:05.058 | Belgium            | Belgium            | 44 | Ball Receipt*   |   -   | [84.3, 59.6]    | Controlled Receipt        |  |
|  +7.38 | 00:25:05.058 | Belgium            | Belgium            | 44 | Carry           |   -   | [84.3, 59.6]    | Carry                     |  |
|  -2.52 | 00:24:55.156 | Italy              | Belgium            | 119 | Clearance       |   -   | [13.6, 22.9]    |                           |  |
|  +5.19 | 00:25:02.870 | Belgium            | Belgium            | 119 | Ball Recovery   |   -   | [32.8, 65.9]    |                           |  |
|  +5.19 | 00:25:02.870 | Belgium            | Belgium            | 119 | Carry           |   -   | [32.8, 65.9]    | Carry                     |  |
|  +7.60 | 00:25:05.280 | Belgium            | Belgium            | 119 | Pass            |   -   | [34.3, 66.7]    | -> Kevin De Bruyn         |  |

---

### Case 72: Episode `3788765_p13_b69c4d20`
- **Match**: `3788765` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Switzerland** vs Actual Opponent: **Turkey** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.87 | 00:05:16.980 | Turkey             | Turkey             | 12 | Ball Receipt*   |   -   | [51.0, 8.9]     | Controlled Receipt        |  |
|  -2.80 | 00:05:17.043 | Turkey             | Turkey             | 12 | Pass            |   -   | [51.0, 8.9]     | -> Mert Müldür            | **OPPONENT LAST CONTROL** |
|  -1.71 | 00:05:18.141 | Turkey             | Turkey             | 12 | Ball Receipt*   |   -   | [42.2, 5.7]     | Controlled Receipt        |  |
|  -1.67 | 00:05:18.181 | Turkey             | Turkey             | 12 | Pass            |   -   | [42.2, 5.7]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:05:19.847 | Turkey             | Turkey             | 12 | Ball Receipt*   |   -   | [57.4, 4.9]     | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:05:19.847 | Switzerland        | Switzerland        | 13 | Pass            |  Yes  | [64.6, 74.8]    | -> Silvan Widmer          | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +1.88 | 00:05:21.728 | Switzerland        | Switzerland        | 13 | Ball Receipt*   |   -   | [70.6, 77.6]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +1.88 | 00:05:21.728 | Switzerland        | Switzerland        | 13 | Pass            |   -   | [70.6, 77.8]    | Incomplete (Incomplete)   |  |
|  +4.11 | 00:05:23.960 | Switzerland        | Switzerland        | 13 | Pressure        |   -   | [95.2, 60.1]    |                           |  |
|  +5.55 | 00:05:25.398 | Switzerland        | Switzerland        | 13 | Ball Receipt*   |   -   | [102.9, 58.8]   | Incomplete Receipt (Incomplete) |  |
|  +5.55 | 00:05:25.398 | Turkey             | Switzerland        | 13 | Clearance       |   -   | [14.2, 23.2]    |                           |  |
|  +7.34 | 00:05:27.183 | Turkey             | Switzerland        | 13 | Pressure        |   -   | [8.8, 20.9]     |                           |  |

---

### Case 73: Episode `3795506_p102_06a2e479`
- **Match**: `3795506` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **England** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `England`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +2.56 | 00:08:22.914 | England            | England            | 15 | Pass            |   -   | [14.1, 0.1]     | -> Harry Kane             | **PRESSING-TEAM FIRST CONTROL** |
|  +4.06 | 00:08:24.412 | England            | England            | 15 | Ball Receipt*   |   -   | [30.0, 4.9]     | Controlled Receipt        |  |
|  +4.06 | 00:08:24.412 | England            | England            | 15 | Carry           |   -   | [30.0, 4.9]     | Carry                     |  |
|  +5.30 | 00:08:25.652 | England            | England            | 15 | Pass            |   -   | [29.1, 2.6]     | Incomplete (Incomplete)   |  |
|  -2.44 | 00:08:17.905 | Italy              | Italy              | 101 | Ball Receipt*   |   -   | [41.3, 35.0]    | Controlled Receipt        |  |
|  -2.44 | 00:08:17.905 | England            | Italy              | 101 | Duel            |  Yes  | [78.0, 45.0]    | Aerial Lost               |  |
|  -2.44 | 00:08:17.905 | Italy              | Italy              | 101 | Pass            |   -   | [42.1, 35.1]    | -> Jorge Luiz Fre         |  |
|  -0.64 | 00:08:19.711 | Italy              | Italy              | 101 | Ball Receipt*   |   -   | [40.4, 40.6]    | Controlled Receipt        |  |
|  -0.55 | 00:08:19.800 | Italy              | Italy              | 101 | Pass            |   -   | [40.4, 40.6]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:08:20.349 | Italy              | Italy              | 101 | Ball Receipt*   |   -   | [49.7, 26.3]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:08:20.349 | England            | England            | 102 | Pass            |  Yes  | [72.1, 49.8]    | -> Declan Rice            | **CP INITIATION** |
|  +0.58 | 00:08:20.931 | England            | England            | 102 | Ball Receipt*   |   -   | [65.2, 44.4]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.58 | 00:08:20.931 | England            | England            | 102 | Carry           |   -   | [65.2, 44.4]    | Carry                     |  |
|  +1.64 | 00:08:21.985 | Italy              | England            | 102 | Pressure        |  Yes  | [49.7, 43.7]    |                           |  |
|  +2.12 | 00:08:22.464 | Italy              | England            | 102 | Dribbled Past   |  Yes  | [51.5, 41.2]    |                           |  |
|  +2.12 | 00:08:22.464 | England            | England            | 102 | Dribble         |   -   | [68.6, 38.9]    | Complete                  |  |
|  +2.12 | 00:08:22.464 | England            | England            | 102 | Carry           |   -   | [68.6, 38.9]    | Carry                     |  |
|  +3.97 | 00:08:24.316 | England            | England            | 102 | Pass            |   -   | [72.7, 28.0]    | -> Mason Mount            |  |
|  +5.52 | 00:08:25.870 | England            | England            | 102 | Ball Receipt*   |   -   | [85.2, 6.7]     | Controlled Receipt        |  |
|  +5.52 | 00:08:25.870 | England            | England            | 102 | Carry           |   -   | [85.2, 6.7]     | Carry                     |  |
|  +5.60 | 00:08:25.950 | England            | England            | 102 | Pass            |   -   | [85.2, 6.7]     | -> Luke Shaw              |  |
|  +6.78 | 00:08:27.130 | England            | England            | 102 | Ball Receipt*   |   -   | [72.4, 2.4]     | Controlled Receipt        |  |
|  +6.78 | 00:08:27.130 | England            | England            | 102 | Carry           |   -   | [72.4, 2.4]     | Carry                     |  |
|  +6.88 | 00:08:27.232 | Italy              | England            | 102 | Pressure        |   -   | [44.4, 76.6]    |                           |  |
|  -2.75 | 00:08:17.597 | Italy              | Italy              | 174 | Shot            |   -   | [95.0, 54.8]    | Blocked                   | **OPPONENT LAST CONTROL** |
|  -2.56 | 00:08:17.793 | England            | Italy              | 174 | Block           |   -   | [21.9, 26.9]    |                           |  |
|  -2.48 | 00:08:17.873 | England            | Italy              | 174 | Goal Keeper     |   -   | [4.7, 37.8]     |                           |  |
|  -0.40 | 00:08:19.946 | England            | England            | 175 | Ball Recovery   |   -   | [3.0, 48.7]     |                           |  |
|  -0.40 | 00:08:19.946 | England            | England            | 175 | Carry           |   -   | [3.0, 48.7]     | Carry                     |  |

---

### Case 74: Episode `3795506_p126_bc52fc8c`
- **Match**: `3795506` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Italy** vs Actual Opponent: **England** (StatsBomb Poss Team: `Italy`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.75 | 00:26:52.292 | Italy              | Italy              | 46 | Ball Receipt*   |   -   | [66.2, 31.0]    | Controlled Receipt        |  |
|  -2.75 | 00:26:52.292 | Italy              | Italy              | 46 | Carry           |   -   | [66.2, 31.0]    | Carry                     |  |
|  -0.87 | 00:26:54.174 | Italy              | Italy              | 46 | Pass            |   -   | [71.3, 28.1]    | -> Giorgio Chiell         |  |
|  +0.41 | 00:26:55.454 | Italy              | Italy              | 46 | Ball Receipt*   |   -   | [63.4, 14.9]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.41 | 00:26:55.454 | Italy              | Italy              | 46 | Carry           |   -   | [63.4, 14.9]    | Carry                     |  |
|  +1.53 | 00:26:56.574 | Italy              | Italy              | 46 | Pass            |   -   | [63.3, 16.9]    | -> Leonardo Bonuc         |  |
|  +2.89 | 00:26:57.934 | Italy              | Italy              | 46 | Ball Receipt*   |   -   | [57.6, 36.7]    | Controlled Receipt        |  |
|  +2.89 | 00:26:57.934 | Italy              | Italy              | 46 | Carry           |   -   | [57.6, 36.7]    | Carry                     |  |
|  +5.14 | 00:27:00.185 | Italy              | Italy              | 46 | Pass            |   -   | [62.8, 43.7]    | -> Giovanni Di Lo         |  |
|  +6.98 | 00:27:02.023 | Italy              | Italy              | 46 | Ball Receipt*   |   -   | [69.4, 73.7]    | Controlled Receipt        |  |
|  +6.98 | 00:27:02.023 | Italy              | Italy              | 46 | Pass            |   -   | [69.4, 74.2]    | -> Jorge Luiz Fre         |  |
|  -1.90 | 00:26:53.141 | England            | England            | 125 | Pass            |   -   | [70.4, 51.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.63 | 00:26:54.414 | England            | England            | 125 | Pressure        |   -   | [84.6, 59.8]    |                           |  |
|  +0.00 | 00:26:55.043 | England            | England            | 125 | Ball Receipt*   |   -   | [79.2, 61.8]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:26:55.043 | Italy              | Italy              | 126 | Pass            |  Yes  | [29.1, 22.9]    | -> Gianluigi Donn         | **CP INITIATION** |
|  +3.47 | 00:26:58.509 | Italy              | Italy              | 126 | Ball Receipt*   |   -   | [3.8, 29.8]     | Controlled Receipt        | (v2.6 Regain Event) |
|  +3.47 | 00:26:58.509 | Italy              | Italy              | 126 | Carry           |   -   | [3.8, 29.8]     | Carry                     |  |
|  +4.91 | 00:26:59.949 | Italy              | Italy              | 126 | Pass            |   -   | [4.9, 33.4]     | -> Leonardo Bonuc         |  |
|  +5.94 | 00:27:00.984 | Italy              | Italy              | 126 | Ball Receipt*   |   -   | [11.4, 38.6]    | Controlled Receipt        |  |
|  +5.94 | 00:27:00.984 | Italy              | Italy              | 126 | Carry           |   -   | [11.4, 38.6]    | Carry                     |  |
|  +7.66 | 00:27:02.704 | Italy              | Italy              | 126 | Pass            |   -   | [12.9, 36.8]    | -> Giorgio Chiell         |  |

---

### Case 75: Episode `3788765_p132_9fdaa035`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Switzerland** vs Actual Opponent: **Turkey** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.37 | 00:19:28.232 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [39.4, 72.9]    | -> Manuel Obafemi         |  |
|  -0.97 | 00:19:29.636 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [33.6, 51.5]    | Controlled Receipt        |  |
|  -0.97 | 00:19:29.636 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [33.6, 51.5]    | Carry                     |  |
|  +3.52 | 00:19:34.121 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [51.4, 25.0]    | -> Breel-Donald E         | **PRESSING-TEAM FIRST CONTROL** |
|  +4.43 | 00:19:35.039 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [59.9, 24.6]    | Controlled Receipt        |  |
|  +4.43 | 00:19:35.039 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [59.9, 24.6]    | Carry                     |  |
|  +4.49 | 00:19:35.095 | Turkey             | Switzerland        | 43 | Pressure        |   -   | [56.7, 55.1]    |                           |  |
|  +4.83 | 00:19:35.436 | Switzerland        | Switzerland        | 43 | Pass            |   -   | [59.9, 24.3]    | -> Manuel Obafemi         |  |
|  +5.82 | 00:19:36.421 | Switzerland        | Switzerland        | 43 | Ball Receipt*   |   -   | [50.1, 24.6]    | Controlled Receipt        |  |
|  +5.82 | 00:19:36.421 | Switzerland        | Switzerland        | 43 | Carry           |   -   | [50.1, 24.6]    | Carry                     |  |
|  -1.38 | 00:19:29.225 | Turkey             | Turkey             | 131 | Ball Receipt*   |   -   | [77.7, 34.9]    | Controlled Receipt        |  |
|  -1.34 | 00:19:29.265 | Switzerland        | Turkey             | 131 | Duel            |   -   | [42.4, 45.2]    | Aerial Lost               |  |
|  -1.34 | 00:19:29.265 | Turkey             | Turkey             | 131 | Pass            |   -   | [77.7, 34.9]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:19:30.604 | Turkey             | Turkey             | 131 | Ball Receipt*   |   -   | [88.4, 34.9]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:19:30.604 | Turkey             | Turkey             | 131 | Duel            |   -   | [86.7, 35.1]    | Aerial Lost               |  |
|  +0.00 | 00:19:30.604 | Switzerland        | Switzerland        | 132 | Pass            |  Yes  | [33.4, 45.0]    | -> Remo Freuler           | **CP INITIATION** |
|  +2.19 | 00:19:32.790 | Switzerland        | Switzerland        | 132 | Ball Receipt*   |   -   | [33.8, 53.8]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.19 | 00:19:32.790 | Switzerland        | Switzerland        | 132 | Carry           |   -   | [33.8, 53.8]    | Carry                     |  |
|  +2.22 | 00:19:32.821 | Switzerland        | Switzerland        | 132 | Pass            |   -   | [33.8, 53.8]    | -> Silvan Widmer          |  |
|  +3.12 | 00:19:33.726 | Switzerland        | Switzerland        | 132 | Ball Receipt*   |   -   | [24.4, 52.0]    | Controlled Receipt        |  |
|  +3.12 | 00:19:33.726 | Switzerland        | Switzerland        | 132 | Pass            |   -   | [24.4, 52.0]    | Incomplete (Incomplete)   |  |
|  +5.43 | 00:19:36.038 | Turkey             | Switzerland        | 132 | Pass            |   -   | [73.6, 38.2]    | -> Okay Yokuşlu           |  |
|  +6.41 | 00:19:37.018 | Turkey             | Switzerland        | 132 | Ball Receipt*   |   -   | [77.3, 28.7]    | Controlled Receipt        |  |
|  +6.41 | 00:19:37.018 | Turkey             | Switzerland        | 132 | Carry           |   -   | [77.3, 28.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +6.83 | 00:19:37.432 | Turkey             | Switzerland        | 132 | Miscontrol      |   -   | [77.3, 28.7]    | Miscontrol                | **POSSIBLE TRANSITION** |
|  +7.09 | 00:19:37.695 | Turkey             | Switzerland        | 132 | Pressure        |   -   | [78.8, 26.9]    |                           |  |
|  +7.79 | 00:19:38.399 | Switzerland        | Switzerland        | 132 | Pass            |   -   | [36.4, 53.4]    | -> Breel-Donald E         |  |

---

### Case 76: Episode `3788765_p96_999f4ff1`
- **Match**: `3788765` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Switzerland** vs Actual Opponent: **Turkey** (StatsBomb Poss Team: `Switzerland`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +5.99 | 00:02:22.167 | Turkey             | Turkey             | 7 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete)   |  |
|  +7.33 | 00:02:23.510 | Turkey             | Turkey             | 7 | Ball Receipt*   |   -   | [112.6, 36.7]   | Incomplete Receipt (Incomplete) |  |
|  +7.33 | 00:02:23.510 | Turkey             | Turkey             | 7 | Duel            |   -   | [114.1, 36.1]   | Aerial Lost               |  |
|  +7.33 | 00:02:23.510 | Switzerland        | Turkey             | 7 | Clearance       |   -   | [6.0, 44.0]     |                           |  |
|  -1.97 | 00:02:14.209 | Turkey             | Turkey             | 95 | Pass            |   -   | [46.3, 75.7]    | Incomplete (Incomplete)   |  |
|  +0.00 | 00:02:16.177 | Turkey             | Turkey             | 95 | Ball Receipt*   |   -   | [90.8, 58.1]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:02:16.177 | Switzerland        | Switzerland        | 96 | Pass            |  Yes  | [36.4, 17.7]    | -> Remo Freuler           | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +1.73 | 00:02:17.907 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [41.0, 27.3]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +1.73 | 00:02:17.907 | Turkey             | Switzerland        | 96 | Duel            |  Yes  | [79.1, 52.8]    | Aerial Lost               |  |
|  +1.73 | 00:02:17.907 | Switzerland        | Switzerland        | 96 | Pass            |   -   | [41.0, 27.3]    | -> Ricardo Iván R         |  |
|  +3.67 | 00:02:19.844 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [36.0, 20.8]    | Controlled Receipt        |  |
|  +3.67 | 00:02:19.844 | Switzerland        | Switzerland        | 96 | Pass            |   -   | [36.0, 20.8]    | Incomplete (Incomplete)   |  |
|  +5.00 | 00:02:21.174 | Switzerland        | Switzerland        | 96 | Ball Receipt*   |   -   | [43.6, 20.3]    | Incomplete Receipt (Incomplete) |  |
|  +5.00 | 00:02:21.174 | Turkey             | Switzerland        | 96 | Pass            |   -   | [73.8, 59.8]    | -> Mehmet Zeki Çe         |  |
|  +5.38 | 00:02:21.554 | Switzerland        | Switzerland        | 96 | Pressure        |  Yes  | [56.7, 12.4]    |                           |  |
|  +6.31 | 00:02:22.491 | Turkey             | Switzerland        | 96 | Ball Receipt*   |   -   | [64.0, 63.2]    | Controlled Receipt        |  |
|  +6.31 | 00:02:22.491 | Turkey             | Switzerland        | 96 | Carry           |   -   | [64.0, 63.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +6.47 | 00:02:22.642 | Turkey             | Switzerland        | 96 | Miscontrol      |   -   | [64.0, 62.4]    | Miscontrol                | **POSSIBLE TRANSITION** |

---

### Case 77: Episode `3788769_p93_47a3beaa`
- **Match**: `3788769` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Russia** vs Actual Opponent: **Denmark** (StatsBomb Poss Team: `Russia`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -0.34 | 00:03:16.502 | Russia             | Russia             | 15 | Referee Ball-Drop |   -   | [68.2, 7.6]     |                           |  |
|  +0.00 | 00:03:16.845 | Denmark            | Russia             | 15 | Pass            |   -   | [47.1, 72.3]    | -> Simon Thorup K         |  |
|  +1.22 | 00:03:18.066 | Denmark            | Russia             | 15 | Ball Receipt*   |   -   | [40.9, 59.7]    | Controlled Receipt        |  |
|  +3.22 | 00:03:20.059 | Denmark            | Russia             | 15 | Pass            |   -   | [40.5, 59.3]    | -> Thomas Delaney         |  |
|  +4.14 | 00:03:20.979 | Denmark            | Russia             | 15 | Ball Receipt*   |   -   | [50.3, 49.9]    | Controlled Receipt        |  |
|  +4.14 | 00:03:20.979 | Denmark            | Russia             | 15 | Carry           |   -   | [50.3, 49.9]    | Carry                     |  |
|  +4.95 | 00:03:21.788 | Denmark            | Russia             | 15 | Pass            |   -   | [47.8, 50.3]    | -> Andreas Christ         |  |
|  +6.47 | 00:03:23.309 | Denmark            | Russia             | 15 | Ball Receipt*   |   -   | [47.8, 75.1]    | Controlled Receipt        |  |
|  +6.47 | 00:03:23.309 | Denmark            | Russia             | 15 | Carry           |   -   | [47.8, 75.1]    | Carry                     |  |
|  +7.77 | 00:03:24.613 | Denmark            | Russia             | 15 | Pass            |   -   | [47.6, 73.0]    | -> Simon Thorup K         |  |
|  -1.55 | 00:03:15.289 | Denmark            | Russia             | 93 | Ball Receipt*   |   -   | [42.5, 56.4]    | Controlled Receipt        |  |
|  -1.55 | 00:03:15.289 | Denmark            | Russia             | 93 | Carry           |   -   | [42.5, 56.4]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.44 | 00:03:15.404 | Denmark            | Russia             | 93 | Pass            |   -   | [42.6, 56.1]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:03:16.843 | Denmark            | Russia             | 93 | Ball Receipt*   |   -   | [55.1, 56.0]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:03:16.843 | Russia             | Russia             | 93 | Pass            |  Yes  | [66.5, 24.6]    | -> Igor Diveev            | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +2.56 | 00:03:19.404 | Russia             | Russia             | 93 | Ball Receipt*   |   -   | [48.9, 34.0]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +2.56 | 00:03:19.404 | Russia             | Russia             | 93 | Carry           |   -   | [48.9, 34.0]    | Carry                     |  |
|  +6.49 | 00:03:23.337 | Russia             | Russia             | 93 | Pass            |   -   | [47.0, 24.0]    | -> Daler Kuzyaev          |  |
|  +7.73 | 00:03:24.575 | Russia             | Russia             | 93 | Ball Receipt*   |   -   | [64.2, 5.4]     | Controlled Receipt        |  |
|  +7.73 | 00:03:24.575 | Russia             | Russia             | 93 | Carry           |   -   | [64.2, 5.4]     | Carry                     |  |

---

### Case 78: Episode `3788747_p183_b959a0a9`
- **Match**: `3788747` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **North Macedonia** vs Actual Opponent: **Austria** (StatsBomb Poss Team: `North Macedonia`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.00 | 00:42:11.590 | Austria            | Austria            | 182 | Duel            |   -   | [58.5, 34.6]    | Aerial Lost               |  |
|  +0.00 | 00:42:11.590 | North Macedonia    | North Macedonia    | 183 | Pass            |  Yes  | [61.6, 45.5]    | -> Stefan Ristovs         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +3.06 | 00:42:14.653 | North Macedonia    | North Macedonia    | 183 | Ball Receipt*   |   -   | [43.1, 58.2]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +3.06 | 00:42:14.653 | North Macedonia    | North Macedonia    | 183 | Carry           |   -   | [43.1, 58.2]    | Carry                     |  |
|  +3.49 | 00:42:15.082 | North Macedonia    | North Macedonia    | 183 | Pass            |   -   | [37.2, 58.2]    | -> Stole Dimitrie         |  |
|  +5.87 | 00:42:17.460 | North Macedonia    | North Macedonia    | 183 | Ball Receipt*   |   -   | [10.6, 46.2]    | Controlled Receipt        |  |
|  +5.87 | 00:42:17.461 | North Macedonia    | North Macedonia    | 183 | Pass            |   -   | [8.3, 47.2]     | -> Stefan Ristovs         |  |
|  +7.42 | 00:42:19.012 | North Macedonia    | North Macedonia    | 183 | Ball Receipt*   |   -   | [27.7, 64.5]    | Controlled Receipt        |  |
|  +7.42 | 00:42:19.012 | North Macedonia    | North Macedonia    | 183 | Carry           |   -   | [27.7, 64.5]    | Carry                     |  |

---

### Case 79: Episode `3788769_p97_1ce450ed`
- **Match**: `3788769` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Denmark** vs Actual Opponent: **Russia** (StatsBomb Poss Team: `Denmark`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.64 | 00:05:24.777 | Denmark            | Denmark            | 17 | Pass            |   -   | [65.9, 46.4]    | -> Andreas Christ         |  |
|  -1.34 | 00:05:26.078 | Russia             | Denmark            | 17 | Pressure        |   -   | [40.5, 10.8]    |                           |  |
|  -1.21 | 00:05:26.204 | Denmark            | Denmark            | 17 | Ball Receipt*   |   -   | [78.0, 70.9]    | Controlled Receipt        |  |
|  -1.21 | 00:05:26.204 | Denmark            | Denmark            | 17 | Carry           |   -   | [78.0, 70.9]    | Carry                     |  |
|  -0.78 | 00:05:26.638 | Denmark            | Denmark            | 17 | Pass            |   -   | [78.9, 71.4]    | -> Daniel Wass            |  |
|  -0.15 | 00:05:27.263 | Denmark            | Denmark            | 17 | Ball Receipt*   |   -   | [84.6, 77.3]    | Controlled Receipt        |  |
|  -0.15 | 00:05:27.263 | Denmark            | Denmark            | 17 | Carry           |   -   | [84.6, 77.3]    | Carry                     |  |
|  +1.60 | 00:05:29.021 | Denmark            | Denmark            | 17 | Pass            |   -   | [85.1, 77.3]    | -> Thomas Delaney         | **PRESSING-TEAM FIRST CONTROL** |
|  +3.11 | 00:05:30.532 | Denmark            | Denmark            | 17 | Ball Receipt*   |   -   | [77.3, 62.5]    | Controlled Receipt        |  |
|  +3.11 | 00:05:30.532 | Denmark            | Denmark            | 17 | Carry           |   -   | [77.3, 62.5]    | Carry                     |  |
|  +4.39 | 00:05:31.804 | Denmark            | Denmark            | 17 | Pass            |   -   | [77.8, 61.1]    | -> Joakim Mæhle           |  |
|  +7.31 | 00:05:34.731 | Denmark            | Denmark            | 17 | Ball Receipt*   |   -   | [112.6, 10.0]   | Controlled Receipt        |  |
|  +7.31 | 00:05:34.731 | Denmark            | Denmark            | 17 | Carry           |   -   | [112.6, 10.0]   | Carry                     |  |
|  +7.40 | 00:05:34.820 | Denmark            | Denmark            | 17 | Miscontrol      |   -   | [112.6, 10.0]   | Miscontrol                |  |
|  -1.38 | 00:05:26.033 | Russia             | Russia             | 96 | Ball Receipt*   |   -   | [67.6, 41.2]    | Controlled Receipt        |  |
|  -1.38 | 00:05:26.033 | Denmark            | Russia             | 96 | Duel            |   -   | [52.5, 38.9]    | Aerial Lost               |  |
|  -1.38 | 00:05:26.033 | Russia             | Russia             | 96 | Pass            |   -   | [67.6, 41.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.00 | 00:05:27.417 | Russia             | Russia             | 96 | Ball Receipt*   |   -   | [69.2, 49.6]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:05:27.417 | Denmark            | Denmark            | 97 | Pass            |  Yes  | [51.7, 33.0]    | -> Joakim Mæhle           | **CP INITIATION** |
|  +1.65 | 00:05:29.070 | Denmark            | Denmark            | 97 | Ball Receipt*   |   -   | [35.9, 16.6]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +1.65 | 00:05:29.070 | Denmark            | Denmark            | 97 | Carry           |   -   | [35.9, 16.6]    | Carry                     |  |
|  +2.72 | 00:05:30.140 | Denmark            | Denmark            | 97 | Pass            |   -   | [36.5, 19.2]    | -> Mikkel Damsgaa         |  |
|  +4.29 | 00:05:31.703 | Denmark            | Denmark            | 97 | Ball Receipt*   |   -   | [59.5, 11.7]    | Controlled Receipt        |  |
|  +4.29 | 00:05:31.703 | Denmark            | Denmark            | 97 | Carry           |   -   | [59.5, 11.7]    | Carry                     |  |
|  +5.67 | 00:05:33.091 | Denmark            | Denmark            | 97 | Pass            |   -   | [61.4, 10.8]    | -> Pierre-Emile H         |  |

---

### Case 80: Episode `3788741_p30_5b4d0ce1`
- **Match**: `3788741` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Turkey** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Turkey`)
- **Stratum**: `ball_receipt` | **First Press Control Candidate**: `Ball Receipt*`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `controlled_ball_receipt`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.20 | 00:12:30.024 | Turkey             | Italy              | 29 | Pressure        |  Yes  | [70.4, 24.7]    |                           |  |
|  -2.12 | 00:12:30.103 | Italy              | Italy              | 29 | Ball Receipt*   |   -   | [42.9, 55.7]    | Controlled Receipt        |  |
|  -2.12 | 00:12:30.103 | Italy              | Italy              | 29 | Carry           |   -   | [42.9, 55.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.77 | 00:12:30.448 | Italy              | Italy              | 29 | Pass            |   -   | [43.9, 55.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.20 | 00:12:32.018 | Italy              | Italy              | 29 | Pressure        |   -   | [57.1, 45.3]    |                           |  |
|  +0.00 | 00:12:32.222 | Italy              | Italy              | 29 | Ball Receipt*   |   -   | [55.4, 44.9]    | Incomplete Receipt (Incomplete) |  |
|  +0.00 | 00:12:32.222 | Turkey             | Turkey             | 30 | Pass            |  Yes  | [67.6, 38.3]    | -> Mehmet Zeki Çe         | **CP INITIATION** | **PRESSING-TEAM FIRST CONTROL** |
|  +0.91 | 00:12:33.135 | Turkey             | Turkey             | 30 | Ball Receipt*   |   -   | [57.0, 51.3]    | Controlled Receipt        | (v2.6 Regain Event) |
|  +0.91 | 00:12:33.135 | Turkey             | Turkey             | 30 | Carry           |   -   | [57.0, 51.3]    | Carry                     |  |
|  +2.78 | 00:12:35.004 | Turkey             | Turkey             | 30 | Pass            |   -   | [50.1, 50.9]    | -> Merih Demiral          |  |
|  +3.91 | 00:12:36.135 | Turkey             | Turkey             | 30 | Ball Receipt*   |   -   | [41.4, 38.8]    | Controlled Receipt        |  |
|  +3.91 | 00:12:36.135 | Turkey             | Turkey             | 30 | Carry           |   -   | [41.4, 38.8]    | Carry                     |  |
|  +4.98 | 00:12:37.201 | Turkey             | Turkey             | 30 | Pass            |   -   | [41.4, 38.8]    | -> Okay Yokuşlu           |  |
|  +5.88 | 00:12:38.098 | Turkey             | Turkey             | 30 | Ball Receipt*   |   -   | [48.8, 31.9]    | Controlled Receipt        |  |
|  +5.88 | 00:12:38.098 | Turkey             | Turkey             | 30 | Carry           |   -   | [48.8, 31.9]    | Carry                     |  |
|  +7.43 | 00:12:39.655 | Turkey             | Turkey             | 30 | Pass            |   -   | [49.1, 31.2]    | -> Caglar Söyüncü         |  |

---

### Case 81: Episode `3893790_p87_4644ab81`
- **Match**: `3893790` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Canada Women's** vs Actual Opponent: **Nigeria Women's** (StatsBomb Poss Team: `Canada Women's`)
- **Stratum**: `dribble` | **First Press Control Candidate**: `Dribble`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `dribble_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.59 | 00:01:28.211 | Nigeria Women's    | Canada Women's     | 6 | Pressure        |   -   | [26.8, 63.2]    |                           |  |
|  -2.27 | 00:01:28.530 | Canada Women's     | Canada Women's     | 6 | Pass            |   -   | [88.8, 15.4]    | -> Ashley Elizabe         |  |
|  -1.95 | 00:01:28.847 | Canada Women's     | Canada Women's     | 6 | Ball Receipt*   |   -   | [95.4, 5.0]     | Controlled Receipt        |  |
|  -1.95 | 00:01:28.847 | Canada Women's     | Canada Women's     | 6 | Carry           |   -   | [95.4, 5.0]     | Carry                     |  |
|  -1.80 | 00:01:29.007 | Canada Women's     | Canada Women's     | 6 | Pass            |   -   | [95.4, 5.0]     | -> Julia Angela G         |  |
|  -0.69 | 00:01:30.117 | Canada Women's     | Canada Women's     | 6 | Ball Receipt*   |   -   | [85.8, 11.7]    | Controlled Receipt        |  |
|  -0.69 | 00:01:30.117 | Canada Women's     | Canada Women's     | 6 | Carry           |   -   | [85.8, 11.7]    | Carry                     |  |
|  +0.39 | 00:01:31.188 | Canada Women's     | Canada Women's     | 6 | Pass            |   -   | [85.8, 11.7]    | -> Vanessa Brigit         | **PRESSING-TEAM FIRST CONTROL** |
|  +2.10 | 00:01:32.907 | Canada Women's     | Canada Women's     | 6 | Ball Receipt*   |   -   | [60.2, 19.0]    | Controlled Receipt        |  |
|  +2.10 | 00:01:32.907 | Canada Women's     | Canada Women's     | 6 | Carry           |   -   | [60.2, 19.0]    | Carry                     |  |
|  +3.93 | 00:01:34.736 | Canada Women's     | Canada Women's     | 6 | Pass            |   -   | [52.3, 19.2]    | -> Kadeisha Bucha         |  |
|  +5.68 | 00:01:36.480 | Canada Women's     | Canada Women's     | 6 | Ball Receipt*   |   -   | [56.3, 43.8]    | Controlled Receipt        |  |
|  +5.68 | 00:01:36.480 | Canada Women's     | Canada Women's     | 6 | Carry           |   -   | [56.3, 43.8]    | Carry                     |  |
|  +7.67 | 00:01:38.470 | Canada Women's     | Canada Women's     | 6 | Pass            |   -   | [60.5, 51.7]    | -> Jordyn Pamela          |  |
|  -1.81 | 00:01:28.988 | Canada Women's     | Canada Women's     | 87 | Pressure        |   -   | [115.9, 72.1]   |                           |  |
|  -1.18 | 00:01:29.627 | Canada Women's     | Canada Women's     | 87 | Ball Receipt*   |   -   | [112.4, 69.7]   | Incomplete Receipt (Incomplete) |  |
|  -1.18 | 00:01:29.627 | Nigeria Women's    | Canada Women's     | 87 | Ball Recovery   |   -   | [5.1, 9.0]      |                           |  |
|  -1.18 | 00:01:29.627 | Nigeria Women's    | Canada Women's     | 87 | Carry           |   -   | [5.1, 9.0]      | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.00 | 00:01:30.802 | Nigeria Women's    | Canada Women's     | 87 | Dispossessed    |   -   | [2.7, 11.1]     | Dispossessed              | **POSSIBLE TRANSITION** |
|  -0.00 | 00:01:30.802 | Canada Women's     | Canada Women's     | 87 | Duel            |  Yes  | [117.4, 69.0]   | Tackle, Won               | **CP INITIATION** |
|  -0.00 | 00:01:30.802 | Canada Women's     | Canada Women's     | 87 | Carry           |   -   | [117.4, 69.0]   | Carry                     |  |
|  +1.52 | 00:01:32.320 | Nigeria Women's    | Canada Women's     | 87 | Pressure        |   -   | [7.2, 16.2]     |                           |  |
|  +2.12 | 00:01:32.924 | Nigeria Women's    | Canada Women's     | 87 | Dribbled Past   |   -   | [3.4, 15.7]     |                           |  |
|  +2.12 | 00:01:32.924 | Canada Women's     | Canada Women's     | 87 | Dribble         |   -   | [116.7, 64.4]   | Complete                  | (v2.6 Regain Event) |
|  +2.12 | 00:01:32.924 | Canada Women's     | Canada Women's     | 87 | Carry           |   -   | [116.7, 64.4]   | Carry                     |  |
|  +2.95 | 00:01:33.748 | Canada Women's     | Canada Women's     | 87 | Pass            |   -   | [111.7, 63.5]   | -> Christine Marg         |  |
|  +3.75 | 00:01:34.551 | Canada Women's     | Canada Women's     | 87 | Ball Receipt*   |   -   | [103.8, 53.2]   | Controlled Receipt        |  |
|  +3.75 | 00:01:34.551 | Canada Women's     | Canada Women's     | 87 | Carry           |   -   | [103.8, 53.2]   | Carry                     |  |
|  +4.18 | 00:01:34.985 | Nigeria Women's    | Canada Women's     | 87 | Pressure        |   -   | [10.7, 22.7]    |                           |  |
|  +4.77 | 00:01:35.568 | Nigeria Women's    | Canada Women's     | 87 | Foul Committed  |   -   | [13.2, 24.9]    |                           |  |
|  +4.77 | 00:01:35.568 | Canada Women's     | Canada Women's     | 87 | Foul Won        |   -   | [106.9, 55.2]   |                           |  |

---

### Case 82: Episode `3802948_p50_f7594958`
- **Match**: `3802948` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Paris Saint-Germain** vs Actual Opponent: **Metz** (StatsBomb Poss Team: `Paris Saint-Germain`)
- **Stratum**: `dribble` | **First Press Control Candidate**: `Dribble`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `dribble_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.59 | 00:22:12.021 | Metz               | Metz               | 49 | Ball Recovery   |   -   | [97.0, 23.7]    |                           |  |
|  +0.00 | 00:22:13.607 | Metz               | Metz               | 49 | Dispossessed    |   -   | [96.8, 10.1]    | Dispossessed              |  |
|  +0.00 | 00:22:13.607 | Paris Saint-Germai | Paris Saint-Germai | 50 | Duel            |  Yes  | [23.3, 70.0]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +1.39 | 00:22:14.994 | Metz               | Paris Saint-Germai | 50 | Pressure        |   -   | [94.2, 3.7]     |                           |  |
|  +1.77 | 00:22:15.376 | Metz               | Paris Saint-Germai | 50 | Dribbled Past   |   -   | [90.3, 3.0]     |                           |  |
|  +1.77 | 00:22:15.376 | Paris Saint-Germai | Paris Saint-Germai | 50 | Dribble         |   -   | [29.8, 77.1]    | Complete                  | (v2.6 Regain Event) |
|  +1.77 | 00:22:15.376 | Paris Saint-Germai | Paris Saint-Germai | 50 | Carry           |   -   | [29.8, 77.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.49 | 00:22:17.093 | Metz               | Paris Saint-Germai | 50 | Pressure        |   -   | [83.2, 2.1]     |                           |  |
|  +5.69 | 00:22:19.297 | Metz               | Paris Saint-Germai | 50 | Foul Committed  |   -   | [65.1, 4.1]     |                           |  |
|  +5.69 | 00:22:19.297 | Paris Saint-Germai | Paris Saint-Germai | 50 | Foul Won        |   -   | [55.0, 76.0]    |                           |  |

---

### Case 83: Episode `3902967_p92_d75810ac`
- **Match**: `3902967` (Women's World Cup) | **Period**: 1
- **Counterpressing Team**: **England Women's** vs Actual Opponent: **Colombia Women's** (StatsBomb Poss Team: `England Women's`)
- **Stratum**: `shot` | **First Press Control Candidate**: `Shot`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `shot_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.84 | 00:50:53.439 | England Women's    | England Women's    | 90 | Ball Receipt*   |   -   | [109.3, 47.7]   | Controlled Receipt        |  |
|  -2.84 | 00:50:53.439 | England Women's    | England Women's    | 90 | Carry           |   -   | [109.3, 47.7]   | Carry                     |  |
|  -2.75 | 00:50:53.530 | England Women's    | England Women's    | 90 | Miscontrol      |   -   | [109.3, 46.8]   | Miscontrol                |  |
|  -1.10 | 00:50:55.182 | Colombia Women's   | Colombia Women's   | 91 | Goal Keeper     |   -   | [8.2, 38.2]     |                           |  |
|  -1.10 | 00:50:55.182 | Colombia Women's   | Colombia Women's   | 91 | Carry           |   -   | [8.2, 38.2]     | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.87 | 00:50:55.407 | Colombia Women's   | Colombia Women's   | 91 | Miscontrol      |   -   | [8.2, 38.9]     | Miscontrol                |  |
|  -0.82 | 00:50:55.461 | Colombia Women's   | Colombia Women's   | 91 | Error           |   -   | [9.0, 38.9]     |                           |  |
|  +0.00 | 00:50:56.279 | Colombia Women's   | Colombia Women's   | 91 | 50/50           |  Yes  | [8.0, 38.7]     |                           |  |
|  +0.00 | 00:50:56.279 | England Women's    | England Women's    | 92 | 50/50           |  Yes  | [112.1, 41.4]   |                           | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +0.07 | 00:50:56.348 | England Women's    | England Women's    | 92 | Shot            |   -   | [111.5, 40.9]   | Saved                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +0.16 | 00:50:56.443 | Colombia Women's   | England Women's    | 92 | Goal Keeper     |   -   | [6.5, 39.2]     |                           |  |
|  +1.42 | 00:50:57.703 | England Women's    | England Women's    | 92 | Ball Recovery   |   -   | [112.8, 39.1]   |                           |  |
|  +1.55 | 00:50:57.834 | England Women's    | England Women's    | 92 | Shot            |   -   | [114.5, 37.5]   | Goal                      |  |
|  +1.99 | 00:50:58.273 | Colombia Women's   | England Women's    | 92 | Goal Keeper     |   -   | [6.0, 41.2]     |                           |  |

---

### Case 84: Episode `3857298_p13_71ba7805`
- **Match**: `3857298` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Ghana** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `shot` | **First Press Control Candidate**: `Shot`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `shot_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.80 | 00:05:42.917 | Ghana              | Ghana              | 12 | Pass            |   -   | [6.9, 67.8]     | -> Thomas Teye Pa         |  |
|  -2.45 | 00:05:43.267 | Ghana              | Ghana              | 12 | Ball Receipt*   |   -   | [13.9, 61.0]    | Controlled Receipt        |  |
|  -2.45 | 00:05:43.267 | Ghana              | Ghana              | 12 | Pass            |   -   | [13.9, 61.0]    | -> Mohammed Kudus         |  |
|  -1.31 | 00:05:44.408 | Ghana              | Ghana              | 12 | Ball Receipt*   |   -   | [24.9, 52.9]    | Controlled Receipt        |  |
|  -1.31 | 00:05:44.408 | Ghana              | Ghana              | 12 | Carry           |   -   | [24.9, 52.9]    | Carry                     |  |
|  -0.34 | 00:05:45.376 | Portugal           | Ghana              | 12 | Pressure        |   -   | [91.4, 27.6]    |                           |  |
|  +0.00 | 00:05:45.714 | Ghana              | Ghana              | 12 | Dispossessed    |   -   | [26.3, 52.0]    | Dispossessed              |  |
|  +0.00 | 00:05:45.714 | Portugal           | Portugal           | 13 | Duel            |  Yes  | [93.8, 28.1]    | Tackle, Won               | **CP INITIATION** |
|  +1.30 | 00:05:47.011 | Portugal           | Portugal           | 13 | Shot            |   -   | [98.1, 36.6]    | Blocked                   | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +1.38 | 00:05:47.096 | Ghana              | Portugal           | 13 | Block           |  Yes  | [19.6, 43.0]    |                           |  |
|  +1.42 | 00:05:47.136 | Ghana              | Portugal           | 13 | Goal Keeper     |   -   | [5.0, 41.3]     |                           |  |
|  +3.89 | 00:05:49.600 | Ghana              | Portugal           | 13 | Pass            |   -   | [36.6, 59.6]    | Incomplete (Incomplete)   |  |
|  +5.53 | 00:05:51.248 | Ghana              | Portugal           | 13 | Ball Receipt*   |   -   | [49.2, 50.9]    | Incomplete Receipt (Incomplete) |  |
|  +5.53 | 00:05:51.248 | Portugal           | Portugal           | 13 | Pass            |   -   | [66.6, 28.1]    | -> Otávio Edmilso         |  |
|  +6.48 | 00:05:52.190 | Portugal           | Portugal           | 13 | Ball Receipt*   |   -   | [72.3, 24.7]    | Controlled Receipt        |  |
|  +6.48 | 00:05:52.190 | Portugal           | Portugal           | 13 | Carry           |   -   | [72.3, 24.7]    | Carry                     |  |
|  +6.50 | 00:05:52.214 | Portugal           | Portugal           | 13 | Pass            |   -   | [72.3, 24.7]    | -> Diogo Meireles         |  |
|  -2.35 | 00:05:43.365 | Ghana              | Ghana              | 100 | Pass            |   -   | [105.5, 21.3]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -1.95 | 00:05:43.761 | Ghana              | Ghana              | 100 | Ball Receipt*   |   -   | [103.1, 15.1]   | Incomplete Receipt (Incomplete) |  |
|  -1.95 | 00:05:43.761 | Portugal           | Portugal           | 101 | Ball Recovery   |   -   | [11.6, 59.1]    |                           |  |
|  -1.95 | 00:05:43.761 | Portugal           | Portugal           | 101 | Carry           |   -   | [11.6, 59.1]    | Carry                     |  |
|  -0.83 | 00:05:44.879 | Ghana              | Portugal           | 101 | Pressure        |  Yes  | [104.4, 14.8]   |                           |  |
|  -0.61 | 00:05:45.105 | Portugal           | Portugal           | 101 | Pass            |   -   | [16.2, 68.8]    | -> Bruno Miguel B         |  |
|  +0.48 | 00:05:46.193 | Portugal           | Portugal           | 101 | Ball Receipt*   |   -   | [31.9, 67.5]    | Controlled Receipt        |  |
|  +0.48 | 00:05:46.193 | Portugal           | Portugal           | 101 | Carry           |   -   | [31.9, 67.5]    | Carry                     |  |
|  +1.49 | 00:05:47.204 | Ghana              | Portugal           | 101 | Pressure        |  Yes  | [88.2, 10.2]    |                           |  |
|  +1.66 | 00:05:47.371 | Portugal           | Portugal           | 101 | Pass            |   -   | [28.7, 69.4]    | -> Rúben Diogo Da         |  |
|  +2.64 | 00:05:48.351 | Portugal           | Portugal           | 101 | Ball Receipt*   |   -   | [25.2, 64.0]    | Controlled Receipt        |  |
|  +2.64 | 00:05:48.351 | Portugal           | Portugal           | 101 | Carry           |   -   | [25.2, 64.0]    | Carry                     |  |
|  +2.71 | 00:05:48.428 | Ghana              | Portugal           | 101 | Pressure        |  Yes  | [92.0, 17.8]    |                           |  |
|  +3.61 | 00:05:49.326 | Portugal           | Portugal           | 101 | Pass            |   -   | [24.9, 55.0]    | Incomplete (Incomplete)   |  |
|  +5.58 | 00:05:51.290 | Portugal           | Portugal           | 101 | Ball Receipt*   |   -   | [26.5, 17.6]    | Incomplete Receipt (Incomplete) |  |
|  +5.58 | 00:05:51.290 | Ghana              | Portugal           | 101 | Ball Recovery   |   -   | [85.7, 56.8]    |                           |  |
|  +5.58 | 00:05:51.290 | Ghana              | Portugal           | 101 | Carry           |   -   | [85.7, 56.8]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 85: Episode `3835321_p115_bed582ee`
- **Match**: `3835321` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Spain Women's** vs Actual Opponent: **WNT Finland** (StatsBomb Poss Team: `Spain Women's`)
- **Stratum**: `shot` | **First Press Control Candidate**: `Shot`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `shot_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.77 | 00:16:26.485 | WNT Finland        | Spain Women's      | 115 | Block           |   -   | [7.5, 40.6]     |                           |  |
|  -0.69 | 00:16:28.568 | Spain Women's      | Spain Women's      | 115 | Pressure        |   -   | [100.4, 36.3]   |                           |  |
|  -0.61 | 00:16:28.651 | Spain Women's      | Spain Women's      | 115 | Pressure        |   -   | [97.4, 35.5]    |                           |  |
|  -0.48 | 00:16:28.777 | WNT Finland        | Spain Women's      | 115 | Ball Recovery   |   -   | [21.5, 44.2]    |                           |  |
|  -0.48 | 00:16:28.777 | WNT Finland        | Spain Women's      | 115 | Carry           |   -   | [21.5, 44.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:16:29.260 | WNT Finland        | Spain Women's      | 115 | Dribble         |   -   | [22.7, 46.1]    | Incomplete                |  |
|  +0.00 | 00:16:29.260 | Spain Women's      | Spain Women's      | 115 | Duel            |  Yes  | [97.4, 34.0]    | Tackle, Won               | **CP INITIATION** | **POSSIBLE TRANSITION** |
|  +1.15 | 00:16:30.408 | Spain Women's      | Spain Women's      | 115 | Shot            |   -   | [103.1, 33.3]   | Off T                     | **PRESSING-TEAM FIRST CONTROL** | (v2.6 Regain Event) |
|  +2.75 | 00:16:32.006 | WNT Finland        | Spain Women's      | 115 | Goal Keeper     |   -   | [1.4, 40.9]     |                           |  |

---

### Case 86: Episode `3895333_p8_2dab9ebc`
- **Match**: `3895333` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Eintracht Frankfurt** vs Actual Opponent: **Bayer Leverkusen** (StatsBomb Poss Team: `Eintracht Frankfurt`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.35 | 00:01:52.126 | Eintracht Frankfur | Eintracht Frankfur | 8 | Pass            |   -   | [63.6, 67.1]    | Incomplete (Incomplete)   |  |
|  -0.60 | 00:01:53.877 | Eintracht Frankfur | Eintracht Frankfur | 8 | Ball Receipt*   |   -   | [90.6, 61.5]    | Incomplete Receipt (Incomplete) |  |
|  -0.60 | 00:01:53.877 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Pass            |   -   | [27.5, 10.3]    | -> Arthur Augusto         |  |
|  +0.00 | 00:01:54.477 | Eintracht Frankfur | Eintracht Frankfur | 8 | Pressure        |  Yes  | [83.9, 69.1]    |                           | **CP INITIATION** |
|  +0.16 | 00:01:54.634 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Ball Receipt*   |   -   | [33.2, 10.5]    | Controlled Receipt        |  |
|  +0.16 | 00:01:54.634 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Carry           |   -   | [33.2, 10.5]    | Carry                     |  |
|  +0.89 | 00:01:55.365 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Dispossessed    |   -   | [30.0, 9.7]     | Dispossessed              |  |
|  +0.89 | 00:01:55.365 | Eintracht Frankfur | Eintracht Frankfur | 8 | Duel            |  Yes  | [90.1, 70.4]    | Tackle, Won               | (v2.6 Regain Event) |
|  +0.89 | 00:01:55.365 | Eintracht Frankfur | Eintracht Frankfur | 8 | Carry           |   -   | [90.1, 70.4]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.88 | 00:01:57.356 | Eintracht Frankfur | Eintracht Frankfur | 8 | Pass            |   -   | [98.0, 66.4]    | Incomplete (Incomplete)   |  |
|  +3.14 | 00:01:57.614 | Eintracht Frankfur | Eintracht Frankfur | 8 | Ball Receipt*   |   -   | [101.6, 60.7]   | Incomplete Receipt (Incomplete) |  |
|  +3.14 | 00:01:57.614 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Interception    |   -   | [17.9, 16.5]    | Won                       |  |
|  +3.14 | 00:01:57.614 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Carry           |   -   | [17.9, 16.5]    | Carry                     |  |
|  +4.92 | 00:01:59.397 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Pass            |   -   | [14.0, 6.6]     | -> Arthur Augusto         |  |
|  +6.08 | 00:02:00.554 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Ball Receipt*   |   -   | [23.7, 4.2]     | Controlled Receipt        |  |
|  +6.08 | 00:02:00.554 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Carry           |   -   | [23.7, 4.2]     | Carry                     |  |
|  +6.19 | 00:02:00.667 | Eintracht Frankfur | Eintracht Frankfur | 8 | Pressure        |  Yes  | [94.7, 75.1]    |                           |  |
|  +6.90 | 00:02:01.377 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Pass            |   -   | [28.4, 4.5]     | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +7.03 | 00:02:01.511 | Bayer Leverkusen   | Eintracht Frankfur | 8 | Ball Receipt*   |   -   | [23.7, 11.7]    | Incomplete Receipt (Incomplete) |  |
|  +7.03 | 00:02:01.511 | Eintracht Frankfur | Eintracht Frankfur | 8 | Block           |  Yes  | [92.6, 72.9]    |                           |  |
|  +8.00 | 00:02:02.475 | Eintracht Frankfur | Eintracht Frankfur | 8 | Ball Recovery   |   -   | [79.4, 65.4]    |                           |  |
|  +8.00 | 00:02:02.475 | Eintracht Frankfur | Eintracht Frankfur | 8 | Carry           |   -   | [79.4, 65.4]    | Carry                     |  |
|  -0.10 | 00:01:54.373 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Ball Receipt*   |   -   | [55.7, 59.5]    | Controlled Receipt        |  |
|  -0.10 | 00:01:54.373 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Carry           |   -   | [55.7, 59.5]    | Carry                     |  |
|  +2.40 | 00:01:56.876 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Pass            |   -   | [49.2, 67.5]    | -> Nathan Tella           |  |
|  +3.52 | 00:01:58.001 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Ball Receipt*   |   -   | [62.7, 75.1]    | Controlled Receipt        |  |
|  +3.52 | 00:01:58.001 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Carry           |   -   | [62.7, 75.1]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.62 | 00:01:58.093 | Eintracht Frankfur | Bayer Leverkusen   | 78 | Pressure        |   -   | [54.5, 5.4]     |                           |  |
|  +4.78 | 00:01:59.262 | Eintracht Frankfur | Bayer Leverkusen   | 78 | Foul Committed  |   -   | [58.6, 4.4]     |                           |  |
|  +4.78 | 00:01:59.262 | Bayer Leverkusen   | Bayer Leverkusen   | 78 | Foul Won        |   -   | [61.5, 75.7]    |                           |  |

---

### Case 87: Episode `3794686_p37_3c14cf4f`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.93 | 00:20:32.387 | Croatia            | Spain              | 36 | Pressure        |   -   | [61.4, 28.8]    |                           |  |
|  -2.31 | 00:20:33.011 | Spain              | Spain              | 36 | Pass            |   -   | [57.0, 53.3]    | -> Jorge Resurrec         |  |
|  -1.51 | 00:20:33.806 | Croatia            | Spain              | 36 | Pressure        |   -   | [47.9, 22.6]    |                           |  |
|  -1.33 | 00:20:33.990 | Spain              | Spain              | 36 | Ball Receipt*   |   -   | [72.0, 57.0]    | Controlled Receipt        |  |
|  -1.33 | 00:20:33.990 | Spain              | Spain              | 36 | Carry           |   -   | [72.0, 57.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:20:35.317 | Spain              | Spain              | 36 | Dispossessed    |   -   | [61.1, 59.4]    | Dispossessed              |  |
|  +0.00 | 00:20:35.317 | Croatia            | Croatia            | 37 | Duel            |  Yes  | [59.0, 20.7]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.18 | 00:20:36.497 | Croatia            | Croatia            | 37 | Ball Recovery   |   -   | [63.7, 20.2]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.18 | 00:20:36.497 | Croatia            | Croatia            | 37 | Carry           |   -   | [63.7, 20.2]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.62 | 00:20:38.933 | Spain              | Croatia            | 37 | Pressure        |  Yes  | [39.5, 52.7]    |                           |  |
|  +3.68 | 00:20:39.001 | Croatia            | Croatia            | 37 | Pass            |   -   | [80.0, 27.4]    | -> Marcelo Brozov         |  |
|  +5.00 | 00:20:40.313 | Croatia            | Croatia            | 37 | Ball Receipt*   |   -   | [82.0, 40.2]    | Controlled Receipt        |  |
|  +5.00 | 00:20:40.313 | Croatia            | Croatia            | 37 | Carry           |   -   | [82.0, 40.2]    | Carry                     |  |
|  +5.96 | 00:20:41.277 | Spain              | Croatia            | 37 | Pressure        |   -   | [35.9, 40.5]    |                           |  |
|  +7.82 | 00:20:43.136 | Croatia            | Croatia            | 37 | Pass            |   -   | [82.8, 37.4]    | -> Mateo Kovačić          |  |

---

### Case 88: Episode `3794686_p83_01d8a962`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.51 | 00:43:57.611 | Spain              | Croatia            | 82 | Pressure        |  Yes  | [92.2, 52.5]    |                           |  |
|  -2.32 | 00:43:57.795 | Croatia            | Croatia            | 82 | Ball Receipt*   |   -   | [26.4, 27.4]    | Controlled Receipt        |  |
|  -2.32 | 00:43:57.795 | Croatia            | Croatia            | 82 | Pass            |   -   | [27.6, 27.4]    | -> Ante Rebić             |  |
|  -1.65 | 00:43:58.471 | Spain              | Croatia            | 82 | Pressure        |   -   | [77.0, 49.5]    |                           |  |
|  -1.49 | 00:43:58.633 | Croatia            | Croatia            | 82 | Ball Receipt*   |   -   | [43.1, 30.7]    | Controlled Receipt        |  |
|  -1.49 | 00:43:58.633 | Croatia            | Croatia            | 82 | Carry           |   -   | [43.1, 30.7]    | Carry                     |  |
|  -0.37 | 00:43:59.749 | Spain              | Croatia            | 82 | Pressure        |   -   | [79.0, 51.0]    |                           |  |
|  +0.00 | 00:44:00.118 | Croatia            | Croatia            | 82 | Dribble         |   -   | [41.1, 29.1]    | Incomplete                |  |
|  +0.00 | 00:44:00.118 | Spain              | Spain              | 83 | Duel            |  Yes  | [79.0, 51.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.37 | 00:44:01.487 | Spain              | Spain              | 83 | Ball Recovery   |   -   | [67.6, 50.6]    |                           | (v2.6 Regain Event) |
|  +1.37 | 00:44:01.487 | Spain              | Spain              | 83 | Carry           |   -   | [67.6, 50.6]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +1.93 | 00:44:02.045 | Spain              | Spain              | 83 | Pass            |   -   | [67.6, 50.6]    | -> José Luis Gayà         |  |
|  +4.25 | 00:44:04.365 | Spain              | Spain              | 83 | Ball Receipt*   |   -   | [56.4, 27.0]    | Controlled Receipt        |  |
|  +4.25 | 00:44:04.365 | Spain              | Spain              | 83 | Carry           |   -   | [56.4, 27.0]    | Carry                     |  |
|  +5.41 | 00:44:05.525 | Spain              | Spain              | 83 | Pass            |   -   | [56.8, 28.0]    | -> Pedro González         |  |
|  +6.46 | 00:44:06.579 | Spain              | Spain              | 83 | Ball Receipt*   |   -   | [63.6, 32.5]    | Controlled Receipt        |  |
|  +6.46 | 00:44:06.579 | Spain              | Spain              | 83 | Carry           |   -   | [63.6, 32.5]    | Carry                     |  |
|  +6.88 | 00:44:07.002 | Spain              | Spain              | 83 | Pass            |   -   | [63.7, 32.4]    | -> José Luis Gayà         |  |
|  +7.96 | 00:44:08.080 | Spain              | Spain              | 83 | Ball Receipt*   |   -   | [60.9, 22.0]    | Controlled Receipt        |  |
|  +7.96 | 00:44:08.080 | Spain              | Spain              | 83 | Carry           |   -   | [60.9, 22.0]    | Carry                     |  |
|  -1.64 | 00:43:58.479 | Croatia            | Croatia            | 166 | Ball Receipt*   |   -   | [8.0, 36.2]     | Controlled Receipt        |  |
|  -1.64 | 00:43:58.479 | Croatia            | Croatia            | 166 | Carry           |   -   | [8.0, 36.2]     | Carry                     |  |
|  +0.39 | 00:44:00.504 | Croatia            | Croatia            | 166 | Pass            |   -   | [13.5, 42.8]    | -> Luka Modrić            |  |
|  +3.72 | 00:44:03.840 | Croatia            | Croatia            | 166 | Ball Receipt*   |   -   | [26.8, 62.8]    | Controlled Receipt        |  |
|  +3.72 | 00:44:03.840 | Croatia            | Croatia            | 166 | Carry           |   -   | [26.8, 62.8]    | Carry                     |  |
|  +5.11 | 00:44:05.228 | Croatia            | Croatia            | 166 | Pass            |   -   | [31.6, 64.6]    | -> Josip Brekalo          |  |
|  +6.05 | 00:44:06.165 | Croatia            | Croatia            | 166 | Ball Receipt*   |   -   | [44.7, 73.5]    | Controlled Receipt        |  |
|  +6.05 | 00:44:06.165 | Croatia            | Croatia            | 166 | Carry           |   -   | [44.7, 73.5]    | Carry                     |  |
|  +6.09 | 00:44:06.211 | Spain              | Croatia            | 166 | Pressure        |   -   | [78.0, 9.2]     |                           |  |
|  +6.49 | 00:44:06.610 | Spain              | Croatia            | 166 | Pressure        |   -   | [77.3, 5.6]     |                           |  |
|  +6.93 | 00:44:07.051 | Croatia            | Croatia            | 166 | Dribble         |   -   | [46.2, 72.9]    | Incomplete                | **POSSIBLE TRANSITION** |
|  +6.93 | 00:44:07.051 | Spain              | Croatia            | 166 | Duel            |   -   | [73.9, 7.2]     | Tackle, Lost In Play      |  |
|  +7.87 | 00:44:07.991 | Spain              | Croatia            | 166 | Pressure        |   -   | [79.8, 16.4]    |                           |  |
|  +7.93 | 00:44:08.051 | Croatia            | Croatia            | 166 | Ball Recovery   |   -   | [45.8, 64.8]    |                           |  |
|  +7.93 | 00:44:08.051 | Croatia            | Croatia            | 166 | Carry           |   -   | [45.8, 64.8]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 89: Episode `3788764_p163_90656f0c`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.70 | 00:48:05.020 | Germany            | Germany            | 162 | Dispossessed    |   -   | [57.2, 19.4]    | Dispossessed              |  |
|  -2.70 | 00:48:05.020 | Portugal           | Germany            | 162 | Duel            |   -   | [62.9, 60.7]    | Tackle, Lost In Play      |  |
|  -1.16 | 00:48:06.554 | Portugal           | Germany            | 162 | Pressure        |   -   | [64.1, 69.1]    |                           |  |
|  -0.81 | 00:48:06.903 | Germany            | Germany            | 162 | Ball Recovery   |   -   | [57.5, 11.2]    |                           |  |
|  -0.81 | 00:48:06.903 | Germany            | Germany            | 162 | Carry           |   -   | [57.5, 11.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:48:07.716 | Germany            | Germany            | 162 | Dispossessed    |   -   | [56.0, 12.0]    | Dispossessed              |  |
|  +0.00 | 00:48:07.716 | Portugal           | Portugal           | 163 | Duel            |  Yes  | [64.1, 68.1]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.31 | 00:48:09.023 | Portugal           | Portugal           | 163 | Ball Recovery   |   -   | [73.9, 65.0]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.31 | 00:48:09.023 | Portugal           | Portugal           | 163 | Carry           |   -   | [73.9, 65.0]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +4.13 | 00:48:11.844 | Germany            | Portugal           | 163 | Pressure        |  Yes  | [27.7, 22.8]    |                           |  |
|  +4.98 | 00:48:12.692 | Portugal           | Portugal           | 163 | Pass            |   -   | [94.1, 55.9]    | -> André Miguel V         |  |
|  +5.93 | 00:48:13.642 | Portugal           | Portugal           | 163 | Ball Receipt*   |   -   | [106.7, 47.9]   | Controlled Receipt        |  |
|  +6.08 | 00:48:13.792 | Germany            | Portugal           | 163 | Pressure        |   -   | [11.7, 33.9]    |                           |  |
|  +6.37 | 00:48:14.082 | Portugal           | Portugal           | 163 | Shot            |   -   | [110.1, 49.8]   | Blocked                   |  |
|  +6.47 | 00:48:14.189 | Germany            | Portugal           | 163 | Block           |   -   | [9.0, 31.2]     |                           |  |
|  +6.51 | 00:48:14.229 | Germany            | Portugal           | 163 | Goal Keeper     |   -   | [3.1, 36.5]     |                           |  |

---

### Case 90: Episode `3794686_p88_77c2c7a6`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Croatia`)
- **Stratum**: `other` | **First Press Control Candidate**: `Interception`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `interception_plus_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.77 | 00:00:09.727 | Spain              | Croatia            | 88 | Pressure        |   -   | [73.2, 43.2]    |                           |  |
|  -2.26 | 00:00:10.233 | Croatia            | Croatia            | 88 | Ball Receipt*   |   -   | [47.3, 30.1]    | Controlled Receipt        |  |
|  -2.26 | 00:00:10.233 | Croatia            | Croatia            | 88 | Carry           |   -   | [47.3, 30.1]    | Carry                     |  |
|  -2.22 | 00:00:10.273 | Croatia            | Croatia            | 88 | Pass            |   -   | [45.8, 34.4]    | Incomplete (Incomplete)   |  |
|  -2.12 | 00:00:10.378 | Croatia            | Croatia            | 88 | Ball Receipt*   |   -   | [56.7, 44.9]    | Incomplete Receipt (Incomplete) |  |
|  -2.12 | 00:00:10.378 | Spain              | Croatia            | 88 | Block           |   -   | [72.8, 41.7]    |                           |  |
|  -0.73 | 00:00:11.767 | Croatia            | Croatia            | 88 | Ball Recovery   |   -   | [37.7, 29.7]    |                           |  |
|  +0.00 | 00:00:12.493 | Croatia            | Croatia            | 88 | Pressure        |  Yes  | [32.4, 42.3]    |                           | **CP INITIATION** |
|  +0.34 | 00:00:12.836 | Croatia            | Croatia            | 88 | Pressure        |  Yes  | [35.1, 37.4]    |                           |  |
|  +0.40 | 00:00:12.897 | Spain              | Spain              | 89 | Pass            |   -   | [87.7, 41.0]    | -> Jorge Resurrec         |  |
|  +1.11 | 00:00:13.604 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [82.4, 40.8]    | Controlled Receipt        |  |
|  +1.11 | 00:00:13.604 | Spain              | Spain              | 89 | Pass            |   -   | [83.3, 40.4]    | -> Pedro González         |  |
|  +1.67 | 00:00:14.163 | Croatia            | Spain              | 89 | Pressure        |  Yes  | [30.7, 50.0]    |                           |  |
|  +2.05 | 00:00:14.544 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [89.4, 30.1]    | Controlled Receipt        |  |
|  +2.05 | 00:00:14.544 | Spain              | Spain              | 89 | Pass            |   -   | [88.7, 26.0]    | -> Sergio Busquet         |  |
|  +3.56 | 00:00:16.055 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [79.4, 48.0]    | Controlled Receipt        |  |
|  +3.56 | 00:00:16.055 | Spain              | Spain              | 89 | Pass            |   -   | [79.4, 48.0]    | Incomplete (Incomplete)   |  |
|  +4.74 | 00:00:17.233 | Spain              | Spain              | 89 | Ball Receipt*   |   -   | [94.0, 58.5]    | Incomplete Receipt (Incomplete) |  |
|  +4.74 | 00:00:17.233 | Croatia            | Croatia            | 90 | Interception    |  Yes  | [27.7, 22.7]    | Won                       | (v2.6 Regain Event) |
|  +4.74 | 00:00:17.233 | Croatia            | Croatia            | 90 | Carry           |   -   | [27.7, 22.7]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +5.20 | 00:00:17.691 | Spain              | Croatia            | 90 | Pressure        |  Yes  | [90.0, 49.6]    |                           |  |
|  +5.84 | 00:00:18.332 | Croatia            | Croatia            | 90 | Pass            |   -   | [30.1, 24.9]    | -> Mateo Kovačić          |  |
|  +6.63 | 00:00:19.126 | Croatia            | Croatia            | 90 | Ball Receipt*   |   -   | [39.4, 17.5]    | Controlled Receipt        |  |
|  +6.63 | 00:00:19.126 | Croatia            | Croatia            | 90 | Carry           |   -   | [39.4, 17.5]    | Carry                     |  |
|  -2.21 | 00:00:10.285 | Croatia            | Spain              | 179 | Pressure        |  Yes  | [75.8, 43.2]    |                           |  |
|  -1.95 | 00:00:10.542 | Spain              | Spain              | 179 | Pass            |   -   | [45.3, 35.5]    | -> Jordi Alba Ram         |  |
|  -0.32 | 00:00:12.173 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [50.6, 10.2]    | Controlled Receipt        |  |
|  -0.32 | 00:00:12.173 | Spain              | Spain              | 179 | Carry           |   -   | [50.6, 10.2]    | Carry                     |  |
|  +2.40 | 00:00:14.890 | Croatia            | Spain              | 179 | Pressure        |   -   | [62.0, 70.7]    |                           |  |
|  +2.65 | 00:00:15.148 | Spain              | Spain              | 179 | Pass            |   -   | [58.9, 9.1]     | -> Daniel Olmo Ca         |  |
|  +3.72 | 00:00:16.210 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [64.7, 1.6]     | Controlled Receipt        |  |
|  +3.72 | 00:00:16.210 | Spain              | Spain              | 179 | Carry           |   -   | [64.7, 1.6]     | Carry                     |  |
|  +4.47 | 00:00:16.963 | Croatia            | Spain              | 179 | Pressure        |   -   | [55.4, 77.1]    |                           |  |
|  +4.66 | 00:00:17.149 | Spain              | Spain              | 179 | Pass            |   -   | [63.4, 3.8]     | -> Pau Francisco          |  |
|  +6.82 | 00:00:19.312 | Spain              | Spain              | 179 | Ball Receipt*   |   -   | [41.4, 3.1]     | Controlled Receipt        |  |
|  +6.82 | 00:00:19.312 | Spain              | Spain              | 179 | Carry           |   -   | [41.4, 3.1]     | Carry                     |  |
|  +7.76 | 00:00:20.248 | Spain              | Spain              | 179 | Pass            |   -   | [41.8, 3.6]     | -> Unai Simón Men         |  |
|  -2.99 | 00:00:09.502 | Spain              | Spain              | 204 | Pass            |   -   | [83.3, 24.7]    | -> Jordi Alba Ram         |  |
|  -1.64 | 00:00:10.853 | Spain              | Spain              | 204 | Ball Receipt*   |   -   | [78.3, 10.1]    | Controlled Receipt        |  |
|  -1.64 | 00:00:10.853 | Spain              | Spain              | 204 | Pass            |   -   | [78.3, 10.1]    | Incomplete (Incomplete)   |  |
|  -1.31 | 00:00:11.184 | Croatia            | Spain              | 204 | Block           |   -   | [43.8, 67.0]    |                           |  |
|  -0.66 | 00:00:11.835 | Spain              | Spain              | 204 | Pressure        |  Yes  | [74.6, 13.1]    |                           |  |
|  -0.26 | 00:00:12.234 | Croatia            | Spain              | 204 | Ball Recovery   |   -   | [46.9, 65.9]    |                           |  |
|  -0.26 | 00:00:12.234 | Croatia            | Spain              | 204 | Carry           |   -   | [46.9, 65.9]    | Carry                     |  |
|  +0.15 | 00:00:12.642 | Croatia            | Spain              | 204 | Dispossessed    |   -   | [46.9, 63.7]    | Dispossessed              |  |
|  +0.15 | 00:00:12.642 | Spain              | Spain              | 204 | Duel            |  Yes  | [73.2, 16.4]    | Tackle, Won               |  |
|  +0.15 | 00:00:12.642 | Spain              | Spain              | 204 | Carry           |   -   | [73.2, 16.4]    | Carry                     |  |
|  +1.63 | 00:00:14.126 | Croatia            | Spain              | 204 | Pressure        |   -   | [47.5, 58.2]    |                           |  |
|  +2.69 | 00:00:15.184 | Spain              | Spain              | 204 | Pass            |   -   | [71.5, 24.3]    | -> Fabián Ruiz Pe         |  |
|  +3.72 | 00:00:16.214 | Spain              | Spain              | 204 | Ball Receipt*   |   -   | [65.2, 42.6]    | Controlled Receipt        |  |
|  +3.72 | 00:00:16.214 | Spain              | Spain              | 204 | Carry           |   -   | [65.2, 42.6]    | Carry                     |  |
|  +5.72 | 00:00:18.209 | Spain              | Spain              | 204 | Pass            |   -   | [65.0, 50.7]    | -> César Azpilicu         |  |
|  +7.01 | 00:00:19.507 | Spain              | Spain              | 204 | Ball Receipt*   |   -   | [50.3, 64.0]    | Controlled Receipt        |  |
|  +7.01 | 00:00:19.507 | Spain              | Spain              | 204 | Carry           |   -   | [50.3, 64.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.42 | 00:00:19.909 | Spain              | Spain              | 204 | Pass            |   -   | [50.3, 64.0]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |

---

### Case 91: Episode `3794686_p108_580c4358`
- **Match**: `3794686` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +1.26 | 00:10:17.294 | Croatia            | Croatia            | 18 | Pass            |   -   | [75.9, 21.1]    | -> Joško Gvardiol         |  |
|  +2.82 | 00:10:18.848 | Croatia            | Croatia            | 18 | Ball Receipt*   |   -   | [99.6, 14.5]    | Controlled Receipt        |  |
|  +2.82 | 00:10:18.848 | Croatia            | Croatia            | 18 | Carry           |   -   | [99.6, 14.5]    | Carry                     |  |
|  +5.76 | 00:10:21.790 | Croatia            | Croatia            | 18 | Pass            |   -   | [111.9, 14.5]   | Incomplete (Incomplete)   |  |
|  +7.58 | 00:10:23.615 | Croatia            | Croatia            | 18 | Ball Receipt*   |   -   | [109.6, 36.9]   | Incomplete Receipt (Incomplete) |  |
|  +7.58 | 00:10:23.615 | Spain              | Croatia            | 18 | Clearance       |   -   | [9.5, 33.4]     |                           |  |
|  -2.94 | 00:10:13.096 | Spain              | Spain              | 108 | Ball Receipt*   |   -   | [84.2, 17.3]    | Controlled Receipt        |  |
|  -2.94 | 00:10:13.096 | Spain              | Spain              | 108 | Miscontrol      |   -   | [84.2, 17.3]    | Miscontrol                |  |
|  -1.49 | 00:10:14.541 | Croatia            | Spain              | 108 | Ball Recovery   |   -   | [42.1, 60.9]    |                           |  |
|  -1.49 | 00:10:14.541 | Croatia            | Spain              | 108 | Carry           |   -   | [42.1, 60.9]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:10:16.032 | Spain              | Spain              | 108 | Pressure        |  Yes  | [69.3, 18.1]    |                           | **CP INITIATION** |
|  +3.62 | 00:10:19.647 | Croatia            | Spain              | 108 | Dispossessed    |   -   | [56.2, 75.3]    | Dispossessed              |  |
|  +3.62 | 00:10:19.647 | Spain              | Spain              | 108 | Duel            |   -   | [63.9, 4.8]     | Tackle, Success Out       | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |

---

### Case 92: Episode `3794686_p11_e71ad0b9`
- **Match**: `3794686` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Croatia** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Interception`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `interception_plus_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.00 | 00:05:31.325 | Spain              | Spain              | 11 | Pressure        |  Yes  | [77.5, 55.6]    |                           | **CP INITIATION** |
|  +2.16 | 00:05:33.484 | Croatia            | Spain              | 11 | Pass            |   -   | [49.5, 7.9]     | Incomplete (Out)          |  |
|  +2.60 | 00:05:33.920 | Spain              | Spain              | 11 | Interception    |   -   | [56.5, 75.1]    | Lost Out                  | (v2.6 Regain Event) |
|  -2.09 | 00:05:29.238 | Spain              | Spain              | 100 | Pass            |   -   | [69.8, 72.7]    | -> Pablo Sarabia          |  |
|  -1.22 | 00:05:30.100 | Spain              | Spain              | 100 | Ball Receipt*   |   -   | [73.7, 78.8]    | Controlled Receipt        |  |
|  -1.22 | 00:05:30.100 | Spain              | Spain              | 100 | Carry           |   -   | [73.7, 78.8]    | Carry                     |  |
|  -0.89 | 00:05:30.437 | Croatia            | Spain              | 100 | Pressure        |   -   | [47.7, 3.1]     |                           |  |
|  -0.62 | 00:05:30.700 | Spain              | Spain              | 100 | Pass            |   -   | [70.6, 77.0]    | -> Jorge Resurrec         |  |
|  +0.08 | 00:05:31.408 | Croatia            | Spain              | 100 | Pressure        |   -   | [58.9, 3.5]     |                           |  |
|  +0.15 | 00:05:31.479 | Spain              | Spain              | 100 | Ball Receipt*   |   -   | [64.7, 77.3]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.15 | 00:05:31.479 | Spain              | Spain              | 100 | Carry           |   -   | [64.7, 77.3]    | Carry                     |  |
|  +1.57 | 00:05:32.894 | Croatia            | Spain              | 100 | Pressure        |   -   | [57.8, 3.5]     |                           |  |
|  +1.79 | 00:05:33.112 | Spain              | Spain              | 100 | Pass            |   -   | [64.5, 78.1]    | Incomplete (Unknown)      |  |
|  +2.39 | 00:05:33.719 | Croatia            | Spain              | 100 | Pressure        |   -   | [52.1, 3.5]     |                           |  |
|  +2.96 | 00:05:34.282 | Croatia            | Spain              | 100 | Foul Committed  |   -   | [49.0, 4.4]     |                           |  |
|  +2.96 | 00:05:34.282 | Spain              | Spain              | 100 | Foul Won        |   -   | [71.1, 75.7]    |                           |  |
|  -1.74 | 00:05:29.587 | Spain              | Spain              | 188 | Pass            |   -   | [8.9, 43.8]     | -> Pau Francisco          |  |
|  -0.34 | 00:05:30.983 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [12.5, 27.4]    | Controlled Receipt        |  |
|  -0.34 | 00:05:30.983 | Spain              | Spain              | 188 | Carry           |   -   | [12.5, 27.4]    | Carry                     |  |
|  +4.32 | 00:05:35.645 | Spain              | Spain              | 188 | Pass            |   -   | [30.0, 16.7]    | -> Aymeric Laport         |  |
|  +6.33 | 00:05:37.654 | Spain              | Spain              | 188 | Ball Receipt*   |   -   | [25.1, 44.9]    | Controlled Receipt        |  |
|  +6.33 | 00:05:37.654 | Spain              | Spain              | 188 | Carry           |   -   | [25.1, 44.9]    | Carry                     |  |
|  +7.37 | 00:05:38.695 | Spain              | Spain              | 188 | Pass            |   -   | [25.1, 45.3]    | -> Fabián Ruiz Pe         |  |
|  +0.28 | 00:05:31.604 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [8.2, 8.8]      | Controlled Receipt        |  |
|  +0.28 | 00:05:31.604 | Spain              | Spain              | 215 | Carry           |   -   | [8.2, 8.8]      | Carry                     |  |
|  +1.58 | 00:05:32.905 | Spain              | Spain              | 215 | Pass            |   -   | [5.6, 7.2]      | -> Pau Francisco          |  |
|  +3.14 | 00:05:34.467 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [5.6, 15.5]     | Controlled Receipt        |  |
|  +3.14 | 00:05:34.467 | Spain              | Spain              | 215 | Pass            |   -   | [5.6, 15.5]     | -> Rodrigo Hernán         |  |
|  +4.31 | 00:05:35.637 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [17.6, 8.5]     | Controlled Receipt        |  |
|  +4.31 | 00:05:35.637 | Spain              | Spain              | 215 | Pass            |   -   | [17.6, 8.5]     | Incomplete (Incomplete)   |  |
|  +6.10 | 00:05:37.425 | Croatia            | Spain              | 215 | Interception    |   -   | [86.1, 68.5]    | Won                       |  |
|  +6.10 | 00:05:37.425 | Croatia            | Spain              | 215 | Carry           |   -   | [86.1, 68.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.60 | 00:05:38.925 | Croatia            | Spain              | 215 | Dispossessed    |   -   | [95.5, 56.9]    | Dispossessed              | **POSSIBLE TRANSITION** |
|  +7.60 | 00:05:38.925 | Spain              | Spain              | 215 | Duel            |  Yes  | [24.6, 23.2]    | Tackle, Won               |  |
|  +7.60 | 00:05:38.925 | Spain              | Spain              | 215 | Carry           |   -   | [24.6, 23.2]    | Carry                     |  |

---

### Case 93: Episode `3788764_p145_bae5b2c5`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.01 | 00:39:47.153 | Germany            | Portugal           | 72 | Ball Recovery   |   -   | [98.2, 54.2]    |                           |  |
|  +0.01 | 00:39:47.153 | Germany            | Portugal           | 72 | Carry           |   -   | [98.2, 54.2]    | Carry                     |  |
|  +1.66 | 00:39:48.803 | Portugal           | Portugal           | 72 | Pressure        |  Yes  | [16.2, 27.2]    |                           |  |
|  +2.65 | 00:39:49.799 | Germany            | Portugal           | 72 | Shot            |   -   | [110.2, 52.8]   | Blocked                   |  |
|  +2.78 | 00:39:49.927 | Portugal           | Portugal           | 72 | Block           |  Yes  | [7.8, 29.3]     |                           |  |
|  +2.82 | 00:39:49.967 | Portugal           | Portugal           | 72 | Goal Keeper     |   -   | [0.5, 38.2]     |                           |  |
|  -2.30 | 00:39:44.848 | Germany            | Germany            | 144 | Ball Receipt*   |   -   | [43.3, 25.3]    | Controlled Receipt        |  |
|  -2.30 | 00:39:44.848 | Germany            | Germany            | 144 | Carry           |   -   | [43.3, 25.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.78 | 00:39:45.366 | Portugal           | Germany            | 144 | Pressure        |   -   | [71.2, 57.3]    |                           |  |
|  -0.98 | 00:39:46.162 | Portugal           | Germany            | 144 | Pressure        |   -   | [69.0, 60.0]    |                           |  |
|  +0.00 | 00:39:47.146 | Germany            | Germany            | 144 | Dispossessed    |   -   | [55.0, 18.7]    | Dispossessed              |  |
|  +0.00 | 00:39:47.146 | Portugal           | Portugal           | 145 | Duel            |  Yes  | [65.1, 61.4]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.14 | 00:39:48.289 | Portugal           | Portugal           | 145 | Ball Recovery   |   -   | [54.7, 66.9]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.14 | 00:39:48.289 | Portugal           | Portugal           | 145 | Carry           |   -   | [54.7, 66.9]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.70 | 00:39:49.846 | Germany            | Portugal           | 145 | Pressure        |  Yes  | [54.4, 6.3]     |                           |  |
|  +3.27 | 00:39:50.419 | Portugal           | Portugal           | 145 | Pass            |   -   | [67.0, 73.0]    | Incomplete (Incomplete)   |  |
|  +3.58 | 00:39:50.723 | Portugal           | Portugal           | 145 | Ball Receipt*   |   -   | [69.0, 67.2]    | Incomplete Receipt (Incomplete) |  |
|  +3.58 | 00:39:50.723 | Germany            | Portugal           | 145 | Block           |  Yes  | [51.1, 9.0]     |                           |  |

---

### Case 94: Episode `3930175_p80_ef2f30eb`
- **Match**: `3930175` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Romania** vs Actual Opponent: **Belgium** (StatsBomb Poss Team: `Romania`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.83 | 00:43:26.644 | Belgium            | Belgium            | 79 | Ball Receipt*   |   -   | [48.4, 17.5]    | Incomplete Receipt (Incomplete) |  |
|  -1.83 | 00:43:26.644 | Romania            | Belgium            | 79 | Pass            |   -   | [64.3, 60.5]    | Incomplete (Incomplete)   |  |
|  -0.92 | 00:43:27.555 | Romania            | Belgium            | 79 | Ball Receipt*   |   -   | [47.3, 51.3]    | Incomplete Receipt (Incomplete) |  |
|  -0.92 | 00:43:27.555 | Belgium            | Belgium            | 79 | Ball Recovery   |   -   | [70.6, 26.3]    |                           |  |
|  -0.92 | 00:43:27.555 | Belgium            | Belgium            | 79 | Carry           |   -   | [70.6, 26.3]    | Carry                     |  |
|  -0.56 | 00:43:27.918 | Romania            | Belgium            | 79 | Pressure        |   -   | [45.2, 52.3]    |                           |  |
|  +0.00 | 00:43:28.474 | Belgium            | Belgium            | 79 | Dispossessed    |   -   | [71.2, 26.5]    | Dispossessed              |  |
|  +0.00 | 00:43:28.474 | Romania            | Romania            | 80 | Duel            |  Yes  | [48.9, 53.6]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.36 | 00:43:28.832 | Romania            | Romania            | 80 | Ball Recovery   |   -   | [49.5, 63.1]    |                           | (v2.6 Regain Event) |
|  +1.23 | 00:43:29.704 | Belgium            | Romania            | 80 | Pressure        |  Yes  | [73.0, 20.1]    |                           |  |
|  +1.67 | 00:43:30.144 | Romania            | Romania            | 80 | Ball Recovery   |   -   | [49.7, 59.1]    |                           | **POSSIBLE TRANSITION** |
|  +1.67 | 00:43:30.144 | Romania            | Romania            | 80 | Carry           |   -   | [49.7, 59.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.00 | 00:43:31.476 | Belgium            | Romania            | 80 | Foul Committed  |  Yes  | [70.3, 20.1]    |                           |  |
|  +3.00 | 00:43:31.476 | Romania            | Romania            | 80 | Foul Won        |   -   | [49.8, 60.0]    |                           |  |
|  +2.34 | 00:43:30.815 | Belgium            | Romania            | 165 | Shot            |   -   | [114.2, 51.8]   | Saved                     | **OPPONENT LAST CONTROL** |
|  +2.55 | 00:43:31.029 | Romania            | Romania            | 165 | Goal Keeper     |   -   | [1.7, 35.6]     |                           |  |

---

### Case 95: Episode `3788764_p64_80b35733`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_pass`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.63 | 00:32:29.113 | Portugal           | Germany            | 64 | Pressure        |   -   | [37.2, 58.7]    |                           |  |
|  -0.71 | 00:32:31.035 | Germany            | Germany            | 64 | Dispossessed    |   -   | [77.1, 20.6]    | Dispossessed              |  |
|  -0.71 | 00:32:31.035 | Portugal           | Germany            | 64 | Duel            |   -   | [43.0, 59.5]    | Tackle, Won               |  |
|  -0.71 | 00:32:31.035 | Portugal           | Germany            | 64 | Carry           |   -   | [43.0, 59.5]    | Carry                     |  |
|  +0.00 | 00:32:31.742 | Germany            | Germany            | 64 | Pressure        |  Yes  | [75.5, 20.2]    |                           | **CP INITIATION** |
|  +0.32 | 00:32:32.060 | Portugal           | Germany            | 64 | Dispossessed    |   -   | [45.6, 63.7]    | Dispossessed              |  |
|  +0.32 | 00:32:32.060 | Germany            | Germany            | 64 | Duel            |  Yes  | [74.5, 16.4]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +1.94 | 00:32:33.682 | Germany            | Germany            | 64 | Pass            |   -   | [63.8, 16.8]    | -> Robin Gosens           | **PRESSING-TEAM FIRST CONTROL** |
|  +3.49 | 00:32:35.232 | Germany            | Germany            | 64 | Ball Receipt*   |   -   | [78.5, 2.4]     | Controlled Receipt        |  |
|  +3.49 | 00:32:35.232 | Germany            | Germany            | 64 | Carry           |   -   | [78.5, 2.4]     | Carry                     |  |
|  +4.21 | 00:32:35.956 | Portugal           | Germany            | 64 | Pressure        |   -   | [36.6, 78.7]    |                           |  |
|  +4.77 | 00:32:36.515 | Germany            | Germany            | 64 | Pass            |   -   | [76.5, 2.8]     | -> Toni Kroos             |  |
|  +5.67 | 00:32:37.415 | Germany            | Germany            | 64 | Ball Receipt*   |   -   | [68.8, 10.5]    | Controlled Receipt        |  |
|  +5.67 | 00:32:37.415 | Germany            | Germany            | 64 | Carry           |   -   | [68.8, 10.5]    | Carry                     |  |
|  -2.90 | 00:32:28.839 | Portugal           | Portugal           | 133 | Ball Receipt*   |   -   | [63.0, 52.4]    | Controlled Receipt        |  |
|  -2.90 | 00:32:28.839 | Portugal           | Portugal           | 133 | Carry           |   -   | [63.0, 52.4]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -1.41 | 00:32:30.330 | Portugal           | Portugal           | 133 | Pass            |   -   | [69.3, 54.3]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +0.66 | 00:32:32.400 | Portugal           | Portugal           | 133 | Ball Receipt*   |   -   | [106.8, 35.5]   | Incomplete Receipt (Incomplete) |  |
|  +0.66 | 00:32:32.400 | Germany            | Portugal           | 133 | Clearance       |   -   | [12.8, 46.7]    |                           |  |
|  +2.92 | 00:32:34.665 | Portugal           | Portugal           | 133 | Pressure        |   -   | [91.1, 19.2]    |                           |  |
|  +3.02 | 00:32:34.763 | Germany            | Portugal           | 133 | Ball Recovery   |   -   | [28.0, 64.1]    |                           |  |
|  +3.02 | 00:32:34.763 | Germany            | Portugal           | 133 | Carry           |   -   | [28.0, 64.1]    | Carry                     |  |

---

### Case 96: Episode `3788764_p10_6fc4e214`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.78 | 00:05:56.582 | Germany            | Portugal           | 9 | Pressure        |   -   | [79.6, 73.0]    |                           |  |
|  -2.70 | 00:05:56.666 | Portugal           | Portugal           | 9 | Ball Receipt*   |   -   | [44.3, 3.3]     | Controlled Receipt        |  |
|  -2.70 | 00:05:56.666 | Portugal           | Portugal           | 9 | Carry           |   -   | [44.3, 3.3]     | Carry                     |  |
|  -2.32 | 00:05:57.043 | Portugal           | Portugal           | 9 | Pass            |   -   | [49.0, 4.5]     | -> Cristiano Rona         |  |
|  -1.37 | 00:05:57.997 | Portugal           | Portugal           | 9 | Ball Receipt*   |   -   | [56.4, 14.7]    | Controlled Receipt        |  |
|  -1.37 | 00:05:57.997 | Portugal           | Portugal           | 9 | Carry           |   -   | [56.4, 14.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.62 | 00:05:58.738 | Germany            | Portugal           | 9 | Pressure        |   -   | [68.8, 70.7]    |                           |  |
|  +0.00 | 00:05:59.362 | Portugal           | Portugal           | 9 | Dispossessed    |   -   | [51.0, 12.9]    | Dispossessed              |  |
|  +0.00 | 00:05:59.362 | Germany            | Germany            | 10 | Duel            |  Yes  | [69.1, 67.2]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.03 | 00:06:00.393 | Germany            | Germany            | 10 | Ball Recovery   |   -   | [69.9, 62.6]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.03 | 00:06:00.393 | Germany            | Germany            | 10 | Carry           |   -   | [69.9, 62.6]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +1.68 | 00:06:01.046 | Germany            | Germany            | 10 | Pass            |   -   | [68.2, 57.3]    | -> Toni Kroos             |  |
|  +2.96 | 00:06:02.319 | Portugal           | Germany            | 10 | Pressure        |  Yes  | [56.8, 34.0]    |                           |  |
|  +2.97 | 00:06:02.330 | Germany            | Germany            | 10 | Ball Receipt*   |   -   | [56.6, 50.7]    | Controlled Receipt        |  |
|  +2.97 | 00:06:02.330 | Germany            | Germany            | 10 | Carry           |   -   | [56.6, 50.7]    | Carry                     |  |
|  +4.00 | 00:06:03.362 | Germany            | Germany            | 10 | Pass            |   -   | [58.0, 52.2]    | Incomplete (Incomplete)   |  |
|  +6.76 | 00:06:06.124 | Germany            | Germany            | 10 | Ball Receipt*   |   -   | [105.7, 58.2]   | Incomplete Receipt (Incomplete) |  |
|  +6.76 | 00:06:06.124 | Portugal           | Germany            | 10 | Clearance       |   -   | [13.5, 23.2]    |                           |  |

---

### Case 97: Episode `3788764_p15_b43631aa`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Interception`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `interception_plus_control`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.87 | 00:09:08.393 | Portugal           | Germany            | 15 | Pressure        |   -   | [5.2, 25.3]     |                           |  |
|  -2.35 | 00:09:08.913 | Germany            | Germany            | 15 | Pass            |   -   | [118.0, 54.8]   | Incomplete (Incomplete)   |  |
|  -1.50 | 00:09:09.764 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [114.7, 47.2]   | Incomplete Receipt (Incomplete) |  |
|  -1.50 | 00:09:09.764 | Portugal           | Germany            | 15 | Ball Recovery   |   -   | [9.8, 35.5]     |                           |  |
|  -1.50 | 00:09:09.764 | Portugal           | Germany            | 15 | Carry           |   -   | [9.8, 35.5]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:09:11.267 | Germany            | Germany            | 15 | Pressure        |  Yes  | [103.9, 47.7]   |                           | **CP INITIATION** |
|  +0.17 | 00:09:11.442 | Portugal           | Germany            | 15 | Pass            |   -   | [13.7, 31.8]    | Incomplete (Incomplete)   |  |
|  +1.25 | 00:09:12.521 | Germany            | Germany            | 15 | Interception    |  Yes  | [99.0, 59.1]    | Won                       | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.25 | 00:09:12.521 | Germany            | Germany            | 15 | Carry           |   -   | [99.0, 59.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.86 | 00:09:14.131 | Germany            | Germany            | 15 | Pass            |   -   | [92.2, 58.5]    | -> İlkay Gündoğan         |  |
|  +3.85 | 00:09:15.119 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [86.6, 46.1]    | Controlled Receipt        |  |
|  +3.85 | 00:09:15.119 | Germany            | Germany            | 15 | Carry           |   -   | [86.6, 46.1]    | Carry                     |  |
|  +7.01 | 00:09:18.281 | Germany            | Germany            | 15 | Pass            |   -   | [79.2, 35.9]    | -> Toni Kroos             |  |
|  +7.71 | 00:09:18.978 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [89.1, 49.3]    | Controlled Receipt        |  |
|  +7.71 | 00:09:18.978 | Germany            | Germany            | 15 | Carry           |   -   | [89.1, 49.3]    | Carry                     |  |
|  -2.47 | 00:09:08.793 | Germany            | Germany            | 98 | Pass            |   -   | [70.6, 72.0]    | -> Toni Kroos             |  |
|  -0.92 | 00:09:10.344 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [68.1, 39.3]    | Controlled Receipt        |  |
|  -0.92 | 00:09:10.344 | Germany            | Germany            | 98 | Carry           |   -   | [68.1, 39.3]    | Carry                     |  |
|  +0.53 | 00:09:11.800 | Germany            | Germany            | 98 | Pass            |   -   | [71.0, 35.2]    | -> İlkay Gündoğan         |  |
|  +1.41 | 00:09:12.679 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [73.7, 51.5]    | Controlled Receipt        |  |
|  +1.41 | 00:09:12.679 | Germany            | Germany            | 98 | Carry           |   -   | [73.7, 51.5]    | Carry                     |  |
|  +1.49 | 00:09:12.759 | Germany            | Germany            | 98 | Pass            |   -   | [73.5, 50.9]    | -> Antonio Rüdige         |  |
|  +3.28 | 00:09:14.550 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [70.3, 17.6]    | Controlled Receipt        |  |
|  +3.28 | 00:09:14.550 | Germany            | Germany            | 98 | Carry           |   -   | [70.3, 17.6]    | Carry                     |  |
|  +4.56 | 00:09:15.824 | Germany            | Germany            | 98 | Pass            |   -   | [70.3, 17.4]    | -> Robin Gosens           |  |
|  +5.18 | 00:09:16.445 | Portugal           | Germany            | 98 | Pressure        |   -   | [39.2, 73.0]    |                           |  |
|  +5.65 | 00:09:16.914 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [79.7, 6.6]     | Controlled Receipt        |  |
|  +5.65 | 00:09:16.914 | Germany            | Germany            | 98 | Pass            |   -   | [79.2, 6.3]     | Incomplete (Out)          |  |
|  +6.38 | 00:09:17.644 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [67.3, 5.7]     | Incomplete Receipt (Incomplete) |  |

---

### Case 98: Episode `3788764_p15_ae5ce844`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Goal Keeper`
- **Automated Pathway Classification**: `opponent_shot` | v2.6 Evidence: `goalkeeper_control`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.19 | 00:08:59.033 | Portugal           | Portugal           | 14 | Pass            |   -   | [15.1, 0.1]     | Incomplete (Incomplete)   |  |
|  -0.06 | 00:09:01.163 | Germany            | Germany            | 15 | Ball Recovery   |   -   | [93.1, 56.7]    |                           |  |
|  +0.00 | 00:09:01.222 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [26.8, 19.9]    |                           | **CP INITIATION** |
|  +0.68 | 00:09:01.904 | Germany            | Germany            | 15 | Pass            |   -   | [92.2, 51.2]    | -> Kai Havertz            |  |
|  +1.40 | 00:09:02.625 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [90.7, 41.2]    | Controlled Receipt        |  |
|  +1.40 | 00:09:02.625 | Germany            | Germany            | 15 | Carry           |   -   | [90.7, 41.2]    | Carry                     |  |
|  +1.92 | 00:09:03.145 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [20.2, 39.5]    |                           |  |
|  +2.40 | 00:09:03.625 | Germany            | Germany            | 15 | Shot            |   -   | [95.5, 40.3]    | Saved                     |  |
|  +3.07 | 00:09:04.295 | Portugal           | Germany            | 15 | Goal Keeper     |   -   | [1.1, 40.4]     |                           | (v2.6 Regain Event) |
|  +4.42 | 00:09:05.645 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [3.4, 34.2]     |                           |  |
|  +5.19 | 00:09:06.415 | Germany            | Germany            | 15 | Ball Recovery   |   -   | [116.5, 48.9]   |                           |  |
|  +5.19 | 00:09:06.415 | Germany            | Germany            | 15 | Carry           |   -   | [116.5, 48.9]   | Carry                     |  |
|  +7.17 | 00:09:08.393 | Portugal           | Germany            | 15 | Pressure        |   -   | [5.2, 25.3]     |                           |  |
|  +7.69 | 00:09:08.913 | Germany            | Germany            | 15 | Pass            |   -   | [118.0, 54.8]   | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  +1.12 | 00:09:02.347 | Germany            | Germany            | 98 | Pass            |   -   | [95.7, 69.6]    | -> Joshua Kimmich         |  |
|  +2.57 | 00:09:03.794 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [84.1, 73.5]    | Controlled Receipt        |  |
|  +2.57 | 00:09:03.794 | Germany            | Germany            | 98 | Carry           |   -   | [84.1, 73.5]    | Carry                     |  |
|  +4.09 | 00:09:05.312 | Germany            | Germany            | 98 | Pass            |   -   | [91.3, 70.5]    | -> Thomas Müller          |  |
|  +4.21 | 00:09:05.432 | Portugal           | Germany            | 98 | Pressure        |   -   | [29.1, 4.2]     |                           |  |
|  +5.16 | 00:09:06.385 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [91.5, 75.4]    | Controlled Receipt        |  |
|  +5.16 | 00:09:06.385 | Germany            | Germany            | 98 | Carry           |   -   | [91.5, 75.4]    | Carry                     |  |
|  +5.20 | 00:09:06.425 | Germany            | Germany            | 98 | Pass            |   -   | [90.5, 75.2]    | -> Matthias Ginte         |  |
|  +6.51 | 00:09:07.728 | Germany            | Germany            | 98 | Ball Receipt*   |   -   | [69.3, 72.7]    | Controlled Receipt        |  |
|  +6.51 | 00:09:07.728 | Germany            | Germany            | 98 | Carry           |   -   | [69.3, 72.7]    | Carry                     |  |
|  +7.57 | 00:09:08.793 | Germany            | Germany            | 98 | Pass            |   -   | [70.6, 72.0]    | -> Toni Kroos             | **OPPONENT LAST CONTROL** |

---

### Case 99: Episode `3788764_p38_d7a37961`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `opponent_incomplete_pass` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.81 | 00:16:22.679 | Germany            | Germany            | 38 | Pass            |   -   | [95.5, 9.9]     | Incomplete (Incomplete)   |  |
|  -2.76 | 00:16:22.735 | Germany            | Germany            | 38 | Ball Receipt*   |   -   | [93.1, 22.9]    | Incomplete Receipt (Incomplete) |  |
|  -2.76 | 00:16:22.735 | Portugal           | Germany            | 38 | Interception    |   -   | [24.1, 64.9]    | Success In Play           |  |
|  -2.18 | 00:16:23.311 | Portugal           | Germany            | 38 | Ball Recovery   |   -   | [30.1, 60.1]    |                           |  |
|  -2.18 | 00:16:23.311 | Portugal           | Germany            | 38 | Carry           |   -   | [30.1, 60.1]    | Carry                     |  |
|  -1.10 | 00:16:24.396 | Portugal           | Germany            | 38 | Pass            |   -   | [27.2, 64.2]    | -> Bruno Miguel B         |  |
|  -0.10 | 00:16:25.395 | Portugal           | Germany            | 38 | Ball Receipt*   |   -   | [34.1, 66.0]    | Controlled Receipt        |  |
|  -0.10 | 00:16:25.395 | Portugal           | Germany            | 38 | Carry           |   -   | [34.1, 66.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:16:25.491 | Germany            | Germany            | 38 | Pressure        |  Yes  | [82.3, 14.1]    |                           | **CP INITIATION** |
|  +0.18 | 00:16:25.669 | Portugal           | Germany            | 38 | Pass            |   -   | [29.2, 65.8]    | Incomplete (Incomplete)   |  |
|  +0.37 | 00:16:25.858 | Portugal           | Germany            | 38 | Ball Receipt*   |   -   | [37.8, 77.1]    | Incomplete Receipt (Incomplete) |  |
|  +0.37 | 00:16:25.858 | Germany            | Germany            | 38 | Block           |  Yes  | [87.6, 12.3]    |                           |  |
|  +1.88 | 00:16:27.372 | Germany            | Germany            | 38 | Ball Recovery   |   -   | [99.2, 5.0]     |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.88 | 00:16:27.372 | Germany            | Germany            | 38 | Carry           |   -   | [99.2, 5.0]     | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.35 | 00:16:28.844 | Germany            | Germany            | 38 | Pass            |   -   | [104.3, 11.8]   | Incomplete (Out)          |  |
|  +5.81 | 00:16:31.301 | Germany            | Germany            | 38 | Ball Receipt*   |   -   | [115.6, 19.8]   | Incomplete Receipt (Incomplete) |  |

---

### Case 100: Episode `3788764_p40_2797ac23`
- **Match**: `3788764` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.67 | 00:16:52.548 | Germany            | Portugal           | 39 | Pressure        |   -   | [65.5, 75.2]    |                           |  |
|  -2.54 | 00:16:52.676 | Portugal           | Portugal           | 39 | Ball Receipt*   |   -   | [51.0, 4.7]     | Controlled Receipt        |  |
|  -2.54 | 00:16:52.676 | Portugal           | Portugal           | 39 | Carry           |   -   | [51.0, 4.7]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:16:55.220 | Portugal           | Portugal           | 39 | Dribble         |   -   | [50.8, 3.1]     | Incomplete                |  |
|  +0.00 | 00:16:55.220 | Germany            | Germany            | 40 | Duel            |  Yes  | [69.3, 77.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.27 | 00:16:56.491 | Germany            | Germany            | 40 | Ball Recovery   |   -   | [70.8, 73.6]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.27 | 00:16:56.491 | Germany            | Germany            | 40 | Carry           |   -   | [70.8, 73.6]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +1.42 | 00:16:56.638 | Germany            | Germany            | 40 | Dispossessed    |   -   | [68.0, 73.9]    | Dispossessed              |  |
|  +1.42 | 00:16:56.638 | Portugal           | Germany            | 40 | Duel            |  Yes  | [52.1, 6.2]     | Tackle, Lost In Play      |  |
|  +2.55 | 00:16:57.768 | Germany            | Germany            | 40 | Ball Recovery   |   -   | [71.9, 69.1]    |                           |  |
|  +2.55 | 00:16:57.768 | Germany            | Germany            | 40 | Carry           |   -   | [71.9, 69.1]    | Carry                     |  |
|  +2.81 | 00:16:58.034 | Germany            | Germany            | 40 | Pass            |   -   | [69.3, 68.8]    | -> Mats Hummels           |  |
|  +4.13 | 00:16:59.348 | Germany            | Germany            | 40 | Ball Receipt*   |   -   | [57.6, 66.8]    | Controlled Receipt        |  |
|  +4.13 | 00:16:59.348 | Germany            | Germany            | 40 | Carry           |   -   | [57.6, 66.8]    | Carry                     |  |
|  +5.86 | 00:17:01.078 | Germany            | Germany            | 40 | Pass            |   -   | [58.5, 56.5]    | -> Toni Kroos             |  |
|  +6.99 | 00:17:02.208 | Germany            | Germany            | 40 | Ball Receipt*   |   -   | [58.9, 45.9]    | Controlled Receipt        |  |
|  +6.99 | 00:17:02.208 | Germany            | Germany            | 40 | Carry           |   -   | [58.9, 45.9]    | Carry                     |  |

---

### Case 101: Episode `3788764_p87_0cbe27b7`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `other` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.49 | 00:01:39.225 | Germany            | Germany            | 5 | Ball Recovery   |   -   | [1.4, 20.0]     |                           |  |
|  -2.49 | 00:01:39.225 | Germany            | Germany            | 5 | Carry           |   -   | [1.4, 20.0]     | Carry                     |  |
|  +2.33 | 00:01:44.051 | Germany            | Germany            | 5 | Pass            |   -   | [14.5, 26.9]    | -> Matthias Ginte         |  |
|  +4.64 | 00:01:46.361 | Germany            | Germany            | 5 | Ball Receipt*   |   -   | [15.7, 62.4]    | Controlled Receipt        |  |
|  +4.64 | 00:01:46.361 | Germany            | Germany            | 5 | Carry           |   -   | [15.7, 62.4]    | Carry                     |  |
|  -1.82 | 00:01:39.900 | Germany            | Portugal           | 87 | Pressure        |   -   | [59.7, 6.1]     |                           |  |
|  -1.05 | 00:01:40.665 | Portugal           | Portugal           | 87 | Pass            |   -   | [70.4, 70.5]    | Incomplete (Incomplete)   |  |
|  -0.16 | 00:01:41.562 | Portugal           | Portugal           | 87 | Ball Receipt*   |   -   | [78.9, 64.7]    | Incomplete Receipt (Incomplete) |  |
|  -0.16 | 00:01:41.562 | Germany            | Portugal           | 87 | Interception    |   -   | [40.6, 15.1]    | Lost In Play              |  |
|  +0.00 | 00:01:41.718 | Portugal           | Portugal           | 87 | Block           |  Yes  | [78.9, 64.2]    |                           | **CP INITIATION** |
|  +0.02 | 00:01:41.741 | Germany            | Portugal           | 87 | Block           |   -   | [40.3, 15.1]    |                           |  |
|  +1.10 | 00:01:42.820 | Germany            | Portugal           | 87 | Pressure        |   -   | [38.4, 4.6]     |                           |  |
|  +1.15 | 00:01:42.866 | Portugal           | Portugal           | 87 | Ball Recovery   |   -   | [81.7, 75.5]    |                           | (v2.6 Regain Event) |
|  +1.15 | 00:01:42.866 | Portugal           | Portugal           | 87 | Carry           |   -   | [81.7, 75.5]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.02 | 00:01:43.742 | Germany            | Portugal           | 87 | Dribbled Past   |   -   | [25.5, 12.3]    |                           |  |
|  +2.02 | 00:01:43.742 | Portugal           | Portugal           | 87 | Dribble         |   -   | [94.6, 67.8]    | Incomplete                |  |
|  +2.89 | 00:01:44.612 | Portugal           | Portugal           | 87 | Pressure        |  Yes  | [94.6, 67.8]    |                           |  |
|  +4.38 | 00:01:46.099 | Germany            | Portugal           | 87 | Ball Recovery   |   -   | [10.3, 12.5]    |                           |  |
|  +4.38 | 00:01:46.099 | Germany            | Portugal           | 87 | Carry           |   -   | [10.3, 12.5]    | Carry                     |  |
|  +5.48 | 00:01:47.197 | Germany            | Portugal           | 87 | Pass            |   -   | [7.3, 9.8]      | -> Antonio Rüdige         |  |
|  +6.55 | 00:01:48.263 | Germany            | Portugal           | 87 | Ball Receipt*   |   -   | [15.8, 3.3]     | Controlled Receipt        |  |
|  +6.55 | 00:01:48.263 | Germany            | Portugal           | 87 | Carry           |   -   | [15.8, 3.3]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +7.11 | 00:01:48.829 | Germany            | Portugal           | 87 | Dribble         |   -   | [15.5, 3.8]     | Incomplete                | **POSSIBLE TRANSITION** |
|  +7.11 | 00:01:48.829 | Portugal           | Portugal           | 87 | Duel            |  Yes  | [104.6, 76.3]   | Tackle, Won               |  |
|  +7.11 | 00:01:48.829 | Portugal           | Portugal           | 87 | Carry           |   -   | [104.6, 76.3]   | Carry                     |  |

---

### Case 102: Episode `3788764_p93_441025ef`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Actual Opponent: **Germany** (StatsBomb Poss Team: `Portugal`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.13 | 00:03:45.405 | Germany            | Germany            | 8 | Pass            |   -   | [67.3, 18.7]    | -> Robin Gosens           |  |
|  -0.37 | 00:03:47.169 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [82.9, 1.8]     | Controlled Receipt        |  |
|  -0.37 | 00:03:47.169 | Germany            | Germany            | 8 | Carry           |   -   | [82.9, 1.8]     | Carry                     |  |
|  +0.23 | 00:03:47.765 | Germany            | Germany            | 8 | Pass            |   -   | [82.9, 1.5]     | -> İlkay Gündoğan         |  |
|  +0.92 | 00:03:48.462 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [85.4, 10.3]    | Controlled Receipt        |  |
|  +0.92 | 00:03:48.462 | Germany            | Germany            | 8 | Carry           |   -   | [85.4, 10.3]    | Carry                     |  |
|  +1.00 | 00:03:48.542 | Germany            | Germany            | 8 | Pass            |   -   | [85.0, 10.4]    | -> Robin Gosens           |  |
|  +1.58 | 00:03:49.121 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [78.3, 2.4]     | Controlled Receipt        |  |
|  +1.58 | 00:03:49.121 | Germany            | Germany            | 8 | Carry           |   -   | [78.3, 2.4]     | Carry                     |  |
|  +1.66 | 00:03:49.201 | Germany            | Germany            | 8 | Pass            |   -   | [78.1, 2.4]     | -> Antonio Rüdige         |  |
|  +3.03 | 00:03:50.569 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [62.9, 5.3]     | Controlled Receipt        |  |
|  +3.03 | 00:03:50.569 | Germany            | Germany            | 8 | Carry           |   -   | [62.9, 5.3]     | Carry                     |  |
|  +3.11 | 00:03:50.649 | Germany            | Germany            | 8 | Pass            |   -   | [62.7, 6.1]     | -> Toni Kroos             |  |
|  +4.39 | 00:03:51.931 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [64.0, 14.5]    | Controlled Receipt        |  |
|  +4.39 | 00:03:51.931 | Germany            | Germany            | 8 | Carry           |   -   | [64.0, 14.5]    | Carry                     |  |
|  +6.39 | 00:03:53.926 | Germany            | Germany            | 8 | Pass            |   -   | [63.5, 21.6]    | -> Matthias Ginte         |  |
|  -2.41 | 00:03:45.131 | Germany            | Germany            | 92 | Ball Receipt*   |   -   | [71.2, 8.5]     | Controlled Receipt        |  |
|  -2.41 | 00:03:45.131 | Germany            | Germany            | 92 | Carry           |   -   | [71.2, 8.5]     | Carry                     |  |
|  -2.07 | 00:03:45.467 | Germany            | Germany            | 92 | Pass            |   -   | [71.2, 8.5]     | -> Robin Gosens           |  |
|  -0.99 | 00:03:46.548 | Germany            | Germany            | 92 | Ball Receipt*   |   -   | [85.3, 7.6]     | Controlled Receipt        |  |
|  -0.99 | 00:03:46.548 | Germany            | Germany            | 92 | Carry           |   -   | [85.3, 7.6]     | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.99 | 00:03:46.549 | Portugal           | Germany            | 92 | Pressure        |   -   | [32.6, 72.5]    |                           |  |
|  +0.00 | 00:03:47.537 | Germany            | Germany            | 92 | Dribble         |   -   | [85.8, 7.4]     | Incomplete                |  |
|  +0.00 | 00:03:47.537 | Portugal           | Portugal           | 93 | Duel            |  Yes  | [34.3, 72.7]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.43 | 00:03:47.968 | Germany            | Portugal           | 93 | Foul Committed  |  Yes  | [85.8, 7.4]     |                           |  |
|  +0.43 | 00:03:47.968 | Portugal           | Portugal           | 93 | Foul Won        |   -   | [34.3, 72.7]    |                           |  |
|  +1.34 | 00:03:48.872 | Portugal           | Portugal           | 93 | Ball Recovery   |   -   | [35.7, 73.5]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.34 | 00:03:48.872 | Portugal           | Portugal           | 93 | Carry           |   -   | [35.7, 73.5]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.13 | 00:03:49.664 | Portugal           | Portugal           | 93 | Pass            |   -   | [40.0, 68.9]    | -> Bruno Miguel B         |  |
|  +2.91 | 00:03:50.442 | Germany            | Portugal           | 93 | Pressure        |  Yes  | [70.9, 18.7]    |                           |  |
|  +2.92 | 00:03:50.456 | Portugal           | Portugal           | 93 | Ball Receipt*   |   -   | [48.3, 65.2]    | Controlled Receipt        |  |
|  +2.92 | 00:03:50.456 | Portugal           | Portugal           | 93 | Pass            |   -   | [49.5, 64.2]    | -> Renato Júnior          |  |
|  +3.49 | 00:03:51.026 | Portugal           | Portugal           | 93 | Ball Receipt*   |   -   | [41.2, 68.1]    | Controlled Receipt        |  |
|  +3.49 | 00:03:51.026 | Portugal           | Portugal           | 93 | Carry           |   -   | [41.2, 68.1]    | Carry                     |  |
|  +5.65 | 00:03:53.187 | Portugal           | Portugal           | 93 | Pass            |   -   | [42.0, 65.2]    | -> Danilo Luís Hé         |  |
|  +7.08 | 00:03:54.617 | Portugal           | Portugal           | 93 | Ball Receipt*   |   -   | [36.8, 58.1]    | Controlled Receipt        |  |
|  +7.08 | 00:03:54.617 | Portugal           | Portugal           | 93 | Carry           |   -   | [36.8, 58.1]    | Carry                     |  |
|  +7.27 | 00:03:54.811 | Portugal           | Portugal           | 93 | Pass            |   -   | [36.0, 54.3]    | -> William Silva          |  |

---

### Case 103: Episode `3788764_p94_98036583`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.03 | 00:04:02.551 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [95.8, 77.2]    | Controlled Receipt        |  |
|  -2.03 | 00:04:02.551 | Germany            | Germany            | 8 | Carry           |   -   | [95.8, 77.2]    | Carry                     |  |
|  -0.84 | 00:04:03.737 | Germany            | Germany            | 8 | Pass            |   -   | [90.4, 76.3]    | -> Matthias Ginte         |  |
|  +0.06 | 00:04:04.634 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [75.6, 73.9]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.06 | 00:04:04.634 | Germany            | Germany            | 8 | Carry           |   -   | [75.6, 73.9]    | Carry                     |  |
|  +0.88 | 00:04:05.458 | Germany            | Germany            | 8 | Pass            |   -   | [76.8, 69.0]    | -> İlkay Gündoğan         |  |
|  +1.64 | 00:04:06.218 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [77.4, 57.5]    | Controlled Receipt        |  |
|  +1.64 | 00:04:06.218 | Germany            | Germany            | 8 | Carry           |   -   | [77.4, 57.5]    | Carry                     |  |
|  +2.31 | 00:04:06.883 | Germany            | Germany            | 8 | Pass            |   -   | [77.4, 57.5]    | -> Antonio Rüdige         |  |
|  +4.18 | 00:04:08.759 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [69.0, 31.6]    | Controlled Receipt        |  |
|  +4.18 | 00:04:08.759 | Germany            | Germany            | 8 | Carry           |   -   | [69.0, 31.6]    | Carry                     |  |
|  +5.50 | 00:04:10.080 | Germany            | Germany            | 8 | Pass            |   -   | [69.0, 26.3]    | -> Toni Kroos             |  |
|  +6.50 | 00:04:11.078 | Germany            | Germany            | 8 | Ball Receipt*   |   -   | [77.6, 18.7]    | Controlled Receipt        |  |
|  +6.50 | 00:04:11.078 | Germany            | Germany            | 8 | Carry           |   -   | [77.6, 18.7]    | Carry                     |  |
|  -2.93 | 00:04:01.648 | Portugal           | Portugal           | 93 | Pass            |   -   | [49.5, 9.1]     | -> Diogo José Tei         |  |
|  -1.86 | 00:04:02.721 | Portugal           | Portugal           | 93 | Ball Receipt*   |   -   | [64.6, 4.2]     | Controlled Receipt        |  |
|  -1.86 | 00:04:02.721 | Portugal           | Portugal           | 93 | Carry           |   -   | [64.6, 4.2]     | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.73 | 00:04:03.845 | Germany            | Portugal           | 93 | Pressure        |   -   | [52.8, 74.6]    |                           |  |
|  +0.00 | 00:04:04.578 | Portugal           | Portugal           | 93 | Dispossessed    |   -   | [66.8, 3.6]     | Dispossessed              | **POSSIBLE TRANSITION** |
|  +0.00 | 00:04:04.578 | Germany            | Germany            | 94 | Duel            |  Yes  | [53.3, 76.5]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.14 | 00:04:05.722 | Portugal           | Germany            | 94 | Pressure        |  Yes  | [63.3, 4.4]     |                           |  |
|  +1.53 | 00:04:06.110 | Germany            | Germany            | 94 | Ball Recovery   |   -   | [49.9, 75.4]    |                           | (v2.6 Regain Event) |
|  +1.53 | 00:04:06.110 | Germany            | Germany            | 94 | Carry           |   -   | [49.9, 75.4]    | Carry                     |  |
|  +1.87 | 00:04:06.450 | Germany            | Germany            | 94 | Pass            |   -   | [49.7, 74.9]    | -> Joshua Kimmich         |  |
|  +2.87 | 00:04:07.446 | Germany            | Germany            | 94 | Ball Receipt*   |   -   | [54.1, 70.7]    | Controlled Receipt        |  |
|  +2.87 | 00:04:07.446 | Germany            | Germany            | 94 | Carry           |   -   | [54.1, 70.7]    | Carry                     |  |
|  +2.95 | 00:04:07.526 | Germany            | Germany            | 94 | Pass            |   -   | [55.0, 68.3]    | -> İlkay Gündoğan         |  |
|  +4.05 | 00:04:08.632 | Germany            | Germany            | 94 | Ball Receipt*   |   -   | [49.9, 71.5]    | Controlled Receipt        |  |
|  +4.05 | 00:04:08.632 | Germany            | Germany            | 94 | Pass            |   -   | [55.3, 69.6]    | -> Joshua Kimmich         |  |
|  +5.07 | 00:04:09.645 | Germany            | Germany            | 94 | Ball Receipt*   |   -   | [49.9, 72.4]    | Controlled Receipt        |  |
|  +5.07 | 00:04:09.645 | Germany            | Germany            | 94 | Carry           |   -   | [49.9, 72.4]    | Carry                     |  |

---

### Case 104: Episode `3788764_p108_b6e53920`
- **Match**: `3788764` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Germany** vs Actual Opponent: **Portugal** (StatsBomb Poss Team: `Germany`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +7.81 | 00:14:03.901 | Germany            | Germany            | 34 | Pass            |   -   | [120.0, 80.0]   | Incomplete (Incomplete)   |  |
|  -2.90 | 00:13:53.189 | Portugal           | Portugal           | 107 | Ball Receipt*   |   -   | [56.4, 55.3]    | Controlled Receipt        |  |
|  -2.90 | 00:13:53.189 | Portugal           | Portugal           | 107 | Carry           |   -   | [56.4, 55.3]    | Carry                     |  |
|  -2.04 | 00:13:54.048 | Portugal           | Portugal           | 107 | Pass            |   -   | [59.1, 56.2]    | -> Rafael Alexand         |  |
|  -1.03 | 00:13:55.057 | Portugal           | Portugal           | 107 | Ball Receipt*   |   -   | [70.9, 49.6]    | Controlled Receipt        |  |
|  -1.03 | 00:13:55.057 | Portugal           | Portugal           | 107 | Carry           |   -   | [70.9, 49.6]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.99 | 00:13:55.099 | Germany            | Portugal           | 107 | Pressure        |   -   | [49.2, 30.5]    |                           |  |
|  +0.00 | 00:13:56.086 | Portugal           | Portugal           | 107 | Dispossessed    |   -   | [71.5, 48.7]    | Dispossessed              |  |
|  +0.00 | 00:13:56.086 | Germany            | Germany            | 108 | Duel            |  Yes  | [48.6, 31.4]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.72 | 00:13:56.806 | Germany            | Germany            | 108 | Ball Recovery   |   -   | [45.5, 33.9]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +0.72 | 00:13:56.806 | Germany            | Germany            | 108 | Carry           |   -   | [45.5, 33.9]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +1.63 | 00:13:57.714 | Germany            | Germany            | 108 | Pass            |   -   | [47.7, 28.9]    | -> Thomas Müller          |  |
|  +2.56 | 00:13:58.650 | Germany            | Germany            | 108 | Ball Receipt*   |   -   | [57.5, 20.3]    | Controlled Receipt        |  |
|  +2.56 | 00:13:58.650 | Germany            | Germany            | 108 | Carry           |   -   | [57.5, 20.3]    | Carry                     |  |
|  +3.89 | 00:13:59.974 | Portugal           | Germany            | 108 | Pressure        |  Yes  | [57.7, 64.2]    |                           |  |
|  +7.60 | 00:14:03.689 | Germany            | Germany            | 108 | Pass            |   -   | [77.7, 5.8]     | -> Robin Gosens           |  |

---

### Case 105: Episode `3788762_p110_41c06bd9`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.84 | 00:19:00.050 | Spain              | Spain              | 34 | Pass            |   -   | [76.0, 67.7]    | -> Rodrigo Hernán         |  |
|  -0.71 | 00:19:01.180 | Spain              | Spain              | 34 | Ball Receipt*   |   -   | [73.9, 58.3]    | Controlled Receipt        |  |
|  -0.71 | 00:19:01.180 | Spain              | Spain              | 34 | Carry           |   -   | [73.9, 58.3]    | Carry                     |  |
|  -0.07 | 00:19:01.817 | Spain              | Spain              | 34 | Pass            |   -   | [73.9, 58.3]    | -> Pau Francisco          |  |
|  +1.60 | 00:19:03.487 | Spain              | Spain              | 34 | Ball Receipt*   |   -   | [67.0, 36.1]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +1.60 | 00:19:03.487 | Spain              | Spain              | 34 | Carry           |   -   | [67.0, 36.1]    | Carry                     |  |
|  +2.45 | 00:19:04.341 | Spain              | Spain              | 34 | Pass            |   -   | [66.8, 35.4]    | -> Pedro González         |  |
|  +3.62 | 00:19:05.508 | Spain              | Spain              | 34 | Ball Receipt*   |   -   | [78.6, 14.1]    | Controlled Receipt        |  |
|  +3.62 | 00:19:05.508 | Spain              | Spain              | 34 | Carry           |   -   | [78.6, 14.1]    | Carry                     |  |
|  +5.71 | 00:19:07.593 | Spain              | Spain              | 34 | Pass            |   -   | [88.4, 8.7]     | -> Jordi Alba Ram         |  |
|  +7.00 | 00:19:08.886 | Spain              | Spain              | 34 | Ball Receipt*   |   -   | [101.0, 3.4]    | Controlled Receipt        |  |
|  +7.00 | 00:19:08.886 | Spain              | Spain              | 34 | Carry           |   -   | [101.0, 3.4]    | Carry                     |  |
|  -0.33 | 00:19:01.554 | Spain              | Spain              | 110 | Miscontrol      |   -   | [98.2, 70.0]    | Miscontrol                |  |
|  -0.20 | 00:19:01.687 | Poland             | Spain              | 110 | Ball Recovery   |   -   | [24.0, 11.0]    |                           |  |
|  -0.20 | 00:19:01.687 | Poland             | Spain              | 110 | Carry           |   -   | [24.0, 11.0]    | Carry                     |  |
|  +0.00 | 00:19:01.887 | Poland             | Spain              | 110 | Dribble         |   -   | [25.7, 10.1]    | Incomplete                |  |
|  +0.00 | 00:19:01.887 | Spain              | Spain              | 110 | Duel            |  Yes  | [94.4, 70.0]    | Tackle, Lost In Play      | **CP INITIATION** |
|  +0.73 | 00:19:02.615 | Spain              | Spain              | 110 | Pressure        |  Yes  | [92.0, 70.3]    |                           |  |
|  +0.85 | 00:19:02.738 | Poland             | Spain              | 110 | Ball Recovery   |   -   | [29.8, 7.4]     |                           |  |
|  +0.85 | 00:19:02.738 | Poland             | Spain              | 110 | Carry           |   -   | [29.8, 7.4]     | Carry                     |  |
|  +1.10 | 00:19:02.989 | Spain              | Spain              | 110 | Dribbled Past   |  Yes  | [89.1, 74.4]    |                           |  |
|  +1.10 | 00:19:02.989 | Poland             | Spain              | 110 | Dribble         |   -   | [31.0, 5.7]     | Complete                  |  |
|  +1.10 | 00:19:02.989 | Poland             | Spain              | 110 | Carry           |   -   | [31.0, 5.7]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.22 | 00:19:05.103 | Poland             | Spain              | 110 | Dribble         |   -   | [34.7, 7.9]     | Incomplete                | **POSSIBLE TRANSITION** |
|  +3.22 | 00:19:05.103 | Spain              | Spain              | 110 | Duel            |  Yes  | [85.4, 72.2]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +4.23 | 00:19:06.121 | Spain              | Spain              | 110 | Ball Recovery   |   -   | [86.2, 75.6]    |                           |  |
|  +4.23 | 00:19:06.121 | Spain              | Spain              | 110 | Carry           |   -   | [86.2, 75.6]    | Carry                     |  |
|  +6.56 | 00:19:08.447 | Spain              | Spain              | 110 | Pass            |   -   | [91.2, 63.3]    | -> Álvaro Borja M         |  |
|  +7.93 | 00:19:09.822 | Spain              | Spain              | 110 | Ball Receipt*   |   -   | [112.7, 58.4]   | Controlled Receipt        |  |

---

### Case 106: Episode `3788762_p70_09e01bd8`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  +0.00 | 00:41:49.846 | Spain              | Spain              | 70 | Pressure        |  Yes  | [26.6, 61.1]    |                           | **CP INITIATION** |
|  +0.61 | 00:41:50.458 | Poland             | Spain              | 70 | Dribble         |   -   | [98.0, 19.0]    | Incomplete                |  |
|  +0.61 | 00:41:50.458 | Spain              | Spain              | 70 | Duel            |  Yes  | [22.1, 61.1]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +2.53 | 00:41:52.377 | Spain              | Spain              | 70 | Ball Recovery   |   -   | [28.5, 46.1]    |                           |  |
|  +2.53 | 00:41:52.377 | Spain              | Spain              | 70 | Carry           |   -   | [28.5, 46.1]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.50 | 00:41:53.349 | Spain              | Spain              | 70 | Pass            |   -   | [29.2, 44.9]    | -> Jordi Alba Ram         |  |
|  +5.10 | 00:41:54.943 | Spain              | Spain              | 70 | Ball Receipt*   |   -   | [31.1, 18.3]    | Controlled Receipt        |  |
|  +5.10 | 00:41:54.943 | Spain              | Spain              | 70 | Carry           |   -   | [31.1, 18.3]    | Carry                     |  |
|  +5.45 | 00:41:55.292 | Poland             | Spain              | 70 | Pressure        |   -   | [86.2, 64.6]    |                           |  |
|  +6.46 | 00:41:56.306 | Spain              | Spain              | 70 | Dispossessed    |   -   | [31.1, 16.2]    | Dispossessed              |  |
|  +6.46 | 00:41:56.306 | Poland             | Poland             | 71 | Duel            |  Yes  | [89.0, 63.9]    | Tackle, Success In Play   |  |
|  +7.82 | 00:41:57.667 | Poland             | Poland             | 71 | Ball Recovery   |   -   | [94.2, 56.0]    |                           |  |
|  +7.82 | 00:41:57.667 | Poland             | Poland             | 71 | Carry           |   -   | [94.2, 56.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -2.99 | 00:41:46.859 | Spain              | Poland             | 143 | Pressure        |   -   | [15.0, 25.6]    |                           |  |
|  -2.61 | 00:41:47.236 | Poland             | Poland             | 143 | Pass            |   -   | [97.4, 53.8]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |
|  -0.93 | 00:41:48.918 | Spain              | Spain              | 144 | Ball Recovery   |   -   | [4.6, 42.0]     |                           |  |
|  -0.93 | 00:41:48.918 | Spain              | Spain              | 144 | Carry           |   -   | [4.6, 42.0]     | Carry                     |  |
|  +2.98 | 00:41:52.826 | Spain              | Spain              | 144 | Pass            |   -   | [15.0, 42.3]    | -> Pau Francisco          |  |
|  +4.33 | 00:41:54.174 | Spain              | Spain              | 144 | Ball Receipt*   |   -   | [18.8, 31.4]    | Controlled Receipt        |  |
|  +4.33 | 00:41:54.174 | Spain              | Spain              | 144 | Carry           |   -   | [18.8, 31.4]    | Carry                     |  |
|  +5.32 | 00:41:55.168 | Spain              | Spain              | 144 | Pass            |   -   | [20.8, 32.1]    | -> Rodrigo Hernán         |  |
|  +6.60 | 00:41:56.446 | Spain              | Spain              | 144 | Ball Receipt*   |   -   | [35.5, 44.9]    | Controlled Receipt        |  |
|  +6.60 | 00:41:56.446 | Spain              | Spain              | 144 | Carry           |   -   | [35.5, 44.9]    | Carry                     |  |

---

### Case 107: Episode `3788762_p71_3edef4a0`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.96 | 00:41:53.349 | Spain              | Spain              | 70 | Pass            |   -   | [29.2, 44.9]    | -> Jordi Alba Ram         |  |
|  -1.36 | 00:41:54.943 | Spain              | Spain              | 70 | Ball Receipt*   |   -   | [31.1, 18.3]    | Controlled Receipt        |  |
|  -1.36 | 00:41:54.943 | Spain              | Spain              | 70 | Carry           |   -   | [31.1, 18.3]    | Carry                     |  |
|  -1.01 | 00:41:55.292 | Poland             | Spain              | 70 | Pressure        |   -   | [86.2, 64.6]    |                           |  |
|  +0.00 | 00:41:56.306 | Spain              | Spain              | 70 | Dispossessed    |   -   | [31.1, 16.2]    | Dispossessed              |  |
|  +0.00 | 00:41:56.306 | Poland             | Poland             | 71 | Duel            |  Yes  | [89.0, 63.9]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.36 | 00:41:57.667 | Poland             | Poland             | 71 | Ball Recovery   |   -   | [94.2, 56.0]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.36 | 00:41:57.667 | Poland             | Poland             | 71 | Carry           |   -   | [94.2, 56.0]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.00 | 00:41:58.310 | Spain              | Poland             | 71 | Pressure        |  Yes  | [23.8, 28.0]    |                           |  |
|  +2.76 | 00:41:59.062 | Spain              | Poland             | 71 | Dribbled Past   |  Yes  | [23.8, 30.3]    |                           |  |
|  +2.76 | 00:41:59.062 | Poland             | Poland             | 71 | Dribble         |   -   | [96.3, 49.8]    | Complete                  |  |
|  +2.76 | 00:41:59.062 | Poland             | Poland             | 71 | Carry           |   -   | [96.3, 49.8]    | Carry                     |  |
|  +3.43 | 00:41:59.735 | Poland             | Poland             | 71 | Shot            |   -   | [97.8, 43.5]    | Post                      |  |
|  +4.18 | 00:42:00.481 | Spain              | Poland             | 71 | Goal Keeper     |   -   | [1.5, 39.2]     |                           |  |
|  +4.98 | 00:42:01.287 | Poland             | Poland             | 71 | Ball Recovery   |   -   | [110.8, 34.2]   |                           |  |
|  +4.98 | 00:42:01.287 | Poland             | Poland             | 71 | Carry           |   -   | [110.8, 34.2]   | Carry                     |  |
|  +5.96 | 00:42:02.267 | Spain              | Poland             | 71 | Pressure        |   -   | [9.7, 48.5]     |                           |  |
|  +6.20 | 00:42:02.510 | Poland             | Poland             | 71 | Shot            |   -   | [112.6, 32.3]   | Saved                     |  |
|  +6.36 | 00:42:02.663 | Spain              | Poland             | 71 | Goal Keeper     |   -   | [2.8, 44.0]     |                           |  |
|  +6.52 | 00:42:02.823 | Spain              | Poland             | 71 | Block           |   -   | [4.6, 41.4]     |                           |  |
|  -2.13 | 00:41:54.174 | Spain              | Spain              | 144 | Ball Receipt*   |   -   | [18.8, 31.4]    | Controlled Receipt        |  |
|  -2.13 | 00:41:54.174 | Spain              | Spain              | 144 | Carry           |   -   | [18.8, 31.4]    | Carry                     |  |
|  -1.14 | 00:41:55.168 | Spain              | Spain              | 144 | Pass            |   -   | [20.8, 32.1]    | -> Rodrigo Hernán         |  |
|  +0.14 | 00:41:56.446 | Spain              | Spain              | 144 | Ball Receipt*   |   -   | [35.5, 44.9]    | Controlled Receipt        |  |
|  +0.14 | 00:41:56.446 | Spain              | Spain              | 144 | Carry           |   -   | [35.5, 44.9]    | Carry                     |  |
|  +4.85 | 00:42:01.159 | Spain              | Spain              | 144 | Pass            |   -   | [53.3, 43.5]    | -> Marcos Llorent         |  |
|  +7.23 | 00:42:03.533 | Spain              | Spain              | 144 | Ball Receipt*   |   -   | [65.4, 74.4]    | Controlled Receipt        |  |
|  +7.23 | 00:42:03.533 | Spain              | Spain              | 144 | Carry           |   -   | [65.4, 74.4]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 108: Episode `3788762_p100_93593bbc`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.29 | 00:13:06.670 | Spain              | Spain              | 27 | Pass            |   -   | [67.9, 69.2]    | -> Aymeric Laport         |  |
|  +0.12 | 00:13:08.082 | Spain              | Spain              | 27 | Ball Receipt*   |   -   | [51.8, 56.0]    | Controlled Receipt        | **PRESSING-TEAM FIRST CONTROL** |
|  +0.12 | 00:13:08.082 | Spain              | Spain              | 27 | Carry           |   -   | [51.8, 56.0]    | Carry                     |  |
|  +1.83 | 00:13:09.791 | Spain              | Spain              | 27 | Pass            |   -   | [50.8, 54.1]    | -> Pau Francisco          |  |
|  +3.44 | 00:13:11.400 | Spain              | Spain              | 27 | Ball Receipt*   |   -   | [50.5, 26.0]    | Controlled Receipt        |  |
|  +3.44 | 00:13:11.400 | Spain              | Spain              | 27 | Carry           |   -   | [50.5, 26.0]    | Carry                     |  |
|  +6.82 | 00:13:14.778 | Spain              | Spain              | 27 | Pass            |   -   | [70.0, 17.5]    | -> Pedro González         |  |
|  +7.83 | 00:13:15.797 | Spain              | Spain              | 27 | Ball Receipt*   |   -   | [78.8, 6.8]     | Controlled Receipt        |  |
|  +7.83 | 00:13:15.797 | Spain              | Spain              | 27 | Carry           |   -   | [78.8, 6.8]     | Carry                     |  |
|  -2.46 | 00:13:05.504 | Poland             | Poland             | 99 | Ball Receipt*   |   -   | [22.8, 55.9]    | Controlled Receipt        |  |
|  -2.46 | 00:13:05.504 | Poland             | Poland             | 99 | Pass            |   -   | [31.0, 56.2]    | -> Kacper Kozłows         |  |
|  -1.79 | 00:13:06.176 | Poland             | Poland             | 99 | Ball Receipt*   |   -   | [77.1, 60.3]    | Controlled Receipt        |  |
|  -1.73 | 00:13:06.232 | Spain              | Poland             | 99 | Dribbled Past   |   -   | [43.0, 19.8]    |                           |  |
|  -1.73 | 00:13:06.232 | Poland             | Poland             | 99 | Dribble         |   -   | [77.1, 60.3]    | Complete                  |  |
|  -1.73 | 00:13:06.232 | Poland             | Poland             | 99 | Carry           |   -   | [77.1, 60.3]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:13:07.963 | Poland             | Poland             | 99 | Dribble         |   -   | [83.6, 58.3]    | Incomplete                | **POSSIBLE TRANSITION** |
|  +0.00 | 00:13:07.963 | Spain              | Spain              | 100 | Duel            |  Yes  | [36.5, 21.8]    | Tackle, Success In Play   | **CP INITIATION** |
|  +2.87 | 00:13:10.833 | Spain              | Spain              | 100 | Ball Recovery   |   -   | [26.8, 61.6]    |                           | (v2.6 Regain Event) |
|  +2.87 | 00:13:10.833 | Spain              | Spain              | 100 | Carry           |   -   | [26.8, 61.6]    | Carry                     |  |
|  +4.47 | 00:13:12.431 | Poland             | Spain              | 100 | Pressure        |  Yes  | [89.4, 13.7]    |                           |  |
|  +4.99 | 00:13:12.957 | Spain              | Spain              | 100 | Miscontrol      |   -   | [32.6, 73.6]    | Miscontrol                |  |
|  +5.69 | 00:13:13.657 | Poland             | Spain              | 100 | Foul Committed  |   -   | [84.4, 6.5]     |                           |  |
|  +5.69 | 00:13:13.657 | Spain              | Spain              | 100 | Foul Won        |   -   | [35.7, 73.6]    |                           |  |
|  +7.16 | 00:13:15.126 | Spain              | Spain              | 100 | Ball Recovery   |   -   | [43.2, 76.1]    |                           |  |
|  +7.16 | 00:13:15.126 | Spain              | Spain              | 100 | Carry           |   -   | [43.2, 76.1]    | Carry                     |  |

---

### Case 109: Episode `3788762_p103_0dc2b7c7`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.50 | 00:15:12.394 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [49.9, 13.4]    | Controlled Receipt        |  |
|  -2.50 | 00:15:12.394 | Spain              | Spain              | 31 | Carry           |   -   | [49.9, 13.4]    | Carry                     |  |
|  -0.18 | 00:15:14.714 | Spain              | Spain              | 31 | Pass            |   -   | [48.4, 15.1]    | -> Marcos Llorent         |  |
|  +2.08 | 00:15:16.975 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [53.5, 65.4]    | Controlled Receipt        |  |
|  +2.08 | 00:15:16.975 | Spain              | Spain              | 31 | Carry           |   -   | [53.5, 65.4]    | Carry                     |  |
|  +3.45 | 00:15:18.338 | Spain              | Spain              | 31 | Pass            |   -   | [54.2, 67.1]    | -> Gerard Moreno          |  |
|  +6.27 | 00:15:21.161 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [73.2, 68.4]    | Controlled Receipt        |  |
|  +6.27 | 00:15:21.161 | Spain              | Spain              | 31 | Carry           |   -   | [73.2, 68.4]    | Carry                     |  |
|  -2.57 | 00:15:12.325 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [72.4, 23.7]    | Controlled Receipt        |  |
|  -2.57 | 00:15:12.325 | Spain              | Spain              | 103 | Carry           |   -   | [72.4, 23.7]    | Carry                     |  |
|  -2.09 | 00:15:12.801 | Poland             | Spain              | 103 | Pass            |   -   | [50.1, 55.0]    | Incomplete (Incomplete)   |  |
|  -2.07 | 00:15:12.816 | Spain              | Spain              | 103 | Miscontrol      |   -   | [71.4, 24.7]    | Miscontrol                |  |
|  -0.35 | 00:15:14.545 | Spain              | Spain              | 103 | Ball Recovery   |   -   | [65.2, 23.2]    |                           |  |
|  -0.35 | 00:15:14.545 | Spain              | Spain              | 103 | Carry           |   -   | [65.2, 23.2]    | Carry                     |  |
|  +0.00 | 00:15:14.891 | Poland             | Spain              | 103 | Pressure        |  Yes  | [52.3, 57.1]    |                           | **CP INITIATION** |
|  +0.26 | 00:15:15.149 | Spain              | Spain              | 103 | Pass            |   -   | [65.9, 23.0]    | -> Rodrigo Hernán         |  |
|  +0.80 | 00:15:15.693 | Poland             | Spain              | 103 | Pressure        |  Yes  | [55.2, 46.8]    |                           |  |
|  +0.86 | 00:15:15.755 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [64.7, 30.2]    | Controlled Receipt        |  |
|  +0.86 | 00:15:15.755 | Spain              | Spain              | 103 | Carry           |   -   | [64.7, 30.2]    | Carry                     |  |
|  +1.14 | 00:15:16.032 | Poland             | Spain              | 103 | Pressure        |   -   | [57.1, 50.4]    |                           |  |
|  +1.46 | 00:15:16.354 | Spain              | Spain              | 103 | Pass            |   -   | [65.2, 30.2]    | -> Daniel Olmo Ca         |  |
|  +1.87 | 00:15:16.762 | Poland             | Spain              | 103 | Pressure        |   -   | [45.0, 49.9]    |                           |  |
|  +2.22 | 00:15:17.108 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [73.1, 30.7]    | Controlled Receipt        |  |
|  +2.22 | 00:15:17.108 | Spain              | Spain              | 103 | Carry           |   -   | [73.1, 30.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +3.45 | 00:15:18.344 | Poland             | Spain              | 103 | Pressure        |   -   | [42.6, 38.8]    |                           |  |
|  +3.74 | 00:15:18.629 | Spain              | Spain              | 103 | Dribble         |   -   | [78.4, 40.1]    | Incomplete                |  |
|  +3.74 | 00:15:18.629 | Poland             | Poland             | 104 | Duel            |  Yes  | [41.7, 40.0]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +5.32 | 00:15:20.214 | Poland             | Poland             | 104 | Ball Recovery   |   -   | [40.9, 59.8]    |                           | **POSSIBLE TRANSITION** |
|  +5.32 | 00:15:20.214 | Poland             | Poland             | 104 | Carry           |   -   | [40.9, 59.8]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +7.60 | 00:15:22.486 | Spain              | Poland             | 104 | Pressure        |  Yes  | [70.0, 14.0]    |                           |  |

---

### Case 110: Episode `3788762_p104_904d8471`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.65 | 00:15:16.975 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [53.5, 65.4]    | Controlled Receipt        |  |
|  -1.65 | 00:15:16.975 | Spain              | Spain              | 31 | Carry           |   -   | [53.5, 65.4]    | Carry                     |  |
|  -0.29 | 00:15:18.338 | Spain              | Spain              | 31 | Pass            |   -   | [54.2, 67.1]    | -> Gerard Moreno          |  |
|  +2.53 | 00:15:21.161 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [73.2, 68.4]    | Controlled Receipt        |  |
|  +2.53 | 00:15:21.161 | Spain              | Spain              | 31 | Carry           |   -   | [73.2, 68.4]    | Carry                     |  |
|  +5.56 | 00:15:24.192 | Spain              | Spain              | 31 | Pass            |   -   | [87.1, 68.6]    | -> Marcos Llorent         |  |
|  +7.34 | 00:15:25.967 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [76.0, 67.3]    | Controlled Receipt        |  |
|  +7.34 | 00:15:25.967 | Spain              | Spain              | 31 | Carry           |   -   | [76.0, 67.3]    | Carry                     |  |
|  -2.94 | 00:15:15.693 | Poland             | Spain              | 103 | Pressure        |  Yes  | [55.2, 46.8]    |                           |  |
|  -2.87 | 00:15:15.755 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [64.7, 30.2]    | Controlled Receipt        |  |
|  -2.87 | 00:15:15.755 | Spain              | Spain              | 103 | Carry           |   -   | [64.7, 30.2]    | Carry                     |  |
|  -2.60 | 00:15:16.032 | Poland             | Spain              | 103 | Pressure        |   -   | [57.1, 50.4]    |                           |  |
|  -2.27 | 00:15:16.354 | Spain              | Spain              | 103 | Pass            |   -   | [65.2, 30.2]    | -> Daniel Olmo Ca         |  |
|  -1.87 | 00:15:16.762 | Poland             | Spain              | 103 | Pressure        |   -   | [45.0, 49.9]    |                           |  |
|  -1.52 | 00:15:17.108 | Spain              | Spain              | 103 | Ball Receipt*   |   -   | [73.1, 30.7]    | Controlled Receipt        |  |
|  -1.52 | 00:15:17.108 | Spain              | Spain              | 103 | Carry           |   -   | [73.1, 30.7]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.28 | 00:15:18.344 | Poland             | Spain              | 103 | Pressure        |   -   | [42.6, 38.8]    |                           |  |
|  +0.00 | 00:15:18.629 | Spain              | Spain              | 103 | Dribble         |   -   | [78.4, 40.1]    | Incomplete                |  |
|  +0.00 | 00:15:18.629 | Poland             | Poland             | 104 | Duel            |  Yes  | [41.7, 40.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +1.58 | 00:15:20.214 | Poland             | Poland             | 104 | Ball Recovery   |   -   | [40.9, 59.8]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.58 | 00:15:20.214 | Poland             | Poland             | 104 | Carry           |   -   | [40.9, 59.8]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.86 | 00:15:22.486 | Spain              | Poland             | 104 | Pressure        |  Yes  | [70.0, 14.0]    |                           |  |
|  +7.94 | 00:15:26.567 | Poland             | Poland             | 104 | Pass            |   -   | [68.9, 73.1]    | -> Piotr Zielińsk         |  |

---

### Case 111: Episode `3788762_p120_c3b340f8`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.21 | 00:27:02.523 | Spain              | Spain              | 44 | Dispossessed    |   -   | [64.0, 3.1]     | Dispossessed              |  |
|  -1.21 | 00:27:02.523 | Poland             | Spain              | 44 | Duel            |   -   | [56.1, 77.0]    | Tackle, Lost Out          |  |
|  -2.03 | 00:27:01.711 | Spain              | Spain              | 120 | Ball Receipt*   |   -   | [103.3, 45.4]   | Controlled Receipt        |  |
|  -2.03 | 00:27:01.711 | Spain              | Spain              | 120 | Carry           |   -   | [103.3, 45.4]   | Carry                     |  |
|  -1.95 | 00:27:01.791 | Spain              | Spain              | 120 | Miscontrol      |   -   | [104.7, 44.4]   | Miscontrol                |  |
|  -1.16 | 00:27:02.577 | Spain              | Spain              | 120 | Pressure        |   -   | [101.1, 45.4]   |                           |  |
|  -0.37 | 00:27:03.368 | Poland             | Spain              | 120 | Ball Recovery   |   -   | [21.4, 36.9]    |                           |  |
|  -0.37 | 00:27:03.368 | Poland             | Spain              | 120 | Carry           |   -   | [21.4, 36.9]    | Carry                     |  |
|  +0.00 | 00:27:03.737 | Spain              | Spain              | 120 | Pressure        |  Yes  | [98.5, 40.3]    |                           | **CP INITIATION** |
|  +0.32 | 00:27:04.062 | Poland             | Spain              | 120 | Pass            |   -   | [23.1, 36.9]    | -> Jakub Moder            |  |
|  +1.19 | 00:27:04.924 | Poland             | Spain              | 120 | Ball Receipt*   |   -   | [34.7, 35.2]    | Controlled Receipt        |  |
|  +1.19 | 00:27:04.924 | Poland             | Spain              | 120 | Carry           |   -   | [34.7, 35.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +1.51 | 00:27:05.250 | Spain              | Spain              | 120 | Pressure        |  Yes  | [86.2, 42.3]    |                           |  |
|  +2.93 | 00:27:06.663 | Poland             | Spain              | 120 | Dispossessed    |   -   | [35.9, 37.1]    | Dispossessed              |  |
|  +2.93 | 00:27:06.663 | Spain              | Spain              | 120 | Duel            |  Yes  | [84.2, 43.0]    | Tackle, Won               | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +2.93 | 00:27:06.663 | Spain              | Spain              | 120 | Carry           |   -   | [84.2, 43.0]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.95 | 00:27:07.683 | Spain              | Spain              | 120 | Pass            |   -   | [84.2, 43.0]    | -> Pablo Sarabia          |  |
|  +5.22 | 00:27:08.955 | Spain              | Spain              | 120 | Ball Receipt*   |   -   | [85.2, 56.0]    | Controlled Receipt        |  |
|  +5.22 | 00:27:08.955 | Spain              | Spain              | 120 | Carry           |   -   | [85.2, 56.0]    | Carry                     |  |
|  +7.02 | 00:27:10.759 | Spain              | Spain              | 120 | Pass            |   -   | [92.7, 55.5]    | -> Marcos Llorent         |  |

---

### Case 112: Episode `3788762_p147_fd75fca8`
- **Match**: `3788762` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_pass`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.91 | 00:43:39.098 | Spain              | Spain              | 73 | Ball Receipt*   |   -   | [54.0, 30.1]    | Controlled Receipt        |  |
|  -1.91 | 00:43:39.098 | Spain              | Spain              | 73 | Pass            |   -   | [53.5, 30.5]    | -> Pau Francisco          |  |
|  -0.46 | 00:43:40.540 | Spain              | Spain              | 73 | Ball Receipt*   |   -   | [42.0, 28.6]    | Controlled Receipt        |  |
|  -0.46 | 00:43:40.540 | Spain              | Spain              | 73 | Pass            |   -   | [42.4, 29.2]    | -> Aymeric Laport         |  |
|  +1.37 | 00:43:42.369 | Spain              | Spain              | 73 | Ball Receipt*   |   -   | [35.1, 60.0]    | Controlled Receipt        |  |
|  +1.37 | 00:43:42.369 | Spain              | Spain              | 73 | Carry           |   -   | [35.1, 60.0]    | Carry                     |  |
|  +3.40 | 00:43:44.407 | Spain              | Spain              | 73 | Pass            |   -   | [36.9, 55.8]    | -> Jorge Resurrec         |  |
|  +4.50 | 00:43:45.505 | Spain              | Spain              | 73 | Ball Receipt*   |   -   | [55.7, 52.8]    | Controlled Receipt        |  |
|  +4.50 | 00:43:45.505 | Spain              | Spain              | 73 | Pass            |   -   | [55.5, 52.8]    | -> Marcos Llorent         |  |
|  +5.68 | 00:43:46.686 | Spain              | Spain              | 73 | Ball Receipt*   |   -   | [56.5, 70.1]    | Controlled Receipt        |  |
|  +5.68 | 00:43:46.686 | Spain              | Spain              | 73 | Carry           |   -   | [56.5, 70.1]    | Carry                     |  |
|  +7.18 | 00:43:48.179 | Spain              | Spain              | 73 | Pass            |   -   | [56.5, 70.1]    | -> Gerard Moreno          |  |
|  +7.86 | 00:43:48.866 | Poland             | Spain              | 73 | Pressure        |   -   | [47.7, 9.8]     |                           |  |
|  -1.88 | 00:43:39.123 | Poland             | Poland             | 146 | Duel            |   -   | [78.6, 68.0]    | Aerial Lost               |  |
|  -1.88 | 00:43:39.123 | Spain              | Spain              | 147 | Pass            |   -   | [41.5, 12.1]    | -> Ferrán Torres          |  |
|  -0.57 | 00:43:40.437 | Spain              | Spain              | 147 | Ball Receipt*   |   -   | [49.0, 4.6]     | Controlled Receipt        |  |
|  -0.57 | 00:43:40.437 | Spain              | Spain              | 147 | Carry           |   -   | [49.0, 4.6]     | Carry                     |  |
|  +0.00 | 00:43:41.004 | Poland             | Spain              | 147 | Pressure        |  Yes  | [70.1, 70.9]    |                           | **CP INITIATION** |
|  +0.39 | 00:43:41.396 | Spain              | Spain              | 147 | Pass            |   -   | [49.7, 6.1]     | Incomplete (Incomplete)   |  |
|  +0.43 | 00:43:41.436 | Spain              | Spain              | 147 | Ball Receipt*   |   -   | [29.0, 17.9]    | Incomplete Receipt (Incomplete) |  |
|  +0.43 | 00:43:41.436 | Poland             | Spain              | 147 | Block           |  Yes  | [72.1, 72.3]    |                           |  |
|  +1.16 | 00:43:42.160 | Poland             | Spain              | 147 | Pressure        |  Yes  | [83.2, 69.9]    |                           |  |
|  +1.38 | 00:43:42.387 | Spain              | Spain              | 147 | Ball Recovery   |   -   | [32.6, 7.5]     |                           |  |
|  +1.38 | 00:43:42.387 | Spain              | Spain              | 147 | Carry           |   -   | [32.6, 7.5]     | Carry                     | **OPPONENT LAST CONTROL** |
|  +1.46 | 00:43:42.467 | Spain              | Spain              | 147 | Dribble         |   -   | [35.0, 7.5]     | Incomplete                |  |
|  +1.46 | 00:43:42.467 | Poland             | Spain              | 147 | Duel            |  Yes  | [85.1, 72.6]    | Tackle, Lost In Play      | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +3.49 | 00:43:44.492 | Poland             | Spain              | 147 | Pressure        |   -   | [96.4, 69.9]    |                           |  |
|  +4.00 | 00:43:45.002 | Spain              | Spain              | 147 | Clearance       |   -   | [17.4, 14.8]    |                           |  |

---

### Case 113: Episode `3788766_p5_b4c397ea`
- **Match**: `3788766` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Wales** vs Actual Opponent: **Italy** (StatsBomb Poss Team: `Wales`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.90 | 00:02:11.084 | Italy              | Italy              | 4 | Ball Receipt*   |   -   | [63.1, 27.0]    | Controlled Receipt        |  |
|  -2.90 | 00:02:11.084 | Italy              | Italy              | 4 | Pass            |   -   | [63.4, 28.7]    | -> Federico Chies         |  |
|  -2.18 | 00:02:11.805 | Wales              | Italy              | 4 | Pressure        |   -   | [45.7, 41.0]    |                           |  |
|  -2.04 | 00:02:11.942 | Italy              | Italy              | 4 | Ball Receipt*   |   -   | [72.6, 39.9]    | Controlled Receipt        |  |
|  -2.04 | 00:02:11.942 | Italy              | Italy              | 4 | Carry           |   -   | [72.6, 39.9]    | Carry                     |  |
|  -1.66 | 00:02:12.321 | Italy              | Italy              | 4 | Pass            |   -   | [71.4, 36.6]    | -> Andrea Belotti         |  |
|  -1.15 | 00:02:12.835 | Italy              | Italy              | 4 | Ball Receipt*   |   -   | [67.3, 34.2]    | Controlled Receipt        |  |
|  -1.15 | 00:02:12.835 | Italy              | Italy              | 4 | Carry           |   -   | [67.3, 34.2]    | Carry                     | **OPPONENT LAST CONTROL** |
|  -0.90 | 00:02:13.087 | Wales              | Italy              | 4 | Pressure        |   -   | [51.1, 48.4]    |                           |  |
|  -0.81 | 00:02:13.172 | Wales              | Italy              | 4 | Pressure        |   -   | [56.1, 46.7]    |                           |  |
|  -0.55 | 00:02:13.437 | Wales              | Italy              | 4 | Pressure        |   -   | [47.6, 40.1]    |                           |  |
|  +0.00 | 00:02:13.986 | Italy              | Italy              | 4 | Dispossessed    |   -   | [69.8, 39.6]    | Dispossessed              |  |
|  +0.00 | 00:02:13.986 | Wales              | Wales              | 5 | Duel            |  Yes  | [50.3, 40.5]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.76 | 00:02:14.747 | Wales              | Wales              | 5 | Ball Recovery   |   -   | [56.8, 36.5]    |                           | (v2.6 Regain Event) |
|  +0.76 | 00:02:14.747 | Wales              | Wales              | 5 | Carry           |   -   | [56.8, 36.5]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +0.78 | 00:02:14.764 | Italy              | Wales              | 5 | Pressure        |  Yes  | [62.9, 39.1]    |                           |  |
|  +1.47 | 00:02:15.457 | Italy              | Wales              | 5 | Foul Committed  |  Yes  | [62.3, 44.6]    |                           |  |
|  +1.47 | 00:02:15.457 | Wales              | Wales              | 5 | Foul Won        |   -   | [57.8, 35.5]    |                           |  |
|  -2.19 | 00:02:11.792 | Wales              | Wales              | 98 | Ball Receipt*   |   -   | [36.7, 2.5]     | Controlled Receipt        |  |
|  -2.19 | 00:02:11.792 | Wales              | Wales              | 98 | Carry           |   -   | [36.7, 2.5]     | Carry                     |  |
|  -0.84 | 00:02:13.146 | Wales              | Wales              | 98 | Pass            |   -   | [36.7, 2.5]     | -> Chris Gunter           |  |
|  +0.16 | 00:02:14.146 | Wales              | Wales              | 98 | Ball Receipt*   |   -   | [15.9, 8.5]     | Controlled Receipt        |  |
|  +0.16 | 00:02:14.146 | Wales              | Wales              | 98 | Carry           |   -   | [15.9, 8.5]     | Carry                     |  |
|  +1.06 | 00:02:15.050 | Wales              | Wales              | 98 | Pass            |   -   | [15.6, 8.5]     | -> Danny Ward             |  |
|  +4.57 | 00:02:18.554 | Wales              | Wales              | 98 | Ball Receipt*   |   -   | [1.2, 40.5]     | Controlled Receipt        |  |
|  +4.57 | 00:02:18.554 | Wales              | Wales              | 98 | Pass            |   -   | [2.4, 41.8]     | Incomplete (Incomplete)   |  |
|  +7.75 | 00:02:21.732 | Wales              | Wales              | 98 | Ball Receipt*   |   -   | [57.6, 54.7]    | Incomplete Receipt (Incomplete) |  |
|  +7.75 | 00:02:21.732 | Italy              | Wales              | 98 | Pass            |   -   | [64.5, 26.2]    | Incomplete (Incomplete)   | **POSSIBLE TRANSITION** |

---

### Case 114: Episode `3788762_p65_8d74503a`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.23 | 00:40:13.258 | Poland             | Spain              | 64 | Ball Receipt*   |   -   | [40.9, 36.5]    | Controlled Receipt        |  |
|  -2.23 | 00:40:13.258 | Poland             | Spain              | 64 | Carry           |   -   | [40.9, 36.5]    | Carry                     |  |
|  -1.26 | 00:40:14.230 | Poland             | Spain              | 64 | Pass            |   -   | [41.1, 38.0]    | Incomplete (Incomplete)   |  |
|  -0.38 | 00:40:15.108 | Poland             | Spain              | 64 | Ball Receipt*   |   -   | [29.1, 32.5]    | Incomplete Receipt (Incomplete) |  |
|  -0.38 | 00:40:15.108 | Spain              | Spain              | 64 | Interception    |  Yes  | [88.2, 45.7]    | Won                       |  |
|  -0.38 | 00:40:15.108 | Spain              | Spain              | 64 | Carry           |   -   | [88.2, 45.7]    | Carry                     |  |
|  +0.00 | 00:40:15.486 | Spain              | Spain              | 64 | Dribble         |   -   | [91.0, 45.9]    | Incomplete                |  |
|  +0.00 | 00:40:15.486 | Poland             | Poland             | 65 | Duel            |  Yes  | [29.1, 34.2]    | Tackle, Success In Play   | **CP INITIATION** |
|  +2.19 | 00:40:17.673 | Spain              | Poland             | 65 | Pressure        |  Yes  | [105.9, 32.9]   |                           |  |
|  +3.21 | 00:40:18.693 | Poland             | Poland             | 65 | Ball Recovery   |   -   | [11.4, 52.8]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +3.21 | 00:40:18.693 | Poland             | Poland             | 65 | Carry           |   -   | [11.4, 52.8]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  -0.04 | 00:40:15.447 | Poland             | Poland             | 140 | Pressure        |   -   | [79.3, 54.2]    |                           |  |
|  +0.83 | 00:40:16.312 | Spain              | Spain              | 141 | Pass            |   -   | [38.9, 28.0]    | -> Unai Simón Men         |  |
|  +3.16 | 00:40:18.650 | Spain              | Spain              | 141 | Ball Receipt*   |   -   | [6.8, 40.8]     | Controlled Receipt        |  |
|  +3.16 | 00:40:18.650 | Spain              | Spain              | 141 | Carry           |   -   | [6.8, 40.8]     | Carry                     |  |
|  +4.27 | 00:40:19.756 | Spain              | Spain              | 141 | Pass            |   -   | [6.8, 40.8]     | -> Aymeric Laport         |  |
|  +6.04 | 00:40:21.522 | Spain              | Spain              | 141 | Ball Receipt*   |   -   | [16.7, 48.3]    | Controlled Receipt        |  |
|  +6.04 | 00:40:21.522 | Spain              | Spain              | 141 | Carry           |   -   | [16.7, 48.3]    | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 115: Episode `3788762_p50_3dcd309c`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.87 | 00:30:28.199 | Spain              | Poland             | 50 | Pressure        |   -   | [27.2, 59.4]    |                           |  |
|  -1.72 | 00:30:28.342 | Spain              | Poland             | 50 | Pressure        |   -   | [31.5, 58.8]    |                           |  |
|  -1.22 | 00:30:28.850 | Poland             | Poland             | 50 | Dribble         |   -   | [92.0, 19.6]    | Incomplete                |  |
|  -1.22 | 00:30:28.850 | Spain              | Poland             | 50 | Duel            |   -   | [28.1, 60.5]    | Tackle, Success In Play   |  |
|  -0.21 | 00:30:29.853 | Spain              | Poland             | 50 | Pass            |   -   | [27.2, 60.0]    | -> Jorge Resurrec         |  |
|  +0.00 | 00:30:30.067 | Poland             | Poland             | 50 | Pressure        |  Yes  | [90.5, 17.7]    |                           | **CP INITIATION** |
|  +0.25 | 00:30:30.316 | Spain              | Poland             | 50 | Ball Receipt*   |   -   | [29.6, 63.5]    | Controlled Receipt        |  |
|  +0.25 | 00:30:30.316 | Spain              | Poland             | 50 | Carry           |   -   | [29.6, 63.5]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.88 | 00:30:30.948 | Spain              | Poland             | 50 | Dispossessed    |   -   | [29.8, 63.2]    | Dispossessed              |  |
|  +0.88 | 00:30:30.948 | Poland             | Poland             | 50 | Duel            |  Yes  | [90.3, 16.9]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +1.74 | 00:30:31.805 | Spain              | Poland             | 50 | Pressure        |   -   | [34.7, 71.6]    |                           |  |
|  +2.26 | 00:30:32.323 | Poland             | Poland             | 50 | Ball Recovery   |   -   | [82.8, 7.4]     |                           | **POSSIBLE TRANSITION** |
|  +2.26 | 00:30:32.323 | Poland             | Poland             | 50 | Carry           |   -   | [82.8, 7.4]     | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +4.32 | 00:30:34.389 | Poland             | Poland             | 50 | Pass            |   -   | [76.4, 7.9]     | -> Mateusz Andrze         |  |
|  +5.04 | 00:30:35.106 | Poland             | Poland             | 50 | Ball Receipt*   |   -   | [71.9, 20.3]    | Controlled Receipt        |  |
|  +5.04 | 00:30:35.106 | Poland             | Poland             | 50 | Carry           |   -   | [71.9, 20.3]    | Carry                     |  |
|  +5.08 | 00:30:35.146 | Poland             | Poland             | 50 | Pass            |   -   | [71.9, 20.3]    | -> Tymoteusz Puch         |  |
|  +6.07 | 00:30:36.137 | Poland             | Poland             | 50 | Ball Receipt*   |   -   | [82.2, 9.2]     | Controlled Receipt        |  |
|  +6.07 | 00:30:36.137 | Poland             | Poland             | 50 | Carry           |   -   | [82.2, 9.2]     | Carry                     |  |
|  +7.12 | 00:30:37.191 | Poland             | Poland             | 50 | Pass            |   -   | [82.2, 9.2]     | Incomplete (Pass Offside) |  |
|  -1.08 | 00:30:28.989 | Poland             | Poland             | 126 | Pass            |   -   | [83.4, 80.0]    | -> Piotr Zielińsk         |  |
|  -0.95 | 00:30:29.114 | Spain              | Poland             | 126 | Pressure        |   -   | [37.7, 11.6]    |                           |  |
|  -0.29 | 00:30:29.774 | Poland             | Poland             | 126 | Ball Receipt*   |   -   | [79.5, 70.9]    | Controlled Receipt        |  |
|  -0.29 | 00:30:29.774 | Poland             | Poland             | 126 | Pass            |   -   | [79.1, 70.9]    | Incomplete (Pass Offside) |  |
|  +1.45 | 00:30:31.515 | Poland             | Poland             | 126 | Ball Receipt*   |   -   | [102.5, 67.3]   | Incomplete Receipt (Incomplete) |  |

---

### Case 116: Episode `3788762_p31_387a8d7c`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -1.94 | 00:14:43.818 | Spain              | Poland             | 30 | Dribbled Past   |   -   | [78.3, 45.9]    |                           |  |
|  -1.94 | 00:14:43.818 | Poland             | Poland             | 30 | Dribble         |   -   | [41.8, 34.2]    | Complete                  |  |
|  -1.94 | 00:14:43.818 | Poland             | Poland             | 30 | Carry           |   -   | [41.8, 34.2]    | Carry                     |  |
|  -0.29 | 00:14:45.461 | Spain              | Poland             | 30 | Pressure        |   -   | [65.3, 50.8]    |                           |  |
|  +0.00 | 00:14:45.753 | Poland             | Poland             | 30 | Dribble         |   -   | [55.0, 26.3]    | Incomplete                |  |
|  +0.00 | 00:14:45.753 | Spain              | Spain              | 31 | Duel            |  Yes  | [65.1, 53.8]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.19 | 00:14:45.946 | Spain              | Spain              | 31 | Block           |  Yes  | [67.0, 54.9]    |                           |  |
|  +1.64 | 00:14:47.392 | Spain              | Spain              | 31 | Ball Recovery   |   -   | [71.3, 60.3]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +1.64 | 00:14:47.392 | Spain              | Spain              | 31 | Carry           |   -   | [71.3, 60.3]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +3.09 | 00:14:48.841 | Spain              | Spain              | 31 | Pass            |   -   | [72.1, 66.0]    | -> Gerard Moreno          |  |
|  +4.01 | 00:14:49.763 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [79.2, 52.8]    | Controlled Receipt        |  |
|  +4.01 | 00:14:49.763 | Spain              | Spain              | 31 | Carry           |   -   | [79.2, 52.8]    | Carry                     |  |
|  +5.77 | 00:14:51.525 | Poland             | Spain              | 31 | Pressure        |   -   | [35.8, 32.7]    |                           |  |
|  +6.01 | 00:14:51.763 | Spain              | Spain              | 31 | Pass            |   -   | [84.3, 52.6]    | -> Álvaro Borja M         |  |
|  +6.61 | 00:14:52.365 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [92.3, 43.4]    | Controlled Receipt        |  |
|  +6.61 | 00:14:52.365 | Spain              | Spain              | 31 | Pass            |   -   | [92.3, 43.4]    | -> Gerard Moreno          |  |
|  +7.08 | 00:14:52.838 | Poland             | Spain              | 31 | Pressure        |   -   | [30.8, 41.5]    |                           |  |
|  +7.39 | 00:14:53.141 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [88.6, 40.4]    | Controlled Receipt        |  |
|  +7.39 | 00:14:53.141 | Spain              | Spain              | 31 | Pass            |   -   | [89.3, 40.4]    | Incomplete (Incomplete)   |  |
|  +7.60 | 00:14:53.356 | Spain              | Spain              | 31 | Ball Receipt*   |   -   | [96.1, 28.8]    | Incomplete Receipt (Incomplete) |  |
|  +7.60 | 00:14:53.356 | Poland             | Spain              | 31 | Block           |   -   | [27.6, 42.3]    |                           |  |
|  -0.75 | 00:14:45.002 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [107.2, 59.4]   | Incomplete Receipt (Incomplete) |  |
|  -0.75 | 00:14:45.002 | Poland             | Poland             | 102 | Ball Recovery   |   -   | [5.7, 31.8]     |                           |  |
|  -0.75 | 00:14:45.002 | Poland             | Poland             | 102 | Carry           |   -   | [5.7, 31.8]     | Carry                     |  |
|  +5.87 | 00:14:51.624 | Poland             | Poland             | 102 | Pass            |   -   | [12.0, 33.7]    | -> Tymoteusz Puch         | **OPPONENT LAST CONTROL** |

---

### Case 117: Episode `3788762_p30_be12410c`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `No`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.70 | 00:14:38.433 | Spain              | Spain              | 29 | Ball Receipt*   |   -   | [104.2, 25.0]   | Incomplete Receipt (Incomplete) |  |
|  -2.70 | 00:14:38.433 | Poland             | Poland             | 30 | Pass            |  Yes  | [20.1, 56.9]    | -> Mateusz Andrze         |  |
|  -2.09 | 00:14:39.046 | Poland             | Poland             | 30 | Ball Receipt*   |   -   | [28.5, 57.9]    | Controlled Receipt        |  |
|  -2.09 | 00:14:39.046 | Poland             | Poland             | 30 | Carry           |   -   | [28.5, 57.9]    | Carry                     |  |
|  +0.00 | 00:14:41.133 | Spain              | Poland             | 30 | Pressure        |  Yes  | [86.3, 24.7]    |                           | **CP INITIATION** |
|  +0.86 | 00:14:41.996 | Poland             | Poland             | 30 | Pass            |   -   | [35.3, 51.9]    | -> Jakub Moder            |  |
|  +1.43 | 00:14:42.561 | Spain              | Poland             | 30 | Pressure        |  Yes  | [81.1, 46.8]    |                           |  |
|  +1.55 | 00:14:42.679 | Poland             | Poland             | 30 | Ball Receipt*   |   -   | [35.8, 36.5]    | Controlled Receipt        |  |
|  +1.55 | 00:14:42.679 | Poland             | Poland             | 30 | Carry           |   -   | [35.8, 36.5]    | Carry                     |  |
|  +2.68 | 00:14:43.818 | Spain              | Poland             | 30 | Dribbled Past   |   -   | [78.3, 45.9]    |                           |  |
|  +2.68 | 00:14:43.818 | Poland             | Poland             | 30 | Dribble         |   -   | [41.8, 34.2]    | Complete                  |  |
|  +2.68 | 00:14:43.818 | Poland             | Poland             | 30 | Carry           |   -   | [41.8, 34.2]    | Carry                     |  |
|  +4.33 | 00:14:45.461 | Spain              | Poland             | 30 | Pressure        |   -   | [65.3, 50.8]    |                           |  |
|  +4.62 | 00:14:45.753 | Poland             | Poland             | 30 | Dribble         |   -   | [55.0, 26.3]    | Incomplete                |  |
|  +4.62 | 00:14:45.753 | Spain              | Spain              | 31 | Duel            |  Yes  | [65.1, 53.8]    | Tackle, Success In Play   | (v2.6 Regain Event) |
|  +4.81 | 00:14:45.946 | Spain              | Spain              | 31 | Block           |  Yes  | [67.0, 54.9]    |                           |  |
|  +6.26 | 00:14:47.392 | Spain              | Spain              | 31 | Ball Recovery   |   -   | [71.3, 60.3]    |                           | **POSSIBLE TRANSITION** |
|  +6.26 | 00:14:47.392 | Spain              | Spain              | 31 | Carry           |   -   | [71.3, 60.3]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +7.71 | 00:14:48.841 | Spain              | Spain              | 31 | Pass            |   -   | [72.1, 66.0]    | -> Gerard Moreno          |  |
|  -2.19 | 00:14:38.944 | Spain              | Spain              | 101 | Pass            |   -   | [75.3, 15.0]    | -> Rodrigo Hernán         |  |
|  -1.36 | 00:14:39.773 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [78.9, 25.1]    | Controlled Receipt        |  |
|  -1.36 | 00:14:39.773 | Spain              | Spain              | 101 | Carry           |   -   | [78.9, 25.1]    | Carry                     |  |
|  -0.53 | 00:14:40.599 | Spain              | Spain              | 101 | Pass            |   -   | [78.0, 24.7]    | -> Marcos Llorent         |  |
|  +1.06 | 00:14:42.189 | Poland             | Spain              | 101 | Pressure        |   -   | [32.7, 29.6]    |                           |  |
|  +1.14 | 00:14:42.274 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [84.0, 50.0]    | Controlled Receipt        |  |
|  +1.14 | 00:14:42.274 | Spain              | Spain              | 101 | Carry           |   -   | [84.0, 50.0]    | Carry                     |  |
|  +1.18 | 00:14:42.314 | Spain              | Spain              | 101 | Pass            |   -   | [84.2, 50.5]    | Incomplete (Incomplete)   |  |
|  +3.87 | 00:14:45.002 | Spain              | Spain              | 101 | Ball Receipt*   |   -   | [107.2, 59.4]   | Incomplete Receipt (Incomplete) |  |
|  +3.87 | 00:14:45.002 | Poland             | Poland             | 102 | Ball Recovery   |   -   | [5.7, 31.8]     |                           |  |
|  +3.87 | 00:14:45.002 | Poland             | Poland             | 102 | Carry           |   -   | [5.7, 31.8]     | Carry                     | **OPPONENT LAST CONTROL** |

---

### Case 118: Episode `3788762_p20_14467df2`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_failed_dribble` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.75 | 00:09:39.505 | Spain              | Spain              | 20 | Ball Receipt*   |   -   | [91.2, 20.0]    | Controlled Receipt        |  |
|  -2.75 | 00:09:39.505 | Spain              | Spain              | 20 | Pass            |   -   | [91.2, 20.0]    | Incomplete (Incomplete)   |  |
|  -1.61 | 00:09:40.653 | Spain              | Spain              | 20 | Ball Receipt*   |   -   | [103.2, 12.6]   | Incomplete Receipt (Incomplete) |  |
|  -1.61 | 00:09:40.653 | Poland             | Spain              | 20 | Interception    |   -   | [17.8, 68.4]    | Won                       |  |
|  -1.61 | 00:09:40.653 | Poland             | Spain              | 20 | Carry           |   -   | [17.8, 68.4]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:09:42.260 | Spain              | Spain              | 20 | Pressure        |  Yes  | [102.1, 7.2]    |                           | **CP INITIATION** |
|  +2.60 | 00:09:44.855 | Poland             | Spain              | 20 | Dribble         |   -   | [15.4, 75.9]    | Incomplete                |  |
|  +2.60 | 00:09:44.855 | Spain              | Spain              | 20 | Duel            |  Yes  | [104.7, 4.2]    | Tackle, Won               | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +2.60 | 00:09:44.855 | Spain              | Spain              | 20 | Carry           |   -   | [104.7, 4.2]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +6.33 | 00:09:48.588 | Poland             | Spain              | 20 | Pressure        |   -   | [12.4, 61.6]    |                           |  |
|  +6.96 | 00:09:49.221 | Spain              | Spain              | 20 | Shot            |   -   | [103.8, 18.9]   | Saved                     |  |

---

### Case 119: Episode `3788762_p15_8690ffdc`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Actual Opponent: **Spain** (StatsBomb Poss Team: `Poland`)
- **Stratum**: `other` | **First Press Control Candidate**: `Duel`
- **Automated Pathway Classification**: `opponent_dispossessed` | v2.6 Evidence: `duel_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.74 | 00:05:14.563 | Poland             | Poland             | 15 | Ball Receipt*   |   -   | [53.7, 72.0]    | Controlled Receipt        |  |
|  -2.74 | 00:05:14.563 | Poland             | Poland             | 15 | Carry           |   -   | [53.7, 72.0]    | Carry                     |  |
|  -2.70 | 00:05:14.603 | Poland             | Poland             | 15 | Pass            |   -   | [53.7, 72.0]    | Incomplete (Incomplete)   |  |
|  -1.24 | 00:05:16.068 | Poland             | Poland             | 15 | Pressure        |   -   | [40.9, 56.2]    |                           |  |
|  -0.68 | 00:05:16.626 | Poland             | Poland             | 15 | Ball Receipt*   |   -   | [40.9, 55.8]    | Incomplete Receipt (Incomplete) |  |
|  -0.68 | 00:05:16.626 | Spain              | Poland             | 15 | Pass            |   -   | [78.3, 19.8]    | -> Jorge Resurrec         |  |
|  -0.07 | 00:05:17.231 | Spain              | Poland             | 15 | Ball Receipt*   |   -   | [71.1, 25.0]    | Controlled Receipt        |  |
|  -0.07 | 00:05:17.231 | Spain              | Poland             | 15 | Carry           |   -   | [71.1, 25.0]    | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:05:17.306 | Poland             | Poland             | 15 | Pressure        |  Yes  | [50.1, 55.4]    |                           | **CP INITIATION** |
|  +0.83 | 00:05:18.133 | Spain              | Poland             | 15 | Dispossessed    |   -   | [75.1, 25.8]    | Dispossessed              |  |
|  +0.83 | 00:05:18.133 | Poland             | Poland             | 15 | Duel            |  Yes  | [45.0, 54.3]    | Tackle, Won               | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +0.83 | 00:05:18.133 | Poland             | Poland             | 15 | Carry           |   -   | [45.0, 54.3]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.22 | 00:05:19.523 | Poland             | Poland             | 15 | Pass            |   -   | [36.0, 50.2]    | -> Tymoteusz Puch         |  |
|  +3.63 | 00:05:20.941 | Poland             | Poland             | 15 | Ball Receipt*   |   -   | [28.1, 23.1]    | Controlled Receipt        |  |
|  +3.63 | 00:05:20.941 | Poland             | Poland             | 15 | Carry           |   -   | [28.1, 23.1]    | Carry                     |  |
|  +5.46 | 00:05:22.761 | Spain              | Poland             | 15 | Pressure        |   -   | [82.4, 59.8]    |                           |  |

---

### Case 120: Episode `3788762_p8_c1af8a76`
- **Match**: `3788762` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Actual Opponent: **Poland** (StatsBomb Poss Team: `Spain`)
- **Stratum**: `other` | **First Press Control Candidate**: `Ball Recovery`
- **Automated Pathway Classification**: `contested_duel` | v2.6 Evidence: `ball_recovery_plus_carry`
- **Affected by Same-Team Annotation**: `Yes`

```text
Human Review Evaluation:
  human_transition_occurred: 
  human_control_established: 
  human_regain_within_5s:    
  human_notes:               
```

| Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details | Tactical Marker |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
|  -2.55 | 00:01:25.857 | Poland             | Poland             | 7 | Ball Recovery   |   -   | [107.8, 71.8]   |                           |  |
|  -2.55 | 00:01:25.857 | Poland             | Poland             | 7 | Carry           |   -   | [107.8, 71.8]   | Carry                     |  |
|  -2.00 | 00:01:26.404 | Poland             | Poland             | 7 | Pass            |   -   | [105.3, 73.3]   | -> Karol Świdersk         |  |
|  -1.61 | 00:01:26.799 | Poland             | Poland             | 7 | Ball Receipt*   |   -   | [111.3, 66.9]   | Controlled Receipt        |  |
|  -1.61 | 00:01:26.799 | Poland             | Poland             | 7 | Carry           |   -   | [111.3, 66.9]   | Carry                     |  |
|  -1.43 | 00:01:26.979 | Spain              | Poland             | 7 | Pressure        |   -   | [10.3, 13.6]    |                           |  |
|  -1.24 | 00:01:27.166 | Poland             | Poland             | 7 | Pass            |   -   | [112.3, 65.4]   | -> Piotr Zielińsk         |  |
|  -0.72 | 00:01:27.689 | Spain              | Poland             | 7 | Pressure        |   -   | [13.1, 20.0]    |                           |  |
|  -0.51 | 00:01:27.897 | Poland             | Poland             | 7 | Ball Receipt*   |   -   | [104.6, 61.1]   | Controlled Receipt        |  |
|  -0.51 | 00:01:27.897 | Poland             | Poland             | 7 | Carry           |   -   | [104.6, 61.1]   | Carry                     | **OPPONENT LAST CONTROL** |
|  +0.00 | 00:01:28.405 | Poland             | Poland             | 7 | Dispossessed    |   -   | [106.8, 57.1]   | Dispossessed              |  |
|  +0.00 | 00:01:28.405 | Spain              | Spain              | 8 | Duel            |  Yes  | [13.3, 23.0]    | Tackle, Success In Play   | **CP INITIATION** |
|  +0.87 | 00:01:29.275 | Spain              | Spain              | 8 | Ball Recovery   |   -   | [13.3, 23.9]    |                           | **POSSIBLE TRANSITION** | (v2.6 Regain Event) |
|  +0.87 | 00:01:29.275 | Spain              | Spain              | 8 | Carry           |   -   | [13.3, 23.9]    | Carry                     | **PRESSING-TEAM FIRST CONTROL** |
|  +2.26 | 00:01:30.664 | Poland             | Spain              | 8 | Pressure        |  Yes  | [98.4, 59.6]    |                           |  |
|  +2.64 | 00:01:31.046 | Poland             | Spain              | 8 | Pressure        |  Yes  | [97.8, 63.3]    |                           |  |
|  +4.08 | 00:01:32.482 | Poland             | Spain              | 8 | Pressure        |  Yes  | [96.2, 69.5]    |                           |  |
|  +4.91 | 00:01:33.319 | Spain              | Spain              | 8 | Pass            |   -   | [14.0, 10.6]    | -> Gerard Moreno          |  |
|  +6.31 | 00:01:34.710 | Poland             | Spain              | 8 | Pressure        |   -   | [84.3, 26.9]    |                           |  |
|  +6.93 | 00:01:35.335 | Spain              | Spain              | 8 | Ball Receipt*   |   -   | [33.6, 55.8]    | Controlled Receipt        |  |
|  +6.93 | 00:01:35.335 | Spain              | Spain              | 8 | Carry           |   -   | [33.6, 55.8]    | Carry                     |  |
|  -1.31 | 00:01:27.096 | Spain              | Spain              | 81 | Pass            |   -   | [15.7, 68.3]    | -> Unai Simón Men         |  |
|  +0.20 | 00:01:28.607 | Spain              | Spain              | 81 | Ball Receipt*   |   -   | [3.4, 51.9]     | Controlled Receipt        |  |
|  +0.20 | 00:01:28.607 | Spain              | Spain              | 81 | Carry           |   -   | [3.4, 51.9]     | Carry                     |  |
|  +1.78 | 00:01:30.186 | Spain              | Spain              | 81 | Pass            |   -   | [4.4, 45.9]     | -> Pau Francisco          |  |
|  +3.55 | 00:01:31.953 | Spain              | Spain              | 81 | Ball Receipt*   |   -   | [3.4, 23.9]     | Controlled Receipt        |  |
|  +3.55 | 00:01:31.953 | Spain              | Spain              | 81 | Carry           |   -   | [3.4, 23.9]     | Carry                     |  |
|  +4.95 | 00:01:33.360 | Poland             | Spain              | 81 | Pressure        |   -   | [111.2, 58.1]   |                           |  |
|  +5.59 | 00:01:33.997 | Spain              | Spain              | 81 | Pass            |   -   | [5.3, 12.6]     | Incomplete (Incomplete)   |  |
|  +7.38 | 00:01:35.785 | Spain              | Spain              | 81 | Ball Receipt*   |   -   | [40.1, 9.2]     | Incomplete Receipt (Incomplete) |  |
|  +7.38 | 00:01:35.785 | Poland             | Spain              | 81 | Interception    |   -   | [82.9, 70.9]    | Success In Play           |  |

---
