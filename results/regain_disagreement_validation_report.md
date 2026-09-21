# Counterpress Regain Label Disagreement Validation Report (100 Cases)

This document contains full chronological event traces for **100 disagreement episodes** between:
1. `regain_5s_possession_annotation` (StatsBomb possession_team annotation)
2. `regain_5s_controlled` (Evidence-based controlled possession regain)

### Sample Stratification:
- **False-Positive Candidates (`annotation=1, controlled=0`)**: 50 cases (prioritizing primary cohort)
- **False-Negative Candidates (`annotation=0, controlled=1`)**: 50 cases (prioritizing primary cohort)

> [!IMPORTANT]
> **Human Review Fields**: All human verification columns remain strictly unpopulated pending expert review.

---

### Disagreement Case 1: `3857284_p133_5d804ddb`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3857284 (FIFA World Cup, 2022)
- **counterpressing_team**: Japan
- **opponent_team_at_turnover**: Germany
- **possession_team_at_counterpress_initiation**: Japan
- **possession_id_at_counterpress_initiation**: 133
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:26:54.157) | **Initiation**: Duel (00:26:54.157)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.138s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.78 |  -1.78 | 00:26:52.375 | Germany            | Germany            | 132 | Pass            |   -   | [68.9, 24.3]    | -> Joshua Kimmich |
|  -0.94 |  -0.94 | 00:26:53.218 | Germany            | Germany            | 132 | Ball Receipt*   |   -   | [69.8, 14.7]    |  |
|  -0.94 |  -0.94 | 00:26:53.218 | Germany            | Germany            | 132 | Carry           |   -   | [69.8, 14.7]    |  |
|  -0.68 |  -0.68 | 00:26:53.472 | Japan              | Germany            | 132 | Pressure        |   -   | [55.2, 67.7]    |  |
|  +0.00 |  +0.00 | 00:26:54.157 | Germany            | Germany            | 132 | Dispossessed    |   -   | [69.3, 13.4]    |  |
|  +0.00 |  +0.00 | 00:26:54.157 | Japan              | Japan              | 133 | Duel            |  Yes  | [50.8, 66.7]    | Tackle, Success In Play |
|  +1.14 |  +1.14 | 00:26:55.295 | Germany            | Japan              | 133 | Pressure        |  Yes  | [74.5, 15.6]    |  |
|  +1.73 |  +1.73 | 00:26:55.886 | Germany            | Japan              | 133 | Foul Committed  |  Yes  | [71.9, 18.8]    |  |
|  +1.73 |  +1.73 | 00:26:55.886 | Japan              | Japan              | 133 | Foul Won        |   -   | [48.2, 61.3]    |  |
| +24.45 | +24.45 | 00:27:18.607 | Japan              | Japan              | 134 | Pass            |   -   | [51.2, 61.8]    | -> Wataru Endo |
| +25.97 | +25.97 | 00:27:20.130 | Japan              | Japan              | 134 | Ball Receipt*   |   -   | [54.6, 40.4]    |  |
| +27.01 | +27.01 | 00:27:21.169 | Japan              | Japan              | 134 | Pass            |   -   | [57.8, 38.2]    | -> Kaoru Mitoma |
| +31.04 | +31.04 | 00:27:25.200 | Japan              | Japan              | 134 | Ball Receipt*   |   -   | [104.9, 3.1]    |  |
| +34.67 | +34.67 | 00:27:28.823 | Japan              | Japan              | 134 | Pass            |   -   | [107.2, 8.9]    | -> Takehiro Tomiy |
| +36.66 | +36.66 | 00:27:30.819 | Japan              | Japan              | 134 | Ball Receipt*   |   -   | [92.5, 13.4]    |  |
| +36.66 | +36.66 | 00:27:30.819 | Japan              | Japan              | 134 | Pass            |   -   | [92.5, 13.4]    | -> Daichi Kamada |
| +37.53 | +37.53 | 00:27:31.685 | Japan              | Japan              | 134 | Ball Receipt*   |   -   | [93.3, 22.6]    |  |

---

### Disagreement Case 2: `3869552_p5_0203d72a`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3869552 (FIFA World Cup, 2022)
- **counterpressing_team**: France
- **opponent_team_at_turnover**: Morocco
- **possession_team_at_counterpress_initiation**: France
- **possession_id_at_counterpress_initiation**: 5
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:03:32.089) | **Initiation**: Duel (00:03:32.089)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.868s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 8.74s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.43 |  -3.43 | 00:03:28.661 | Morocco            | Morocco            | 4 | Pass            |   -   | [31.9, 46.3]    | -> Hakim Ziyech |
|  -1.94 |  -1.94 | 00:03:30.149 | Morocco            | Morocco            | 4 | Ball Receipt*   |   -   | [47.5, 71.2]    |  |
|  -1.94 |  -1.94 | 00:03:30.149 | Morocco            | Morocco            | 4 | Carry           |   -   | [47.5, 71.2]    |  |
|  -1.61 |  -1.61 | 00:03:30.479 | France             | Morocco            | 4 | Pressure        |   -   | [67.3, 4.5]     |  |
|  +0.00 |  +0.00 | 00:03:32.089 | Morocco            | Morocco            | 4 | Dribble         |   -   | [60.9, 76.3]    |  |
|  +0.00 |  +0.00 | 00:03:32.089 | France             | France             | 5 | Duel            |  Yes  | [59.2, 3.8]     | Tackle, Won |
|  +0.87 |  +0.87 | 00:03:32.957 | Morocco            | France             | 5 | Duel            |  Yes  | [63.6, 77.9]    | Aerial Lost |
|  +0.87 |  +0.87 | 00:03:32.957 | France             | France             | 5 | Pass            |   -   | [56.5, 2.2]     | Incomplete (Incomplete) |
|  +2.11 |  +2.11 | 00:03:34.197 | France             | France             | 5 | Duel            |  Yes  | [58.2, 1.6]     | Aerial Lost |
|  +2.11 |  +2.11 | 00:03:34.197 | Morocco            | France             | 5 | Pass            |   -   | [61.9, 78.5]    | Incomplete (Out) |
|  +3.48 |  +3.48 | 00:03:35.572 | Morocco            | France             | 5 | Ball Receipt*   |   -   | [55.1, 79.0]    | Incomplete |
|  +8.74 |  +8.74 | 00:03:40.829 | France             | France             | 6 | Pass            |   -   | [61.1, 0.1]     | -> Aurélien Djani |
| +10.08 | +10.08 | 00:03:42.170 | France             | France             | 6 | Ball Receipt*   |   -   | [51.2, 12.7]    |  |
| +10.08 | +10.08 | 00:03:42.170 | France             | France             | 6 | Carry           |   -   | [51.2, 12.7]    |  |
| +11.57 | +11.57 | 00:03:43.655 | France             | France             | 6 | Pass            |   -   | [51.2, 12.7]    | -> Ibrahima Konat |
| +13.42 | +13.42 | 00:03:45.507 | France             | France             | 6 | Ball Receipt*   |   -   | [35.4, 7.2]     |  |
| +13.42 | +13.42 | 00:03:45.507 | France             | France             | 6 | Carry           |   -   | [35.4, 7.2]     |  |

---

### Disagreement Case 3: `3869152_p13_cee3cdc9`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3869152 (FIFA World Cup, 2022)
- **counterpressing_team**: Poland
- **opponent_team_at_turnover**: France
- **possession_team_at_counterpress_initiation**: Poland
- **possession_id_at_counterpress_initiation**: 13
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:04:40.544) | **Initiation**: Duel (00:04:40.544)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.971s) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.156s) | Evidence: `completed_pass` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.96 |  -2.96 | 00:04:37.580 | France             | France             | 12 | Pass            |   -   | [37.7, 0.1]     | -> Kylian Mbappé  |
|  -1.41 |  -1.41 | 00:04:39.136 | France             | France             | 12 | Ball Receipt*   |   -   | [53.6, 8.0]     |  |
|  -1.41 |  -1.41 | 00:04:39.136 | France             | France             | 12 | Carry           |   -   | [53.6, 8.0]     |  |
|  -0.78 |  -0.78 | 00:04:39.761 | Poland             | France             | 12 | Pressure        |   -   | [66.5, 72.1]    |  |
|  +0.00 |  +0.00 | 00:04:40.544 | France             | France             | 12 | Dispossessed    |   -   | [53.6, 8.0]     |  |
|  +0.00 |  +0.00 | 00:04:40.544 | Poland             | Poland             | 13 | Duel            |  Yes  | [66.5, 72.1]    | Tackle, Success In Play |
|  +0.97 |  +0.97 | 00:04:41.515 | Poland             | Poland             | 13 | Pass            |   -   | [71.8, 72.1]    | Incomplete (Incomplete) |
|  +1.80 |  +1.80 | 00:04:42.342 | Poland             | Poland             | 13 | Ball Receipt*   |   -   | [100.5, 68.4]   | Incomplete |
|  +1.80 |  +1.80 | 00:04:42.342 | France             | Poland             | 13 | Interception    |  Yes  | [24.0, 8.5]     | Lost In Play |
|  +2.54 |  +2.54 | 00:04:43.082 | France             | Poland             | 13 | Pressure        |  Yes  | [29.8, 12.1]    |  |
|  +2.69 |  +2.69 | 00:04:43.233 | Poland             | Poland             | 13 | Pass            |   -   | [84.6, 65.7]    | Incomplete (Incomplete) |
|  +3.16 |  +3.16 | 00:04:43.703 | Poland             | Poland             | 13 | Ball Receipt*   |   -   | [104.8, 71.0]   | Incomplete |
|  +3.16 |  +3.16 | 00:04:43.703 | France             | Poland             | 13 | Block           |  Yes  | [27.3, 11.9]    |  |
|  +4.45 |  +4.45 | 00:04:44.998 | France             | Poland             | 13 | Pass            |   -   | [26.5, 8.5]     | Incomplete (Incomplete) |
|  +5.16 |  +5.16 | 00:04:45.700 | Poland             | Poland             | 13 | Pass            |   -   | [79.3, 70.6]    | -> Jakub Kamiński |
|  +6.69 |  +6.69 | 00:04:47.238 | Poland             | Poland             | 13 | Ball Receipt*   |   -   | [77.7, 70.0]    |  |
|  +6.69 |  +6.69 | 00:04:47.238 | Poland             | Poland             | 13 | Pass            |   -   | [98.1, 71.0]    | -> Robert Lewando |
|  +7.42 |  +7.42 | 00:04:47.968 | France             | Poland             | 13 | Pressure        |   -   | [24.9, 14.0]    |  |
|  +7.73 |  +7.73 | 00:04:48.273 | Poland             | Poland             | 13 | Ball Receipt*   |   -   | [96.3, 65.9]    |  |
|  +7.73 |  +7.73 | 00:04:48.273 | Poland             | Poland             | 13 | Carry           |   -   | [96.3, 65.9]    |  |
|  +8.01 |  +8.01 | 00:04:48.555 | Poland             | Poland             | 13 | Dispossessed    |   -   | [92.4, 67.6]    |  |
|  +8.01 |  +8.01 | 00:04:48.555 | France             | Poland             | 13 | Duel            |   -   | [27.7, 12.5]    | Tackle, Lost In Play |
| +10.39 | +10.39 | 00:04:50.935 | Poland             | Poland             | 13 | Ball Recovery   |   -   | [86.7, 72.1]    |  |
| +10.39 | +10.39 | 00:04:50.935 | Poland             | Poland             | 13 | Carry           |   -   | [86.7, 72.1]    |  |

---

### Disagreement Case 4: `3857300_p92_f1cf8d0d`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3857300 (FIFA World Cup, 2022)
- **counterpressing_team**: Argentina
- **opponent_team_at_turnover**: Saudi Arabia
- **possession_team_at_counterpress_initiation**: Argentina
- **possession_id_at_counterpress_initiation**: 92
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:10:06.364) | **Initiation**: Duel (00:10:06.364)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.337s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.125s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.33 |  -3.33 | 00:10:03.035 | Saudi Arabia       | Saudi Arabia       | 91 | Duel            |   -   | [70.9, 68.6]    | Aerial Lost |
|  -2.30 |  -2.30 | 00:10:04.065 | Saudi Arabia       | Saudi Arabia       | 91 | Ball Recovery   |   -   | [75.6, 57.0]    |  |
|  -2.30 |  -2.30 | 00:10:04.065 | Saudi Arabia       | Saudi Arabia       | 91 | Carry           |   -   | [75.6, 57.0]    |  |
|  -0.44 |  -0.44 | 00:10:05.926 | Argentina          | Saudi Arabia       | 91 | Pressure        |   -   | [41.1, 22.6]    |  |
|  +0.00 |  +0.00 | 00:10:06.364 | Saudi Arabia       | Saudi Arabia       | 91 | Dispossessed    |   -   | [81.6, 58.8]    |  |
|  +0.00 |  +0.00 | 00:10:06.364 | Argentina          | Argentina          | 92 | Duel            |  Yes  | [38.5, 21.3]    | Tackle, Success In Play |
|  +0.34 |  +0.34 | 00:10:06.701 | Saudi Arabia       | Argentina          | 92 | Foul Committed  |  Yes  | [84.8, 57.9]    |  |
|  +0.34 |  +0.34 | 00:10:06.701 | Argentina          | Argentina          | 92 | Foul Won        |   -   | [35.3, 22.2]    |  |
|  +6.12 |  +6.12 | 00:10:12.489 | Argentina          | Argentina          | 93 | Pass            |   -   | [34.3, 21.3]    | -> Lautaro Javier |
|  +7.03 |  +7.03 | 00:10:13.391 | Argentina          | Argentina          | 93 | Ball Receipt*   |   -   | [44.5, 33.8]    |  |
|  +7.59 |  +7.59 | 00:10:13.951 | Saudi Arabia       | Argentina          | 93 | Pressure        |   -   | [74.9, 47.8]    |  |
|  +7.97 |  +7.97 | 00:10:14.332 | Saudi Arabia       | Argentina          | 93 | Foul Committed  |   -   | [74.9, 46.8]    |  |
|  +7.97 |  +7.97 | 00:10:14.332 | Argentina          | Argentina          | 93 | Foul Won        |   -   | [45.2, 33.3]    |  |
| +20.31 | +20.31 | 00:10:26.676 | Argentina          | Argentina          | 94 | Pass            |   -   | [45.2, 33.3]    | -> Cristian Gabri |
| +22.53 | +22.53 | 00:10:28.894 | Argentina          | Argentina          | 94 | Ball Receipt*   |   -   | [39.6, 50.9]    |  |
| +22.53 | +22.53 | 00:10:28.894 | Argentina          | Argentina          | 94 | Carry           |   -   | [39.6, 50.9]    |  |
| +23.62 | +23.62 | 00:10:29.984 | Argentina          | Argentina          | 94 | Pass            |   -   | [39.6, 50.9]    | -> Leandro Daniel |

---

### Disagreement Case 5: `3773587_p123_004f5ac8`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3773587 (La Liga, 2020/2021)
- **counterpressing_team**: Getafe
- **opponent_team_at_turnover**: Barcelona
- **possession_team_at_counterpress_initiation**: Getafe
- **possession_id_at_counterpress_initiation**: 123
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:36:32.261) | **Initiation**: Duel (00:36:32.261)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.44s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.45 |  -2.45 | 00:36:29.807 | Barcelona          | Barcelona          | 122 | Pass            |   -   | [87.1, 2.8]     | -> Sergino Dest |
|  -1.89 |  -1.89 | 00:36:30.371 | Barcelona          | Barcelona          | 122 | Ball Receipt*   |   -   | [82.7, 11.4]    |  |
|  -1.89 |  -1.89 | 00:36:30.371 | Barcelona          | Barcelona          | 122 | Carry           |   -   | [82.7, 11.4]    |  |
|  -0.52 |  -0.52 | 00:36:31.738 | Getafe             | Barcelona          | 122 | Pressure        |   -   | [36.6, 70.2]    |  |
|  +0.00 |  +0.00 | 00:36:32.261 | Barcelona          | Barcelona          | 122 | Dribble         |   -   | [85.9, 8.7]     |  |
|  +0.00 |  +0.00 | 00:36:32.261 | Getafe             | Getafe             | 123 | Duel            |  Yes  | [34.2, 71.4]    | Tackle, Success In Play |
|  +1.44 |  +1.44 | 00:36:33.701 | Getafe             | Getafe             | 123 | Pass            |   -   | [26.6, 71.6]    | Incomplete (Incomplete) |
|  +1.47 |  +1.47 | 00:36:33.726 | Barcelona          | Getafe             | 123 | Block           |  Yes  | [91.9, 8.3]     |  |
| +38.52 | +38.52 | 00:37:10.783 | Getafe             | Getafe             | 124 | Pass            |   -   | [42.1, 80.0]    | -> Enes Ünal |
| +40.17 | +40.17 | 00:37:12.431 | Getafe             | Getafe             | 124 | Ball Receipt*   |   -   | [55.2, 74.0]    |  |
| +40.18 | +40.18 | 00:37:12.438 | Getafe             | Getafe             | 124 | Pass            |   -   | [55.2, 74.0]    | -> Juan Camilo He |
| +40.85 | +40.85 | 00:37:13.111 | Barcelona          | Getafe             | 124 | Pressure        |   -   | [53.6, 10.1]    |  |
| +40.90 | +40.90 | 00:37:13.159 | Getafe             | Getafe             | 124 | Ball Receipt*   |   -   | [65.1, 70.2]    |  |
| +40.90 | +40.90 | 00:37:13.159 | Getafe             | Getafe             | 124 | Carry           |   -   | [65.1, 70.2]    |  |
| +41.62 | +41.62 | 00:37:13.877 | Getafe             | Getafe             | 124 | Pass            |   -   | [65.1, 70.4]    | Incomplete (Incomplete) |
| +42.59 | +42.59 | 00:37:14.851 | Getafe             | Getafe             | 124 | Pressure        |   -   | [70.2, 75.3]    |  |
| +43.27 | +43.27 | 00:37:15.533 | Getafe             | Getafe             | 124 | Ball Receipt*   |   -   | [71.8, 74.8]    | Incomplete |

---

### Disagreement Case 6: `3773585_p142_07211243`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3773585 (La Liga, 2020/2021)
- **counterpressing_team**: Barcelona
- **opponent_team_at_turnover**: Real Madrid
- **possession_team_at_counterpress_initiation**: Barcelona
- **possession_id_at_counterpress_initiation**: 142
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:32:03.544) | **Initiation**: Duel (00:32:03.544)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 4.808s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.014s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.63 |  -2.63 | 00:32:00.916 | Barcelona          | Real Madrid        | 141 | Duel            |  Yes  | [70.0, 23.1]    | Tackle, Lost In Play |
|  -1.70 |  -1.70 | 00:32:01.849 | Real Madrid        | Real Madrid        | 141 | Ball Recovery   |   -   | [50.6, 60.0]    |  |
|  -1.70 |  -1.70 | 00:32:01.849 | Real Madrid        | Real Madrid        | 141 | Carry           |   -   | [50.6, 60.0]    |  |
|  -0.82 |  -0.82 | 00:32:02.724 | Barcelona          | Real Madrid        | 141 | Pressure        |  Yes  | [66.0, 20.1]    |  |
|  +0.00 |  +0.00 | 00:32:03.544 | Real Madrid        | Real Madrid        | 141 | Dispossessed    |   -   | [59.1, 60.6]    |  |
|  +0.00 |  +0.00 | 00:32:03.544 | Barcelona          | Barcelona          | 142 | Duel            |  Yes  | [61.0, 19.5]    | Tackle, Success In Play |
|  +4.81 |  +4.81 | 00:32:08.352 | Real Madrid        | Barcelona          | 142 | Pressure        |  Yes  | [98.3, 69.0]    |  |
|  +5.01 |  +5.01 | 00:32:08.558 | Barcelona          | Barcelona          | 142 | Ball Recovery   |   -   | [22.3, 8.7]     |  |
|  +5.01 |  +5.01 | 00:32:08.558 | Barcelona          | Barcelona          | 142 | Carry           |   -   | [22.3, 8.7]     |  |
|  +7.49 |  +7.49 | 00:32:11.032 | Barcelona          | Barcelona          | 142 | Pass            |   -   | [31.5, 8.2]     | -> Jordi Alba Ram |
|  +8.86 |  +8.86 | 00:32:12.406 | Barcelona          | Barcelona          | 142 | Ball Receipt*   |   -   | [45.8, 13.7]    |  |
|  +8.86 |  +8.86 | 00:32:12.406 | Barcelona          | Barcelona          | 142 | Carry           |   -   | [45.8, 13.7]    |  |
|  +9.97 |  +9.97 | 00:32:13.516 | Barcelona          | Barcelona          | 142 | Pass            |   -   | [45.8, 13.7]    | -> Frenkie de Jon |
| +11.79 | +11.79 | 00:32:15.337 | Barcelona          | Barcelona          | 142 | Ball Receipt*   |   -   | [56.6, 9.3]     |  |
| +11.79 | +11.79 | 00:32:15.337 | Barcelona          | Barcelona          | 142 | Carry           |   -   | [56.6, 9.3]     |  |
| +15.38 | +15.38 | 00:32:18.926 | Barcelona          | Barcelona          | 142 | Pass            |   -   | [70.4, 11.1]    | -> Sergio Busquet |
| +16.59 | +16.59 | 00:32:20.133 | Barcelona          | Barcelona          | 142 | Ball Receipt*   |   -   | [63.3, 20.1]    |  |

---

### Disagreement Case 7: `3773661_p38_63267f23`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3773661 (La Liga, 2020/2021)
- **counterpressing_team**: Getafe
- **opponent_team_at_turnover**: Barcelona
- **possession_team_at_counterpress_initiation**: Getafe
- **possession_id_at_counterpress_initiation**: 38
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:27:11.698) | **Initiation**: Duel (00:27:11.698)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 2.182s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.22 |  -4.22 | 00:27:07.479 | Barcelona          | Barcelona          | 37 | Ball Receipt*   |   -   | [51.9, 39.2]    |  |
|  -4.22 |  -4.22 | 00:27:07.479 | Barcelona          | Barcelona          | 37 | Carry           |   -   | [51.9, 39.2]    |  |
|  -1.60 |  -1.60 | 00:27:10.101 | Getafe             | Barcelona          | 37 | Pressure        |   -   | [54.8, 51.7]    |  |
|  -0.61 |  -0.61 | 00:27:11.087 | Getafe             | Barcelona          | 37 | Pressure        |   -   | [42.9, 58.0]    |  |
|  +0.00 |  +0.00 | 00:27:11.698 | Barcelona          | Barcelona          | 37 | Dribble         |   -   | [76.5, 24.1]    |  |
|  +0.00 |  +0.00 | 00:27:11.698 | Getafe             | Getafe             | 38 | Duel            |  Yes  | [43.6, 56.0]    | Tackle, Success In Play |
|  +2.18 |  +2.18 | 00:27:13.880 | Getafe             | Getafe             | 38 | Pass            |   -   | [16.4, 43.4]    | Incomplete (Unknown) |
|  +5.12 |  +5.12 | 00:27:16.818 | Getafe             | Getafe             | 38 | Ball Receipt*   |   -   | [2.4, 42.8]     | Incomplete |
|  +5.16 |  +5.16 | 00:27:16.858 | Barcelona          | Getafe             | 38 | Own Goal For    |   -   | [104.5, 36.7]   |  |
|  +5.16 |  +5.16 | 00:27:16.858 | Getafe             | Getafe             | 38 | Own Goal Against |   -   | [15.6, 43.4]    |  |
| +61.99 | +61.99 | 00:28:13.688 | Getafe             | Getafe             | 39 | Pass            |   -   | [61.0, 40.1]    | -> Marc Cucurella |
| +63.59 | +63.59 | 00:28:15.288 | Getafe             | Getafe             | 39 | Ball Receipt*   |   -   | [41.9, 6.9]     |  |
| +74.20 | +74.20 | 00:28:25.895 | Getafe             | Getafe             | 39 | Pass            |   -   | [39.5, 5.1]     | Incomplete (Incomplete) |
| +74.93 | +74.93 | 00:28:26.626 | Barcelona          | Getafe             | 39 | Block           |   -   | [77.7, 75.2]    |  |
| +87.82 | +87.82 | 00:28:39.521 | Getafe             | Getafe             | 40 | Pass            |   -   | [73.2, 0.1]     | -> Ángel Luis Rod |
| +89.80 | +89.80 | 00:28:41.500 | Getafe             | Getafe             | 40 | Ball Receipt*   |   -   | [92.3, 5.1]     |  |
| +89.80 | +89.80 | 00:28:41.500 | Barcelona          | Getafe             | 40 | Duel            |   -   | [26.8, 74.0]    | Aerial Lost |

---

### Disagreement Case 8: `3837928_p42_6bc2080f`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837928 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Lyon
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 42
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:19:05.302) | **Initiation**: Duel (00:19:05.302)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.902s) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 9.104s) | Evidence: `completed_pass` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.68 |  -4.68 | 00:19:00.624 | Lyon               | Lyon               | 41 | Pass            |   -   | [51.2, 80.0]    | -> Johann Lepenan |
|  -4.07 |  -4.07 | 00:19:01.228 | Lyon               | Lyon               | 41 | Ball Receipt*   |   -   | [50.3, 69.5]    |  |
|  -4.07 |  -4.07 | 00:19:01.228 | Lyon               | Lyon               | 41 | Carry           |   -   | [50.3, 69.5]    |  |
|  -2.91 |  -2.91 | 00:19:02.396 | Paris Saint-Germai | Lyon               | 41 | Pressure        |   -   | [69.8, 8.7]     |  |
|  +0.00 |  +0.00 | 00:19:05.302 | Lyon               | Lyon               | 41 | Dispossessed    |   -   | [45.2, 63.2]    |  |
|  +0.00 |  +0.00 | 00:19:05.302 | Paris Saint-Germai | Paris Saint-Germai | 42 | Duel            |  Yes  | [74.9, 16.9]    | Tackle, Success In Play |
|  +0.90 |  +0.90 | 00:19:06.204 | Paris Saint-Germai | Paris Saint-Germai | 42 | Pass            |   -   | [73.9, 20.8]    | Incomplete (Incomplete) |
|  +2.19 |  +2.19 | 00:19:07.492 | Paris Saint-Germai | Paris Saint-Germai | 42 | Pressure        |   -   | [86.0, 30.8]    |  |
|  +2.45 |  +2.45 | 00:19:07.747 | Paris Saint-Germai | Paris Saint-Germai | 42 | Ball Receipt*   |   -   | [80.8, 28.5]    | Incomplete |
|  +2.45 |  +2.45 | 00:19:07.747 | Lyon               | Paris Saint-Germai | 42 | Pass            |   -   | [31.0, 51.1]    | Incomplete (Incomplete) |
|  +6.19 |  +6.19 | 00:19:11.489 | Lyon               | Paris Saint-Germai | 42 | Ball Receipt*   |   -   | [61.6, 43.7]    | Incomplete |
|  +6.19 |  +6.19 | 00:19:11.489 | Paris Saint-Germai | Paris Saint-Germai | 42 | Pass            |   -   | [40.0, 34.4]    | Incomplete (Incomplete) |
|  +8.27 |  +8.27 | 00:19:13.570 | Paris Saint-Germai | Paris Saint-Germai | 42 | Pressure        |   -   | [51.6, 45.4]    |  |
|  +8.38 |  +8.38 | 00:19:13.682 | Paris Saint-Germai | Paris Saint-Germai | 42 | Ball Receipt*   |   -   | [46.2, 49.4]    | Incomplete |
|  +8.38 |  +8.38 | 00:19:13.682 | Lyon               | Paris Saint-Germai | 42 | Ball Recovery   |   -   | [65.8, 34.3]    |  |
|  +9.10 |  +9.10 | 00:19:14.406 | Paris Saint-Germai | Paris Saint-Germai | 42 | Pass            |   -   | [47.7, 40.6]    | -> Achraf Hakimi  |
| +10.29 | +10.29 | 00:19:15.588 | Lyon               | Paris Saint-Germai | 42 | Pressure        |   -   | [67.9, 35.5]    |  |

---

### Disagreement Case 9: `3837752_p154_984a69c9`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837752 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: AC Ajaccio
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 154
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:38:08.668) | **Initiation**: Duel (00:38:08.668)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.213s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 14.385s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -5.29 |  -5.29 | 00:38:03.375 | AC Ajaccio         | AC Ajaccio         | 153 | Pass            |   -   | [59.0, 3.6]     | -> Ismaël Chester |
|  -3.91 |  -3.91 | 00:38:04.757 | AC Ajaccio         | AC Ajaccio         | 153 | Ball Receipt*   |   -   | [72.0, 3.0]     |  |
|  -3.91 |  -3.91 | 00:38:04.757 | AC Ajaccio         | AC Ajaccio         | 153 | Carry           |   -   | [72.0, 3.0]     |  |
|  -0.23 |  -0.23 | 00:38:08.442 | Paris Saint-Germai | AC Ajaccio         | 153 | Pressure        |   -   | [24.8, 75.9]    |  |
|  +0.00 |  +0.00 | 00:38:08.668 | AC Ajaccio         | AC Ajaccio         | 153 | Dribble         |   -   | [96.1, 5.6]     |  |
|  +0.00 |  +0.00 | 00:38:08.668 | Paris Saint-Germai | Paris Saint-Germai | 154 | Duel            |  Yes  | [24.0, 74.5]    | Tackle, Success In Play |
|  +0.21 |  +0.21 | 00:38:08.881 | AC Ajaccio         | Paris Saint-Germai | 154 | Foul Committed  |  Yes  | [96.1, 6.3]     |  |
| +14.38 | +14.38 | 00:38:23.053 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [24.0, 73.8]    | -> El Chadaille B |
| +15.50 | +15.50 | 00:38:24.169 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [19.2, 30.6]    |  |
| +15.97 | +15.97 | 00:38:24.642 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [22.2, 25.6]    | -> Juan Bernat Ve |
| +16.98 | +16.98 | 00:38:25.649 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [31.7, 9.0]     |  |
| +16.98 | +16.98 | 00:38:25.649 | Paris Saint-Germai | Paris Saint-Germai | 155 | Carry           |   -   | [31.7, 9.0]     |  |
| +18.26 | +18.26 | 00:38:26.926 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [31.9, 9.0]     | -> El Chadaille B |
| +19.51 | +19.51 | 00:38:28.176 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [23.3, 22.7]    |  |
| +19.51 | +19.51 | 00:38:28.176 | Paris Saint-Germai | Paris Saint-Germai | 155 | Carry           |   -   | [23.3, 22.7]    |  |
| +20.42 | +20.42 | 00:38:29.092 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [24.5, 22.9]    | -> Marco Verratti |
| +21.62 | +21.62 | 00:38:30.286 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [32.0, 36.3]    |  |

---

### Disagreement Case 10: `3837771_p127_99d00347`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837771 (Ligue 1, 2022/2023)
- **counterpressing_team**: Troyes
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Troyes
- **possession_id_at_counterpress_initiation**: 127
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:24:58.253) | **Initiation**: Duel (00:24:58.253)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.798s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.15 |  -2.15 | 00:24:56.098 | Paris Saint-Germai | Paris Saint-Germai | 126 | Pass            |   -   | [98.6, 27.9]    | -> Lionel Andrés  |
|  -1.11 |  -1.11 | 00:24:57.142 | Paris Saint-Germai | Paris Saint-Germai | 126 | Ball Receipt*   |   -   | [100.9, 45.1]   |  |
|  -1.11 |  -1.11 | 00:24:57.142 | Paris Saint-Germai | Paris Saint-Germai | 126 | Carry           |   -   | [100.9, 45.1]   |  |
|  -0.84 |  -0.84 | 00:24:57.415 | Troyes             | Paris Saint-Germai | 126 | Pressure        |   -   | [16.4, 34.2]    |  |
|  +0.00 |  +0.00 | 00:24:58.253 | Paris Saint-Germai | Paris Saint-Germai | 126 | Dribble         |   -   | [103.7, 45.9]   |  |
|  +0.00 |  +0.00 | 00:24:58.253 | Troyes             | Troyes             | 127 | Duel            |  Yes  | [16.4, 34.2]    | Tackle, Success In Play |
|  +1.80 |  +1.80 | 00:25:00.051 | Paris Saint-Germai | Troyes             | 127 | Pressure        |  Yes  | [95.0, 32.7]    |  |
|  +2.32 |  +2.32 | 00:25:00.573 | Paris Saint-Germai | Troyes             | 127 | Foul Committed  |  Yes  | [95.0, 32.7]    |  |
|  +2.32 |  +2.32 | 00:25:00.573 | Troyes             | Troyes             | 127 | Foul Won        |   -   | [25.1, 47.4]    |  |
| +29.91 | +29.91 | 00:25:28.167 | Troyes             | Troyes             | 128 | Pass            |   -   | [26.4, 47.7]    | -> Abdu Conté |
| +33.23 | +33.23 | 00:25:31.478 | Troyes             | Troyes             | 128 | Ball Receipt*   |   -   | [44.5, 10.8]    |  |
| +33.42 | +33.42 | 00:25:31.671 | Troyes             | Troyes             | 128 | Pass            |   -   | [44.0, 7.2]     | -> Yoann Salmier |
| +34.06 | +34.06 | 00:25:32.314 | Troyes             | Troyes             | 128 | Ball Receipt*   |   -   | [31.5, 15.3]    |  |
| +36.53 | +36.53 | 00:25:34.785 | Troyes             | Troyes             | 128 | Pass            |   -   | [32.6, 15.6]    | -> Erik Palmer-Br |
| +38.15 | +38.15 | 00:25:36.404 | Troyes             | Troyes             | 128 | Ball Receipt*   |   -   | [26.1, 29.2]    |  |
| +38.15 | +38.15 | 00:25:36.404 | Troyes             | Troyes             | 128 | Carry           |   -   | [26.1, 29.2]    |  |
| +38.56 | +38.56 | 00:25:36.816 | Troyes             | Troyes             | 128 | Pass            |   -   | [26.1, 29.2]    | -> Rominigue Koua |

---

### Disagreement Case 11: `3802665_p140_eb6d80eb`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3802665 (Ligue 1, 2021/2022)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Montpellier
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 140
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:25:12.294) | **Initiation**: Duel (00:25:12.294)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.495s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.90 |  -0.90 | 00:25:11.397 | Montpellier        | Montpellier        | 139 | Ball Receipt*   |   -   | [65.5, 63.0]    |  |
|  -0.90 |  -0.90 | 00:25:11.397 | Montpellier        | Montpellier        | 139 | Carry           |   -   | [65.5, 63.0]    |  |
|  -0.70 |  -0.70 | 00:25:11.599 | Paris Saint-Germai | Montpellier        | 139 | Pressure        |   -   | [51.8, 17.8]    |  |
|  -0.50 |  -0.50 | 00:25:11.798 | Paris Saint-Germai | Montpellier        | 139 | Pressure        |   -   | [52.9, 12.6]    |  |
|  +0.00 |  +0.00 | 00:25:12.294 | Montpellier        | Montpellier        | 139 | Dispossessed    |   -   | [68.6, 63.7]    |  |
|  +0.00 |  +0.00 | 00:25:12.294 | Paris Saint-Germai | Paris Saint-Germai | 140 | Duel            |  Yes  | [51.5, 16.4]    | Tackle, Success In Play |
|  +0.49 |  +0.49 | 00:25:12.789 | Montpellier        | Paris Saint-Germai | 140 | Foul Committed  |  Yes  | [68.6, 63.8]    |  |
|  +0.49 |  +0.49 | 00:25:12.789 | Paris Saint-Germai | Paris Saint-Germai | 140 | Foul Won        |   -   | [51.5, 16.3]    |  |
| +42.42 | +42.42 | 00:25:54.713 | Paris Saint-Germai | Paris Saint-Germai | 141 | Pass            |   -   | [50.9, 19.9]    | -> Edouard Michut |
| +42.94 | +42.94 | 00:25:55.232 | Paris Saint-Germai | Paris Saint-Germai | 141 | Ball Receipt*   |   -   | [57.0, 20.1]    |  |
| +42.94 | +42.94 | 00:25:55.232 | Paris Saint-Germai | Paris Saint-Germai | 141 | Pass            |   -   | [57.0, 19.9]    | -> Marco Verratti |
| +44.12 | +44.12 | 00:25:56.418 | Montpellier        | Paris Saint-Germai | 141 | Pressure        |   -   | [67.3, 60.6]    |  |
| +44.24 | +44.24 | 00:25:56.533 | Paris Saint-Germai | Paris Saint-Germai | 141 | Ball Receipt*   |   -   | [48.7, 19.2]    |  |
| +44.24 | +44.24 | 00:25:56.533 | Paris Saint-Germai | Paris Saint-Germai | 141 | Carry           |   -   | [48.7, 19.2]    |  |
| +44.60 | +44.60 | 00:25:56.891 | Paris Saint-Germai | Paris Saint-Germai | 141 | Pass            |   -   | [48.5, 19.1]    | -> Marcos Aoás Co |
| +48.86 | +48.86 | 00:26:01.155 | Paris Saint-Germai | Paris Saint-Germai | 141 | Ball Receipt*   |   -   | [28.8, 58.9]    |  |
| +48.86 | +48.86 | 00:26:01.155 | Paris Saint-Germai | Paris Saint-Germai | 141 | Carry           |   -   | [28.8, 58.9]    |  |

---

### Disagreement Case 12: `3802837_p75_67388e33`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3802837 (Ligue 1, 2021/2022)
- **counterpressing_team**: Saint-Étienne
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Saint-Étienne
- **possession_id_at_counterpress_initiation**: 75
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:48:02.638) | **Initiation**: Duel (00:48:02.638)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.572s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.27 |  -2.27 | 00:48:00.366 | Saint-Étienne      | Paris Saint-Germai | 74 | Duel            |   -   | [21.0, 58.2]    | Tackle, Lost In Play |
|  -0.75 |  -0.75 | 00:48:01.892 | Paris Saint-Germai | Paris Saint-Germai | 74 | Ball Recovery   |   -   | [106.2, 21.5]   |  |
|  -0.75 |  -0.75 | 00:48:01.892 | Paris Saint-Germai | Paris Saint-Germai | 74 | Carry           |   -   | [106.2, 21.5]   |  |
|  -0.27 |  -0.27 | 00:48:02.367 | Saint-Étienne      | Paris Saint-Germai | 74 | Pressure        |   -   | [15.0, 58.6]    |  |
|  +0.00 |  +0.00 | 00:48:02.638 | Paris Saint-Germai | Paris Saint-Germai | 74 | Dribble         |   -   | [105.2, 21.5]   |  |
|  +0.00 |  +0.00 | 00:48:02.638 | Saint-Étienne      | Saint-Étienne      | 75 | Duel            |  Yes  | [14.9, 58.6]    | Tackle, Won |
|  +0.57 |  +0.57 | 00:48:03.210 | Paris Saint-Germai | Saint-Étienne      | 75 | Block           |  Yes  | [105.2, 17.3]   |  |
|  +2.08 |  +2.08 | 00:48:04.722 | Saint-Étienne      | Saint-Étienne      | 75 | Half End        |   -   | -               |  |
|  +2.08 |  +2.08 | 00:48:04.722 | Paris Saint-Germai | Saint-Étienne      | 75 | Half End        |   -   | -               |  |
| -2882.64 | -2882.64 | 00:00:00.000 | Saint-Étienne      | Saint-Étienne      | 75 | Half Start      |   -   | -               |  |
| -2882.64 | -2882.64 | 00:00:00.000 | Paris Saint-Germai | Saint-Étienne      | 75 | Half Start      |   -   | -               |  |
| -2882.64 | -2882.64 | 00:00:00.000 | Saint-Étienne      | Saint-Étienne      | 75 | Substitution    |   -   | -               |  |
| -2882.64 | -2882.64 | 00:00:00.000 | Saint-Étienne      | Saint-Étienne      | 75 | Substitution    |   -   | -               |  |
| -2882.43 | -2882.43 | 00:00:00.205 | Saint-Étienne      | Saint-Étienne      | 76 | Pass            |   -   | [61.0, 40.1]    | -> Ryad Boudebouz |
| -2881.76 | -2881.76 | 00:00:00.882 | Saint-Étienne      | Saint-Étienne      | 76 | Ball Receipt*   |   -   | [55.4, 41.2]    |  |
| -2881.76 | -2881.76 | 00:00:00.882 | Saint-Étienne      | Saint-Étienne      | 76 | Carry           |   -   | [55.4, 41.2]    |  |
| -2880.82 | -2880.82 | 00:00:01.817 | Saint-Étienne      | Saint-Étienne      | 76 | Pass            |   -   | [54.8, 40.2]    | -> Denis Bouanga |
| -2878.85 | -2878.85 | 00:00:03.791 | Saint-Étienne      | Saint-Étienne      | 76 | Ball Receipt*   |   -   | [64.5, 5.2]     |  |
| -2878.85 | -2878.85 | 00:00:03.791 | Saint-Étienne      | Saint-Étienne      | 76 | Carry           |   -   | [64.5, 5.2]     |  |
| -2878.54 | -2878.54 | 00:00:04.095 | Paris Saint-Germai | Saint-Étienne      | 76 | Pressure        |   -   | [48.2, 72.5]    |  |
| -2877.70 | -2877.70 | 00:00:04.940 | Saint-Étienne      | Saint-Étienne      | 76 | Dribble         |   -   | [69.0, 4.5]     |  |
| -2877.70 | -2877.70 | 00:00:04.940 | Paris Saint-Germai | Paris Saint-Germai | 77 | Duel            |  Yes  | [51.1, 75.6]    | Tackle, Won |
| -2877.70 | -2877.70 | 00:00:04.940 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [51.1, 75.6]    |  |
| -2876.57 | -2876.57 | 00:00:06.068 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [49.8, 75.5]    | -> Ángel Fabián D |
| -2875.98 | -2875.98 | 00:00:06.657 | Saint-Étienne      | Paris Saint-Germai | 77 | Tactical Shift  |   -   | -               |  |
| -2875.85 | -2875.85 | 00:00:06.784 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [52.6, 75.5]    |  |
| -2875.85 | -2875.85 | 00:00:06.784 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [52.6, 75.5]    |  |
| -2875.62 | -2875.62 | 00:00:07.016 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [54.2, 75.5]    | -> Danilo Luís Hé |
| -2874.75 | -2874.75 | 00:00:07.884 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [46.7, 69.7]    |  |
| -2874.75 | -2874.75 | 00:00:07.884 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [46.7, 69.7]    |  |
| -2872.54 | -2872.54 | 00:00:10.102 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [47.2, 68.3]    | -> Sergio Ramos G |
| -2870.65 | -2870.65 | 00:00:11.988 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [34.0, 26.4]    |  |
| -2870.65 | -2870.65 | 00:00:11.988 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [34.0, 26.4]    |  |
| -2868.65 | -2868.65 | 00:00:13.985 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [48.4, 12.4]    | -> Juan Bernat Ve |
| -2867.01 | -2867.01 | 00:00:15.628 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [64.7, 2.8]     |  |
| -2867.01 | -2867.01 | 00:00:15.628 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [64.7, 2.8]     |  |
| -2866.90 | -2866.90 | 00:00:15.733 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [64.7, 2.8]     | -> Sergio Ramos G |
| -2865.26 | -2865.26 | 00:00:17.378 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [53.1, 6.3]     |  |
| -2865.26 | -2865.26 | 00:00:17.378 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [53.1, 6.3]     |  |
| -2863.74 | -2863.74 | 00:00:18.901 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [54.5, 6.3]     | -> Neymar da Silv |
| -2862.77 | -2862.77 | 00:00:19.866 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [70.0, 11.4]    |  |
| -2862.77 | -2862.77 | 00:00:19.866 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [70.0, 11.4]    | -> Sergio Ramos G |
| -2861.17 | -2861.17 | 00:00:21.467 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [60.7, 10.2]    |  |
| -2861.17 | -2861.17 | 00:00:21.467 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [60.7, 10.2]    |  |
| -2859.82 | -2859.82 | 00:00:22.813 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [57.2, 14.4]    | -> Marcos Aoás Co |
| -2857.23 | -2857.23 | 00:00:25.407 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [57.0, 45.6]    |  |
| -2857.23 | -2857.23 | 00:00:25.407 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [57.0, 45.6]    |  |
| -2855.05 | -2855.05 | 00:00:27.584 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [64.2, 52.5]    | -> Ángel Fabián D |
| -2853.93 | -2853.93 | 00:00:28.710 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [69.8, 64.4]    |  |
| -2853.93 | -2853.93 | 00:00:28.710 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [69.8, 64.4]    |  |
| -2853.11 | -2853.11 | 00:00:29.523 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [69.8, 63.3]    | -> Lionel Andrés  |
| -2850.76 | -2850.76 | 00:00:31.875 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [100.1, 60.0]   |  |
| -2850.76 | -2850.76 | 00:00:31.875 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [100.1, 60.0]   |  |
| -2849.84 | -2849.84 | 00:00:32.797 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [104.0, 68.6]   | -> Achraf Hakimi  |
| -2848.52 | -2848.52 | 00:00:34.116 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [98.2, 76.7]    |  |
| -2848.52 | -2848.52 | 00:00:34.116 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [98.2, 76.7]    |  |
| -2848.35 | -2848.35 | 00:00:34.291 | Saint-Étienne      | Paris Saint-Germai | 77 | Pressure        |   -   | [24.6, 10.1]    |  |
| -2848.05 | -2848.05 | 00:00:34.587 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [98.2, 76.7]    | -> Lionel Andrés  |
| -2847.59 | -2847.59 | 00:00:35.051 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [100.1, 76.4]   |  |
| -2847.59 | -2847.59 | 00:00:35.051 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [100.1, 76.4]   | -> Ángel Fabián D |
| -2846.10 | -2846.10 | 00:00:36.534 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [79.3, 71.1]    |  |
| -2846.10 | -2846.10 | 00:00:36.534 | Paris Saint-Germai | Paris Saint-Germai | 77 | Carry           |   -   | [79.3, 71.1]    |  |
| -2843.62 | -2843.62 | 00:00:39.021 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [78.7, 69.2]    | -> Sergio Ramos G |
| -2841.00 | -2841.00 | 00:00:41.634 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [77.8, 27.4]    |  |
| -2841.00 | -2841.00 | 00:00:41.634 | Paris Saint-Germai | Paris Saint-Germai | 77 | Pass            |   -   | [77.2, 26.7]    | Incomplete (Out) |
| -2838.67 | -2838.67 | 00:00:43.969 | Paris Saint-Germai | Paris Saint-Germai | 77 | Ball Receipt*   |   -   | [98.6, 2.2]     | Incomplete |
| -2827.34 | -2827.34 | 00:00:55.294 | Saint-Étienne      | Saint-Étienne      | 78 | Pass            |   -   | [7.8, 80.0]     | -> Ryad Boudebouz |
| -2826.86 | -2826.86 | 00:00:55.780 | Paris Saint-Germai | Saint-Étienne      | 78 | Pressure        |   -   | [107.3, 7.5]    |  |
| -2826.58 | -2826.58 | 00:00:56.062 | Saint-Étienne      | Saint-Étienne      | 78 | Ball Receipt*   |   -   | [10.8, 73.8]    |  |
| -2826.58 | -2826.58 | 00:00:56.062 | Saint-Étienne      | Saint-Étienne      | 78 | Pass            |   -   | [10.3, 73.8]    | -> Yvann Macon |
| -2825.78 | -2825.78 | 00:00:56.853 | Saint-Étienne      | Saint-Étienne      | 78 | Ball Receipt*   |   -   | [6.9, 77.7]     |  |
| -2825.78 | -2825.78 | 00:00:56.853 | Saint-Étienne      | Saint-Étienne      | 78 | Carry           |   -   | [6.9, 77.7]     |  |
| -2824.84 | -2824.84 | 00:00:57.795 | Saint-Étienne      | Saint-Étienne      | 78 | Pass            |   -   | [6.9, 78.2]     | Incomplete (Incomplete) |
| -2822.98 | -2822.98 | 00:00:59.658 | Saint-Étienne      | Saint-Étienne      | 78 | Ball Receipt*   |   -   | [30.6, 75.7]    | Incomplete |
| -2822.98 | -2822.98 | 00:00:59.658 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |  Yes  | [91.1, 4.2]     | -> Idrissa Gana G |
| -2821.91 | -2821.91 | 00:01:00.728 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [89.5, 11.0]    |  |
| -2821.91 | -2821.91 | 00:01:00.728 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [89.5, 11.0]    |  |
| -2821.29 | -2821.29 | 00:01:01.346 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [88.6, 11.4]    | -> Danilo Luís Hé |
| -2820.48 | -2820.48 | 00:01:02.155 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [82.0, 17.7]    |  |
| -2820.48 | -2820.48 | 00:01:02.155 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [82.0, 17.7]    |  |
| -2819.66 | -2819.66 | 00:01:02.974 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [83.2, 19.9]    | -> Lionel Andrés  |
| -2818.65 | -2818.65 | 00:01:03.986 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [83.7, 37.7]    |  |
| -2818.65 | -2818.65 | 00:01:03.986 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [83.7, 37.7]    |  |
| -2818.26 | -2818.26 | 00:01:04.380 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [83.2, 37.5]    | -> Kylian Mbappé  |
| -2817.90 | -2817.90 | 00:01:04.741 | Saint-Étienne      | Paris Saint-Germai | 79 | Pressure        |   -   | [24.7, 49.8]    |  |
| -2817.44 | -2817.44 | 00:01:05.193 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [95.0, 30.3]    |  |
| -2817.44 | -2817.44 | 00:01:05.193 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [93.1, 30.3]    | -> Lionel Andrés  |
| -2816.98 | -2816.98 | 00:01:05.659 | Saint-Étienne      | Paris Saint-Germai | 79 | Pressure        |   -   | [32.5, 49.1]    |  |
| -2816.83 | -2816.83 | 00:01:05.804 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [85.6, 31.3]    |  |
| -2816.83 | -2816.83 | 00:01:05.804 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [85.6, 31.3]    |  |
| -2815.41 | -2815.41 | 00:01:07.232 | Saint-Étienne      | Paris Saint-Germai | 79 | Dribbled Past   |   -   | [34.5, 49.1]    |  |
| -2815.41 | -2815.41 | 00:01:07.232 | Paris Saint-Germai | Paris Saint-Germai | 79 | Dribble         |   -   | [85.6, 31.0]    |  |
| -2815.41 | -2815.41 | 00:01:07.232 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [85.6, 31.0]    |  |
| -2815.26 | -2815.26 | 00:01:07.383 | Saint-Étienne      | Paris Saint-Germai | 79 | Pressure        |   -   | [29.4, 51.5]    |  |
| -2814.91 | -2814.91 | 00:01:07.728 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [89.2, 27.4]    | -> Juan Bernat Ve |
| -2813.89 | -2813.89 | 00:01:08.746 | Saint-Étienne      | Paris Saint-Germai | 79 | Pressure        |   -   | [18.9, 57.6]    |  |
| -2813.61 | -2813.61 | 00:01:09.028 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [99.5, 19.5]    |  |
| -2813.61 | -2813.61 | 00:01:09.028 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [99.5, 19.5]    |  |
| -2813.47 | -2813.47 | 00:01:09.168 | Paris Saint-Germai | Paris Saint-Germai | 79 | Miscontrol      |   -   | [102.8, 20.8]   |  |
| -2812.59 | -2812.59 | 00:01:10.044 | Saint-Étienne      | Paris Saint-Germai | 79 | Clearance       |   -   | [19.8, 56.0]    |  |
| -2809.69 | -2809.69 | 00:01:12.949 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [73.4, 38.8]    | -> Achraf Hakimi  |
| -2807.13 | -2807.13 | 00:01:15.503 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [70.0, 72.0]    |  |
| -2807.13 | -2807.13 | 00:01:15.503 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [70.0, 72.0]    |  |
| -2806.13 | -2806.13 | 00:01:16.504 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [70.0, 69.1]    | -> Ángel Fabián D |
| -2805.32 | -2805.32 | 00:01:17.316 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [75.3, 60.0]    |  |
| -2805.32 | -2805.32 | 00:01:17.316 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [75.1, 60.0]    | -> Danilo Luís Hé |
| -2803.85 | -2803.85 | 00:01:18.791 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [65.3, 46.1]    |  |
| -2803.85 | -2803.85 | 00:01:18.791 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [65.3, 46.1]    |  |
| -2802.43 | -2802.43 | 00:01:20.209 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [65.0, 42.7]    | -> Idrissa Gana G |
| -2801.17 | -2801.17 | 00:01:21.465 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [70.3, 30.6]    |  |
| -2801.17 | -2801.17 | 00:01:21.465 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [70.3, 30.6]    |  |
| -2800.32 | -2800.32 | 00:01:22.322 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [73.2, 28.8]    | -> Neymar da Silv |
| -2799.47 | -2799.47 | 00:01:23.166 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [80.3, 25.2]    |  |
| -2799.47 | -2799.47 | 00:01:23.166 | Paris Saint-Germai | Paris Saint-Germai | 79 | Carry           |   -   | [80.3, 25.2]    |  |
| -2798.95 | -2798.95 | 00:01:23.688 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [82.5, 24.9]    | Incomplete (Incomplete) |
| -2798.18 | -2798.18 | 00:01:24.460 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [98.1, 26.6]    | Incomplete |
| -2798.18 | -2798.18 | 00:01:24.460 | Saint-Étienne      | Saint-Étienne      | 80 | Pass            |  Yes  | [24.5, 53.5]    | -> Zaydou Youssou |
| -2796.72 | -2796.72 | 00:01:25.920 | Paris Saint-Germai | Saint-Étienne      | 80 | Pressure        |  Yes  | [83.1, 23.8]    |  |
| -2796.50 | -2796.50 | 00:01:26.141 | Saint-Étienne      | Saint-Étienne      | 80 | Ball Receipt*   |   -   | [32.9, 55.7]    |  |
| -2796.50 | -2796.50 | 00:01:26.141 | Saint-Étienne      | Saint-Étienne      | 80 | Carry           |   -   | [32.9, 55.7]    |  |
| -2796.44 | -2796.44 | 00:01:26.198 | Saint-Étienne      | Saint-Étienne      | 80 | Pass            |   -   | [35.1, 57.4]    | -> Ryad Boudebouz |
| -2795.56 | -2795.56 | 00:01:27.081 | Saint-Étienne      | Saint-Étienne      | 80 | Ball Receipt*   |   -   | [36.9, 50.2]    |  |
| -2795.56 | -2795.56 | 00:01:27.081 | Saint-Étienne      | Saint-Étienne      | 80 | Carry           |   -   | [36.9, 50.2]    |  |
| -2794.20 | -2794.20 | 00:01:28.441 | Paris Saint-Germai | Saint-Étienne      | 80 | Pressure        |  Yes  | [84.5, 30.6]    |  |
| -2793.68 | -2793.68 | 00:01:28.959 | Saint-Étienne      | Saint-Étienne      | 80 | Pass            |   -   | [36.2, 47.0]    | -> Denis Bouanga |
| -2791.49 | -2791.49 | 00:01:31.148 | Paris Saint-Germai | Saint-Étienne      | 80 | Pressure        |   -   | [53.7, 61.9]    |  |
| -2790.95 | -2790.95 | 00:01:31.685 | Saint-Étienne      | Saint-Étienne      | 80 | Ball Receipt*   |   -   | [66.9, 15.1]    |  |
| -2790.95 | -2790.95 | 00:01:31.685 | Saint-Étienne      | Saint-Étienne      | 80 | Carry           |   -   | [66.9, 15.1]    |  |
| -2789.66 | -2789.66 | 00:01:32.981 | Paris Saint-Germai | Saint-Étienne      | 80 | Dribbled Past   |   -   | [40.7, 60.3]    |  |
| -2789.66 | -2789.66 | 00:01:32.981 | Saint-Étienne      | Saint-Étienne      | 80 | Dribble         |   -   | [79.4, 19.8]    |  |
| -2789.66 | -2789.66 | 00:01:32.981 | Saint-Étienne      | Saint-Étienne      | 80 | Carry           |   -   | [79.4, 19.8]    |  |
| -2788.76 | -2788.76 | 00:01:33.877 | Paris Saint-Germai | Saint-Étienne      | 80 | Pressure        |   -   | [30.1, 56.1]    |  |
| -2786.40 | -2786.40 | 00:01:36.234 | Saint-Étienne      | Saint-Étienne      | 80 | Shot            |   -   | [108.8, 28.7]   | Off T |
| -2785.97 | -2785.97 | 00:01:36.672 | Paris Saint-Germai | Saint-Étienne      | 80 | Goal Keeper     |   -   | [1.6, 43.0]     |  |
| -2781.75 | -2781.75 | 00:01:40.892 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [6.0, 44.0]     | -> Sergio Ramos G |
| -2780.35 | -2780.35 | 00:01:42.284 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [6.2, 29.9]     |  |
| -2778.52 | -2778.52 | 00:01:44.121 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [11.1, 30.5]    | -> Juan Bernat Ve |
| -2777.07 | -2777.07 | 00:01:45.570 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [25.1, 8.9]     |  |
| -2777.07 | -2777.07 | 00:01:45.570 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [25.1, 8.9]     |  |
| -2774.94 | -2774.94 | 00:01:47.695 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [30.7, 8.1]     | -> Idrissa Gana G |
| -2773.82 | -2773.82 | 00:01:48.817 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [35.4, 21.1]    |  |
| -2773.82 | -2773.82 | 00:01:48.817 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [35.4, 21.1]    |  |
| -2772.97 | -2772.97 | 00:01:49.670 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [37.9, 21.3]    | -> Kylian Mbappé  |
| -2772.10 | -2772.10 | 00:01:50.542 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [48.6, 20.8]    |  |
| -2772.10 | -2772.10 | 00:01:50.542 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [48.6, 20.8]    | -> Juan Bernat Ve |
| -2770.65 | -2770.65 | 00:01:51.989 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [44.5, 3.9]     |  |
| -2770.65 | -2770.65 | 00:01:51.989 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [44.5, 3.9]     |  |
| -2767.90 | -2767.90 | 00:01:54.742 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [48.4, 6.1]     | -> Neymar da Silv |
| -2767.11 | -2767.11 | 00:01:55.531 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [56.8, 3.3]     |  |
| -2767.11 | -2767.11 | 00:01:55.531 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [56.8, 3.3]     |  |
| -2766.96 | -2766.96 | 00:01:55.680 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [56.8, 3.3]     | -> Juan Bernat Ve |
| -2765.44 | -2765.44 | 00:01:57.201 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [53.9, 10.0]    |  |
| -2765.44 | -2765.44 | 00:01:57.201 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [53.9, 10.0]    |  |
| -2765.19 | -2765.19 | 00:01:57.448 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [53.9, 10.8]    | -> Idrissa Gana G |
| -2764.22 | -2764.22 | 00:01:58.417 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [53.1, 19.5]    |  |
| -2764.22 | -2764.22 | 00:01:58.417 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [53.1, 19.5]    |  |
| -2761.93 | -2761.93 | 00:02:00.712 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [54.3, 23.8]    | -> Ángel Fabián D |
| -2760.28 | -2760.28 | 00:02:02.354 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [56.8, 44.1]    |  |
| -2760.28 | -2760.28 | 00:02:02.354 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [56.8, 44.1]    |  |
| -2755.71 | -2755.71 | 00:02:06.930 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [67.6, 45.5]    | -> Juan Bernat Ve |
| -2754.18 | -2754.18 | 00:02:08.453 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [69.3, 18.1]    |  |
| -2754.18 | -2754.18 | 00:02:08.453 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [69.3, 18.1]    |  |
| -2753.37 | -2753.37 | 00:02:09.271 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [69.5, 16.3]    | -> Neymar da Silv |
| -2751.99 | -2751.99 | 00:02:10.653 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [86.2, 4.9]     |  |
| -2751.99 | -2751.99 | 00:02:10.653 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [86.2, 4.9]     |  |
| -2751.09 | -2751.09 | 00:02:11.546 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [86.2, 4.9]     | -> Juan Bernat Ve |
| -2749.42 | -2749.42 | 00:02:13.213 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [75.1, 8.3]     |  |
| -2749.42 | -2749.42 | 00:02:13.213 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [75.1, 8.3]     |  |
| -2747.46 | -2747.46 | 00:02:15.181 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [76.7, 8.5]     | -> Neymar da Silv |
| -2746.59 | -2746.59 | 00:02:16.047 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [83.9, 3.8]     |  |
| -2746.59 | -2746.59 | 00:02:16.047 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [83.9, 3.8]     |  |
| -2743.67 | -2743.67 | 00:02:18.963 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [84.2, 3.8]     | -> Danilo Luís Hé |
| -2742.03 | -2742.03 | 00:02:20.603 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [76.1, 32.0]    |  |
| -2742.03 | -2742.03 | 00:02:20.603 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [76.1, 32.0]    |  |
| -2740.96 | -2740.96 | 00:02:21.675 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [76.7, 36.3]    | -> Lionel Andrés  |
| -2740.08 | -2740.08 | 00:02:22.554 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [77.2, 48.3]    |  |
| -2740.08 | -2740.08 | 00:02:22.554 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [77.2, 48.3]    |  |
| -2738.65 | -2738.65 | 00:02:23.987 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [78.6, 48.0]    | -> Ángel Fabián D |
| -2737.89 | -2737.89 | 00:02:24.745 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [85.9, 48.9]    |  |
| -2737.89 | -2737.89 | 00:02:24.745 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [85.9, 48.9]    |  |
| -2736.44 | -2736.44 | 00:02:26.198 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [90.7, 43.5]    | Incomplete (Incomplete) |
| -2735.05 | -2735.05 | 00:02:27.592 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [106.7, 35.8]   | Incomplete |
| -2735.05 | -2735.05 | 00:02:27.592 | Saint-Étienne      | Paris Saint-Germai | 81 | Interception    |   -   | [15.0, 42.9]    | Lost In Play |
| -2730.51 | -2730.51 | 00:02:32.125 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Recovery   |   -   | [64.0, 72.4]    |  |
| -2730.51 | -2730.51 | 00:02:32.125 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [64.0, 72.4]    |  |
| -2729.07 | -2729.07 | 00:02:33.565 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [69.8, 71.1]    | -> Lionel Andrés  |
| -2727.42 | -2727.42 | 00:02:35.222 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [71.2, 60.0]    |  |
| -2727.42 | -2727.42 | 00:02:35.222 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [71.2, 60.0]    |  |
| -2724.84 | -2724.84 | 00:02:37.794 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [73.9, 52.7]    | -> Juan Bernat Ve |
| -2722.22 | -2722.22 | 00:02:40.414 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [77.0, 7.8]     |  |
| -2722.22 | -2722.22 | 00:02:40.414 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [77.0, 7.8]     |  |
| -2719.24 | -2719.24 | 00:02:43.395 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [76.5, 5.6]     | -> Sergio Ramos G |
| -2717.97 | -2717.97 | 00:02:44.668 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [68.9, 16.0]    |  |
| -2717.97 | -2717.97 | 00:02:44.668 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [68.9, 16.0]    |  |
| -2717.40 | -2717.40 | 00:02:45.239 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [69.5, 12.2]    | -> Idrissa Gana G |
| -2716.49 | -2716.49 | 00:02:46.143 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [79.3, 16.3]    |  |
| -2716.49 | -2716.49 | 00:02:46.143 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [79.3, 16.3]    |  |
| -2714.55 | -2714.55 | 00:02:48.093 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [84.5, 16.6]    | -> Juan Bernat Ve |
| -2713.12 | -2713.12 | 00:02:49.514 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [97.5, 5.0]     |  |
| -2713.12 | -2713.12 | 00:02:49.514 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [97.5, 5.0]     |  |
| -2712.46 | -2712.46 | 00:02:50.177 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [97.5, 5.0]     | -> Neymar da Silv |
| -2711.61 | -2711.61 | 00:02:51.031 | Saint-Étienne      | Paris Saint-Germai | 81 | Pressure        |   -   | [29.2, 65.7]    |  |
| -2711.58 | -2711.58 | 00:02:51.061 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [90.9, 9.5]     |  |
| -2711.58 | -2711.58 | 00:02:51.061 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [90.9, 9.5]     |  |
| -2709.47 | -2709.47 | 00:02:53.164 | Saint-Étienne      | Paris Saint-Germai | 81 | Dribbled Past   |   -   | [18.7, 70.4]    |  |
| -2709.47 | -2709.47 | 00:02:53.164 | Paris Saint-Germai | Paris Saint-Germai | 81 | Dribble         |   -   | [101.4, 9.7]    |  |
| -2709.47 | -2709.47 | 00:02:53.164 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [101.4, 9.7]    |  |
| -2709.14 | -2709.14 | 00:02:53.496 | Saint-Étienne      | Paris Saint-Germai | 81 | Pressure        |   -   | [20.0, 70.6]    |  |
| -2708.72 | -2708.72 | 00:02:53.919 | Paris Saint-Germai | Paris Saint-Germai | 81 | Dribble         |   -   | [105.3, 10.0]   |  |
| -2708.72 | -2708.72 | 00:02:53.919 | Saint-Étienne      | Paris Saint-Germai | 81 | Duel            |   -   | [14.8, 70.1]    | Tackle, Lost Out |
| -2698.18 | -2698.18 | 00:03:04.459 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [98.6, 0.1]     | -> Sergio Ramos G |
| -2697.18 | -2697.18 | 00:03:05.453 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [90.3, 7.8]     |  |
| -2697.18 | -2697.18 | 00:03:05.453 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [90.3, 7.8]     |  |
| -2697.11 | -2697.11 | 00:03:05.526 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [30.6, 70.1]    |  |
| -2696.53 | -2696.53 | 00:03:06.103 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [91.7, 5.6]     | -> Neymar da Silv |
| -2696.22 | -2696.22 | 00:03:06.417 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [20.0, 72.0]    |  |
| -2695.90 | -2695.90 | 00:03:06.741 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [98.6, 7.5]     |  |
| -2695.90 | -2695.90 | 00:03:06.741 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [98.7, 8.1]     | -> Danilo Luís Hé |
| -2694.27 | -2694.27 | 00:03:08.368 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [79.2, 14.1]    |  |
| -2694.27 | -2694.27 | 00:03:08.368 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [79.2, 14.1]    |  |
| -2692.99 | -2692.99 | 00:03:09.652 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [77.0, 14.4]    | -> Lionel Andrés  |
| -2691.98 | -2691.98 | 00:03:10.658 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [83.7, 30.3]    |  |
| -2691.98 | -2691.98 | 00:03:10.658 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [83.7, 30.3]    |  |
| -2691.37 | -2691.37 | 00:03:11.267 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [83.7, 30.3]    | -> Ángel Fabián D |
| -2690.70 | -2690.70 | 00:03:11.936 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [92.8, 36.0]    |  |
| -2690.70 | -2690.70 | 00:03:11.936 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [92.8, 36.0]    |  |
| -2690.28 | -2690.28 | 00:03:12.355 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [91.8, 35.8]    | -> Lionel Andrés  |
| -2689.21 | -2689.21 | 00:03:13.425 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [83.6, 39.2]    |  |
| -2689.21 | -2689.21 | 00:03:13.425 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [83.6, 39.2]    |  |
| -2688.44 | -2688.44 | 00:03:14.196 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [82.6, 41.7]    | -> Achraf Hakimi  |
| -2685.58 | -2685.58 | 00:03:17.062 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [92.8, 71.6]    |  |
| -2685.58 | -2685.58 | 00:03:17.062 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [92.8, 71.6]    |  |
| -2684.78 | -2684.78 | 00:03:17.863 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [92.8, 71.4]    | -> Kylian Mbappé  |
| -2684.03 | -2684.03 | 00:03:18.611 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [23.7, 25.6]    |  |
| -2683.90 | -2683.90 | 00:03:18.736 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [94.7, 56.1]    |  |
| -2683.90 | -2683.90 | 00:03:18.736 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [93.6, 56.7]    | -> Marcos Aoás Co |
| -2682.13 | -2682.13 | 00:03:20.507 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [78.1, 62.5]    |  |
| -2682.13 | -2682.13 | 00:03:20.507 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [78.1, 62.5]    | -> Lionel Andrés  |
| -2680.64 | -2680.64 | 00:03:22.001 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [79.0, 45.0]    |  |
| -2680.64 | -2680.64 | 00:03:22.001 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [79.0, 45.0]    |  |
| -2680.43 | -2680.43 | 00:03:22.207 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [39.0, 32.4]    |  |
| -2679.67 | -2679.67 | 00:03:22.970 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [77.8, 40.3]    | -> Sergio Ramos G |
| -2677.60 | -2677.60 | 00:03:25.041 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [78.4, 22.0]    |  |
| -2677.60 | -2677.60 | 00:03:25.041 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [80.6, 22.0]    | -> Juan Bernat Ve |
| -2675.99 | -2675.99 | 00:03:26.648 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [97.5, 6.6]     |  |
| -2675.99 | -2675.99 | 00:03:26.648 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [97.5, 6.6]     |  |
| -2675.83 | -2675.83 | 00:03:26.805 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [97.3, 6.6]     | -> Neymar da Silv |
| -2674.96 | -2674.96 | 00:03:27.681 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [91.1, 13.3]    |  |
| -2674.96 | -2674.96 | 00:03:27.681 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [91.1, 13.3]    |  |
| -2672.83 | -2672.83 | 00:03:29.805 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [90.3, 19.9]    | -> Lionel Andrés  |
| -2671.94 | -2671.94 | 00:03:30.694 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [91.5, 38.3]    |  |
| -2671.94 | -2671.94 | 00:03:30.694 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [91.5, 38.3]    |  |
| -2671.27 | -2671.27 | 00:03:31.367 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [24.8, 40.9]    |  |
| -2667.12 | -2667.12 | 00:03:35.515 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [92.3, 57.5]    | Incomplete (Incomplete) |
| -2666.96 | -2666.96 | 00:03:35.678 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [93.4, 68.1]    | Incomplete |
| -2666.96 | -2666.96 | 00:03:35.678 | Saint-Étienne      | Paris Saint-Germai | 82 | Interception    |   -   | [27.2, 19.6]    | Lost In Play |
| -2666.82 | -2666.82 | 00:03:35.816 | Paris Saint-Germai | Paris Saint-Germai | 82 | Block           |   -   | [92.8, 60.6]    |  |
| -2665.91 | -2665.91 | 00:03:36.726 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [28.6, 14.8]    |  |
| -2665.43 | -2665.43 | 00:03:37.208 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [91.5, 69.5]    | -> Ángel Fabián D |
| -2664.32 | -2664.32 | 00:03:38.318 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [82.3, 65.6]    |  |
| -2664.32 | -2664.32 | 00:03:38.318 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [82.3, 65.6]    |  |
| -2662.03 | -2662.03 | 00:03:40.609 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [89.7, 54.1]    | -> Neymar da Silv |
| -2660.79 | -2660.79 | 00:03:41.848 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [90.4, 39.1]    |  |
| -2660.79 | -2660.79 | 00:03:41.848 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [90.4, 39.1]    |  |
| -2659.45 | -2659.45 | 00:03:43.188 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [25.9, 43.8]    |  |
| -2658.95 | -2658.95 | 00:03:43.692 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [91.5, 34.9]    | -> Sergio Ramos G |
| -2657.59 | -2657.59 | 00:03:45.043 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [91.8, 19.9]    |  |
| -2657.59 | -2657.59 | 00:03:45.043 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [91.8, 19.9]    | -> Juan Bernat Ve |
| -2656.69 | -2656.69 | 00:03:45.946 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [103.9, 20.0]   |  |
| -2656.69 | -2656.69 | 00:03:45.946 | Paris Saint-Germai | Paris Saint-Germai | 82 | Carry           |   -   | [103.9, 20.0]   |  |
| -2656.45 | -2656.45 | 00:03:46.192 | Saint-Étienne      | Paris Saint-Germai | 82 | Pressure        |   -   | [20.9, 61.2]    |  |
| -2656.01 | -2656.01 | 00:03:46.626 | Paris Saint-Germai | Paris Saint-Germai | 82 | Pass            |   -   | [104.0, 19.2]   | Incomplete (Incomplete) |
| -2655.34 | -2655.34 | 00:03:47.294 | Paris Saint-Germai | Paris Saint-Germai | 82 | Ball Receipt*   |   -   | [97.3, 26.4]    | Incomplete |
| -2655.34 | -2655.34 | 00:03:47.294 | Saint-Étienne      | Saint-Étienne      | 83 | Interception    |  Yes  | [21.4, 55.2]    | Won |
| -2655.34 | -2655.34 | 00:03:47.294 | Saint-Étienne      | Saint-Étienne      | 83 | Carry           |   -   | [21.4, 55.2]    |  |
| -2654.72 | -2654.72 | 00:03:47.922 | Paris Saint-Germai | Saint-Étienne      | 83 | Pressure        |  Yes  | [97.9, 26.1]    |  |
| -2653.11 | -2653.11 | 00:03:49.523 | Paris Saint-Germai | Saint-Étienne      | 83 | Foul Committed  |  Yes  | [92.9, 17.2]    |  |
| -2653.11 | -2653.11 | 00:03:49.523 | Saint-Étienne      | Saint-Étienne      | 83 | Foul Won        |   -   | [27.2, 62.9]    |  |
| -2642.13 | -2642.13 | 00:04:00.509 | Saint-Étienne      | Saint-Étienne      | 84 | Pass            |   -   | [22.6, 60.6]    | -> Mahdi Camara |
| -2640.70 | -2640.70 | 00:04:01.942 | Saint-Étienne      | Saint-Étienne      | 84 | Ball Receipt*   |   -   | [35.9, 52.7]    |  |
| -2640.63 | -2640.63 | 00:04:02.004 | Saint-Étienne      | Saint-Étienne      | 84 | Pass            |   -   | [33.6, 52.7]    | -> Harold Moukoud |
| -2637.07 | -2637.07 | 00:04:05.570 | Saint-Étienne      | Saint-Étienne      | 84 | Ball Receipt*   |   -   | [21.4, 54.9]    |  |
| -2637.02 | -2637.02 | 00:04:05.617 | Saint-Étienne      | Saint-Étienne      | 84 | Pass            |   -   | [20.9, 56.3]    | -> Yvann Macon |
| -2635.88 | -2635.88 | 00:04:06.760 | Saint-Étienne      | Saint-Étienne      | 84 | Ball Receipt*   |   -   | [29.4, 77.7]    |  |
| -2635.88 | -2635.88 | 00:04:06.760 | Saint-Étienne      | Saint-Étienne      | 84 | Carry           |   -   | [29.4, 77.7]    |  |
| -2634.72 | -2634.72 | 00:04:07.920 | Paris Saint-Germai | Saint-Étienne      | 84 | Pressure        |   -   | [87.2, 6.4]     |  |
| -2634.63 | -2634.63 | 00:04:08.007 | Saint-Étienne      | Saint-Étienne      | 84 | Pass            |   -   | [33.1, 79.0]    | -> Wahbi Khazri |
| -2633.73 | -2633.73 | 00:04:08.905 | Paris Saint-Germai | Saint-Étienne      | 84 | Pressure        |   -   | [65.9, 22.5]    |  |
| -2633.22 | -2633.22 | 00:04:09.416 | Saint-Étienne      | Saint-Étienne      | 84 | Ball Receipt*   |   -   | [50.6, 57.3]    |  |
| -2633.22 | -2633.22 | 00:04:09.416 | Saint-Étienne      | Saint-Étienne      | 84 | Carry           |   -   | [50.6, 57.3]    |  |
| -2632.38 | -2632.38 | 00:04:10.254 | Saint-Étienne      | Saint-Étienne      | 84 | Miscontrol      |   -   | [51.2, 57.9]    |  |
| -2631.33 | -2631.33 | 00:04:11.306 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pass            |   -   | [69.3, 23.8]    | -> Idrissa Gana G |
| -2630.46 | -2630.46 | 00:04:12.176 | Paris Saint-Germai | Paris Saint-Germai | 85 | Ball Receipt*   |   -   | [75.7, 18.1]    |  |
| -2630.46 | -2630.46 | 00:04:12.176 | Paris Saint-Germai | Paris Saint-Germai | 85 | Carry           |   -   | [75.7, 18.1]    |  |
| -2628.72 | -2628.72 | 00:04:13.916 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pass            |   -   | [79.2, 19.9]    | -> Kylian Mbappé  |
| -2628.25 | -2628.25 | 00:04:14.387 | Saint-Étienne      | Paris Saint-Germai | 85 | Pressure        |  Yes  | [29.2, 51.8]    |  |
| -2627.88 | -2627.88 | 00:04:14.759 | Paris Saint-Germai | Paris Saint-Germai | 85 | Ball Receipt*   |   -   | [89.0, 29.7]    |  |
| -2627.88 | -2627.88 | 00:04:14.759 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pass            |   -   | [90.3, 29.9]    | -> Lionel Andrés  |
| -2626.80 | -2626.80 | 00:04:15.842 | Paris Saint-Germai | Paris Saint-Germai | 85 | Ball Receipt*   |   -   | [84.2, 43.5]    |  |
| -2626.80 | -2626.80 | 00:04:15.842 | Paris Saint-Germai | Paris Saint-Germai | 85 | Carry           |   -   | [84.2, 43.5]    |  |
| -2626.76 | -2626.76 | 00:04:15.877 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pass            |   -   | [85.1, 44.1]    | -> Ángel Fabián D |
| -2624.79 | -2624.79 | 00:04:17.848 | Paris Saint-Germai | Paris Saint-Germai | 85 | Ball Receipt*   |   -   | [85.1, 56.7]    |  |
| -2624.79 | -2624.79 | 00:04:17.848 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pass            |   -   | [88.4, 57.8]    | Incomplete (Incomplete) |
| -2623.29 | -2623.29 | 00:04:19.347 | Paris Saint-Germai | Paris Saint-Germai | 85 | Pressure        |   -   | [106.5, 56.0]   |  |
| -2623.07 | -2623.07 | 00:04:19.568 | Paris Saint-Germai | Paris Saint-Germai | 85 | Ball Receipt*   |   -   | [107.3, 55.8]   | Incomplete |
| -2623.07 | -2623.07 | 00:04:19.568 | Saint-Étienne      | Saint-Étienne      | 86 | Interception    |  Yes  | [11.7, 24.8]    | Won |
| -2623.07 | -2623.07 | 00:04:19.568 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [11.7, 24.8]    |  |
| -2622.04 | -2622.04 | 00:04:20.594 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [8.4, 24.6]     | -> Mickaël Nade |
| -2621.18 | -2621.18 | 00:04:21.457 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [7.5, 30.9]     |  |
| -2621.18 | -2621.18 | 00:04:21.457 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [7.5, 30.9]     |  |
| -2620.40 | -2620.40 | 00:04:22.242 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [9.5, 29.8]     | -> Denis Bouanga |
| -2619.60 | -2619.60 | 00:04:23.040 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [14.8, 22.3]    |  |
| -2619.60 | -2619.60 | 00:04:23.040 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [14.8, 22.3]    |  |
| -2619.56 | -2619.56 | 00:04:23.080 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [14.8, 22.3]    | -> Miguel Ángel T |
| -2618.56 | -2618.56 | 00:04:24.077 | Paris Saint-Germai | Saint-Étienne      | 86 | Pressure        |  Yes  | [105.3, 69.5]   |  |
| -2618.09 | -2618.09 | 00:04:24.546 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [10.4, 10.9]    |  |
| -2618.09 | -2618.09 | 00:04:24.546 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [10.4, 10.9]    |  |
| -2617.97 | -2617.97 | 00:04:24.666 | Paris Saint-Germai | Saint-Étienne      | 86 | Dribbled Past   |   -   | [108.1, 68.9]   |  |
| -2617.97 | -2617.97 | 00:04:24.666 | Saint-Étienne      | Saint-Étienne      | 86 | Dribble         |   -   | [12.0, 11.2]    |  |
| -2617.97 | -2617.97 | 00:04:24.666 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [12.0, 11.2]    |  |
| -2616.86 | -2616.86 | 00:04:25.781 | Paris Saint-Germai | Saint-Étienne      | 86 | Dribbled Past   |   -   | [104.2, 68.6]   |  |
| -2616.86 | -2616.86 | 00:04:25.781 | Saint-Étienne      | Saint-Étienne      | 86 | Dribble         |   -   | [15.9, 11.5]    |  |
| -2616.86 | -2616.86 | 00:04:25.781 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [15.9, 11.5]    |  |
| -2614.79 | -2614.79 | 00:04:27.847 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [22.0, 20.7]    | Incomplete (Incomplete) |
| -2613.48 | -2613.48 | 00:04:29.157 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [38.9, 40.9]    | Incomplete |
| -2613.48 | -2613.48 | 00:04:29.157 | Paris Saint-Germai | Saint-Étienne      | 86 | Interception    |   -   | [81.8, 40.5]    | Won |
| -2613.48 | -2613.48 | 00:04:29.157 | Paris Saint-Germai | Saint-Étienne      | 86 | Carry           |   -   | [81.8, 40.5]    |  |
| -2612.30 | -2612.30 | 00:04:30.333 | Paris Saint-Germai | Saint-Étienne      | 86 | Pass            |   -   | [84.7, 50.6]    | -> Kylian Mbappé  |
| -2611.80 | -2611.80 | 00:04:30.838 | Saint-Étienne      | Saint-Étienne      | 86 | Pressure        |  Yes  | [20.6, 36.5]    |  |
| -2611.32 | -2611.32 | 00:04:31.321 | Paris Saint-Germai | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [99.7, 44.9]    |  |
| -2611.32 | -2611.32 | 00:04:31.321 | Paris Saint-Germai | Saint-Étienne      | 86 | Miscontrol      |   -   | [99.7, 44.9]    |  |
| -2609.39 | -2609.39 | 00:04:33.248 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Recovery   |   -   | [8.9, 35.9]     |  |
| -2606.37 | -2606.37 | 00:04:36.266 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [11.5, 46.3]    | -> Yvann Macon |
| -2604.10 | -2604.10 | 00:04:38.541 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [26.7, 66.3]    |  |
| -2601.82 | -2601.82 | 00:04:40.817 | Paris Saint-Germai | Saint-Étienne      | 86 | Pressure        |   -   | [84.2, 12.4]    |  |
| -2601.39 | -2601.39 | 00:04:41.252 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [34.4, 70.4]    | -> Zaydou Youssou |
| -2600.51 | -2600.51 | 00:04:42.124 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [38.1, 77.3]    |  |
| -2600.51 | -2600.51 | 00:04:42.124 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [38.1, 77.3]    |  |
| -2599.20 | -2599.20 | 00:04:43.439 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [38.3, 77.7]    | -> Yvann Macon |
| -2597.85 | -2597.85 | 00:04:44.785 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [27.8, 74.3]    |  |
| -2597.85 | -2597.85 | 00:04:44.785 | Saint-Étienne      | Saint-Étienne      | 86 | Carry           |   -   | [27.8, 74.3]    |  |
| -2596.63 | -2596.63 | 00:04:46.006 | Paris Saint-Germai | Saint-Étienne      | 86 | Pressure        |   -   | [89.8, 8.3]     |  |
| -2595.55 | -2595.55 | 00:04:47.089 | Saint-Étienne      | Saint-Étienne      | 86 | Pass            |   -   | [23.1, 70.7]    | Incomplete (Incomplete) |
| -2594.22 | -2594.22 | 00:04:48.415 | Saint-Étienne      | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [18.6, 40.2]    | Incomplete |
| -2594.22 | -2594.22 | 00:04:48.415 | Paris Saint-Germai | Saint-Étienne      | 86 | Pass            |   -   | [92.2, 38.1]    | Incomplete (Out) |
| -2591.16 | -2591.16 | 00:04:51.475 | Paris Saint-Germai | Saint-Étienne      | 86 | Ball Receipt*   |   -   | [102.6, 24.9]   | Incomplete |
| -2571.04 | -2571.04 | 00:05:11.602 | Saint-Étienne      | Saint-Étienne      | 87 | Pass            |   -   | [7.0, 36.1]     | Incomplete (Incomplete) |
| -2566.66 | -2566.66 | 00:05:15.977 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [70.6, 59.2]    | -> Achraf Hakimi  |
| -2564.77 | -2564.77 | 00:05:17.867 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [62.9, 74.4]    |  |
| -2564.77 | -2564.77 | 00:05:17.867 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [62.9, 74.4]    |  |
| -2563.22 | -2563.22 | 00:05:19.413 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [62.9, 75.0]    | -> Danilo Luís Hé |
| -2562.22 | -2562.22 | 00:05:20.421 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [67.0, 64.9]    |  |
| -2562.22 | -2562.22 | 00:05:20.421 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [67.0, 64.9]    |  |
| -2560.81 | -2560.81 | 00:05:21.824 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [67.6, 65.0]    | -> Lionel Andrés  |
| -2560.32 | -2560.32 | 00:05:22.318 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [70.6, 53.9]    |  |
| -2560.32 | -2560.32 | 00:05:22.318 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [70.6, 53.9]    | -> Danilo Luís Hé |
| -2559.23 | -2559.23 | 00:05:23.411 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [67.0, 61.4]    |  |
| -2559.23 | -2559.23 | 00:05:23.411 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [67.0, 61.4]    | -> Sergio Ramos G |
| -2556.72 | -2556.72 | 00:05:25.918 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [63.4, 24.1]    |  |
| -2556.72 | -2556.72 | 00:05:25.918 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [63.4, 26.7]    | -> Neymar da Silv |
| -2555.55 | -2555.55 | 00:05:27.090 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [80.6, 18.9]    |  |
| -2555.55 | -2555.55 | 00:05:27.090 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [80.6, 18.9]    |  |
| -2554.71 | -2554.71 | 00:05:27.928 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [79.7, 18.8]    | -> Juan Bernat Ve |
| -2553.43 | -2553.43 | 00:05:29.205 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [85.6, 4.9]     |  |
| -2553.43 | -2553.43 | 00:05:29.205 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [85.6, 4.9]     |  |
| -2552.27 | -2552.27 | 00:05:30.371 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [85.6, 4.9]     | -> Neymar da Silv |
| -2551.42 | -2551.42 | 00:05:31.220 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [84.5, 15.5]    |  |
| -2551.42 | -2551.42 | 00:05:31.220 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [84.5, 15.5]    |  |
| -2549.80 | -2549.80 | 00:05:32.841 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [84.3, 16.9]    | -> Ángel Fabián D |
| -2547.84 | -2547.84 | 00:05:34.798 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [78.7, 52.0]    |  |
| -2547.84 | -2547.84 | 00:05:34.798 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [78.7, 52.0]    |  |
| -2544.59 | -2544.59 | 00:05:38.045 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [84.5, 53.1]    | -> Danilo Luís Hé |
| -2543.07 | -2543.07 | 00:05:39.570 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [80.9, 40.5]    |  |
| -2543.07 | -2543.07 | 00:05:39.570 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [80.9, 40.5]    | -> Idrissa Gana G |
| -2541.71 | -2541.71 | 00:05:40.932 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [84.5, 29.4]    |  |
| -2541.71 | -2541.71 | 00:05:40.932 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [84.5, 29.4]    |  |
| -2540.18 | -2540.18 | 00:05:42.456 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [84.3, 36.3]    | -> Ángel Fabián D |
| -2538.61 | -2538.61 | 00:05:44.026 | Paris Saint-Germai | Paris Saint-Germai | 88 | Ball Receipt*   |   -   | [86.4, 54.9]    |  |
| -2538.61 | -2538.61 | 00:05:44.026 | Paris Saint-Germai | Paris Saint-Germai | 88 | Carry           |   -   | [86.4, 54.9]    |  |
| -2537.51 | -2537.51 | 00:05:45.127 | Paris Saint-Germai | Paris Saint-Germai | 88 | Pass            |   -   | [86.4, 54.9]    | Incomplete (Incomplete) |
| -2535.49 | -2535.49 | 00:05:47.148 | Saint-Étienne      | Paris Saint-Germai | 88 | Interception    |   -   | [17.6, 57.4]    | Lost Out |
| -2528.84 | -2528.84 | 00:05:53.803 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [100.1, 0.1]    | -> Sergio Ramos G |
| -2526.02 | -2526.02 | 00:05:56.616 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [83.1, 8.1]     |  |
| -2526.02 | -2526.02 | 00:05:56.616 | Paris Saint-Germai | Paris Saint-Germai | 89 | Carry           |   -   | [83.1, 8.1]     |  |
| -2525.85 | -2525.85 | 00:05:56.790 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [78.6, 8.1]     | -> Danilo Luís Hé |
| -2524.46 | -2524.46 | 00:05:58.180 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [71.2, 24.1]    |  |
| -2524.46 | -2524.46 | 00:05:58.180 | Paris Saint-Germai | Paris Saint-Germai | 89 | Carry           |   -   | [71.2, 24.1]    |  |
| -2523.94 | -2523.94 | 00:05:58.701 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [71.2, 24.1]    | -> Idrissa Gana G |
| -2523.07 | -2523.07 | 00:05:59.572 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [80.9, 24.4]    |  |
| -2523.07 | -2523.07 | 00:05:59.572 | Paris Saint-Germai | Paris Saint-Germai | 89 | Carry           |   -   | [80.9, 24.4]    |  |
| -2519.85 | -2519.85 | 00:06:02.789 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [91.1, 22.7]    | -> Neymar da Silv |
| -2519.30 | -2519.30 | 00:06:03.340 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [92.9, 28.0]    |  |
| -2519.30 | -2519.30 | 00:06:03.340 | Paris Saint-Germai | Paris Saint-Germai | 89 | Carry           |   -   | [92.9, 28.0]    |  |
| -2519.01 | -2519.01 | 00:06:03.623 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [92.9, 28.0]    | -> Lionel Andrés  |
| -2518.12 | -2518.12 | 00:06:04.514 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [88.9, 37.5]    |  |
| -2518.12 | -2518.12 | 00:06:04.514 | Paris Saint-Germai | Paris Saint-Germai | 89 | Carry           |   -   | [88.9, 37.5]    |  |
| -2517.38 | -2517.38 | 00:06:05.259 | Saint-Étienne      | Paris Saint-Germai | 89 | Pressure        |   -   | [25.3, 43.2]    |  |
| -2517.21 | -2517.21 | 00:06:05.430 | Paris Saint-Germai | Paris Saint-Germai | 89 | Pass            |   -   | [91.4, 39.9]    | Incomplete (Incomplete) |
| -2515.41 | -2515.41 | 00:06:07.227 | Paris Saint-Germai | Paris Saint-Germai | 89 | Ball Receipt*   |   -   | [98.2, 48.0]    | Incomplete |
| -2515.41 | -2515.41 | 00:06:07.227 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Recovery   |   -   | [23.3, 25.6]    |  |
| -2515.41 | -2515.41 | 00:06:07.227 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [23.3, 25.6]    |  |
| -2507.61 | -2507.61 | 00:06:15.025 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [51.2, 4.3]     | -> Miguel Ángel T |
| -2506.53 | -2506.53 | 00:06:16.103 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [51.4, 14.8]    |  |
| -2506.53 | -2506.53 | 00:06:16.103 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [51.4, 14.8]    |  |
| -2506.46 | -2506.46 | 00:06:16.182 | Paris Saint-Germai | Saint-Étienne      | 90 | Pressure        |   -   | [68.7, 59.4]    |  |
| -2505.68 | -2505.68 | 00:06:16.953 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [52.2, 16.8]    | -> Mahdi Camara |
| -2505.50 | -2505.50 | 00:06:17.138 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [54.7, 26.3]    |  |
| -2505.50 | -2505.50 | 00:06:17.138 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [54.7, 26.3]    |  |
| -2505.50 | -2505.50 | 00:06:17.138 | Paris Saint-Germai | Saint-Étienne      | 90 | Block           |   -   | [67.3, 59.4]    |  |
| -2504.45 | -2504.45 | 00:06:18.184 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [56.5, 28.2]    | -> Ryad Boudebouz |
| -2503.77 | -2503.77 | 00:06:18.867 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [51.2, 31.5]    |  |
| -2503.77 | -2503.77 | 00:06:18.867 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [51.2, 31.5]    |  |
| -2503.37 | -2503.37 | 00:06:19.272 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [52.2, 30.9]    | -> Zaydou Youssou |
| -2502.22 | -2502.22 | 00:06:20.419 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [66.9, 33.4]    |  |
| -2502.22 | -2502.22 | 00:06:20.419 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [66.9, 33.4]    | -> Mahdi Camara |
| -2501.55 | -2501.55 | 00:06:21.085 | Paris Saint-Germai | Saint-Étienne      | 90 | Pressure        |   -   | [57.0, 56.7]    |  |
| -2501.46 | -2501.46 | 00:06:21.177 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [64.5, 23.5]    |  |
| -2501.46 | -2501.46 | 00:06:21.177 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [64.5, 23.5]    |  |
| -2501.12 | -2501.12 | 00:06:21.515 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [65.0, 24.9]    | Incomplete (Incomplete) |
| -2501.04 | -2501.04 | 00:06:21.600 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [55.1, 25.6]    | Incomplete |
| -2501.04 | -2501.04 | 00:06:21.600 | Paris Saint-Germai | Saint-Étienne      | 90 | Block           |   -   | [57.0, 54.2]    |  |
| -2499.38 | -2499.38 | 00:06:23.260 | Paris Saint-Germai | Saint-Étienne      | 90 | Pass            |   -   | [42.2, 36.4]    | -> Neymar da Silv |
| -2497.63 | -2497.63 | 00:06:25.011 | Paris Saint-Germai | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [55.7, 27.2]    |  |
| -2497.63 | -2497.63 | 00:06:25.011 | Paris Saint-Germai | Saint-Étienne      | 90 | Carry           |   -   | [55.7, 27.2]    |  |
| -2496.08 | -2496.08 | 00:06:26.561 | Saint-Étienne      | Saint-Étienne      | 90 | Pressure        |  Yes  | [63.1, 56.2]    |  |
| -2495.23 | -2495.23 | 00:06:27.409 | Saint-Étienne      | Saint-Étienne      | 90 | Pressure        |  Yes  | [59.7, 56.3]    |  |
| -2494.62 | -2494.62 | 00:06:28.019 | Paris Saint-Germai | Saint-Étienne      | 90 | Pass            |   -   | [60.7, 25.8]    | Incomplete (Incomplete) |
| -2493.51 | -2493.51 | 00:06:29.129 | Paris Saint-Germai | Saint-Étienne      | 90 | Pressure        |   -   | [56.4, 36.4]    |  |
| -2493.22 | -2493.22 | 00:06:29.416 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Recovery   |   -   | [63.7, 45.7]    |  |
| -2493.22 | -2493.22 | 00:06:29.416 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [63.7, 45.7]    |  |
| -2491.11 | -2491.11 | 00:06:31.524 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [51.4, 51.0]    | -> Etienne Green |
| -2488.24 | -2488.24 | 00:06:34.401 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [15.6, 42.3]    |  |
| -2488.24 | -2488.24 | 00:06:34.401 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [15.6, 42.3]    |  |
| -2487.20 | -2487.20 | 00:06:35.441 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [12.9, 41.3]    | -> Mickaël Nade |
| -2485.45 | -2485.45 | 00:06:37.187 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [25.1, 27.4]    |  |
| -2485.45 | -2485.45 | 00:06:37.187 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [25.1, 27.4]    |  |
| -2484.30 | -2484.30 | 00:06:38.336 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [26.7, 27.0]    | -> Ryad Boudebouz |
| -2483.37 | -2483.37 | 00:06:39.266 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [35.8, 42.3]    |  |
| -2483.37 | -2483.37 | 00:06:39.266 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [35.8, 42.3]    |  |
| -2483.25 | -2483.25 | 00:06:39.386 | Saint-Étienne      | Saint-Étienne      | 90 | Pass            |   -   | [35.8, 41.8]    | -> Mickaël Nade |
| -2481.93 | -2481.93 | 00:06:40.706 | Saint-Étienne      | Saint-Étienne      | 90 | Ball Receipt*   |   -   | [28.3, 24.3]    |  |
| -2481.93 | -2481.93 | 00:06:40.706 | Saint-Étienne      | Saint-Étienne      | 90 | Carry           |   -   | [28.3, 24.3]    |  |
| -2481.91 | -2481.91 | 00:06:40.727 | Paris Saint-Germai | Saint-Étienne      | 90 | Pressure        |   -   | [87.2, 50.3]    |  |
| -2481.13 | -2481.13 | 00:06:41.511 | Saint-Étienne      | Saint-Étienne      | 90 | Dispossessed    |   -   | [31.7, 24.1]    |  |
| -2481.13 | -2481.13 | 00:06:41.511 | Paris Saint-Germai | Paris Saint-Germai | 91 | Duel            |  Yes  | [88.4, 56.0]    | Tackle, Success In Play |
| -2479.87 | -2479.87 | 00:06:42.767 | Paris Saint-Germai | Paris Saint-Germai | 91 | Ball Recovery   |   -   | [82.6, 63.6]    |  |
| -2479.87 | -2479.87 | 00:06:42.767 | Paris Saint-Germai | Paris Saint-Germai | 91 | Carry           |   -   | [82.6, 63.6]    |  |
| -2477.62 | -2477.62 | 00:06:45.020 | Paris Saint-Germai | Paris Saint-Germai | 91 | Pass            |   -   | [86.8, 55.2]    | Incomplete (Pass Offside) |
| -2476.61 | -2476.61 | 00:06:46.030 | Paris Saint-Germai | Paris Saint-Germai | 91 | Ball Receipt*   |   -   | [98.6, 56.6]    | Incomplete |
| -2437.35 | -2437.35 | 00:07:25.288 | Saint-Étienne      | Saint-Étienne      | 92 | Pass            |   -   | [20.8, 25.2]    | Incomplete (Out) |
| -2427.61 | -2427.61 | 00:07:35.024 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [67.0, 0.1]     | -> Neymar da Silv |
| -2426.63 | -2426.63 | 00:07:36.003 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [70.3, 7.5]     |  |
| -2426.63 | -2426.63 | 00:07:36.003 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [70.3, 7.5]     |  |
| -2421.02 | -2421.02 | 00:07:41.617 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [64.2, 11.4]    | -> Marcos Aoás Co |
| -2418.47 | -2418.47 | 00:07:44.166 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [55.6, 39.2]    |  |
| -2418.47 | -2418.47 | 00:07:44.166 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [55.6, 39.2]    | -> Ángel Fabián D |
| -2416.45 | -2416.45 | 00:07:46.186 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [69.8, 56.7]    |  |
| -2416.45 | -2416.45 | 00:07:46.186 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [69.8, 56.7]    |  |
| -2413.72 | -2413.72 | 00:07:48.917 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [70.0, 58.1]    | -> Sergio Ramos G |
| -2411.41 | -2411.41 | 00:07:51.228 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [64.7, 25.3]    |  |
| -2411.41 | -2411.41 | 00:07:51.228 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [64.7, 25.3]    |  |
| -2409.32 | -2409.32 | 00:07:53.317 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [59.8, 18.3]    | -> Neymar da Silv |
| -2408.05 | -2408.05 | 00:07:54.586 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [71.4, 15.5]    |  |
| -2408.05 | -2408.05 | 00:07:54.586 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [71.4, 15.5]    |  |
| -2406.28 | -2406.28 | 00:07:56.356 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [77.9, 16.7]    | -> Juan Bernat Ve |
| -2403.20 | -2403.20 | 00:07:59.433 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [104.8, 2.8]    |  |
| -2403.20 | -2403.20 | 00:07:59.433 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [104.8, 2.8]    |  |
| -2401.73 | -2401.73 | 00:08:00.907 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [106.8, 3.9]    | -> Neymar da Silv |
| -2400.85 | -2400.85 | 00:08:01.784 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [91.7, 10.5]    |  |
| -2400.85 | -2400.85 | 00:08:01.784 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [91.7, 10.5]    |  |
| -2400.14 | -2400.14 | 00:08:02.499 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [90.4, 12.7]    | -> Idrissa Gana G |
| -2398.84 | -2398.84 | 00:08:03.800 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [90.4, 22.8]    |  |
| -2398.84 | -2398.84 | 00:08:03.800 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [90.4, 22.8]    |  |
| -2394.74 | -2394.74 | 00:08:07.900 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [88.6, 21.6]    | -> Danilo Luís Hé |
| -2393.45 | -2393.45 | 00:08:09.187 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [83.1, 39.9]    |  |
| -2393.45 | -2393.45 | 00:08:09.187 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [83.1, 39.9]    |  |
| -2392.57 | -2392.57 | 00:08:10.064 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [83.2, 41.0]    | -> Lionel Andrés  |
| -2391.85 | -2391.85 | 00:08:10.792 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [83.7, 50.0]    |  |
| -2391.85 | -2391.85 | 00:08:10.792 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [83.7, 50.0]    |  |
| -2391.02 | -2391.02 | 00:08:11.621 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [83.7, 50.0]    | -> Sergio Ramos G |
| -2389.76 | -2389.76 | 00:08:12.877 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [82.5, 29.7]    |  |
| -2389.76 | -2389.76 | 00:08:12.877 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [82.5, 29.7]    |  |
| -2388.67 | -2388.67 | 00:08:13.963 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [83.2, 29.4]    | -> Juan Bernat Ve |
| -2386.83 | -2386.83 | 00:08:15.808 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [104.5, 11.0]   |  |
| -2386.83 | -2386.83 | 00:08:15.808 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [104.5, 11.0]   |  |
| -2386.38 | -2386.38 | 00:08:16.255 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [104.5, 11.0]   | -> Neymar da Silv |
| -2385.36 | -2385.36 | 00:08:17.273 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [97.6, 16.0]    |  |
| -2385.36 | -2385.36 | 00:08:17.273 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [97.6, 16.0]    |  |
| -2384.45 | -2384.45 | 00:08:18.185 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [96.4, 16.9]    | -> Idrissa Gana G |
| -2383.60 | -2383.60 | 00:08:19.042 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [92.5, 28.0]    |  |
| -2383.60 | -2383.60 | 00:08:19.042 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [92.5, 28.0]    |  |
| -2383.13 | -2383.13 | 00:08:19.509 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [92.5, 28.0]    | -> Neymar da Silv |
| -2382.26 | -2382.26 | 00:08:20.379 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [92.3, 19.9]    |  |
| -2382.26 | -2382.26 | 00:08:20.379 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [92.3, 19.9]    |  |
| -2380.96 | -2380.96 | 00:08:21.675 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [90.7, 20.5]    | -> Lionel Andrés  |
| -2379.58 | -2379.58 | 00:08:23.056 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [90.3, 53.3]    |  |
| -2379.58 | -2379.58 | 00:08:23.056 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [90.3, 53.3]    |  |
| -2377.73 | -2377.73 | 00:08:24.906 | Saint-Étienne      | Paris Saint-Germai | 93 | Pressure        |   -   | [26.5, 30.2]    |  |
| -2377.23 | -2377.23 | 00:08:25.406 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [89.2, 47.4]    | Incomplete (Out) |
| -2374.10 | -2374.10 | 00:08:28.534 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [111.1, 19.9]   | Incomplete |
| -2340.70 | -2340.70 | 00:09:01.939 | Saint-Étienne      | Saint-Étienne      | 94 | Pass            |   -   | [7.0, 36.1]     | -> Denis Bouanga |
| -2337.22 | -2337.22 | 00:09:05.423 | Saint-Étienne      | Saint-Étienne      | 94 | Ball Receipt*   |   -   | [70.1, 5.7]     |  |
| -2337.22 | -2337.22 | 00:09:05.423 | Saint-Étienne      | Saint-Étienne      | 94 | Pass            |   -   | [70.1, 5.7]     | Incomplete (Incomplete) |
| -2337.22 | -2337.22 | 00:09:05.423 | Paris Saint-Germai | Saint-Étienne      | 94 | Duel            |   -   | [50.0, 74.4]    | Aerial Lost |
| -2335.40 | -2335.40 | 00:09:07.235 | Saint-Étienne      | Saint-Étienne      | 94 | Ball Receipt*   |   -   | [83.4, 20.1]    | Incomplete |
| -2335.40 | -2335.40 | 00:09:07.235 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [35.4, 59.9]    | -> Danilo Luís Hé |
| -2334.51 | -2334.51 | 00:09:08.124 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [45.9, 63.6]    |  |
| -2334.51 | -2334.51 | 00:09:08.124 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [45.9, 63.6]    |  |
| -2333.73 | -2333.73 | 00:09:08.912 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [41.8, 61.1]    | -> Sergio Ramos G |
| -2331.03 | -2331.03 | 00:09:11.603 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [31.1, 39.2]    |  |
| -2331.03 | -2331.03 | 00:09:11.603 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [31.1, 39.2]    |  |
| -2330.83 | -2330.83 | 00:09:11.805 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [27.6, 34.9]    | -> Gianluigi Donn |
| -2328.90 | -2328.90 | 00:09:13.740 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [4.0, 37.8]     |  |
| -2328.90 | -2328.90 | 00:09:13.740 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [4.5, 37.8]     | -> Sergio Ramos G |
| -2326.81 | -2326.81 | 00:09:15.826 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [13.7, 18.6]    |  |
| -2326.81 | -2326.81 | 00:09:15.826 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [13.7, 18.6]    |  |
| -2325.90 | -2325.90 | 00:09:16.737 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [14.7, 17.7]    | -> Idrissa Gana G |
| -2324.39 | -2324.39 | 00:09:18.247 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [35.0, 22.2]    |  |
| -2324.39 | -2324.39 | 00:09:18.247 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [35.0, 22.2]    |  |
| -2323.94 | -2323.94 | 00:09:18.702 | Saint-Étienne      | Paris Saint-Germai | 95 | Pressure        |   -   | [85.1, 54.6]    |  |
| -2321.73 | -2321.73 | 00:09:20.911 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [43.7, 6.6]     | -> Neymar da Silv |
| -2320.87 | -2320.87 | 00:09:21.764 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [54.8, 3.8]     |  |
| -2320.87 | -2320.87 | 00:09:21.764 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [55.9, 3.9]     | -> Juan Bernat Ve |
| -2319.51 | -2319.51 | 00:09:23.130 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [43.1, 3.9]     |  |
| -2319.51 | -2319.51 | 00:09:23.130 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [43.1, 3.9]     |  |
| -2316.26 | -2316.26 | 00:09:26.381 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [47.6, 9.7]     | -> Marcos Aoás Co |
| -2314.54 | -2314.54 | 00:09:28.095 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [40.4, 42.0]    |  |
| -2314.54 | -2314.54 | 00:09:28.095 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [40.4, 42.0]    |  |
| -2313.12 | -2313.12 | 00:09:29.517 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [42.2, 43.0]    | -> Lionel Andrés  |
| -2311.61 | -2311.61 | 00:09:31.026 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [56.2, 45.6]    |  |
| -2311.61 | -2311.61 | 00:09:31.026 | Paris Saint-Germai | Paris Saint-Germai | 95 | Carry           |   -   | [56.2, 45.6]    |  |
| -2309.91 | -2309.91 | 00:09:32.732 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pass            |   -   | [64.7, 42.0]    | Incomplete (Incomplete) |
| -2308.87 | -2308.87 | 00:09:33.767 | Paris Saint-Germai | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [84.7, 31.6]    | Incomplete |
| -2308.87 | -2308.87 | 00:09:33.767 | Saint-Étienne      | Paris Saint-Germai | 95 | Pass            |   -   | [35.4, 41.6]    | -> Ryad Boudebouz |
| -2307.49 | -2307.49 | 00:09:35.152 | Saint-Étienne      | Paris Saint-Germai | 95 | Ball Receipt*   |   -   | [43.6, 54.6]    |  |
| -2307.49 | -2307.49 | 00:09:35.152 | Saint-Étienne      | Paris Saint-Germai | 95 | Carry           |   -   | [43.6, 54.6]    |  |
| -2306.19 | -2306.19 | 00:09:36.446 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pressure        |  Yes  | [69.5, 31.7]    |  |
| -2303.82 | -2303.82 | 00:09:38.823 | Paris Saint-Germai | Paris Saint-Germai | 95 | Pressure        |  Yes  | [63.6, 26.7]    |  |
| -2303.21 | -2303.21 | 00:09:39.428 | Paris Saint-Germai | Paris Saint-Germai | 95 | Foul Committed  |  Yes  | [59.0, 26.4]    |  |
| -2303.21 | -2303.21 | 00:09:39.428 | Saint-Étienne      | Paris Saint-Germai | 95 | Foul Won        |   -   | [61.1, 53.7]    |  |
| -2265.75 | -2265.75 | 00:10:16.885 | Saint-Étienne      | Saint-Étienne      | 96 | Pass            |   -   | [64.2, 53.4]    | Incomplete (Out) |
| -2263.99 | -2263.99 | 00:10:18.652 | Saint-Étienne      | Saint-Étienne      | 96 | Ball Receipt*   |   -   | [68.1, 74.6]    | Incomplete |
| -2259.32 | -2259.32 | 00:10:23.321 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [43.9, 0.1]     | -> Sergio Ramos G |
| -2258.14 | -2258.14 | 00:10:24.499 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [34.2, 9.1]     |  |
| -2255.88 | -2255.88 | 00:10:26.755 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [34.2, 10.3]    | -> Marcos Aoás Co |
| -2254.18 | -2254.18 | 00:10:28.462 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [32.9, 39.7]    |  |
| -2254.18 | -2254.18 | 00:10:28.462 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [32.9, 39.7]    |  |
| -2249.43 | -2249.43 | 00:10:33.208 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [39.2, 50.8]    | -> Achraf Hakimi  |
| -2247.89 | -2247.89 | 00:10:34.746 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [54.5, 70.3]    |  |
| -2247.89 | -2247.89 | 00:10:34.746 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [54.5, 70.3]    |  |
| -2247.07 | -2247.07 | 00:10:35.568 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [56.4, 71.0]    | -> Ángel Fabián D |
| -2246.17 | -2246.17 | 00:10:36.468 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [66.4, 75.6]    |  |
| -2246.17 | -2246.17 | 00:10:36.468 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [66.4, 75.6]    |  |
| -2244.85 | -2244.85 | 00:10:37.784 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [64.7, 75.6]    | -> Danilo Luís Hé |
| -2243.49 | -2243.49 | 00:10:39.147 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [55.6, 59.1]    |  |
| -2243.49 | -2243.49 | 00:10:39.147 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [55.6, 59.1]    |  |
| -2241.41 | -2241.41 | 00:10:41.229 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [56.4, 48.9]    | -> Sergio Ramos G |
| -2239.52 | -2239.52 | 00:10:43.120 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [54.5, 26.6]    |  |
| -2239.52 | -2239.52 | 00:10:43.120 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [54.5, 26.6]    |  |
| -2239.42 | -2239.42 | 00:10:43.220 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [54.5, 26.6]    | -> Juan Bernat Ve |
| -2237.62 | -2237.62 | 00:10:45.022 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [70.1, 4.4]     |  |
| -2237.62 | -2237.62 | 00:10:45.022 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [70.1, 4.4]     |  |
| -2236.61 | -2236.61 | 00:10:46.030 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [76.1, 4.4]     | -> Neymar da Silv |
| -2235.90 | -2235.90 | 00:10:46.740 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [82.5, 4.4]     |  |
| -2235.90 | -2235.90 | 00:10:46.740 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [82.5, 4.4]     | -> Juan Bernat Ve |
| -2234.51 | -2234.51 | 00:10:48.126 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [76.7, 5.2]     |  |
| -2234.51 | -2234.51 | 00:10:48.126 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [76.7, 5.2]     |  |
| -2233.24 | -2233.24 | 00:10:49.400 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [76.7, 5.2]     | -> Sergio Ramos G |
| -2232.25 | -2232.25 | 00:10:50.392 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [70.0, 13.8]    |  |
| -2232.25 | -2232.25 | 00:10:50.392 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [70.0, 13.8]    |  |
| -2230.69 | -2230.69 | 00:10:51.943 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [69.5, 18.3]    | -> Ángel Fabián D |
| -2227.41 | -2227.41 | 00:10:55.223 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [87.8, 73.6]    |  |
| -2227.41 | -2227.41 | 00:10:55.223 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [87.8, 73.6]    |  |
| -2221.50 | -2221.50 | 00:11:01.142 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [85.1, 48.3]    | -> Neymar da Silv |
| -2219.56 | -2219.56 | 00:11:03.074 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [95.6, 18.8]    |  |
| -2219.56 | -2219.56 | 00:11:03.074 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [95.6, 18.8]    |  |
| -2218.48 | -2218.48 | 00:11:04.157 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [94.2, 21.9]    | -> Kylian Mbappé  |
| -2218.18 | -2218.18 | 00:11:04.458 | Saint-Étienne      | Paris Saint-Germai | 97 | Pressure        |   -   | [16.7, 47.0]    |  |
| -2217.87 | -2217.87 | 00:11:04.770 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [100.1, 31.7]   |  |
| -2217.87 | -2217.87 | 00:11:04.770 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [99.2, 30.6]    | Incomplete (Incomplete) |
| -2216.57 | -2216.57 | 00:11:06.066 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pressure        |   -   | [96.2, 39.5]    |  |
| -2216.23 | -2216.23 | 00:11:06.410 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [97.6, 38.8]    | Incomplete |
| -2216.23 | -2216.23 | 00:11:06.410 | Saint-Étienne      | Paris Saint-Germai | 97 | Clearance       |   -   | [20.1, 40.6]    |  |
| -2215.05 | -2215.05 | 00:11:07.584 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pressure        |   -   | [82.9, 35.2]    |  |
| -2214.36 | -2214.36 | 00:11:08.276 | Saint-Étienne      | Paris Saint-Germai | 97 | Ball Recovery   |   -   | [34.8, 47.0]    |  |
| -2214.36 | -2214.36 | 00:11:08.276 | Saint-Étienne      | Paris Saint-Germai | 97 | Carry           |   -   | [34.8, 47.0]    |  |
| -2210.12 | -2210.12 | 00:11:12.517 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pressure        |  Yes  | [85.7, 9.4]     |  |
| -2209.28 | -2209.28 | 00:11:13.361 | Saint-Étienne      | Paris Saint-Germai | 97 | Dribble         |   -   | [34.5, 73.7]    |  |
| -2209.28 | -2209.28 | 00:11:13.361 | Paris Saint-Germai | Paris Saint-Germai | 97 | Duel            |   -   | [85.6, 6.4]     | Tackle, Success In Play |
| -2208.27 | -2208.27 | 00:11:14.367 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [83.9, 5.5]     | -> Sergio Ramos G |
| -2207.17 | -2207.17 | 00:11:15.472 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [69.8, 6.3]     |  |
| -2207.17 | -2207.17 | 00:11:15.472 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [69.8, 6.3]     |  |
| -2206.47 | -2206.47 | 00:11:16.171 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [69.8, 6.3]     | -> Ángel Fabián D |
| -2205.58 | -2205.58 | 00:11:17.056 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [77.9, 23.3]    |  |
| -2205.58 | -2205.58 | 00:11:17.056 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [77.9, 23.3]    |  |
| -2204.96 | -2204.96 | 00:11:17.681 | Saint-Étienne      | Paris Saint-Germai | 97 | Pressure        |   -   | [39.2, 60.2]    |  |
| -2204.18 | -2204.18 | 00:11:18.460 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [77.9, 24.7]    | -> Marcos Aoás Co |
| -2202.25 | -2202.25 | 00:11:20.385 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [73.1, 46.3]    |  |
| -2202.25 | -2202.25 | 00:11:20.385 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [73.1, 46.3]    |  |
| -2200.28 | -2200.28 | 00:11:22.361 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [79.3, 44.9]    | -> Lionel Andrés  |
| -2199.13 | -2199.13 | 00:11:23.505 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [84.7, 29.4]    |  |
| -2199.13 | -2199.13 | 00:11:23.505 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [84.7, 29.4]    |  |
| -2198.03 | -2198.03 | 00:11:24.611 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [84.7, 29.4]    | -> Neymar da Silv |
| -2197.64 | -2197.64 | 00:11:24.993 | Saint-Étienne      | Paris Saint-Germai | 97 | Pressure        |   -   | [23.4, 52.4]    |  |
| -2197.31 | -2197.31 | 00:11:25.325 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [95.4, 28.0]    |  |
| -2197.31 | -2197.31 | 00:11:25.325 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [96.1, 27.7]    | -> Lionel Andrés  |
| -2196.59 | -2196.59 | 00:11:26.049 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [87.2, 27.7]    |  |
| -2196.59 | -2196.59 | 00:11:26.049 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [87.2, 27.7]    |  |
| -2196.55 | -2196.55 | 00:11:26.089 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [87.2, 27.7]    | -> Juan Bernat Ve |
| -2192.88 | -2192.88 | 00:11:29.763 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [116.5, 14.1]   |  |
| -2192.88 | -2192.88 | 00:11:29.763 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [116.8, 14.1]   | Incomplete (Incomplete) |
| -2191.13 | -2191.13 | 00:11:31.505 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [109.7, 45.3]   | Incomplete |
| -2191.13 | -2191.13 | 00:11:31.505 | Paris Saint-Germai | Paris Saint-Germai | 97 | Duel            |   -   | [109.7, 44.4]   | Aerial Lost |
| -2191.13 | -2191.13 | 00:11:31.505 | Saint-Étienne      | Paris Saint-Germai | 97 | Clearance       |   -   | [10.4, 35.7]    |  |
| -2189.19 | -2189.19 | 00:11:33.449 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Recovery   |   -   | [98.6, 50.2]    |  |
| -2189.16 | -2189.16 | 00:11:33.474 | Paris Saint-Germai | Paris Saint-Germai | 97 | Shot            |   -   | [97.2, 47.6]    | Wayward |
| -2188.14 | -2188.14 | 00:11:34.501 | Saint-Étienne      | Paris Saint-Germai | 97 | Goal Keeper     |   -   | [2.1, 39.1]     |  |
| -2187.77 | -2187.77 | 00:11:34.864 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [105.1, 35.2]   | -> Lionel Andrés  |
| -2186.86 | -2186.86 | 00:11:35.776 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [99.5, 39.5]    |  |
| -2186.86 | -2186.86 | 00:11:35.776 | Paris Saint-Germai | Paris Saint-Germai | 97 | Shot            |   -   | [99.8, 37.1]    | Blocked |
| -2186.47 | -2186.47 | 00:11:36.165 | Saint-Étienne      | Paris Saint-Germai | 97 | Block           |   -   | [12.5, 42.5]    |  |
| -2186.39 | -2186.39 | 00:11:36.245 | Saint-Étienne      | Paris Saint-Germai | 97 | Goal Keeper     |   -   | [2.3, 40.1]     |  |
| -2185.61 | -2185.61 | 00:11:37.031 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Recovery   |   -   | [104.5, 41.4]   |  |
| -2185.61 | -2185.61 | 00:11:37.031 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [104.5, 41.4]   |  |
| -2185.56 | -2185.56 | 00:11:37.082 | Saint-Étienne      | Paris Saint-Germai | 97 | Pressure        |   -   | [14.2, 36.5]    |  |
| -2185.13 | -2185.13 | 00:11:37.512 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [104.2, 44.1]   | -> Achraf Hakimi  |
| -2183.53 | -2183.53 | 00:11:39.103 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [111.2, 53.8]   |  |
| -2183.53 | -2183.53 | 00:11:39.103 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [111.2, 53.8]   |  |
| -2182.70 | -2182.70 | 00:11:39.938 | Paris Saint-Germai | Paris Saint-Germai | 97 | Shot            |   -   | [107.5, 49.7]   | Blocked |
| -2182.51 | -2182.51 | 00:11:40.128 | Saint-Étienne      | Paris Saint-Germai | 97 | Block           |   -   | [11.4, 31.8]    |  |
| -2182.43 | -2182.43 | 00:11:40.208 | Saint-Étienne      | Paris Saint-Germai | 97 | Goal Keeper     |   -   | [3.1, 37.2]     |  |
| -2182.35 | -2182.35 | 00:11:40.285 | Paris Saint-Germai | Paris Saint-Germai | 97 | Block           |   -   | [107.8, 48.1]   |  |
| -2180.56 | -2180.56 | 00:11:42.081 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [97.9, 51.6]    | -> Ángel Fabián D |
| -2179.52 | -2179.52 | 00:11:43.122 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [98.2, 61.0]    |  |
| -2179.52 | -2179.52 | 00:11:43.122 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [98.2, 61.0]    |  |
| -2178.72 | -2178.72 | 00:11:43.916 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [98.2, 61.0]    | Incomplete (Incomplete) |
| -2177.86 | -2177.86 | 00:11:44.774 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [107.5, 45.3]   | Incomplete |
| -2177.86 | -2177.86 | 00:11:44.774 | Saint-Étienne      | Paris Saint-Germai | 97 | Clearance       |   -   | [14.2, 33.2]    |  |
| -2175.86 | -2175.86 | 00:11:46.781 | Saint-Étienne      | Paris Saint-Germai | 97 | Clearance       |   -   | [16.7, 53.7]    |  |
| -2173.79 | -2173.79 | 00:11:48.852 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Recovery   |   -   | [83.7, 18.8]    |  |
| -2173.79 | -2173.79 | 00:11:48.852 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [83.7, 18.8]    |  |
| -2172.00 | -2172.00 | 00:11:50.640 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [83.2, 18.9]    | -> Kylian Mbappé  |
| -2171.16 | -2171.16 | 00:11:51.482 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [94.0, 21.9]    |  |
| -2171.16 | -2171.16 | 00:11:51.482 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [94.0, 21.9]    |  |
| -2169.15 | -2169.15 | 00:11:53.491 | Paris Saint-Germai | Paris Saint-Germai | 97 | Pass            |   -   | [93.1, 24.9]    | -> Lionel Andrés  |
| -2168.54 | -2168.54 | 00:11:54.095 | Paris Saint-Germai | Paris Saint-Germai | 97 | Ball Receipt*   |   -   | [96.7, 31.0]    |  |
| -2168.54 | -2168.54 | 00:11:54.095 | Paris Saint-Germai | Paris Saint-Germai | 97 | Carry           |   -   | [96.7, 31.0]    |  |
| -2168.24 | -2168.24 | 00:11:54.402 | Saint-Étienne      | Paris Saint-Germai | 97 | Pressure        |   -   | [21.2, 49.5]    |  |
| -2167.75 | -2167.75 | 00:11:54.886 | Paris Saint-Germai | Paris Saint-Germai | 97 | Dispossessed    |   -   | [98.7, 29.7]    |  |
| -2167.75 | -2167.75 | 00:11:54.886 | Saint-Étienne      | Saint-Étienne      | 98 | Duel            |  Yes  | [21.4, 50.4]    | Tackle, Success In Play |
| -2166.36 | -2166.36 | 00:11:56.283 | Saint-Étienne      | Saint-Étienne      | 98 | Ball Recovery   |   -   | [31.1, 47.4]    |  |
| -2166.36 | -2166.36 | 00:11:56.283 | Saint-Étienne      | Saint-Étienne      | 98 | Carry           |   -   | [31.1, 47.4]    |  |
| -2163.03 | -2163.03 | 00:11:59.604 | Saint-Étienne      | Saint-Étienne      | 98 | Pass            |   -   | [39.7, 41.3]    | -> Denis Bouanga |
| -2160.09 | -2160.09 | 00:12:02.546 | Saint-Étienne      | Saint-Étienne      | 98 | Ball Receipt*   |   -   | [83.3, 13.8]    |  |
| -2160.09 | -2160.09 | 00:12:02.546 | Saint-Étienne      | Saint-Étienne      | 98 | Carry           |   -   | [83.3, 13.8]    |  |
| -2155.66 | -2155.66 | 00:12:06.982 | Paris Saint-Germai | Saint-Étienne      | 98 | Dribbled Past   |   -   | [22.3, 58.1]    |  |
| -2155.66 | -2155.66 | 00:12:06.982 | Saint-Étienne      | Saint-Étienne      | 98 | Dribble         |   -   | [97.8, 22.0]    |  |
| -2155.66 | -2155.66 | 00:12:06.982 | Saint-Étienne      | Saint-Étienne      | 98 | Carry           |   -   | [97.8, 22.0]    |  |
| -2154.56 | -2154.56 | 00:12:08.074 | Paris Saint-Germai | Saint-Étienne      | 98 | Pressure        |   -   | [12.6, 53.9]    |  |
| -2154.16 | -2154.16 | 00:12:08.481 | Saint-Étienne      | Saint-Étienne      | 98 | Shot            |   -   | [107.5, 24.9]   | Blocked |
| -2154.06 | -2154.06 | 00:12:08.576 | Paris Saint-Germai | Saint-Étienne      | 98 | Block           |   -   | [11.6, 54.0]    |  |
| -2153.96 | -2153.96 | 00:12:08.676 | Paris Saint-Germai | Saint-Étienne      | 98 | Goal Keeper     |   -   | [2.0, 43.1]     |  |
| -2109.64 | -2109.64 | 00:12:52.999 | Saint-Étienne      | Saint-Étienne      | 99 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete) |
| -2108.50 | -2108.50 | 00:12:54.139 | Paris Saint-Germai | Saint-Étienne      | 99 | Clearance       |   -   | [2.0, 45.6]     |  |
| -2091.51 | -2091.51 | 00:13:11.124 | Saint-Étienne      | Saint-Étienne      | 100 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Out) |
| -2084.30 | -2084.30 | 00:13:18.333 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [6.0, 44.0]     | -> Sergio Ramos G |
| -2082.12 | -2082.12 | 00:13:20.520 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [30.4, 24.9]    |  |
| -2075.83 | -2075.83 | 00:13:26.811 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [40.7, 21.4]    | -> Juan Bernat Ve |
| -2073.76 | -2073.76 | 00:13:28.876 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [55.9, 4.5]     |  |
| -2073.76 | -2073.76 | 00:13:28.876 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [55.9, 4.5]     |  |
| -2072.16 | -2072.16 | 00:13:30.479 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [62.6, 6.6]     | -> Idrissa Gana G |
| -2070.50 | -2070.50 | 00:13:32.139 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [58.9, 22.7]    |  |
| -2070.50 | -2070.50 | 00:13:32.139 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [58.9, 22.7]    |  |
| -2069.06 | -2069.06 | 00:13:33.575 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [61.5, 24.4]    | -> Ángel Fabián D |
| -2067.72 | -2067.72 | 00:13:34.913 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [62.8, 43.5]    |  |
| -2067.72 | -2067.72 | 00:13:34.913 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [62.8, 43.5]    |  |
| -2066.58 | -2066.58 | 00:13:36.057 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [65.6, 46.9]    | -> Lionel Andrés  |
| -2065.13 | -2065.13 | 00:13:37.507 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [71.4, 70.3]    |  |
| -2065.13 | -2065.13 | 00:13:37.507 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [71.4, 70.3]    |  |
| -2061.32 | -2061.32 | 00:13:41.323 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [75.1, 45.6]    | -> Kylian Mbappé  |
| -2060.68 | -2060.68 | 00:13:41.962 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [82.0, 41.6]    |  |
| -2060.68 | -2060.68 | 00:13:41.962 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [84.2, 40.5]    | -> Ángel Fabián D |
| -2059.27 | -2059.27 | 00:13:43.371 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [83.2, 54.5]    |  |
| -2059.27 | -2059.27 | 00:13:43.371 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [83.2, 54.5]    |  |
| -2057.16 | -2057.16 | 00:13:45.474 | Saint-Étienne      | Paris Saint-Germai | 101 | Pressure        |   -   | [34.2, 25.2]    |  |
| -2056.79 | -2056.79 | 00:13:45.852 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [83.2, 55.3]    | -> Achraf Hakimi  |
| -2054.90 | -2054.90 | 00:13:47.741 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [99.2, 70.3]    |  |
| -2054.90 | -2054.90 | 00:13:47.741 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [99.2, 70.3]    |  |
| -2054.13 | -2054.13 | 00:13:48.506 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [98.9, 73.1]    | -> Ángel Fabián D |
| -2053.38 | -2053.38 | 00:13:49.262 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [98.6, 66.0]    |  |
| -2053.38 | -2053.38 | 00:13:49.262 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [98.6, 66.0]    | -> Achraf Hakimi  |
| -2052.42 | -2052.42 | 00:13:50.217 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [98.6, 75.5]    |  |
| -2052.42 | -2052.42 | 00:13:50.217 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [98.6, 75.5]    |  |
| -2051.84 | -2051.84 | 00:13:50.801 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [98.6, 75.5]    | -> Marcos Aoás Co |
| -2050.30 | -2050.30 | 00:13:52.342 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [81.4, 69.5]    |  |
| -2050.30 | -2050.30 | 00:13:52.342 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [81.4, 69.5]    |  |
| -2049.32 | -2049.32 | 00:13:53.313 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [81.4, 66.9]    | -> Sergio Ramos G |
| -2047.82 | -2047.82 | 00:13:54.818 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [78.4, 29.9]    |  |
| -2047.82 | -2047.82 | 00:13:54.818 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [78.4, 29.9]    |  |
| -2046.46 | -2046.46 | 00:13:56.182 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [86.4, 27.2]    | -> Juan Bernat Ve |
| -2044.40 | -2044.40 | 00:13:58.235 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [106.5, 12.0]   |  |
| -2044.40 | -2044.40 | 00:13:58.235 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [106.5, 12.0]   |  |
| -2042.39 | -2042.39 | 00:14:00.243 | Saint-Étienne      | Paris Saint-Germai | 101 | Pressure        |   -   | [15.9, 70.7]    |  |
| -2040.45 | -2040.45 | 00:14:02.189 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [97.9, 15.5]    | -> Sergio Ramos G |
| -2039.70 | -2039.70 | 00:14:02.941 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [91.1, 20.2]    |  |
| -2039.70 | -2039.70 | 00:14:02.941 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [91.1, 20.2]    |  |
| -2039.52 | -2039.52 | 00:14:03.121 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [91.1, 20.2]    | -> Neymar da Silv |
| -2038.23 | -2038.23 | 00:14:04.404 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [97.5, 6.4]     |  |
| -2038.23 | -2038.23 | 00:14:04.404 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [97.5, 6.4]     |  |
| -2034.80 | -2034.80 | 00:14:07.834 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [92.3, 24.7]    | Incomplete (Incomplete) |
| -2033.53 | -2033.53 | 00:14:09.112 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [107.2, 61.0]   | Incomplete |
| -2033.53 | -2033.53 | 00:14:09.112 | Saint-Étienne      | Paris Saint-Germai | 101 | Clearance       |   -   | [14.7, 32.1]    |  |
| -2033.45 | -2033.45 | 00:14:09.189 | Saint-Étienne      | Paris Saint-Germai | 101 | Error           |   -   | [14.4, 33.8]    |  |
| -2031.14 | -2031.14 | 00:14:11.495 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Recovery   |   -   | [113.6, 30.3]   |  |
| -2031.13 | -2031.13 | 00:14:11.511 | Paris Saint-Germai | Paris Saint-Germai | 101 | Shot            |   -   | [113.0, 30.9]   | Wayward |
| -2029.56 | -2029.56 | 00:14:13.074 | Saint-Étienne      | Paris Saint-Germai | 101 | Goal Keeper     |   -   | [2.3, 43.4]     |  |
| -1999.22 | -1999.22 | 00:14:43.419 | Saint-Étienne      | Saint-Étienne      | 102 | Pass            |   -   | [7.0, 36.1]     | -> Denis Bouanga |
| -1995.00 | -1995.00 | 00:14:47.639 | Saint-Étienne      | Saint-Étienne      | 102 | Ball Receipt*   |   -   | [54.7, 3.1]     |  |
| -1995.00 | -1995.00 | 00:14:47.639 | Saint-Étienne      | Saint-Étienne      | 102 | Pass            |   -   | [54.7, 3.1]     | Incomplete (Incomplete) |
| -1993.02 | -1993.02 | 00:14:49.613 | Saint-Étienne      | Saint-Étienne      | 102 | Ball Receipt*   |   -   | [65.3, 17.0]    | Incomplete |
| -1993.02 | -1993.02 | 00:14:49.613 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [53.2, 66.0]    | -> Lionel Andrés  |
| -1991.58 | -1991.58 | 00:14:51.057 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [74.2, 54.9]    |  |
| -1991.58 | -1991.58 | 00:14:51.057 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [73.4, 54.9]    | -> Kylian Mbappé  |
| -1990.22 | -1990.22 | 00:14:52.415 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [76.4, 41.0]    |  |
| -1990.22 | -1990.22 | 00:14:52.415 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [77.2, 42.2]    | -> Neymar da Silv |
| -1987.96 | -1987.96 | 00:14:54.676 | Saint-Étienne      | Paris Saint-Germai | 103 | Pressure        |   -   | [50.9, 51.6]    |  |
| -1987.59 | -1987.59 | 00:14:55.043 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [71.4, 26.6]    |  |
| -1987.59 | -1987.59 | 00:14:55.043 | Paris Saint-Germai | Paris Saint-Germai | 103 | Carry           |   -   | [71.4, 26.6]    |  |
| -1987.23 | -1987.23 | 00:14:55.409 | Saint-Étienne      | Paris Saint-Germai | 103 | Dribbled Past   |   -   | [50.1, 54.8]    |  |
| -1987.23 | -1987.23 | 00:14:55.409 | Paris Saint-Germai | Paris Saint-Germai | 103 | Dribble         |   -   | [70.0, 25.3]    |  |
| -1987.23 | -1987.23 | 00:14:55.409 | Paris Saint-Germai | Paris Saint-Germai | 103 | Carry           |   -   | [70.0, 25.3]    |  |
| -1982.99 | -1982.99 | 00:14:59.647 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [77.3, 33.1]    | Incomplete (Incomplete) |
| -1979.92 | -1979.92 | 00:15:02.717 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [110.1, 46.7]   | Incomplete |
| -1979.92 | -1979.92 | 00:15:02.717 | Saint-Étienne      | Paris Saint-Germai | 103 | Interception    |   -   | [10.9, 33.4]    | Lost In Play |
| -1978.86 | -1978.86 | 00:15:03.780 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Recovery   |   -   | [113.6, 46.0]   |  |
| -1978.83 | -1978.83 | 00:15:03.804 | Paris Saint-Germai | Paris Saint-Germai | 103 | Shot            |   -   | [113.0, 45.7]   | Saved |
| -1978.21 | -1978.21 | 00:15:04.428 | Saint-Étienne      | Saint-Étienne      | 104 | Goal Keeper     |   -   | [3.6, 36.6]     |  |
| -1975.59 | -1975.59 | 00:15:07.047 | Saint-Étienne      | Saint-Étienne      | 105 | Pass            |   -   | [9.5, 33.2]     | -> Ryad Boudebouz |
| -1974.96 | -1974.96 | 00:15:07.676 | Saint-Étienne      | Saint-Étienne      | 105 | Ball Receipt*   |   -   | [27.8, 22.6]    |  |
| -1973.55 | -1973.55 | 00:15:09.090 | Paris Saint-Germai | Saint-Étienne      | 105 | Pressure        |   -   | [81.7, 58.8]    |  |
| -1969.84 | -1969.84 | 00:15:12.802 | Paris Saint-Germai | Saint-Étienne      | 105 | Foul Committed  |   -   | [79.3, 67.2]    |  |
| -1969.84 | -1969.84 | 00:15:12.802 | Saint-Étienne      | Saint-Étienne      | 105 | Foul Won        |   -   | [40.8, 12.9]    |  |
| -1958.41 | -1958.41 | 00:15:24.229 | Saint-Étienne      | Saint-Étienne      | 105 | Injury Stoppage |   -   | -               |  |
| -1956.06 | -1956.06 | 00:15:26.581 | Paris Saint-Germai | Saint-Étienne      | 105 | Injury Stoppage |   -   | -               |  |
| -1887.14 | -1887.14 | 00:16:35.493 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [43.7, 18.8]    | -> Miguel Ángel T |
| -1885.95 | -1885.95 | 00:16:36.685 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [53.1, 5.1]     |  |
| -1885.95 | -1885.95 | 00:16:36.685 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [53.1, 5.1]     |  |
| -1885.61 | -1885.61 | 00:16:37.023 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [64.0, 74.4]    |  |
| -1885.24 | -1885.24 | 00:16:37.398 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [52.8, 5.1]     | -> Ryad Boudebouz |
| -1883.74 | -1883.74 | 00:16:38.896 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [44.8, 12.4]    |  |
| -1883.74 | -1883.74 | 00:16:38.896 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [44.8, 12.4]    |  |
| -1883.59 | -1883.59 | 00:16:39.052 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [71.8, 69.9]    |  |
| -1882.04 | -1882.04 | 00:16:40.594 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [43.4, 16.5]    | -> Etienne Green |
| -1879.28 | -1879.28 | 00:16:43.360 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [11.4, 40.2]    |  |
| -1879.28 | -1879.28 | 00:16:43.360 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [11.4, 40.2]    |  |
| -1877.81 | -1877.81 | 00:16:44.828 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [12.8, 40.4]    | -> Miguel Ángel T |
| -1875.34 | -1875.34 | 00:16:47.296 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [56.4, 7.1]     |  |
| -1875.34 | -1875.34 | 00:16:47.296 | Paris Saint-Germai | Saint-Étienne      | 106 | Duel            |   -   | [63.7, 71.4]    | Aerial Lost |
| -1875.34 | -1875.34 | 00:16:47.296 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [56.4, 8.7]     | -> Wahbi Khazri |
| -1873.55 | -1873.55 | 00:16:49.087 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [63.9, 28.5]    |  |
| -1873.55 | -1873.55 | 00:16:49.087 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [63.9, 28.5]    |  |
| -1873.26 | -1873.26 | 00:16:49.375 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [57.0, 58.1]    |  |
| -1873.02 | -1873.02 | 00:16:49.617 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [64.2, 26.6]    | -> Mahdi Camara |
| -1872.44 | -1872.44 | 00:16:50.193 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [56.5, 25.9]    |  |
| -1872.44 | -1872.44 | 00:16:50.193 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [56.5, 25.9]    |  |
| -1872.04 | -1872.04 | 00:16:50.595 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [64.2, 51.6]    |  |
| -1871.29 | -1871.29 | 00:16:51.348 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [57.3, 22.7]    | -> Miguel Ángel T |
| -1870.97 | -1870.97 | 00:16:51.667 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [54.5, 67.2]    |  |
| -1870.70 | -1870.70 | 00:16:51.934 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [63.3, 13.2]    |  |
| -1870.70 | -1870.70 | 00:16:51.934 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [63.1, 12.9]    | -> Ryad Boudebouz |
| -1869.63 | -1869.63 | 00:16:53.003 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [51.9, 22.1]    |  |
| -1869.63 | -1869.63 | 00:16:53.003 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [51.9, 22.1]    |  |
| -1868.17 | -1868.17 | 00:16:54.467 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [55.3, 32.4]    | -> Yvann Macon |
| -1864.36 | -1864.36 | 00:16:58.281 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [94.5, 75.2]    |  |
| -1864.36 | -1864.36 | 00:16:58.281 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [94.5, 75.2]    |  |
| -1860.78 | -1860.78 | 00:17:01.861 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [26.4, 11.1]    |  |
| -1860.41 | -1860.41 | 00:17:02.225 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [94.0, 69.0]    | -> Mahdi Camara |
| -1859.30 | -1859.30 | 00:17:03.340 | Paris Saint-Germai | Saint-Étienne      | 106 | Pressure        |   -   | [20.3, 27.8]    |  |
| -1859.26 | -1859.26 | 00:17:03.374 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [100.1, 54.6]   |  |
| -1859.26 | -1859.26 | 00:17:03.374 | Saint-Étienne      | Saint-Étienne      | 106 | Carry           |   -   | [100.1, 54.6]   |  |
| -1858.94 | -1858.94 | 00:17:03.697 | Saint-Étienne      | Saint-Étienne      | 106 | Pass            |   -   | [99.5, 52.7]    | Incomplete (Incomplete) |
| -1858.73 | -1858.73 | 00:17:03.910 | Saint-Étienne      | Saint-Étienne      | 106 | Ball Receipt*   |   -   | [105.0, 39.9]   | Incomplete |
| -1858.73 | -1858.73 | 00:17:03.910 | Paris Saint-Germai | Saint-Étienne      | 106 | Block           |   -   | [16.7, 28.8]    |  |
| -1857.16 | -1857.16 | 00:17:05.480 | Paris Saint-Germai | Paris Saint-Germai | 107 | Ball Recovery   |   -   | [23.6, 28.8]    |  |
| -1857.16 | -1857.16 | 00:17:05.480 | Paris Saint-Germai | Paris Saint-Germai | 107 | Carry           |   -   | [23.6, 28.8]    |  |
| -1855.83 | -1855.83 | 00:17:06.804 | Paris Saint-Germai | Paris Saint-Germai | 107 | Pass            |   -   | [30.1, 31.7]    | -> Lionel Andrés  |
| -1854.27 | -1854.27 | 00:17:08.366 | Paris Saint-Germai | Paris Saint-Germai | 107 | Ball Receipt*   |   -   | [52.6, 32.4]    |  |
| -1854.27 | -1854.27 | 00:17:08.366 | Paris Saint-Germai | Paris Saint-Germai | 107 | Pass            |   -   | [52.6, 32.4]    | -> Neymar da Silv |
| -1853.38 | -1853.38 | 00:17:09.259 | Paris Saint-Germai | Paris Saint-Germai | 107 | Ball Receipt*   |   -   | [62.9, 22.2]    |  |
| -1853.38 | -1853.38 | 00:17:09.259 | Paris Saint-Germai | Paris Saint-Germai | 107 | Carry           |   -   | [62.9, 22.2]    |  |
| -1852.80 | -1852.80 | 00:17:09.833 | Saint-Étienne      | Paris Saint-Germai | 107 | Pressure        |  Yes  | [61.9, 56.3]    |  |
| -1851.83 | -1851.83 | 00:17:10.805 | Saint-Étienne      | Paris Saint-Germai | 107 | Dribbled Past   |   -   | [57.2, 59.0]    |  |
| -1851.83 | -1851.83 | 00:17:10.805 | Paris Saint-Germai | Paris Saint-Germai | 107 | Dribble         |   -   | [62.9, 21.1]    |  |
| -1851.28 | -1851.28 | 00:17:11.361 | Paris Saint-Germai | Paris Saint-Germai | 107 | Pressure        |   -   | [61.5, 21.1]    |  |
| -1850.85 | -1850.85 | 00:17:11.790 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Recovery   |   -   | [64.7, 60.1]    |  |
| -1850.85 | -1850.85 | 00:17:11.790 | Saint-Étienne      | Saint-Étienne      | 108 | Carry           |   -   | [64.7, 60.1]    |  |
| -1847.67 | -1847.67 | 00:17:14.966 | Paris Saint-Germai | Saint-Étienne      | 108 | Pressure        |  Yes  | [62.2, 6.9]     |  |
| -1847.30 | -1847.30 | 00:17:15.333 | Saint-Étienne      | Saint-Étienne      | 108 | Pass            |   -   | [54.7, 76.3]    | -> Zaydou Youssou |
| -1846.38 | -1846.38 | 00:17:16.261 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Receipt*   |   -   | [51.4, 76.3]    |  |
| -1846.38 | -1846.38 | 00:17:16.261 | Saint-Étienne      | Saint-Étienne      | 108 | Carry           |   -   | [51.4, 76.3]    |  |
| -1841.78 | -1841.78 | 00:17:20.857 | Paris Saint-Germai | Saint-Étienne      | 108 | Pressure        |   -   | [51.7, 20.8]    |  |
| -1841.15 | -1841.15 | 00:17:21.486 | Saint-Étienne      | Saint-Étienne      | 108 | Pass            |   -   | [64.5, 60.9]    | -> Ryad Boudebouz |
| -1840.36 | -1840.36 | 00:17:22.282 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Receipt*   |   -   | [52.8, 62.9]    |  |
| -1840.36 | -1840.36 | 00:17:22.282 | Saint-Étienne      | Saint-Étienne      | 108 | Carry           |   -   | [52.8, 62.9]    |  |
| -1839.57 | -1839.57 | 00:17:23.070 | Paris Saint-Germai | Saint-Étienne      | 108 | Pressure        |   -   | [64.7, 18.1]    |  |
| -1839.33 | -1839.33 | 00:17:23.307 | Saint-Étienne      | Saint-Étienne      | 108 | Pass            |   -   | [54.0, 63.2]    | -> Harold Moukoud |
| -1838.27 | -1838.27 | 00:17:24.371 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Receipt*   |   -   | [36.9, 62.0]    |  |
| -1838.27 | -1838.27 | 00:17:24.371 | Saint-Étienne      | Saint-Étienne      | 108 | Carry           |   -   | [36.9, 62.0]    |  |
| -1837.13 | -1837.13 | 00:17:25.509 | Saint-Étienne      | Saint-Étienne      | 108 | Pass            |   -   | [36.9, 62.0]    | -> Miguel Ángel T |
| -1834.37 | -1834.37 | 00:17:28.273 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Receipt*   |   -   | [63.9, 12.0]    |  |
| -1834.37 | -1834.37 | 00:17:28.273 | Saint-Étienne      | Saint-Étienne      | 108 | Carry           |   -   | [63.9, 12.0]    |  |
| -1827.16 | -1827.16 | 00:17:35.477 | Paris Saint-Germai | Saint-Étienne      | 108 | Pressure        |   -   | [9.3, 56.7]     |  |
| -1826.60 | -1826.60 | 00:17:36.036 | Saint-Étienne      | Saint-Étienne      | 108 | Pass            |   -   | [111.4, 20.9]   | Incomplete (Incomplete) |
| -1826.33 | -1826.33 | 00:17:36.311 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Receipt*   |   -   | [106.9, 33.2]   | Incomplete |
| -1826.33 | -1826.33 | 00:17:36.311 | Paris Saint-Germai | Saint-Étienne      | 108 | Block           |   -   | [10.0, 57.4]    |  |
| -1824.77 | -1824.77 | 00:17:37.865 | Saint-Étienne      | Saint-Étienne      | 108 | Ball Recovery   |   -   | [102.2, 33.5]   |  |
| -1824.54 | -1824.54 | 00:17:38.102 | Saint-Étienne      | Saint-Étienne      | 108 | Shot            |   -   | [102.1, 32.9]   | Saved |
| -1823.78 | -1823.78 | 00:17:38.854 | Paris Saint-Germai | Paris Saint-Germai | 109 | Goal Keeper     |   -   | [1.6, 41.7]     |  |
| -1818.43 | -1818.43 | 00:17:44.205 | Paris Saint-Germai | Paris Saint-Germai | 110 | Pass            |   -   | [12.8, 44.9]    | -> Juan Bernat Ve |
| -1815.63 | -1815.63 | 00:17:47.005 | Paris Saint-Germai | Paris Saint-Germai | 110 | Ball Receipt*   |   -   | [30.3, 5.0]     |  |
| -1804.70 | -1804.70 | 00:17:57.933 | Paris Saint-Germai | Paris Saint-Germai | 111 | Pass            |   -   | [55.1, 6.6]     | -> Sergio Ramos G |
| -1803.56 | -1803.56 | 00:17:59.079 | Paris Saint-Germai | Paris Saint-Germai | 111 | Ball Receipt*   |   -   | [48.2, 18.6]    |  |
| -1803.56 | -1803.56 | 00:17:59.079 | Paris Saint-Germai | Paris Saint-Germai | 111 | Carry           |   -   | [48.2, 18.6]    |  |
| -1802.37 | -1802.37 | 00:18:00.264 | Paris Saint-Germai | Paris Saint-Germai | 112 | Pass            |   -   | [48.4, 18.8]    | -> Danilo Luís Hé |
| -1801.50 | -1801.50 | 00:18:01.133 | Paris Saint-Germai | Paris Saint-Germai | 112 | Ball Receipt*   |   -   | [47.0, 27.7]    |  |
| -1801.50 | -1801.50 | 00:18:01.133 | Paris Saint-Germai | Paris Saint-Germai | 112 | Carry           |   -   | [47.0, 27.7]    |  |
| -1800.19 | -1800.19 | 00:18:02.452 | Paris Saint-Germai | Paris Saint-Germai | 113 | Pass            |   -   | [49.8, 29.1]    | -> Lionel Andrés  |
| -1798.21 | -1798.21 | 00:18:04.424 | Paris Saint-Germai | Paris Saint-Germai | 113 | Ball Receipt*   |   -   | [60.7, 59.1]    |  |
| -1798.21 | -1798.21 | 00:18:04.424 | Paris Saint-Germai | Paris Saint-Germai | 113 | Carry           |   -   | [60.7, 59.1]    |  |
| -1796.60 | -1796.60 | 00:18:06.034 | Paris Saint-Germai | Paris Saint-Germai | 114 | Pass            |   -   | [72.6, 57.8]    | -> Ángel Fabián D |
| -1795.23 | -1795.23 | 00:18:07.405 | Paris Saint-Germai | Paris Saint-Germai | 114 | Ball Receipt*   |   -   | [83.7, 71.7]    |  |
| -1795.23 | -1795.23 | 00:18:07.405 | Paris Saint-Germai | Paris Saint-Germai | 114 | Carry           |   -   | [83.7, 71.7]    |  |
| -1793.62 | -1793.62 | 00:18:09.016 | Paris Saint-Germai | Paris Saint-Germai | 115 | Pass            |   -   | [83.7, 71.7]    | -> Idrissa Gana G |
| -1792.01 | -1792.01 | 00:18:10.629 | Paris Saint-Germai | Paris Saint-Germai | 115 | Ball Receipt*   |   -   | [83.6, 52.0]    |  |
| -1792.01 | -1792.01 | 00:18:10.629 | Paris Saint-Germai | Paris Saint-Germai | 115 | Carry           |   -   | [83.6, 52.0]    |  |
| -1791.33 | -1791.33 | 00:18:11.307 | Paris Saint-Germai | Paris Saint-Germai | 116 | Pass            |   -   | [83.6, 52.0]    | -> Kylian Mbappé  |
| -1789.96 | -1789.96 | 00:18:12.676 | Paris Saint-Germai | Paris Saint-Germai | 116 | Ball Receipt*   |   -   | [83.7, 29.7]    |  |
| -1789.96 | -1789.96 | 00:18:12.676 | Paris Saint-Germai | Paris Saint-Germai | 116 | Carry           |   -   | [83.7, 29.7]    |  |
| -1788.26 | -1788.26 | 00:18:14.379 | Paris Saint-Germai | Paris Saint-Germai | 117 | Pass            |   -   | [85.3, 27.8]    | -> Juan Bernat Ve |
| -1785.89 | -1785.89 | 00:18:16.751 | Paris Saint-Germai | Paris Saint-Germai | 117 | Ball Receipt*   |   -   | [105.4, 5.6]    |  |
| -1785.89 | -1785.89 | 00:18:16.751 | Paris Saint-Germai | Paris Saint-Germai | 117 | Carry           |   -   | [105.4, 5.6]    |  |
| -1785.42 | -1785.42 | 00:18:17.216 | Saint-Étienne      | Paris Saint-Germai | 117 | Pressure        |  Yes  | [12.6, 72.9]    |  |
| -1784.53 | -1784.53 | 00:18:18.104 | Paris Saint-Germai | Paris Saint-Germai | 118 | Pass            |   -   | [105.1, 4.9]    | -> Kylian Mbappé  |
| -1783.04 | -1783.04 | 00:18:19.597 | Paris Saint-Germai | Paris Saint-Germai | 118 | Ball Receipt*   |   -   | [97.5, 6.6]     |  |
| -1783.04 | -1783.04 | 00:18:19.597 | Paris Saint-Germai | Paris Saint-Germai | 118 | Carry           |   -   | [97.5, 6.6]     |  |
| -1781.14 | -1781.14 | 00:18:21.501 | Paris Saint-Germai | Paris Saint-Germai | 119 | Pass            |   -   | [96.8, 10.3]    | -> Achraf Hakimi  |
| -1777.63 | -1777.63 | 00:18:25.003 | Paris Saint-Germai | Paris Saint-Germai | 119 | Ball Receipt*   |   -   | [73.2, 75.3]    |  |
| -1777.63 | -1777.63 | 00:18:25.003 | Paris Saint-Germai | Paris Saint-Germai | 119 | Carry           |   -   | [73.2, 75.3]    |  |
| -1775.99 | -1775.99 | 00:18:26.651 | Paris Saint-Germai | Paris Saint-Germai | 120 | Pass            |   -   | [75.9, 74.9]    | -> Ángel Fabián D |
| -1774.42 | -1774.42 | 00:18:28.220 | Paris Saint-Germai | Paris Saint-Germai | 120 | Ball Receipt*   |   -   | [93.1, 72.0]    |  |
| -1774.42 | -1774.42 | 00:18:28.220 | Paris Saint-Germai | Paris Saint-Germai | 120 | Carry           |   -   | [93.1, 72.0]    |  |
| -1770.52 | -1770.52 | 00:18:32.122 | Paris Saint-Germai | Paris Saint-Germai | 121 | Pass            |   -   | [88.4, 62.0]    | -> Danilo Luís Hé |
| -1768.63 | -1768.63 | 00:18:34.009 | Paris Saint-Germai | Paris Saint-Germai | 121 | Ball Receipt*   |   -   | [81.2, 41.6]    |  |
| -1768.63 | -1768.63 | 00:18:34.009 | Paris Saint-Germai | Paris Saint-Germai | 121 | Carry           |   -   | [81.2, 41.6]    |  |
| -1767.68 | -1767.68 | 00:18:34.953 | Paris Saint-Germai | Paris Saint-Germai | 122 | Pass            |   -   | [81.2, 39.2]    | -> Sergio Ramos G |
| -1766.26 | -1766.26 | 00:18:36.381 | Paris Saint-Germai | Paris Saint-Germai | 122 | Ball Receipt*   |   -   | [84.2, 24.4]    |  |
| -1766.26 | -1766.26 | 00:18:36.381 | Paris Saint-Germai | Paris Saint-Germai | 122 | Carry           |   -   | [84.2, 24.4]    |  |
| -1764.59 | -1764.59 | 00:18:38.047 | Paris Saint-Germai | Paris Saint-Germai | 123 | Pass            |   -   | [87.6, 24.7]    | -> Achraf Hakimi  |
| -1761.48 | -1761.48 | 00:18:41.158 | Paris Saint-Germai | Paris Saint-Germai | 123 | Ball Receipt*   |   -   | [104.7, 70.3]   |  |
| -1761.48 | -1761.48 | 00:18:41.158 | Paris Saint-Germai | Paris Saint-Germai | 123 | Carry           |   -   | [104.7, 70.3]   |  |
| -1758.52 | -1758.52 | 00:18:44.122 | Paris Saint-Germai | Paris Saint-Germai | 124 | Pass            |   -   | [109.0, 74.1]   | Incomplete (Incomplete) |
| -1758.31 | -1758.31 | 00:18:44.324 | Saint-Étienne      | Paris Saint-Germai | 124 | Block           |  Yes  | [10.9, 10.9]    |  |
| -1753.67 | -1753.67 | 00:18:48.963 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [112.3, 80.0]   | -> Ángel Fabián D |
| -1752.23 | -1752.23 | 00:18:50.410 | Saint-Étienne      | Paris Saint-Germai | 125 | Pressure        |   -   | [22.5, 12.0]    |  |
| -1752.02 | -1752.02 | 00:18:50.622 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [100.3, 73.5]   |  |
| -1752.02 | -1752.02 | 00:18:50.622 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [100.1, 75.3]   | -> Marcos Aoás Co |
| -1749.87 | -1749.87 | 00:18:52.766 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [84.3, 73.1]    |  |
| -1749.87 | -1749.87 | 00:18:52.766 | Paris Saint-Germai | Paris Saint-Germai | 125 | Carry           |   -   | [84.3, 73.1]    |  |
| -1749.17 | -1749.17 | 00:18:53.468 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [84.3, 73.1]    | -> Lionel Andrés  |
| -1747.47 | -1747.47 | 00:18:55.163 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [82.5, 46.1]    |  |
| -1747.47 | -1747.47 | 00:18:55.163 | Paris Saint-Germai | Paris Saint-Germai | 125 | Carry           |   -   | [82.5, 46.1]    |  |
| -1745.80 | -1745.80 | 00:18:56.834 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [87.8, 41.6]    | -> Neymar da Silv |
| -1745.39 | -1745.39 | 00:18:57.252 | Saint-Étienne      | Paris Saint-Germai | 125 | Pressure        |   -   | [21.2, 50.1]    |  |
| -1744.83 | -1744.83 | 00:18:57.808 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [96.4, 31.9]    |  |
| -1744.83 | -1744.83 | 00:18:57.808 | Paris Saint-Germai | Paris Saint-Germai | 125 | Carry           |   -   | [96.4, 31.9]    |  |
| -1744.26 | -1744.26 | 00:18:58.382 | Saint-Étienne      | Paris Saint-Germai | 125 | Dribbled Past   |   -   | [26.4, 49.6]    |  |
| -1744.26 | -1744.26 | 00:18:58.382 | Paris Saint-Germai | Paris Saint-Germai | 125 | Dribble         |   -   | [93.7, 30.5]    |  |
| -1744.26 | -1744.26 | 00:18:58.382 | Paris Saint-Germai | Paris Saint-Germai | 125 | Carry           |   -   | [93.7, 30.5]    |  |
| -1741.73 | -1741.73 | 00:19:00.909 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [94.2, 48.3]    | Incomplete (Incomplete) |
| -1740.54 | -1740.54 | 00:19:02.093 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [106.8, 48.1]   | Incomplete |
| -1740.54 | -1740.54 | 00:19:02.093 | Saint-Étienne      | Paris Saint-Germai | 125 | Clearance       |   -   | [14.0, 28.5]    |  |
| -1736.67 | -1736.67 | 00:19:05.963 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [81.1, 38.8]    | -> Danilo Luís Hé |
| -1731.83 | -1731.83 | 00:19:10.808 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [42.5, 27.2]    |  |
| -1731.83 | -1731.83 | 00:19:10.808 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [42.8, 14.1]    | -> Sergio Ramos G |
| -1730.33 | -1730.33 | 00:19:12.309 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [65.3, 5.0]     |  |
| -1730.33 | -1730.33 | 00:19:12.309 | Paris Saint-Germai | Paris Saint-Germai | 125 | Carry           |   -   | [65.3, 5.0]     |  |
| -1726.71 | -1726.71 | 00:19:15.923 | Paris Saint-Germai | Paris Saint-Germai | 125 | Pass            |   -   | [82.5, 10.5]    | Incomplete (Out) |
| -1723.95 | -1723.95 | 00:19:18.689 | Paris Saint-Germai | Paris Saint-Germai | 125 | Ball Receipt*   |   -   | [98.7, 16.3]    | Incomplete |
| -1694.05 | -1694.05 | 00:19:48.589 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [7.0, 36.1]     | -> Denis Bouanga |
| -1691.00 | -1691.00 | 00:19:51.641 | Saint-Étienne      | Saint-Étienne      | 126 | Ball Receipt*   |   -   | [64.7, 10.2]    |  |
| -1691.00 | -1691.00 | 00:19:51.641 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [64.5, 10.4]    | Incomplete (Incomplete) |
| -1691.00 | -1691.00 | 00:19:51.641 | Paris Saint-Germai | Saint-Étienne      | 126 | Duel            |   -   | [55.6, 69.7]    | Aerial Lost |
| -1688.41 | -1688.41 | 00:19:54.226 | Saint-Étienne      | Saint-Étienne      | 126 | Ball Receipt*   |   -   | [77.3, 33.8]    | Incomplete |
| -1688.41 | -1688.41 | 00:19:54.226 | Paris Saint-Germai | Saint-Étienne      | 126 | Clearance       |   -   | [42.8, 43.5]    |  |
| -1687.21 | -1687.21 | 00:19:55.425 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [65.1, 28.7]    | -> Zaydou Youssou |
| -1686.32 | -1686.32 | 00:19:56.322 | Paris Saint-Germai | Saint-Étienne      | 126 | Pressure        |   -   | [54.2, 41.6]    |  |
| -1685.94 | -1685.94 | 00:19:56.699 | Saint-Étienne      | Saint-Étienne      | 126 | Ball Receipt*   |   -   | [66.2, 39.9]    |  |
| -1685.94 | -1685.94 | 00:19:56.699 | Saint-Étienne      | Saint-Étienne      | 126 | Carry           |   -   | [66.2, 39.9]    |  |
| -1685.82 | -1685.82 | 00:19:56.822 | Paris Saint-Germai | Saint-Étienne      | 126 | Dribbled Past   |   -   | [55.1, 38.3]    |  |
| -1685.82 | -1685.82 | 00:19:56.822 | Saint-Étienne      | Saint-Étienne      | 126 | Dribble         |   -   | [65.0, 41.8]    |  |
| -1685.82 | -1685.82 | 00:19:56.822 | Saint-Étienne      | Saint-Étienne      | 126 | Carry           |   -   | [65.0, 41.8]    |  |
| -1684.24 | -1684.24 | 00:19:58.400 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [67.2, 37.7]    | -> Ryad Boudebouz |
| -1683.65 | -1683.65 | 00:19:58.989 | Saint-Étienne      | Saint-Étienne      | 126 | Ball Receipt*   |   -   | [64.2, 34.6]    |  |
| -1683.65 | -1683.65 | 00:19:58.989 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [63.1, 33.2]    | -> Yvann Macon |
| -1680.50 | -1680.50 | 00:20:02.134 | Saint-Étienne      | Saint-Étienne      | 126 | Ball Receipt*   |   -   | [82.8, 75.1]    |  |
| -1680.50 | -1680.50 | 00:20:02.134 | Saint-Étienne      | Saint-Étienne      | 126 | Carry           |   -   | [82.8, 75.1]    |  |
| -1674.41 | -1674.41 | 00:20:08.229 | Saint-Étienne      | Saint-Étienne      | 126 | Pass            |   -   | [109.0, 72.6]   | Incomplete (Incomplete) |
| -1674.33 | -1674.33 | 00:20:08.306 | Paris Saint-Germai | Saint-Étienne      | 126 | Block           |   -   | [10.0, 9.5]     |  |
| -1649.03 | -1649.03 | 00:20:33.610 | Saint-Étienne      | Saint-Étienne      | 127 | Pass            |   -   | [120.0, 80.0]   | Incomplete (Incomplete) |
| -1647.39 | -1647.39 | 00:20:35.247 | Paris Saint-Germai | Saint-Étienne      | 127 | Clearance       |   -   | [7.8, 44.2]     |  |
| -1645.26 | -1645.26 | 00:20:37.379 | Saint-Étienne      | Saint-Étienne      | 127 | Ball Recovery   |   -   | [94.5, 24.6]    |  |
| -1644.52 | -1644.52 | 00:20:38.114 | Saint-Étienne      | Saint-Étienne      | 127 | Pressure        |   -   | [94.5, 27.6]    |  |
| -1644.21 | -1644.21 | 00:20:38.425 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Recovery   |   -   | [25.1, 50.0]    |  |
| -1644.21 | -1644.21 | 00:20:38.425 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [25.1, 50.0]    |  |
| -1644.14 | -1644.14 | 00:20:38.501 | Saint-Étienne      | Paris Saint-Germai | 128 | Dribbled Past   |  Yes  | [94.0, 28.2]    |  |
| -1644.14 | -1644.14 | 00:20:38.501 | Paris Saint-Germai | Paris Saint-Germai | 128 | Dribble         |   -   | [26.1, 51.9]    |  |
| -1644.14 | -1644.14 | 00:20:38.501 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [26.1, 51.9]    |  |
| -1639.78 | -1639.78 | 00:20:42.858 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [51.2, 54.2]    | -> Kylian Mbappé  |
| -1637.76 | -1637.76 | 00:20:44.882 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [56.8, 26.0]    |  |
| -1637.76 | -1637.76 | 00:20:44.882 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [56.8, 26.0]    |  |
| -1635.65 | -1635.65 | 00:20:46.984 | Saint-Étienne      | Paris Saint-Germai | 128 | Dribbled Past   |   -   | [51.9, 56.3]    |  |
| -1635.65 | -1635.65 | 00:20:46.984 | Paris Saint-Germai | Paris Saint-Germai | 128 | Dribble         |   -   | [68.2, 23.8]    |  |
| -1635.65 | -1635.65 | 00:20:46.984 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [68.2, 23.8]    |  |
| -1632.42 | -1632.42 | 00:20:50.219 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [65.9, 38.5]    | -> Achraf Hakimi  |
| -1629.98 | -1629.98 | 00:20:52.662 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [91.1, 67.0]    |  |
| -1629.98 | -1629.98 | 00:20:52.662 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [91.1, 67.0]    |  |
| -1627.61 | -1627.61 | 00:20:55.029 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [96.2, 61.1]    | Incomplete (Incomplete) |
| -1627.02 | -1627.02 | 00:20:55.620 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [98.1, 51.9]    | Incomplete |
| -1627.02 | -1627.02 | 00:20:55.620 | Saint-Étienne      | Paris Saint-Germai | 128 | Interception    |   -   | [21.9, 27.6]    | Lost In Play |
| -1625.89 | -1625.89 | 00:20:56.747 | Saint-Étienne      | Paris Saint-Germai | 128 | Pressure        |   -   | [23.4, 24.6]    |  |
| -1625.72 | -1625.72 | 00:20:56.915 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Recovery   |   -   | [94.8, 56.0]    |  |
| -1625.72 | -1625.72 | 00:20:56.915 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [94.8, 56.0]    |  |
| -1623.50 | -1623.50 | 00:20:59.137 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [90.9, 48.8]    | -> Lionel Andrés  |
| -1622.77 | -1622.77 | 00:20:59.863 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [86.5, 39.1]    |  |
| -1622.77 | -1622.77 | 00:20:59.863 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [86.5, 39.1]    |  |
| -1621.97 | -1621.97 | 00:21:00.666 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [86.5, 39.1]    | -> Neymar da Silv |
| -1621.15 | -1621.15 | 00:21:01.488 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [98.6, 28.6]    |  |
| -1621.15 | -1621.15 | 00:21:01.488 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [98.6, 28.6]    |  |
| -1620.59 | -1620.59 | 00:21:02.045 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [99.5, 26.4]    | Incomplete (Incomplete) |
| -1619.58 | -1619.58 | 00:21:03.056 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [102.6, 35.8]   | Incomplete |
| -1619.58 | -1619.58 | 00:21:03.056 | Saint-Étienne      | Paris Saint-Germai | 128 | Interception    |   -   | [17.5, 44.5]    | Success In Play |
| -1616.53 | -1616.53 | 00:21:06.104 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Recovery   |   -   | [3.3, 52.7]     |  |
| -1606.57 | -1606.57 | 00:21:16.063 | Saint-Étienne      | Saint-Étienne      | 129 | Pass            |   -   | [12.2, 48.2]    | -> Miguel Ángel T |
| -1604.02 | -1604.02 | 00:21:18.622 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Receipt*   |   -   | [33.1, 8.5]     |  |
| -1602.38 | -1602.38 | 00:21:20.256 | Saint-Étienne      | Saint-Étienne      | 129 | Pass            |   -   | [32.9, 9.0]     | -> Wahbi Khazri |
| -1601.29 | -1601.29 | 00:21:21.347 | Paris Saint-Germai | Saint-Étienne      | 129 | Pressure        |   -   | [67.6, 58.8]    |  |
| -1600.93 | -1600.93 | 00:21:21.704 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Receipt*   |   -   | [50.3, 20.7]    |  |
| -1600.93 | -1600.93 | 00:21:21.704 | Saint-Étienne      | Saint-Étienne      | 129 | Pass            |   -   | [50.0, 20.2]    | -> Ryad Boudebouz |
| -1599.05 | -1599.05 | 00:21:23.590 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Receipt*   |   -   | [32.3, 22.1]    |  |
| -1599.05 | -1599.05 | 00:21:23.590 | Saint-Étienne      | Saint-Étienne      | 129 | Carry           |   -   | [32.3, 22.1]    |  |
| -1596.40 | -1596.40 | 00:21:26.239 | Saint-Étienne      | Saint-Étienne      | 129 | Pass            |   -   | [37.6, 20.2]    | -> Wahbi Khazri |
| -1595.53 | -1595.53 | 00:21:27.106 | Paris Saint-Germai | Saint-Étienne      | 129 | Pressure        |   -   | [70.1, 71.7]    |  |
| -1595.41 | -1595.41 | 00:21:27.227 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Receipt*   |   -   | [50.3, 7.1]     |  |
| -1595.41 | -1595.41 | 00:21:27.227 | Saint-Étienne      | Saint-Étienne      | 129 | Carry           |   -   | [50.3, 7.1]     |  |
| -1592.64 | -1592.64 | 00:21:29.996 | Saint-Étienne      | Saint-Étienne      | 129 | Pass            |   -   | [37.8, 5.2]     | Incomplete (Incomplete) |
| -1589.76 | -1589.76 | 00:21:32.880 | Saint-Étienne      | Saint-Étienne      | 129 | Ball Receipt*   |   -   | [35.9, 62.9]    | Incomplete |
| -1589.76 | -1589.76 | 00:21:32.880 | Paris Saint-Germai | Paris Saint-Germai | 130 | Pass            |   -   | [85.0, 23.9]    | -> Juan Bernat Ve |
| -1587.52 | -1587.52 | 00:21:35.117 | Saint-Étienne      | Paris Saint-Germai | 130 | Pressure        |  Yes  | [50.3, 56.6]    |  |
| -1587.08 | -1587.08 | 00:21:35.560 | Paris Saint-Germai | Paris Saint-Germai | 130 | Ball Receipt*   |   -   | [68.9, 24.9]    |  |
| -1587.08 | -1587.08 | 00:21:35.560 | Paris Saint-Germai | Paris Saint-Germai | 130 | Pass            |   -   | [69.5, 24.7]    | -> Sergio Ramos G |
| -1585.96 | -1585.96 | 00:21:36.677 | Paris Saint-Germai | Paris Saint-Germai | 130 | Ball Receipt*   |   -   | [62.2, 34.4]    |  |
| -1585.96 | -1585.96 | 00:21:36.677 | Paris Saint-Germai | Paris Saint-Germai | 130 | Carry           |   -   | [62.2, 34.4]    |  |
| -1583.87 | -1583.87 | 00:21:38.766 | Paris Saint-Germai | Paris Saint-Germai | 130 | Pass            |   -   | [64.7, 34.4]    | -> Lionel Andrés  |
| -1582.90 | -1582.90 | 00:21:39.736 | Paris Saint-Germai | Paris Saint-Germai | 130 | Ball Receipt*   |   -   | [79.7, 38.3]    |  |
| -1582.90 | -1582.90 | 00:21:39.736 | Paris Saint-Germai | Paris Saint-Germai | 130 | Carry           |   -   | [79.7, 38.3]    |  |
| -1582.07 | -1582.07 | 00:21:40.570 | Paris Saint-Germai | Paris Saint-Germai | 130 | Pass            |   -   | [79.7, 38.3]    | -> Ángel Fabián D |
| -1581.03 | -1581.03 | 00:21:41.612 | Paris Saint-Germai | Paris Saint-Germai | 130 | Ball Receipt*   |   -   | [85.6, 48.9]    |  |
| -1581.03 | -1581.03 | 00:21:41.612 | Paris Saint-Germai | Paris Saint-Germai | 130 | Carry           |   -   | [85.6, 48.9]    |  |
| -1579.85 | -1579.85 | 00:21:42.789 | Paris Saint-Germai | Paris Saint-Germai | 130 | Pass            |   -   | [85.6, 51.4]    | Incomplete (Pass Offside) |
| -1578.59 | -1578.59 | 00:21:44.045 | Paris Saint-Germai | Paris Saint-Germai | 130 | Ball Receipt*   |   -   | [109.8, 53.9]   | Incomplete |
| -1545.77 | -1545.77 | 00:22:16.870 | Saint-Étienne      | Saint-Étienne      | 131 | Pass            |   -   | [12.0, 27.0]    | Incomplete (Incomplete) |
| -1542.27 | -1542.27 | 00:22:20.370 | Saint-Étienne      | Saint-Étienne      | 131 | Ball Receipt*   |   -   | [80.1, 9.3]     | Incomplete |
| -1542.27 | -1542.27 | 00:22:20.370 | Saint-Étienne      | Saint-Étienne      | 131 | Duel            |   -   | [80.1, 8.7]     | Aerial Lost |
| -1542.27 | -1542.27 | 00:22:20.370 | Paris Saint-Germai | Saint-Étienne      | 131 | Clearance       |   -   | [40.0, 71.4]    |  |
| -1540.63 | -1540.63 | 00:22:22.004 | Paris Saint-Germai | Saint-Étienne      | 131 | Clearance       |   -   | [39.2, 61.3]    |  |
| -1538.46 | -1538.46 | 00:22:24.179 | Saint-Étienne      | Saint-Étienne      | 131 | Ball Recovery   |   -   | [61.2, 13.2]    |  |
| -1538.46 | -1538.46 | 00:22:24.179 | Saint-Étienne      | Saint-Étienne      | 131 | Carry           |   -   | [61.2, 13.2]    |  |
| -1537.43 | -1537.43 | 00:22:25.204 | Saint-Étienne      | Saint-Étienne      | 131 | Pass            |   -   | [57.9, 13.7]    | Incomplete (Incomplete) |
| -1535.58 | -1535.58 | 00:22:27.057 | Saint-Étienne      | Saint-Étienne      | 131 | Ball Receipt*   |   -   | [63.3, 53.5]    | Incomplete |
| -1535.58 | -1535.58 | 00:22:27.057 | Paris Saint-Germai | Paris Saint-Germai | 132 | Pass            |  Yes  | [57.0, 29.4]    | -> Idrissa Gana G |
| -1533.83 | -1533.83 | 00:22:28.807 | Paris Saint-Germai | Paris Saint-Germai | 132 | Ball Receipt*   |   -   | [56.2, 40.3]    |  |
| -1533.83 | -1533.83 | 00:22:28.807 | Paris Saint-Germai | Paris Saint-Germai | 132 | Carry           |   -   | [56.2, 40.3]    |  |
| -1532.31 | -1532.31 | 00:22:30.331 | Saint-Étienne      | Paris Saint-Germai | 132 | Pressure        |  Yes  | [54.0, 40.6]    |  |
| -1531.95 | -1531.95 | 00:22:30.691 | Paris Saint-Germai | Paris Saint-Germai | 132 | Pass            |   -   | [65.4, 37.5]    | -> Lionel Andrés  |
| -1531.62 | -1531.62 | 00:22:31.020 | Saint-Étienne      | Paris Saint-Germai | 132 | Pressure        |  Yes  | [40.4, 40.6]    |  |
| -1531.30 | -1531.30 | 00:22:31.340 | Paris Saint-Germai | Paris Saint-Germai | 132 | Ball Receipt*   |   -   | [77.8, 39.1]    |  |
| -1531.30 | -1531.30 | 00:22:31.340 | Paris Saint-Germai | Paris Saint-Germai | 132 | Carry           |   -   | [77.8, 39.1]    |  |
| -1531.07 | -1531.07 | 00:22:31.570 | Paris Saint-Germai | Paris Saint-Germai | 132 | Dispossessed    |   -   | [79.0, 34.2]    |  |
| -1531.07 | -1531.07 | 00:22:31.570 | Saint-Étienne      | Saint-Étienne      | 133 | Duel            |  Yes  | [41.1, 45.9]    | Tackle, Success In Play |
| -1529.53 | -1529.53 | 00:22:33.105 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Recovery   |   -   | [33.6, 51.5]    |  |
| -1529.53 | -1529.53 | 00:22:33.105 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [33.6, 51.5]    |  |
| -1528.80 | -1528.80 | 00:22:33.842 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [32.5, 56.3]    | -> Ryad Boudebouz |
| -1527.78 | -1527.78 | 00:22:34.857 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [36.9, 61.5]    |  |
| -1527.78 | -1527.78 | 00:22:34.857 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [36.9, 61.5]    |  |
| -1527.36 | -1527.36 | 00:22:35.283 | Paris Saint-Germai | Saint-Étienne      | 133 | Pressure        |  Yes  | [78.1, 20.6]    |  |
| -1524.23 | -1524.23 | 00:22:38.410 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [48.6, 60.9]    | -> Mahdi Camara |
| -1522.87 | -1522.87 | 00:22:39.766 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [56.7, 43.5]    |  |
| -1522.87 | -1522.87 | 00:22:39.766 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [56.7, 43.5]    |  |
| -1522.49 | -1522.49 | 00:22:40.145 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [56.7, 42.6]    | -> Denis Bouanga |
| -1519.62 | -1519.62 | 00:22:43.022 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [71.5, 8.1]     |  |
| -1519.62 | -1519.62 | 00:22:43.022 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [71.5, 8.1]     |  |
| -1515.61 | -1515.61 | 00:22:47.033 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [83.9, 7.3]     | -> Miguel Ángel T |
| -1514.04 | -1514.04 | 00:22:48.599 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [71.9, 8.5]     |  |
| -1514.04 | -1514.04 | 00:22:48.599 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [71.9, 8.5]     |  |
| -1513.80 | -1513.80 | 00:22:48.840 | Paris Saint-Germai | Saint-Étienne      | 133 | Pressure        |   -   | [45.3, 69.1]    |  |
| -1513.15 | -1513.15 | 00:22:49.487 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [72.2, 9.0]     | -> Denis Bouanga |
| -1511.13 | -1511.13 | 00:22:51.510 | Paris Saint-Germai | Saint-Étienne      | 133 | Pressure        |   -   | [17.6, 70.2]    |  |
| -1510.84 | -1510.84 | 00:22:51.796 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [104.4, 9.1]    |  |
| -1510.84 | -1510.84 | 00:22:51.796 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [104.4, 9.1]    |  |
| -1510.35 | -1510.35 | 00:22:52.289 | Paris Saint-Germai | Saint-Étienne      | 133 | Dribbled Past   |   -   | [14.5, 70.3]    |  |
| -1510.35 | -1510.35 | 00:22:52.289 | Saint-Étienne      | Saint-Étienne      | 133 | Dribble         |   -   | [105.6, 9.8]    |  |
| -1508.07 | -1508.07 | 00:22:54.568 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [92.3, 10.4]    | Incomplete (Incomplete) |
| -1506.66 | -1506.66 | 00:22:55.982 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [83.4, 12.0]    | Incomplete |
| -1506.66 | -1506.66 | 00:22:55.982 | Paris Saint-Germai | Saint-Étienne      | 133 | Ball Recovery   |   -   | [42.8, 71.4]    |  |
| -1506.66 | -1506.66 | 00:22:55.982 | Paris Saint-Germai | Saint-Étienne      | 133 | Carry           |   -   | [42.8, 71.4]    |  |
| -1504.64 | -1504.64 | 00:22:58.001 | Paris Saint-Germai | Saint-Étienne      | 133 | Pass            |   -   | [43.1, 55.8]    | -> Kylian Mbappé  |
| -1503.79 | -1503.79 | 00:22:58.851 | Saint-Étienne      | Saint-Étienne      | 133 | Pressure        |  Yes  | [54.7, 24.3]    |  |
| -1503.42 | -1503.42 | 00:22:59.213 | Paris Saint-Germai | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [62.8, 55.8]    |  |
| -1503.42 | -1503.42 | 00:22:59.213 | Paris Saint-Germai | Saint-Étienne      | 133 | Pass            |   -   | [64.0, 55.8]    | Incomplete (Incomplete) |
| -1502.59 | -1502.59 | 00:23:00.049 | Paris Saint-Germai | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [62.3, 43.1]    | Incomplete |
| -1502.59 | -1502.59 | 00:23:00.049 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |  Yes  | [56.4, 37.1]    | -> Ryad Boudebouz |
| -1501.12 | -1501.12 | 00:23:01.519 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [65.3, 26.8]    |  |
| -1501.12 | -1501.12 | 00:23:01.519 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [65.3, 26.8]    |  |
| -1501.10 | -1501.10 | 00:23:01.536 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [65.1, 26.6]    | -> Miguel Ángel T |
| -1499.38 | -1499.38 | 00:23:03.262 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [62.3, 9.6]     |  |
| -1499.38 | -1499.38 | 00:23:03.262 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [62.3, 9.6]     |  |
| -1498.57 | -1498.57 | 00:23:04.067 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [63.1, 9.0]     | -> Ryad Boudebouz |
| -1497.75 | -1497.75 | 00:23:04.889 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [64.4, 20.7]    |  |
| -1497.75 | -1497.75 | 00:23:04.889 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [64.4, 20.7]    |  |
| -1497.50 | -1497.50 | 00:23:05.138 | Saint-Étienne      | Saint-Étienne      | 133 | Pass            |   -   | [64.4, 20.7]    | -> Miguel Ángel T |
| -1496.51 | -1496.51 | 00:23:06.123 | Saint-Étienne      | Saint-Étienne      | 133 | Ball Receipt*   |   -   | [67.0, 7.0]     |  |
| -1496.51 | -1496.51 | 00:23:06.123 | Saint-Étienne      | Saint-Étienne      | 133 | Carry           |   -   | [67.0, 7.0]     |  |
| -1496.41 | -1496.41 | 00:23:06.231 | Saint-Étienne      | Saint-Étienne      | 133 | Dispossessed    |   -   | [67.6, 7.0]     |  |
| -1496.41 | -1496.41 | 00:23:06.231 | Paris Saint-Germai | Paris Saint-Germai | 134 | Duel            |  Yes  | [52.5, 73.1]    | Tackle, Success In Play |
| -1494.51 | -1494.51 | 00:23:08.125 | Saint-Étienne      | Paris Saint-Germai | 134 | 50/50           |  Yes  | [53.1, 11.5]    |  |
| -1494.51 | -1494.51 | 00:23:08.125 | Paris Saint-Germai | Paris Saint-Germai | 134 | 50/50           |  Yes  | [67.0, 68.6]    |  |
| -1492.83 | -1492.83 | 00:23:09.810 | Paris Saint-Germai | Paris Saint-Germai | 134 | Pass            |   -   | [67.9, 64.2]    | -> Neymar da Silv |
| -1489.18 | -1489.18 | 00:23:13.459 | Paris Saint-Germai | Paris Saint-Germai | 134 | Ball Receipt*   |   -   | [106.1, 27.8]   |  |
| -1489.18 | -1489.18 | 00:23:13.459 | Paris Saint-Germai | Paris Saint-Germai | 134 | Carry           |   -   | [106.1, 27.8]   |  |
| -1488.67 | -1488.67 | 00:23:13.969 | Saint-Étienne      | Paris Saint-Germai | 134 | Pressure        |   -   | [14.8, 48.2]    |  |
| -1488.22 | -1488.22 | 00:23:14.413 | Paris Saint-Germai | Paris Saint-Germai | 134 | Shot            |   -   | [110.8, 29.8]   | Saved |
| -1488.02 | -1488.02 | 00:23:14.618 | Saint-Étienne      | Paris Saint-Germai | 134 | Goal Keeper     |   -   | [5.9, 45.8]     |  |
| -1486.67 | -1486.67 | 00:23:15.963 | Paris Saint-Germai | Paris Saint-Germai | 134 | Ball Recovery   |   -   | [105.1, 38.9]   |  |
| -1486.62 | -1486.62 | 00:23:16.022 | Paris Saint-Germai | Paris Saint-Germai | 134 | Shot            |   -   | [105.4, 36.3]   | Off T |
| -1485.75 | -1485.75 | 00:23:16.886 | Saint-Étienne      | Paris Saint-Germai | 134 | Goal Keeper     |   -   | [8.5, 44.2]     |  |
| -1453.62 | -1453.62 | 00:23:49.019 | Saint-Étienne      | Saint-Étienne      | 135 | Pass            |   -   | [7.0, 36.1]     | -> Denis Bouanga |
| -1447.81 | -1447.81 | 00:23:54.829 | Saint-Étienne      | Saint-Étienne      | 135 | Ball Receipt*   |   -   | [72.2, 15.6]    |  |
| -1447.81 | -1447.81 | 00:23:54.829 | Saint-Étienne      | Saint-Étienne      | 135 | Pass            |   -   | [72.5, 15.6]    | Incomplete (Incomplete) |
| -1447.81 | -1447.81 | 00:23:54.829 | Paris Saint-Germai | Saint-Étienne      | 135 | Duel            |   -   | [47.6, 64.5]    | Aerial Lost |
| -1444.95 | -1444.95 | 00:23:57.688 | Paris Saint-Germai | Saint-Étienne      | 135 | Goal Keeper     |   -   | [20.4, 58.1]    |  |
| -1435.14 | -1435.14 | 00:24:07.496 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [91.1, 0.1]     | -> Mahdi Camara |
| -1434.26 | -1434.26 | 00:24:08.373 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [91.2, 9.8]     |  |
| -1434.26 | -1434.26 | 00:24:08.373 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [91.2, 9.8]     |  |
| -1433.91 | -1433.91 | 00:24:08.729 | Paris Saint-Germai | Saint-Étienne      | 136 | Pressure        |   -   | [30.1, 71.7]    |  |
| -1433.30 | -1433.30 | 00:24:09.338 | Paris Saint-Germai | Saint-Étienne      | 136 | Dribbled Past   |   -   | [34.8, 72.8]    |  |
| -1433.30 | -1433.30 | 00:24:09.338 | Saint-Étienne      | Saint-Étienne      | 136 | Dribble         |   -   | [85.3, 7.3]     |  |
| -1433.30 | -1433.30 | 00:24:09.338 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [85.3, 7.3]     |  |
| -1432.75 | -1432.75 | 00:24:09.883 | Paris Saint-Germai | Saint-Étienne      | 136 | Pressure        |   -   | [26.5, 70.8]    |  |
| -1432.52 | -1432.52 | 00:24:10.115 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [93.3, 5.2]     | -> Denis Bouanga |
| -1431.96 | -1431.96 | 00:24:10.676 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [97.8, 5.2]     |  |
| -1431.96 | -1431.96 | 00:24:10.676 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [97.8, 5.2]     |  |
| -1431.93 | -1431.93 | 00:24:10.712 | Paris Saint-Germai | Saint-Étienne      | 136 | Pressure        |   -   | [21.1, 72.8]    |  |
| -1429.61 | -1429.61 | 00:24:13.026 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [92.6, 12.9]    | -> Ryad Boudebouz |
| -1428.48 | -1428.48 | 00:24:14.158 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [79.4, 18.7]    |  |
| -1428.48 | -1428.48 | 00:24:14.158 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [79.4, 18.7]    |  |
| -1426.96 | -1426.96 | 00:24:15.677 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [82.6, 13.1]    | -> Mahdi Camara |
| -1425.96 | -1425.96 | 00:24:16.677 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [92.3, 4.6]     |  |
| -1425.96 | -1425.96 | 00:24:16.677 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [92.3, 4.6]     |  |
| -1423.00 | -1423.00 | 00:24:19.639 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [98.6, 12.4]    | Incomplete (Incomplete) |
| -1422.68 | -1422.68 | 00:24:19.960 | Paris Saint-Germai | Saint-Étienne      | 136 | Interception    |   -   | [21.5, 61.3]    | Lost In Play |
| -1420.85 | -1420.85 | 00:24:21.792 | Paris Saint-Germai | Saint-Étienne      | 136 | Pressure        |   -   | [26.5, 56.1]    |  |
| -1420.40 | -1420.40 | 00:24:22.236 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [93.6, 22.6]    | -> Ryad Boudebouz |
| -1419.37 | -1419.37 | 00:24:23.273 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [80.8, 19.5]    |  |
| -1419.37 | -1419.37 | 00:24:23.273 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [80.8, 19.5]    |  |
| -1417.68 | -1417.68 | 00:24:24.959 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [82.8, 19.8]    | -> Yvann Macon |
| -1415.97 | -1415.97 | 00:24:26.671 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [79.7, 75.2]    |  |
| -1415.97 | -1415.97 | 00:24:26.671 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [79.7, 75.2]    |  |
| -1412.39 | -1412.39 | 00:24:30.247 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [90.4, 61.5]    | -> Miguel Ángel T |
| -1409.35 | -1409.35 | 00:24:33.290 | Saint-Étienne      | Saint-Étienne      | 136 | Ball Receipt*   |   -   | [99.0, 11.5]    |  |
| -1409.35 | -1409.35 | 00:24:33.290 | Saint-Étienne      | Saint-Étienne      | 136 | Carry           |   -   | [99.0, 11.5]    |  |
| -1408.07 | -1408.07 | 00:24:34.570 | Saint-Étienne      | Saint-Étienne      | 136 | Pass            |   -   | [105.1, 10.4]   | Incomplete (Incomplete) |
| -1407.88 | -1407.88 | 00:24:34.757 | Paris Saint-Germai | Saint-Étienne      | 136 | Block           |   -   | [14.0, 66.0]    |  |
| -1405.62 | -1405.62 | 00:24:37.020 | Saint-Étienne      | Saint-Étienne      | 136 | Pressure        |   -   | [90.4, 25.6]    |  |
| -1405.04 | -1405.04 | 00:24:37.596 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Recovery   |   -   | [31.7, 51.6]    |  |
| -1405.04 | -1405.04 | 00:24:37.596 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [31.7, 51.6]    |  |
| -1403.78 | -1403.78 | 00:24:38.862 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [31.5, 49.9]    | -> Ángel Fabián D |
| -1402.85 | -1402.85 | 00:24:39.785 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [34.2, 57.8]    |  |
| -1402.85 | -1402.85 | 00:24:39.785 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [34.2, 57.8]    |  |
| -1399.25 | -1399.25 | 00:24:43.392 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [56.5, 43.8]    | -> Neymar da Silv |
| -1398.26 | -1398.26 | 00:24:44.377 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [64.0, 33.9]    |  |
| -1398.26 | -1398.26 | 00:24:44.377 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [64.0, 33.9]    |  |
| -1393.38 | -1393.38 | 00:24:49.258 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [85.1, 40.5]    | -> Lionel Andrés  |
| -1391.77 | -1391.77 | 00:24:50.867 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [97.5, 57.4]    |  |
| -1391.77 | -1391.77 | 00:24:50.867 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [97.5, 57.4]    |  |
| -1390.08 | -1390.08 | 00:24:52.558 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [102.2, 55.2]   | Incomplete (Incomplete) |
| -1389.77 | -1389.77 | 00:24:52.869 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [102.2, 41.4]   | Incomplete |
| -1389.77 | -1389.77 | 00:24:52.869 | Saint-Étienne      | Paris Saint-Germai | 137 | Block           |   -   | [17.3, 27.4]    |  |
| -1389.20 | -1389.20 | 00:24:53.434 | Saint-Étienne      | Paris Saint-Germai | 137 | Ball Recovery   |   -   | [14.2, 27.4]    |  |
| -1389.20 | -1389.20 | 00:24:53.434 | Saint-Étienne      | Paris Saint-Germai | 137 | Carry           |   -   | [14.2, 27.4]    |  |
| -1388.50 | -1388.50 | 00:24:54.139 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pressure        |  Yes  | [101.4, 53.8]   |  |
| -1387.74 | -1387.74 | 00:24:54.893 | Saint-Étienne      | Paris Saint-Germai | 137 | Pass            |   -   | [12.0, 25.6]    | Incomplete (Incomplete) |
| -1382.82 | -1382.82 | 00:24:59.819 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Recovery   |   -   | [50.6, 70.8]    |  |
| -1382.82 | -1382.82 | 00:24:59.819 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [50.6, 70.8]    |  |
| -1381.63 | -1381.63 | 00:25:01.012 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [51.5, 67.2]    | -> Sergio Ramos G |
| -1379.38 | -1379.38 | 00:25:03.253 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [56.8, 41.4]    |  |
| -1379.38 | -1379.38 | 00:25:03.253 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [56.8, 41.4]    |  |
| -1378.32 | -1378.32 | 00:25:04.315 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [64.3, 39.2]    | -> Idrissa Gana G |
| -1376.94 | -1376.94 | 00:25:05.698 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [76.5, 29.1]    |  |
| -1376.94 | -1376.94 | 00:25:05.698 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [76.5, 29.1]    |  |
| -1376.09 | -1376.09 | 00:25:06.551 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [78.1, 29.1]    | -> Kylian Mbappé  |
| -1375.25 | -1375.25 | 00:25:07.385 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [94.8, 24.4]    |  |
| -1375.25 | -1375.25 | 00:25:07.385 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [94.8, 24.4]    |  |
| -1372.45 | -1372.45 | 00:25:10.187 | Paris Saint-Germai | Paris Saint-Germai | 137 | Miscontrol      |   -   | [102.9, 26.6]   |  |
| -1371.92 | -1371.92 | 00:25:10.722 | Saint-Étienne      | Paris Saint-Germai | 137 | Clearance       |   -   | [16.1, 43.2]    |  |
| -1367.18 | -1367.18 | 00:25:15.457 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Recovery   |   -   | [69.2, 4.9]     |  |
| -1367.18 | -1367.18 | 00:25:15.457 | Paris Saint-Germai | Paris Saint-Germai | 137 | Carry           |   -   | [69.2, 4.9]     |  |
| -1365.96 | -1365.96 | 00:25:16.673 | Paris Saint-Germai | Paris Saint-Germai | 137 | Pass            |   -   | [68.9, 5.2]     | -> Idrissa Gana G |
| -1364.70 | -1364.70 | 00:25:17.942 | Paris Saint-Germai | Paris Saint-Germai | 137 | Ball Receipt*   |   -   | [82.9, 18.9]    |  |
| -1362.92 | -1362.92 | 00:25:19.721 | Paris Saint-Germai | Paris Saint-Germai | 137 | Injury Stoppage |   -   | -               |  |
| -1360.44 | -1360.44 | 00:25:22.194 | Saint-Étienne      | Paris Saint-Germai | 137 | Injury Stoppage |   -   | -               |  |
| -1282.04 | -1282.04 | 00:26:40.594 | Saint-Étienne      | Paris Saint-Germai | 137 | Substitution    |   -   | -               |  |
| -1246.41 | -1246.41 | 00:27:16.229 | Paris Saint-Germai | Paris Saint-Germai | 138 | Referee Ball-Drop |   -   | [72.8, 16.7]    |  |
| -1246.28 | -1246.28 | 00:27:16.353 | Saint-Étienne      | Saint-Étienne      | 139 | Referee Ball-Drop |   -   | [46.9, 63.2]    |  |
| -1245.16 | -1245.16 | 00:27:17.475 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [73.2, 16.9]    |  |
| -1245.16 | -1245.16 | 00:27:17.475 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [73.2, 16.9]    |  |
| -1245.04 | -1245.04 | 00:27:17.595 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [71.8, 17.7]    | -> Ángel Fabián D |
| -1243.40 | -1243.40 | 00:27:19.236 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [77.2, 39.5]    |  |
| -1243.40 | -1243.40 | 00:27:19.236 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [77.2, 39.5]    |  |
| -1242.29 | -1242.29 | 00:27:20.345 | Saint-Étienne      | Paris Saint-Germai | 140 | Pressure        |  Yes  | [39.2, 42.3]    |  |
| -1241.63 | -1241.63 | 00:27:21.010 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [77.9, 39.5]    | -> Marcos Aoás Co |
| -1240.37 | -1240.37 | 00:27:22.267 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [69.8, 55.5]    |  |
| -1240.37 | -1240.37 | 00:27:22.267 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [69.8, 55.5]    |  |
| -1237.86 | -1237.86 | 00:27:24.775 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [74.8, 52.0]    | -> Sergio Ramos G |
| -1235.45 | -1235.45 | 00:27:27.187 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [72.0, 11.4]    |  |
| -1235.45 | -1235.45 | 00:27:27.187 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [72.0, 11.4]    |  |
| -1235.41 | -1235.41 | 00:27:27.227 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [72.0, 11.4]    | -> Juan Bernat Ve |
| -1233.87 | -1233.87 | 00:27:28.767 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [92.5, 3.1]     |  |
| -1233.87 | -1233.87 | 00:27:28.767 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [92.5, 3.1]     |  |
| -1233.45 | -1233.45 | 00:27:29.186 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [94.7, 5.2]     | -> Idrissa Gana G |
| -1230.87 | -1230.87 | 00:27:31.765 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [81.1, 24.5]    |  |
| -1230.87 | -1230.87 | 00:27:31.765 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [81.1, 24.4]    | -> Lionel Andrés  |
| -1229.38 | -1229.38 | 00:27:33.259 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [80.6, 43.0]    |  |
| -1229.38 | -1229.38 | 00:27:33.259 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [80.6, 43.0]    |  |
| -1228.31 | -1228.31 | 00:27:34.324 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [80.6, 43.0]    | -> Ángel Fabián D |
| -1227.17 | -1227.17 | 00:27:35.464 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [84.7, 61.1]    |  |
| -1227.17 | -1227.17 | 00:27:35.464 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [84.7, 61.1]    |  |
| -1223.62 | -1223.62 | 00:27:39.016 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [84.3, 56.1]    | Incomplete (Incomplete) |
| -1222.00 | -1222.00 | 00:27:40.635 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [111.8, 24.5]   | Incomplete |
| -1222.00 | -1222.00 | 00:27:40.635 | Saint-Étienne      | Paris Saint-Germai | 140 | Interception    |   -   | [11.4, 46.5]    | Lost In Play |
| -1221.17 | -1221.17 | 00:27:41.464 | Saint-Étienne      | Paris Saint-Germai | 140 | Pressure        |   -   | [19.4, 52.1]    |  |
| -1221.04 | -1221.04 | 00:27:41.598 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [102.5, 27.4]   |  |
| -1221.04 | -1221.04 | 00:27:41.598 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [102.5, 27.4]   |  |
| -1218.76 | -1218.76 | 00:27:43.881 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [110.0, 27.8]   | Incomplete (Incomplete) |
| -1218.27 | -1218.27 | 00:27:44.364 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [112.5, 37.7]   | Incomplete |
| -1218.27 | -1218.27 | 00:27:44.364 | Saint-Étienne      | Paris Saint-Germai | 140 | Clearance       |   -   | [8.1, 43.7]     |  |
| -1217.65 | -1217.65 | 00:27:44.984 | Saint-Étienne      | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [12.0, 55.6]    |  |
| -1217.18 | -1217.18 | 00:27:45.454 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pressure        |   -   | [109.3, 26.7]   |  |
| -1216.68 | -1216.68 | 00:27:45.958 | Saint-Étienne      | Paris Saint-Germai | 140 | Clearance       |   -   | [10.3, 51.6]    |  |
| -1214.27 | -1214.27 | 00:27:48.364 | Saint-Étienne      | Paris Saint-Germai | 140 | Pressure        |   -   | [36.5, 58.1]    |  |
| -1213.83 | -1213.83 | 00:27:48.808 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [81.4, 22.5]    | -> Marcos Aoás Co |
| -1212.01 | -1212.01 | 00:27:50.631 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [66.7, 38.3]    |  |
| -1212.01 | -1212.01 | 00:27:50.631 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [66.7, 38.3]    |  |
| -1208.29 | -1208.29 | 00:27:54.350 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [79.7, 37.5]    | -> Ángel Fabián D |
| -1206.97 | -1206.97 | 00:27:55.666 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [81.1, 53.9]    |  |
| -1206.97 | -1206.97 | 00:27:55.666 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [81.1, 53.9]    |  |
| -1202.69 | -1202.69 | 00:27:59.943 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [93.6, 56.1]    | -> Achraf Hakimi  |
| -1201.46 | -1201.46 | 00:28:01.175 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [93.6, 76.1]    |  |
| -1201.46 | -1201.46 | 00:28:01.175 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [93.6, 76.1]    |  |
| -1200.56 | -1200.56 | 00:28:02.080 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [93.6, 76.1]    | -> Kylian Mbappé  |
| -1199.35 | -1199.35 | 00:28:03.288 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [91.8, 55.5]    |  |
| -1199.35 | -1199.35 | 00:28:03.288 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [91.8, 55.5]    | -> Marcos Aoás Co |
| -1197.71 | -1197.71 | 00:28:04.930 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [72.0, 63.6]    |  |
| -1197.71 | -1197.71 | 00:28:04.930 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [72.0, 63.6]    |  |
| -1196.63 | -1196.63 | 00:28:06.009 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [74.8, 60.3]    | -> Lionel Andrés  |
| -1195.02 | -1195.02 | 00:28:07.619 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [79.2, 29.9]    |  |
| -1195.02 | -1195.02 | 00:28:07.619 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [79.2, 29.9]    |  |
| -1193.98 | -1193.98 | 00:28:08.657 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [82.5, 30.0]    | -> Neymar da Silv |
| -1193.12 | -1193.12 | 00:28:09.520 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [93.1, 28.5]    |  |
| -1193.12 | -1193.12 | 00:28:09.520 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [93.1, 28.5]    |  |
| -1191.75 | -1191.75 | 00:28:10.883 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [96.8, 27.4]    | -> Lionel Andrés  |
| -1190.99 | -1190.99 | 00:28:11.646 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [95.3, 33.0]    |  |
| -1190.99 | -1190.99 | 00:28:11.646 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [95.3, 32.5]    | Incomplete (Incomplete) |
| -1190.63 | -1190.63 | 00:28:12.005 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [104.8, 29.1]   | Incomplete |
| -1190.63 | -1190.63 | 00:28:12.005 | Saint-Étienne      | Paris Saint-Germai | 140 | Clearance       |   -   | [17.6, 49.0]    |  |
| -1188.51 | -1188.51 | 00:28:14.129 | Saint-Étienne      | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [32.6, 54.0]    |  |
| -1188.51 | -1188.51 | 00:28:14.129 | Saint-Étienne      | Paris Saint-Germai | 140 | Carry           |   -   | [32.6, 54.0]    |  |
| -1187.47 | -1187.47 | 00:28:15.164 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pressure        |  Yes  | [84.2, 23.9]    |  |
| -1186.68 | -1186.68 | 00:28:15.957 | Saint-Étienne      | Paris Saint-Germai | 140 | Dispossessed    |   -   | [36.2, 58.1]    |  |
| -1186.68 | -1186.68 | 00:28:15.957 | Paris Saint-Germai | Paris Saint-Germai | 140 | Duel            |  Yes  | [83.9, 22.0]    | Tackle, Success In Play |
| -1186.05 | -1186.05 | 00:28:16.590 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [84.3, 12.7]    |  |
| -1186.05 | -1186.05 | 00:28:16.590 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [84.3, 12.7]    |  |
| -1183.61 | -1183.61 | 00:28:19.033 | Saint-Étienne      | Paris Saint-Germai | 140 | Dribbled Past   |   -   | [34.8, 64.8]    |  |
| -1183.61 | -1183.61 | 00:28:19.033 | Paris Saint-Germai | Paris Saint-Germai | 140 | Dribble         |   -   | [85.3, 15.3]    |  |
| -1183.61 | -1183.61 | 00:28:19.033 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [85.3, 15.3]    |  |
| -1182.44 | -1182.44 | 00:28:20.197 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [86.2, 18.9]    | -> Ángel Fabián D |
| -1179.85 | -1179.85 | 00:28:22.792 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [99.5, 63.9]    |  |
| -1179.85 | -1179.85 | 00:28:22.792 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [99.5, 63.9]    |  |
| -1178.68 | -1178.68 | 00:28:23.961 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [98.2, 65.2]    | Incomplete (Unknown) |
| -1177.11 | -1177.11 | 00:28:25.531 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [111.4, 38.3]   | Incomplete |
| -1177.09 | -1177.09 | 00:28:25.548 | Paris Saint-Germai | Paris Saint-Germai | 140 | Foul Committed  |   -   | [110.7, 40.2]   |  |
| -1177.09 | -1177.09 | 00:28:25.548 | Saint-Étienne      | Paris Saint-Germai | 140 | Foul Won        |   -   | [9.4, 39.9]     |  |
| -1130.05 | -1130.05 | 00:29:12.586 | Paris Saint-Germai | Paris Saint-Germai | 140 | Substitution    |   -   | -               |  |
| -1116.48 | -1116.48 | 00:29:26.154 | Saint-Étienne      | Saint-Étienne      | 141 | Pass            |   -   | [13.6, 36.6]    | Incomplete (Incomplete) |
| -1113.55 | -1113.55 | 00:29:29.088 | Saint-Étienne      | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [60.6, 9.9]     | Incomplete |
| -1113.55 | -1113.55 | 00:29:29.088 | Paris Saint-Germai | Saint-Étienne      | 141 | Pass            |   -   | [63.1, 67.2]    | -> Lionel Andrés  |
| -1112.23 | -1112.23 | 00:29:30.410 | Paris Saint-Germai | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [70.7, 54.5]    |  |
| -1112.23 | -1112.23 | 00:29:30.410 | Paris Saint-Germai | Saint-Étienne      | 141 | Carry           |   -   | [70.7, 54.5]    |  |
| -1112.05 | -1112.05 | 00:29:30.587 | Saint-Étienne      | Saint-Étienne      | 141 | Pressure        |  Yes  | [47.6, 26.3]    |  |
| -1111.37 | -1111.37 | 00:29:31.271 | Paris Saint-Germai | Saint-Étienne      | 141 | Pass            |   -   | [70.3, 56.1]    | Incomplete (Incomplete) |
| -1110.37 | -1110.37 | 00:29:32.270 | Paris Saint-Germai | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [55.7, 55.2]    | Incomplete |
| -1110.37 | -1110.37 | 00:29:32.270 | Saint-Étienne      | Saint-Étienne      | 141 | Interception    |  Yes  | [61.7, 26.6]    | Success In Play |
| -1108.97 | -1108.97 | 00:29:33.666 | Saint-Étienne      | Saint-Étienne      | 141 | Ball Recovery   |   -   | [54.0, 41.3]    |  |
| -1108.97 | -1108.97 | 00:29:33.666 | Saint-Étienne      | Saint-Étienne      | 141 | Carry           |   -   | [54.0, 41.3]    |  |
| -1107.56 | -1107.56 | 00:29:35.073 | Paris Saint-Germai | Saint-Étienne      | 141 | Pressure        |   -   | [64.8, 36.0]    |  |
| -1107.35 | -1107.35 | 00:29:35.293 | Saint-Étienne      | Saint-Étienne      | 141 | Pass            |   -   | [56.5, 42.9]    | -> Mahdi Camara |
| -1106.16 | -1106.16 | 00:29:36.477 | Saint-Étienne      | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [66.2, 32.0]    |  |
| -1106.16 | -1106.16 | 00:29:36.477 | Saint-Étienne      | Saint-Étienne      | 141 | Carry           |   -   | [66.2, 32.0]    |  |
| -1106.14 | -1106.14 | 00:29:36.499 | Paris Saint-Germai | Saint-Étienne      | 141 | Pressure        |   -   | [52.3, 50.6]    |  |
| -1104.99 | -1104.99 | 00:29:37.652 | Saint-Étienne      | Saint-Étienne      | 141 | Pass            |   -   | [69.5, 31.3]    | -> Lucas Gourna-D |
| -1104.17 | -1104.17 | 00:29:38.471 | Saint-Étienne      | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [63.9, 27.9]    |  |
| -1104.17 | -1104.17 | 00:29:38.471 | Saint-Étienne      | Saint-Étienne      | 141 | Carry           |   -   | [63.9, 27.9]    |  |
| -1101.98 | -1101.98 | 00:29:40.659 | Saint-Étienne      | Saint-Étienne      | 141 | Pass            |   -   | [80.1, 19.1]    | -> Miguel Ángel T |
| -1100.77 | -1100.77 | 00:29:41.872 | Paris Saint-Germai | Saint-Étienne      | 141 | Pressure        |   -   | [28.2, 71.1]    |  |
| -1100.31 | -1100.31 | 00:29:42.324 | Saint-Étienne      | Saint-Étienne      | 141 | Ball Receipt*   |   -   | [87.9, 4.5]     |  |
| -1100.31 | -1100.31 | 00:29:42.324 | Saint-Étienne      | Saint-Étienne      | 141 | Carry           |   -   | [87.9, 4.5]     |  |
| -1099.50 | -1099.50 | 00:29:43.137 | Saint-Étienne      | Saint-Étienne      | 141 | Dispossessed    |   -   | [89.4, 5.9]     |  |
| -1099.50 | -1099.50 | 00:29:43.137 | Paris Saint-Germai | Paris Saint-Germai | 142 | Duel            |  Yes  | [30.7, 74.2]    | Tackle, Won |
| -1099.50 | -1099.50 | 00:29:43.137 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [30.7, 74.2]    |  |
| -1099.27 | -1099.27 | 00:29:43.363 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [30.4, 74.2]    | -> Ángel Fabián D |
| -1098.57 | -1098.57 | 00:29:44.071 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [33.4, 74.2]    |  |
| -1098.57 | -1098.57 | 00:29:44.071 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [33.4, 74.2]    |  |
| -1096.99 | -1096.99 | 00:29:45.651 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [26.2, 73.8]    | -> Marcos Aoás Co |
| -1095.72 | -1095.72 | 00:29:46.918 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [21.8, 57.2]    |  |
| -1095.72 | -1095.72 | 00:29:46.918 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [21.8, 57.2]    |  |
| -1094.66 | -1094.66 | 00:29:47.975 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [22.6, 54.9]    | -> Leandro Daniel |
| -1092.85 | -1092.85 | 00:29:49.789 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [32.3, 49.4]    |  |
| -1092.85 | -1092.85 | 00:29:49.789 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [32.3, 49.4]    |  |
| -1091.94 | -1091.94 | 00:29:50.701 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [35.9, 48.3]    | -> Sergio Ramos G |
| -1090.52 | -1090.52 | 00:29:52.122 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [38.1, 26.1]    |  |
| -1090.52 | -1090.52 | 00:29:52.122 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [38.1, 26.1]    |  |
| -1090.37 | -1090.37 | 00:29:52.265 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [37.5, 25.8]    | -> Juan Bernat Ve |
| -1088.32 | -1088.32 | 00:29:54.321 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [56.8, 5.0]     |  |
| -1088.32 | -1088.32 | 00:29:54.321 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [56.8, 5.0]     |  |
| -1084.38 | -1084.38 | 00:29:58.259 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [76.4, 4.2]     | -> Leandro Daniel |
| -1083.11 | -1083.11 | 00:29:59.526 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [68.7, 16.6]    |  |
| -1083.11 | -1083.11 | 00:29:59.526 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [68.7, 16.6]    |  |
| -1082.30 | -1082.30 | 00:30:00.338 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [68.7, 16.3]    | -> Lionel Andrés  |
| -1081.27 | -1081.27 | 00:30:01.370 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [66.7, 34.9]    |  |
| -1081.27 | -1081.27 | 00:30:01.370 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [66.7, 34.9]    |  |
| -1079.31 | -1079.31 | 00:30:03.332 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [81.4, 25.5]    | -> Kylian Mbappé  |
| -1078.50 | -1078.50 | 00:30:04.141 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [87.2, 27.7]    |  |
| -1078.50 | -1078.50 | 00:30:04.141 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [87.0, 27.8]    | -> Danilo Luís Hé |
| -1077.51 | -1077.51 | 00:30:05.130 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [74.2, 49.2]    |  |
| -1077.51 | -1077.51 | 00:30:05.130 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [74.2, 49.2]    |  |
| -1076.71 | -1076.71 | 00:30:05.930 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [76.7, 46.9]    | -> Ángel Fabián D |
| -1075.66 | -1075.66 | 00:30:06.974 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [85.7, 54.5]    |  |
| -1075.66 | -1075.66 | 00:30:06.974 | Paris Saint-Germai | Paris Saint-Germai | 142 | Carry           |   -   | [85.7, 54.5]    |  |
| -1074.28 | -1074.28 | 00:30:08.353 | Paris Saint-Germai | Paris Saint-Germai | 142 | Pass            |   -   | [85.3, 52.5]    | -> Lionel Andrés  |
| -1071.97 | -1071.97 | 00:30:10.669 | Paris Saint-Germai | Paris Saint-Germai | 142 | Ball Receipt*   |   -   | [110.6, 26.1]   |  |
| -1071.97 | -1071.97 | 00:30:10.669 | Paris Saint-Germai | Paris Saint-Germai | 142 | Miscontrol      |   -   | [111.2, 25.8]   |  |
| -1045.96 | -1045.96 | 00:30:36.673 | Saint-Étienne      | Saint-Étienne      | 143 | Pass            |   -   | [7.0, 36.1]     | Incomplete (Incomplete) |
| -1042.43 | -1042.43 | 00:30:40.207 | Saint-Étienne      | Saint-Étienne      | 143 | Ball Receipt*   |   -   | [70.8, 17.4]    | Incomplete |
| -1042.43 | -1042.43 | 00:30:40.207 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Recovery   |   -   | [47.9, 65.6]    |  |
| -1042.43 | -1042.43 | 00:30:40.207 | Paris Saint-Germai | Paris Saint-Germai | 144 | Carry           |   -   | [47.9, 65.6]    |  |
| -1041.87 | -1041.87 | 00:30:40.771 | Saint-Étienne      | Paris Saint-Germai | 144 | Pressure        |  Yes  | [69.2, 19.5]    |  |
| -1041.50 | -1041.50 | 00:30:41.135 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pass            |   -   | [48.6, 63.1]    | -> Marcos Aoás Co |
| -1039.98 | -1039.98 | 00:30:42.658 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Receipt*   |   -   | [37.9, 55.8]    |  |
| -1039.98 | -1039.98 | 00:30:42.658 | Paris Saint-Germai | Paris Saint-Germai | 144 | Carry           |   -   | [37.9, 55.8]    |  |
| -1038.69 | -1038.69 | 00:30:43.951 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pass            |   -   | [38.6, 52.8]    | -> Leandro Daniel |
| -1037.34 | -1037.34 | 00:30:45.296 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Receipt*   |   -   | [42.6, 38.1]    |  |
| -1037.34 | -1037.34 | 00:30:45.296 | Paris Saint-Germai | Paris Saint-Germai | 144 | Carry           |   -   | [42.6, 38.1]    |  |
| -1036.53 | -1036.53 | 00:30:46.106 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pass            |   -   | [42.6, 36.3]    | -> Juan Bernat Ve |
| -1034.42 | -1034.42 | 00:30:48.216 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Receipt*   |   -   | [62.0, 6.3]     |  |
| -1034.42 | -1034.42 | 00:30:48.216 | Paris Saint-Germai | Paris Saint-Germai | 144 | Carry           |   -   | [62.0, 6.3]     |  |
| -1031.47 | -1031.47 | 00:30:51.170 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pass            |   -   | [85.3, 8.1]     | -> Neymar da Silv |
| -1030.59 | -1030.59 | 00:30:52.052 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Receipt*   |   -   | [95.0, 3.0]     |  |
| -1030.59 | -1030.59 | 00:30:52.052 | Paris Saint-Germai | Paris Saint-Germai | 144 | Carry           |   -   | [95.0, 3.0]     |  |
| -1029.49 | -1029.49 | 00:30:53.143 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pass            |   -   | [96.4, 3.8]     | Incomplete (Incomplete) |
| -1027.80 | -1027.80 | 00:30:54.837 | Paris Saint-Germai | Paris Saint-Germai | 144 | Pressure        |   -   | [111.1, 11.6]   |  |
| -1026.87 | -1026.87 | 00:30:55.773 | Paris Saint-Germai | Paris Saint-Germai | 144 | Ball Receipt*   |   -   | [115.6, 12.7]   | Incomplete |
| -1026.87 | -1026.87 | 00:30:55.773 | Saint-Étienne      | Paris Saint-Germai | 144 | Interception    |   -   | [3.1, 67.4]     | Lost Out |
| -1009.46 | -1009.46 | 00:31:13.182 | Paris Saint-Germai | Paris Saint-Germai | 145 | Pass            |   -   | [120.0, 0.1]    | -> Ángel Fabián D |
| -1008.57 | -1008.57 | 00:31:14.072 | Paris Saint-Germai | Paris Saint-Germai | 145 | Ball Receipt*   |   -   | [115.6, 3.9]    |  |
| -1008.57 | -1008.57 | 00:31:14.072 | Paris Saint-Germai | Paris Saint-Germai | 145 | Carry           |   -   | [115.6, 3.9]    |  |
| -1006.79 | -1006.79 | 00:31:15.843 | Paris Saint-Germai | Paris Saint-Germai | 145 | Pass            |   -   | [116.8, 5.6]    | -> Sergio Ramos G |
| -1005.61 | -1005.61 | 00:31:17.026 | Paris Saint-Germai | Paris Saint-Germai | 145 | Ball Receipt*   |   -   | [113.6, 39.2]   |  |
| -1005.61 | -1005.61 | 00:31:17.026 | Saint-Étienne      | Paris Saint-Germai | 145 | Duel            |   -   | [6.4, 41.0]     | Aerial Lost |
| -1005.61 | -1005.61 | 00:31:17.026 | Paris Saint-Germai | Paris Saint-Germai | 145 | Miscontrol      |   -   | [113.7, 39.1]   |  |
| -1003.05 | -1003.05 | 00:31:19.586 | Saint-Étienne      | Paris Saint-Germai | 145 | Clearance       |   -   | [14.4, 51.5]    |  |
| -1002.16 | -1002.16 | 00:31:20.473 | Paris Saint-Germai | Paris Saint-Germai | 145 | Ball Recovery   |   -   | [94.3, 18.3]    |  |
| -999.59 | -999.59 | 00:31:23.044 | Paris Saint-Germai | Paris Saint-Germai | 145 | Pass            |   -   | [83.9, 4.9]     | Incomplete (Incomplete) |
| -998.94 | -998.94 | 00:31:23.701 | Paris Saint-Germai | Paris Saint-Germai | 145 | Ball Receipt*   |   -   | [97.9, 4.9]     | Incomplete |
| -998.94 | -998.94 | 00:31:23.701 | Saint-Étienne      | Paris Saint-Germai | 145 | Interception    |   -   | [24.7, 75.7]    | Lost Out |
| -971.82 | -971.82 | 00:31:50.819 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [83.2, 0.1]     | -> Neymar da Silv |
| -971.10 | -971.10 | 00:31:51.537 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [80.0, 10.3]    |  |
| -971.10 | -971.10 | 00:31:51.537 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [80.0, 10.3]    |  |
| -969.91 | -969.91 | 00:31:52.725 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [81.1, 9.7]     | -> Leandro Daniel |
| -968.20 | -968.20 | 00:31:54.442 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [79.8, 27.8]    |  |
| -968.20 | -968.20 | 00:31:54.442 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [79.8, 27.8]    |  |
| -967.40 | -967.40 | 00:31:55.233 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [79.8, 27.8]    | -> Lionel Andrés  |
| -966.06 | -966.06 | 00:31:56.577 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [82.3, 50.0]    |  |
| -966.06 | -966.06 | 00:31:56.577 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [82.3, 50.0]    |  |
| -964.68 | -964.68 | 00:31:57.954 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [84.3, 49.9]    | -> Ángel Fabián D |
| -963.55 | -963.55 | 00:31:59.092 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [94.3, 41.1]    |  |
| -963.55 | -963.55 | 00:31:59.092 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [94.3, 41.1]    |  |
| -963.43 | -963.43 | 00:31:59.206 | Saint-Étienne      | Paris Saint-Germai | 146 | Pressure        |   -   | [25.1, 39.1]    |  |
| -962.85 | -962.85 | 00:31:59.793 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [91.4, 43.0]    | -> Lionel Andrés  |
| -962.28 | -962.28 | 00:32:00.355 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [83.1, 41.0]    |  |
| -962.28 | -962.28 | 00:32:00.355 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [83.1, 41.0]    |  |
| -960.86 | -960.86 | 00:32:01.778 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [86.5, 38.1]    | -> Neymar da Silv |
| -960.36 | -960.36 | 00:32:02.280 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [96.1, 27.8]    |  |
| -960.36 | -960.36 | 00:32:02.280 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [96.1, 27.8]    |  |
| -959.94 | -959.94 | 00:32:02.697 | Saint-Étienne      | Paris Saint-Germai | 146 | Pressure        |   -   | [23.7, 53.5]    |  |
| -959.53 | -959.53 | 00:32:03.109 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [98.2, 26.1]    | -> Juan Bernat Ve |
| -958.51 | -958.51 | 00:32:04.124 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [106.1, 19.4]   |  |
| -958.51 | -958.51 | 00:32:04.124 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [106.1, 19.4]   |  |
| -957.59 | -957.59 | 00:32:05.049 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [109.3, 19.4]   | Incomplete (Incomplete) |
| -956.02 | -956.02 | 00:32:06.614 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [105.9, 42.8]   | Incomplete |
| -956.02 | -956.02 | 00:32:06.614 | Saint-Étienne      | Paris Saint-Germai | 146 | Interception    |   -   | [10.4, 34.1]    | Lost In Play |
| -952.05 | -952.05 | 00:32:10.591 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Recovery   |   -   | [63.7, 36.3]    |  |
| -952.05 | -952.05 | 00:32:10.591 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [63.7, 36.3]    |  |
| -950.39 | -950.39 | 00:32:12.246 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [66.1, 36.0]    | -> Leandro Daniel |
| -948.88 | -948.88 | 00:32:13.754 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [81.4, 44.9]    |  |
| -948.88 | -948.88 | 00:32:13.754 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [81.4, 44.9]    |  |
| -947.62 | -947.62 | 00:32:15.017 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [82.6, 46.3]    | -> Ángel Fabián D |
| -946.12 | -946.12 | 00:32:16.523 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [99.5, 68.9]    |  |
| -946.12 | -946.12 | 00:32:16.523 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [99.5, 68.9]    |  |
| -942.82 | -942.82 | 00:32:19.813 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [94.2, 60.5]    | -> Leandro Daniel |
| -941.84 | -941.84 | 00:32:20.798 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [85.9, 53.9]    |  |
| -941.84 | -941.84 | 00:32:20.798 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [85.9, 53.9]    |  |
| -940.90 | -940.90 | 00:32:21.737 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [84.7, 53.9]    | -> Sergio Ramos G |
| -939.42 | -939.42 | 00:32:23.220 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [85.0, 26.6]    |  |
| -939.42 | -939.42 | 00:32:23.220 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [85.0, 26.6]    |  |
| -937.62 | -937.62 | 00:32:25.020 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [88.6, 23.8]    | -> Juan Bernat Ve |
| -935.46 | -935.46 | 00:32:27.173 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [107.8, 4.5]    |  |
| -935.46 | -935.46 | 00:32:27.173 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [107.8, 4.5]    |  |
| -933.11 | -933.11 | 00:32:29.533 | Saint-Étienne      | Paris Saint-Germai | 146 | Pressure        |   -   | [15.0, 73.1]    |  |
| -931.94 | -931.94 | 00:32:30.698 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [98.6, 5.2]     | -> Neymar da Silv |
| -930.93 | -930.93 | 00:32:31.712 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [85.9, 25.2]    |  |
| -930.93 | -930.93 | 00:32:31.712 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [85.9, 25.2]    |  |
| -930.88 | -930.88 | 00:32:31.762 | Saint-Étienne      | Paris Saint-Germai | 146 | Pressure        |   -   | [29.2, 57.4]    |  |
| -930.15 | -930.15 | 00:32:32.487 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [85.3, 26.0]    | -> Juan Bernat Ve |
| -928.92 | -928.92 | 00:32:33.714 | Saint-Étienne      | Paris Saint-Germai | 146 | Pressure        |   -   | [15.3, 57.4]    |  |
| -928.50 | -928.50 | 00:32:34.138 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [107.8, 24.7]   |  |
| -928.50 | -928.50 | 00:32:34.138 | Paris Saint-Germai | Paris Saint-Germai | 146 | Pass            |   -   | [108.6, 23.9]   | -> Kylian Mbappé  |
| -927.85 | -927.85 | 00:32:34.791 | Paris Saint-Germai | Paris Saint-Germai | 146 | Ball Receipt*   |   -   | [109.7, 36.0]   |  |
| -927.85 | -927.85 | 00:32:34.791 | Paris Saint-Germai | Paris Saint-Germai | 146 | Carry           |   -   | [109.7, 36.0]   |  |
| -927.81 | -927.81 | 00:32:34.831 | Paris Saint-Germai | Paris Saint-Germai | 146 | Miscontrol      |   -   | [109.7, 36.0]   |  |
| -925.88 | -925.88 | 00:32:36.756 | Saint-Étienne      | Paris Saint-Germai | 146 | Clearance       |   -   | [8.2, 24.3]     |  |
| -917.40 | -917.40 | 00:32:45.237 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [77.2, 80.0]    | -> Ángel Fabián D |
| -916.13 | -916.13 | 00:32:46.507 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [79.2, 63.6]    |  |
| -916.13 | -916.13 | 00:32:46.507 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [79.2, 63.6]    |  |
| -913.94 | -913.94 | 00:32:48.696 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [82.9, 65.3]    | -> Danilo Luís Hé |
| -912.66 | -912.66 | 00:32:49.982 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [77.9, 43.5]    |  |
| -912.66 | -912.66 | 00:32:49.982 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [77.9, 43.5]    |  |
| -911.76 | -911.76 | 00:32:50.880 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [77.8, 43.1]    | -> Sergio Ramos G |
| -910.27 | -910.27 | 00:32:52.372 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [82.6, 28.0]    |  |
| -910.27 | -910.27 | 00:32:52.372 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [82.6, 28.0]    |  |
| -909.54 | -909.54 | 00:32:53.093 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [82.6, 28.0]    | -> Juan Bernat Ve |
| -908.29 | -908.29 | 00:32:54.352 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [98.2, 16.3]    |  |
| -908.29 | -908.29 | 00:32:54.352 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [98.2, 16.3]    |  |
| -907.44 | -907.44 | 00:32:55.196 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [98.6, 16.0]    | -> Neymar da Silv |
| -906.84 | -906.84 | 00:32:55.794 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [95.0, 18.8]    |  |
| -906.84 | -906.84 | 00:32:55.794 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [95.0, 18.8]    |  |
| -904.57 | -904.57 | 00:32:58.070 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [94.8, 16.3]    | -> Sergio Ramos G |
| -904.05 | -904.05 | 00:32:58.589 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [87.0, 24.9]    |  |
| -904.05 | -904.05 | 00:32:58.589 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [87.0, 24.9]    |  |
| -902.60 | -902.60 | 00:33:00.036 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [84.5, 27.0]    | -> Lionel Andrés  |
| -901.08 | -901.08 | 00:33:01.555 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [85.9, 56.1]    |  |
| -901.08 | -901.08 | 00:33:01.555 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [85.9, 56.1]    |  |
| -899.61 | -899.61 | 00:33:03.031 | Saint-Étienne      | Paris Saint-Germai | 147 | Pressure        |   -   | [30.3, 24.9]    |  |
| -899.17 | -899.17 | 00:33:03.468 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [86.8, 54.7]    | -> Danilo Luís Hé |
| -897.80 | -897.80 | 00:33:04.842 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [85.0, 40.8]    |  |
| -897.80 | -897.80 | 00:33:04.842 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [85.0, 40.8]    |  |
| -896.94 | -896.94 | 00:33:05.698 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [83.6, 37.5]    | -> Neymar da Silv |
| -895.89 | -895.89 | 00:33:06.750 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [104.5, 22.7]   |  |
| -895.89 | -895.89 | 00:33:06.750 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [104.5, 22.7]   |  |
| -891.19 | -891.19 | 00:33:11.443 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [107.3, 20.8]   | -> Danilo Luís Hé |
| -889.33 | -889.33 | 00:33:13.306 | Saint-Étienne      | Paris Saint-Germai | 147 | Pressure        |   -   | [23.4, 49.6]    |  |
| -889.28 | -889.28 | 00:33:13.357 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [93.1, 28.8]    |  |
| -889.28 | -889.28 | 00:33:13.357 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [93.1, 28.8]    |  |
| -889.20 | -889.20 | 00:33:13.437 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [94.2, 30.6]    | -> Lionel Andrés  |
| -888.51 | -888.51 | 00:33:14.131 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [93.4, 42.0]    |  |
| -888.51 | -888.51 | 00:33:14.131 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [93.4, 42.0]    |  |
| -888.36 | -888.36 | 00:33:14.283 | Saint-Étienne      | Paris Saint-Germai | 147 | Pressure        |   -   | [20.4, 39.8]    |  |
| -887.65 | -887.65 | 00:33:14.986 | Saint-Étienne      | Paris Saint-Germai | 147 | Dribbled Past   |   -   | [24.7, 39.6]    |  |
| -887.65 | -887.65 | 00:33:14.986 | Paris Saint-Germai | Paris Saint-Germai | 147 | Dribble         |   -   | [95.4, 40.5]    |  |
| -887.65 | -887.65 | 00:33:14.986 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [95.4, 40.5]    |  |
| -886.79 | -886.79 | 00:33:15.847 | Saint-Étienne      | Paris Saint-Germai | 147 | Pressure        |   -   | [17.5, 37.3]    |  |
| -886.60 | -886.60 | 00:33:16.042 | Paris Saint-Germai | Paris Saint-Germai | 147 | Pass            |   -   | [98.9, 44.9]    | -> Ángel Fabián D |
| -885.31 | -885.31 | 00:33:17.329 | Paris Saint-Germai | Paris Saint-Germai | 147 | Ball Receipt*   |   -   | [108.6, 53.8]   |  |
| -885.31 | -885.31 | 00:33:17.329 | Paris Saint-Germai | Paris Saint-Germai | 147 | Carry           |   -   | [108.6, 53.8]   |  |
| -883.93 | -883.93 | 00:33:18.707 | Paris Saint-Germai | Paris Saint-Germai | 147 | Shot            |   -   | [111.4, 47.5]   | Goal |
| -883.36 | -883.36 | 00:33:19.274 | Saint-Étienne      | Paris Saint-Germai | 147 | Goal Keeper     |   -   | [1.5, 36.9]     |  |
| -812.11 | -812.11 | 00:34:30.525 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [61.0, 40.1]    | -> Harold Moukoud |
| -809.99 | -809.99 | 00:34:32.647 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [41.5, 49.1]    |  |
| -809.93 | -809.93 | 00:34:32.707 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [42.2, 50.1]    | -> Lucas Gourna-D |
| -809.07 | -809.07 | 00:34:33.568 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [48.1, 41.3]    |  |
| -809.07 | -809.07 | 00:34:33.568 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [48.1, 41.3]    |  |
| -806.90 | -806.90 | 00:34:35.738 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [54.0, 41.6]    | -> Mahdi Camara |
| -806.29 | -806.29 | 00:34:36.345 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [55.8, 47.1]    |  |
| -806.29 | -806.29 | 00:34:36.345 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [55.8, 47.1]    |  |
| -806.21 | -806.21 | 00:34:36.425 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [53.4, 49.0]    | -> Mickaël Nade |
| -804.38 | -804.38 | 00:34:38.256 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [37.5, 40.9]    |  |
| -804.38 | -804.38 | 00:34:38.256 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [37.5, 40.9]    |  |
| -803.69 | -803.69 | 00:34:38.950 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [37.2, 40.4]    | -> Miguel Ángel T |
| -802.25 | -802.25 | 00:34:40.388 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [38.4, 14.5]    |  |
| -802.25 | -802.25 | 00:34:40.388 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [38.4, 14.5]    |  |
| -801.64 | -801.64 | 00:34:40.996 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [39.0, 14.3]    | -> Mickaël Nade |
| -800.28 | -800.28 | 00:34:42.357 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [36.2, 30.7]    |  |
| -800.28 | -800.28 | 00:34:42.357 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [36.2, 30.7]    |  |
| -799.65 | -799.65 | 00:34:42.985 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [35.9, 31.5]    | -> Harold Moukoud |
| -797.91 | -797.91 | 00:34:44.732 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [35.4, 55.2]    |  |
| -797.91 | -797.91 | 00:34:44.732 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [35.4, 55.2]    |  |
| -794.57 | -794.57 | 00:34:48.071 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [48.7, 59.5]    | -> Yvann Macon |
| -792.85 | -792.85 | 00:34:49.790 | Paris Saint-Germai | Saint-Étienne      | 148 | Pressure        |   -   | [65.9, 6.9]     |  |
| -792.65 | -792.65 | 00:34:49.986 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [52.5, 75.9]    |  |
| -792.65 | -792.65 | 00:34:49.986 | Saint-Étienne      | Saint-Étienne      | 148 | Carry           |   -   | [52.5, 75.9]    |  |
| -792.34 | -792.34 | 00:34:50.299 | Saint-Étienne      | Saint-Étienne      | 148 | Pass            |   -   | [52.0, 78.2]    | Incomplete (Out) |
| -790.96 | -790.96 | 00:34:51.682 | Saint-Étienne      | Saint-Étienne      | 148 | Ball Receipt*   |   -   | [64.2, 77.9]    | Incomplete |
| -781.73 | -781.73 | 00:35:00.905 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [55.6, 0.1]     | -> Leandro Daniel |
| -780.46 | -780.46 | 00:35:02.180 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [53.9, 7.2]     |  |
| -778.76 | -778.76 | 00:35:03.874 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [53.9, 7.2]     | -> Sergio Ramos G |
| -774.95 | -774.95 | 00:35:07.685 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [40.0, 5.5]     |  |
| -774.95 | -774.95 | 00:35:07.685 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [40.0, 5.5]     |  |
| -773.66 | -773.66 | 00:35:08.982 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [24.3, 8.5]     | -> Leandro Daniel |
| -771.36 | -771.36 | 00:35:11.281 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [36.8, 28.6]    |  |
| -771.36 | -771.36 | 00:35:11.281 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [36.8, 28.6]    |  |
| -768.70 | -768.70 | 00:35:13.933 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [36.8, 28.5]    | -> Ángel Fabián D |
| -766.96 | -766.96 | 00:35:15.681 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [56.4, 53.3]    |  |
| -766.96 | -766.96 | 00:35:15.681 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [56.4, 53.3]    |  |
| -765.18 | -765.18 | 00:35:17.462 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [62.0, 55.2]    | -> Sergio Ramos G |
| -763.40 | -763.40 | 00:35:19.242 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [50.0, 29.4]    |  |
| -763.40 | -763.40 | 00:35:19.242 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [50.0, 29.4]    |  |
| -762.46 | -762.46 | 00:35:20.177 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [53.9, 28.3]    | -> Neymar da Silv |
| -760.78 | -760.78 | 00:35:21.854 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [83.2, 3.9]     |  |
| -760.78 | -760.78 | 00:35:21.854 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [83.2, 3.9]     |  |
| -760.08 | -760.08 | 00:35:22.556 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [79.8, 5.5]     | -> Juan Bernat Ve |
| -758.60 | -758.60 | 00:35:24.035 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [66.2, 5.6]     |  |
| -758.60 | -758.60 | 00:35:24.035 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [67.6, 6.6]     | -> Leandro Daniel |
| -757.47 | -757.47 | 00:35:25.164 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [63.4, 21.6]    |  |
| -757.47 | -757.47 | 00:35:25.164 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [63.4, 21.6]    |  |
| -756.33 | -756.33 | 00:35:26.308 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [64.3, 24.9]    | -> Lionel Andrés  |
| -754.80 | -754.80 | 00:35:27.833 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [68.7, 51.6]    |  |
| -754.80 | -754.80 | 00:35:27.833 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [68.7, 51.6]    |  |
| -753.08 | -753.08 | 00:35:29.561 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [75.4, 51.9]    | -> Achraf Hakimi  |
| -751.77 | -751.77 | 00:35:30.871 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [82.5, 72.2]    |  |
| -751.77 | -751.77 | 00:35:30.871 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [82.5, 72.2]    |  |
| -751.72 | -751.72 | 00:35:30.923 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [83.7, 75.6]    | -> Ángel Fabián D |
| -751.14 | -751.14 | 00:35:31.501 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [85.9, 71.0]    |  |
| -751.14 | -751.14 | 00:35:31.501 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [85.9, 71.0]    |  |
| -747.66 | -747.66 | 00:35:34.977 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [84.2, 55.5]    | -> Leandro Daniel |
| -746.15 | -746.15 | 00:35:36.487 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [74.5, 37.8]    |  |
| -746.15 | -746.15 | 00:35:36.487 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [74.5, 37.8]    |  |
| -745.65 | -745.65 | 00:35:36.992 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [73.9, 37.8]    | -> Juan Bernat Ve |
| -743.70 | -743.70 | 00:35:38.934 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [80.6, 12.2]    |  |
| -743.70 | -743.70 | 00:35:38.934 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [80.6, 12.2]    |  |
| -742.85 | -742.85 | 00:35:39.788 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [79.2, 11.7]    | -> Neymar da Silv |
| -741.88 | -741.88 | 00:35:40.753 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [97.6, 7.2]     |  |
| -741.88 | -741.88 | 00:35:40.753 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [97.6, 7.2]     |  |
| -738.50 | -738.50 | 00:35:44.142 | Paris Saint-Germai | Paris Saint-Germai | 149 | Pass            |   -   | [113.2, 11.6]   | Incomplete (Incomplete) |
| -737.46 | -737.46 | 00:35:45.175 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [106.1, 36.0]   | Incomplete |
| -737.46 | -737.46 | 00:35:45.175 | Saint-Étienne      | Paris Saint-Germai | 149 | Clearance       |   -   | [11.4, 44.9]    |  |
| -735.51 | -735.51 | 00:35:47.125 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Recovery   |   -   | [21.9, 59.9]    |  |
| -735.51 | -735.51 | 00:35:47.125 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [21.9, 59.9]    |  |
| -735.13 | -735.13 | 00:35:47.503 | Paris Saint-Germai | Saint-Étienne      | 150 | Pressure        |  Yes  | [92.9, 20.2]    |  |
| -733.80 | -733.80 | 00:35:48.843 | Saint-Étienne      | Saint-Étienne      | 150 | Dispossessed    |   -   | [27.2, 58.8]    |  |
| -733.80 | -733.80 | 00:35:48.843 | Paris Saint-Germai | Saint-Étienne      | 150 | Duel            |  Yes  | [92.9, 21.3]    | Tackle, Lost In Play |
| -732.88 | -732.88 | 00:35:49.755 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Recovery   |   -   | [28.7, 57.3]    |  |
| -732.88 | -732.88 | 00:35:49.755 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [28.7, 57.3]    |  |
| -732.30 | -732.30 | 00:35:50.343 | Saint-Étienne      | Saint-Étienne      | 150 | Pass            |   -   | [29.2, 56.2]    | -> Lucas Gourna-D |
| -731.70 | -731.70 | 00:35:50.942 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Receipt*   |   -   | [29.2, 48.4]    |  |
| -731.70 | -731.70 | 00:35:50.942 | Saint-Étienne      | Saint-Étienne      | 150 | Pass            |   -   | [29.2, 48.4]    | -> Yvann Macon |
| -730.95 | -730.95 | 00:35:51.683 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Receipt*   |   -   | [24.8, 61.3]    |  |
| -730.95 | -730.95 | 00:35:51.683 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [24.8, 61.3]    |  |
| -729.94 | -729.94 | 00:35:52.701 | Saint-Étienne      | Saint-Étienne      | 150 | Pass            |   -   | [25.9, 61.8]    | -> Zaydou Youssou |
| -728.86 | -728.86 | 00:35:53.782 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Receipt*   |   -   | [39.0, 76.2]    |  |
| -728.86 | -728.86 | 00:35:53.782 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [39.0, 76.2]    |  |
| -728.34 | -728.34 | 00:35:54.303 | Paris Saint-Germai | Saint-Étienne      | 150 | Pressure        |   -   | [81.2, 4.9]     |  |
| -727.49 | -727.49 | 00:35:55.146 | Saint-Étienne      | Saint-Étienne      | 150 | Pass            |   -   | [36.5, 75.1]    | -> Mahdi Camara |
| -726.76 | -726.76 | 00:35:55.878 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Receipt*   |   -   | [38.9, 65.4]    |  |
| -726.76 | -726.76 | 00:35:55.878 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [38.9, 65.4]    |  |
| -726.35 | -726.35 | 00:35:56.288 | Saint-Étienne      | Saint-Étienne      | 150 | Pass            |   -   | [39.8, 64.1]    | -> Zaydou Youssou |
| -725.07 | -725.07 | 00:35:57.570 | Paris Saint-Germai | Saint-Étienne      | 150 | Pressure        |   -   | [62.9, 4.2]     |  |
| -724.63 | -724.63 | 00:35:58.012 | Saint-Étienne      | Saint-Étienne      | 150 | Ball Receipt*   |   -   | [52.5, 76.2]    |  |
| -724.63 | -724.63 | 00:35:58.012 | Saint-Étienne      | Saint-Étienne      | 150 | Carry           |   -   | [52.5, 76.2]    |  |
| -724.39 | -724.39 | 00:35:58.252 | Saint-Étienne      | Saint-Étienne      | 150 | Dribble         |   -   | [55.3, 76.3]    |  |
| -724.39 | -724.39 | 00:35:58.252 | Paris Saint-Germai | Saint-Étienne      | 150 | Duel            |   -   | [64.8, 3.8]     | Tackle, Lost Out |
| -716.52 | -716.52 | 00:36:06.114 | Saint-Étienne      | Saint-Étienne      | 151 | Pass            |   -   | [54.7, 80.0]    | -> Lucas Gourna-D |
| -714.50 | -714.50 | 00:36:08.142 | Saint-Étienne      | Saint-Étienne      | 151 | Ball Receipt*   |   -   | [54.2, 68.4]    |  |
| -714.31 | -714.31 | 00:36:08.327 | Saint-Étienne      | Saint-Étienne      | 151 | Pass            |   -   | [54.2, 68.1]    | -> Miguel Ángel T |
| -711.85 | -711.85 | 00:36:10.790 | Saint-Étienne      | Saint-Étienne      | 151 | Ball Receipt*   |   -   | [63.6, 7.9]     |  |
| -711.85 | -711.85 | 00:36:10.790 | Saint-Étienne      | Saint-Étienne      | 151 | Carry           |   -   | [63.6, 7.9]     |  |
| -708.40 | -708.40 | 00:36:14.236 | Saint-Étienne      | Saint-Étienne      | 151 | Pass            |   -   | [87.5, 9.8]     | Incomplete (Incomplete) |
| -707.42 | -707.42 | 00:36:15.221 | Saint-Étienne      | Saint-Étienne      | 151 | Ball Receipt*   |   -   | [106.1, 36.5]   | Incomplete |
| -707.42 | -707.42 | 00:36:15.221 | Paris Saint-Germai | Saint-Étienne      | 151 | Interception    |   -   | [15.0, 50.8]    | Lost Out |
| -696.11 | -696.11 | 00:36:26.530 | Saint-Étienne      | Saint-Étienne      | 152 | Pass            |   -   | [107.3, 0.1]    | -> Wahbi Khazri |
| -695.34 | -695.34 | 00:36:27.294 | Paris Saint-Germai | Saint-Étienne      | 152 | Pressure        |   -   | [3.2, 64.4]     |  |
| -694.88 | -694.88 | 00:36:27.758 | Saint-Étienne      | Saint-Étienne      | 152 | Ball Receipt*   |   -   | [113.9, 12.4]   |  |
| -694.88 | -694.88 | 00:36:27.758 | Saint-Étienne      | Saint-Étienne      | 152 | Carry           |   -   | [113.9, 12.4]   |  |
| -694.46 | -694.46 | 00:36:28.174 | Saint-Étienne      | Saint-Étienne      | 152 | Pass            |   -   | [116.9, 13.5]   | Incomplete (Incomplete) |
| -694.07 | -694.07 | 00:36:28.571 | Saint-Étienne      | Saint-Étienne      | 152 | Ball Receipt*   |   -   | [105.0, 12.4]   | Incomplete |
| -694.07 | -694.07 | 00:36:28.571 | Paris Saint-Germai | Paris Saint-Germai | 153 | Interception    |  Yes  | [9.2, 67.7]     | Won |
| -694.07 | -694.07 | 00:36:28.571 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [9.2, 67.7]     |  |
| -693.79 | -693.79 | 00:36:28.844 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [7.8, 70.3]     | -> Danilo Luís Hé |
| -692.90 | -692.90 | 00:36:29.742 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [10.0, 61.7]    |  |
| -692.90 | -692.90 | 00:36:29.742 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [10.0, 61.7]    |  |
| -692.71 | -692.71 | 00:36:29.932 | Saint-Étienne      | Paris Saint-Germai | 153 | Pressure        |  Yes  | [108.4, 13.1]   |  |
| -692.40 | -692.40 | 00:36:30.239 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [9.2, 61.1]     | -> Leandro Daniel |
| -690.17 | -690.17 | 00:36:32.472 | Saint-Étienne      | Paris Saint-Germai | 153 | Pressure        |  Yes  | [106.9, 27.3]   |  |
| -689.71 | -689.71 | 00:36:32.925 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [13.1, 50.2]    |  |
| -689.71 | -689.71 | 00:36:32.925 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [13.9, 47.7]    | -> Sergio Ramos G |
| -688.87 | -688.87 | 00:36:33.772 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [9.5, 42.8]     |  |
| -688.87 | -688.87 | 00:36:33.772 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [9.5, 42.8]     |  |
| -688.73 | -688.73 | 00:36:33.908 | Saint-Étienne      | Paris Saint-Germai | 153 | Pressure        |   -   | [107.9, 36.6]   |  |
| -688.25 | -688.25 | 00:36:34.389 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [9.3, 39.9]     | -> Juan Bernat Ve |
| -686.80 | -686.80 | 00:36:35.841 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [15.4, 24.1]    |  |
| -686.80 | -686.80 | 00:36:35.841 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [15.4, 23.8]    | -> Leandro Daniel |
| -686.07 | -686.07 | 00:36:36.569 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [15.1, 35.2]    |  |
| -686.07 | -686.07 | 00:36:36.569 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [15.1, 35.2]    |  |
| -684.72 | -684.72 | 00:36:37.914 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [22.2, 24.4]    | -> Juan Bernat Ve |
| -683.99 | -683.99 | 00:36:38.653 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [16.1, 19.9]    |  |
| -683.99 | -683.99 | 00:36:38.653 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [16.1, 19.9]    |  |
| -683.26 | -683.26 | 00:36:39.374 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [15.1, 21.1]    | -> Neymar da Silv |
| -682.01 | -682.01 | 00:36:40.624 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [32.2, 5.0]     |  |
| -682.01 | -682.01 | 00:36:40.624 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [32.2, 5.0]     |  |
| -680.18 | -680.18 | 00:36:42.459 | Paris Saint-Germai | Paris Saint-Germai | 153 | Pass            |   -   | [39.3, 4.2]     | -> Kylian Mbappé  |
| -678.80 | -678.80 | 00:36:43.840 | Paris Saint-Germai | Paris Saint-Germai | 153 | Ball Receipt*   |   -   | [48.7, 22.0]    |  |
| -678.80 | -678.80 | 00:36:43.840 | Paris Saint-Germai | Paris Saint-Germai | 153 | Carry           |   -   | [48.7, 22.0]    |  |
| -678.75 | -678.75 | 00:36:43.890 | Saint-Étienne      | Paris Saint-Germai | 153 | Pressure        |   -   | [73.6, 57.9]    |  |
| -677.83 | -677.83 | 00:36:44.806 | Saint-Étienne      | Paris Saint-Germai | 153 | Pressure        |   -   | [67.0, 65.7]    |  |
| -675.65 | -675.65 | 00:36:46.991 | Paris Saint-Germai | Paris Saint-Germai | 153 | Miscontrol      |   -   | [60.3, 2.2]     |  |
| -673.26 | -673.26 | 00:36:49.377 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [38.4, 75.7]    | -> Etienne Green |
| -670.24 | -670.24 | 00:36:52.399 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [10.0, 48.1]    |  |
| -670.24 | -670.24 | 00:36:52.399 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [10.0, 48.1]    |  |
| -668.74 | -668.74 | 00:36:53.903 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [12.8, 47.6]    | -> Miguel Ángel T |
| -666.90 | -666.90 | 00:36:55.741 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [28.7, 25.6]    |  |
| -666.90 | -666.90 | 00:36:55.741 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [28.7, 25.6]    |  |
| -666.05 | -666.05 | 00:36:56.590 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [27.6, 23.7]    | -> Lucas Gourna-D |
| -664.36 | -664.36 | 00:36:58.280 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [37.0, 41.0]    |  |
| -664.36 | -664.36 | 00:36:58.280 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [37.0, 41.0]    |  |
| -661.44 | -661.44 | 00:37:01.193 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [48.1, 49.8]    | -> Mahdi Camara |
| -660.02 | -660.02 | 00:37:02.617 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [55.4, 70.4]    |  |
| -660.02 | -660.02 | 00:37:02.617 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [55.4, 70.4]    |  |
| -658.80 | -658.80 | 00:37:03.841 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [55.4, 70.4]    | -> Zaydou Youssou |
| -658.01 | -658.01 | 00:37:04.631 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [59.2, 78.4]    |  |
| -658.01 | -658.01 | 00:37:04.631 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [59.2, 78.4]    |  |
| -653.94 | -653.94 | 00:37:08.699 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [64.7, 77.3]    | -> Lucas Gourna-D |
| -652.84 | -652.84 | 00:37:09.798 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [55.1, 59.5]    |  |
| -652.84 | -652.84 | 00:37:09.798 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [55.1, 59.5]    |  |
| -652.34 | -652.34 | 00:37:10.301 | Paris Saint-Germai | Saint-Étienne      | 154 | Pressure        |   -   | [63.6, 27.4]    |  |
| -650.95 | -650.95 | 00:37:11.684 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [55.3, 56.6]    | -> Harold Moukoud |
| -649.69 | -649.69 | 00:37:12.943 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [37.6, 61.8]    |  |
| -649.69 | -649.69 | 00:37:12.943 | Saint-Étienne      | Saint-Étienne      | 154 | Carry           |   -   | [37.6, 61.8]    |  |
| -648.50 | -648.50 | 00:37:14.136 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [37.6, 61.8]    | -> Miguel Ángel T |
| -645.39 | -645.39 | 00:37:17.249 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [64.2, 11.2]    |  |
| -645.39 | -645.39 | 00:37:17.249 | Saint-Étienne      | Saint-Étienne      | 154 | Pass            |   -   | [64.2, 9.0]     | Incomplete (Incomplete) |
| -644.22 | -644.22 | 00:37:18.419 | Saint-Étienne      | Saint-Étienne      | 154 | Ball Receipt*   |   -   | [68.6, 21.6]    | Incomplete |
| -644.22 | -644.22 | 00:37:18.419 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [48.2, 59.9]    | -> Lionel Andrés  |
| -641.91 | -641.91 | 00:37:20.726 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [69.8, 67.8]    |  |
| -641.91 | -641.91 | 00:37:20.726 | Paris Saint-Germai | Paris Saint-Germai | 155 | Carry           |   -   | [69.8, 67.8]    |  |
| -641.71 | -641.71 | 00:37:20.927 | Saint-Étienne      | Paris Saint-Germai | 155 | Pressure        |  Yes  | [51.2, 15.2]    |  |
| -638.76 | -638.76 | 00:37:23.876 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [69.3, 54.5]    | -> Ángel Fabián D |
| -637.78 | -637.78 | 00:37:24.857 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [79.7, 39.7]    |  |
| -637.78 | -637.78 | 00:37:24.857 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [79.7, 39.7]    | -> Lionel Andrés  |
| -636.93 | -636.93 | 00:37:25.703 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [76.7, 43.8]    |  |
| -636.93 | -636.93 | 00:37:25.703 | Paris Saint-Germai | Paris Saint-Germai | 155 | Carry           |   -   | [76.7, 43.8]    |  |
| -635.86 | -635.86 | 00:37:26.775 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [79.2, 39.1]    | -> Kylian Mbappé  |
| -634.94 | -634.94 | 00:37:27.698 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [88.9, 33.6]    |  |
| -634.94 | -634.94 | 00:37:27.698 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [88.9, 33.6]    | -> Ángel Fabián D |
| -634.18 | -634.18 | 00:37:28.456 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [88.9, 40.3]    |  |
| -634.18 | -634.18 | 00:37:28.456 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [88.9, 41.4]    | Incomplete (Incomplete) |
| -633.86 | -633.86 | 00:37:28.778 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [95.6, 31.9]    | Incomplete |
| -633.86 | -633.86 | 00:37:28.778 | Saint-Étienne      | Paris Saint-Germai | 155 | Interception    |   -   | [27.2, 41.0]    | Lost In Play |
| -633.14 | -633.14 | 00:37:29.498 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Recovery   |   -   | [94.2, 38.3]    |  |
| -633.14 | -633.14 | 00:37:29.498 | Paris Saint-Germai | Paris Saint-Germai | 155 | Carry           |   -   | [94.2, 38.3]    |  |
| -632.60 | -632.60 | 00:37:30.035 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pass            |   -   | [92.3, 40.3]    | -> Lionel Andrés  |
| -631.80 | -631.80 | 00:37:30.838 | Paris Saint-Germai | Paris Saint-Germai | 155 | Ball Receipt*   |   -   | [97.0, 49.5]    |  |
| -631.80 | -631.80 | 00:37:30.838 | Paris Saint-Germai | Paris Saint-Germai | 155 | Miscontrol      |   -   | [96.4, 50.3]    |  |
| -631.66 | -631.66 | 00:37:30.976 | Paris Saint-Germai | Paris Saint-Germai | 155 | Pressure        |   -   | [97.9, 50.3]    |  |
| -631.57 | -631.57 | 00:37:31.063 | Saint-Étienne      | Saint-Étienne      | 156 | Pass            |   -   | [21.2, 28.8]    | -> Denis Bouanga |
| -629.67 | -629.67 | 00:37:32.963 | Saint-Étienne      | Saint-Étienne      | 156 | Ball Receipt*   |   -   | [41.5, 27.9]    |  |
| -629.67 | -629.67 | 00:37:32.963 | Saint-Étienne      | Saint-Étienne      | 156 | Carry           |   -   | [41.5, 27.9]    |  |
| -629.42 | -629.42 | 00:37:33.220 | Saint-Étienne      | Saint-Étienne      | 156 | Pass            |   -   | [41.5, 27.9]    | -> Wahbi Khazri |
| -627.20 | -627.20 | 00:37:35.442 | Saint-Étienne      | Saint-Étienne      | 156 | Ball Receipt*   |   -   | [50.6, 15.7]    |  |
| -627.20 | -627.20 | 00:37:35.442 | Saint-Étienne      | Saint-Étienne      | 156 | Carry           |   -   | [50.6, 15.7]    |  |
| -624.85 | -624.85 | 00:37:37.786 | Paris Saint-Germai | Saint-Étienne      | 156 | Pressure        |   -   | [43.7, 61.4]    |  |
| -622.23 | -622.23 | 00:37:40.412 | Saint-Étienne      | Saint-Étienne      | 156 | Dispossessed    |   -   | [82.6, 7.6]     |  |
| -622.23 | -622.23 | 00:37:40.412 | Paris Saint-Germai | Saint-Étienne      | 156 | Duel            |   -   | [37.5, 72.5]    | Tackle, Lost Out |
| -614.65 | -614.65 | 00:37:47.986 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [75.3, 0.1]     | -> Wahbi Khazri |
| -613.26 | -613.26 | 00:37:49.379 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [84.5, 3.4]     |  |
| -613.18 | -613.18 | 00:37:49.458 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [86.5, 4.5]     | -> Miguel Ángel T |
| -611.83 | -611.83 | 00:37:50.810 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [69.5, 4.5]     |  |
| -611.35 | -611.35 | 00:37:51.286 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [69.5, 4.5]     | -> Lucas Gourna-D |
| -609.89 | -609.89 | 00:37:52.746 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [68.4, 24.3]    |  |
| -609.89 | -609.89 | 00:37:52.746 | Saint-Étienne      | Saint-Étienne      | 157 | Carry           |   -   | [68.4, 24.3]    |  |
| -608.79 | -608.79 | 00:37:53.846 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [69.8, 24.0]    | -> Zaydou Youssou |
| -607.44 | -607.44 | 00:37:55.195 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [75.3, 42.0]    |  |
| -607.44 | -607.44 | 00:37:55.195 | Saint-Étienne      | Saint-Étienne      | 157 | Carry           |   -   | [75.3, 42.0]    |  |
| -603.17 | -603.17 | 00:37:59.472 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [77.6, 48.2]    | -> Yvann Macon |
| -601.32 | -601.32 | 00:38:01.321 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [78.3, 77.7]    |  |
| -601.32 | -601.32 | 00:38:01.321 | Saint-Étienne      | Saint-Étienne      | 157 | Carry           |   -   | [78.3, 77.7]    |  |
| -598.33 | -598.33 | 00:38:04.304 | Saint-Étienne      | Saint-Étienne      | 157 | Pass            |   -   | [77.3, 73.5]    | Incomplete (Incomplete) |
| -597.14 | -597.14 | 00:38:05.497 | Saint-Étienne      | Saint-Étienne      | 157 | Ball Receipt*   |   -   | [83.9, 54.0]    | Incomplete |
| -597.14 | -597.14 | 00:38:05.497 | Paris Saint-Germai | Paris Saint-Germai | 158 | Pass            |  Yes  | [38.2, 25.3]    | -> Neymar da Silv |
| -595.69 | -595.69 | 00:38:06.947 | Saint-Étienne      | Paris Saint-Germai | 158 | Pressure        |  Yes  | [76.2, 57.9]    |  |
| -595.59 | -595.59 | 00:38:07.046 | Paris Saint-Germai | Paris Saint-Germai | 158 | Ball Receipt*   |   -   | [43.1, 23.5]    |  |
| -595.59 | -595.59 | 00:38:07.046 | Paris Saint-Germai | Paris Saint-Germai | 158 | Carry           |   -   | [43.1, 23.5]    |  |
| -594.64 | -594.64 | 00:38:07.993 | Saint-Étienne      | Paris Saint-Germai | 158 | Foul Committed  |  Yes  | [77.5, 53.4]    |  |
| -594.64 | -594.64 | 00:38:07.993 | Paris Saint-Germai | Paris Saint-Germai | 158 | Foul Won        |   -   | [42.6, 26.7]    |  |
| -591.71 | -591.71 | 00:38:10.925 | Saint-Étienne      | Paris Saint-Germai | 158 | Injury Stoppage |   -   | -               |  |
| -589.64 | -589.64 | 00:38:12.997 | Paris Saint-Germai | Paris Saint-Germai | 158 | Injury Stoppage |   -   | -               |  |
| -423.18 | -423.18 | 00:40:59.461 | Saint-Étienne      | Paris Saint-Germai | 158 | Substitution    |   -   | -               |  |
| -412.81 | -412.81 | 00:41:09.825 | Saint-Étienne      | Paris Saint-Germai | 158 | Substitution    |   -   | -               |  |
| -410.01 | -410.01 | 00:41:12.633 | Saint-Étienne      | Paris Saint-Germai | 158 | Tactical Shift  |   -   | -               |  |
| -353.04 | -353.04 | 00:42:09.595 | Paris Saint-Germai | Paris Saint-Germai | 158 | Substitution    |   -   | -               |  |
| -343.65 | -343.65 | 00:42:18.983 | Paris Saint-Germai | Paris Saint-Germai | 158 | Tactical Shift  |   -   | -               |  |
| -339.79 | -339.79 | 00:42:22.847 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [41.8, 27.4]    | -> Juan Bernat Ve |
| -337.99 | -337.99 | 00:42:24.652 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [47.0, 6.9]     |  |
| -337.99 | -337.99 | 00:42:24.652 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [47.0, 6.9]     |  |
| -337.39 | -337.39 | 00:42:25.251 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [47.0, 6.9]     | -> Leandro Daniel |
| -335.98 | -335.98 | 00:42:26.658 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [41.4, 27.8]    |  |
| -335.98 | -335.98 | 00:42:26.658 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [41.4, 27.8]    |  |
| -334.99 | -334.99 | 00:42:27.645 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [41.2, 28.0]    | -> Marcos Aoás Co |
| -334.12 | -334.12 | 00:42:28.517 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [35.0, 36.0]    |  |
| -334.12 | -334.12 | 00:42:28.517 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [35.0, 36.0]    |  |
| -332.81 | -332.81 | 00:42:29.831 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [34.3, 39.1]    | -> Sergio Ramos G |
| -330.74 | -330.74 | 00:42:31.903 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [34.2, 18.9]    |  |
| -330.74 | -330.74 | 00:42:31.903 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [34.2, 18.9]    | -> Ángel Fabián D |
| -329.57 | -329.57 | 00:42:33.072 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [43.9, 16.3]    |  |
| -329.57 | -329.57 | 00:42:33.072 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [43.9, 16.3]    |  |
| -329.06 | -329.06 | 00:42:33.579 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [78.6, 61.5]    |  |
| -328.69 | -328.69 | 00:42:33.951 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [46.1, 15.6]    | -> Leandro Daniel |
| -327.57 | -327.57 | 00:42:35.064 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [39.3, 28.0]    |  |
| -327.57 | -327.57 | 00:42:35.064 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [39.3, 28.0]    |  |
| -326.52 | -326.52 | 00:42:36.117 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [39.3, 28.0]    | -> Danilo Luís Hé |
| -325.12 | -325.12 | 00:42:37.518 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [44.8, 57.5]    |  |
| -325.12 | -325.12 | 00:42:37.518 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [44.8, 57.5]    |  |
| -323.42 | -323.42 | 00:42:39.221 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [74.4, 27.6]    |  |
| -322.96 | -322.96 | 00:42:39.676 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [45.9, 56.4]    | -> Marcos Aoás Co |
| -321.82 | -321.82 | 00:42:40.817 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [37.6, 48.1]    |  |
| -321.82 | -321.82 | 00:42:40.817 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [37.6, 48.1]    |  |
| -320.40 | -320.40 | 00:42:42.234 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [37.2, 46.7]    | -> Leandro Daniel |
| -319.65 | -319.65 | 00:42:42.984 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [46.4, 47.0]    |  |
| -319.65 | -319.65 | 00:42:42.984 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [46.4, 47.0]    | -> Danilo Luís Hé |
| -318.85 | -318.85 | 00:42:43.792 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [44.5, 60.5]    |  |
| -318.85 | -318.85 | 00:42:43.792 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [44.5, 60.5]    |  |
| -318.09 | -318.09 | 00:42:44.549 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [71.9, 15.6]    |  |
| -317.59 | -317.59 | 00:42:45.046 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [47.6, 59.4]    | -> Leandro Daniel |
| -316.95 | -316.95 | 00:42:45.687 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [48.7, 50.0]    |  |
| -316.95 | -316.95 | 00:42:45.687 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [49.0, 49.4]    | -> Achraf Hakimi  |
| -314.95 | -314.95 | 00:42:47.685 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [55.1, 74.2]    |  |
| -314.95 | -314.95 | 00:42:47.685 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [55.1, 74.2]    |  |
| -314.09 | -314.09 | 00:42:48.545 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [55.7, 74.2]    | -> Danilo Luís Hé |
| -312.66 | -312.66 | 00:42:49.976 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [43.2, 62.5]    |  |
| -312.66 | -312.66 | 00:42:49.976 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [43.2, 62.5]    |  |
| -312.44 | -312.44 | 00:42:50.200 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [43.2, 62.5]    | -> Marcos Aoás Co |
| -310.79 | -310.79 | 00:42:51.852 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [27.5, 54.5]    |  |
| -310.79 | -310.79 | 00:42:51.852 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [27.5, 54.5]    |  |
| -309.04 | -309.04 | 00:42:53.600 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [26.1, 48.9]    | -> Leandro Daniel |
| -308.06 | -308.06 | 00:42:54.574 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [36.2, 43.8]    |  |
| -308.06 | -308.06 | 00:42:54.574 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [36.2, 43.8]    |  |
| -307.10 | -307.10 | 00:42:55.539 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [34.3, 45.5]    | -> Achraf Hakimi  |
| -305.57 | -305.57 | 00:42:57.066 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [39.5, 75.0]    |  |
| -305.57 | -305.57 | 00:42:57.066 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [39.5, 75.0]    |  |
| -304.28 | -304.28 | 00:42:58.363 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [76.4, 4.8]     |  |
| -303.62 | -303.62 | 00:42:59.020 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [37.6, 75.3]    | -> Marcos Aoás Co |
| -301.69 | -301.69 | 00:43:00.945 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [21.7, 54.1]    |  |
| -301.69 | -301.69 | 00:43:00.945 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [21.7, 54.1]    |  |
| -300.71 | -300.71 | 00:43:01.929 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [23.2, 53.5]    | -> Danilo Luís Hé |
| -299.36 | -299.36 | 00:43:03.277 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [39.2, 42.4]    |  |
| -299.36 | -299.36 | 00:43:03.277 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [39.2, 42.4]    |  |
| -298.76 | -298.76 | 00:43:03.877 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [39.3, 43.0]    | -> Ángel Fabián D |
| -297.56 | -297.56 | 00:43:05.078 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [42.2, 27.8]    |  |
| -297.56 | -297.56 | 00:43:05.078 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [42.2, 27.8]    |  |
| -296.24 | -296.24 | 00:43:06.397 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [41.2, 24.7]    | -> Juan Bernat Ve |
| -294.86 | -294.86 | 00:43:07.778 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [51.5, 5.6]     |  |
| -294.86 | -294.86 | 00:43:07.778 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [51.5, 5.6]     |  |
| -293.74 | -293.74 | 00:43:08.901 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [51.5, 5.6]     | -> Ángel Fabián D |
| -292.86 | -292.86 | 00:43:09.778 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [43.1, 8.8]     |  |
| -292.86 | -292.86 | 00:43:09.778 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [43.1, 8.8]     |  |
| -292.34 | -292.34 | 00:43:10.293 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [43.1, 8.8]     | -> Sergio Ramos G |
| -291.09 | -291.09 | 00:43:11.552 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [26.5, 15.0]    |  |
| -291.09 | -291.09 | 00:43:11.552 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [26.5, 15.0]    |  |
| -288.82 | -288.82 | 00:43:13.823 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [23.1, 20.5]    | -> Leandro Daniel |
| -287.42 | -287.42 | 00:43:15.217 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [35.4, 54.2]    |  |
| -287.42 | -287.42 | 00:43:15.217 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [35.4, 54.2]    |  |
| -286.34 | -286.34 | 00:43:16.297 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [34.2, 53.9]    | -> Marcos Aoás Co |
| -283.39 | -283.39 | 00:43:19.246 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [9.8, 46.3]     |  |
| -283.39 | -283.39 | 00:43:19.246 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [9.8, 46.3]     |  |
| -282.08 | -282.08 | 00:43:20.561 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [9.8, 46.1]     | -> Juan Bernat Ve |
| -279.43 | -279.43 | 00:43:23.203 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [37.2, 2.4]     |  |
| -279.43 | -279.43 | 00:43:23.203 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [37.2, 2.4]     |  |
| -274.11 | -274.11 | 00:43:28.523 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [84.3, 17.2]    | -> Kylian Mbappé  |
| -272.34 | -272.34 | 00:43:30.293 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [96.2, 4.2]     |  |
| -272.34 | -272.34 | 00:43:30.293 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [96.2, 4.2]     |  |
| -269.24 | -269.24 | 00:43:33.397 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [94.3, 4.5]     | -> Ángel Fabián D |
| -267.40 | -267.40 | 00:43:35.235 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [83.1, 20.0]    |  |
| -267.40 | -267.40 | 00:43:35.235 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [83.1, 20.0]    |  |
| -267.03 | -267.03 | 00:43:35.613 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [81.8, 22.2]    | -> Eric Junior Di |
| -266.17 | -266.17 | 00:43:36.469 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [82.9, 31.9]    |  |
| -266.17 | -266.17 | 00:43:36.469 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [82.9, 31.9]    | -> Ángel Fabián D |
| -265.19 | -265.19 | 00:43:37.447 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [82.6, 23.1]    |  |
| -265.19 | -265.19 | 00:43:37.447 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [82.6, 23.1]    |  |
| -264.63 | -264.63 | 00:43:38.011 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [82.3, 23.9]    | -> Lionel Andrés  |
| -263.50 | -263.50 | 00:43:39.138 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [82.5, 43.8]    |  |
| -263.50 | -263.50 | 00:43:39.138 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [82.5, 43.8]    |  |
| -261.29 | -261.29 | 00:43:41.352 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [81.4, 43.0]    | -> Leandro Daniel |
| -260.32 | -260.32 | 00:43:42.323 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [72.2, 43.8]    |  |
| -260.32 | -260.32 | 00:43:42.323 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [72.2, 43.8]    |  |
| -259.59 | -259.59 | 00:43:43.052 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [72.2, 43.8]    | -> Lionel Andrés  |
| -258.73 | -258.73 | 00:43:43.911 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [77.3, 37.0]    |  |
| -258.73 | -258.73 | 00:43:43.911 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [77.3, 37.0]    | -> Leandro Daniel |
| -258.01 | -258.01 | 00:43:44.632 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [71.8, 44.2]    |  |
| -258.01 | -258.01 | 00:43:44.632 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [71.8, 44.2]    | -> Lionel Andrés  |
| -257.27 | -257.27 | 00:43:45.367 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [72.0, 37.8]    |  |
| -257.27 | -257.27 | 00:43:45.367 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [72.0, 37.8]    |  |
| -256.94 | -256.94 | 00:43:45.693 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [72.0, 37.2]    | -> Danilo Luís Hé |
| -255.70 | -255.70 | 00:43:46.940 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [70.0, 28.8]    |  |
| -255.70 | -255.70 | 00:43:46.940 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [70.0, 28.8]    |  |
| -255.66 | -255.66 | 00:43:46.980 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [69.3, 28.5]    | -> Ángel Fabián D |
| -254.58 | -254.58 | 00:43:48.061 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [81.4, 22.5]    |  |
| -254.58 | -254.58 | 00:43:48.061 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [81.4, 22.5]    |  |
| -253.31 | -253.31 | 00:43:49.329 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [81.7, 22.5]    | -> Kylian Mbappé  |
| -252.33 | -252.33 | 00:43:50.306 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [89.8, 2.2]     |  |
| -252.33 | -252.33 | 00:43:50.306 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [89.8, 2.2]     |  |
| -251.27 | -251.27 | 00:43:51.366 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [89.8, 2.2]     | -> Juan Bernat Ve |
| -250.20 | -250.20 | 00:43:52.442 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [80.9, 2.5]     |  |
| -250.20 | -250.20 | 00:43:52.442 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [80.9, 2.5]     |  |
| -248.54 | -248.54 | 00:43:54.100 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [76.7, 4.4]     | -> Lionel Andrés  |
| -247.59 | -247.59 | 00:43:55.047 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [74.8, 23.9]    |  |
| -247.59 | -247.59 | 00:43:55.047 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [74.8, 23.9]    |  |
| -246.68 | -246.68 | 00:43:55.959 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [77.5, 23.5]    | -> Ángel Fabián D |
| -245.83 | -245.83 | 00:43:56.808 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [81.4, 14.9]    |  |
| -245.83 | -245.83 | 00:43:56.808 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [81.4, 14.9]    |  |
| -244.61 | -244.61 | 00:43:58.023 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [86.2, 14.4]    | -> Kylian Mbappé  |
| -242.89 | -242.89 | 00:43:59.749 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [90.1, 2.8]     |  |
| -242.89 | -242.89 | 00:43:59.749 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [90.1, 2.8]     |  |
| -240.26 | -240.26 | 00:44:02.379 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [87.8, 4.5]     | -> Lionel Andrés  |
| -239.20 | -239.20 | 00:44:03.442 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [82.9, 24.5]    |  |
| -239.20 | -239.20 | 00:44:03.442 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [82.0, 25.8]    | -> Sergio Ramos G |
| -238.01 | -238.01 | 00:44:04.626 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [66.2, 21.6]    |  |
| -238.01 | -238.01 | 00:44:04.626 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [66.2, 21.6]    |  |
| -236.95 | -236.95 | 00:44:05.690 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [66.2, 21.6]    | -> Ángel Fabián D |
| -235.42 | -235.42 | 00:44:07.222 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [82.9, 4.9]     |  |
| -235.42 | -235.42 | 00:44:07.222 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [82.9, 4.9]     |  |
| -233.55 | -233.55 | 00:44:09.088 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [82.9, 4.9]     | -> Sergio Ramos G |
| -232.44 | -232.44 | 00:44:10.193 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [62.3, 18.8]    |  |
| -232.44 | -232.44 | 00:44:10.193 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [62.3, 18.8]    |  |
| -231.84 | -231.84 | 00:44:10.796 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [57.2, 58.1]    |  |
| -231.35 | -231.35 | 00:44:11.284 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [62.8, 18.3]    | -> Ángel Fabián D |
| -230.75 | -230.75 | 00:44:11.888 | Saint-Étienne      | Paris Saint-Germai | 159 | Pressure        |   -   | [40.9, 69.9]    |  |
| -230.56 | -230.56 | 00:44:12.080 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [79.3, 6.3]     |  |
| -230.56 | -230.56 | 00:44:12.080 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [79.3, 6.3]     |  |
| -229.22 | -229.22 | 00:44:13.414 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [71.2, 9.1]     | -> Sergio Ramos G |
| -228.36 | -228.36 | 00:44:14.278 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [57.0, 11.4]    |  |
| -228.36 | -228.36 | 00:44:14.278 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [57.0, 11.4]    |  |
| -227.10 | -227.10 | 00:44:15.537 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [57.0, 11.4]    | -> Leandro Daniel |
| -225.85 | -225.85 | 00:44:16.785 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [63.1, 39.5]    |  |
| -225.85 | -225.85 | 00:44:16.785 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [63.1, 39.5]    |  |
| -224.77 | -224.77 | 00:44:17.865 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [63.1, 39.5]    | -> Eric Junior Di |
| -223.55 | -223.55 | 00:44:19.090 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [72.0, 59.2]    |  |
| -223.55 | -223.55 | 00:44:19.090 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [72.6, 58.5]    | -> Marcos Aoás Co |
| -222.81 | -222.81 | 00:44:19.826 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [67.9, 59.7]    |  |
| -222.81 | -222.81 | 00:44:19.826 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [67.9, 59.7]    |  |
| -221.09 | -221.09 | 00:44:21.553 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [66.7, 60.3]    | -> Kylian Mbappé  |
| -218.69 | -218.69 | 00:44:23.950 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [104.0, 50.3]   |  |
| -218.69 | -218.69 | 00:44:23.950 | Paris Saint-Germai | Paris Saint-Germai | 159 | Carry           |   -   | [104.0, 50.3]   |  |
| -215.41 | -215.41 | 00:44:27.223 | Paris Saint-Germai | Paris Saint-Germai | 159 | Pass            |   -   | [113.6, 57.4]   | Incomplete (Incomplete) |
| -214.11 | -214.11 | 00:44:28.532 | Paris Saint-Germai | Paris Saint-Germai | 159 | Ball Receipt*   |   -   | [110.7, 32.0]   | Incomplete |
| -214.11 | -214.11 | 00:44:28.532 | Saint-Étienne      | Paris Saint-Germai | 159 | Interception    |   -   | [7.0, 41.6]     | Lost Out |
| -190.02 | -190.02 | 00:44:52.622 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [120.0, 0.1]    | -> Juan Bernat Ve |
| -188.62 | -188.62 | 00:44:54.019 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [115.3, 3.9]    |  |
| -187.22 | -187.22 | 00:44:55.423 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [117.0, 5.2]    | -> Lionel Andrés  |
| -186.24 | -186.24 | 00:44:56.399 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [107.9, 2.2]    |  |
| -186.24 | -186.24 | 00:44:56.399 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [107.9, 2.2]    |  |
| -185.67 | -185.67 | 00:44:56.968 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [106.7, 3.8]    | -> Ángel Fabián D |
| -184.14 | -184.14 | 00:44:58.494 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [91.7, 16.9]    |  |
| -184.14 | -184.14 | 00:44:58.494 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [91.7, 16.9]    |  |
| -182.60 | -182.60 | 00:45:00.039 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [91.7, 16.9]    | -> Leandro Daniel |
| -180.82 | -180.82 | 00:45:01.818 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [83.6, 39.5]    |  |
| -180.82 | -180.82 | 00:45:01.818 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [83.6, 39.5]    |  |
| -179.83 | -179.83 | 00:45:02.804 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [83.7, 39.9]    | -> Achraf Hakimi  |
| -178.10 | -178.10 | 00:45:04.539 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [86.2, 67.2]    |  |
| -178.10 | -178.10 | 00:45:04.539 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [86.2, 67.2]    |  |
| -177.63 | -177.63 | 00:45:05.010 | Saint-Étienne      | Paris Saint-Germai | 160 | Pressure        |   -   | [28.6, 13.8]    |  |
| -177.15 | -177.15 | 00:45:05.491 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [85.3, 65.8]    | -> Sergio Ramos G |
| -175.37 | -175.37 | 00:45:07.268 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [66.4, 40.2]    |  |
| -175.37 | -175.37 | 00:45:07.268 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [66.4, 40.2]    |  |
| -174.47 | -174.47 | 00:45:08.169 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [64.8, 38.3]    | -> Ángel Fabián D |
| -172.84 | -172.84 | 00:45:09.799 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [69.5, 22.5]    |  |
| -172.84 | -172.84 | 00:45:09.799 | Paris Saint-Germai | Paris Saint-Germai | 160 | Carry           |   -   | [69.5, 22.5]    |  |
| -169.32 | -169.32 | 00:45:13.315 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [80.6, 22.7]    | -> Lionel Andrés  |
| -166.47 | -166.47 | 00:45:16.171 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [114.3, 14.4]   |  |
| -166.47 | -166.47 | 00:45:16.171 | Paris Saint-Germai | Paris Saint-Germai | 160 | Pass            |   -   | [115.3, 15.3]   | -> Marcos Aoás Co |
| -164.81 | -164.81 | 00:45:17.831 | Paris Saint-Germai | Paris Saint-Germai | 160 | Ball Receipt*   |   -   | [113.7, 43.6]   |  |
| -164.80 | -164.80 | 00:45:17.834 | Saint-Étienne      | Paris Saint-Germai | 160 | Duel            |   -   | [4.9, 38.9]     | Aerial Lost |
| -164.80 | -164.80 | 00:45:17.834 | Paris Saint-Germai | Paris Saint-Germai | 160 | Shot            |   -   | [115.2, 41.2]   | Goal |
| -164.06 | -164.06 | 00:45:18.575 | Saint-Étienne      | Paris Saint-Germai | 160 | Goal Keeper     |   -   | [1.2, 40.5]     |  |
| -97.70 | -97.70 | 00:46:24.933 | Saint-Étienne      | Saint-Étienne      | 161 | Pass            |   -   | [61.0, 40.1]    | -> Wahbi Khazri |
| -96.98 | -96.98 | 00:46:25.654 | Saint-Étienne      | Saint-Étienne      | 161 | Ball Receipt*   |   -   | [59.8, 44.1]    |  |
| -96.40 | -96.40 | 00:46:26.233 | Saint-Étienne      | Saint-Étienne      | 161 | Pass            |   -   | [59.8, 44.1]    | -> Zaydou Youssou |
| -95.57 | -95.57 | 00:46:27.069 | Saint-Étienne      | Saint-Étienne      | 161 | Ball Receipt*   |   -   | [53.4, 45.9]    |  |
| -95.57 | -95.57 | 00:46:27.069 | Saint-Étienne      | Saint-Étienne      | 161 | Carry           |   -   | [53.4, 45.9]    |  |
| -94.75 | -94.75 | 00:46:27.890 | Saint-Étienne      | Saint-Étienne      | 161 | Pass            |   -   | [53.4, 45.9]    | -> Miguel Ángel T |
| -92.91 | -92.91 | 00:46:29.726 | Saint-Étienne      | Saint-Étienne      | 161 | Ball Receipt*   |   -   | [44.4, 22.0]    |  |
| -92.91 | -92.91 | 00:46:29.726 | Saint-Étienne      | Saint-Étienne      | 161 | Carry           |   -   | [44.4, 22.0]    |  |
| -91.55 | -91.55 | 00:46:31.093 | Saint-Étienne      | Saint-Étienne      | 161 | Pass            |   -   | [46.4, 20.1]    | Incomplete (Out) |
| -90.13 | -90.13 | 00:46:32.507 | Saint-Étienne      | Saint-Étienne      | 161 | Ball Receipt*   |   -   | [63.6, 4.6]     | Incomplete |
| -75.15 | -75.15 | 00:46:47.491 | Paris Saint-Germai | Paris Saint-Germai | 162 | Pass            |   -   | [56.5, 80.0]    | -> Leandro Daniel |
| -73.86 | -73.86 | 00:46:48.782 | Saint-Étienne      | Paris Saint-Germai | 162 | Pressure        |   -   | [63.7, 13.2]    |  |
| -73.36 | -73.36 | 00:46:49.282 | Paris Saint-Germai | Paris Saint-Germai | 162 | Ball Receipt*   |   -   | [54.2, 64.4]    |  |
| -73.36 | -73.36 | 00:46:49.282 | Paris Saint-Germai | Paris Saint-Germai | 162 | Carry           |   -   | [54.2, 64.4]    |  |
| -73.28 | -73.28 | 00:46:49.362 | Paris Saint-Germai | Paris Saint-Germai | 162 | Pass            |   -   | [54.2, 65.3]    | Incomplete (Incomplete) |
| -71.61 | -71.61 | 00:46:51.023 | Saint-Étienne      | Paris Saint-Germai | 162 | Ball Recovery   |   -   | [79.5, 17.0]    |  |
| -71.61 | -71.61 | 00:46:51.023 | Saint-Étienne      | Paris Saint-Germai | 162 | Carry           |   -   | [79.5, 17.0]    |  |
| -70.27 | -70.27 | 00:46:52.371 | Paris Saint-Germai | Paris Saint-Germai | 162 | Pressure        |  Yes  | [40.1, 62.4]    |  |
| -67.77 | -67.77 | 00:46:54.864 | Saint-Étienne      | Paris Saint-Germai | 162 | Shot            |   -   | [101.9, 21.1]   | Saved |
| -66.88 | -66.88 | 00:46:55.753 | Paris Saint-Germai | Paris Saint-Germai | 162 | Goal Keeper     |   -   | [1.3, 43.0]     |  |
| -62.39 | -62.39 | 00:47:00.250 | Paris Saint-Germai | Paris Saint-Germai | 163 | Pass            |   -   | [13.9, 35.6]    | -> Juan Bernat Ve |
| -59.92 | -59.92 | 00:47:02.717 | Paris Saint-Germai | Paris Saint-Germai | 163 | Ball Receipt*   |   -   | [36.7, 24.5]    |  |
| -56.87 | -56.87 | 00:47:05.766 | Paris Saint-Germai | Paris Saint-Germai | 164 | Pass            |   -   | [38.9, 23.8]    | -> Ángel Fabián D |
| -55.36 | -55.36 | 00:47:07.273 | Paris Saint-Germai | Paris Saint-Germai | 164 | Ball Receipt*   |   -   | [42.8, 5.6]     |  |
| -54.05 | -54.05 | 00:47:08.583 | Paris Saint-Germai | Paris Saint-Germai | 165 | Pass            |   -   | [45.4, 6.3]     | -> Leandro Daniel |
| -53.11 | -53.11 | 00:47:09.525 | Paris Saint-Germai | Paris Saint-Germai | 165 | Ball Receipt*   |   -   | [39.2, 12.4]    |  |
| -53.11 | -53.11 | 00:47:09.525 | Paris Saint-Germai | Paris Saint-Germai | 166 | Pass            |   -   | [39.2, 12.4]    | -> Ángel Fabián D |
| -52.07 | -52.07 | 00:47:10.571 | Paris Saint-Germai | Paris Saint-Germai | 166 | Ball Receipt*   |   -   | [44.5, 4.4]     |  |
| -52.07 | -52.07 | 00:47:10.571 | Paris Saint-Germai | Paris Saint-Germai | 166 | Carry           |   -   | [44.5, 4.4]     |  |
| -51.69 | -51.69 | 00:47:10.950 | Paris Saint-Germai | Paris Saint-Germai | 167 | Pass            |   -   | [44.5, 5.6]     | -> Juan Bernat Ve |
| -51.11 | -51.11 | 00:47:11.526 | Paris Saint-Germai | Paris Saint-Germai | 167 | Ball Receipt*   |   -   | [36.5, 3.3]     |  |
| -51.11 | -51.11 | 00:47:11.526 | Paris Saint-Germai | Paris Saint-Germai | 168 | Pass            |   -   | [36.2, 3.3]     | -> Leandro Daniel |
| -49.87 | -49.87 | 00:47:12.772 | Paris Saint-Germai | Paris Saint-Germai | 168 | Ball Receipt*   |   -   | [33.6, 17.2]    |  |
| -49.87 | -49.87 | 00:47:12.772 | Paris Saint-Germai | Paris Saint-Germai | 168 | Carry           |   -   | [33.6, 17.2]    |  |
| -48.87 | -48.87 | 00:47:13.772 | Paris Saint-Germai | Paris Saint-Germai | 169 | Pass            |   -   | [32.2, 18.3]    | -> Danilo Luís Hé |
| -47.73 | -47.73 | 00:47:14.910 | Paris Saint-Germai | Paris Saint-Germai | 169 | Ball Receipt*   |   -   | [47.2, 31.3]    |  |
| -47.73 | -47.73 | 00:47:14.910 | Paris Saint-Germai | Paris Saint-Germai | 170 | Pass            |   -   | [47.2, 31.3]    | -> Marcos Aoás Co |
| -45.82 | -45.82 | 00:47:16.817 | Paris Saint-Germai | Paris Saint-Germai | 170 | Ball Receipt*   |   -   | [28.4, 54.2]    |  |
| -45.82 | -45.82 | 00:47:16.817 | Paris Saint-Germai | Paris Saint-Germai | 170 | Carry           |   -   | [28.4, 54.2]    |  |
| -43.34 | -43.34 | 00:47:19.300 | Paris Saint-Germai | Paris Saint-Germai | 171 | Pass            |   -   | [38.2, 57.0]    | -> Danilo Luís Hé |
| -42.32 | -42.32 | 00:47:20.317 | Paris Saint-Germai | Paris Saint-Germai | 171 | Ball Receipt*   |   -   | [45.7, 46.0]    |  |
| -42.32 | -42.32 | 00:47:20.317 | Paris Saint-Germai | Paris Saint-Germai | 171 | Carry           |   -   | [45.7, 46.0]    |  |
| -41.25 | -41.25 | 00:47:21.391 | Paris Saint-Germai | Paris Saint-Germai | 172 | Pass            |   -   | [43.2, 43.1]    | -> Ángel Fabián D |
| -39.09 | -39.09 | 00:47:23.552 | Paris Saint-Germai | Paris Saint-Germai | 172 | Ball Receipt*   |   -   | [57.0, 21.4]    |  |
| -39.09 | -39.09 | 00:47:23.552 | Paris Saint-Germai | Paris Saint-Germai | 172 | Carry           |   -   | [57.0, 21.4]    |  |
| -37.47 | -37.47 | 00:47:25.165 | Paris Saint-Germai | Paris Saint-Germai | 173 | Pass            |   -   | [64.2, 15.5]    | -> Kylian Mbappé  |
| -35.79 | -35.79 | 00:47:26.846 | Paris Saint-Germai | Paris Saint-Germai | 173 | Ball Receipt*   |   -   | [82.6, 3.0]     |  |
| -35.79 | -35.79 | 00:47:26.846 | Paris Saint-Germai | Paris Saint-Germai | 173 | Carry           |   -   | [82.6, 3.0]     |  |
| -32.87 | -32.87 | 00:47:29.767 | Paris Saint-Germai | Paris Saint-Germai | 174 | Pass            |   -   | [94.7, 19.5]    | -> Lionel Andrés  |
| -31.75 | -31.75 | 00:47:30.887 | Paris Saint-Germai | Paris Saint-Germai | 174 | Ball Receipt*   |   -   | [86.5, 44.9]    |  |
| -31.75 | -31.75 | 00:47:30.887 | Paris Saint-Germai | Paris Saint-Germai | 174 | Carry           |   -   | [86.5, 44.9]    |  |
| -30.38 | -30.38 | 00:47:32.257 | Saint-Étienne      | Paris Saint-Germai | 174 | Pressure        |  Yes  | [33.6, 37.1]    |  |
| -29.36 | -29.36 | 00:47:33.274 | Paris Saint-Germai | Paris Saint-Germai | 175 | Pass            |   -   | [93.6, 49.5]    | -> Achraf Hakimi  |
| -27.75 | -27.75 | 00:47:34.884 | Paris Saint-Germai | Paris Saint-Germai | 175 | Ball Receipt*   |   -   | [107.8, 56.0]   |  |
| -27.75 | -27.75 | 00:47:34.884 | Paris Saint-Germai | Paris Saint-Germai | 176 | Pass            |   -   | [107.8, 56.0]   | Incomplete (Pass Offside) |
| -26.73 | -26.73 | 00:47:35.910 | Paris Saint-Germai | Paris Saint-Germai | 176 | Ball Receipt*   |   -   | [113.9, 39.1]   | Incomplete |
|  -5.28 |  -5.28 | 00:47:57.353 | Saint-Étienne      | Saint-Étienne      | 177 | Pass            |   -   | [6.5, 41.3]     | -> Jean-Philippe  |
|  -1.71 |  -1.71 | 00:48:00.929 | Saint-Étienne      | Saint-Étienne      | 177 | Ball Receipt*   |   -   | [71.7, 22.7]    |  |
|  -1.71 |  -1.71 | 00:48:00.929 | Paris Saint-Germai | Saint-Étienne      | 177 | Duel            |   -   | [49.2, 55.3]    | Aerial Lost |
|  -1.71 |  -1.71 | 00:48:00.929 | Saint-Étienne      | Saint-Étienne      | 177 | Miscontrol      |   -   | [70.9, 24.8]    |  |
|  -0.46 |  -0.46 | 00:48:02.178 | Saint-Étienne      | Saint-Étienne      | 177 | Pressure        |   -   | [68.1, 24.9]    |  |
|  -0.41 |  -0.41 | 00:48:02.229 | Paris Saint-Germai | Paris Saint-Germai | 178 | Ball Recovery   |   -   | [55.7, 55.3]    |  |
|  -0.41 |  -0.41 | 00:48:02.229 | Paris Saint-Germai | Paris Saint-Germai | 178 | Carry           |   -   | [55.7, 55.3]    |  |
|  +0.17 |  +0.17 | 00:48:02.809 | Paris Saint-Germai | Paris Saint-Germai | 178 | Pass            |   -   | [55.7, 56.7]    | -> Marcos Aoás Co |
|  +1.49 |  +1.49 | 00:48:04.125 | Paris Saint-Germai | Paris Saint-Germai | 178 | Ball Receipt*   |   -   | [42.2, 53.3]    |  |
|  +1.49 |  +1.49 | 00:48:04.125 | Paris Saint-Germai | Paris Saint-Germai | 178 | Carry           |   -   | [42.2, 53.3]    |  |
|  +3.45 |  +3.45 | 00:48:06.092 | Paris Saint-Germai | Paris Saint-Germai | 178 | Pass            |   -   | [42.5, 52.8]    | -> Juan Bernat Ve |
|  +5.72 |  +5.72 | 00:48:08.353 | Paris Saint-Germai | Paris Saint-Germai | 178 | Ball Receipt*   |   -   | [41.4, 24.1]    |  |
|  +5.72 |  +5.72 | 00:48:08.353 | Paris Saint-Germai | Paris Saint-Germai | 178 | Carry           |   -   | [41.4, 24.1]    |  |
|  +6.69 |  +6.69 | 00:48:09.330 | Paris Saint-Germai | Paris Saint-Germai | 178 | Pass            |   -   | [41.4, 24.1]    | -> Ángel Fabián D |
|  +7.97 |  +7.97 | 00:48:10.608 | Paris Saint-Germai | Paris Saint-Germai | 178 | Ball Receipt*   |   -   | [55.6, 10.5]    |  |
|  +7.97 |  +7.97 | 00:48:10.608 | Paris Saint-Germai | Paris Saint-Germai | 178 | Carry           |   -   | [55.6, 10.5]    |  |
|  +9.67 |  +9.67 | 00:48:12.306 | Paris Saint-Germai | Paris Saint-Germai | 178 | Pass            |   -   | [55.6, 10.5]    | Incomplete (Incomplete) |
| +12.81 | +12.81 | 00:48:15.447 | Paris Saint-Germai | Paris Saint-Germai | 178 | Ball Receipt*   |   -   | [100.0, 28.8]   | Incomplete |

---

### Disagreement Case 13: `3802709_p70_f42b2960`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3802709 (Ligue 1, 2021/2022)
- **counterpressing_team**: Saint-Étienne
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Saint-Étienne
- **possession_id_at_counterpress_initiation**: 70
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:29:48.276) | **Initiation**: Duel (00:29:48.276)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.011s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.975s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.33 |  -1.33 | 00:29:46.951 | Paris Saint-Germai | Paris Saint-Germai | 69 | Ball Receipt*   |   -   | [103.1, 36.1]   |  |
|  -1.33 |  -1.33 | 00:29:46.951 | Paris Saint-Germai | Paris Saint-Germai | 69 | Carry           |   -   | [103.1, 36.1]   |  |
|  -1.01 |  -1.01 | 00:29:47.265 | Saint-Étienne      | Paris Saint-Germai | 69 | Pressure        |   -   | [14.0, 43.3]    |  |
|  -0.28 |  -0.28 | 00:29:47.996 | Saint-Étienne      | Paris Saint-Germai | 69 | Pressure        |   -   | [12.8, 47.2]    |  |
|  +0.00 |  +0.00 | 00:29:48.276 | Paris Saint-Germai | Paris Saint-Germai | 69 | Dribble         |   -   | [108.1, 32.5]   |  |
|  +0.00 |  +0.00 | 00:29:48.276 | Saint-Étienne      | Saint-Étienne      | 70 | Duel            |  Yes  | [12.0, 47.6]    | Tackle, Success In Play |
|  +1.01 |  +1.01 | 00:29:49.287 | Saint-Étienne      | Saint-Étienne      | 70 | Clearance       |   -   | [11.4, 45.2]    |  |
|  +1.98 |  +1.98 | 00:29:50.259 | Paris Saint-Germai | Saint-Étienne      | 70 | Pass            |   -   | [90.0, 24.5]    | Incomplete (Incomplete) |
|  +4.06 |  +4.06 | 00:29:52.334 | Saint-Étienne      | Saint-Étienne      | 70 | Clearance       |   -   | [9.9, 44.0]     |  |
|  +5.97 |  +5.97 | 00:29:54.251 | Saint-Étienne      | Saint-Étienne      | 70 | Ball Recovery   |   -   | [14.8, 57.1]    |  |
|  +5.97 |  +5.97 | 00:29:54.251 | Saint-Étienne      | Saint-Étienne      | 70 | Carry           |   -   | [14.8, 57.1]    |  |
|  +7.79 |  +7.79 | 00:29:56.070 | Saint-Étienne      | Saint-Étienne      | 70 | Pass            |   -   | [20.6, 60.4]    | -> Arnaud Nordin |
|  +8.35 |  +8.35 | 00:29:56.627 | Paris Saint-Germai | Saint-Étienne      | 70 | Pressure        |   -   | [91.5, 3.5]     |  |
|  +8.66 |  +8.66 | 00:29:56.941 | Saint-Étienne      | Saint-Étienne      | 70 | Ball Receipt*   |   -   | [30.5, 77.4]    |  |
|  +8.66 |  +8.66 | 00:29:56.941 | Saint-Étienne      | Saint-Étienne      | 70 | Carry           |   -   | [30.5, 77.4]    |  |
| +12.05 | +12.05 | 00:30:00.322 | Paris Saint-Germai | Saint-Étienne      | 70 | Pressure        |   -   | [90.9, 7.1]     |  |
| +14.53 | +14.53 | 00:30:02.803 | Paris Saint-Germai | Saint-Étienne      | 70 | Pressure        |   -   | [91.2, 11.7]    |  |

---

### Disagreement Case 14: `3942382_p38_2dafadef`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3942382 (UEFA Euro, 2024)
- **counterpressing_team**: Turkey
- **opponent_team_at_turnover**: Netherlands
- **possession_team_at_counterpress_initiation**: Turkey
- **possession_id_at_counterpress_initiation**: 38
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:29:24.011) | **Initiation**: Duel (00:29:24.011)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.236s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.86 |  -3.86 | 00:29:20.156 | Netherlands        | Netherlands        | 37 | Block           |  Yes  | [20.0, 23.5]    |  |
|  -1.59 |  -1.59 | 00:29:22.425 | Netherlands        | Netherlands        | 37 | Ball Recovery   |   -   | [29.8, 16.4]    |  |
|  -1.59 |  -1.59 | 00:29:22.425 | Netherlands        | Netherlands        | 37 | Carry           |   -   | [29.8, 16.4]    |  |
|  -0.68 |  -0.68 | 00:29:23.334 | Turkey             | Netherlands        | 37 | Pressure        |   -   | [90.6, 64.6]    |  |
|  +0.00 |  +0.00 | 00:29:24.011 | Netherlands        | Netherlands        | 37 | Dribble         |   -   | [32.0, 14.9]    |  |
|  +0.00 |  +0.00 | 00:29:24.011 | Turkey             | Turkey             | 38 | Duel            |  Yes  | [88.1, 65.2]    | Tackle, Success In Play |
|  +0.24 |  +0.24 | 00:29:24.247 | Netherlands        | Turkey             | 38 | Foul Committed  |  Yes  | [32.0, 14.9]    |  |
|  +0.24 |  +0.24 | 00:29:24.247 | Turkey             | Turkey             | 38 | Foul Won        |   -   | [88.1, 65.2]    |  |
|  +1.07 |  +1.07 | 00:29:25.079 | Netherlands        | Turkey             | 38 | Injury Stoppage |   -   | -               |  |
| +60.84 | +60.84 | 00:30:24.853 | Turkey             | Turkey             | 38 | Injury Stoppage |   -   | -               |  |
| +100.57 | +100.57 | 00:31:04.578 | Turkey             | Turkey             | 39 | Pass            |   -   | [89.3, 65.6]    | Incomplete (Incomplete) |
| +101.92 | +101.92 | 00:31:05.934 | Netherlands        | Turkey             | 39 | Goal Keeper     |   -   | [5.1, 41.3]     |  |
| +104.40 | +104.40 | 00:31:08.416 | Turkey             | Turkey             | 39 | Ball Recovery   |   -   | [92.1, 24.0]    |  |
| +104.40 | +104.40 | 00:31:08.416 | Turkey             | Turkey             | 39 | Carry           |   -   | [92.1, 24.0]    |  |
| +106.42 | +106.42 | 00:31:10.430 | Turkey             | Turkey             | 39 | Pass            |   -   | [92.9, 25.2]    | -> Kaan Ayhan |
| +108.98 | +108.98 | 00:31:12.992 | Turkey             | Turkey             | 39 | Ball Receipt*   |   -   | [109.4, 61.4]   |  |
| +108.98 | +108.98 | 00:31:12.992 | Turkey             | Turkey             | 39 | Carry           |   -   | [109.4, 61.4]   |  |

---

### Disagreement Case 15: `3930175_p117_8847c733`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3930175 (UEFA Euro, 2024)
- **counterpressing_team**: Romania
- **opponent_team_at_turnover**: Belgium
- **possession_team_at_counterpress_initiation**: Romania
- **possession_id_at_counterpress_initiation**: 117
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:16:01.381) | **Initiation**: Duel (00:16:01.381)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.466s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.85 |  -1.85 | 00:15:59.533 | Romania            | Belgium            | 116 | Pressure        |   -   | [5.2, 76.1]     |  |
|  -1.84 |  -1.84 | 00:15:59.538 | Belgium            | Belgium            | 116 | Ball Recovery   |   -   | [114.5, 5.3]    |  |
|  -1.84 |  -1.84 | 00:15:59.538 | Belgium            | Belgium            | 116 | Carry           |   -   | [114.5, 5.3]    |  |
|  -0.89 |  -0.89 | 00:16:00.486 | Romania            | Belgium            | 116 | Pressure        |   -   | [7.8, 76.1]     |  |
|  +0.00 |  +0.00 | 00:16:01.381 | Belgium            | Belgium            | 116 | Dispossessed    |   -   | [113.0, 4.7]    |  |
|  +0.00 |  +0.00 | 00:16:01.381 | Romania            | Romania            | 117 | Duel            |  Yes  | [7.1, 75.4]     | Tackle, Success In Play |
|  +0.47 |  +0.47 | 00:16:01.847 | Belgium            | Romania            | 117 | Offside         |   -   | [115.3, 5.9]    |  |
| +30.21 | +30.21 | 00:16:31.586 | Romania            | Romania            | 118 | Pass            |   -   | [12.3, 66.9]    | Incomplete (Incomplete) |
| +33.40 | +33.40 | 00:16:34.777 | Romania            | Romania            | 118 | Ball Receipt*   |   -   | [77.5, 69.0]    | Incomplete |
| +33.40 | +33.40 | 00:16:34.777 | Belgium            | Romania            | 118 | Pass            |   -   | [43.7, 12.1]    | Incomplete (Incomplete) |
| +33.40 | +33.40 | 00:16:34.777 | Romania            | Romania            | 118 | Duel            |   -   | [76.4, 68.0]    | Aerial Lost |
| +35.51 | +35.51 | 00:16:36.895 | Belgium            | Romania            | 118 | Ball Receipt*   |   -   | [50.9, 4.9]     | Incomplete |
| +35.51 | +35.51 | 00:16:36.895 | Romania            | Romania            | 118 | Pass            |   -   | [69.2, 76.9]    | -> Răzvan Gabriel |
| +36.63 | +36.63 | 00:16:38.016 | Romania            | Romania            | 118 | Ball Receipt*   |   -   | [69.4, 65.0]    |  |
| +36.63 | +36.63 | 00:16:38.016 | Romania            | Romania            | 118 | Carry           |   -   | [69.4, 65.0]    |  |
| +37.36 | +37.36 | 00:16:38.738 | Romania            | Romania            | 118 | Pass            |   -   | [70.0, 65.0]    | -> Nicolae Claudi |
| +38.23 | +38.23 | 00:16:39.607 | Romania            | Romania            | 118 | Ball Receipt*   |   -   | [69.6, 53.4]    |  |

---

### Disagreement Case 16: `3930165_p46_96dbd444`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3930165 (UEFA Euro, 2024)
- **counterpressing_team**: France
- **opponent_team_at_turnover**: Austria
- **possession_team_at_counterpress_initiation**: France
- **possession_id_at_counterpress_initiation**: 46
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:24:06.572) | **Initiation**: Duel (00:24:06.572)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.302s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.751s) | Evidence: `interception_plus_control` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.25 |  -3.25 | 00:24:03.323 | France             | Austria            | 45 | Dribbled Past   |   -   | [14.0, 66.5]    |  |
|  -3.25 |  -3.25 | 00:24:03.323 | Austria            | Austria            | 45 | Dribble         |   -   | [106.1, 13.6]   |  |
|  -3.25 |  -3.25 | 00:24:03.323 | Austria            | Austria            | 45 | Carry           |   -   | [106.1, 13.6]   |  |
|  -0.81 |  -0.81 | 00:24:05.766 | France             | Austria            | 45 | Pressure        |   -   | [10.7, 50.5]    |  |
|  +0.00 |  +0.00 | 00:24:06.572 | Austria            | Austria            | 45 | Dispossessed    |   -   | [107.7, 30.7]   |  |
|  +0.00 |  +0.00 | 00:24:06.572 | France             | France             | 46 | Duel            |  Yes  | [12.4, 49.4]    | Tackle, Success In Play |
|  +1.30 |  +1.30 | 00:24:07.874 | Austria            | France             | 46 | Pressure        |  Yes  | [104.4, 37.4]   |  |
|  +1.50 |  +1.50 | 00:24:08.068 | France             | France             | 46 | Clearance       |   -   | [12.7, 43.1]    |  |
|  +4.07 |  +4.07 | 00:24:10.644 | Austria            | France             | 46 | Pass            |   -   | [61.2, 43.7]    | Incomplete (Incomplete) |
|  +5.75 |  +5.75 | 00:24:12.323 | Austria            | France             | 46 | Ball Receipt*   |   -   | [81.1, 45.8]    | Incomplete |
|  +5.75 |  +5.75 | 00:24:12.323 | France             | France             | 46 | Interception    |   -   | [41.3, 34.7]    | Won |
|  +5.75 |  +5.75 | 00:24:12.323 | France             | France             | 46 | Carry           |   -   | [41.3, 34.7]    |  |
|  +6.77 |  +6.77 | 00:24:13.341 | Austria            | France             | 46 | Pressure        |   -   | [78.0, 40.5]    |  |
|  +6.96 |  +6.96 | 00:24:13.529 | France             | France             | 46 | Pass            |   -   | [41.9, 41.3]    | -> N'Golo Kanté |
|  +7.61 |  +7.61 | 00:24:14.185 | France             | France             | 46 | Ball Receipt*   |   -   | [34.5, 38.6]    |  |
|  +7.61 |  +7.61 | 00:24:14.185 | France             | France             | 46 | Pass            |   -   | [35.7, 37.8]    | -> Antoine Griezm |
|  +9.41 |  +9.41 | 00:24:15.977 | France             | France             | 46 | Ball Receipt*   |   -   | [49.3, 27.4]    |  |
|  +9.41 |  +9.41 | 00:24:15.977 | France             | France             | 46 | Carry           |   -   | [49.3, 27.4]    |  |

---

### Disagreement Case 17: `3794692_p75_5905ca75`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3794692 (UEFA Euro, 2020)
- **counterpressing_team**: Ukraine
- **opponent_team_at_turnover**: Sweden
- **possession_team_at_counterpress_initiation**: Ukraine
- **possession_id_at_counterpress_initiation**: 75
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:02:53.230) | **Initiation**: Duel (00:02:53.230)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.632s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.527s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.59 |  -0.59 | 00:02:52.638 | Ukraine            | Sweden             | 74 | Dribbled Past   |   -   | [8.6, 58.8]     |  |
|  -0.59 |  -0.59 | 00:02:52.638 | Sweden             | Sweden             | 74 | Dribble         |   -   | [111.5, 21.3]   |  |
|  -0.59 |  -0.59 | 00:02:52.638 | Sweden             | Sweden             | 74 | Carry           |   -   | [111.5, 21.3]   |  |
|  -0.15 |  -0.15 | 00:02:53.080 | Ukraine            | Sweden             | 74 | Pressure        |   -   | [9.6, 57.2]     |  |
|  +0.00 |  +0.00 | 00:02:53.230 | Sweden             | Sweden             | 74 | Dribble         |   -   | [110.5, 22.9]   |  |
|  +0.00 |  +0.00 | 00:02:53.230 | Ukraine            | Ukraine            | 75 | Duel            |  Yes  | [9.6, 57.2]     | Tackle, Success In Play |
|  +1.63 |  +1.63 | 00:02:54.862 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [9.4, 60.2]     | Incomplete (Incomplete) |
|  +3.84 |  +3.84 | 00:02:57.068 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [46.2, 57.4]    | Incomplete |
|  +3.84 |  +3.84 | 00:02:57.068 | Sweden             | Ukraine            | 75 | Interception    |  Yes  | [74.7, 23.3]    | Lost In Play |
|  +4.16 |  +4.16 | 00:02:57.385 | Ukraine            | Ukraine            | 75 | Block           |   -   | [46.0, 57.2]    |  |
|  +5.04 |  +5.04 | 00:02:58.272 | Sweden             | Ukraine            | 75 | Pressure        |   -   | [78.6, 21.7]    |  |
|  +5.17 |  +5.17 | 00:02:58.404 | Sweden             | Ukraine            | 75 | Pressure        |   -   | [79.7, 22.0]    |  |
|  +5.53 |  +5.53 | 00:02:58.757 | Ukraine            | Ukraine            | 75 | Ball Recovery   |   -   | [40.8, 57.8]    |  |
|  +5.53 |  +5.53 | 00:02:58.757 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [40.8, 57.8]    |  |
|  +6.22 |  +6.22 | 00:02:59.454 | Ukraine            | Ukraine            | 75 | Dispossessed    |   -   | [39.0, 56.8]    |  |
|  +6.22 |  +6.22 | 00:02:59.454 | Sweden             | Ukraine            | 75 | Duel            |   -   | [81.1, 23.3]    | Tackle, Lost In Play |
|  +7.57 |  +7.57 | 00:03:00.797 | Ukraine            | Ukraine            | 75 | Pass            |   -   | [37.3, 51.9]    | -> Oleksandr Zinc |
| +10.06 | +10.06 | 00:03:03.290 | Ukraine            | Ukraine            | 75 | Ball Receipt*   |   -   | [46.2, 10.0]    |  |
| +10.06 | +10.06 | 00:03:03.290 | Ukraine            | Ukraine            | 75 | Carry           |   -   | [46.2, 10.0]    |  |

---

### Disagreement Case 18: `3795220_p198_3c293375`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3795220 (UEFA Euro, 2020)
- **counterpressing_team**: Italy
- **opponent_team_at_turnover**: Spain
- **possession_team_at_counterpress_initiation**: Italy
- **possession_id_at_counterpress_initiation**: 198
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:14:50.700) | **Initiation**: Duel (00:14:50.700)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.591s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.13 |  -1.13 | 00:14:49.568 | Italy              | Spain              | 197 | Error           |   -   | [9.9, 30.8]     |  |
|  -0.82 |  -0.82 | 00:14:49.880 | Spain              | Spain              | 197 | Interception    |   -   | [111.3, 50.6]   | Won |
|  -0.82 |  -0.82 | 00:14:49.880 | Spain              | Spain              | 197 | Carry           |   -   | [111.3, 50.6]   |  |
|  -0.31 |  -0.31 | 00:14:50.388 | Italy              | Spain              | 197 | Pressure        |   -   | [5.8, 28.6]     |  |
|  +0.00 |  +0.00 | 00:14:50.700 | Spain              | Spain              | 197 | Dribble         |   -   | [114.3, 51.5]   |  |
|  +0.00 |  +0.00 | 00:14:50.700 | Italy              | Italy              | 198 | Duel            |  Yes  | [5.8, 28.6]     | Tackle, Success In Play |
|  +1.59 |  +1.59 | 00:14:52.291 | Italy              | Italy              | 198 | Clearance       |   -   | [7.7, 35.0]     |  |
| +15.26 | +15.26 | 00:15:05.961 | Spain              | Spain              | 199 | Pass            |   -   | [52.3, 80.0]    | Incomplete (Unknown) |
| +17.63 | +17.63 | 00:15:08.335 | Spain              | Spain              | 199 | Half End        |   -   | -               |  |
| +17.63 | +17.63 | 00:15:08.335 | Italy              | Spain              | 199 | Half End        |   -   | -               |  |
| -890.70 | -890.70 | 00:00:00.000 | Spain              | Spain              | 199 | Half Start      |   -   | -               |  |
| -890.70 | -890.70 | 00:00:00.000 | Italy              | Spain              | 199 | Half Start      |   -   | -               |  |
| -890.70 | -890.70 | 00:00:00.000 | Spain              | Spain              | 199 | Substitution    |   -   | -               |  |
| -889.92 | -889.92 | 00:00:00.783 | Italy              | Italy              | 200 | Pass            |   -   | [60.0, 40.0]    | -> Jorge Luiz Fre |
| -888.98 | -888.98 | 00:00:01.721 | Italy              | Italy              | 200 | Ball Receipt*   |   -   | [47.1, 37.2]    |  |
| -888.98 | -888.98 | 00:00:01.721 | Italy              | Italy              | 200 | Carry           |   -   | [47.1, 37.2]    |  |
| -888.13 | -888.13 | 00:00:02.569 | Italy              | Italy              | 200 | Pass            |   -   | [48.4, 38.4]    | -> Leonardo Bonuc |
| -887.15 | -887.15 | 00:00:03.552 | Italy              | Italy              | 200 | Ball Receipt*   |   -   | [36.9, 41.2]    |  |
| -887.15 | -887.15 | 00:00:03.552 | Italy              | Italy              | 200 | Carry           |   -   | [36.9, 41.2]    |  |
| -885.86 | -885.86 | 00:00:04.845 | Spain              | Italy              | 200 | Pressure        |   -   | [82.8, 47.2]    |  |
| -884.72 | -884.72 | 00:00:05.976 | Italy              | Italy              | 200 | Pass            |   -   | [34.3, 31.2]    | -> Giorgio Chiell |
| -883.50 | -883.50 | 00:00:07.204 | Italy              | Italy              | 200 | Ball Receipt*   |   -   | [28.3, 14.1]    |  |
| -883.50 | -883.50 | 00:00:07.204 | Italy              | Italy              | 200 | Carry           |   -   | [28.3, 14.1]    |  |
| -883.42 | -883.42 | 00:00:07.284 | Italy              | Italy              | 200 | Pass            |   -   | [28.1, 14.5]    | -> Gianluigi Donn |
| -881.62 | -881.62 | 00:00:09.075 | Italy              | Italy              | 200 | Ball Receipt*   |   -   | [12.7, 33.5]    |  |
| -881.62 | -881.62 | 00:00:09.075 | Italy              | Italy              | 200 | Carry           |   -   | [12.7, 33.5]    |  |
| -880.89 | -880.89 | 00:00:09.814 | Spain              | Italy              | 200 | Pressure        |   -   | [104.2, 52.1]   |  |
| -879.40 | -879.40 | 00:00:11.298 | Italy              | Italy              | 200 | Pass            |   -   | [10.3, 40.4]    | Incomplete (Out) |
| -857.43 | -857.43 | 00:00:33.267 | Spain              | Spain              | 201 | Pass            |   -   | [73.6, 0.1]     | -> Álvaro Borja M |
| -856.66 | -856.66 | 00:00:34.036 | Italy              | Spain              | 201 | Pressure        |   -   | [36.9, 74.4]    |  |
| -856.33 | -856.33 | 00:00:34.368 | Spain              | Spain              | 201 | Ball Receipt*   |   -   | [82.2, 5.7]     |  |
| -856.33 | -856.33 | 00:00:34.368 | Spain              | Spain              | 201 | Carry           |   -   | [82.2, 5.7]     |  |
| -854.79 | -854.79 | 00:00:35.911 | Italy              | Spain              | 201 | Pressure        |   -   | [40.1, 73.9]    |  |
| -854.49 | -854.49 | 00:00:36.213 | Spain              | Spain              | 201 | Pass            |   -   | [81.5, 4.4]     | -> Jordi Alba Ram |
| -854.37 | -854.37 | 00:00:36.329 | Spain              | Spain              | 201 | Ball Receipt*   |   -   | [72.3, 4.2]     |  |
| -854.37 | -854.37 | 00:00:36.329 | Spain              | Spain              | 201 | Carry           |   -   | [72.3, 4.2]     |  |
| -854.37 | -854.37 | 00:00:36.329 | Italy              | Spain              | 201 | Block           |   -   | [43.1, 76.1]    |  |
| -852.66 | -852.66 | 00:00:38.038 | Spain              | Spain              | 201 | Pass            |   -   | [73.4, 5.5]     | Incomplete (Incomplete) |
| -850.86 | -850.86 | 00:00:39.838 | Spain              | Spain              | 201 | Ball Receipt*   |   -   | [89.7, 5.9]     | Incomplete |
| -850.86 | -850.86 | 00:00:39.838 | Italy              | Spain              | 201 | Clearance       |   -   | [29.8, 72.7]    |  |
| -849.78 | -849.78 | 00:00:40.924 | Spain              | Spain              | 201 | Pass            |   -   | [71.3, 7.2]     | Incomplete (Incomplete) |
| -848.40 | -848.40 | 00:00:42.299 | Spain              | Spain              | 201 | Ball Receipt*   |   -   | [89.0, 13.9]    | Incomplete |
| -848.40 | -848.40 | 00:00:42.299 | Italy              | Spain              | 201 | Clearance       |   -   | [29.8, 63.2]    |  |
| -845.60 | -845.60 | 00:00:45.096 | Italy              | Spain              | 201 | Duel            |   -   | [57.4, 56.6]    | Aerial Lost |
| -845.60 | -845.60 | 00:00:45.096 | Spain              | Spain              | 201 | Pass            |   -   | [62.7, 23.5]    | -> Daniel Olmo Ca |
| -844.75 | -844.75 | 00:00:45.954 | Italy              | Spain              | 201 | Pressure        |   -   | [50.3, 52.3]    |  |
| -844.29 | -844.29 | 00:00:46.415 | Spain              | Spain              | 201 | Ball Receipt*   |   -   | [70.0, 27.3]    |  |
| -844.29 | -844.29 | 00:00:46.415 | Spain              | Spain              | 201 | Carry           |   -   | [70.0, 27.3]    |  |
| -843.75 | -843.75 | 00:00:46.953 | Italy              | Spain              | 201 | Dribbled Past   |   -   | [50.8, 51.3]    |  |
| -843.75 | -843.75 | 00:00:46.953 | Spain              | Spain              | 201 | Dribble         |   -   | [69.3, 28.8]    |  |
| -843.75 | -843.75 | 00:00:46.953 | Spain              | Spain              | 201 | Carry           |   -   | [69.3, 28.8]    |  |
| -840.76 | -840.76 | 00:00:49.942 | Italy              | Spain              | 201 | Pressure        |   -   | [36.4, 55.8]    |  |
| -840.20 | -840.20 | 00:00:50.505 | Italy              | Spain              | 201 | Foul Committed  |   -   | [35.1, 58.5]    |  |
| -840.20 | -840.20 | 00:00:50.505 | Spain              | Spain              | 201 | Foul Won        |   -   | [85.0, 21.6]    |  |
| -795.91 | -795.91 | 00:01:34.790 | Italy              | Spain              | 201 | Substitution    |   -   | -               |  |
| -772.82 | -772.82 | 00:01:57.882 | Spain              | Spain              | 202 | Shot            |   -   | [86.3, 18.3]    | Blocked |
| -772.53 | -772.53 | 00:01:58.168 | Italy              | Spain              | 202 | Block           |   -   | [26.5, 56.9]    |  |
| -772.49 | -772.49 | 00:01:58.208 | Italy              | Spain              | 202 | Goal Keeper     |   -   | [6.1, 40.7]     |  |
| -770.58 | -770.58 | 00:02:00.122 | Italy              | Italy              | 203 | Ball Recovery   |   -   | [3.3, 42.1]     |  |
| -770.58 | -770.58 | 00:02:00.122 | Italy              | Italy              | 203 | Carry           |   -   | [3.3, 42.1]     |  |
| -755.83 | -755.83 | 00:02:14.871 | Italy              | Italy              | 203 | Pass            |   -   | [5.2, 40.4]     | -> Giorgio Chiell |
| -754.50 | -754.50 | 00:02:16.201 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [8.6, 27.1]     |  |
| -754.50 | -754.50 | 00:02:16.201 | Italy              | Italy              | 203 | Carry           |   -   | [8.6, 27.1]     |  |
| -753.93 | -753.93 | 00:02:16.775 | Italy              | Italy              | 203 | Pass            |   -   | [9.7, 24.5]     | -> Giovanni Di Lo |
| -752.63 | -752.63 | 00:02:18.072 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [24.0, 0.4]     |  |
| -752.63 | -752.63 | 00:02:18.072 | Italy              | Italy              | 203 | Carry           |   -   | [24.0, 0.4]     |  |
| -751.62 | -751.62 | 00:02:19.081 | Italy              | Italy              | 203 | Pass            |   -   | [27.7, 2.5]     | -> Andrea Belotti |
| -750.22 | -750.22 | 00:02:20.484 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [54.4, 11.9]    |  |
| -750.22 | -750.22 | 00:02:20.484 | Italy              | Italy              | 203 | Carry           |   -   | [54.4, 11.9]    |  |
| -750.17 | -750.17 | 00:02:20.531 | Spain              | Italy              | 203 | Pressure        |   -   | [62.9, 66.5]    |  |
| -748.60 | -748.60 | 00:02:22.096 | Italy              | Italy              | 203 | Pass            |   -   | [52.9, 15.8]    | -> Domenico Berar |
| -746.16 | -746.16 | 00:02:24.538 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [69.8, 70.5]    |  |
| -746.16 | -746.16 | 00:02:24.538 | Italy              | Italy              | 203 | Carry           |   -   | [69.8, 70.5]    |  |
| -742.78 | -742.78 | 00:02:27.920 | Italy              | Italy              | 203 | Pass            |   -   | [90.5, 57.7]    | -> Federico Berna |
| -742.29 | -742.29 | 00:02:28.412 | Spain              | Italy              | 203 | Pressure        |   -   | [23.1, 32.9]    |  |
| -741.94 | -741.94 | 00:02:28.758 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [95.7, 48.7]    |  |
| -741.94 | -741.94 | 00:02:28.758 | Italy              | Italy              | 203 | Carry           |   -   | [95.7, 48.7]    |  |
| -741.90 | -741.90 | 00:02:28.798 | Italy              | Italy              | 203 | Pass            |   -   | [98.5, 48.7]    | Incomplete (Incomplete) |
| -740.71 | -740.71 | 00:02:29.988 | Italy              | Italy              | 203 | Ball Receipt*   |   -   | [97.2, 27.5]    | Incomplete |
| -740.71 | -740.71 | 00:02:29.988 | Spain              | Italy              | 203 | Pass            |   -   | [23.4, 48.5]    | -> Unai Simón Men |
| -739.55 | -739.55 | 00:02:31.152 | Spain              | Italy              | 203 | Ball Receipt*   |   -   | [4.1, 50.0]     |  |
| -739.55 | -739.55 | 00:02:31.152 | Spain              | Italy              | 203 | Pass            |   -   | [6.0, 47.9]     | Incomplete (Out) |
| -734.27 | -734.27 | 00:02:36.430 | Spain              | Italy              | 203 | Ball Receipt*   |   -   | [76.6, 8.3]     | Incomplete |
| -727.07 | -727.07 | 00:02:43.632 | Italy              | Italy              | 203 | Injury Stoppage |   -   | -               |  |
| -668.25 | -668.25 | 00:03:42.451 | Spain              | Italy              | 203 | Substitution    |   -   | -               |  |
| -667.66 | -667.66 | 00:03:43.038 | Spain              | Italy              | 203 | Tactical Shift  |   -   | -               |  |
| -651.73 | -651.73 | 00:03:58.966 | Italy              | Italy              | 204 | Pass            |   -   | [54.8, 80.0]    | -> Jorge Luiz Fre |
| -651.00 | -651.00 | 00:03:59.698 | Italy              | Italy              | 204 | Ball Receipt*   |   -   | [50.1, 71.8]    |  |
| -651.00 | -651.00 | 00:03:59.698 | Italy              | Italy              | 204 | Carry           |   -   | [50.1, 71.8]    |  |
| -650.92 | -650.92 | 00:03:59.778 | Italy              | Italy              | 204 | Pass            |   -   | [49.3, 71.2]    | Incomplete (Incomplete) |
| -647.83 | -647.83 | 00:04:02.868 | Italy              | Italy              | 204 | Ball Receipt*   |   -   | [96.5, 75.2]    | Incomplete |
| -647.83 | -647.83 | 00:04:02.868 | Spain              | Italy              | 204 | Interception    |   -   | [23.8, 8.3]     | Lost Out |
| -628.90 | -628.90 | 00:04:21.798 | Italy              | Italy              | 205 | Pass            |   -   | [99.1, 80.0]    | -> Matteo Pessina |
| -628.02 | -628.02 | 00:04:22.680 | Spain              | Italy              | 205 | Pressure        |   -   | [6.0, 12.1]     |  |
| -627.75 | -627.75 | 00:04:22.947 | Italy              | Italy              | 205 | Ball Receipt*   |   -   | [115.6, 66.5]   |  |
| -627.75 | -627.75 | 00:04:22.947 | Italy              | Italy              | 205 | Carry           |   -   | [115.6, 66.5]   |  |
| -627.71 | -627.71 | 00:04:22.987 | Italy              | Italy              | 205 | Pass            |   -   | [115.8, 70.7]   | -> Domenico Berar |
| -626.34 | -626.34 | 00:04:24.365 | Spain              | Italy              | 205 | Pressure        |   -   | [12.0, 20.5]    |  |
| -626.14 | -626.14 | 00:04:24.555 | Italy              | Italy              | 205 | Ball Receipt*   |   -   | [105.5, 64.1]   |  |
| -626.14 | -626.14 | 00:04:24.555 | Italy              | Italy              | 205 | Carry           |   -   | [105.5, 64.1]   |  |
| -624.59 | -624.59 | 00:04:26.106 | Spain              | Italy              | 205 | Dribbled Past   |   -   | [14.4, 24.1]    |  |
| -624.59 | -624.59 | 00:04:26.106 | Italy              | Italy              | 205 | Dribble         |   -   | [105.7, 56.0]   |  |
| -624.59 | -624.59 | 00:04:26.106 | Italy              | Italy              | 205 | Carry           |   -   | [105.7, 56.0]   |  |
| -623.76 | -623.76 | 00:04:26.945 | Italy              | Italy              | 205 | Shot            |   -   | [105.0, 48.2]   | Blocked |
| -623.52 | -623.52 | 00:04:27.177 | Spain              | Italy              | 205 | Block           |   -   | [9.3, 37.4]     |  |
| -623.17 | -623.17 | 00:04:27.528 | Spain              | Italy              | 205 | Goal Keeper     |   -   | [3.0, 38.4]     |  |
| -619.23 | -619.23 | 00:04:31.471 | Italy              | Italy              | 205 | Pass            |   -   | [84.3, 5.7]     | -> Giorgio Chiell |
| -618.01 | -618.01 | 00:04:32.690 | Italy              | Italy              | 205 | Ball Receipt*   |   -   | [67.0, 13.8]    |  |
| -618.01 | -618.01 | 00:04:32.690 | Italy              | Italy              | 205 | Carry           |   -   | [67.0, 13.8]    |  |
| -616.05 | -616.05 | 00:04:34.655 | Italy              | Italy              | 205 | Pass            |   -   | [67.4, 14.3]    | Incomplete (Pass Offside) |
| -612.51 | -612.51 | 00:04:38.191 | Italy              | Italy              | 205 | Ball Receipt*   |   -   | [100.2, 22.6]   | Incomplete |
| -585.96 | -585.96 | 00:05:04.741 | Spain              | Spain              | 206 | Pass            |   -   | [7.7, 44.7]     | -> Pau Francisco  |
| -584.11 | -584.11 | 00:05:06.593 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [34.5, 28.6]    |  |
| -579.06 | -579.06 | 00:05:11.639 | Spain              | Spain              | 206 | Pass            |   -   | [35.1, 29.5]    | -> Unai Simón Men |
| -576.42 | -576.42 | 00:05:14.284 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [13.7, 41.9]    |  |
| -576.42 | -576.42 | 00:05:14.284 | Spain              | Spain              | 206 | Carry           |   -   | [13.7, 41.9]    |  |
| -576.38 | -576.38 | 00:05:14.324 | Spain              | Spain              | 206 | Pass            |   -   | [13.5, 42.7]    | -> Aymeric Laport |
| -574.93 | -574.93 | 00:05:15.772 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [26.6, 58.3]    |  |
| -574.93 | -574.93 | 00:05:15.772 | Spain              | Spain              | 206 | Carry           |   -   | [26.6, 58.3]    |  |
| -572.61 | -572.61 | 00:05:18.090 | Spain              | Spain              | 206 | Pass            |   -   | [32.1, 60.3]    | -> Pau Francisco  |
| -571.00 | -571.00 | 00:05:19.703 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [27.6, 41.2]    |  |
| -571.00 | -571.00 | 00:05:19.703 | Spain              | Spain              | 206 | Carry           |   -   | [27.6, 41.2]    |  |
| -565.88 | -565.88 | 00:05:24.815 | Spain              | Spain              | 206 | Pass            |   -   | [49.5, 26.7]    | -> Rodrigo Hernán |
| -565.21 | -565.21 | 00:05:25.493 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [56.1, 41.5]    |  |
| -565.21 | -565.21 | 00:05:25.493 | Spain              | Spain              | 206 | Carry           |   -   | [56.1, 41.5]    |  |
| -564.16 | -564.16 | 00:05:26.537 | Spain              | Spain              | 206 | Pass            |   -   | [56.3, 43.8]    | -> Aymeric Laport |
| -562.61 | -562.61 | 00:05:28.087 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [44.1, 56.6]    |  |
| -562.61 | -562.61 | 00:05:28.087 | Spain              | Spain              | 206 | Carry           |   -   | [44.1, 56.6]    |  |
| -561.56 | -561.56 | 00:05:29.139 | Spain              | Spain              | 206 | Pass            |   -   | [51.4, 62.0]    | -> Gerard Moreno  |
| -560.10 | -560.10 | 00:05:30.600 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [68.7, 77.8]    |  |
| -560.10 | -560.10 | 00:05:30.600 | Spain              | Spain              | 206 | Carry           |   -   | [68.7, 77.8]    |  |
| -559.01 | -559.01 | 00:05:31.692 | Spain              | Spain              | 206 | Pass            |   -   | [69.1, 76.3]    | -> Thiago Alcânta |
| -557.61 | -557.61 | 00:05:33.093 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [56.5, 74.0]    |  |
| -557.61 | -557.61 | 00:05:33.093 | Spain              | Spain              | 206 | Carry           |   -   | [56.5, 74.0]    |  |
| -556.79 | -556.79 | 00:05:33.914 | Spain              | Spain              | 206 | Pass            |   -   | [56.3, 73.3]    | -> Aymeric Laport |
| -555.81 | -555.81 | 00:05:34.891 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [42.8, 66.5]    |  |
| -555.81 | -555.81 | 00:05:34.891 | Spain              | Spain              | 206 | Carry           |   -   | [42.8, 66.5]    |  |
| -552.01 | -552.01 | 00:05:38.692 | Spain              | Spain              | 206 | Pass            |   -   | [49.5, 58.3]    | -> Rodrigo Hernán |
| -551.26 | -551.26 | 00:05:39.443 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [55.0, 47.2]    |  |
| -551.26 | -551.26 | 00:05:39.443 | Spain              | Spain              | 206 | Carry           |   -   | [55.0, 47.2]    |  |
| -550.21 | -550.21 | 00:05:40.492 | Spain              | Spain              | 206 | Pass            |   -   | [55.9, 45.7]    | -> Pau Francisco  |
| -549.00 | -549.00 | 00:05:41.703 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [41.8, 31.4]    |  |
| -549.00 | -549.00 | 00:05:41.703 | Spain              | Spain              | 206 | Carry           |   -   | [41.8, 31.4]    |  |
| -547.84 | -547.84 | 00:05:42.864 | Spain              | Spain              | 206 | Pass            |   -   | [43.5, 28.6]    | -> Jordi Alba Ram |
| -546.25 | -546.25 | 00:05:44.454 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [64.2, 13.9]    |  |
| -546.25 | -546.25 | 00:05:44.454 | Spain              | Spain              | 206 | Carry           |   -   | [64.2, 13.9]    |  |
| -545.49 | -545.49 | 00:05:45.210 | Spain              | Spain              | 206 | Pass            |   -   | [71.1, 9.4]     | -> Pedro González |
| -544.34 | -544.34 | 00:05:46.359 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [70.6, 18.3]    |  |
| -544.34 | -544.34 | 00:05:46.359 | Spain              | Spain              | 206 | Carry           |   -   | [70.6, 18.3]    |  |
| -544.26 | -544.26 | 00:05:46.439 | Spain              | Spain              | 206 | Pass            |   -   | [70.0, 18.3]    | -> Pau Francisco  |
| -542.58 | -542.58 | 00:05:48.117 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [52.9, 23.7]    |  |
| -542.58 | -542.58 | 00:05:48.117 | Spain              | Spain              | 206 | Carry           |   -   | [52.9, 23.7]    |  |
| -537.49 | -537.49 | 00:05:53.212 | Spain              | Spain              | 206 | Pass            |   -   | [64.9, 24.6]    | -> Álvaro Borja M |
| -536.68 | -536.68 | 00:05:54.023 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [76.0, 20.7]    |  |
| -536.68 | -536.68 | 00:05:54.023 | Spain              | Spain              | 206 | Carry           |   -   | [76.0, 20.7]    |  |
| -536.14 | -536.14 | 00:05:54.564 | Spain              | Spain              | 206 | Miscontrol      |   -   | [77.7, 19.4]    |  |
| -536.05 | -536.05 | 00:05:54.652 | Spain              | Spain              | 206 | Pressure        |   -   | [74.7, 16.4]    |  |
| -535.77 | -535.77 | 00:05:54.930 | Italy              | Spain              | 206 | Clearance       |   -   | [46.5, 64.1]    |  |
| -535.69 | -535.69 | 00:05:55.007 | Spain              | Spain              | 206 | Block           |   -   | [75.3, 18.3]    |  |
| -534.23 | -534.23 | 00:05:56.468 | Spain              | Spain              | 206 | Ball Recovery   |   -   | [56.3, 23.3]    |  |
| -534.23 | -534.23 | 00:05:56.468 | Spain              | Spain              | 206 | Carry           |   -   | [56.3, 23.3]    |  |
| -533.19 | -533.19 | 00:05:57.509 | Spain              | Spain              | 206 | Pass            |   -   | [58.2, 26.3]    | -> Thiago Alcânta |
| -531.06 | -531.06 | 00:05:59.637 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [53.9, 61.3]    |  |
| -531.06 | -531.06 | 00:05:59.637 | Spain              | Spain              | 206 | Carry           |   -   | [53.9, 61.3]    |  |
| -529.80 | -529.80 | 00:06:00.904 | Spain              | Spain              | 206 | Pass            |   -   | [50.3, 59.8]    | -> Rodrigo Hernán |
| -528.43 | -528.43 | 00:06:02.269 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [66.4, 55.6]    |  |
| -528.43 | -528.43 | 00:06:02.269 | Spain              | Spain              | 206 | Pass            |   -   | [65.3, 56.2]    | -> Marcos Llorent |
| -527.10 | -527.10 | 00:06:03.601 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [70.8, 77.4]    |  |
| -527.10 | -527.10 | 00:06:03.601 | Spain              | Spain              | 206 | Carry           |   -   | [70.8, 77.4]    |  |
| -524.41 | -524.41 | 00:06:06.291 | Spain              | Spain              | 206 | Pass            |   -   | [77.7, 77.6]    | -> Rodrigo Hernán |
| -523.38 | -523.38 | 00:06:07.323 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [73.0, 66.5]    |  |
| -523.38 | -523.38 | 00:06:07.323 | Spain              | Spain              | 206 | Carry           |   -   | [73.0, 66.5]    |  |
| -523.34 | -523.34 | 00:06:07.363 | Spain              | Spain              | 206 | Pass            |   -   | [73.0, 68.2]    | -> Thiago Alcânta |
| -522.34 | -522.34 | 00:06:08.362 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [65.1, 74.2]    |  |
| -522.34 | -522.34 | 00:06:08.362 | Spain              | Spain              | 206 | Carry           |   -   | [65.1, 74.2]    |  |
| -521.34 | -521.34 | 00:06:09.364 | Spain              | Spain              | 206 | Pass            |   -   | [64.4, 73.3]    | -> Pau Francisco  |
| -519.62 | -519.62 | 00:06:11.077 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [53.7, 38.0]    |  |
| -519.62 | -519.62 | 00:06:11.077 | Spain              | Spain              | 206 | Carry           |   -   | [53.7, 38.0]    |  |
| -518.72 | -518.72 | 00:06:11.983 | Spain              | Spain              | 206 | Pass            |   -   | [57.6, 32.9]    | -> Jordi Alba Ram |
| -517.55 | -517.55 | 00:06:13.151 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [69.3, 17.1]    |  |
| -517.55 | -517.55 | 00:06:13.151 | Spain              | Spain              | 206 | Carry           |   -   | [69.3, 17.1]    |  |
| -513.81 | -513.81 | 00:06:16.889 | Spain              | Spain              | 206 | Pass            |   -   | [70.2, 20.5]    | -> Rodrigo Hernán |
| -513.00 | -513.00 | 00:06:17.701 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [75.1, 29.9]    |  |
| -513.00 | -513.00 | 00:06:17.701 | Spain              | Spain              | 206 | Carry           |   -   | [75.1, 29.9]    |  |
| -512.92 | -512.92 | 00:06:17.781 | Spain              | Spain              | 206 | Pass            |   -   | [75.1, 29.9]    | -> Pau Francisco  |
| -511.70 | -511.70 | 00:06:19.000 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [57.8, 25.0]    |  |
| -511.70 | -511.70 | 00:06:19.000 | Spain              | Spain              | 206 | Carry           |   -   | [57.8, 25.0]    |  |
| -509.40 | -509.40 | 00:06:21.303 | Spain              | Spain              | 206 | Pass            |   -   | [68.1, 28.8]    | -> Daniel Olmo Ca |
| -508.58 | -508.58 | 00:06:22.125 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [81.5, 40.0]    |  |
| -508.58 | -508.58 | 00:06:22.125 | Spain              | Spain              | 206 | Pass            |   -   | [83.2, 39.1]    | Incomplete (Incomplete) |
| -508.48 | -508.48 | 00:06:22.221 | Spain              | Spain              | 206 | Ball Receipt*   |   -   | [84.1, 34.2]    | Incomplete |
| -508.48 | -508.48 | 00:06:22.221 | Italy              | Spain              | 206 | Pass            |   -   | [34.7, 42.1]    | -> Andrea Belotti |
| -507.16 | -507.16 | 00:06:23.544 | Italy              | Spain              | 206 | Ball Receipt*   |   -   | [48.6, 51.9]    |  |
| -507.16 | -507.16 | 00:06:23.544 | Italy              | Spain              | 206 | Carry           |   -   | [48.6, 51.9]    |  |
| -506.98 | -506.98 | 00:06:23.722 | Italy              | Spain              | 206 | Miscontrol      |   -   | [53.3, 59.0]    |  |
| -506.47 | -506.47 | 00:06:24.232 | Italy              | Spain              | 206 | Pressure        |   -   | [53.1, 58.1]    |  |
| -506.29 | -506.29 | 00:06:24.414 | Spain              | Spain              | 206 | Ball Recovery   |   -   | [66.8, 19.6]    |  |
| -506.29 | -506.29 | 00:06:24.414 | Spain              | Spain              | 206 | Carry           |   -   | [66.8, 19.6]    |  |
| -505.86 | -505.86 | 00:06:24.837 | Italy              | Spain              | 206 | Foul Committed  |   -   | [52.9, 60.5]    |  |
| -505.86 | -505.86 | 00:06:24.837 | Spain              | Spain              | 206 | Foul Won        |   -   | [67.2, 19.6]    |  |
| -477.93 | -477.93 | 00:06:52.775 | Spain              | Spain              | 207 | Pass            |   -   | [68.3, 21.6]    | -> Aymeric Laport |
| -475.13 | -475.13 | 00:06:55.569 | Spain              | Spain              | 207 | Ball Receipt*   |   -   | [70.4, 50.2]    |  |
| -470.92 | -470.92 | 00:06:59.776 | Spain              | Spain              | 207 | Pass            |   -   | [71.3, 54.5]    | -> Thiago Alcânta |
| -469.42 | -469.42 | 00:07:01.276 | Spain              | Spain              | 207 | Ball Receipt*   |   -   | [76.8, 75.2]    |  |
| -469.42 | -469.42 | 00:07:01.276 | Spain              | Spain              | 207 | Carry           |   -   | [76.8, 75.2]    |  |
| -465.63 | -465.63 | 00:07:05.071 | Italy              | Spain              | 207 | Pressure        |   -   | [37.3, 5.5]     |  |
| -464.76 | -464.76 | 00:07:05.943 | Spain              | Spain              | 207 | Pass            |   -   | [83.9, 76.1]    | -> Aymeric Laport |
| -463.30 | -463.30 | 00:07:07.400 | Spain              | Spain              | 207 | Ball Receipt*   |   -   | [66.1, 77.0]    |  |
| -463.30 | -463.30 | 00:07:07.400 | Spain              | Spain              | 207 | Carry           |   -   | [66.1, 77.0]    |  |
| -463.00 | -463.00 | 00:07:07.704 | Italy              | Spain              | 207 | Pressure        |   -   | [50.5, 5.3]     |  |
| -461.98 | -461.98 | 00:07:08.725 | Italy              | Spain              | 207 | Dribbled Past   |   -   | [44.6, 4.2]     |  |
| -461.98 | -461.98 | 00:07:08.725 | Spain              | Spain              | 207 | Dribble         |   -   | [75.5, 75.9]    |  |
| -461.98 | -461.98 | 00:07:08.725 | Spain              | Spain              | 207 | Carry           |   -   | [75.5, 75.9]    |  |
| -460.13 | -460.13 | 00:07:10.568 | Spain              | Spain              | 207 | Dribble         |   -   | [79.2, 76.1]    |  |
| -460.13 | -460.13 | 00:07:10.568 | Italy              | Spain              | 207 | Duel            |   -   | [40.9, 4.0]     | Tackle, Lost In Play |
| -459.06 | -459.06 | 00:07:11.639 | Spain              | Spain              | 207 | Pass            |   -   | [76.0, 77.6]    | Incomplete (Incomplete) |
| -458.16 | -458.16 | 00:07:12.537 | Spain              | Spain              | 207 | Pressure        |   -   | [76.4, 70.1]    |  |
| -457.88 | -457.88 | 00:07:12.823 | Spain              | Spain              | 207 | Ball Receipt*   |   -   | [77.9, 68.0]    | Incomplete |
| -457.88 | -457.88 | 00:07:12.823 | Italy              | Italy              | 208 | Ball Recovery   |   -   | [44.3, 9.1]     |  |
| -457.88 | -457.88 | 00:07:12.823 | Italy              | Italy              | 208 | Carry           |   -   | [44.3, 9.1]     |  |
| -457.46 | -457.46 | 00:07:13.239 | Italy              | Italy              | 208 | Pass            |   -   | [43.5, 10.0]    | -> Giorgio Chiell |
| -456.44 | -456.44 | 00:07:14.259 | Italy              | Italy              | 208 | Ball Receipt*   |   -   | [34.3, 5.7]     |  |
| -456.44 | -456.44 | 00:07:14.259 | Italy              | Italy              | 208 | Carry           |   -   | [34.3, 5.7]     |  |
| -456.38 | -456.38 | 00:07:14.316 | Spain              | Italy              | 208 | Pressure        |  Yes  | [82.0, 75.9]    |  |
| -455.50 | -455.50 | 00:07:15.196 | Italy              | Italy              | 208 | Pass            |   -   | [33.6, 1.4]     | -> Domenico Berar |
| -453.36 | -453.36 | 00:07:17.339 | Italy              | Italy              | 208 | Ball Receipt*   |   -   | [66.6, 32.4]    |  |
| -453.36 | -453.36 | 00:07:17.339 | Italy              | Italy              | 208 | Carry           |   -   | [66.6, 32.4]    |  |
| -453.11 | -453.11 | 00:07:17.588 | Spain              | Italy              | 208 | Pressure        |  Yes  | [51.4, 44.7]    |  |
| -451.94 | -451.94 | 00:07:18.757 | Italy              | Italy              | 208 | Dribble         |   -   | [70.9, 30.7]    |  |
| -451.94 | -451.94 | 00:07:18.757 | Spain              | Spain              | 209 | Duel            |  Yes  | [49.2, 49.4]    | Tackle, Won |
| -451.94 | -451.94 | 00:07:18.757 | Spain              | Spain              | 209 | Carry           |   -   | [49.2, 49.4]    |  |
| -451.07 | -451.07 | 00:07:19.628 | Spain              | Spain              | 209 | Pass            |   -   | [45.6, 49.4]    | -> Pau Francisco  |
| -449.79 | -449.79 | 00:07:20.915 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [29.3, 48.7]    |  |
| -449.79 | -449.79 | 00:07:20.915 | Spain              | Spain              | 209 | Carry           |   -   | [29.3, 48.7]    |  |
| -449.11 | -449.11 | 00:07:21.595 | Spain              | Spain              | 209 | Pass            |   -   | [29.1, 48.9]    | -> Unai Simón Men |
| -447.31 | -447.31 | 00:07:23.395 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [6.2, 47.4]     |  |
| -447.31 | -447.31 | 00:07:23.395 | Spain              | Spain              | 209 | Carry           |   -   | [6.2, 47.4]     |  |
| -445.27 | -445.27 | 00:07:25.428 | Spain              | Spain              | 209 | Pass            |   -   | [9.5, 46.4]     | -> Pau Francisco  |
| -442.89 | -442.89 | 00:07:27.806 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [13.3, 19.4]    |  |
| -442.89 | -442.89 | 00:07:27.806 | Spain              | Spain              | 209 | Carry           |   -   | [13.3, 19.4]    |  |
| -442.06 | -442.06 | 00:07:28.645 | Spain              | Spain              | 209 | Pass            |   -   | [23.6, 18.6]    | -> Pedro González |
| -440.29 | -440.29 | 00:07:30.408 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [45.0, 7.0]     |  |
| -440.29 | -440.29 | 00:07:30.408 | Spain              | Spain              | 209 | Carry           |   -   | [45.0, 7.0]     |  |
| -434.02 | -434.02 | 00:07:36.685 | Spain              | Spain              | 209 | Pass            |   -   | [66.6, 7.4]     | -> Pau Francisco  |
| -432.45 | -432.45 | 00:07:38.251 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [37.7, 20.9]    |  |
| -432.45 | -432.45 | 00:07:38.251 | Spain              | Spain              | 209 | Carry           |   -   | [37.7, 20.9]    |  |
| -430.11 | -430.11 | 00:07:40.593 | Spain              | Spain              | 209 | Pass            |   -   | [48.0, 28.2]    | -> Aymeric Laport |
| -427.76 | -427.76 | 00:07:42.941 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [43.2, 57.9]    |  |
| -427.76 | -427.76 | 00:07:42.941 | Spain              | Spain              | 209 | Carry           |   -   | [43.2, 57.9]    |  |
| -427.68 | -427.68 | 00:07:43.021 | Spain              | Spain              | 209 | Pass            |   -   | [43.7, 58.6]    | -> Thiago Alcânta |
| -426.53 | -426.53 | 00:07:44.174 | Spain              | Spain              | 209 | Ball Receipt*   |   -   | [52.9, 65.8]    |  |
| -426.53 | -426.53 | 00:07:44.174 | Spain              | Spain              | 209 | Carry           |   -   | [52.9, 65.8]    |  |
| -424.74 | -424.74 | 00:07:45.956 | Spain              | Spain              | 209 | Pass            |   -   | [57.8, 68.4]    | Incomplete (Incomplete) |
| -421.09 | -421.09 | 00:07:49.606 | Italy              | Italy              | 210 | Ball Recovery   |   -   | [5.2, 49.8]     |  |
| -421.09 | -421.09 | 00:07:49.606 | Italy              | Italy              | 210 | Carry           |   -   | [5.2, 49.8]     |  |
| -416.62 | -416.62 | 00:07:54.076 | Italy              | Italy              | 210 | Pass            |   -   | [6.5, 53.6]     | -> Rafael Tolói |
| -414.95 | -414.95 | 00:07:55.752 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [27.0, 69.2]    |  |
| -414.95 | -414.95 | 00:07:55.752 | Italy              | Italy              | 210 | Carry           |   -   | [27.0, 69.2]    |  |
| -413.22 | -413.22 | 00:07:57.483 | Italy              | Italy              | 210 | Pass            |   -   | [30.2, 71.8]    | -> Domenico Berar |
| -412.12 | -412.12 | 00:07:58.579 | Spain              | Italy              | 210 | Pressure        |   -   | [65.1, 14.1]    |  |
| -411.84 | -411.84 | 00:07:58.860 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [54.8, 67.1]    |  |
| -411.84 | -411.84 | 00:07:58.860 | Italy              | Italy              | 210 | Carry           |   -   | [54.8, 67.1]    |  |
| -411.22 | -411.22 | 00:07:59.479 | Italy              | Italy              | 210 | Pass            |   -   | [54.6, 63.9]    | Incomplete (Pass Offside) |
| -409.31 | -409.31 | 00:08:01.389 | Italy              | Italy              | 210 | Ball Receipt*   |   -   | [64.0, 45.3]    | Incomplete |
| -399.11 | -399.11 | 00:08:11.592 | Spain              | Spain              | 211 | Pass            |   -   | [48.4, 31.6]    | -> Aymeric Laport |
| -397.90 | -397.90 | 00:08:12.798 | Spain              | Spain              | 211 | Ball Receipt*   |   -   | [48.0, 47.7]    |  |
| -393.15 | -393.15 | 00:08:17.547 | Spain              | Spain              | 211 | Pass            |   -   | [48.2, 50.6]    | Incomplete (Incomplete) |
| -390.69 | -390.69 | 00:08:20.009 | Spain              | Spain              | 211 | Ball Receipt*   |   -   | [83.9, 79.5]    | Incomplete |
| -390.69 | -390.69 | 00:08:20.009 | Italy              | Spain              | 211 | Pass            |   -   | [36.4, 6.6]     | -> Manuel Locatel |
| -388.87 | -388.87 | 00:08:21.828 | Italy              | Spain              | 211 | Ball Receipt*   |   -   | [60.4, 5.9]     |  |
| -388.87 | -388.87 | 00:08:21.828 | Italy              | Spain              | 211 | Carry           |   -   | [60.4, 5.9]     |  |
| -387.14 | -387.14 | 00:08:23.563 | Spain              | Spain              | 211 | Pressure        |  Yes  | [62.5, 75.9]    |  |
| -386.04 | -386.04 | 00:08:24.656 | Spain              | Spain              | 211 | Pressure        |  Yes  | [58.2, 76.1]    |  |
| -384.76 | -384.76 | 00:08:25.943 | Italy              | Spain              | 211 | Miscontrol      |   -   | [61.9, 2.5]     |  |
| -379.10 | -379.10 | 00:08:31.601 | Spain              | Spain              | 212 | Pass            |   -   | [54.6, 80.0]    | -> Aymeric Laport |
| -377.62 | -377.62 | 00:08:33.080 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [38.1, 74.2]    |  |
| -377.62 | -377.62 | 00:08:33.080 | Spain              | Spain              | 212 | Carry           |   -   | [38.1, 74.2]    |  |
| -376.54 | -376.54 | 00:08:34.157 | Spain              | Spain              | 212 | Pass            |   -   | [37.3, 73.1]    | -> Marcos Llorent |
| -375.67 | -375.67 | 00:08:35.026 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [49.2, 76.5]    |  |
| -375.67 | -375.67 | 00:08:35.026 | Spain              | Spain              | 212 | Carry           |   -   | [49.2, 76.5]    |  |
| -375.65 | -375.65 | 00:08:35.050 | Italy              | Spain              | 212 | Pressure        |   -   | [67.4, 3.8]     |  |
| -375.36 | -375.36 | 00:08:35.339 | Italy              | Spain              | 212 | Pressure        |   -   | [69.2, 2.9]     |  |
| -374.91 | -374.91 | 00:08:35.795 | Spain              | Spain              | 212 | Pass            |   -   | [51.2, 77.6]    | -> Thiago Alcânta |
| -374.00 | -374.00 | 00:08:36.700 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [51.4, 72.0]    |  |
| -374.00 | -374.00 | 00:08:36.700 | Spain              | Spain              | 212 | Carry           |   -   | [51.4, 72.0]    |  |
| -372.09 | -372.09 | 00:08:38.606 | Spain              | Spain              | 212 | Pass            |   -   | [48.8, 74.0]    | -> Rodrigo Hernán |
| -370.70 | -370.70 | 00:08:40.000 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [41.1, 64.8]    |  |
| -370.70 | -370.70 | 00:08:40.000 | Spain              | Spain              | 212 | Carry           |   -   | [41.1, 64.8]    |  |
| -369.21 | -369.21 | 00:08:41.495 | Spain              | Spain              | 212 | Pass            |   -   | [40.5, 59.6]    | -> Pedro González |
| -368.27 | -368.27 | 00:08:42.435 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [50.1, 42.9]    |  |
| -368.27 | -368.27 | 00:08:42.435 | Spain              | Spain              | 212 | Carry           |   -   | [50.1, 42.9]    |  |
| -368.23 | -368.23 | 00:08:42.475 | Spain              | Spain              | 212 | Pass            |   -   | [50.1, 42.9]    | -> Pau Francisco  |
| -366.85 | -366.85 | 00:08:43.849 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [33.6, 37.4]    |  |
| -366.85 | -366.85 | 00:08:43.849 | Spain              | Spain              | 212 | Carry           |   -   | [33.6, 37.4]    |  |
| -359.59 | -359.59 | 00:08:51.106 | Spain              | Spain              | 212 | Pass            |   -   | [50.1, 34.2]    | -> Álvaro Borja M |
| -358.70 | -358.70 | 00:08:51.999 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [62.5, 34.0]    |  |
| -358.70 | -358.70 | 00:08:51.999 | Spain              | Spain              | 212 | Carry           |   -   | [62.5, 34.0]    |  |
| -358.66 | -358.66 | 00:08:52.039 | Spain              | Spain              | 212 | Pass            |   -   | [62.7, 34.2]    | -> Jordi Alba Ram |
| -356.87 | -356.87 | 00:08:53.832 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [67.6, 11.1]    |  |
| -356.87 | -356.87 | 00:08:53.832 | Spain              | Spain              | 212 | Carry           |   -   | [67.6, 11.1]    |  |
| -352.73 | -352.73 | 00:08:57.968 | Spain              | Spain              | 212 | Pass            |   -   | [90.9, 16.9]    | -> Daniel Olmo Ca |
| -351.72 | -351.72 | 00:08:58.980 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [96.1, 7.4]     |  |
| -351.72 | -351.72 | 00:08:58.980 | Spain              | Spain              | 212 | Carry           |   -   | [96.1, 7.4]     |  |
| -350.36 | -350.36 | 00:09:00.342 | Spain              | Spain              | 212 | Pass            |   -   | [92.9, 7.2]     | -> Rodrigo Hernán |
| -349.05 | -349.05 | 00:09:01.648 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [75.3, 13.4]    |  |
| -349.05 | -349.05 | 00:09:01.648 | Spain              | Spain              | 212 | Carry           |   -   | [75.3, 13.4]    |  |
| -347.91 | -347.91 | 00:09:02.793 | Spain              | Spain              | 212 | Pass            |   -   | [78.5, 14.7]    | -> Aymeric Laport |
| -344.26 | -344.26 | 00:09:06.439 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [72.1, 60.9]    |  |
| -344.26 | -344.26 | 00:09:06.439 | Spain              | Spain              | 212 | Carry           |   -   | [72.1, 60.9]    |  |
| -344.02 | -344.02 | 00:09:06.679 | Spain              | Spain              | 212 | Pass            |   -   | [74.7, 72.9]    | -> Gerard Moreno  |
| -342.03 | -342.03 | 00:09:08.675 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [91.2, 78.0]    |  |
| -342.03 | -342.03 | 00:09:08.675 | Spain              | Spain              | 212 | Carry           |   -   | [91.2, 78.0]    |  |
| -340.87 | -340.87 | 00:09:09.833 | Spain              | Spain              | 212 | Pass            |   -   | [93.3, 75.5]    | Incomplete (Incomplete) |
| -340.76 | -340.76 | 00:09:09.943 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [96.3, 69.0]    | Incomplete |
| -340.76 | -340.76 | 00:09:09.943 | Italy              | Spain              | 212 | Block           |   -   | [22.7, 6.8]     |  |
| -339.68 | -339.68 | 00:09:11.021 | Spain              | Spain              | 212 | Pressure        |   -   | [90.7, 71.0]    |  |
| -339.57 | -339.57 | 00:09:11.126 | Italy              | Spain              | 212 | Ball Recovery   |   -   | [30.6, 12.1]    |  |
| -339.57 | -339.57 | 00:09:11.126 | Italy              | Spain              | 212 | Carry           |   -   | [30.6, 12.1]    |  |
| -338.95 | -338.95 | 00:09:11.751 | Italy              | Spain              | 212 | Pass            |   -   | [31.9, 12.1]    | -> Andrea Belotti |
| -338.16 | -338.16 | 00:09:12.542 | Italy              | Spain              | 212 | Ball Receipt*   |   -   | [43.7, 13.0]    |  |
| -338.16 | -338.16 | 00:09:12.542 | Italy              | Spain              | 212 | Carry           |   -   | [43.7, 13.0]    |  |
| -335.65 | -335.65 | 00:09:15.052 | Italy              | Spain              | 212 | Pass            |   -   | [57.8, 17.0]    | Incomplete (Incomplete) |
| -335.02 | -335.02 | 00:09:15.684 | Italy              | Spain              | 212 | Ball Receipt*   |   -   | [73.9, 41.0]    | Incomplete |
| -335.02 | -335.02 | 00:09:15.684 | Spain              | Spain              | 212 | Interception    |  Yes  | [49.0, 52.1]    | Success In Play |
| -334.19 | -334.19 | 00:09:16.506 | Spain              | Spain              | 212 | Ball Recovery   |   -   | [55.9, 47.7]    |  |
| -334.19 | -334.19 | 00:09:16.506 | Spain              | Spain              | 212 | Carry           |   -   | [55.9, 47.7]    |  |
| -333.20 | -333.20 | 00:09:17.501 | Spain              | Spain              | 212 | Pass            |   -   | [56.1, 48.3]    | -> Daniel Olmo Ca |
| -331.93 | -331.93 | 00:09:18.771 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [72.3, 32.0]    |  |
| -331.93 | -331.93 | 00:09:18.771 | Spain              | Spain              | 212 | Pass            |   -   | [72.3, 32.0]    | -> Álvaro Borja M |
| -330.89 | -330.89 | 00:09:19.808 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [79.0, 36.1]    |  |
| -330.89 | -330.89 | 00:09:19.808 | Spain              | Spain              | 212 | Carry           |   -   | [79.0, 36.1]    |  |
| -325.24 | -325.24 | 00:09:25.459 | Spain              | Spain              | 212 | Pass            |   -   | [110.6, 21.8]   | Incomplete (Incomplete) |
| -325.16 | -325.16 | 00:09:25.543 | Spain              | Spain              | 212 | Ball Receipt*   |   -   | [113.0, 31.4]   | Incomplete |
| -325.16 | -325.16 | 00:09:25.543 | Italy              | Spain              | 212 | Block           |   -   | [7.1, 53.0]     |  |
| -320.19 | -320.19 | 00:09:30.510 | Spain              | Spain              | 213 | Pass            |   -   | [111.7, 0.1]    | -> Daniel Olmo Ca |
| -318.79 | -318.79 | 00:09:31.914 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [100.4, 13.2]   |  |
| -318.79 | -318.79 | 00:09:31.914 | Spain              | Spain              | 213 | Carry           |   -   | [100.4, 13.2]   |  |
| -315.42 | -315.42 | 00:09:35.280 | Spain              | Spain              | 213 | Pass            |   -   | [101.0, 21.1]   | -> Álvaro Borja M |
| -314.15 | -314.15 | 00:09:36.551 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [103.1, 9.6]    |  |
| -314.15 | -314.15 | 00:09:36.551 | Spain              | Spain              | 213 | Carry           |   -   | [103.1, 9.6]    |  |
| -310.53 | -310.53 | 00:09:40.172 | Italy              | Spain              | 213 | Pressure        |   -   | [24.0, 56.8]    |  |
| -308.87 | -308.87 | 00:09:41.832 | Spain              | Spain              | 213 | Pass            |   -   | [96.1, 27.5]    | Incomplete (Incomplete) |
| -308.57 | -308.57 | 00:09:42.133 | Spain              | Spain              | 213 | Pressure        |   -   | [90.3, 41.7]    |  |
| -308.17 | -308.17 | 00:09:42.531 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [88.8, 34.6]    | Incomplete |
| -308.17 | -308.17 | 00:09:42.531 | Italy              | Spain              | 213 | Ball Recovery   |   -   | [30.6, 40.8]    |  |
| -306.43 | -306.43 | 00:09:44.275 | Spain              | Spain              | 213 | Ball Recovery   |   -   | [96.3, 53.4]    |  |
| -306.43 | -306.43 | 00:09:44.275 | Spain              | Spain              | 213 | Carry           |   -   | [96.3, 53.4]    |  |
| -301.71 | -301.71 | 00:09:48.988 | Spain              | Spain              | 213 | Pass            |   -   | [97.6, 62.4]    | -> Gerard Moreno  |
| -300.98 | -300.98 | 00:09:49.718 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [97.6, 74.4]    |  |
| -300.98 | -300.98 | 00:09:49.718 | Spain              | Spain              | 213 | Carry           |   -   | [97.6, 74.4]    |  |
| -299.37 | -299.37 | 00:09:51.328 | Spain              | Spain              | 213 | Pass            |   -   | [97.8, 73.3]    | -> Pedro González |
| -298.05 | -298.05 | 00:09:52.647 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [92.4, 54.7]    |  |
| -298.05 | -298.05 | 00:09:52.647 | Spain              | Spain              | 213 | Carry           |   -   | [92.4, 54.7]    |  |
| -297.04 | -297.04 | 00:09:53.662 | Spain              | Spain              | 213 | Pass            |   -   | [92.2, 54.7]    | -> Gerard Moreno  |
| -295.38 | -295.38 | 00:09:55.316 | Spain              | Spain              | 213 | Ball Receipt*   |   -   | [95.0, 74.6]    |  |
| -295.38 | -295.38 | 00:09:55.316 | Spain              | Spain              | 213 | Carry           |   -   | [95.0, 74.6]    |  |
| -294.05 | -294.05 | 00:09:56.653 | Spain              | Spain              | 213 | Pass            |   -   | [95.2, 72.5]    | Incomplete (Incomplete) |
| -291.80 | -291.80 | 00:09:58.898 | Italy              | Italy              | 214 | Goal Keeper     |   -   | [6.3, 46.1]     |  |
| -280.59 | -280.59 | 00:10:10.108 | Italy              | Italy              | 214 | Pass            |   -   | [7.1, 45.3]     | -> Rafael Tolói |
| -279.48 | -279.48 | 00:10:11.218 | Italy              | Italy              | 214 | Ball Receipt*   |   -   | [21.7, 49.3]    |  |
| -279.12 | -279.12 | 00:10:11.579 | Italy              | Italy              | 214 | Pass            |   -   | [45.2, 72.4]    | -> Domenico Berar |
| -278.10 | -278.10 | 00:10:12.604 | Italy              | Italy              | 214 | Ball Receipt*   |   -   | [54.4, 66.2]    |  |
| -278.10 | -278.10 | 00:10:12.604 | Italy              | Italy              | 214 | Carry           |   -   | [54.4, 66.2]    |  |
| -276.45 | -276.45 | 00:10:14.249 | Spain              | Italy              | 214 | Pressure        |   -   | [67.0, 20.7]    |  |
| -273.66 | -273.66 | 00:10:17.040 | Italy              | Italy              | 214 | Pass            |   -   | [47.3, 55.5]    | -> Giorgio Chiell |
| -271.46 | -271.46 | 00:10:19.241 | Italy              | Italy              | 214 | Ball Receipt*   |   -   | [39.8, 23.0]    |  |
| -271.46 | -271.46 | 00:10:19.241 | Italy              | Italy              | 214 | Carry           |   -   | [39.8, 23.0]    |  |
| -267.27 | -267.27 | 00:10:23.434 | Italy              | Italy              | 214 | Pass            |   -   | [55.0, 22.4]    | Incomplete (Pass Offside) |
| -264.14 | -264.14 | 00:10:26.559 | Italy              | Italy              | 214 | Ball Receipt*   |   -   | [102.3, 54.9]   | Incomplete |
| -253.89 | -253.89 | 00:10:36.807 | Spain              | Spain              | 215 | Pass            |   -   | [18.2, 26.5]    | -> Marcos Llorent |
| -252.56 | -252.56 | 00:10:38.142 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [29.1, 39.3]    |  |
| -248.82 | -248.82 | 00:10:41.879 | Spain              | Spain              | 215 | Pass            |   -   | [55.0, 72.9]    | -> Thiago Alcânta |
| -247.64 | -247.64 | 00:10:43.056 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [54.2, 62.2]    |  |
| -247.64 | -247.64 | 00:10:43.056 | Spain              | Spain              | 215 | Carry           |   -   | [54.2, 62.2]    |  |
| -244.41 | -244.41 | 00:10:46.291 | Spain              | Spain              | 215 | Pass            |   -   | [54.4, 48.1]    | -> Rodrigo Hernán |
| -243.47 | -243.47 | 00:10:47.228 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [64.2, 43.8]    |  |
| -243.47 | -243.47 | 00:10:47.228 | Spain              | Spain              | 215 | Carry           |   -   | [64.2, 43.8]    |  |
| -243.33 | -243.33 | 00:10:47.368 | Italy              | Spain              | 215 | Pressure        |   -   | [55.5, 38.0]    |  |
| -242.95 | -242.95 | 00:10:47.751 | Spain              | Spain              | 215 | Pass            |   -   | [65.3, 41.5]    | -> Pau Francisco  |
| -241.08 | -241.08 | 00:10:49.622 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [50.7, 35.2]    |  |
| -241.08 | -241.08 | 00:10:49.622 | Spain              | Spain              | 215 | Carry           |   -   | [50.7, 35.2]    |  |
| -241.04 | -241.04 | 00:10:49.662 | Spain              | Spain              | 215 | Pass            |   -   | [50.5, 35.0]    | -> Aymeric Laport |
| -239.81 | -239.81 | 00:10:50.886 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [47.7, 49.6]    |  |
| -239.81 | -239.81 | 00:10:50.886 | Spain              | Spain              | 215 | Carry           |   -   | [47.7, 49.6]    |  |
| -237.86 | -237.86 | 00:10:52.838 | Spain              | Spain              | 215 | Pass            |   -   | [44.3, 49.4]    | -> Thiago Alcânta |
| -236.84 | -236.84 | 00:10:53.860 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [50.5, 59.0]    |  |
| -236.84 | -236.84 | 00:10:53.860 | Spain              | Spain              | 215 | Carry           |   -   | [50.5, 59.0]    |  |
| -235.53 | -235.53 | 00:10:55.175 | Spain              | Spain              | 215 | Pass            |   -   | [51.6, 62.2]    | Incomplete (Out) |
| -230.86 | -230.86 | 00:10:59.839 | Spain              | Spain              | 215 | Ball Receipt*   |   -   | [117.5, 68.4]   | Incomplete |
| -208.04 | -208.04 | 00:11:22.663 | Italy              | Italy              | 216 | Pass            |   -   | [6.0, 44.0]     | -> Gianluigi Donn |
| -206.93 | -206.93 | 00:11:23.772 | Italy              | Italy              | 216 | Ball Receipt*   |   -   | [5.2, 41.9]     |  |
| -206.93 | -206.93 | 00:11:23.772 | Italy              | Italy              | 216 | Carry           |   -   | [5.2, 41.9]     |  |
| -203.54 | -203.54 | 00:11:27.158 | Italy              | Italy              | 216 | Pass            |   -   | [6.3, 35.7]     | -> Andrea Belotti |
| -201.58 | -201.58 | 00:11:29.122 | Italy              | Italy              | 216 | Ball Receipt*   |   -   | [54.2, 31.8]    |  |
| -201.58 | -201.58 | 00:11:29.122 | Italy              | Italy              | 216 | Carry           |   -   | [54.2, 31.8]    |  |
| -201.51 | -201.51 | 00:11:29.188 | Spain              | Italy              | 216 | Pressure        |   -   | [65.1, 49.2]    |  |
| -201.22 | -201.22 | 00:11:29.480 | Italy              | Italy              | 216 | Miscontrol      |   -   | [54.8, 31.6]    |  |
| -200.33 | -200.33 | 00:11:30.375 | Spain              | Italy              | 216 | Ball Recovery   |   -   | [65.9, 48.3]    |  |
| -200.33 | -200.33 | 00:11:30.375 | Spain              | Italy              | 216 | Carry           |   -   | [65.9, 48.3]    |  |
| -199.29 | -199.29 | 00:11:31.412 | Spain              | Italy              | 216 | Pass            |   -   | [62.5, 44.7]    | -> Rodrigo Hernán |
| -198.37 | -198.37 | 00:11:32.330 | Spain              | Italy              | 216 | Ball Receipt*   |   -   | [57.6, 39.5]    |  |
| -198.37 | -198.37 | 00:11:32.330 | Spain              | Italy              | 216 | Carry           |   -   | [57.6, 39.5]    |  |
| -196.75 | -196.75 | 00:11:33.948 | Spain              | Italy              | 216 | Pass            |   -   | [56.3, 28.8]    | Incomplete (Incomplete) |
| -194.42 | -194.42 | 00:11:36.285 | Spain              | Italy              | 216 | Ball Receipt*   |   -   | [76.4, 9.8]     | Incomplete |
| -194.42 | -194.42 | 00:11:36.285 | Italy              | Italy              | 216 | Pass            |  Yes  | [45.0, 68.4]    | -> Domenico Berar |
| -192.96 | -192.96 | 00:11:37.738 | Italy              | Italy              | 216 | Ball Receipt*   |   -   | [67.2, 66.9]    |  |
| -192.96 | -192.96 | 00:11:37.738 | Italy              | Italy              | 216 | Carry           |   -   | [67.2, 66.9]    |  |
| -192.64 | -192.64 | 00:11:38.059 | Spain              | Italy              | 216 | Pressure        |   -   | [53.9, 11.3]    |  |
| -191.98 | -191.98 | 00:11:38.719 | Italy              | Italy              | 216 | Dribble         |   -   | [67.0, 71.8]    |  |
| -191.98 | -191.98 | 00:11:38.719 | Spain              | Italy              | 216 | Duel            |   -   | [53.1, 8.3]     | Tackle, Lost Out |
| -177.63 | -177.63 | 00:11:53.069 | Italy              | Italy              | 217 | Pass            |   -   | [64.2, 80.0]    | -> Matteo Pessina |
| -176.93 | -176.93 | 00:11:53.768 | Spain              | Italy              | 217 | Pressure        |   -   | [43.2, 9.6]     |  |
| -176.57 | -176.57 | 00:11:54.132 | Italy              | Italy              | 217 | Ball Receipt*   |   -   | [68.3, 71.4]    |  |
| -176.57 | -176.57 | 00:11:54.132 | Italy              | Italy              | 217 | Carry           |   -   | [68.3, 71.4]    |  |
| -176.53 | -176.53 | 00:11:54.174 | Italy              | Italy              | 217 | Pass            |   -   | [76.9, 69.2]    | -> Rafael Tolói |
| -175.90 | -175.90 | 00:11:54.799 | Italy              | Italy              | 217 | Ball Receipt*   |   -   | [76.0, 76.3]    |  |
| -175.90 | -175.90 | 00:11:54.799 | Italy              | Italy              | 217 | Carry           |   -   | [76.0, 76.3]    |  |
| -175.86 | -175.86 | 00:11:54.839 | Italy              | Italy              | 217 | Pass            |   -   | [76.0, 75.4]    | Incomplete (Incomplete) |
| -170.95 | -170.95 | 00:11:59.746 | Italy              | Italy              | 217 | Ball Receipt*   |   -   | [112.4, 67.1]   | Incomplete |
| -170.95 | -170.95 | 00:11:59.746 | Spain              | Italy              | 217 | Clearance       |   -   | [4.7, 13.9]     |  |
| -157.58 | -157.58 | 00:12:13.124 | Italy              | Italy              | 218 | Pass            |   -   | [95.0, 80.0]    | Incomplete (Incomplete) |
| -156.88 | -156.88 | 00:12:13.819 | Italy              | Italy              | 218 | Ball Receipt*   |   -   | [107.7, 73.1]   | Incomplete |
| -156.88 | -156.88 | 00:12:13.819 | Spain              | Spain              | 219 | Interception    |   -   | [16.1, 6.4]     | Won |
| -156.88 | -156.88 | 00:12:13.819 | Spain              | Spain              | 219 | Carry           |   -   | [16.1, 6.4]     |  |
| -154.84 | -154.84 | 00:12:15.859 | Spain              | Spain              | 219 | Pass            |   -   | [22.9, 5.1]     | -> Álvaro Borja M |
| -154.20 | -154.20 | 00:12:16.498 | Italy              | Spain              | 219 | Pressure        |  Yes  | [84.3, 70.1]    |  |
| -153.85 | -153.85 | 00:12:16.847 | Spain              | Spain              | 219 | Ball Receipt*   |   -   | [35.1, 10.0]    |  |
| -153.85 | -153.85 | 00:12:16.847 | Spain              | Spain              | 219 | Carry           |   -   | [35.1, 10.0]    |  |
| -153.54 | -153.54 | 00:12:17.157 | Italy              | Spain              | 219 | Foul Committed  |  Yes  | [84.3, 70.1]    |  |
| -153.54 | -153.54 | 00:12:17.157 | Spain              | Spain              | 219 | Foul Won        |   -   | [35.8, 10.0]    |  |
| -125.21 | -125.21 | 00:12:45.491 | Spain              | Spain              | 220 | Pass            |   -   | [35.8, 10.0]    | -> Pau Francisco  |
| -123.23 | -123.23 | 00:12:47.475 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [18.2, 15.8]    |  |
| -122.16 | -122.16 | 00:12:48.542 | Spain              | Spain              | 220 | Pass            |   -   | [17.8, 15.8]    | -> Unai Simón Men |
| -120.49 | -120.49 | 00:12:50.210 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [7.5, 35.2]     |  |
| -120.49 | -120.49 | 00:12:50.210 | Spain              | Spain              | 220 | Carry           |   -   | [7.5, 35.2]     |  |
| -119.33 | -119.33 | 00:12:51.375 | Spain              | Spain              | 220 | Pass            |   -   | [6.9, 36.1]     | -> Aymeric Laport |
| -117.43 | -117.43 | 00:12:53.275 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [19.7, 59.8]    |  |
| -117.43 | -117.43 | 00:12:53.275 | Spain              | Spain              | 220 | Carry           |   -   | [19.7, 59.8]    |  |
| -113.06 | -113.06 | 00:12:57.641 | Spain              | Spain              | 220 | Pass            |   -   | [41.5, 60.1]    | -> Pau Francisco  |
| -111.67 | -111.67 | 00:12:59.027 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [40.5, 32.5]    |  |
| -111.67 | -111.67 | 00:12:59.027 | Spain              | Spain              | 220 | Carry           |   -   | [40.5, 32.5]    |  |
| -106.60 | -106.60 | 00:13:04.099 | Spain              | Spain              | 220 | Pass            |   -   | [70.4, 32.5]    | -> Gerard Moreno  |
| -103.80 | -103.80 | 00:13:06.905 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [103.4, 75.2]   |  |
| -103.80 | -103.80 | 00:13:06.905 | Spain              | Spain              | 220 | Carry           |   -   | [103.4, 75.2]   |  |
| -102.94 | -102.94 | 00:13:07.763 | Italy              | Spain              | 220 | Pressure        |   -   | [17.2, 5.5]     |  |
| -102.42 | -102.42 | 00:13:08.279 | Spain              | Spain              | 220 | Pass            |   -   | [102.1, 77.2]   | -> Marcos Llorent |
| -100.75 | -100.75 | 00:13:09.948 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [87.5, 72.5]    |  |
| -100.75 | -100.75 | 00:13:09.948 | Spain              | Spain              | 220 | Carry           |   -   | [87.5, 72.5]    |  |
| -99.86 | -99.86 | 00:13:10.837 | Spain              | Spain              | 220 | Pass            |   -   | [85.4, 70.8]    | -> Rodrigo Hernán |
| -99.03 | -99.03 | 00:13:11.669 | Italy              | Spain              | 220 | Pressure        |   -   | [40.9, 20.3]    |  |
| -99.01 | -99.01 | 00:13:11.690 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [79.0, 62.0]    |  |
| -99.01 | -99.01 | 00:13:11.690 | Spain              | Spain              | 220 | Carry           |   -   | [79.0, 62.0]    |  |
| -98.10 | -98.10 | 00:13:12.598 | Spain              | Spain              | 220 | Pass            |   -   | [78.5, 61.1]    | -> Aymeric Laport |
| -96.41 | -96.41 | 00:13:14.291 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [65.1, 62.4]    |  |
| -96.41 | -96.41 | 00:13:14.291 | Spain              | Spain              | 220 | Pass            |   -   | [64.0, 58.1]    | -> Pau Francisco  |
| -95.13 | -95.13 | 00:13:15.566 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [65.9, 40.4]    |  |
| -95.13 | -95.13 | 00:13:15.566 | Spain              | Spain              | 220 | Carry           |   -   | [65.9, 40.4]    |  |
| -90.32 | -90.32 | 00:13:20.384 | Spain              | Spain              | 220 | Pass            |   -   | [90.1, 30.8]    | -> Pedro González |
| -89.72 | -89.72 | 00:13:20.983 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [98.6, 29.0]    |  |
| -89.72 | -89.72 | 00:13:20.983 | Spain              | Spain              | 220 | Carry           |   -   | [98.6, 29.0]    |  |
| -88.83 | -88.83 | 00:13:21.868 | Spain              | Spain              | 220 | Pass            |   -   | [100.4, 28.2]   | Incomplete (Incomplete) |
| -88.02 | -88.02 | 00:13:22.681 | Spain              | Spain              | 220 | Ball Receipt*   |   -   | [104.6, 43.4]   | Incomplete |
| -88.02 | -88.02 | 00:13:22.681 | Italy              | Spain              | 220 | Clearance       |   -   | [15.9, 40.1]    |  |
| -67.45 | -67.45 | 00:13:43.247 | Spain              | Spain              | 221 | Pass            |   -   | [86.0, 0.1]     | Incomplete (Incomplete) |
| -66.24 | -66.24 | 00:13:44.460 | Spain              | Spain              | 221 | Ball Receipt*   |   -   | [102.3, 10.0]   | Incomplete |
| -66.24 | -66.24 | 00:13:44.460 | Italy              | Spain              | 221 | Interception    |   -   | [20.4, 67.3]    | Lost Out |
| -50.29 | -50.29 | 00:14:00.413 | Spain              | Spain              | 222 | Pass            |   -   | [76.4, 0.1]     | -> Álvaro Borja M |
| -49.05 | -49.05 | 00:14:01.653 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [98.9, 7.0]     |  |
| -49.03 | -49.03 | 00:14:01.673 | Spain              | Spain              | 222 | Pass            |   -   | [96.5, 6.2]     | Incomplete (Incomplete) |
| -46.76 | -46.76 | 00:14:03.937 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [93.1, 37.4]    | Incomplete |
| -46.76 | -46.76 | 00:14:03.937 | Spain              | Spain              | 222 | Duel            |   -   | [93.5, 34.8]    | Aerial Lost |
| -46.76 | -46.76 | 00:14:03.937 | Italy              | Spain              | 222 | Clearance       |   -   | [26.6, 45.3]    |  |
| -44.61 | -44.61 | 00:14:06.089 | Spain              | Spain              | 222 | Ball Recovery   |   -   | [82.4, 57.3]    |  |
| -44.61 | -44.61 | 00:14:06.089 | Spain              | Spain              | 222 | Carry           |   -   | [82.4, 57.3]    |  |
| -43.24 | -43.24 | 00:14:07.459 | Spain              | Spain              | 222 | Pass            |   -   | [82.8, 58.1]    | Incomplete (Out) |
| -40.63 | -40.63 | 00:14:10.072 | Spain              | Spain              | 222 | Ball Receipt*   |   -   | [113.6, 66.0]   | Incomplete |
|  -9.05 |  -9.05 | 00:14:41.650 | Italy              | Italy              | 223 | Pass            |   -   | [6.0, 36.0]     | Incomplete (Incomplete) |
|  -6.13 |  -6.13 | 00:14:44.565 | Italy              | Italy              | 223 | Ball Receipt*   |   -   | [66.2, 6.4]     | Incomplete |
|  -6.13 |  -6.13 | 00:14:44.565 | Italy              | Italy              | 223 | Duel            |   -   | [67.0, 3.6]     | Aerial Lost |
|  -6.13 |  -6.13 | 00:14:44.565 | Spain              | Italy              | 223 | Clearance       |   -   | [53.1, 76.5]    |  |
|  +8.57 |  +8.57 | 00:14:59.272 | Italy              | Italy              | 224 | Pass            |   -   | [58.2, 0.1]     | -> Andrea Belotti |
| +12.05 | +12.05 | 00:15:02.755 | Italy              | Italy              | 224 | Ball Receipt*   |   -   | [100.8, 6.8]    |  |

---

### Disagreement Case 19: `3788754_p53_c36f6fab`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3788754 (UEFA Euro, 2020)
- **counterpressing_team**: Switzerland
- **opponent_team_at_turnover**: Italy
- **possession_team_at_counterpress_initiation**: Switzerland
- **possession_id_at_counterpress_initiation**: 53
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:32:25.887) | **Initiation**: Duel (00:32:25.887)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.142s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 10.617s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.54 |  -2.54 | 00:32:23.346 | Italy              | Italy              | 52 | Pass            |   -   | [71.9, 10.1]    | -> Lorenzo Insign |
|  -0.91 |  -0.91 | 00:32:24.979 | Italy              | Italy              | 52 | Ball Receipt*   |   -   | [77.7, 3.3]     |  |
|  -0.91 |  -0.91 | 00:32:24.979 | Italy              | Italy              | 52 | Carry           |   -   | [77.7, 3.3]     |  |
|  -0.16 |  -0.16 | 00:32:25.722 | Switzerland        | Italy              | 52 | Pressure        |  Yes  | [36.3, 76.0]    |  |
|  +0.00 |  +0.00 | 00:32:25.887 | Italy              | Italy              | 52 | Dispossessed    |   -   | [83.3, 2.6]     |  |
|  +0.00 |  +0.00 | 00:32:25.887 | Switzerland        | Switzerland        | 53 | Duel            |  Yes  | [36.8, 77.5]    | Tackle, Success In Play |
|  +1.14 |  +1.14 | 00:32:27.029 | Italy              | Switzerland        | 53 | Pressure        |  Yes  | [74.3, 3.6]     |  |
|  +1.80 |  +1.80 | 00:32:27.691 | Switzerland        | Switzerland        | 53 | Pass            |   -   | [45.2, 77.0]    | Incomplete (Incomplete) |
|  +1.87 |  +1.87 | 00:32:27.756 | Italy              | Switzerland        | 53 | Block           |  Yes  | [73.4, 3.3]     |  |
| +10.62 | +10.62 | 00:32:36.504 | Switzerland        | Switzerland        | 54 | Pass            |   -   | [55.8, 80.0]    | -> Fabian Lukas S |
| +13.56 | +13.56 | 00:32:39.442 | Switzerland        | Switzerland        | 54 | Ball Receipt*   |   -   | [26.8, 59.6]    |  |
| +13.56 | +13.56 | 00:32:39.442 | Switzerland        | Switzerland        | 54 | Carry           |   -   | [26.8, 59.6]    |  |
| +15.17 | +15.17 | 00:32:41.056 | Switzerland        | Switzerland        | 54 | Pass            |   -   | [27.2, 50.5]    | -> Manuel Obafemi |
| +16.98 | +16.98 | 00:32:42.862 | Switzerland        | Switzerland        | 54 | Ball Receipt*   |   -   | [33.1, 26.5]    |  |
| +16.98 | +16.98 | 00:32:42.862 | Switzerland        | Switzerland        | 54 | Carry           |   -   | [33.1, 26.5]    |  |
| +18.91 | +18.91 | 00:32:44.800 | Switzerland        | Switzerland        | 54 | Pass            |   -   | [39.2, 25.1]    | -> Ricardo Iván R |
| +20.18 | +20.18 | 00:32:46.063 | Switzerland        | Switzerland        | 54 | Ball Receipt*   |   -   | [55.4, 2.9]     |  |

---

### Disagreement Case 20: `3795221_p122_3250dba6`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3795221 (UEFA Euro, 2020)
- **counterpressing_team**: Denmark
- **opponent_team_at_turnover**: England
- **possession_team_at_counterpress_initiation**: Denmark
- **possession_id_at_counterpress_initiation**: 122
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:28:20.706) | **Initiation**: Duel (00:28:20.706)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.632s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.70 |  -2.70 | 00:28:18.006 | England            | England            | 121 | Pass            |   -   | [88.0, 25.1]    | -> Harry Kane |
|  -2.18 |  -2.18 | 00:28:18.525 | England            | England            | 121 | Ball Receipt*   |   -   | [92.5, 21.2]    |  |
|  -2.18 |  -2.18 | 00:28:18.525 | England            | England            | 121 | Carry           |   -   | [92.5, 21.2]    |  |
|  -1.52 |  -1.52 | 00:28:19.186 | Denmark            | England            | 121 | Pressure        |   -   | [26.5, 55.8]    |  |
|  +0.00 |  +0.00 | 00:28:20.706 | England            | England            | 121 | Dispossessed    |   -   | [91.6, 21.8]    |  |
|  +0.00 |  +0.00 | 00:28:20.706 | Denmark            | Denmark            | 122 | Duel            |  Yes  | [28.5, 58.3]    | Tackle, Success In Play |
|  +1.63 |  +1.63 | 00:28:22.338 | England            | Denmark            | 122 | Foul Committed  |  Yes  | [103.1, 22.9]   |  |
|  +1.63 |  +1.63 | 00:28:22.338 | Denmark            | Denmark            | 122 | Foul Won        |   -   | [17.0, 57.2]    |  |
| +63.60 | +63.60 | 00:29:24.304 | Denmark            | Denmark            | 123 | Pass            |   -   | [15.6, 48.2]    | -> Joakim Mæhle |
| +67.17 | +67.17 | 00:29:27.871 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [63.8, 6.7]     |  |
| +68.01 | +68.01 | 00:29:28.711 | England            | Denmark            | 123 | Pressure        |   -   | [50.4, 69.2]    |  |
| +69.41 | +69.41 | 00:29:30.114 | Denmark            | Denmark            | 123 | Pass            |   -   | [64.6, 2.2]     | -> Jannik Vesterg |
| +71.80 | +71.80 | 00:29:32.506 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [45.0, 7.6]     |  |
| +71.80 | +71.80 | 00:29:32.506 | Denmark            | Denmark            | 123 | Carry           |   -   | [45.0, 7.6]     |  |
| +73.79 | +73.79 | 00:29:34.496 | Denmark            | Denmark            | 123 | Pass            |   -   | [44.2, 17.1]    | Incomplete (Incomplete) |
| +78.27 | +78.27 | 00:29:38.973 | Denmark            | Denmark            | 123 | Ball Receipt*   |   -   | [89.6, 31.4]    | Incomplete |
| +78.27 | +78.27 | 00:29:38.973 | England            | England            | 124 | Ball Recovery   |   -   | [12.5, 42.5]    |  |

---

### Disagreement Case 21: `3788743_p122_84c548bb`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3788743 (UEFA Euro, 2020)
- **counterpressing_team**: Russia
- **opponent_team_at_turnover**: Belgium
- **possession_team_at_counterpress_initiation**: Russia
- **possession_id_at_counterpress_initiation**: 122
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:18:15.862) | **Initiation**: Duel (00:18:15.862)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.837s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.489s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.70 |  -1.70 | 00:18:14.162 | Russia             | Belgium            | 121 | Pressure        |   -   | [9.7, 18.3]     |  |
|  -1.45 |  -1.45 | 00:18:14.414 | Belgium            | Belgium            | 121 | Ball Receipt*   |   -   | [110.6, 60.3]   |  |
|  -1.45 |  -1.45 | 00:18:14.414 | Belgium            | Belgium            | 121 | Carry           |   -   | [110.6, 60.3]   |  |
|  -0.45 |  -0.45 | 00:18:15.412 | Russia             | Belgium            | 121 | Pressure        |   -   | [10.3, 18.5]    |  |
|  +0.00 |  +0.00 | 00:18:15.862 | Belgium            | Belgium            | 121 | Dispossessed    |   -   | [109.6, 59.0]   |  |
|  +0.00 |  +0.00 | 00:18:15.862 | Russia             | Russia             | 122 | Duel            |  Yes  | [10.5, 21.1]    | Tackle, Success In Play |
|  +1.84 |  +1.84 | 00:18:17.699 | Russia             | Russia             | 122 | Pass            |   -   | [10.3, 28.4]    | Incomplete (Incomplete) |
|  +4.77 |  +4.77 | 00:18:20.637 | Russia             | Russia             | 122 | Ball Receipt*   |   -   | [58.9, 21.5]    | Incomplete |
|  +4.77 |  +4.77 | 00:18:20.637 | Belgium            | Russia             | 122 | Interception    |  Yes  | [63.1, 59.8]    | Lost In Play |
|  +5.82 |  +5.82 | 00:18:21.683 | Belgium            | Russia             | 122 | Pressure        |   -   | [56.9, 68.4]    |  |
|  +6.49 |  +6.49 | 00:18:22.351 | Russia             | Russia             | 122 | Ball Recovery   |   -   | [64.4, 12.1]    |  |
|  +6.49 |  +6.49 | 00:18:22.351 | Russia             | Russia             | 122 | Carry           |   -   | [64.4, 12.1]    |  |
|  +6.60 |  +6.60 | 00:18:22.460 | Belgium            | Russia             | 122 | Foul Committed  |   -   | [51.8, 66.9]    |  |
|  +6.60 |  +6.60 | 00:18:22.460 | Russia             | Russia             | 122 | Foul Won        |   -   | [68.3, 13.2]    |  |
| +31.09 | +31.09 | 00:18:46.954 | Russia             | Russia             | 123 | Pass            |   -   | [71.7, 5.5]     | -> Maksim Mukhin |
| +32.08 | +32.08 | 00:18:47.943 | Russia             | Russia             | 123 | Ball Receipt*   |   -   | [70.2, 13.4]    |  |
| +32.08 | +32.08 | 00:18:47.943 | Russia             | Russia             | 123 | Carry           |   -   | [70.2, 13.4]    |  |

---

### Disagreement Case 22: `4020846_p111_5742f924`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 4020846 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Spain Women's
- **opponent_team_at_turnover**: England Women's
- **possession_team_at_counterpress_initiation**: Spain Women's
- **possession_id_at_counterpress_initiation**: 111
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:12:13.170) | **Initiation**: Duel (00:12:13.170)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.297s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.02 |  -2.02 | 00:12:11.152 | England Women's    | England Women's    | 110 | Pass            |   -   | [63.1, 35.4]    | -> Georgia Stanwa |
|  -0.90 |  -0.90 | 00:12:12.265 | England Women's    | England Women's    | 110 | Ball Receipt*   |   -   | [77.0, 30.8]    |  |
|  -0.90 |  -0.90 | 00:12:12.265 | England Women's    | England Women's    | 110 | Carry           |   -   | [77.0, 30.8]    |  |
|  -0.27 |  -0.27 | 00:12:12.898 | Spain Women's      | England Women's    | 110 | Pressure        |   -   | [46.7, 47.2]    |  |
|  +0.00 |  +0.00 | 00:12:13.170 | England Women's    | England Women's    | 110 | Dribble         |   -   | [74.2, 31.6]    |  |
|  +0.00 |  +0.00 | 00:12:13.170 | Spain Women's      | Spain Women's      | 111 | Duel            |  Yes  | [45.9, 48.5]    | Tackle, Success In Play |
|  +1.30 |  +1.30 | 00:12:14.467 | England Women's    | Spain Women's      | 111 | Pressure        |  Yes  | [86.5, 29.0]    |  |
|  +1.73 |  +1.73 | 00:12:14.895 | Spain Women's      | Spain Women's      | 111 | Pass            |   -   | [35.0, 52.7]    | Incomplete (Unknown) |
|  +2.29 |  +2.29 | 00:12:15.463 | England Women's    | Spain Women's      | 111 | Foul Committed  |  Yes  | [85.1, 28.4]    |  |
|  +2.29 |  +2.29 | 00:12:15.463 | Spain Women's      | Spain Women's      | 111 | Foul Won        |   -   | [35.0, 51.7]    |  |
| +33.54 | +33.54 | 00:12:46.707 | Spain Women's      | Spain Women's      | 112 | Pass            |   -   | [35.0, 51.7]    | -> Laia Aleixandr |
| +35.22 | +35.22 | 00:12:48.388 | Spain Women's      | Spain Women's      | 112 | Ball Receipt*   |   -   | [55.5, 16.5]    |  |
| +36.87 | +36.87 | 00:12:50.040 | Spain Women's      | Spain Women's      | 112 | Pass            |   -   | [55.5, 16.5]    | -> Irene Paredes  |
| +38.40 | +38.40 | 00:12:51.567 | Spain Women's      | Spain Women's      | 112 | Ball Receipt*   |   -   | [45.9, 33.6]    |  |
| +39.41 | +39.41 | 00:12:52.583 | Spain Women's      | Spain Women's      | 112 | Pass            |   -   | [45.9, 33.6]    | -> Laia Aleixandr |
| +40.99 | +40.99 | 00:12:54.163 | Spain Women's      | Spain Women's      | 112 | Ball Receipt*   |   -   | [51.5, 17.9]    |  |
| +40.99 | +40.99 | 00:12:54.163 | Spain Women's      | Spain Women's      | 112 | Carry           |   -   | [51.5, 17.9]    |  |

---

### Disagreement Case 23: `4018355_p243_c67e409e`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 4018355 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Sweden Women's
- **opponent_team_at_turnover**: England Women's
- **possession_team_at_counterpress_initiation**: Sweden Women's
- **possession_id_at_counterpress_initiation**: 243
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:13:05.045) | **Initiation**: Duel (00:13:05.045)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.145s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.714s) | Evidence: `completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.29 |  -4.29 | 00:13:00.754 | England Women's    | England Women's    | 242 | Pass            |   -   | [65.9, 56.0]    | -> Chloe Kelly |
|  -3.18 |  -3.18 | 00:13:01.860 | England Women's    | England Women's    | 242 | Ball Receipt*   |   -   | [74.3, 43.2]    |  |
|  -3.18 |  -3.18 | 00:13:01.860 | England Women's    | England Women's    | 242 | Carry           |   -   | [74.3, 43.2]    |  |
|  -0.46 |  -0.46 | 00:13:04.581 | Sweden Women's     | England Women's    | 242 | Pressure        |   -   | [33.6, 45.3]    |  |
|  +0.00 |  +0.00 | 00:13:05.045 | England Women's    | England Women's    | 242 | Dribble         |   -   | [86.0, 36.1]    |  |
|  +0.00 |  +0.00 | 00:13:05.045 | Sweden Women's     | Sweden Women's     | 243 | Duel            |  Yes  | [34.1, 44.0]    | Tackle, Success In Play |
|  +1.15 |  +1.15 | 00:13:06.190 | Sweden Women's     | Sweden Women's     | 243 | Pass            |   -   | [32.4, 38.5]    | Incomplete (Incomplete) |
|  +4.48 |  +4.48 | 00:13:09.520 | Sweden Women's     | Sweden Women's     | 243 | Duel            |   -   | [64.5, 54.7]    | Aerial Lost |
|  +4.48 |  +4.48 | 00:13:09.520 | England Women's    | Sweden Women's     | 243 | Pass            |   -   | [55.6, 25.4]    | Incomplete (Incomplete) |
|  +5.71 |  +5.71 | 00:13:10.759 | Sweden Women's     | Sweden Women's     | 243 | Pass            |   -   | [52.9, 58.1]    | -> Julia Zigiotti |
|  +8.73 |  +8.73 | 00:13:13.774 | England Women's    | Sweden Women's     | 243 | Pressure        |   -   | [65.1, 45.7]    |  |
|  +9.22 |  +9.22 | 00:13:14.263 | Sweden Women's     | Sweden Women's     | 243 | Ball Receipt*   |   -   | [56.1, 34.6]    |  |
|  +9.22 |  +9.22 | 00:13:14.263 | Sweden Women's     | Sweden Women's     | 243 | Carry           |   -   | [56.1, 34.6]    |  |
|  +9.26 |  +9.26 | 00:13:14.303 | Sweden Women's     | Sweden Women's     | 243 | Pass            |   -   | [55.7, 34.4]    | -> Lina Mona Andr |
| +10.37 | +10.37 | 00:13:15.416 | Sweden Women's     | Sweden Women's     | 243 | Ball Receipt*   |   -   | [63.9, 35.2]    |  |
| +10.37 | +10.37 | 00:13:15.416 | England Women's    | Sweden Women's     | 243 | Duel            |   -   | [56.7, 44.7]    | Aerial Lost |
| +10.37 | +10.37 | 00:13:15.416 | Sweden Women's     | Sweden Women's     | 243 | Pass            |   -   | [63.4, 35.4]    | -> Emma Stina Bla |

---

### Disagreement Case 24: `3835339_p75_519e4347`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3835339 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Switzerland Women's
- **opponent_team_at_turnover**: Netherlands Women's
- **possession_team_at_counterpress_initiation**: Switzerland Women's
- **possession_id_at_counterpress_initiation**: 75
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:38:08.999) | **Initiation**: Duel (00:38:08.999)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.921s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.21 |  -2.21 | 00:38:06.791 | Netherlands Women' | Netherlands Women' | 74 | Pass            |   -   | [92.3, 12.8]    | -> Sherida Spitse |
|  -0.89 |  -0.89 | 00:38:08.111 | Netherlands Women' | Netherlands Women' | 74 | Ball Receipt*   |   -   | [91.6, 33.7]    |  |
|  -0.89 |  -0.89 | 00:38:08.111 | Netherlands Women' | Netherlands Women' | 74 | Carry           |   -   | [91.6, 33.7]    |  |
|  -0.51 |  -0.51 | 00:38:08.491 | Switzerland Women' | Netherlands Women' | 74 | Pressure        |   -   | [26.0, 44.0]    |  |
|  +0.00 |  +0.00 | 00:38:08.999 | Netherlands Women' | Netherlands Women' | 74 | Dribble         |   -   | [95.9, 34.2]    |  |
|  +0.00 |  +0.00 | 00:38:08.999 | Switzerland Women' | Switzerland Women' | 75 | Duel            |  Yes  | [24.2, 45.9]    | Tackle, Success In Play |
|  +1.92 |  +1.92 | 00:38:10.920 | Netherlands Women' | Switzerland Women' | 75 | Foul Committed  |  Yes  | [99.2, 28.7]    |  |
|  +1.92 |  +1.92 | 00:38:10.920 | Switzerland Women' | Switzerland Women' | 75 | Foul Won        |   -   | [20.9, 51.4]    |  |
| +24.67 | +24.67 | 00:38:33.672 | Switzerland Women' | Switzerland Women' | 76 | Pass            |   -   | [16.3, 47.3]    | -> Luana Bühler |
| +27.09 | +27.09 | 00:38:36.092 | Switzerland Women' | Switzerland Women' | 76 | Ball Receipt*   |   -   | [18.8, 38.5]    |  |
| +32.09 | +32.09 | 00:38:41.089 | Switzerland Women' | Switzerland Women' | 76 | Pass            |   -   | [34.3, 23.4]    | -> Viola Calligar |
| +34.27 | +34.27 | 00:38:43.269 | Switzerland Women' | Switzerland Women' | 76 | Ball Receipt*   |   -   | [28.4, 43.6]    |  |
| +34.27 | +34.27 | 00:38:43.269 | Switzerland Women' | Switzerland Women' | 76 | Carry           |   -   | [28.4, 43.6]    |  |
| +35.07 | +35.07 | 00:38:44.069 | Switzerland Women' | Switzerland Women' | 76 | Pass            |   -   | [26.7, 49.1]    | -> Gaëlle Thalman |
| +36.89 | +36.89 | 00:38:45.894 | Switzerland Women' | Switzerland Women' | 76 | Ball Receipt*   |   -   | [16.3, 34.4]    |  |
| +36.89 | +36.89 | 00:38:45.894 | Switzerland Women' | Switzerland Women' | 76 | Carry           |   -   | [16.3, 34.4]    |  |
| +37.08 | +37.08 | 00:38:46.074 | Switzerland Women' | Switzerland Women' | 76 | Pass            |   -   | [16.3, 34.3]    | -> Luana Bühler |

---

### Disagreement Case 25: `3835323_p7_7b74e727`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3835323 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Switzerland Women's
- **opponent_team_at_turnover**: Portugal Women's
- **possession_team_at_counterpress_initiation**: Switzerland Women's
- **possession_id_at_counterpress_initiation**: 7
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:02:43.445) | **Initiation**: Duel (00:02:43.445)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.909s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.49 |  -4.49 | 00:02:38.952 | Switzerland Women' | Portugal Women's   | 6 | Pressure        |   -   | [9.5, 5.6]      |  |
|  -1.25 |  -1.25 | 00:02:42.196 | Portugal Women's   | Portugal Women's   | 6 | Pass            |   -   | [116.3, 74.9]   | -> Tatiana Vaness |
|  -0.40 |  -0.40 | 00:02:43.045 | Switzerland Women' | Portugal Women's   | 6 | Pressure        |   -   | [14.4, 7.4]     |  |
|  +0.00 |  +0.00 | 00:02:43.445 | Portugal Women's   | Portugal Women's   | 6 | Ball Receipt*   |   -   | [104.9, 74.8]   |  |
|  +0.00 |  +0.00 | 00:02:43.445 | Portugal Women's   | Portugal Women's   | 6 | Dispossessed    |   -   | [108.3, 75.2]   |  |
|  +0.00 |  +0.00 | 00:02:43.445 | Switzerland Women' | Switzerland Women' | 7 | Duel            |  Yes  | [11.8, 4.9]     | Tackle, Success In Play |
|  +0.91 |  +0.91 | 00:02:44.354 | Portugal Women's   | Switzerland Women' | 7 | Pressure        |  Yes  | [113.8, 74.1]   |  |
|  +0.95 |  +0.95 | 00:02:44.398 | Portugal Women's   | Switzerland Women' | 7 | Pressure        |  Yes  | [111.8, 73.4]   |  |
|  +1.01 |  +1.01 | 00:02:44.456 | Switzerland Women' | Switzerland Women' | 7 | Pass            |   -   | [9.1, 6.7]      | Incomplete (Incomplete) |
|  +1.18 |  +1.18 | 00:02:44.629 | Portugal Women's   | Switzerland Women' | 7 | Block           |  Yes  | [107.7, 73.4]   |  |
| +19.68 | +19.68 | 00:03:03.127 | Switzerland Women' | Switzerland Women' | 8 | Pass            |   -   | [7.0, 36.1]     | -> Viola Calligar |
| +22.33 | +22.33 | 00:03:05.776 | Switzerland Women' | Switzerland Women' | 8 | Ball Receipt*   |   -   | [14.9, 55.8]    |  |
| +24.53 | +24.53 | 00:03:07.970 | Switzerland Women' | Switzerland Women' | 8 | Pass            |   -   | [23.4, 58.1]    | -> Gaëlle Thalman |
| +26.66 | +26.66 | 00:03:10.109 | Switzerland Women' | Switzerland Women' | 8 | Ball Receipt*   |   -   | [11.0, 43.2]    |  |
| +26.66 | +26.66 | 00:03:10.109 | Switzerland Women' | Switzerland Women' | 8 | Carry           |   -   | [11.0, 43.2]    |  |
| +31.13 | +31.13 | 00:03:14.578 | Switzerland Women' | Switzerland Women' | 8 | Pass            |   -   | [13.9, 46.3]    | -> Viola Calligar |
| +33.04 | +33.04 | 00:03:16.487 | Switzerland Women' | Switzerland Women' | 8 | Ball Receipt*   |   -   | [19.8, 59.3]    |  |

---

### Disagreement Case 26: `3844387_p202_dbea4515`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3844387 (UEFA Women's Euro, 2022)
- **counterpressing_team**: France Women's
- **opponent_team_at_turnover**: Netherlands Women's
- **possession_team_at_counterpress_initiation**: France Women's
- **possession_id_at_counterpress_initiation**: 202
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:15:03.975) | **Initiation**: Duel (00:15:03.975)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 2.019s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.543s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.31 |  -3.31 | 00:15:00.668 | France Women's     | Netherlands Women' | 201 | Duel            |   -   | [7.7, 67.0]     | Tackle, Lost In Play |
|  -1.42 |  -1.42 | 00:15:02.560 | Netherlands Women' | Netherlands Women' | 201 | Ball Recovery   |   -   | [114.1, 17.9]   |  |
|  -1.42 |  -1.42 | 00:15:02.560 | Netherlands Women' | Netherlands Women' | 201 | Carry           |   -   | [114.1, 17.9]   |  |
|  -1.21 |  -1.21 | 00:15:02.770 | France Women's     | Netherlands Women' | 201 | Pressure        |   -   | [2.9, 63.1]     |  |
|  +0.00 |  +0.00 | 00:15:03.975 | Netherlands Women' | Netherlands Women' | 201 | Dribble         |   -   | [115.8, 21.1]   |  |
|  +0.00 |  +0.00 | 00:15:03.975 | France Women's     | France Women's     | 202 | Duel            |  Yes  | [4.3, 59.0]     | Tackle, Success In Play |
|  +2.02 |  +2.02 | 00:15:05.994 | France Women's     | France Women's     | 202 | Pass            |   -   | [3.9, 57.8]     | Incomplete (Incomplete) |
|  +4.48 |  +4.48 | 00:15:08.454 | France Women's     | France Women's     | 202 | Ball Receipt*   |   -   | [41.0, 66.2]    | Incomplete |
|  +4.48 |  +4.48 | 00:15:08.454 | Netherlands Women' | France Women's     | 202 | Interception    |  Yes  | [80.1, 13.9]    | Lost In Play |
|  +5.26 |  +5.26 | 00:15:09.238 | Netherlands Women' | France Women's     | 202 | Pressure        |   -   | [80.1, 13.1]    |  |
|  +5.54 |  +5.54 | 00:15:09.518 | France Women's     | France Women's     | 202 | Ball Recovery   |   -   | [38.8, 69.1]    |  |
|  +5.54 |  +5.54 | 00:15:09.518 | France Women's     | France Women's     | 202 | Carry           |   -   | [38.8, 69.1]    |  |
|  +6.04 |  +6.04 | 00:15:10.019 | Netherlands Women' | France Women's     | 202 | Dribbled Past   |   -   | [81.3, 10.2]    |  |
|  +6.04 |  +6.04 | 00:15:10.019 | France Women's     | France Women's     | 202 | Dribble         |   -   | [38.8, 69.9]    |  |
|  +6.04 |  +6.04 | 00:15:10.019 | France Women's     | France Women's     | 202 | Carry           |   -   | [38.8, 69.9]    |  |
| +14.68 | +14.68 | 00:15:18.660 | France Women's     | France Women's     | 202 | Pass            |   -   | [110.3, 69.1]   | Incomplete (Incomplete) |
| +16.13 | +16.13 | 00:15:20.108 | France Women's     | France Women's     | 202 | Ball Receipt*   |   -   | [111.3, 49.1]   | Incomplete |

---

### Disagreement Case 27: `3893833_p103_c845784a`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893833 (Women's World Cup, 2023)
- **counterpressing_team**: Germany Women's
- **opponent_team_at_turnover**: Korea Republic Women's
- **possession_team_at_counterpress_initiation**: Germany Women's
- **possession_id_at_counterpress_initiation**: 103
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:05:18.191) | **Initiation**: Duel (00:05:18.191)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.808s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.44 |  -4.44 | 00:05:13.748 | Korea Republic Wom | Korea Republic Wom | 102 | Pass            |   -   | [57.7, 17.8]    | -> Young-Ju Lee |
|  -3.40 |  -3.40 | 00:05:14.792 | Korea Republic Wom | Korea Republic Wom | 102 | Ball Receipt*   |   -   | [46.2, 25.2]    |  |
|  -3.40 |  -3.40 | 00:05:14.792 | Korea Republic Wom | Korea Republic Wom | 102 | Carry           |   -   | [46.2, 25.2]    |  |
|  -0.30 |  -0.30 | 00:05:17.895 | Germany Women's    | Korea Republic Wom | 102 | Pressure        |   -   | [65.9, 50.8]    |  |
|  +0.00 |  +0.00 | 00:05:18.191 | Korea Republic Wom | Korea Republic Wom | 102 | Dribble         |   -   | [54.2, 29.3]    |  |
|  +0.00 |  +0.00 | 00:05:18.191 | Germany Women's    | Germany Women's    | 103 | Duel            |  Yes  | [65.9, 50.8]    | Tackle, Success In Play |
|  +1.81 |  +1.81 | 00:05:19.999 | Korea Republic Wom | Germany Women's    | 103 | Pressure        |  Yes  | [55.9, 14.8]    |  |
|  +2.14 |  +2.14 | 00:05:20.330 | Korea Republic Wom | Germany Women's    | 103 | Foul Committed  |  Yes  | [55.9, 14.8]    |  |
|  +2.14 |  +2.14 | 00:05:20.330 | Germany Women's    | Germany Women's    | 103 | Foul Won        |   -   | [64.2, 65.3]    |  |
| +33.82 | +33.82 | 00:05:52.012 | Germany Women's    | Germany Women's    | 104 | Pass            |   -   | [64.2, 65.3]    | -> Chantal Hagel |
| +35.25 | +35.25 | 00:05:53.439 | Germany Women's    | Germany Women's    | 104 | Ball Receipt*   |   -   | [71.8, 19.4]    |  |
| +36.84 | +36.84 | 00:05:55.030 | Germany Women's    | Germany Women's    | 104 | Pass            |   -   | [71.8, 19.4]    | -> Kathrin Julia  |
| +38.00 | +38.00 | 00:05:56.187 | Germany Women's    | Germany Women's    | 104 | Ball Receipt*   |   -   | [62.4, 53.5]    |  |
| +38.00 | +38.00 | 00:05:56.187 | Germany Women's    | Germany Women's    | 104 | Carry           |   -   | [62.4, 53.5]    |  |
| +41.77 | +41.77 | 00:05:59.964 | Germany Women's    | Germany Women's    | 104 | Pass            |   -   | [74.4, 50.8]    | -> Marina Hegerin |
| +43.53 | +43.53 | 00:06:01.720 | Germany Women's    | Germany Women's    | 104 | Ball Receipt*   |   -   | [61.7, 43.8]    |  |
| +43.53 | +43.53 | 00:06:01.720 | Germany Women's    | Germany Women's    | 104 | Carry           |   -   | [61.7, 43.8]    |  |

---

### Disagreement Case 28: `3893831_p176_087a4529`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893831 (Women's World Cup, 2023)
- **counterpressing_team**: South Africa Women's
- **opponent_team_at_turnover**: Italy Women's
- **possession_team_at_counterpress_initiation**: South Africa Women's
- **possession_id_at_counterpress_initiation**: 176
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:39:12.601) | **Initiation**: Duel (00:39:12.601)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.524s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -6.25 |  -6.25 | 00:39:06.351 | Italy Women's      | Italy Women's      | 175 | Pass            |   -   | [36.9, 28.0]    | -> Benedetta Orsi |
|  -4.96 |  -4.96 | 00:39:07.639 | Italy Women's      | Italy Women's      | 175 | Ball Receipt*   |   -   | [37.9, 47.6]    |  |
|  -4.96 |  -4.96 | 00:39:07.639 | Italy Women's      | Italy Women's      | 175 | Carry           |   -   | [37.9, 47.6]    |  |
|  -3.16 |  -3.16 | 00:39:09.444 | South Africa Women | Italy Women's      | 175 | Pressure        |   -   | [73.2, 27.7]    |  |
|  +0.00 |  +0.00 | 00:39:12.601 | Italy Women's      | Italy Women's      | 175 | Dribble         |   -   | [68.8, 60.6]    |  |
|  +0.00 |  +0.00 | 00:39:12.601 | South Africa Women | South Africa Women | 176 | Duel            |  Yes  | [51.3, 19.5]    | Tackle, Success In Play |
|  +0.52 |  +0.52 | 00:39:13.125 | Italy Women's      | South Africa Women | 176 | Foul Committed  |  Yes  | [69.9, 62.4]    |  |
|  +0.52 |  +0.52 | 00:39:13.125 | South Africa Women | South Africa Women | 176 | Foul Won        |   -   | [50.2, 17.7]    |  |
| +31.23 | +31.23 | 00:39:43.833 | South Africa Women | South Africa Women | 177 | Pass            |   -   | [64.8, 26.3]    | -> Bongeka Gamede |
| +33.22 | +33.22 | 00:39:45.822 | Italy Women's      | South Africa Women | 177 | Pressure        |   -   | [37.1, 34.6]    |  |
| +33.55 | +33.55 | 00:39:46.147 | South Africa Women | South Africa Women | 177 | Ball Receipt*   |   -   | [80.5, 49.2]    |  |
| +33.55 | +33.55 | 00:39:46.147 | South Africa Women | South Africa Women | 177 | Pass            |   -   | [80.3, 47.9]    | -> Linda Maserame |
| +34.59 | +34.59 | 00:39:47.195 | Italy Women's      | South Africa Women | 177 | Pressure        |   -   | [39.8, 40.8]    |  |
| +34.96 | +34.96 | 00:39:47.561 | South Africa Women | South Africa Women | 177 | Ball Receipt*   |   -   | [80.0, 35.5]    |  |
| +34.96 | +34.96 | 00:39:47.561 | South Africa Women | South Africa Women | 177 | Carry           |   -   | [80.0, 35.5]    |  |
| +35.00 | +35.00 | 00:39:47.597 | South Africa Women | South Africa Women | 177 | Pass            |   -   | [80.5, 35.7]    | Incomplete (Incomplete) |
| +35.70 | +35.70 | 00:39:48.299 | South Africa Women | South Africa Women | 177 | Ball Receipt*   |   -   | [95.2, 45.3]    | Incomplete |

---

### Disagreement Case 29: `3893826_p57_89af3219`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893826 (Women's World Cup, 2023)
- **counterpressing_team**: United States Women's
- **opponent_team_at_turnover**: Portugal Women's
- **possession_team_at_counterpress_initiation**: United States Women's
- **possession_id_at_counterpress_initiation**: 57
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:28:15.450) | **Initiation**: Duel (00:28:15.450)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 3.335s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.38 |  -3.38 | 00:28:12.074 | Portugal Women's   | Portugal Women's   | 56 | Pass            |   -   | [50.9, 55.0]    | -> Andreia Alexan |
|  -1.94 |  -1.94 | 00:28:13.506 | Portugal Women's   | Portugal Women's   | 56 | Ball Receipt*   |   -   | [66.3, 44.3]    |  |
|  -1.94 |  -1.94 | 00:28:13.506 | Portugal Women's   | Portugal Women's   | 56 | Carry           |   -   | [66.3, 44.3]    |  |
|  -1.78 |  -1.78 | 00:28:13.666 | United States Wome | Portugal Women's   | 56 | Pressure        |   -   | [53.8, 35.8]    |  |
|  +0.00 |  +0.00 | 00:28:15.450 | Portugal Women's   | Portugal Women's   | 56 | Dispossessed    |   -   | [76.2, 35.4]    |  |
|  +0.00 |  +0.00 | 00:28:15.450 | United States Wome | United States Wome | 57 | Duel            |  Yes  | [43.9, 44.7]    | Tackle, Success In Play |
|  +3.34 |  +3.34 | 00:28:18.785 | United States Wome | United States Wome | 57 | Pass            |   -   | [24.3, 75.2]    | Incomplete (Incomplete) |
|  +3.40 |  +3.40 | 00:28:18.850 | United States Wome | United States Wome | 57 | Ball Receipt*   |   -   | [48.0, 66.1]    | Incomplete |
|  +3.40 |  +3.40 | 00:28:18.850 | Portugal Women's   | United States Wome | 57 | Block           |  Yes  | [93.1, 4.1]     |  |
|  +5.21 |  +5.21 | 00:28:20.664 | Portugal Women's   | United States Wome | 57 | Pressure        |   -   | [116.4, 3.9]    |  |
|  +6.86 |  +6.86 | 00:28:22.310 | United States Wome | United States Wome | 57 | Shield          |   -   | [3.7, 76.2]     |  |
| +17.68 | +17.68 | 00:28:33.128 | United States Wome | United States Wome | 58 | Pass            |   -   | [7.0, 44.1]     | -> Naomi Haile Gi |
| +20.16 | +20.16 | 00:28:35.613 | United States Wome | United States Wome | 58 | Ball Receipt*   |   -   | [11.3, 24.7]    |  |
| +20.16 | +20.16 | 00:28:35.613 | United States Wome | United States Wome | 58 | Carry           |   -   | [11.3, 24.7]    |  |
| +22.92 | +22.92 | 00:28:38.372 | United States Wome | United States Wome | 58 | Pass            |   -   | [21.0, 25.5]    | -> Crystal Alyssi |
| +24.32 | +24.32 | 00:28:39.772 | United States Wome | United States Wome | 58 | Ball Receipt*   |   -   | [33.4, 8.2]     |  |
| +24.32 | +24.32 | 00:28:39.772 | United States Wome | United States Wome | 58 | Carry           |   -   | [33.4, 8.2]     |  |

---

### Disagreement Case 30: `3901796_p98_b90c8fc6`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3901796 (Women's World Cup, 2023)
- **counterpressing_team**: Netherlands Women's
- **opponent_team_at_turnover**: South Africa Women's
- **possession_team_at_counterpress_initiation**: Netherlands Women's
- **possession_id_at_counterpress_initiation**: 98
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dribble (00:04:52.277) | **Initiation**: Duel (00:04:52.277)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.152s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.40 |  -1.40 | 00:04:50.878 | Netherlands Women' | South Africa Women | 97 | Dispossessed    |   -   | [62.2, 73.7]    |  |
|  -1.40 |  -1.40 | 00:04:50.878 | South Africa Women | South Africa Women | 97 | Duel            |  Yes  | [57.9, 6.4]     | Tackle, Won |
|  -1.40 |  -1.40 | 00:04:50.878 | South Africa Women | South Africa Women | 97 | Carry           |   -   | [57.9, 6.4]     |  |
|  -0.55 |  -0.55 | 00:04:51.731 | Netherlands Women' | South Africa Women | 97 | Pressure        |   -   | [66.3, 73.3]    |  |
|  +0.00 |  +0.00 | 00:04:52.277 | South Africa Women | South Africa Women | 97 | Dribble         |   -   | [54.9, 12.7]    |  |
|  +0.00 |  +0.00 | 00:04:52.277 | Netherlands Women' | Netherlands Women' | 98 | Duel            |  Yes  | [65.2, 67.4]    | Tackle, Success In Play |
|  +0.15 |  +0.15 | 00:04:52.429 | South Africa Women | Netherlands Women' | 98 | Foul Committed  |  Yes  | [54.9, 14.3]    |  |
|  +0.15 |  +0.15 | 00:04:52.429 | Netherlands Women' | Netherlands Women' | 98 | Foul Won        |   -   | [65.2, 65.8]    |  |
| +17.44 | +17.44 | 00:05:09.713 | Netherlands Women' | Netherlands Women' | 99 | Pass            |   -   | [64.1, 66.9]    | -> Dominique Joha |
| +18.90 | +18.90 | 00:05:11.174 | Netherlands Women' | Netherlands Women' | 99 | Ball Receipt*   |   -   | [68.9, 15.0]    |  |
| +19.81 | +19.81 | 00:05:12.084 | Netherlands Women' | Netherlands Women' | 99 | Pass            |   -   | [69.7, 14.0]    | Incomplete (Out) |
| +23.70 | +23.70 | 00:05:15.974 | Netherlands Women' | Netherlands Women' | 99 | Ball Receipt*   |   -   | [100.7, 16.0]   | Incomplete |
| +44.58 | +44.58 | 00:05:36.859 | South Africa Women | South Africa Women | 100 | Pass            |   -   | [6.0, 44.0]     | Incomplete (Incomplete) |
| +47.15 | +47.15 | 00:05:39.429 | South Africa Women | South Africa Women | 100 | Ball Receipt*   |   -   | [54.6, 61.8]    | Incomplete |
| +47.15 | +47.15 | 00:05:39.429 | South Africa Women | South Africa Women | 100 | Duel            |   -   | [52.3, 59.7]    | Aerial Lost |
| +47.15 | +47.15 | 00:05:39.429 | Netherlands Women' | Netherlands Women' | 101 | Pass            |   -   | [67.8, 20.4]    | -> Lineth Beerens |
| +48.57 | +48.57 | 00:05:40.852 | South Africa Women | Netherlands Women' | 101 | Pressure        |  Yes  | [43.5, 42.1]    |  |

---

### Disagreement Case 31: `3902239_p178_b3ad4c37`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3902239 (Women's World Cup, 2023)
- **counterpressing_team**: Sweden Women's
- **opponent_team_at_turnover**: Japan Women's
- **possession_team_at_counterpress_initiation**: Sweden Women's
- **possession_id_at_counterpress_initiation**: 178
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:51:31.999) | **Initiation**: Duel (00:51:31.999)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 2.222s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.40 |  -2.40 | 00:51:29.594 | Japan Women's      | Japan Women's      | 177 | Pass            |   -   | [91.2, 23.9]    | -> Jun Endo |
|  -1.49 |  -1.49 | 00:51:30.504 | Japan Women's      | Japan Women's      | 177 | Ball Receipt*   |   -   | [93.1, 12.8]    |  |
|  -1.49 |  -1.49 | 00:51:30.504 | Japan Women's      | Japan Women's      | 177 | Carry           |   -   | [93.1, 12.8]    |  |
|  -0.69 |  -0.69 | 00:51:31.313 | Sweden Women's     | Japan Women's      | 177 | Pressure        |   -   | [25.1, 62.6]    |  |
|  +0.00 |  +0.00 | 00:51:31.999 | Japan Women's      | Japan Women's      | 177 | Dispossessed    |   -   | [96.5, 17.9]    |  |
|  +0.00 |  +0.00 | 00:51:31.999 | Sweden Women's     | Sweden Women's     | 178 | Duel            |  Yes  | [23.6, 62.2]    | Tackle, Success In Play |
|  +2.22 |  +2.22 | 00:51:34.221 | Japan Women's      | Sweden Women's     | 178 | Pressure        |  Yes  | [92.4, 16.6]    |  |
|  +6.47 |  +6.47 | 00:51:38.470 | Japan Women's      | Sweden Women's     | 178 | Pressure        |   -   | [83.9, 26.3]    |  |
| +18.18 | +18.18 | 00:51:50.180 | Japan Women's      | Sweden Women's     | 178 | Pressure        |   -   | [24.2, 8.1]     |  |
| +18.83 | +18.83 | 00:51:50.828 | Sweden Women's     | Sweden Women's     | 178 | Pass            |   -   | [94.4, 72.0]    | -> Eva Sofia Jako |
| +20.33 | +20.33 | 00:51:52.330 | Sweden Women's     | Sweden Women's     | 178 | Ball Receipt*   |   -   | [79.8, 71.2]    |  |
| +20.33 | +20.33 | 00:51:52.330 | Sweden Women's     | Sweden Women's     | 178 | Carry           |   -   | [79.8, 71.2]    |  |
| +21.69 | +21.69 | 00:51:53.685 | Sweden Women's     | Sweden Women's     | 178 | Pass            |   -   | [83.3, 69.0]    | Incomplete (Incomplete) |
| +22.76 | +22.76 | 00:51:54.755 | Sweden Women's     | Sweden Women's     | 178 | Ball Receipt*   |   -   | [92.9, 73.9]    | Incomplete |
| +22.76 | +22.76 | 00:51:54.755 | Japan Women's      | Sweden Women's     | 178 | Interception    |   -   | [27.8, 6.2]     | Lost Out |
| +38.89 | +38.89 | 00:52:10.889 | Sweden Women's     | Sweden Women's     | 179 | Pass            |   -   | [102.3, 80.0]   | Incomplete (Incomplete) |
| +44.15 | +44.15 | 00:52:16.148 | Sweden Women's     | Sweden Women's     | 179 | Ball Receipt*   |   -   | [112.3, 71.5]   | Incomplete |

---

### Disagreement Case 32: `3838017_p31_8aa5e85d`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3838017 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Clermont Foot
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 31
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:23:48.971) | **Initiation**: Pressure (00:23:48.972)
- **Initiation Delay**: 0.001s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.149s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.30 |  -1.31 | 00:23:47.667 | Paris Saint-Germai | Paris Saint-Germai | 31 | Carry           |   -   | [11.0, 49.2]    |  |
|  -1.16 |  -1.16 | 00:23:47.815 | Paris Saint-Germai | Paris Saint-Germai | 31 | Error           |   -   | [11.7, 48.2]    |  |
|  -0.99 |  -0.99 | 00:23:47.979 | Paris Saint-Germai | Paris Saint-Germai | 31 | Pass            |   -   | [10.1, 48.7]    | Incomplete (Incomplete) |
|  +0.00 |  -0.00 | 00:23:48.971 | Paris Saint-Germai | Paris Saint-Germai | 31 | Ball Receipt*   |   -   | [3.7, 43.0]     | Incomplete |
|  +0.00 |  -0.00 | 00:23:48.971 | Clermont Foot      | Paris Saint-Germai | 31 | Interception    |   -   | [112.4, 37.9]   | Won |
|  +0.00 |  +0.00 | 00:23:48.972 | Paris Saint-Germai | Paris Saint-Germai | 31 | Pressure        |  Yes  | [5.2, 41.4]     |  |
|  +0.15 |  +0.15 | 00:23:49.121 | Clermont Foot      | Paris Saint-Germai | 31 | Shot            |   -   | [113.0, 41.2]   | Goal |
|  +1.00 |  +1.00 | 00:23:49.975 | Paris Saint-Germai | Paris Saint-Germai | 31 | Goal Keeper     |   -   | [4.7, 39.8]     |  |
| +35.56 | +35.56 | 00:24:24.527 | Paris Saint-Germai | Paris Saint-Germai | 32 | Pass            |   -   | [61.0, 40.1]    | -> Danilo Luís Hé |
| +36.38 | +36.38 | 00:24:25.356 | Paris Saint-Germai | Paris Saint-Germai | 32 | Ball Receipt*   |   -   | [32.8, 66.9]    |  |
| +39.87 | +39.87 | 00:24:28.843 | Paris Saint-Germai | Paris Saint-Germai | 32 | Pass            |   -   | [33.8, 65.1]    | -> Marco Verratti |
| +40.93 | +40.93 | 00:24:29.906 | Paris Saint-Germai | Paris Saint-Germai | 32 | Ball Receipt*   |   -   | [39.7, 60.3]    |  |
| +40.93 | +40.93 | 00:24:29.906 | Paris Saint-Germai | Paris Saint-Germai | 32 | Carry           |   -   | [39.7, 60.3]    |  |
| +42.27 | +42.27 | 00:24:31.238 | Paris Saint-Germai | Paris Saint-Germai | 32 | Pass            |   -   | [39.0, 59.9]    | -> Danilo Luís Hé |
| +43.82 | +43.82 | 00:24:32.788 | Paris Saint-Germai | Paris Saint-Germai | 32 | Ball Receipt*   |   -   | [38.9, 69.0]    |  |
| +43.82 | +43.82 | 00:24:32.788 | Paris Saint-Germai | Paris Saint-Germai | 32 | Carry           |   -   | [38.9, 69.0]    |  |
| +44.69 | +44.69 | 00:24:33.660 | Paris Saint-Germai | Paris Saint-Germai | 32 | Pass            |   -   | [39.0, 69.1]    | -> Sergio Ramos G |

---

### Disagreement Case 33: `3893808_p135_4721050b`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893808 (Women's World Cup, 2023)
- **counterpressing_team**: Netherlands Women's
- **opponent_team_at_turnover**: United States Women's
- **possession_team_at_counterpress_initiation**: Netherlands Women's
- **possession_id_at_counterpress_initiation**: 135
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Interception (00:21:02.984) | **Initiation**: Pressure (00:21:02.989)
- **Initiation Delay**: 0.005s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.925s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 10.148s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.05 |  -1.06 | 00:21:01.934 | Netherlands Women' | Netherlands Women' | 135 | Carry           |   -   | [76.9, 69.1]    |  |
|  -0.99 |  -0.99 | 00:21:01.997 | Netherlands Women' | Netherlands Women' | 135 | Pass            |   -   | [76.9, 69.2]    | Incomplete (Incomplete) |
|  +0.00 |  -0.01 | 00:21:02.984 | Netherlands Women' | Netherlands Women' | 135 | Ball Receipt*   |   -   | [67.8, 60.3]    | Incomplete |
|  +0.00 |  -0.01 | 00:21:02.984 | United States Wome | Netherlands Women' | 135 | Interception    |   -   | [50.6, 19.8]    | Won |
|  +0.00 |  -0.01 | 00:21:02.984 | United States Wome | Netherlands Women' | 135 | Carry           |   -   | [50.6, 19.8]    |  |
|  +0.01 |  +0.00 | 00:21:02.989 | Netherlands Women' | Netherlands Women' | 135 | Pressure        |  Yes  | [68.4, 62.5]    |  |
|  +0.93 |  +0.92 | 00:21:03.914 | Netherlands Women' | Netherlands Women' | 135 | Pressure        |  Yes  | [63.6, 74.2]    |  |
|  +1.67 |  +1.66 | 00:21:04.651 | Netherlands Women' | Netherlands Women' | 135 | Dribbled Past   |  Yes  | [61.8, 76.3]    |  |
|  +1.67 |  +1.66 | 00:21:04.651 | United States Wome | Netherlands Women' | 135 | Dribble         |   -   | [58.3, 3.8]     |  |
|  +1.67 |  +1.66 | 00:21:04.651 | United States Wome | Netherlands Women' | 135 | Carry           |   -   | [58.3, 3.8]     |  |
|  +3.45 |  +3.45 | 00:21:06.437 | United States Wome | Netherlands Women' | 135 | Pass            |   -   | [64.9, 2.4]     | Incomplete (Incomplete) |
|  +5.11 |  +5.11 | 00:21:08.095 | United States Wome | Netherlands Women' | 135 | Pressure        |   -   | [84.6, 29.0]    |  |
|  +5.38 |  +5.37 | 00:21:08.360 | United States Wome | Netherlands Women' | 135 | Ball Receipt*   |   -   | [86.2, 29.0]    | Incomplete |
|  +5.38 |  +5.37 | 00:21:08.360 | Netherlands Women' | Netherlands Women' | 135 | Pass            |   -   | [34.9, 56.0]    | Incomplete (Incomplete) |
|  +8.15 |  +8.15 | 00:21:11.136 | Netherlands Women' | Netherlands Women' | 135 | Ball Receipt*   |   -   | [46.7, 49.4]    | Incomplete |
|  +8.15 |  +8.15 | 00:21:11.136 | United States Wome | Netherlands Women' | 135 | Ball Recovery   |   -   | [64.0, 29.2]    |  |
|  +9.11 |  +9.10 | 00:21:12.090 | Netherlands Women' | Netherlands Women' | 135 | Pressure        |   -   | [50.1, 51.1]    |  |
| +10.15 | +10.15 | 00:21:13.137 | Netherlands Women' | Netherlands Women' | 135 | Ball Recovery   |   -   | [55.3, 50.9]    |  |

---

### Disagreement Case 34: `3902239_p101_65383156`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3902239 (Women's World Cup, 2023)
- **counterpressing_team**: Japan Women's
- **opponent_team_at_turnover**: Sweden Women's
- **possession_team_at_counterpress_initiation**: Japan Women's
- **possession_id_at_counterpress_initiation**: 101
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:08:36.357) | **Initiation**: Pressure (00:08:36.365)
- **Initiation Delay**: 0.008s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.994s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 7.196s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.59 |  -2.60 | 00:08:33.767 | Japan Women's      | Japan Women's      | 101 | Carry           |   -   | [98.4, 75.7]    |  |
|  -1.86 |  -1.87 | 00:08:34.499 | Japan Women's      | Japan Women's      | 101 | Pass            |   -   | [98.4, 75.7]    | Incomplete (Incomplete) |
|  +0.00 |  -0.01 | 00:08:36.357 | Japan Women's      | Japan Women's      | 101 | Ball Receipt*   |   -   | [110.4, 63.9]   | Incomplete |
|  +0.00 |  -0.01 | 00:08:36.357 | Sweden Women's     | Japan Women's      | 101 | Ball Recovery   |   -   | [8.2, 17.7]     |  |
|  +0.00 |  -0.01 | 00:08:36.357 | Sweden Women's     | Japan Women's      | 101 | Carry           |   -   | [8.2, 17.7]     |  |
|  +0.01 |  +0.00 | 00:08:36.365 | Japan Women's      | Japan Women's      | 101 | Pressure        |  Yes  | [111.1, 61.6]   |  |
|  +1.00 |  +0.99 | 00:08:37.359 | Sweden Women's     | Japan Women's      | 101 | Pass            |   -   | [8.0, 21.3]     | -> Kosovare Aslla |
|  +2.42 |  +2.41 | 00:08:38.777 | Japan Women's      | Japan Women's      | 101 | Pressure        |  Yes  | [94.2, 54.7]    |  |
|  +2.50 |  +2.49 | 00:08:38.859 | Sweden Women's     | Japan Women's      | 101 | Ball Receipt*   |   -   | [25.9, 25.4]    |  |
|  +2.50 |  +2.49 | 00:08:38.859 | Sweden Women's     | Japan Women's      | 101 | Carry           |   -   | [25.9, 25.4]    |  |
|  +5.81 |  +5.80 | 00:08:42.164 | Japan Women's      | Japan Women's      | 101 | Pressure        |  Yes  | [80.0, 51.1]    |  |
|  +7.20 |  +7.20 | 00:08:43.561 | Sweden Women's     | Japan Women's      | 101 | Dispossessed    |   -   | [51.0, 35.9]    |  |
|  +7.20 |  +7.20 | 00:08:43.561 | Japan Women's      | Japan Women's      | 101 | Duel            |  Yes  | [69.1, 44.2]    | Tackle, Won |
|  +7.20 |  +7.20 | 00:08:43.561 | Japan Women's      | Japan Women's      | 101 | Carry           |   -   | [69.1, 44.2]    |  |
|  +8.80 |  +8.79 | 00:08:45.153 | Sweden Women's     | Japan Women's      | 101 | Pressure        |   -   | [66.8, 37.8]    |  |
|  +9.52 |  +9.51 | 00:08:45.874 | Sweden Women's     | Japan Women's      | 101 | Pressure        |   -   | [66.6, 37.8]    |  |
|  +9.53 |  +9.52 | 00:08:45.883 | Japan Women's      | Japan Women's      | 101 | Pass            |   -   | [53.5, 42.3]    | -> Risa Shimizu |

---

### Disagreement Case 35: `3837947_p47_ef9ead3f`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837947 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Lens
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 47
- **Turnover Context**: open_play (Origin: From Keeper)
- **Turnover**: Ball Recovery (00:35:29.947) | **Initiation**: Pressure (00:35:29.961)
- **Initiation Delay**: 0.014s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.013s) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.288s) | Evidence: `completed_pass` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.87 |  -0.88 | 00:35:29.081 | Paris Saint-Germai | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [113.6, 65.7]   |  |
|  -0.87 |  -0.88 | 00:35:29.081 | Paris Saint-Germai | Paris Saint-Germai | 47 | Carry           |   -   | [113.6, 65.7]   |  |
|  -0.83 |  -0.84 | 00:35:29.120 | Paris Saint-Germai | Paris Saint-Germai | 47 | Miscontrol      |   -   | [113.6, 65.7]   |  |
|  +0.00 |  -0.01 | 00:35:29.947 | Lens               | Paris Saint-Germai | 47 | Ball Recovery   |   -   | [14.9, 13.9]    |  |
|  +0.00 |  -0.01 | 00:35:29.947 | Lens               | Paris Saint-Germai | 47 | Carry           |   -   | [14.9, 13.9]    |  |
|  +0.01 |  +0.00 | 00:35:29.961 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pressure        |  Yes  | [105.7, 66.3]   |  |
|  +1.03 |  +1.01 | 00:35:30.974 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pressure        |  Yes  | [105.4, 70.0]   |  |
|  +1.87 |  +1.85 | 00:35:31.813 | Lens               | Paris Saint-Germai | 47 | Pass            |   -   | [14.7, 10.1]    | -> Deiver Andrés  |
|  +2.70 |  +2.69 | 00:35:32.650 | Lens               | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [14.3, 5.2]     |  |
|  +2.70 |  +2.69 | 00:35:32.650 | Lens               | Paris Saint-Germai | 47 | Carry           |   -   | [14.3, 5.2]     |  |
|  +2.82 |  +2.81 | 00:35:32.770 | Lens               | Paris Saint-Germai | 47 | Pass            |   -   | [14.3, 5.2]     | Incomplete (Incomplete) |
|  +5.30 |  +5.29 | 00:35:35.249 | Lens               | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [47.0, 27.5]    | Incomplete |
|  +5.30 |  +5.29 | 00:35:35.249 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pass            |   -   | [68.5, 52.9]    | -> Marcos Aoás Co |
|  +6.55 |  +6.54 | 00:35:36.502 | Paris Saint-Germai | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [73.8, 68.3]    |  |
|  +6.55 |  +6.54 | 00:35:36.502 | Paris Saint-Germai | Paris Saint-Germai | 47 | Carry           |   -   | [73.8, 68.3]    |  |
|  +7.43 |  +7.42 | 00:35:37.381 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pass            |   -   | [74.7, 74.7]    | -> Achraf Hakimi  |
|  +8.36 |  +8.34 | 00:35:38.305 | Paris Saint-Germai | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [82.2, 73.9]    |  |
|  +8.36 |  +8.34 | 00:35:38.305 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pass            |   -   | [82.2, 73.9]    | -> Fabián Ruiz Pe |
|  +9.16 |  +9.15 | 00:35:39.111 | Paris Saint-Germai | Paris Saint-Germai | 47 | Ball Receipt*   |   -   | [80.1, 64.0]    |  |
|  +9.16 |  +9.15 | 00:35:39.111 | Paris Saint-Germai | Paris Saint-Germai | 47 | Pass            |   -   | [80.1, 64.0]    | -> Marcos Aoás Co |

---

### Disagreement Case 36: `3837954_p13_e5b0392c`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837954 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Angers
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 13
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:11:43.543) | **Initiation**: Pressure (00:11:43.558)
- **Initiation Delay**: 0.015s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 3.18s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 10.987s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.30 |  -1.31 | 00:11:42.247 | Paris Saint-Germai | Paris Saint-Germai | 13 | Pass            |   -   | [76.7, 52.4]    | Incomplete (Incomplete) |
|  -1.25 |  -1.27 | 00:11:42.288 | Angers             | Paris Saint-Germai | 13 | Pressure        |   -   | [43.4, 28.9]    |  |
|  +0.00 |  -0.01 | 00:11:43.543 | Paris Saint-Germai | Paris Saint-Germai | 13 | Ball Receipt*   |   -   | [80.0, 37.0]    | Incomplete |
|  +0.00 |  -0.01 | 00:11:43.543 | Angers             | Paris Saint-Germai | 13 | Ball Recovery   |   -   | [40.1, 44.3]    |  |
|  +0.00 |  -0.01 | 00:11:43.543 | Angers             | Paris Saint-Germai | 13 | Carry           |   -   | [40.1, 44.3]    |  |
|  +0.01 |  +0.00 | 00:11:43.558 | Paris Saint-Germai | Paris Saint-Germai | 13 | Pressure        |  Yes  | [79.3, 36.3]    |  |
|  +3.20 |  +3.18 | 00:11:46.738 | Angers             | Paris Saint-Germai | 13 | Pass            |   -   | [47.3, 54.1]    | -> Yan Valery |
|  +4.63 |  +4.61 | 00:11:48.170 | Angers             | Paris Saint-Germai | 13 | Ball Receipt*   |   -   | [39.2, 70.8]    |  |
|  +4.63 |  +4.61 | 00:11:48.170 | Angers             | Paris Saint-Germai | 13 | Carry           |   -   | [39.2, 70.8]    |  |
|  +6.32 |  +6.31 | 00:11:49.867 | Paris Saint-Germai | Paris Saint-Germai | 13 | Pressure        |  Yes  | [70.9, 3.4]     |  |
| +11.00 | +10.99 | 00:11:54.545 | Angers             | Paris Saint-Germai | 13 | Dispossessed    |   -   | [67.1, 79.2]    |  |
| +11.00 | +10.99 | 00:11:54.545 | Paris Saint-Germai | Paris Saint-Germai | 13 | Duel            |   -   | [53.0, 0.9]     | Tackle, Success Out |
| +15.08 | +15.07 | 00:11:58.625 | Paris Saint-Germai | Paris Saint-Germai | 14 | Pass            |   -   | [53.0, 0.1]     | -> Fabián Ruiz Pe |
| +16.34 | +16.32 | 00:11:59.879 | Paris Saint-Germai | Paris Saint-Germai | 14 | Ball Receipt*   |   -   | [52.0, 16.7]    |  |
| +20.52 | +20.50 | 00:12:04.060 | Paris Saint-Germai | Paris Saint-Germai | 14 | Pass            |   -   | [57.9, 31.2]    | -> Lionel Andrés  |
| +21.30 | +21.28 | 00:12:04.843 | Angers             | Paris Saint-Germai | 14 | Pressure        |   -   | [52.7, 36.4]    |  |
| +21.47 | +21.45 | 00:12:05.008 | Paris Saint-Germai | Paris Saint-Germai | 14 | Ball Receipt*   |   -   | [66.9, 44.7]    |  |

---

### Disagreement Case 37: `3893802_p184_0bdef800`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893802 (Women's World Cup, 2023)
- **counterpressing_team**: Colombia Women's
- **opponent_team_at_turnover**: Korea Republic Women's
- **possession_team_at_counterpress_initiation**: Colombia Women's
- **possession_id_at_counterpress_initiation**: 184
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:35:11.097) | **Initiation**: Duel (00:35:11.114)
- **Initiation Delay**: 0.017s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.421s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.938s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.45 |  -2.47 | 00:35:08.649 | Korea Republic Wom | Korea Republic Wom | 183 | Pass            |   -   | [69.1, 18.1]    | -> Eun-Sun Park |
|  -0.18 |  -0.20 | 00:35:10.914 | Colombia Women's   | Korea Republic Wom | 183 | Pressure        |   -   | [18.7, 39.7]    |  |
|  +0.00 |  -0.02 | 00:35:11.097 | Korea Republic Wom | Korea Republic Wom | 183 | Ball Receipt*   |   -   | [99.3, 40.2]    |  |
|  +0.00 |  -0.02 | 00:35:11.097 | Korea Republic Wom | Korea Republic Wom | 183 | Carry           |   -   | [99.3, 40.2]    |  |
|  +0.02 |  +0.00 | 00:35:11.114 | Korea Republic Wom | Korea Republic Wom | 183 | Dispossessed    |   -   | [99.7, 40.4]    |  |
|  +0.02 |  +0.00 | 00:35:11.114 | Colombia Women's   | Colombia Women's   | 184 | Duel            |  Yes  | [20.4, 39.7]    | Tackle, Success In Play |
|  +0.44 |  +0.42 | 00:35:11.535 | Korea Republic Wom | Colombia Women's   | 184 | Pressure        |  Yes  | [99.5, 31.0]    |  |
|  +0.98 |  +0.97 | 00:35:12.080 | Colombia Women's   | Colombia Women's   | 184 | Clearance       |   -   | [16.7, 45.3]    |  |
|  +4.37 |  +4.35 | 00:35:15.463 | Colombia Women's   | Colombia Women's   | 184 | Pressure        |  Yes  | [51.4, 59.2]    |  |
|  +4.49 |  +4.48 | 00:35:15.592 | Korea Republic Wom | Colombia Women's   | 184 | Pass            |   -   | [69.8, 17.1]    | Incomplete (Incomplete) |
|  +4.62 |  +4.61 | 00:35:15.721 | Colombia Women's   | Colombia Women's   | 184 | Block           |  Yes  | [51.6, 60.5]    |  |
|  +5.40 |  +5.38 | 00:35:16.499 | Korea Republic Wom | Colombia Women's   | 184 | Pressure        |   -   | [71.9, 20.3]    |  |
|  +5.95 |  +5.94 | 00:35:17.052 | Colombia Women's   | Colombia Women's   | 184 | Ball Recovery   |   -   | [47.1, 65.4]    |  |
|  +5.95 |  +5.94 | 00:35:17.052 | Colombia Women's   | Colombia Women's   | 184 | Carry           |   -   | [47.1, 65.4]    |  |
| +15.76 | +15.74 | 00:35:26.859 | Korea Republic Wom | Colombia Women's   | 184 | Pressure        |   -   | [17.4, 21.1]    |  |
| +16.20 | +16.19 | 00:35:27.300 | Colombia Women's   | Colombia Women's   | 184 | Pass            |   -   | [100.0, 59.0]   | -> Linda Lizeth C |
| +18.34 | +18.32 | 00:35:29.438 | Colombia Women's   | Colombia Women's   | 184 | Ball Receipt*   |   -   | [94.4, 27.1]    |  |

---

### Disagreement Case 38: `3998852_p40_f5a7c6e2`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3998852 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Switzerland Women's
- **opponent_team_at_turnover**: WNT Finland
- **possession_team_at_counterpress_initiation**: Switzerland Women's
- **possession_id_at_counterpress_initiation**: 40
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:15:13.004) | **Initiation**: Pressure (00:15:13.023)
- **Initiation Delay**: 0.019s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.553s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.02 |  -3.04 | 00:15:09.987 | Switzerland Women' | Switzerland Women' | 40 | Ball Receipt*   |   -   | [63.5, 34.6]    |  |
|  -3.02 |  -3.04 | 00:15:09.987 | Switzerland Women' | Switzerland Women' | 40 | Carry           |   -   | [63.5, 34.6]    |  |
|  -2.75 |  -2.77 | 00:15:10.251 | Switzerland Women' | Switzerland Women' | 40 | Pass            |   -   | [63.5, 34.6]    | Incomplete (Incomplete) |
|  +0.00 |  -0.02 | 00:15:13.004 | WNT Finland        | Switzerland Women' | 40 | Ball Recovery   |   -   | [49.4, 67.5]    |  |
|  +0.00 |  -0.02 | 00:15:13.004 | WNT Finland        | Switzerland Women' | 40 | Carry           |   -   | [49.4, 67.5]    |  |
|  +0.02 |  +0.00 | 00:15:13.023 | Switzerland Women' | Switzerland Women' | 40 | Pressure        |  Yes  | [68.6, 14.4]    |  |
|  +1.57 |  +1.55 | 00:15:14.576 | Switzerland Women' | Switzerland Women' | 40 | Foul Committed  |  Yes  | [75.6, 10.4]    |  |
|  +1.57 |  +1.55 | 00:15:14.576 | WNT Finland        | Switzerland Women' | 40 | Foul Won        |   -   | [44.5, 69.7]    |  |
| +21.42 | +21.41 | 00:15:34.429 | WNT Finland        | WNT Finland        | 41 | Pass            |   -   | [45.2, 66.8]    | Incomplete (Incomplete) |
| +25.72 | +25.70 | 00:15:38.724 | WNT Finland        | WNT Finland        | 41 | Pressure        |   -   | [97.9, 19.5]    |  |
| +26.35 | +26.33 | 00:15:39.358 | Switzerland Women' | Switzerland Women' | 42 | Pass            |   -   | [17.0, 58.9]    | -> Livia Peng |
| +28.19 | +28.17 | 00:15:41.195 | WNT Finland        | Switzerland Women' | 42 | Pressure        |  Yes  | [106.9, 32.1]   |  |
| +28.43 | +28.41 | 00:15:41.435 | Switzerland Women' | Switzerland Women' | 42 | Ball Receipt*   |   -   | [3.0, 50.3]     |  |
| +28.43 | +28.41 | 00:15:41.435 | Switzerland Women' | Switzerland Women' | 42 | Pass            |   -   | [2.3, 50.6]     | Incomplete (Incomplete) |
| +31.66 | +31.64 | 00:15:44.667 | WNT Finland        | Switzerland Women' | 42 | Pass            |   -   | [64.4, 29.8]    | Incomplete (Incomplete) |
| +32.70 | +32.68 | 00:15:45.702 | WNT Finland        | Switzerland Women' | 42 | Pressure        |   -   | [77.5, 37.1]    |  |
| +32.96 | +32.94 | 00:15:45.961 | Switzerland Women' | Switzerland Women' | 42 | Pass            |   -   | [43.2, 45.9]    | -> Sydney Scherte |

---

### Disagreement Case 39: `3837727_p60_ff8b6cf2`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3837727 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: OGC Nice
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 60
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:40:20.466) | **Initiation**: Pressure (00:40:20.489)
- **Initiation Delay**: 0.023s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.06s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 11.803s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.27 |  -1.29 | 00:40:19.195 | Paris Saint-Germai | Paris Saint-Germai | 60 | Ball Receipt*   |   -   | [70.9, 71.8]    |  |
|  -1.27 |  -1.29 | 00:40:19.195 | Paris Saint-Germai | Paris Saint-Germai | 60 | Carry           |   -   | [70.9, 71.8]    |  |
|  -1.22 |  -1.24 | 00:40:19.248 | Paris Saint-Germai | Paris Saint-Germai | 60 | Miscontrol      |   -   | [70.9, 71.8]    |  |
|  +0.00 |  -0.02 | 00:40:20.466 | OGC Nice           | Paris Saint-Germai | 60 | Ball Recovery   |   -   | [50.7, 7.4]     |  |
|  +0.00 |  -0.02 | 00:40:20.466 | OGC Nice           | Paris Saint-Germai | 60 | Carry           |   -   | [50.7, 7.4]     |  |
|  +0.02 |  +0.00 | 00:40:20.489 | Paris Saint-Germai | Paris Saint-Germai | 60 | Pressure        |  Yes  | [74.7, 72.9]    |  |
|  +1.08 |  +1.06 | 00:40:21.549 | Paris Saint-Germai | Paris Saint-Germai | 60 | Pressure        |  Yes  | [70.6, 70.1]    |  |
|  +1.44 |  +1.41 | 00:40:21.903 | OGC Nice           | Paris Saint-Germai | 60 | Pass            |   -   | [45.7, 14.8]    | -> Aaron Ramsey |
|  +2.28 |  +2.25 | 00:40:22.743 | OGC Nice           | Paris Saint-Germai | 60 | Ball Receipt*   |   -   | [51.7, 24.5]    |  |
|  +2.28 |  +2.25 | 00:40:22.743 | OGC Nice           | Paris Saint-Germai | 60 | Carry           |   -   | [51.7, 24.5]    |  |
|  +5.81 |  +5.79 | 00:40:26.280 | OGC Nice           | Paris Saint-Germai | 60 | Pass            |   -   | [75.0, 22.8]    | Incomplete (Out) |
|  +8.02 |  +8.00 | 00:40:28.489 | OGC Nice           | Paris Saint-Germai | 60 | Ball Receipt*   |   -   | [86.8, 3.6]     | Incomplete |
| +11.83 | +11.80 | 00:40:32.292 | Paris Saint-Germai | Paris Saint-Germai | 61 | Pass            |   -   | [17.5, 80.0]    | -> Gianluigi Donn |
| +14.17 | +14.15 | 00:40:34.637 | Paris Saint-Germai | Paris Saint-Germai | 61 | Ball Receipt*   |   -   | [8.4, 52.1]     |  |
| +15.82 | +15.80 | 00:40:36.288 | Paris Saint-Germai | Paris Saint-Germai | 61 | Pass            |   -   | [10.3, 46.4]    | -> Marcos Aoás Co |
| +17.22 | +17.20 | 00:40:37.690 | Paris Saint-Germai | Paris Saint-Germai | 61 | Ball Receipt*   |   -   | [15.8, 43.0]    |  |
| +17.22 | +17.20 | 00:40:37.690 | Paris Saint-Germai | Paris Saint-Germai | 61 | Carry           |   -   | [15.8, 43.0]    |  |

---

### Disagreement Case 40: `3895244_p146_f4a67886`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3895244 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: FC Heidenheim
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: FC Heidenheim
- **possession_id_at_counterpress_initiation**: 146
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:24:25.823) | **Initiation**: Pressure (00:24:25.850)
- **Initiation Delay**: 0.027s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.631s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 13.38s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.74 |  -0.77 | 00:24:25.084 | FC Heidenheim      | FC Heidenheim      | 146 | Pass            |   -   | [115.2, 23.8]   | Incomplete (Incomplete) |
|  -0.65 |  -0.68 | 00:24:25.171 | Bayer Leverkusen   | FC Heidenheim      | 146 | Block           |   -   | [4.9, 54.4]     |  |
|  -0.62 |  -0.65 | 00:24:25.203 | FC Heidenheim      | FC Heidenheim      | 146 | Block           |   -   | [115.2, 25.7]   |  |
|  +0.00 |  -0.03 | 00:24:25.823 | Bayer Leverkusen   | FC Heidenheim      | 146 | Ball Recovery   |   -   | [4.9, 54.4]     |  |
|  +0.00 |  -0.03 | 00:24:25.823 | Bayer Leverkusen   | FC Heidenheim      | 146 | Carry           |   -   | [4.9, 54.4]     |  |
|  +0.03 |  +0.00 | 00:24:25.850 | FC Heidenheim      | FC Heidenheim      | 146 | Pressure        |  Yes  | [117.0, 25.7]   |  |
|  +1.66 |  +1.63 | 00:24:27.481 | Bayer Leverkusen   | FC Heidenheim      | 146 | Pass            |   -   | [2.4, 56.0]     | Incomplete (Out) |
| +13.41 | +13.38 | 00:24:39.230 | FC Heidenheim      | FC Heidenheim      | 147 | Pass            |   -   | [102.8, 0.1]    | -> Kevin Sessa |
| +14.49 | +14.47 | 00:24:40.317 | Bayer Leverkusen   | FC Heidenheim      | 147 | Pressure        |   -   | [3.5, 69.1]     |  |
| +14.56 | +14.54 | 00:24:40.388 | FC Heidenheim      | FC Heidenheim      | 147 | Ball Receipt*   |   -   | [116.1, 11.2]   |  |
| +14.56 | +14.54 | 00:24:40.388 | FC Heidenheim      | FC Heidenheim      | 147 | Carry           |   -   | [116.1, 11.2]   |  |
| +15.04 | +15.01 | 00:24:40.862 | FC Heidenheim      | FC Heidenheim      | 147 | Pass            |   -   | [120.0, 11.6]   | -> Jonas Föhrenba |
| +15.85 | +15.82 | 00:24:41.671 | FC Heidenheim      | FC Heidenheim      | 147 | Ball Receipt*   |   -   | [117.0, 5.7]    |  |
| +15.85 | +15.82 | 00:24:41.671 | FC Heidenheim      | FC Heidenheim      | 147 | Carry           |   -   | [117.0, 5.7]    |  |
| +16.62 | +16.60 | 00:24:42.446 | FC Heidenheim      | FC Heidenheim      | 147 | Pass            |   -   | [117.0, 5.7]    | -> Jan-Niklas Bes |
| +17.06 | +17.03 | 00:24:42.880 | Bayer Leverkusen   | FC Heidenheim      | 147 | Pressure        |   -   | [9.1, 65.5]     |  |
| +17.32 | +17.29 | 00:24:43.144 | FC Heidenheim      | FC Heidenheim      | 147 | Ball Receipt*   |   -   | [111.0, 12.8]   |  |

---

### Disagreement Case 41: `3835329_p118_91f1c040`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3835329 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Denmark Women's
- **opponent_team_at_turnover**: WNT Finland
- **possession_team_at_counterpress_initiation**: Denmark Women's
- **possession_id_at_counterpress_initiation**: 118
- **Turnover Context**: open_play (Origin: From Free Kick)
- **Turnover**: Interception (00:09:08.663) | **Initiation**: Pressure (00:09:08.690)
- **Initiation Delay**: 0.027s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 2.399s) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -5.01 |  -5.04 | 00:09:03.654 | Denmark Women's    | Denmark Women's    | 118 | Carry           |   -   | [54.6, 58.2]    |  |
|  -3.44 |  -3.46 | 00:09:05.228 | Denmark Women's    | Denmark Women's    | 118 | Pass            |   -   | [56.4, 58.2]    | Incomplete (Incomplete) |
|  +0.00 |  -0.03 | 00:09:08.663 | Denmark Women's    | Denmark Women's    | 118 | Ball Receipt*   |   -   | [100.4, 66.4]   | Incomplete |
|  +0.00 |  -0.03 | 00:09:08.663 | WNT Finland        | Denmark Women's    | 118 | Interception    |   -   | [18.0, 14.1]    | Won |
|  +0.00 |  -0.03 | 00:09:08.663 | WNT Finland        | Denmark Women's    | 118 | Carry           |   -   | [18.0, 14.1]    |  |
|  +0.03 |  +0.00 | 00:09:08.690 | Denmark Women's    | Denmark Women's    | 118 | Pressure        |  Yes  | [101.4, 67.4]   |  |
|  +2.43 |  +2.40 | 00:09:11.089 | WNT Finland        | Denmark Women's    | 118 | Pass            |   -   | [13.7, 3.8]     | Incomplete (Incomplete) |
|  +2.65 |  +2.62 | 00:09:11.315 | Denmark Women's    | Denmark Women's    | 118 | Block           |  Yes  | [104.1, 75.7]   |  |
|  +5.76 |  +5.73 | 00:09:14.423 | Denmark Women's    | Denmark Women's    | 118 | Pressure        |   -   | [116.9, 72.2]   |  |
|  +6.31 |  +6.29 | 00:09:14.977 | WNT Finland        | Denmark Women's    | 118 | Shield          |   -   | [2.2, 7.9]      |  |
| +41.78 | +41.75 | 00:09:50.441 | WNT Finland        | WNT Finland        | 119 | Pass            |   -   | [6.0, 36.0]     | Incomplete (Incomplete) |
| +43.98 | +43.95 | 00:09:52.644 | WNT Finland        | WNT Finland        | 119 | Ball Receipt*   |   -   | [47.9, 12.3]    | Incomplete |
| +43.98 | +43.95 | 00:09:52.644 | WNT Finland        | WNT Finland        | 119 | Duel            |   -   | [49.6, 10.9]    | Aerial Lost |
| +43.98 | +43.95 | 00:09:52.644 | Denmark Women's    | Denmark Women's    | 120 | Pass            |   -   | [70.5, 69.2]    | -> Rikke Læntver  |
| +46.23 | +46.20 | 00:09:54.889 | Denmark Women's    | Denmark Women's    | 120 | Ball Receipt*   |   -   | [56.6, 77.7]    |  |
| +46.23 | +46.20 | 00:09:54.889 | Denmark Women's    | Denmark Women's    | 120 | Pass            |   -   | [56.6, 77.7]    | -> Signe Kallesøe |
| +47.99 | +47.96 | 00:09:56.651 | Denmark Women's    | Denmark Women's    | 120 | Ball Receipt*   |   -   | [76.7, 60.5]    |  |

---

### Disagreement Case 42: `3906390_p36_dbe91784`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3906390 (Women's World Cup, 2023)
- **counterpressing_team**: England Women's
- **opponent_team_at_turnover**: Spain Women's
- **possession_team_at_counterpress_initiation**: England Women's
- **possession_id_at_counterpress_initiation**: 36
- **Turnover Context**: open_play (Origin: From Goal Kick)
- **Turnover**: Ball Recovery (00:14:03.159) | **Initiation**: Pressure (00:14:03.190)
- **Initiation Delay**: 0.031s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.447s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.61 |  -1.64 | 00:14:01.548 | Spain Women's      | England Women's    | 36 | Pressure        |   -   | [66.9, 4.9]     |  |
|  -1.50 |  -1.53 | 00:14:01.662 | England Women's    | England Women's    | 36 | Ball Receipt*   |   -   | [52.7, 75.0]    |  |
|  -1.50 |  -1.53 | 00:14:01.662 | England Women's    | England Women's    | 36 | Miscontrol      |   -   | [53.0, 76.8]    |  |
|  +0.00 |  -0.03 | 00:14:03.159 | Spain Women's      | England Women's    | 36 | Ball Recovery   |   -   | [71.1, 1.4]     |  |
|  +0.00 |  -0.03 | 00:14:03.159 | Spain Women's      | England Women's    | 36 | Carry           |   -   | [71.1, 1.4]     |  |
|  +0.03 |  +0.00 | 00:14:03.190 | England Women's    | England Women's    | 36 | Pressure        |  Yes  | [49.5, 78.1]    |  |
|  +1.48 |  +1.45 | 00:14:04.637 | England Women's    | England Women's    | 36 | Foul Committed  |  Yes  | [46.9, 78.7]    |  |
|  +1.48 |  +1.45 | 00:14:04.637 | Spain Women's      | England Women's    | 36 | Foul Won        |   -   | [73.2, 1.4]     |  |
| +16.84 | +16.81 | 00:14:20.000 | Spain Women's      | Spain Women's      | 37 | Pass            |   -   | [73.2, 0.6]     | -> Jennifer Hermo |
| +17.96 | +17.93 | 00:14:21.116 | Spain Women's      | Spain Women's      | 37 | Ball Receipt*   |   -   | [76.1, 7.0]     |  |
| +20.42 | +20.39 | 00:14:23.583 | Spain Women's      | Spain Women's      | 37 | Pass            |   -   | [72.0, 7.8]     | Incomplete (Incomplete) |
| +23.12 | +23.09 | 00:14:26.278 | Spain Women's      | Spain Women's      | 37 | Ball Receipt*   |   -   | [89.6, 29.0]    | Incomplete |
| +23.12 | +23.09 | 00:14:26.278 | England Women's    | England Women's    | 38 | Pass            |   -   | [30.7, 47.3]    | -> Keira Walsh |
| +23.72 | +23.69 | 00:14:26.877 | England Women's    | England Women's    | 38 | Ball Receipt*   |   -   | [35.7, 41.0]    |  |
| +23.72 | +23.69 | 00:14:26.877 | England Women's    | England Women's    | 38 | Carry           |   -   | [35.7, 41.0]    |  |
| +23.85 | +23.81 | 00:14:27.005 | Spain Women's      | England Women's    | 38 | Pressure        |  Yes  | [84.4, 38.8]    |  |
| +24.54 | +24.51 | 00:14:27.701 | Spain Women's      | England Women's    | 38 | Foul Committed  |  Yes  | [87.2, 38.5]    |  |

---

### Disagreement Case 43: `3930160_p122_35ffe2d1`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3930160 (UEFA Euro, 2024)
- **counterpressing_team**: Croatia
- **opponent_team_at_turnover**: Spain
- **possession_team_at_counterpress_initiation**: Croatia
- **possession_id_at_counterpress_initiation**: 122
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:20:52.096) | **Initiation**: Dribbled Past (00:20:52.131)
- **Initiation Delay**: 0.035s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.0s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.421s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.16 |  -2.20 | 00:20:49.933 | Spain              | Croatia            | 122 | Pressure        |   -   | [12.7, 58.8]    |  |
|  -1.83 |  -1.86 | 00:20:50.270 | Croatia            | Croatia            | 122 | Pass            |   -   | [109.4, 19.5]   | Incomplete (Incomplete) |
|  -0.23 |  -0.26 | 00:20:51.870 | Croatia            | Croatia            | 122 | Pressure        |   -   | [94.2, 21.9]    |  |
|  +0.00 |  -0.04 | 00:20:52.096 | Spain              | Croatia            | 122 | Ball Recovery   |   -   | [22.6, 56.7]    |  |
|  +0.00 |  -0.04 | 00:20:52.096 | Spain              | Croatia            | 122 | Carry           |   -   | [22.6, 56.7]    |  |
|  +0.04 |  +0.00 | 00:20:52.131 | Croatia            | Croatia            | 122 | Dribbled Past   |  Yes  | [95.8, 22.9]    |  |
|  +0.04 |  +0.00 | 00:20:52.131 | Spain              | Croatia            | 122 | Dribble         |   -   | [24.3, 57.2]    |  |
|  +0.04 |  +0.00 | 00:20:52.131 | Spain              | Croatia            | 122 | Carry           |   -   | [24.3, 57.2]    |  |
|  +1.53 |  +1.50 | 00:20:53.628 | Spain              | Croatia            | 122 | Pass            |   -   | [27.2, 53.4]    | Incomplete (Incomplete) |
|  +6.46 |  +6.42 | 00:20:58.552 | Spain              | Croatia            | 122 | Ball Receipt*   |   -   | [38.0, 71.8]    | Incomplete |
|  +6.46 |  +6.42 | 00:20:58.552 | Croatia            | Croatia            | 122 | Ball Recovery   |   -   | [46.8, 3.3]     |  |
|  +6.46 |  +6.42 | 00:20:58.552 | Croatia            | Croatia            | 122 | Carry           |   -   | [46.8, 3.3]     |  |
|  +8.64 |  +8.61 | 00:21:00.738 | Croatia            | Croatia            | 122 | Pass            |   -   | [48.3, 11.6]    | -> Marcelo Brozov |
| +10.18 | +10.14 | 00:21:02.275 | Croatia            | Croatia            | 122 | Ball Receipt*   |   -   | [55.4, 25.7]    |  |
| +10.18 | +10.14 | 00:21:02.275 | Croatia            | Croatia            | 122 | Carry           |   -   | [55.4, 25.7]    |  |
| +11.23 | +11.19 | 00:21:03.324 | Croatia            | Croatia            | 122 | Pass            |   -   | [56.0, 26.0]    | -> Joško Gvardiol |
| +12.54 | +12.50 | 00:21:04.635 | Spain              | Croatia            | 122 | Pressure        |   -   | [48.8, 65.2]    |  |

---

### Disagreement Case 44: `3795109_p134_5bb1f604`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3795109 (UEFA Euro, 2020)
- **counterpressing_team**: Denmark
- **opponent_team_at_turnover**: Czech Republic
- **possession_team_at_counterpress_initiation**: Denmark
- **possession_id_at_counterpress_initiation**: 134
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:24:11.298) | **Initiation**: Pressure (00:24:11.333)
- **Initiation Delay**: 0.035s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.813s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.16 |  -1.20 | 00:24:10.133 | Denmark            | Denmark            | 134 | Pass            |   -   | [30.9, 2.1]     | -> Thomas Delaney |
|  -0.97 |  -1.00 | 00:24:10.330 | Denmark            | Denmark            | 134 | Ball Receipt*   |   -   | [34.1, 5.4]     |  |
|  -0.97 |  -1.00 | 00:24:10.330 | Denmark            | Denmark            | 134 | Miscontrol      |   -   | [34.1, 5.4]     |  |
|  +0.00 |  -0.04 | 00:24:11.298 | Czech Republic     | Denmark            | 134 | Ball Recovery   |   -   | [83.0, 74.7]    |  |
|  +0.00 |  -0.04 | 00:24:11.298 | Czech Republic     | Denmark            | 134 | Carry           |   -   | [83.0, 74.7]    |  |
|  +0.04 |  +0.00 | 00:24:11.333 | Denmark            | Denmark            | 134 | Pressure        |  Yes  | [34.6, 10.0]    |  |
|  +0.85 |  +0.81 | 00:24:12.146 | Denmark            | Denmark            | 134 | Dribbled Past   |  Yes  | [35.0, 10.2]    |  |
|  +0.85 |  +0.81 | 00:24:12.146 | Czech Republic     | Denmark            | 134 | Dribble         |   -   | [85.1, 69.9]    |  |
|  +0.85 |  +0.81 | 00:24:12.146 | Czech Republic     | Denmark            | 134 | Carry           |   -   | [85.1, 69.9]    |  |
|  +4.00 |  +3.96 | 00:24:15.297 | Czech Republic     | Denmark            | 134 | Pass            |   -   | [99.5, 55.8]    | -> Michael Krmenč |
|  +4.48 |  +4.44 | 00:24:15.778 | Czech Republic     | Denmark            | 134 | Ball Receipt*   |   -   | [105.8, 60.7]   |  |
|  +4.48 |  +4.44 | 00:24:15.778 | Czech Republic     | Denmark            | 134 | Carry           |   -   | [105.8, 60.7]   |  |
|  +4.52 |  +4.48 | 00:24:15.818 | Czech Republic     | Denmark            | 134 | Miscontrol      |   -   | [106.1, 60.5]   |  |
| +50.66 | +50.62 | 00:25:01.956 | Denmark            | Denmark            | 134 | Substitution    |   -   | -               |  |
| +61.28 | +61.24 | 00:25:12.574 | Denmark            | Denmark            | 135 | Pass            |   -   | [6.0, 36.0]     | -> Yussuf Yurary  |
| +64.78 | +64.74 | 00:25:16.076 | Denmark            | Denmark            | 135 | Ball Receipt*   |   -   | [77.2, 15.7]    |  |
| +64.78 | +64.74 | 00:25:16.076 | Denmark            | Denmark            | 135 | Pass            |   -   | [77.2, 15.7]    | Incomplete (Incomplete) |

---

### Disagreement Case 45: `3788759_p85_14ea8c61`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3788759 (UEFA Euro, 2020)
- **counterpressing_team**: Scotland
- **opponent_team_at_turnover**: England
- **possession_team_at_counterpress_initiation**: Scotland
- **possession_id_at_counterpress_initiation**: 85
- **Turnover Context**: open_play (Origin: From Goal Kick)
- **Turnover**: Ball Recovery (00:11:09.264) | **Initiation**: Foul Committed (00:11:09.304)
- **Initiation Delay**: 0.04s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.0s) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.81 |  -1.85 | 00:11:07.457 | England            | Scotland           | 85 | Block           |   -   | [11.9, 39.3]    |  |
|  -1.73 |  -1.77 | 00:11:07.537 | England            | Scotland           | 85 | Goal Keeper     |   -   | [4.2, 40.5]     |  |
|  -0.53 |  -0.57 | 00:11:08.732 | Scotland           | Scotland           | 85 | Pressure        |   -   | [100.3, 28.3]   |  |
|  +0.00 |  -0.04 | 00:11:09.264 | England            | Scotland           | 85 | Ball Recovery   |   -   | [19.5, 53.3]    |  |
|  +0.00 |  -0.04 | 00:11:09.264 | England            | Scotland           | 85 | Carry           |   -   | [19.5, 53.3]    |  |
|  +0.04 |  +0.00 | 00:11:09.304 | Scotland           | Scotland           | 85 | Foul Committed  |  Yes  | [101.7, 30.1]   |  |
|  +0.04 |  +0.00 | 00:11:09.304 | England            | Scotland           | 85 | Foul Won        |   -   | [18.4, 50.0]    |  |
|  +0.04 |  +0.00 | 00:11:09.304 | England            | Scotland           | 85 | Carry           |   -   | [18.4, 50.0]    |  |
|  +2.84 |  +2.80 | 00:11:12.108 | Scotland           | Scotland           | 85 | Pressure        |  Yes  | [84.3, 40.4]    |  |
|  +3.55 |  +3.51 | 00:11:12.814 | Scotland           | Scotland           | 85 | Dribbled Past   |  Yes  | [81.4, 40.8]    |  |
|  +3.55 |  +3.51 | 00:11:12.814 | England            | Scotland           | 85 | Dribble         |   -   | [38.7, 39.3]    |  |
|  +3.55 |  +3.51 | 00:11:12.814 | England            | Scotland           | 85 | Carry           |   -   | [38.7, 39.3]    |  |
|  +4.26 |  +4.22 | 00:11:13.524 | England            | Scotland           | 85 | Pass            |   -   | [38.7, 39.3]    | -> Harry Kane |
|  +5.86 |  +5.82 | 00:11:15.126 | England            | Scotland           | 85 | Ball Receipt*   |   -   | [61.7, 18.1]    |  |
|  +5.86 |  +5.82 | 00:11:15.126 | England            | Scotland           | 85 | Carry           |   -   | [61.7, 18.1]    |  |
|  +7.60 |  +7.56 | 00:11:16.860 | Scotland           | Scotland           | 85 | Pressure        |  Yes  | [52.3, 64.4]    |  |
|  +9.04 |  +9.00 | 00:11:18.300 | Scotland           | Scotland           | 85 | Foul Committed  |  Yes  | [40.1, 62.0]    |  |
|  +9.04 |  +9.00 | 00:11:18.300 | England            | Scotland           | 85 | Foul Won        |   -   | [80.0, 18.1]    |  |

---

### Disagreement Case 46: `3893834_p100_dc3f7461`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3893834 (Women's World Cup, 2023)
- **counterpressing_team**: Colombia Women's
- **opponent_team_at_turnover**: Morocco Women's
- **possession_team_at_counterpress_initiation**: Colombia Women's
- **possession_id_at_counterpress_initiation**: 100
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Shot (00:48:40.262) | **Initiation**: Pressure (00:48:40.302)
- **Initiation Delay**: 0.04s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.248s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.09 |  -1.13 | 00:48:39.168 | Colombia Women's   | Morocco Women's    | 99 | Pressure        |   -   | [5.7, 34.7]     |  |
|  -1.05 |  -1.09 | 00:48:39.210 | Morocco Women's    | Morocco Women's    | 99 | Pass            |   -   | [116.0, 48.5]   | -> Anissa Lahmari |
|  -0.93 |  -0.97 | 00:48:39.328 | Morocco Women's    | Morocco Women's    | 99 | Ball Receipt*   |   -   | [117.1, 44.1]   |  |
|  -0.93 |  -0.97 | 00:48:39.328 | Colombia Women's   | Morocco Women's    | 99 | Block           |   -   | [4.6, 33.0]     |  |
|  +0.00 |  -0.04 | 00:48:40.262 | Morocco Women's    | Morocco Women's    | 99 | Shot            |   -   | [116.6, 41.2]   | Goal |
|  +0.04 |  +0.00 | 00:48:40.302 | Colombia Women's   | Colombia Women's   | 100 | Pressure        |  Yes  | [2.9, 39.4]     |  |
|  +0.29 |  +0.25 | 00:48:40.550 | Colombia Women's   | Colombia Women's   | 100 | Goal Keeper     |   -   | [3.6, 32.0]     |  |
| +95.00 | +94.96 | 00:50:15.260 | Colombia Women's   | Colombia Women's   | 101 | Pass            |   -   | [60.0, 40.0]    | -> María Catalina |
| +97.51 | +97.47 | 00:50:17.777 | Colombia Women's   | Colombia Women's   | 101 | Ball Receipt*   |   -   | [49.8, 38.8]    |  |
| +97.64 | +97.60 | 00:50:17.898 | Morocco Women's    | Colombia Women's   | 101 | Pressure        |   -   | [62.4, 41.5]    |  |
| +98.23 | +98.19 | 00:50:18.491 | Colombia Women's   | Colombia Women's   | 101 | Pass            |   -   | [56.9, 43.8]    | -> Linda Lizeth C |
| +99.96 | +99.92 | 00:50:20.225 | Colombia Women's   | Colombia Women's   | 101 | Ball Receipt*   |   -   | [74.4, 73.8]    |  |
| +99.96 | +99.92 | 00:50:20.225 | Colombia Women's   | Colombia Women's   | 101 | Carry           |   -   | [74.4, 73.8]    |  |
| +101.95 | +101.91 | 00:50:22.208 | Colombia Women's   | Colombia Women's   | 101 | Pass            |   -   | [67.7, 73.8]    | -> Jorelyn Andrea |
| +103.82 | +103.78 | 00:50:24.083 | Colombia Women's   | Colombia Women's   | 101 | Ball Receipt*   |   -   | [44.8, 72.7]    |  |
| +103.82 | +103.78 | 00:50:24.083 | Colombia Women's   | Colombia Women's   | 101 | Carry           |   -   | [44.8, 72.7]    |  |
| +105.62 | +105.59 | 00:50:25.887 | Colombia Women's   | Colombia Women's   | 101 | Pass            |   -   | [44.8, 73.5]    | Incomplete (Incomplete) |

---

### Disagreement Case 47: `3869219_p28_e66a8bc8`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3869219 (FIFA World Cup, 2022)
- **counterpressing_team**: Japan
- **opponent_team_at_turnover**: Croatia
- **possession_team_at_counterpress_initiation**: Japan
- **possession_id_at_counterpress_initiation**: 28
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:19:16.193) | **Initiation**: Pressure (00:19:16.236)
- **Initiation Delay**: 0.043s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 0.436s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 7.981s) | Evidence: `new_possession_completed_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.92 |  -3.97 | 00:19:12.270 | Croatia            | Japan              | 28 | Block           |   -   | [74.9, 18.5]    |  |
|  -2.47 |  -2.51 | 00:19:13.726 | Japan              | Japan              | 28 | Pass            |   -   | [42.9, 47.1]    | Incomplete (Incomplete) |
|  +0.00 |  -0.04 | 00:19:16.193 | Japan              | Japan              | 28 | Ball Receipt*   |   -   | [55.2, 40.2]    | Incomplete |
|  +0.00 |  -0.04 | 00:19:16.193 | Croatia            | Japan              | 28 | Ball Recovery   |   -   | [61.5, 41.2]    |  |
|  +0.00 |  -0.04 | 00:19:16.193 | Croatia            | Japan              | 28 | Carry           |   -   | [61.5, 41.2]    |  |
|  +0.04 |  +0.00 | 00:19:16.236 | Japan              | Japan              | 28 | Pressure        |  Yes  | [61.9, 40.5]    |  |
|  +0.48 |  +0.44 | 00:19:16.672 | Croatia            | Japan              | 28 | Pass            |   -   | [58.0, 44.1]    | Incomplete (Out) |
|  +8.02 |  +7.98 | 00:19:24.217 | Japan              | Japan              | 29 | Pass            |   -   | [68.2, 0.1]     | -> Shogo Taniguch |
|  +9.74 |  +9.69 | 00:19:25.928 | Japan              | Japan              | 29 | Ball Receipt*   |   -   | [49.4, 7.1]     |  |
|  +9.74 |  +9.69 | 00:19:25.928 | Japan              | Japan              | 29 | Carry           |   -   | [49.4, 7.1]     |  |
| +12.21 | +12.17 | 00:19:28.408 | Japan              | Japan              | 29 | Pass            |   -   | [48.3, 11.1]    | -> Takehiro Tomiy |
| +16.42 | +16.38 | 00:19:32.616 | Japan              | Japan              | 29 | Ball Receipt*   |   -   | [63.4, 78.0]    |  |
| +16.42 | +16.38 | 00:19:32.616 | Japan              | Japan              | 29 | Carry           |   -   | [63.4, 78.0]    |  |
| +16.58 | +16.54 | 00:19:32.776 | Japan              | Japan              | 29 | Pass            |   -   | [63.4, 78.0]    | -> Junya Ito |
| +17.65 | +17.61 | 00:19:33.843 | Japan              | Japan              | 29 | Ball Receipt*   |   -   | [85.9, 77.0]    |  |
| +17.65 | +17.61 | 00:19:33.843 | Japan              | Japan              | 29 | Carry           |   -   | [85.9, 77.0]    |  |
| +21.16 | +21.12 | 00:19:37.352 | Japan              | Japan              | 29 | Pass            |   -   | [109.4, 74.0]   | Incomplete (Incomplete) |

---

### Disagreement Case 48: `3942382_p37_59730dd8`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3942382 (UEFA Euro, 2024)
- **counterpressing_team**: Netherlands
- **opponent_team_at_turnover**: Turkey
- **possession_team_at_counterpress_initiation**: Netherlands
- **possession_id_at_counterpress_initiation**: 37
- **Turnover Context**: open_play (Origin: From Goal Kick)
- **Turnover**: Ball Recovery (00:29:14.424) | **Initiation**: Pressure (00:29:14.471)
- **Initiation Delay**: 0.047s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 2.208s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 7.954s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.87 |  -1.92 | 00:29:12.552 | Netherlands        | Netherlands        | 37 | Carry           |   -   | [14.3, 28.7]    |  |
|  -1.30 |  -1.35 | 00:29:13.120 | Turkey             | Netherlands        | 37 | Pressure        |   -   | [110.4, 52.6]   |  |
|  -0.56 |  -0.61 | 00:29:13.862 | Netherlands        | Netherlands        | 37 | Miscontrol      |   -   | [11.1, 27.2]    |  |
|  +0.00 |  -0.05 | 00:29:14.424 | Turkey             | Netherlands        | 37 | Ball Recovery   |   -   | [109.4, 53.3]   |  |
|  +0.00 |  -0.05 | 00:29:14.424 | Turkey             | Netherlands        | 37 | Carry           |   -   | [109.4, 53.3]   |  |
|  +0.05 |  +0.00 | 00:29:14.471 | Netherlands        | Netherlands        | 37 | Pressure        |  Yes  | [9.1, 27.3]     |  |
|  +2.26 |  +2.21 | 00:29:16.679 | Turkey             | Netherlands        | 37 | Pass            |   -   | [110.9, 54.8]   | -> Arda Güler |
|  +2.60 |  +2.56 | 00:29:17.028 | Turkey             | Netherlands        | 37 | Ball Receipt*   |   -   | [106.1, 57.1]   |  |
|  +2.60 |  +2.56 | 00:29:17.028 | Turkey             | Netherlands        | 37 | Carry           |   -   | [106.1, 57.1]   |  |
|  +5.52 |  +5.47 | 00:29:19.939 | Turkey             | Netherlands        | 37 | Pass            |   -   | [98.5, 59.5]    | Incomplete (Incomplete) |
|  +5.73 |  +5.68 | 00:29:20.156 | Turkey             | Netherlands        | 37 | Ball Receipt*   |   -   | [106.6, 46.5]   | Incomplete |
|  +5.73 |  +5.68 | 00:29:20.156 | Netherlands        | Netherlands        | 37 | Block           |  Yes  | [20.0, 23.5]    |  |
|  +8.00 |  +7.95 | 00:29:22.425 | Netherlands        | Netherlands        | 37 | Ball Recovery   |   -   | [29.8, 16.4]    |  |
|  +8.00 |  +7.95 | 00:29:22.425 | Netherlands        | Netherlands        | 37 | Carry           |   -   | [29.8, 16.4]    |  |
|  +8.91 |  +8.86 | 00:29:23.334 | Turkey             | Netherlands        | 37 | Pressure        |   -   | [90.6, 64.6]    |  |
|  +9.59 |  +9.54 | 00:29:24.011 | Netherlands        | Netherlands        | 37 | Dribble         |   -   | [32.0, 14.9]    |  |
|  +9.59 |  +9.54 | 00:29:24.011 | Turkey             | Turkey             | 38 | Duel            |  Yes  | [88.1, 65.2]    | Tackle, Success In Play |

---

### Disagreement Case 49: `3835322_p117_0f5aff36`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3835322 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Denmark Women's
- **opponent_team_at_turnover**: Germany Women's
- **possession_team_at_counterpress_initiation**: Denmark Women's
- **possession_id_at_counterpress_initiation**: 117
- **Turnover Context**: open_play (Origin: From Free Kick)
- **Turnover**: Interception (00:06:06.585) | **Initiation**: Pressure (00:06:06.632)
- **Initiation Delay**: 0.047s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 1.885s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.801s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.38 |  -1.42 | 00:06:05.210 | Denmark Women's    | Denmark Women's    | 117 | Carry           |   -   | [48.2, 46.3]    |  |
|  -1.29 |  -1.34 | 00:06:05.290 | Denmark Women's    | Denmark Women's    | 117 | Pass            |   -   | [48.2, 46.3]    | Incomplete (Incomplete) |
|  +0.00 |  -0.05 | 00:06:06.585 | Denmark Women's    | Denmark Women's    | 117 | Ball Receipt*   |   -   | [41.1, 52.8]    | Incomplete |
|  +0.00 |  -0.05 | 00:06:06.585 | Germany Women's    | Denmark Women's    | 117 | Interception    |   -   | [73.8, 26.7]    | Won |
|  +0.00 |  -0.05 | 00:06:06.585 | Germany Women's    | Denmark Women's    | 117 | Carry           |   -   | [73.8, 26.7]    |  |
|  +0.05 |  +0.00 | 00:06:06.632 | Denmark Women's    | Denmark Women's    | 117 | Pressure        |  Yes  | [43.9, 52.3]    |  |
|  +1.93 |  +1.88 | 00:06:08.517 | Germany Women's    | Denmark Women's    | 117 | Pass            |   -   | [79.6, 16.6]    | Incomplete (Incomplete) |
|  +6.85 |  +6.80 | 00:06:13.433 | Denmark Women's    | Denmark Women's    | 117 | Ball Recovery   |   -   | [3.1, 54.1]     |  |
|  +6.85 |  +6.80 | 00:06:13.433 | Denmark Women's    | Denmark Women's    | 117 | Carry           |   -   | [3.1, 54.1]     |  |
| +13.54 | +13.50 | 00:06:20.129 | Denmark Women's    | Denmark Women's    | 117 | Pass            |   -   | [7.3, 44.6]     | -> Sofie Junge Pe |
| +15.07 | +15.03 | 00:06:21.659 | Denmark Women's    | Denmark Women's    | 117 | Ball Receipt*   |   -   | [18.2, 41.9]    |  |
| +15.07 | +15.03 | 00:06:21.659 | Denmark Women's    | Denmark Women's    | 117 | Carry           |   -   | [18.2, 41.9]    |  |
| +15.57 | +15.53 | 00:06:22.158 | Germany Women's    | Denmark Women's    | 117 | Pressure        |   -   | [97.2, 42.1]    |  |
| +16.11 | +16.06 | 00:06:22.695 | Denmark Women's    | Denmark Women's    | 117 | Pass            |   -   | [15.6, 44.6]    | Incomplete (Incomplete) |
| +17.76 | +17.71 | 00:06:24.344 | Denmark Women's    | Denmark Women's    | 117 | Ball Receipt*   |   -   | [43.3, 58.0]    | Incomplete |
| +17.76 | +17.71 | 00:06:24.344 | Germany Women's    | Denmark Women's    | 117 | Interception    |   -   | [82.2, 23.7]    | Success In Play |
| +19.88 | +19.83 | 00:06:26.467 | Germany Women's    | Germany Women's    | 118 | Ball Recovery   |   -   | [99.0, 22.3]    |  |

---

### Disagreement Case 50: `3901833_p94_61bb6fd0`
**Classification**: False-Positive Candidate (Annot=1, Ctrl=0) | **Cohort Eligible**: `True`
- **Match**: 3901833 (Women's World Cup, 2023)
- **counterpressing_team**: France Women's
- **opponent_team_at_turnover**: Morocco Women's
- **possession_team_at_counterpress_initiation**: France Women's
- **possession_id_at_counterpress_initiation**: 94
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:45:25.775) | **Initiation**: Pressure (00:45:25.827)
- **Initiation Delay**: 0.052s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` (time: 3.961s) | Outcome 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.851s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.59 |  -0.65 | 00:45:25.182 | France Women's     | France Women's     | 94 | Ball Receipt*   |   -   | [51.8, 6.4]     |  |
|  -0.59 |  -0.65 | 00:45:25.182 | France Women's     | France Women's     | 94 | Carry           |   -   | [51.8, 6.4]     |  |
|  -0.54 |  -0.59 | 00:45:25.238 | France Women's     | France Women's     | 94 | Miscontrol      |   -   | [51.8, 6.4]     |  |
|  +0.00 |  -0.05 | 00:45:25.775 | Morocco Women's    | France Women's     | 94 | Ball Recovery   |   -   | [65.7, 73.7]    |  |
|  +0.00 |  -0.05 | 00:45:25.775 | Morocco Women's    | France Women's     | 94 | Carry           |   -   | [65.7, 73.7]    |  |
|  +0.05 |  +0.00 | 00:45:25.827 | France Women's     | France Women's     | 94 | Pressure        |  Yes  | [55.1, 6.4]     |  |
|  +4.01 |  +3.96 | 00:45:29.788 | France Women's     | France Women's     | 94 | Dribbled Past   |  Yes  | [43.5, 5.0]     |  |
|  +4.01 |  +3.96 | 00:45:29.788 | Morocco Women's    | France Women's     | 94 | Dribble         |   -   | [76.6, 75.1]    |  |
|  +4.01 |  +3.96 | 00:45:29.788 | Morocco Women's    | France Women's     | 94 | Carry           |   -   | [76.6, 75.1]    |  |
|  +5.90 |  +5.85 | 00:45:31.678 | Morocco Women's    | France Women's     | 94 | Dispossessed    |   -   | [89.9, 74.6]    |  |
|  +5.90 |  +5.85 | 00:45:31.678 | France Women's     | France Women's     | 94 | Duel            |   -   | [30.2, 5.5]     | Tackle, Success In Play |
|  +6.51 |  +6.46 | 00:45:32.285 | Morocco Women's    | France Women's     | 94 | Pressure        |   -   | [95.0, 73.3]    |  |
|  +7.42 |  +7.37 | 00:45:33.200 | France Women's     | France Women's     | 94 | Pass            |   -   | [26.2, 6.6]     | -> Wendie Renard |
|  +8.21 |  +8.16 | 00:45:33.987 | France Women's     | France Women's     | 94 | Ball Receipt*   |   -   | [22.7, 20.6]    |  |
|  +8.21 |  +8.16 | 00:45:33.987 | France Women's     | France Women's     | 94 | Carry           |   -   | [22.7, 20.6]    |  |
|  +8.26 |  +8.20 | 00:45:34.032 | France Women's     | France Women's     | 94 | Pass            |   -   | [22.7, 20.6]    | -> Sakina Karchao |
|  +9.40 |  +9.35 | 00:45:35.175 | France Women's     | France Women's     | 94 | Ball Receipt*   |   -   | [33.1, 10.9]    |  |
|  +9.40 |  +9.35 | 00:45:35.175 | France Women's     | France Women's     | 94 | Carry           |   -   | [33.1, 10.9]    |  |

---

### Disagreement Case 51: `3802643_p21_40519b75`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3802643 (Ligue 1, 2021/2022)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Strasbourg
- **possession_team_at_counterpress_initiation**: Strasbourg
- **possession_id_at_counterpress_initiation**: 21
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:14:59.580) | **Initiation**: Pressure (00:14:59.590)
- **Initiation Delay**: 0.01s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 6.757s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.977s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.14 |  -1.15 | 00:14:58.436 | Paris Saint-Germai | Paris Saint-Germai | 20 | Pass            |   -   | [90.4, 34.5]    | -> Kylian Mbappé  |
|  -0.24 |  -0.25 | 00:14:59.342 | Paris Saint-Germai | Paris Saint-Germai | 20 | Ball Receipt*   |   -   | [104.2, 36.5]   |  |
|  -0.24 |  -0.25 | 00:14:59.342 | Paris Saint-Germai | Paris Saint-Germai | 20 | Carry           |   -   | [104.2, 36.5]   |  |
|  -0.20 |  -0.21 | 00:14:59.381 | Paris Saint-Germai | Paris Saint-Germai | 20 | Miscontrol      |   -   | [104.2, 36.5]   |  |
|  +0.00 |  -0.01 | 00:14:59.580 | Strasbourg         | Strasbourg         | 21 | Pass            |  Yes  | [12.3, 44.2]    | -> Matz Sels |
|  +0.01 |  +0.00 | 00:14:59.590 | Paris Saint-Germai | Strasbourg         | 21 | Pressure        |  Yes  | [104.7, 38.3]   |  |
|  +0.35 |  +0.34 | 00:14:59.931 | Paris Saint-Germai | Strasbourg         | 21 | Pressure        |  Yes  | [112.3, 39.6]   |  |
|  +0.70 |  +0.69 | 00:15:00.279 | Strasbourg         | Strasbourg         | 21 | Ball Receipt*   |   -   | [3.6, 41.8]     |  |
|  +0.70 |  +0.69 | 00:15:00.279 | Strasbourg         | Strasbourg         | 21 | Carry           |   -   | [3.6, 41.8]     |  |
|  +0.86 |  +0.85 | 00:15:00.439 | Strasbourg         | Strasbourg         | 21 | Pass            |   -   | [3.9, 42.6]     | -> Adrien Thomass |
|  +3.99 |  +3.98 | 00:15:03.567 | Strasbourg         | Strasbourg         | 21 | Ball Receipt*   |   -   | [20.9, 65.6]    |  |
|  +3.99 |  +3.98 | 00:15:03.567 | Strasbourg         | Strasbourg         | 21 | Pass            |   -   | [20.9, 65.6]    | Incomplete (Incomplete) |
|  +3.99 |  +3.98 | 00:15:03.567 | Paris Saint-Germai | Strasbourg         | 21 | Duel            |  Yes  | [99.2, 14.5]    | Aerial Lost |
|  +4.05 |  +4.04 | 00:15:03.630 | Paris Saint-Germai | Strasbourg         | 21 | Block           |  Yes  | [97.1, 13.4]    |  |
|  +6.77 |  +6.76 | 00:15:06.347 | Paris Saint-Germai | Paris Saint-Germai | 22 | Ball Recovery   |   -   | [82.5, 22.5]    |  |
|  +6.77 |  +6.76 | 00:15:06.347 | Paris Saint-Germai | Paris Saint-Germai | 22 | Carry           |   -   | [82.5, 22.5]    |  |
|  +9.25 |  +9.24 | 00:15:08.826 | Paris Saint-Germai | Paris Saint-Germai | 22 | Pass            |   -   | [86.6, 18.9]    | -> Juan Bernat Ve |
| +10.93 | +10.92 | 00:15:10.514 | Paris Saint-Germai | Paris Saint-Germai | 22 | Ball Receipt*   |   -   | [100.0, 5.6]    |  |

---

### Disagreement Case 52: `3893828_p53_c7823536`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893828 (Women's World Cup, 2023)
- **counterpressing_team**: China PR Women's
- **opponent_team_at_turnover**: England Women's
- **possession_team_at_counterpress_initiation**: England Women's
- **possession_id_at_counterpress_initiation**: 53
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:29:26.687) | **Initiation**: Pressure (00:29:26.704)
- **Initiation Delay**: 0.017s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.565s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.09 |  -4.11 | 00:29:22.597 | China PR Women's   | China PR Women's   | 52 | Carry           |   -   | [105.5, 75.0]   |  |
|  -2.96 |  -2.98 | 00:29:23.722 | England Women's    | China PR Women's   | 52 | Pressure        |   -   | [6.2, 11.1]     |  |
|  -2.53 |  -2.55 | 00:29:24.155 | China PR Women's   | China PR Women's   | 52 | Miscontrol      |   -   | [113.0, 71.4]   |  |
|  +0.00 |  -0.02 | 00:29:26.687 | England Women's    | England Women's    | 53 | Ball Recovery   |   -   | [2.6, 17.5]     |  |
|  +0.00 |  -0.02 | 00:29:26.687 | England Women's    | England Women's    | 53 | Carry           |   -   | [2.6, 17.5]     |  |
|  +0.02 |  +0.00 | 00:29:26.704 | China PR Women's   | England Women's    | 53 | Pressure        |  Yes  | [117.7, 65.8]   |  |
|  +2.07 |  +2.05 | 00:29:28.753 | England Women's    | England Women's    | 53 | Pass            |   -   | [6.9, 19.4]     | -> Rachel Daly |
|  +2.32 |  +2.30 | 00:29:29.008 | China PR Women's   | England Women's    | 53 | Pressure        |  Yes  | [109.4, 66.7]   |  |
|  +2.38 |  +2.36 | 00:29:29.063 | China PR Women's   | England Women's    | 53 | Pressure        |  Yes  | [110.4, 66.2]   |  |
|  +2.97 |  +2.96 | 00:29:29.660 | England Women's    | England Women's    | 53 | Ball Receipt*   |   -   | [8.4, 14.7]     |  |
|  +2.97 |  +2.96 | 00:29:29.660 | England Women's    | England Women's    | 53 | Carry           |   -   | [8.4, 14.7]     |  |
|  +3.20 |  +3.18 | 00:29:29.883 | England Women's    | England Women's    | 53 | Pass            |   -   | [8.8, 13.9]     | Incomplete (Incomplete) |
|  +3.24 |  +3.22 | 00:29:29.926 | China PR Women's   | England Women's    | 53 | Block           |  Yes  | [109.8, 66.5]   |  |
|  +4.02 |  +4.01 | 00:29:30.709 | China PR Women's   | England Women's    | 53 | Pressure        |  Yes  | [103.6, 64.3]   |  |
|  +4.53 |  +4.52 | 00:29:31.220 | England Women's    | England Women's    | 53 | Ball Recovery   |   -   | [16.5, 17.5]    |  |
|  +4.53 |  +4.52 | 00:29:31.220 | England Women's    | England Women's    | 53 | Carry           |   -   | [16.5, 17.5]    |  |
|  +4.58 |  +4.57 | 00:29:31.269 | England Women's    | England Women's    | 53 | Dispossessed    |   -   | [15.4, 15.6]    |  |
|  +4.58 |  +4.57 | 00:29:31.269 | China PR Women's   | England Women's    | 53 | Duel            |  Yes  | [104.7, 64.5]   | Tackle, Success In Play |
|  +5.20 |  +5.19 | 00:29:31.891 | China PR Women's   | England Women's    | 53 | Ball Recovery   |   -   | [107.9, 68.4]   |  |
|  +5.20 |  +5.19 | 00:29:31.891 | China PR Women's   | England Women's    | 53 | Carry           |   -   | [107.9, 68.4]   |  |
|  +5.32 |  +5.30 | 00:29:32.007 | England Women's    | England Women's    | 53 | Pressure        |  Yes  | [14.2, 13.6]    |  |
|  +6.01 |  +5.99 | 00:29:32.692 | China PR Women's   | England Women's    | 53 | Dispossessed    |   -   | [106.8, 67.3]   |  |
|  +6.01 |  +5.99 | 00:29:32.692 | England Women's    | England Women's    | 53 | Duel            |  Yes  | [13.3, 12.8]    | Tackle, Won |
|  +6.01 |  +5.99 | 00:29:32.692 | England Women's    | England Women's    | 53 | Carry           |   -   | [13.3, 12.8]    |  |
|  +7.76 |  +7.75 | 00:29:34.449 | China PR Women's   | England Women's    | 53 | Pressure        |   -   | [112.4, 74.4]   |  |
|  +8.52 |  +8.50 | 00:29:35.206 | England Women's    | England Women's    | 53 | Pass            |   -   | [5.6, 4.4]      | -> Alessia Russo |
| +10.29 | +10.27 | 00:29:36.976 | England Women's    | England Women's    | 53 | Ball Receipt*   |   -   | [40.7, 8.7]     |  |

---

### Disagreement Case 53: `3857265_p40_e78e2334`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3857265 (FIFA World Cup, 2022)
- **counterpressing_team**: Poland
- **opponent_team_at_turnover**: Mexico
- **possession_team_at_counterpress_initiation**: Mexico
- **possession_id_at_counterpress_initiation**: 40
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:21:19.571) | **Initiation**: Pressure (00:21:19.616)
- **Initiation Delay**: 0.045s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.431s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.90 |  -0.94 | 00:21:18.675 | Poland             | Poland             | 39 | Pass            |   -   | [82.3, 26.1]    | Incomplete (Incomplete) |
|  -0.14 |  -0.19 | 00:21:19.430 | Poland             | Poland             | 39 | Pressure        |   -   | [75.9, 22.7]    |  |
|  +0.00 |  -0.05 | 00:21:19.571 | Poland             | Poland             | 39 | Ball Receipt*   |   -   | [73.7, 22.5]    | Incomplete |
|  +0.00 |  -0.05 | 00:21:19.571 | Mexico             | Mexico             | 40 | Interception    |  Yes  | [42.8, 56.3]    | Won |
|  +0.00 |  -0.05 | 00:21:19.571 | Mexico             | Mexico             | 40 | Carry           |   -   | [42.8, 56.3]    |  |
|  +0.05 |  +0.00 | 00:21:19.616 | Poland             | Mexico             | 40 | Pressure        |  Yes  | [79.1, 22.7]    |  |
|  +0.39 |  +0.34 | 00:21:19.957 | Mexico             | Mexico             | 40 | Dispossessed    |   -   | [42.3, 58.1]    |  |
|  +0.39 |  +0.34 | 00:21:19.957 | Poland             | Mexico             | 40 | Duel            |  Yes  | [77.8, 22.0]    | Tackle, Lost In Play |
|  +1.73 |  +1.68 | 00:21:21.298 | Mexico             | Mexico             | 40 | Pass            |   -   | [37.8, 62.1]    | -> Edson Omar Álv |
|  +2.34 |  +2.29 | 00:21:21.907 | Mexico             | Mexico             | 40 | Ball Receipt*   |   -   | [36.9, 54.2]    |  |
|  +2.34 |  +2.29 | 00:21:21.907 | Mexico             | Mexico             | 40 | Carry           |   -   | [36.9, 54.2]    |  |
|  +2.87 |  +2.83 | 00:21:22.443 | Mexico             | Mexico             | 40 | Pass            |   -   | [36.9, 54.2]    | Incomplete (Incomplete) |
|  +4.48 |  +4.43 | 00:21:24.047 | Poland             | Mexico             | 40 | Ball Recovery   |   -   | [87.1, 47.3]    |  |
|  +4.48 |  +4.43 | 00:21:24.047 | Poland             | Mexico             | 40 | Carry           |   -   | [87.1, 47.3]    |  |
|  +5.00 |  +4.96 | 00:21:24.574 | Poland             | Mexico             | 40 | Pass            |   -   | [89.4, 43.7]    | Incomplete (Incomplete) |
|  +8.00 |  +7.95 | 00:21:27.570 | Poland             | Mexico             | 40 | Ball Receipt*   |   -   | [102.7, 41.8]   | Incomplete |
|  +8.00 |  +7.95 | 00:21:27.570 | Mexico             | Mexico             | 40 | Ball Recovery   |   -   | [5.1, 43.1]     |  |
| +14.53 | +14.49 | 00:21:34.102 | Mexico             | Mexico             | 40 | Pass            |   -   | [9.4, 43.1]     | -> Héctor Alfredo |
| +16.85 | +16.81 | 00:21:36.423 | Mexico             | Mexico             | 40 | Ball Receipt*   |   -   | [18.2, 24.8]    |  |

---

### Disagreement Case 54: `3788764_p15_ae5ce844`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3788764 (UEFA Euro, 2020)
- **counterpressing_team**: Portugal
- **opponent_team_at_turnover**: Germany
- **possession_team_at_counterpress_initiation**: Germany
- **possession_id_at_counterpress_initiation**: 15
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:09:01.163) | **Initiation**: Pressure (00:09:01.222)
- **Initiation Delay**: 0.059s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.073s) | Evidence: `goalkeeper_control` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| -20.78 | -20.84 | 00:08:40.382 | Germany            | Germany            | 13 | Carry           |   -   | [82.9, 55.6]    |  |
| -20.35 | -20.40 | 00:08:40.817 | Germany            | Germany            | 13 | Pass            |   -   | [84.1, 50.1]    | Incomplete (Out) |
| -18.24 | -18.30 | 00:08:42.921 | Germany            | Germany            | 13 | Ball Receipt*   |   -   | [97.8, 76.6]    | Incomplete |
|  -2.13 |  -2.19 | 00:08:59.033 | Portugal           | Portugal           | 14 | Pass            |   -   | [15.1, 0.1]     | Incomplete (Incomplete) |
|  +0.00 |  -0.06 | 00:09:01.163 | Germany            | Germany            | 15 | Ball Recovery   |   -   | [93.1, 56.7]    |  |
|  +0.06 |  +0.00 | 00:09:01.222 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [26.8, 19.9]    |  |
|  +0.74 |  +0.68 | 00:09:01.904 | Germany            | Germany            | 15 | Pass            |   -   | [92.2, 51.2]    | -> Kai Havertz |
|  +1.46 |  +1.40 | 00:09:02.625 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [90.7, 41.2]    |  |
|  +1.46 |  +1.40 | 00:09:02.625 | Germany            | Germany            | 15 | Carry           |   -   | [90.7, 41.2]    |  |
|  +1.98 |  +1.92 | 00:09:03.145 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [20.2, 39.5]    |  |
|  +2.46 |  +2.40 | 00:09:03.625 | Germany            | Germany            | 15 | Shot            |   -   | [95.5, 40.3]    | Saved |
|  +3.13 |  +3.07 | 00:09:04.295 | Portugal           | Germany            | 15 | Goal Keeper     |   -   | [1.1, 40.4]     |  |
|  +4.48 |  +4.42 | 00:09:05.645 | Portugal           | Germany            | 15 | Pressure        |  Yes  | [3.4, 34.2]     |  |
|  +5.25 |  +5.19 | 00:09:06.415 | Germany            | Germany            | 15 | Ball Recovery   |   -   | [116.5, 48.9]   |  |
|  +5.25 |  +5.19 | 00:09:06.415 | Germany            | Germany            | 15 | Carry           |   -   | [116.5, 48.9]   |  |
|  +7.23 |  +7.17 | 00:09:08.393 | Portugal           | Germany            | 15 | Pressure        |   -   | [5.2, 25.3]     |  |
|  +7.75 |  +7.69 | 00:09:08.913 | Germany            | Germany            | 15 | Pass            |   -   | [118.0, 54.8]   | Incomplete (Incomplete) |
|  +8.60 |  +8.54 | 00:09:09.764 | Germany            | Germany            | 15 | Ball Receipt*   |   -   | [114.7, 47.2]   | Incomplete |
|  +8.60 |  +8.54 | 00:09:09.764 | Portugal           | Germany            | 15 | Ball Recovery   |   -   | [9.8, 35.5]     |  |

---

### Disagreement Case 55: `4020846_p157_30f5d80b`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 4020846 (UEFA Women's Euro, 2025)
- **counterpressing_team**: England Women's
- **opponent_team_at_turnover**: Spain Women's
- **possession_team_at_counterpress_initiation**: Spain Women's
- **possession_id_at_counterpress_initiation**: 157
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:41:41.171) | **Initiation**: Dribbled Past (00:41:41.251)
- **Initiation Delay**: 0.08s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 9.176s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.063s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.94 |  -4.02 | 00:41:37.232 | England Women's    | England Women's    | 156 | Pass            |   -   | [93.6, 66.0]    | Incomplete (Incomplete) |
|  -3.94 |  -4.02 | 00:41:37.232 | Spain Women's      | England Women's    | 156 | Duel            |   -   | [26.5, 14.1]    | Aerial Lost |
|  -0.24 |  -0.32 | 00:41:40.932 | England Women's    | England Women's    | 156 | Pressure        |   -   | [100.5, 73.7]   |  |
|  +0.00 |  -0.08 | 00:41:41.171 | Spain Women's      | Spain Women's      | 157 | Ball Recovery   |   -   | [16.1, 6.4]     |  |
|  +0.00 |  -0.08 | 00:41:41.171 | Spain Women's      | Spain Women's      | 157 | Carry           |   -   | [16.1, 6.4]     |  |
|  +0.08 |  +0.00 | 00:41:41.251 | England Women's    | Spain Women's      | 157 | Dribbled Past   |  Yes  | [103.5, 75.9]   |  |
|  +0.08 |  +0.00 | 00:41:41.251 | Spain Women's      | Spain Women's      | 157 | Dribble         |   -   | [16.6, 4.2]     |  |
|  +0.08 |  +0.00 | 00:41:41.251 | Spain Women's      | Spain Women's      | 157 | Carry           |   -   | [16.6, 4.2]     |  |
|  +0.89 |  +0.81 | 00:41:42.060 | England Women's    | Spain Women's      | 157 | Pressure        |  Yes  | [98.5, 75.9]    |  |
|  +1.31 |  +1.23 | 00:41:42.483 | Spain Women's      | Spain Women's      | 157 | Pass            |   -   | [16.6, 2.9]     | -> Patricia Guija |
|  +2.00 |  +1.92 | 00:41:43.174 | Spain Women's      | Spain Women's      | 157 | Ball Receipt*   |   -   | [20.6, 14.6]    |  |
|  +2.00 |  +1.92 | 00:41:43.174 | Spain Women's      | Spain Women's      | 157 | Pass            |   -   | [20.6, 14.6]    | -> Claudia Pina M |
|  +2.95 |  +2.87 | 00:41:44.118 | Spain Women's      | Spain Women's      | 157 | Ball Receipt*   |   -   | [29.2, 4.9]     |  |
|  +2.95 |  +2.87 | 00:41:44.118 | Spain Women's      | Spain Women's      | 157 | Carry           |   -   | [29.2, 4.9]     |  |
|  +3.21 |  +3.13 | 00:41:44.382 | England Women's    | Spain Women's      | 157 | Pressure        |  Yes  | [94.4, 72.8]    |  |
|  +4.14 |  +4.06 | 00:41:45.314 | Spain Women's      | Spain Women's      | 157 | Dribble         |   -   | [27.5, 6.1]     |  |
|  +4.14 |  +4.06 | 00:41:45.314 | England Women's    | Spain Women's      | 157 | Duel            |  Yes  | [92.6, 74.0]    | Tackle, Success Out |
|  +4.26 |  +4.18 | 00:41:45.432 | Spain Women's      | Spain Women's      | 157 | Block           |   -   | [29.5, 4.2]     |  |
|  +9.26 |  +9.18 | 00:41:50.427 | England Women's    | England Women's    | 158 | Pass            |   -   | [88.9, 80.0]    | -> Lauren Hemp |
|  +9.87 |  +9.79 | 00:41:51.043 | Spain Women's      | England Women's    | 158 | Pressure        |   -   | [17.0, 3.9]     |  |

---

### Disagreement Case 56: `3895107_p137_e167f860`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895107 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: FC Köln
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 137
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Block (00:37:12.978) | **Initiation**: Block (00:37:13.060)
- **Initiation Delay**: 0.082s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.43s) | Evidence: `completed_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.65 |  -1.73 | 00:37:11.328 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Carry           |   -   | [66.6, 16.6]    |  |
|  -1.54 |  -1.62 | 00:37:11.439 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Pass            |   -   | [66.6, 16.6]    | Incomplete (Incomplete) |
|  -0.31 |  -0.39 | 00:37:12.667 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Ball Receipt*   |   -   | [75.5, 26.0]    | Incomplete |
|  -0.31 |  -0.39 | 00:37:12.667 | FC Köln            | Bayer Leverkusen   | 137 | Pass            |   -   | [42.0, 53.4]    | Incomplete (Incomplete) |
|  +0.00 |  -0.08 | 00:37:12.978 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Block           |   -   | [76.0, 25.0]    |  |
|  +0.08 |  +0.00 | 00:37:13.060 | FC Köln            | Bayer Leverkusen   | 137 | Block           |  Yes  | [41.6, 55.8]    |  |
|  +0.95 |  +0.87 | 00:37:13.929 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Pressure        |   -   | [77.3, 25.2]    |  |
|  +1.51 |  +1.43 | 00:37:14.490 | FC Köln            | Bayer Leverkusen   | 137 | Pass            |   -   | [42.6, 58.5]    | -> Florian Kainz |
|  +3.11 |  +3.03 | 00:37:16.088 | FC Köln            | Bayer Leverkusen   | 137 | Ball Receipt*   |   -   | [52.0, 71.2]    |  |
|  +3.11 |  +3.03 | 00:37:16.088 | FC Köln            | Bayer Leverkusen   | 137 | Carry           |   -   | [52.0, 71.2]    |  |
|  +3.25 |  +3.17 | 00:37:16.231 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Pressure        |  Yes  | [68.5, 13.9]    |  |
|  +4.18 |  +4.10 | 00:37:17.162 | FC Köln            | Bayer Leverkusen   | 137 | Pass            |   -   | [52.5, 71.6]    | Incomplete (Incomplete) |
|  +7.50 |  +7.42 | 00:37:20.480 | FC Köln            | Bayer Leverkusen   | 137 | Pressure        |   -   | [94.8, 66.5]    |  |
|  +7.93 |  +7.85 | 00:37:20.909 | FC Köln            | Bayer Leverkusen   | 137 | Ball Receipt*   |   -   | [95.0, 66.5]    | Incomplete |
|  +7.93 |  +7.85 | 00:37:20.909 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Ball Recovery   |   -   | [22.9, 10.6]    |  |
|  +7.93 |  +7.85 | 00:37:20.909 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Carry           |   -   | [22.9, 10.6]    |  |
|  +9.03 |  +8.94 | 00:37:22.003 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Pass            |   -   | [22.3, 6.8]     | -> Exequiel Aleja |
| +10.04 |  +9.96 | 00:37:23.016 | Bayer Leverkusen   | Bayer Leverkusen   | 137 | Ball Receipt*   |   -   | [35.8, 6.8]     |  |

---

### Disagreement Case 57: `3794690_p18_a224ee5e`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3794690 (UEFA Euro, 2020)
- **counterpressing_team**: Netherlands
- **opponent_team_at_turnover**: Czech Republic
- **possession_team_at_counterpress_initiation**: Czech Republic
- **possession_id_at_counterpress_initiation**: 18
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:08:54.189) | **Initiation**: Pressure (00:08:54.281)
- **Initiation Delay**: 0.092s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 7.973s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.888s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.21 |  -3.30 | 00:08:50.977 | Netherlands        | Netherlands        | 17 | Pass            |   -   | [84.5, 26.3]    | -> Patrick van Aa |
|  -2.43 |  -2.52 | 00:08:51.760 | Netherlands        | Netherlands        | 17 | Ball Receipt*   |   -   | [92.8, 32.8]    |  |
|  -2.43 |  -2.52 | 00:08:51.760 | Netherlands        | Netherlands        | 17 | Carry           |   -   | [92.8, 32.8]    |  |
|  -1.95 |  -2.05 | 00:08:52.234 | Netherlands        | Netherlands        | 17 | Miscontrol      |   -   | [91.9, 31.3]    |  |
|  +0.00 |  -0.09 | 00:08:54.189 | Czech Republic     | Czech Republic     | 18 | Pass            |   -   | [27.6, 38.3]    | -> Petr Ševčík |
|  +0.09 |  +0.00 | 00:08:54.281 | Netherlands        | Czech Republic     | 18 | Pressure        |  Yes  | [81.8, 43.9]    |  |
|  +0.74 |  +0.64 | 00:08:54.925 | Czech Republic     | Czech Republic     | 18 | Ball Receipt*   |   -   | [34.4, 33.6]    |  |
|  +0.74 |  +0.64 | 00:08:54.925 | Czech Republic     | Czech Republic     | 18 | Carry           |   -   | [34.4, 33.6]    |  |
|  +2.54 |  +2.45 | 00:08:56.731 | Netherlands        | Czech Republic     | 18 | Pressure        |  Yes  | [85.9, 45.1]    |  |
|  +3.83 |  +3.74 | 00:08:58.019 | Czech Republic     | Czech Republic     | 18 | Pass            |   -   | [30.9, 31.7]    | -> Tomáš Holeš |
|  +4.31 |  +4.21 | 00:08:58.495 | Netherlands        | Czech Republic     | 18 | Pressure        |  Yes  | [90.7, 43.2]    |  |
|  +4.80 |  +4.70 | 00:08:58.985 | Czech Republic     | Czech Republic     | 18 | Ball Receipt*   |   -   | [27.3, 36.6]    |  |
|  +4.80 |  +4.70 | 00:08:58.985 | Czech Republic     | Czech Republic     | 18 | Carry           |   -   | [27.3, 36.6]    |  |
|  +4.98 |  +4.89 | 00:08:59.169 | Czech Republic     | Czech Republic     | 18 | Dispossessed    |   -   | [25.9, 38.1]    |  |
|  +4.98 |  +4.89 | 00:08:59.169 | Netherlands        | Czech Republic     | 18 | Duel            |  Yes  | [94.2, 42.0]    | Tackle, Lost In Play |
|  +6.09 |  +5.99 | 00:09:00.274 | Czech Republic     | Czech Republic     | 18 | Clearance       |   -   | [26.4, 39.5]    |  |
|  +8.07 |  +7.97 | 00:09:02.254 | Netherlands        | Netherlands        | 19 | Pass            |   -   | [78.3, 37.4]    | -> Marten de Roon |
|  +8.95 |  +8.86 | 00:09:03.140 | Netherlands        | Netherlands        | 19 | Ball Receipt*   |   -   | [73.8, 48.0]    |  |
|  +8.95 |  +8.86 | 00:09:03.140 | Netherlands        | Netherlands        | 19 | Pass            |   -   | [73.5, 48.0]    | -> Frenkie de Jon |

---

### Disagreement Case 58: `3835332_p98_e706205f`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3835332 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Portugal Women's
- **opponent_team_at_turnover**: Netherlands Women's
- **possession_team_at_counterpress_initiation**: Netherlands Women's
- **possession_id_at_counterpress_initiation**: 98
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:09:30.961) | **Initiation**: Pressure (00:09:31.054)
- **Initiation Delay**: 0.093s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 6.399s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.602s) | Evidence: `interception_plus_control` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.02 |  -1.11 | 00:09:29.944 | Portugal Women's   | Portugal Women's   | 97 | Dribble         |   -   | [97.8, 64.1]    |  |
|  -1.02 |  -1.11 | 00:09:29.944 | Portugal Women's   | Portugal Women's   | 97 | Carry           |   -   | [97.8, 64.1]    |  |
|  -0.51 |  -0.61 | 00:09:30.447 | Portugal Women's   | Portugal Women's   | 97 | Pass            |   -   | [97.6, 64.7]    | Incomplete (Incomplete) |
|  +0.00 |  -0.09 | 00:09:30.961 | Netherlands Women' | Netherlands Women' | 98 | Ball Recovery   |   -   | [13.7, 11.9]    |  |
|  +0.00 |  -0.09 | 00:09:30.961 | Netherlands Women' | Netherlands Women' | 98 | Carry           |   -   | [13.7, 11.9]    |  |
|  +0.09 |  +0.00 | 00:09:31.054 | Portugal Women's   | Netherlands Women' | 98 | Pressure        |  Yes  | [107.4, 69.7]   |  |
|  +0.44 |  +0.35 | 00:09:31.401 | Netherlands Women' | Netherlands Women' | 98 | Dispossessed    |   -   | [12.7, 13.4]    |  |
|  +0.44 |  +0.35 | 00:09:31.401 | Portugal Women's   | Netherlands Women' | 98 | Duel            |  Yes  | [107.4, 66.7]   | Tackle, Lost In Play |
|  +0.99 |  +0.89 | 00:09:31.948 | Netherlands Women' | Netherlands Women' | 98 | Pass            |   -   | [16.9, 18.3]    | -> Damaris Berta  |
|  +2.24 |  +2.15 | 00:09:33.200 | Netherlands Women' | Netherlands Women' | 98 | Ball Receipt*   |   -   | [22.1, 16.4]    |  |
|  +2.24 |  +2.15 | 00:09:33.200 | Netherlands Women' | Netherlands Women' | 98 | Carry           |   -   | [22.1, 16.4]    |  |
|  +2.48 |  +2.38 | 00:09:33.438 | Netherlands Women' | Netherlands Women' | 98 | Pass            |   -   | [25.3, 17.9]    | Incomplete (Incomplete) |
|  +4.69 |  +4.60 | 00:09:35.656 | Portugal Women's   | Netherlands Women' | 98 | Interception    |  Yes  | [89.5, 32.4]    | Success In Play |
|  +6.49 |  +6.40 | 00:09:37.453 | Portugal Women's   | Portugal Women's   | 99 | Ball Recovery   |   -   | [83.5, 23.5]    |  |
|  +6.49 |  +6.40 | 00:09:37.453 | Portugal Women's   | Portugal Women's   | 99 | Carry           |   -   | [83.5, 23.5]    |  |
|  +9.66 |  +9.57 | 00:09:40.625 | Portugal Women's   | Portugal Women's   | 99 | Pass            |   -   | [83.5, 19.0]    | -> Ana Borges |
| +11.86 | +11.77 | 00:09:42.825 | Portugal Women's   | Portugal Women's   | 99 | Ball Receipt*   |   -   | [68.5, 6.1]     |  |

---

### Disagreement Case 59: `3788745_p123_750e9e86`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3788745 (UEFA Euro, 2020)
- **counterpressing_team**: England
- **opponent_team_at_turnover**: Croatia
- **possession_team_at_counterpress_initiation**: Croatia
- **possession_id_at_counterpress_initiation**: 123
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:31:25.641) | **Initiation**: Duel (00:31:25.744)
- **Initiation Delay**: 0.103s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.086s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.28 |  -1.38 | 00:31:24.360 | Croatia            | England            | 122 | Clearance       |   -   | [53.3, 14.3]    |  |
|  -0.34 |  -0.45 | 00:31:25.297 | England            | England            | 122 | Pressure        |   -   | [62.3, 64.5]    |  |
|  +0.00 |  -0.10 | 00:31:25.641 | Croatia            | Croatia            | 123 | Ball Recovery   |   -   | [57.6, 12.4]    |  |
|  +0.00 |  -0.10 | 00:31:25.641 | Croatia            | Croatia            | 123 | Carry           |   -   | [57.6, 12.4]    |  |
|  +0.10 |  +0.00 | 00:31:25.744 | Croatia            | Croatia            | 123 | Dribble         |   -   | [57.4, 12.6]    |  |
|  +0.10 |  +0.00 | 00:31:25.744 | England            | Croatia            | 123 | Duel            |  Yes  | [62.7, 67.5]    | Tackle, Lost In Play |
|  +1.26 |  +1.16 | 00:31:26.904 | Croatia            | Croatia            | 123 | Ball Recovery   |   -   | [52.0, 8.9]     |  |
|  +1.26 |  +1.16 | 00:31:26.904 | Croatia            | Croatia            | 123 | Carry           |   -   | [52.0, 8.9]     |  |
|  +1.73 |  +1.63 | 00:31:27.373 | England            | Croatia            | 123 | Pressure        |  Yes  | [64.7, 69.7]    |  |
|  +2.15 |  +2.05 | 00:31:27.794 | Croatia            | Croatia            | 123 | Pass            |   -   | [52.9, 8.5]     | -> Nikola Vlašić |
|  +2.68 |  +2.58 | 00:31:28.326 | Croatia            | Croatia            | 123 | Ball Receipt*   |   -   | [61.4, 13.9]    |  |
|  +2.68 |  +2.58 | 00:31:28.326 | Croatia            | Croatia            | 123 | Carry           |   -   | [61.4, 13.9]    |  |
|  +2.73 |  +2.63 | 00:31:28.374 | Croatia            | Croatia            | 123 | Miscontrol      |   -   | [61.4, 13.6]    |  |
|  +3.26 |  +3.15 | 00:31:28.898 | Croatia            | Croatia            | 123 | Pressure        |   -   | [60.6, 12.6]    |  |
|  +4.13 |  +4.02 | 00:31:29.767 | Croatia            | Croatia            | 123 | Pressure        |   -   | [64.2, 7.4]     |  |
|  +4.19 |  +4.09 | 00:31:29.830 | England            | Croatia            | 123 | Ball Recovery   |   -   | [57.8, 73.9]    |  |
|  +4.19 |  +4.09 | 00:31:29.830 | England            | Croatia            | 123 | Carry           |   -   | [57.8, 73.9]    |  |
|  +4.91 |  +4.81 | 00:31:30.556 | England            | Croatia            | 123 | Pass            |   -   | [56.7, 74.8]    | Incomplete (Incomplete) |
|  +8.58 |  +8.48 | 00:31:34.225 | England            | Croatia            | 123 | Ball Receipt*   |   -   | [69.8, 68.6]    | Incomplete |
|  +8.58 |  +8.48 | 00:31:34.225 | Croatia            | Croatia            | 123 | Pass            |   -   | [34.9, 24.3]    | -> Domagoj Vida |
|  +9.71 |  +9.60 | 00:31:35.347 | Croatia            | Croatia            | 123 | Ball Receipt*   |   -   | [35.5, 38.2]    |  |
|  +9.71 |  +9.60 | 00:31:35.347 | Croatia            | Croatia            | 123 | Carry           |   -   | [35.5, 38.2]    |  |

---

### Disagreement Case 60: `3837998_p122_5b8223a8`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3837998 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Auxerre
- **possession_team_at_counterpress_initiation**: Auxerre
- **possession_id_at_counterpress_initiation**: 122
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:31:13.984) | **Initiation**: Pressure (00:31:14.098)
- **Initiation Delay**: 0.114s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 11.155s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.143s) | Evidence: `goalkeeper_control` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.54 |  -1.65 | 00:31:12.446 | Paris Saint-Germai | Paris Saint-Germai | 121 | Ball Receipt*   |   -   | [31.6, 9.1]     |  |
|  -1.54 |  -1.65 | 00:31:12.446 | Paris Saint-Germai | Paris Saint-Germai | 121 | Carry           |   -   | [31.6, 9.1]     |  |
|  -0.91 |  -1.03 | 00:31:13.072 | Paris Saint-Germai | Paris Saint-Germai | 121 | Miscontrol      |   -   | [28.9, 7.7]     |  |
|  +0.00 |  -0.11 | 00:31:13.984 | Auxerre            | Auxerre            | 122 | Ball Recovery   |   -   | [92.9, 67.6]    |  |
|  +0.00 |  -0.11 | 00:31:13.984 | Auxerre            | Auxerre            | 122 | Carry           |   -   | [92.9, 67.6]    |  |
|  +0.11 |  +0.00 | 00:31:14.098 | Paris Saint-Germai | Auxerre            | 122 | Pressure        |  Yes  | [27.9, 16.0]    |  |
|  +2.66 |  +2.55 | 00:31:16.648 | Paris Saint-Germai | Auxerre            | 122 | Pressure        |  Yes  | [9.6, 21.8]     |  |
|  +2.90 |  +2.78 | 00:31:16.881 | Auxerre            | Auxerre            | 122 | Pass            |   -   | [112.1, 59.3]   | Incomplete (Incomplete) |
|  +4.26 |  +4.14 | 00:31:18.241 | Auxerre            | Auxerre            | 122 | Ball Receipt*   |   -   | [115.7, 48.1]   | Incomplete |
|  +4.26 |  +4.14 | 00:31:18.241 | Paris Saint-Germai | Auxerre            | 122 | Goal Keeper     |   -   | [3.1, 31.4]     |  |
|  +5.01 |  +4.90 | 00:31:18.996 | Paris Saint-Germai | Auxerre            | 122 | Clearance       |   -   | [8.2, 28.2]     |  |
|  +9.30 |  +9.18 | 00:31:23.279 | Paris Saint-Germai | Auxerre            | 122 | Pressure        |   -   | [36.8, 57.0]    |  |
|  +9.75 |  +9.63 | 00:31:23.733 | Auxerre            | Auxerre            | 122 | Ball Recovery   |   -   | [79.5, 20.3]    |  |
|  +9.75 |  +9.63 | 00:31:23.733 | Auxerre            | Auxerre            | 122 | Carry           |   -   | [79.5, 20.3]    |  |
|  +9.94 |  +9.83 | 00:31:23.928 | Paris Saint-Germai | Auxerre            | 122 | Dribbled Past   |   -   | [41.8, 59.8]    |  |
|  +9.94 |  +9.83 | 00:31:23.928 | Auxerre            | Auxerre            | 122 | Dribble         |   -   | [78.3, 20.3]    |  |
| +11.27 | +11.15 | 00:31:25.253 | Paris Saint-Germai | Paris Saint-Germai | 123 | Ball Recovery   |   -   | [39.2, 56.4]    |  |

---

### Disagreement Case 61: `3930177_p98_e3b8bf66`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3930177 (UEFA Euro, 2024)
- **counterpressing_team**: Hungary
- **opponent_team_at_turnover**: Scotland
- **possession_team_at_counterpress_initiation**: Scotland
- **possession_id_at_counterpress_initiation**: 98
- **Turnover Context**: open_play (Origin: From Keeper)
- **Turnover**: Goal Keeper (00:13:44.804) | **Initiation**: Pressure (00:13:44.918)
- **Initiation Delay**: 0.114s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.114s) | Evidence: `completed_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.22 |  -4.34 | 00:13:40.582 | Hungary            | Hungary            | 97 | Carry           |   -   | [43.3, 13.0]    |  |
|  -4.15 |  -4.27 | 00:13:40.649 | Hungary            | Hungary            | 97 | Pass            |   -   | [43.3, 12.7]    | Incomplete (Incomplete) |
|  +0.00 |  -0.11 | 00:13:44.804 | Hungary            | Hungary            | 97 | Ball Receipt*   |   -   | [54.7, 26.0]    | Incomplete |
|  +0.00 |  -0.11 | 00:13:44.804 | Scotland           | Scotland           | 98 | Goal Keeper     |   -   | [27.3, 51.1]    |  |
|  +0.00 |  -0.11 | 00:13:44.804 | Scotland           | Scotland           | 98 | Carry           |   -   | [27.3, 51.1]    |  |
|  +0.11 |  +0.00 | 00:13:44.918 | Hungary            | Scotland           | 98 | Pressure        |  Yes  | [84.8, 32.6]    |  |
|  +0.61 |  +0.49 | 00:13:45.410 | Scotland           | Scotland           | 98 | Pass            |   -   | [28.1, 52.1]    | -> Anthony Ralsto |
|  +2.89 |  +2.78 | 00:13:47.699 | Scotland           | Scotland           | 98 | Ball Receipt*   |   -   | [56.4, 65.4]    |  |
|  +2.89 |  +2.78 | 00:13:47.699 | Scotland           | Scotland           | 98 | Pass            |   -   | [56.4, 65.4]    | Incomplete (Incomplete) |
|  +4.23 |  +4.11 | 00:13:49.032 | Scotland           | Scotland           | 98 | Ball Receipt*   |   -   | [69.1, 63.4]    | Incomplete |
|  +4.23 |  +4.11 | 00:13:49.032 | Hungary            | Scotland           | 98 | Pass            |   -   | [51.0, 14.2]    | -> Dominik Szobos |
|  +5.85 |  +5.74 | 00:13:50.654 | Hungary            | Scotland           | 98 | Ball Receipt*   |   -   | [70.7, 21.8]    |  |
|  +5.85 |  +5.74 | 00:13:50.654 | Hungary            | Scotland           | 98 | Pass            |   -   | [70.7, 21.8]    | Incomplete (Pass Offside) |
|  +7.71 |  +7.60 | 00:13:52.518 | Hungary            | Scotland           | 98 | Ball Receipt*   |   -   | [77.8, 28.2]    | Incomplete |
| +25.51 | +25.40 | 00:14:10.317 | Scotland           | Scotland           | 99 | Pass            |   -   | [41.1, 51.7]    | -> Scott McKenna |
| +26.54 | +26.43 | 00:14:11.344 | Scotland           | Scotland           | 99 | Ball Receipt*   |   -   | [40.7, 27.9]    |  |
| +26.55 | +26.43 | 00:14:11.349 | Scotland           | Scotland           | 99 | Pass            |   -   | [41.3, 26.5]    | -> Andrew Roberts |

---

### Disagreement Case 62: `3773565_p6_14d0dc17`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3773565 (La Liga, 2020/2021)
- **counterpressing_team**: Barcelona
- **opponent_team_at_turnover**: Granada
- **possession_team_at_counterpress_initiation**: Granada
- **possession_id_at_counterpress_initiation**: 6
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:01:35.188) | **Initiation**: Duel (00:01:35.308)
- **Initiation Delay**: 0.12s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.346s) | Evidence: `goalkeeper_control` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.46 |  -0.58 | 00:01:34.730 | Barcelona          | Barcelona          | 5 | Pressure        |   -   | [31.2, 45.1]    |  |
|  +0.00 |  -0.12 | 00:01:35.188 | Barcelona          | Barcelona          | 5 | Ball Receipt*   |   -   | [28.6, 43.2]    | Incomplete |
|  +0.00 |  -0.12 | 00:01:35.188 | Granada            | Granada            | 6 | Ball Recovery   |   -   | [92.4, 38.8]    |  |
|  +0.00 |  -0.12 | 00:01:35.188 | Granada            | Granada            | 6 | Carry           |   -   | [92.4, 38.8]    |  |
|  +0.12 |  -0.00 | 00:01:35.308 | Granada            | Granada            | 6 | Dispossessed    |   -   | [92.7, 39.8]    |  |
|  +0.12 |  -0.00 | 00:01:35.308 | Barcelona          | Granada            | 6 | Duel            |  Yes  | [27.4, 40.3]    | Tackle, Lost In Play |
|  +0.72 |  +0.60 | 00:01:35.912 | Barcelona          | Granada            | 6 | Foul Committed  |  Yes  | [27.4, 40.3]    |  |
|  +0.72 |  +0.60 | 00:01:35.912 | Granada            | Granada            | 6 | Foul Won        |   -   | [92.7, 39.8]    |  |
|  +2.07 |  +1.95 | 00:01:37.255 | Granada            | Granada            | 6 | Ball Recovery   |   -   | [89.1, 54.1]    |  |
|  +2.07 |  +1.95 | 00:01:37.255 | Granada            | Granada            | 6 | Carry           |   -   | [89.1, 54.1]    |  |
|  +3.85 |  +3.73 | 00:01:39.034 | Granada            | Granada            | 6 | Shot            |   -   | [101.1, 50.9]   | Saved |
|  +4.47 |  +4.35 | 00:01:39.654 | Barcelona          | Granada            | 6 | Goal Keeper     |   -   | [3.1, 38.5]     |  |
| +47.39 | +47.27 | 00:02:22.579 | Granada            | Granada            | 7 | Pass            |   -   | [120.0, 0.1]    | -> Roberto Soldad |
| +48.55 | +48.43 | 00:02:23.736 | Granada            | Granada            | 7 | Ball Receipt*   |   -   | [112.9, 30.9]   |  |
| +48.55 | +48.43 | 00:02:23.736 | Granada            | Granada            | 7 | Pass            |   -   | [112.5, 30.9]   | Incomplete (Incomplete) |
| +48.96 | +48.84 | 00:02:24.149 | Granada            | Granada            | 7 | Ball Receipt*   |   -   | [110.1, 43.6]   | Incomplete |
| +48.96 | +48.84 | 00:02:24.149 | Barcelona          | Granada            | 7 | Clearance       |   -   | [8.6, 41.1]     |  |

---

### Disagreement Case 63: `3998837_p89_1c054110`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3998837 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Switzerland Women's
- **opponent_team_at_turnover**: Norway Women's
- **possession_team_at_counterpress_initiation**: Norway Women's
- **possession_id_at_counterpress_initiation**: 89
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:46:44.859) | **Initiation**: Duel (00:46:45.008)
- **Initiation Delay**: 0.149s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.808s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.93 |  -1.07 | 00:46:43.933 | Switzerland Women' | Switzerland Women' | 88 | Pass            |   -   | [62.6, 2.0]     | Incomplete (Incomplete) |
|  +0.00 |  -0.15 | 00:46:44.859 | Switzerland Women' | Switzerland Women' | 88 | Ball Receipt*   |   -   | [63.6, 11.5]    | Incomplete |
|  +0.00 |  -0.15 | 00:46:44.859 | Norway Women's     | Norway Women's     | 89 | Ball Recovery   |   -   | [57.8, 68.9]    |  |
|  +0.00 |  -0.15 | 00:46:44.859 | Norway Women's     | Norway Women's     | 89 | Carry           |   -   | [57.8, 68.9]    |  |
|  +0.15 |  +0.00 | 00:46:45.008 | Norway Women's     | Norway Women's     | 89 | Dispossessed    |   -   | [56.7, 69.1]    |  |
|  +0.15 |  +0.00 | 00:46:45.008 | Switzerland Women' | Norway Women's     | 89 | Duel            |  Yes  | [63.4, 11.0]    | Tackle, Lost In Play |
|  +0.74 |  +0.59 | 00:46:45.597 | Switzerland Women' | Norway Women's     | 89 | Pressure        |  Yes  | [58.8, 3.6]     |  |
|  +1.12 |  +0.97 | 00:46:45.980 | Norway Women's     | Norway Women's     | 89 | Ball Recovery   |   -   | [60.3, 74.5]    |  |
|  +1.12 |  +0.97 | 00:46:45.980 | Norway Women's     | Norway Women's     | 89 | Carry           |   -   | [60.3, 74.5]    |  |
|  +1.51 |  +1.36 | 00:46:46.367 | Switzerland Women' | Norway Women's     | 89 | Pressure        |  Yes  | [61.3, 7.7]     |  |
|  +1.96 |  +1.81 | 00:46:46.816 | Norway Women's     | Norway Women's     | 89 | Dribble         |   -   | [60.3, 73.2]    |  |
|  +1.96 |  +1.81 | 00:46:46.816 | Switzerland Women' | Norway Women's     | 89 | Duel            |  Yes  | [59.8, 6.9]     | Tackle, Won |
|  +1.96 |  +1.81 | 00:46:46.816 | Switzerland Women' | Norway Women's     | 89 | Carry           |   -   | [59.8, 6.9]     |  |
|  +3.27 |  +3.12 | 00:46:48.133 | Norway Women's     | Norway Women's     | 89 | Pressure        |  Yes  | [55.5, 75.3]    |  |
|  +3.61 |  +3.46 | 00:46:48.469 | Switzerland Women' | Norway Women's     | 89 | Pass            |   -   | [60.9, 6.9]     | Incomplete (Incomplete) |
|  +3.97 |  +3.82 | 00:46:48.829 | Switzerland Women' | Norway Women's     | 89 | Ball Receipt*   |   -   | [71.1, 15.4]    | Incomplete |
|  +3.97 |  +3.82 | 00:46:48.829 | Norway Women's     | Norway Women's     | 89 | Interception    |  Yes  | [52.2, 67.6]    | Success In Play |
|  +5.38 |  +5.23 | 00:46:50.242 | Norway Women's     | Norway Women's     | 89 | Ball Recovery   |   -   | [62.9, 56.3]    |  |
|  +5.38 |  +5.23 | 00:46:50.242 | Norway Women's     | Norway Women's     | 89 | Carry           |   -   | [62.9, 56.3]    |  |
|  +5.40 |  +5.25 | 00:46:50.260 | Switzerland Women' | Norway Women's     | 89 | Pressure        |   -   | [54.4, 25.3]    |  |
|  +6.26 |  +6.11 | 00:46:51.122 | Norway Women's     | Norway Women's     | 89 | Pass            |   -   | [63.6, 54.8]    | Incomplete (Incomplete) |
|  +7.61 |  +7.46 | 00:46:52.468 | Norway Women's     | Norway Women's     | 89 | Ball Receipt*   |   -   | [61.3, 40.7]    | Incomplete |
|  +7.61 |  +7.46 | 00:46:52.468 | Switzerland Women' | Norway Women's     | 89 | Ball Recovery   |   -   | [57.5, 31.9]    |  |
|  +9.90 |  +9.75 | 00:46:54.757 | Norway Women's     | Norway Women's     | 89 | Half End        |   -   | -               |  |
|  +9.90 |  +9.75 | 00:46:54.757 | Switzerland Women' | Norway Women's     | 89 | Half End        |   -   | -               |  |

---

### Disagreement Case 64: `3893826_p130_a3267a0b`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893826 (Women's World Cup, 2023)
- **counterpressing_team**: Portugal Women's
- **opponent_team_at_turnover**: United States Women's
- **possession_team_at_counterpress_initiation**: United States Women's
- **possession_id_at_counterpress_initiation**: 130
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:25:16.140) | **Initiation**: Pressure (00:25:16.291)
- **Initiation Delay**: 0.151s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.017s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.52 |  -3.67 | 00:25:12.624 | United States Wome | Portugal Women's   | 129 | Ball Recovery   |   -   | [56.3, 57.0]    |  |
|  -2.35 |  -2.50 | 00:25:13.795 | Portugal Women's   | Portugal Women's   | 129 | Pass            |   -   | [57.2, 29.3]    | Incomplete (Incomplete) |
|  +0.00 |  -0.15 | 00:25:16.140 | Portugal Women's   | Portugal Women's   | 129 | Ball Receipt*   |   -   | [58.9, 47.4]    | Incomplete |
|  +0.00 |  -0.15 | 00:25:16.140 | United States Wome | United States Wome | 130 | Ball Recovery   |   -   | [61.2, 30.9]    |  |
|  +0.00 |  -0.15 | 00:25:16.140 | United States Wome | United States Wome | 130 | Carry           |   -   | [61.2, 30.9]    |  |
|  +0.15 |  +0.00 | 00:25:16.291 | Portugal Women's   | United States Wome | 130 | Pressure        |  Yes  | [58.7, 48.5]    |  |
|  +1.17 |  +1.02 | 00:25:17.308 | United States Wome | United States Wome | 130 | Dispossessed    |   -   | [69.2, 26.2]    |  |
|  +1.17 |  +1.02 | 00:25:17.308 | Portugal Women's   | United States Wome | 130 | Duel            |  Yes  | [50.9, 53.9]    | Tackle, Success In Play |
|  +1.78 |  +1.63 | 00:25:17.917 | Portugal Women's   | United States Wome | 130 | Pass            |   -   | [44.3, 58.3]    | Incomplete (Incomplete) |
|  +2.86 |  +2.71 | 00:25:19.002 | Portugal Women's   | United States Wome | 130 | Ball Receipt*   |   -   | [51.8, 59.6]    | Incomplete |
|  +2.86 |  +2.71 | 00:25:19.002 | United States Wome | United States Wome | 130 | Ball Recovery   |   -   | [67.0, 18.8]    |  |
|  +2.86 |  +2.71 | 00:25:19.002 | United States Wome | United States Wome | 130 | Carry           |   -   | [67.0, 18.8]    |  |
|  +7.72 |  +7.57 | 00:25:23.865 | United States Wome | United States Wome | 130 | Pass            |   -   | [99.1, 8.5]     | Incomplete (Incomplete) |
|  +7.87 |  +7.72 | 00:25:24.013 | United States Wome | United States Wome | 130 | Ball Receipt*   |   -   | [104.9, 36.1]   | Incomplete |
|  +7.87 |  +7.72 | 00:25:24.013 | Portugal Women's   | United States Wome | 130 | Block           |   -   | [19.3, 68.8]    |  |
| +11.13 | +10.98 | 00:25:27.273 | Portugal Women's   | United States Wome | 130 | Ball Recovery   |   -   | [46.0, 74.4]    |  |
| +11.13 | +10.98 | 00:25:27.273 | Portugal Women's   | United States Wome | 130 | Carry           |   -   | [46.0, 74.4]    |  |

---

### Disagreement Case 65: `3998856_p131_3e93b6ac`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3998856 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Germany Women's
- **opponent_team_at_turnover**: Sweden Women's
- **possession_team_at_counterpress_initiation**: Sweden Women's
- **possession_id_at_counterpress_initiation**: 131
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:18:13.230) | **Initiation**: Pressure (00:18:13.398)
- **Initiation Delay**: 0.168s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.192s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.22 |  -2.38 | 00:18:11.013 | Germany Women's    | Germany Women's    | 130 | Ball Receipt*   |   -   | [67.6, 73.6]    |  |
|  -2.22 |  -2.38 | 00:18:11.013 | Germany Women's    | Germany Women's    | 130 | Pass            |   -   | [67.8, 73.6]    | Incomplete (Incomplete) |
|  +0.00 |  -0.17 | 00:18:13.230 | Germany Women's    | Germany Women's    | 130 | Ball Receipt*   |   -   | [55.7, 75.6]    | Incomplete |
|  +0.00 |  -0.17 | 00:18:13.230 | Sweden Women's     | Sweden Women's     | 131 | Ball Recovery   |   -   | [68.2, 6.1]     |  |
|  +0.00 |  -0.17 | 00:18:13.230 | Sweden Women's     | Sweden Women's     | 131 | Carry           |   -   | [68.2, 6.1]     |  |
|  +0.17 |  +0.00 | 00:18:13.398 | Germany Women's    | Sweden Women's     | 131 | Pressure        |  Yes  | [52.1, 77.2]    |  |
|  +0.36 |  +0.19 | 00:18:13.590 | Sweden Women's     | Sweden Women's     | 131 | Dispossessed    |   -   | [67.9, 1.8]     |  |
|  +0.36 |  +0.19 | 00:18:13.590 | Germany Women's    | Sweden Women's     | 131 | Duel            |  Yes  | [52.2, 78.3]    | Tackle, Success Out |
| +18.52 | +18.35 | 00:18:31.750 | Germany Women's    | Germany Women's    | 132 | Pass            |   -   | [55.1, 80.0]    | Incomplete (Incomplete) |
| +19.69 | +19.52 | 00:18:32.916 | Sweden Women's     | Sweden Women's     | 133 | Pass            |   -   | [52.5, 5.3]     | -> Ingrid Filippa |
| +21.69 | +21.53 | 00:18:34.924 | Sweden Women's     | Sweden Women's     | 133 | Ball Receipt*   |   -   | [48.6, 17.2]    |  |
| +21.69 | +21.53 | 00:18:34.924 | Sweden Women's     | Sweden Women's     | 133 | Carry           |   -   | [48.6, 17.2]    |  |
| +23.31 | +23.14 | 00:18:36.542 | Germany Women's    | Sweden Women's     | 133 | Pressure        |  Yes  | [69.2, 60.8]    |  |
| +23.42 | +23.26 | 00:18:36.653 | Sweden Women's     | Sweden Women's     | 133 | Pass            |   -   | [49.0, 21.2]    | -> Linda Brigitta |
| +24.80 | +24.63 | 00:18:38.028 | Sweden Women's     | Sweden Women's     | 133 | Ball Receipt*   |   -   | [40.3, 31.4]    |  |
| +24.80 | +24.63 | 00:18:38.028 | Sweden Women's     | Sweden Women's     | 133 | Carry           |   -   | [40.3, 31.4]    |  |
| +25.82 | +25.66 | 00:18:39.054 | Sweden Women's     | Sweden Women's     | 133 | Pass            |   -   | [40.4, 31.4]    | -> Magdalena Lill |

---

### Disagreement Case 66: `3895258_p42_3e173758`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895258 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: FC Köln
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 42
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:24:23.183) | **Initiation**: Duel (00:24:23.394)
- **Initiation Delay**: 0.211s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.716s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.07 |  -0.28 | 00:24:23.116 | FC Köln            | FC Köln            | 41 | Pressure        |   -   | [13.9, 62.2]    |  |
|  +0.00 |  -0.21 | 00:24:23.183 | FC Köln            | FC Köln            | 41 | Ball Receipt*   |   -   | [13.0, 62.9]    | Incomplete |
|  +0.00 |  -0.21 | 00:24:23.183 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Interception    |  Yes  | [104.7, 16.5]   | Won |
|  +0.00 |  -0.21 | 00:24:23.183 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Carry           |   -   | [104.7, 16.5]   |  |
|  +0.21 |  +0.00 | 00:24:23.394 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Dispossessed    |   -   | [106.2, 17.9]   |  |
|  +0.21 |  +0.00 | 00:24:23.394 | FC Köln            | Bayer Leverkusen   | 42 | Duel            |  Yes  | [13.9, 62.2]    | Tackle, Lost In Play |
|  +0.90 |  +0.69 | 00:24:24.085 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Ball Recovery   |   -   | [103.2, 19.4]   |  |
|  +0.90 |  +0.69 | 00:24:24.085 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Carry           |   -   | [103.2, 19.4]   |  |
|  +2.08 |  +1.86 | 00:24:25.258 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Pass            |   -   | [101.0, 20.0]   | -> Granit Xhaka |
|  +3.32 |  +3.11 | 00:24:26.499 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Ball Receipt*   |   -   | [96.3, 41.7]    |  |
|  +3.32 |  +3.11 | 00:24:26.499 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Carry           |   -   | [96.3, 41.7]    |  |
|  +3.41 |  +3.20 | 00:24:26.596 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Pass            |   -   | [96.3, 41.7]    | -> Jonas Hofmann |
|  +4.08 |  +3.87 | 00:24:27.262 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Ball Receipt*   |   -   | [105.6, 39.8]   |  |
|  +4.08 |  +3.87 | 00:24:27.262 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Carry           |   -   | [105.6, 39.8]   |  |
|  +4.38 |  +4.17 | 00:24:27.562 | FC Köln            | Bayer Leverkusen   | 42 | Pressure        |  Yes  | [14.5, 39.4]    |  |
|  +4.93 |  +4.72 | 00:24:28.110 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Dispossessed    |   -   | [108.8, 39.8]   |  |
|  +4.93 |  +4.72 | 00:24:28.110 | FC Köln            | Bayer Leverkusen   | 42 | Duel            |  Yes  | [11.3, 40.3]    | Tackle, Won |
|  +4.93 |  +4.72 | 00:24:28.110 | FC Köln            | Bayer Leverkusen   | 42 | Carry           |   -   | [11.3, 40.3]    |  |
|  +5.62 |  +5.41 | 00:24:28.808 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Pressure        |  Yes  | [107.3, 39.8]   |  |
|  +6.43 |  +6.22 | 00:24:29.611 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | Pressure        |  Yes  | [109.5, 39.0]   |  |
|  +6.87 |  +6.66 | 00:24:30.056 | FC Köln            | Bayer Leverkusen   | 42 | Miscontrol      |   -   | [11.4, 37.8]    |  |
|  +8.03 |  +7.82 | 00:24:31.209 | FC Köln            | Bayer Leverkusen   | 42 | Clearance       |   -   | [12.2, 37.8]    |  |
|  +8.48 |  +8.27 | 00:24:31.665 | FC Köln            | Bayer Leverkusen   | 42 | Block           |   -   | [17.0, 33.9]    |  |
|  +9.31 |  +9.10 | 00:24:32.494 | FC Köln            | Bayer Leverkusen   | 42 | 50/50           |   -   | [14.7, 34.2]    |  |
|  +9.31 |  +9.10 | 00:24:32.494 | Bayer Leverkusen   | Bayer Leverkusen   | 42 | 50/50           |  Yes  | [105.4, 45.9]   |  |

---

### Disagreement Case 67: `3902967_p182_569524e4`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3902967 (Women's World Cup, 2023)
- **counterpressing_team**: England Women's
- **opponent_team_at_turnover**: Colombia Women's
- **possession_team_at_counterpress_initiation**: Colombia Women's
- **possession_id_at_counterpress_initiation**: 182
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:53:05.533) | **Initiation**: Pressure (00:53:05.760)
- **Initiation Delay**: 0.227s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.156s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.09 |  -1.32 | 00:53:04.440 | England Women's    | Colombia Women's   | 182 | Pass            |   -   | [77.1, 55.5]    | Incomplete (Incomplete) |
|  -1.09 |  -1.32 | 00:53:04.440 | Colombia Women's   | Colombia Women's   | 182 | Duel            |  Yes  | [43.0, 24.6]    | Aerial Lost |
|  +0.00 |  -0.23 | 00:53:05.533 | England Women's    | Colombia Women's   | 182 | Ball Receipt*   |   -   | [91.8, 55.5]    | Incomplete |
|  +0.00 |  -0.23 | 00:53:05.533 | Colombia Women's   | Colombia Women's   | 182 | Ball Recovery   |   -   | [29.6, 27.3]    |  |
|  +0.00 |  -0.23 | 00:53:05.533 | Colombia Women's   | Colombia Women's   | 182 | Carry           |   -   | [29.6, 27.3]    |  |
|  +0.23 |  +0.00 | 00:53:05.760 | England Women's    | Colombia Women's   | 182 | Pressure        |  Yes  | [92.5, 51.5]    |  |
|  +1.62 |  +1.39 | 00:53:07.151 | England Women's    | Colombia Women's   | 182 | Pressure        |   -   | [85.6, 61.5]    |  |
|  +1.79 |  +1.56 | 00:53:07.324 | Colombia Women's   | Colombia Women's   | 182 | Miscontrol      |   -   | [37.0, 16.9]    |  |
|  +3.04 |  +2.81 | 00:53:08.575 | England Women's    | Colombia Women's   | 182 | Pressure        |   -   | [73.0, 58.5]    |  |
|  +3.06 |  +2.84 | 00:53:08.596 | Colombia Women's   | Colombia Women's   | 182 | Ball Recovery   |   -   | [45.0, 17.7]    |  |
|  +3.06 |  +2.84 | 00:53:08.596 | Colombia Women's   | Colombia Women's   | 182 | Carry           |   -   | [45.0, 17.7]    |  |
|  +3.38 |  +3.16 | 00:53:08.916 | Colombia Women's   | Colombia Women's   | 182 | Dispossessed    |   -   | [35.5, 16.0]    |  |
|  +3.38 |  +3.16 | 00:53:08.916 | England Women's    | Colombia Women's   | 182 | Duel            |   -   | [84.6, 64.1]    | Tackle, Success In Play |
|  +5.00 |  +4.77 | 00:53:10.535 | England Women's    | Colombia Women's   | 182 | Ball Recovery   |   -   | [87.5, 65.0]    |  |
|  +5.00 |  +4.77 | 00:53:10.535 | England Women's    | Colombia Women's   | 182 | Carry           |   -   | [87.5, 65.0]    |  |
|  +5.26 |  +5.03 | 00:53:10.793 | England Women's    | Colombia Women's   | 182 | Dispossessed    |   -   | [91.4, 62.0]    |  |
|  +5.26 |  +5.03 | 00:53:10.793 | Colombia Women's   | Colombia Women's   | 182 | Duel            |  Yes  | [28.7, 18.1]    | Tackle, Won |
|  +5.26 |  +5.03 | 00:53:10.793 | Colombia Women's   | Colombia Women's   | 182 | Carry           |   -   | [28.7, 18.1]    |  |
|  +6.59 |  +6.36 | 00:53:12.118 | England Women's    | Colombia Women's   | 182 | Foul Committed  |   -   | [94.8, 59.6]    |  |
|  +6.59 |  +6.36 | 00:53:12.118 | Colombia Women's   | Colombia Women's   | 182 | Foul Won        |   -   | [25.3, 20.5]    |  |
| +27.28 | +27.05 | 00:53:32.809 | Colombia Women's   | Colombia Women's   | 183 | Pass            |   -   | [25.7, 20.7]    | Incomplete (Incomplete) |
| +29.10 | +28.87 | 00:53:34.631 | Colombia Women's   | Colombia Women's   | 183 | Ball Receipt*   |   -   | [86.5, 44.4]    | Incomplete |

---

### Disagreement Case 68: `3837839_p82_6fb33f04`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3837839 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Stade de Reims
- **possession_team_at_counterpress_initiation**: Stade de Reims
- **possession_id_at_counterpress_initiation**: 82
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:45:05.222) | **Initiation**: Pressure (00:45:05.453)
- **Initiation Delay**: 0.231s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.363s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.45 |  -1.68 | 00:45:03.770 | Paris Saint-Germai | Paris Saint-Germai | 81 | Carry           |   -   | [88.9, 7.9]     |  |
|  -0.26 |  -0.49 | 00:45:04.964 | Paris Saint-Germai | Paris Saint-Germai | 81 | Pass            |   -   | [89.8, 8.1]     | Incomplete (Incomplete) |
|  +0.00 |  -0.23 | 00:45:05.222 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [96.5, 18.0]    | Incomplete |
|  +0.00 |  -0.23 | 00:45:05.222 | Stade de Reims     | Stade de Reims     | 82 | Interception    |  Yes  | [26.4, 69.9]    | Won |
|  +0.00 |  -0.23 | 00:45:05.222 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [26.4, 69.9]    |  |
|  +0.23 |  +0.00 | 00:45:05.453 | Paris Saint-Germai | Stade de Reims     | 82 | Pressure        |  Yes  | [95.1, 14.6]    |  |
|  +0.43 |  +0.20 | 00:45:05.652 | Stade de Reims     | Stade de Reims     | 82 | Pass            |   -   | [25.2, 65.8]    | -> Junya Ito |
|  +1.05 |  +0.82 | 00:45:06.269 | Stade de Reims     | Stade de Reims     | 82 | Ball Receipt*   |   -   | [28.3, 62.1]    |  |
|  +1.05 |  +0.82 | 00:45:06.269 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [28.3, 62.1]    |  |
|  +3.36 |  +3.13 | 00:45:08.584 | Stade de Reims     | Stade de Reims     | 82 | Pass            |   -   | [37.0, 64.1]    | -> Marshall Nyash |
|  +4.35 |  +4.12 | 00:45:09.569 | Stade de Reims     | Stade de Reims     | 82 | Ball Receipt*   |   -   | [40.4, 55.6]    |  |
|  +4.35 |  +4.12 | 00:45:09.569 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [40.4, 55.6]    |  |
|  +4.59 |  +4.36 | 00:45:09.816 | Stade de Reims     | Stade de Reims     | 82 | Dribble         |   -   | [41.8, 55.2]    |  |
|  +4.59 |  +4.36 | 00:45:09.816 | Paris Saint-Germai | Stade de Reims     | 82 | Duel            |  Yes  | [78.3, 24.9]    | Tackle, Won |
|  +4.59 |  +4.36 | 00:45:09.816 | Paris Saint-Germai | Stade de Reims     | 82 | Carry           |   -   | [78.3, 24.9]    |  |
|  +6.02 |  +5.79 | 00:45:11.247 | Paris Saint-Germai | Stade de Reims     | 82 | Pass            |   -   | [82.2, 22.5]    | -> Kylian Mbappé  |
|  +6.84 |  +6.61 | 00:45:12.063 | Paris Saint-Germai | Stade de Reims     | 82 | Ball Receipt*   |   -   | [92.0, 21.8]    |  |
|  +6.84 |  +6.61 | 00:45:12.063 | Paris Saint-Germai | Stade de Reims     | 82 | Carry           |   -   | [92.0, 21.8]    |  |
|  +7.63 |  +7.40 | 00:45:12.852 | Paris Saint-Germai | Stade de Reims     | 82 | Pass            |   -   | [94.9, 24.2]    | Incomplete (Incomplete) |
|  +8.13 |  +7.90 | 00:45:13.353 | Paris Saint-Germai | Stade de Reims     | 82 | Ball Receipt*   |   -   | [93.7, 47.2]    | Incomplete |
|  +8.13 |  +7.90 | 00:45:13.353 | Stade de Reims     | Stade de Reims     | 82 | Interception    |  Yes  | [25.0, 48.7]    | Success In Play |
|  +9.46 |  +9.23 | 00:45:14.679 | Stade de Reims     | Stade de Reims     | 82 | Ball Recovery   |   -   | [29.3, 35.7]    |  |
|  +9.46 |  +9.23 | 00:45:14.679 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [29.3, 35.7]    |  |

---

### Disagreement Case 69: `3938644_p59_c41c955a`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3938644 (UEFA Euro, 2024)
- **counterpressing_team**: Portugal
- **opponent_team_at_turnover**: Georgia
- **possession_team_at_counterpress_initiation**: Georgia
- **possession_id_at_counterpress_initiation**: 59
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:39:11.405) | **Initiation**: Block (00:39:11.644)
- **Initiation Delay**: 0.239s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.462s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.21 |  -2.45 | 00:39:09.196 | Portugal           | Portugal           | 58 | Pass            |   -   | [85.2, 59.0]    | Incomplete (Incomplete) |
|  +0.00 |  -0.24 | 00:39:11.405 | Portugal           | Portugal           | 58 | Ball Receipt*   |   -   | [95.8, 51.4]    | Incomplete |
|  +0.00 |  -0.24 | 00:39:11.405 | Georgia            | Georgia            | 59 | Pass            |   -   | [15.0, 30.6]    | -> Khvicha Kvarat |
|  +0.24 |  +0.00 | 00:39:11.644 | Georgia            | Georgia            | 59 | Ball Receipt*   |   -   | [32.6, 27.6]    |  |
|  +0.24 |  +0.00 | 00:39:11.644 | Georgia            | Georgia            | 59 | Carry           |   -   | [32.6, 27.6]    |  |
|  +0.24 |  +0.00 | 00:39:11.644 | Portugal           | Georgia            | 59 | Block           |  Yes  | [98.8, 51.4]    |  |
|  +0.64 |  +0.41 | 00:39:12.049 | Portugal           | Georgia            | 59 | Pressure        |  Yes  | [88.9, 47.7]    |  |
|  +0.85 |  +0.61 | 00:39:12.256 | Georgia            | Georgia            | 59 | Pass            |   -   | [30.6, 31.9]    | -> Giorgi Chakvet |
|  +1.40 |  +1.17 | 00:39:12.810 | Georgia            | Georgia            | 59 | Ball Receipt*   |   -   | [32.5, 24.1]    |  |
|  +1.40 |  +1.17 | 00:39:12.810 | Georgia            | Georgia            | 59 | Carry           |   -   | [32.5, 24.1]    |  |
|  +1.46 |  +1.23 | 00:39:12.870 | Georgia            | Georgia            | 59 | Pass            |   -   | [34.2, 26.1]    | Incomplete (Incomplete) |
|  +3.70 |  +3.46 | 00:39:15.106 | Georgia            | Georgia            | 59 | Ball Receipt*   |   -   | [43.6, 36.0]    | Incomplete |
|  +3.70 |  +3.46 | 00:39:15.106 | Portugal           | Georgia            | 59 | Ball Recovery   |   -   | [70.7, 39.0]    |  |
|  +3.70 |  +3.46 | 00:39:15.106 | Portugal           | Georgia            | 59 | Carry           |   -   | [70.7, 39.0]    |  |
|  +4.16 |  +3.93 | 00:39:15.570 | Georgia            | Georgia            | 59 | Pressure        |  Yes  | [48.8, 37.2]    |  |
|  +9.16 |  +8.92 | 00:39:20.565 | Portugal           | Georgia            | 59 | Pass            |   -   | [82.9, 36.1]    | -> João Félix Seq |
| +10.42 | +10.19 | 00:39:21.830 | Portugal           | Georgia            | 59 | Ball Receipt*   |   -   | [84.3, 21.0]    |  |

---

### Disagreement Case 70: `3930172_p51_93ca7e9c`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3930172 (UEFA Euro, 2024)
- **counterpressing_team**: Spain
- **opponent_team_at_turnover**: Italy
- **possession_team_at_counterpress_initiation**: Italy
- **possession_id_at_counterpress_initiation**: 51
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:29:01.503) | **Initiation**: Pressure (00:29:01.743)
- **Initiation Delay**: 0.24s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.463s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.34 |  -2.58 | 00:28:59.164 | Italy              | Spain              | 50 | Pressure        |   -   | [28.7, 75.4]    |  |
|  -0.75 |  -0.99 | 00:29:00.757 | Spain              | Spain              | 50 | Pass            |   -   | [92.9, 3.5]     | Incomplete (Incomplete) |
|  +0.00 |  -0.24 | 00:29:01.503 | Spain              | Spain              | 50 | Ball Receipt*   |   -   | [98.9, 2.9]     | Incomplete |
|  +0.00 |  -0.24 | 00:29:01.503 | Italy              | Italy              | 51 | Interception    |  Yes  | [21.2, 79.0]    | Won |
|  +0.00 |  -0.24 | 00:29:01.503 | Italy              | Italy              | 51 | Carry           |   -   | [21.2, 79.0]    |  |
|  +0.24 |  +0.00 | 00:29:01.743 | Spain              | Italy              | 51 | Pressure        |  Yes  | [98.9, 2.4]     |  |
|  +0.70 |  +0.46 | 00:29:02.206 | Italy              | Italy              | 51 | Dispossessed    |   -   | [22.5, 77.7]    |  |
|  +0.70 |  +0.46 | 00:29:02.206 | Spain              | Italy              | 51 | Duel            |  Yes  | [97.6, 2.4]     | Tackle, Success In Play |
|  +1.29 |  +1.05 | 00:29:02.789 | Spain              | Italy              | 51 | Pass            |   -   | [96.7, 3.5]     | Incomplete (Incomplete) |
|  +2.25 |  +2.01 | 00:29:03.757 | Spain              | Italy              | 51 | Pressure        |  Yes  | [105.9, 5.5]    |  |
|  +3.24 |  +3.00 | 00:29:04.747 | Spain              | Italy              | 51 | Ball Receipt*   |   -   | [107.7, 4.4]    | Incomplete |
|  +3.24 |  +3.00 | 00:29:04.747 | Spain              | Italy              | 51 | Foul Committed  |  Yes  | [109.1, 6.5]    |  |
|  +3.24 |  +3.00 | 00:29:04.747 | Italy              | Italy              | 51 | Foul Won        |   -   | [11.0, 73.6]    |  |
| +27.84 | +27.60 | 00:29:29.341 | Italy              | Italy              | 52 | Pass            |   -   | [9.1, 70.2]     | -> Jorge Luiz Fre |
| +29.07 | +28.83 | 00:29:30.575 | Italy              | Italy              | 52 | Ball Receipt*   |   -   | [29.2, 65.0]    |  |
| +29.07 | +28.83 | 00:29:30.575 | Italy              | Italy              | 52 | Carry           |   -   | [29.2, 65.0]    |  |
| +30.09 | +29.85 | 00:29:31.588 | Spain              | Italy              | 52 | Pressure        |   -   | [94.0, 15.1]    |  |

---

### Disagreement Case 71: `3857276_p12_fcc6b2e3`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3857276 (FIFA World Cup, 2022)
- **counterpressing_team**: Morocco
- **opponent_team_at_turnover**: Canada
- **possession_team_at_counterpress_initiation**: Canada
- **possession_id_at_counterpress_initiation**: 12
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:05:49.229) | **Initiation**: Pressure (00:05:49.485)
- **Initiation Delay**: 0.256s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.892s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.98 |  -2.24 | 00:05:47.247 | Morocco            | Morocco            | 11 | Ball Receipt*   |   -   | [42.3, 8.4]     |  |
|  -1.98 |  -2.24 | 00:05:47.247 | Canada             | Morocco            | 11 | Duel            |   -   | [76.8, 71.2]    | Aerial Lost |
|  -1.98 |  -2.24 | 00:05:47.247 | Morocco            | Morocco            | 11 | Pass            |   -   | [43.3, 8.9]     | Incomplete (Incomplete) |
|  +0.00 |  -0.26 | 00:05:49.229 | Canada             | Canada             | 12 | Ball Recovery   |   -   | [55.5, 68.8]    |  |
|  +0.00 |  -0.26 | 00:05:49.229 | Canada             | Canada             | 12 | Carry           |   -   | [55.5, 68.8]    |  |
|  +0.26 |  +0.00 | 00:05:49.485 | Morocco            | Canada             | 12 | Pressure        |  Yes  | [63.1, 11.3]    |  |
|  +0.66 |  +0.40 | 00:05:49.885 | Canada             | Canada             | 12 | Pass            |   -   | [56.0, 68.8]    | -> Steven de Sous |
|  +2.05 |  +1.80 | 00:05:51.283 | Canada             | Canada             | 12 | Ball Receipt*   |   -   | [42.3, 59.4]    |  |
|  +2.05 |  +1.80 | 00:05:51.283 | Canada             | Canada             | 12 | Pass            |   -   | [42.8, 59.4]    | -> Mark Anthony K |
|  +2.98 |  +2.73 | 00:05:52.212 | Canada             | Canada             | 12 | Ball Receipt*   |   -   | [54.9, 50.2]    |  |
|  +2.98 |  +2.73 | 00:05:52.212 | Canada             | Canada             | 12 | Carry           |   -   | [54.9, 50.2]    |  |
|  +3.06 |  +2.81 | 00:05:52.293 | Canada             | Canada             | 12 | Miscontrol      |   -   | [54.9, 50.2]    |  |
|  +4.15 |  +3.89 | 00:05:53.377 | Morocco            | Canada             | 12 | Ball Recovery   |   -   | [53.2, 31.2]    |  |
|  +4.15 |  +3.89 | 00:05:53.377 | Morocco            | Canada             | 12 | Carry           |   -   | [53.2, 31.2]    |  |
|  +4.79 |  +4.53 | 00:05:54.016 | Canada             | Canada             | 12 | Pressure        |  Yes  | [62.2, 49.2]    |  |
|  +5.20 |  +4.94 | 00:05:54.427 | Morocco            | Canada             | 12 | Pass            |   -   | [57.4, 33.0]    | Incomplete (Out) |
|  +9.48 |  +9.22 | 00:05:58.705 | Morocco            | Canada             | 12 | Ball Receipt*   |   -   | [92.9, 3.9]     | Incomplete |
| +26.44 | +26.19 | 00:06:15.673 | Canada             | Canada             | 13 | Pass            |   -   | [30.5, 80.0]    | -> Cyle Larin |

---

### Disagreement Case 72: `3838004_p80_9882f82b`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3838004 (Ligue 1, 2022/2023)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Strasbourg
- **possession_team_at_counterpress_initiation**: Strasbourg
- **possession_id_at_counterpress_initiation**: 80
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:09:28.816) | **Initiation**: Duel (00:09:29.098)
- **Initiation Delay**: 0.282s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.494s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.61 |  -0.89 | 00:09:28.203 | Paris Saint-Germai | Paris Saint-Germai | 79 | Pass            |   -   | [102.5, 65.7]   | Incomplete (Incomplete) |
|  +0.00 |  -0.28 | 00:09:28.816 | Paris Saint-Germai | Paris Saint-Germai | 79 | Ball Receipt*   |   -   | [106.7, 58.4]   | Incomplete |
|  +0.00 |  -0.28 | 00:09:28.816 | Strasbourg         | Strasbourg         | 80 | Interception    |  Yes  | [13.4, 18.0]    | Won |
|  +0.00 |  -0.28 | 00:09:28.816 | Strasbourg         | Strasbourg         | 80 | Carry           |   -   | [13.4, 18.0]    |  |
|  +0.28 |  +0.00 | 00:09:29.098 | Strasbourg         | Strasbourg         | 80 | Dribble         |   -   | [13.0, 19.8]    |  |
|  +0.28 |  +0.00 | 00:09:29.098 | Paris Saint-Germai | Strasbourg         | 80 | Duel            |  Yes  | [107.1, 60.3]   | Tackle, Lost In Play |
|  +0.86 |  +0.58 | 00:09:29.678 | Strasbourg         | Strasbourg         | 80 | Pass            |   -   | [13.6, 15.4]    | -> Morgan Sanson |
|  +2.31 |  +2.03 | 00:09:31.129 | Strasbourg         | Strasbourg         | 80 | Ball Receipt*   |   -   | [22.9, 23.9]    |  |
|  +2.31 |  +2.03 | 00:09:31.129 | Strasbourg         | Strasbourg         | 80 | Carry           |   -   | [22.9, 23.9]    |  |
|  +2.79 |  +2.51 | 00:09:31.611 | Paris Saint-Germai | Strasbourg         | 80 | Pressure        |  Yes  | [90.6, 51.6]    |  |
|  +3.78 |  +3.49 | 00:09:32.592 | Strasbourg         | Strasbourg         | 80 | Dribble         |   -   | [29.5, 26.5]    |  |
|  +3.78 |  +3.49 | 00:09:32.592 | Paris Saint-Germai | Strasbourg         | 80 | Duel            |  Yes  | [90.6, 53.6]    | Tackle, Success In Play |
|  +4.00 |  +3.72 | 00:09:32.818 | Strasbourg         | Strasbourg         | 80 | Pressure        |  Yes  | [36.7, 26.1]    |  |
|  +4.37 |  +4.08 | 00:09:33.182 | Paris Saint-Germai | Strasbourg         | 80 | Ball Recovery   |   -   | [83.4, 56.2]    |  |
|  +4.37 |  +4.08 | 00:09:33.182 | Paris Saint-Germai | Strasbourg         | 80 | Carry           |   -   | [83.4, 56.2]    |  |
|  +6.11 |  +5.83 | 00:09:34.925 | Strasbourg         | Strasbourg         | 80 | Pressure        |  Yes  | [33.1, 25.5]    |  |
|  +6.46 |  +6.17 | 00:09:35.272 | Paris Saint-Germai | Strasbourg         | 80 | Pass            |   -   | [91.0, 53.0]    | Incomplete (Out) |
|  +9.21 |  +8.93 | 00:09:38.023 | Paris Saint-Germai | Strasbourg         | 80 | Ball Receipt*   |   -   | [112.5, 32.6]   | Incomplete |
| +32.31 | +32.03 | 00:10:01.131 | Strasbourg         | Strasbourg         | 81 | Pass            |   -   | [7.0, 44.1]     | -> Ismael Doukour |

---

### Disagreement Case 73: `3998846_p150_2cf00bd2`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3998846 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Portugal Women's
- **opponent_team_at_turnover**: Italy Women's
- **possession_team_at_counterpress_initiation**: Italy Women's
- **possession_id_at_counterpress_initiation**: 150
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:32:15.657) | **Initiation**: Dribbled Past (00:32:15.989)
- **Initiation Delay**: 0.332s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 12.023s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.109s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.06 |  -1.39 | 00:32:14.596 | Portugal Women's   | Portugal Women's   | 149 | Ball Receipt*   |   -   | [94.9, 27.1]    |  |
|  -1.06 |  -1.39 | 00:32:14.596 | Portugal Women's   | Portugal Women's   | 149 | Miscontrol      |   -   | [94.9, 28.0]    |  |
|  -0.34 |  -0.67 | 00:32:15.320 | Portugal Women's   | Portugal Women's   | 149 | Pressure        |   -   | [94.9, 29.3]    |  |
|  +0.00 |  -0.33 | 00:32:15.657 | Italy Women's      | Italy Women's      | 150 | Ball Recovery   |   -   | [25.5, 48.1]    |  |
|  +0.00 |  -0.33 | 00:32:15.657 | Italy Women's      | Italy Women's      | 150 | Carry           |   -   | [25.5, 48.1]    |  |
|  +0.33 |  +0.00 | 00:32:15.989 | Portugal Women's   | Italy Women's      | 150 | Dribbled Past   |  Yes  | [94.0, 29.7]    |  |
|  +0.33 |  +0.00 | 00:32:15.989 | Italy Women's      | Italy Women's      | 150 | Dribble         |   -   | [26.1, 50.4]    |  |
|  +0.33 |  +0.00 | 00:32:15.989 | Italy Women's      | Italy Women's      | 150 | Carry           |   -   | [26.1, 50.4]    |  |
|  +1.49 |  +1.16 | 00:32:17.149 | Portugal Women's   | Italy Women's      | 150 | Pressure        |  Yes  | [91.5, 23.5]    |  |
|  +2.44 |  +2.11 | 00:32:18.098 | Italy Women's      | Italy Women's      | 150 | Dribble         |   -   | [28.9, 54.7]    |  |
|  +2.44 |  +2.11 | 00:32:18.098 | Portugal Women's   | Italy Women's      | 150 | Duel            |  Yes  | [91.2, 25.4]    | Tackle, Success In Play |
|  +3.72 |  +3.38 | 00:32:19.372 | Portugal Women's   | Italy Women's      | 150 | Pass            |   -   | [85.7, 26.6]    | Incomplete (Incomplete) |
|  +5.33 |  +5.00 | 00:32:20.989 | Portugal Women's   | Italy Women's      | 150 | Pressure        |   -   | [77.0, 9.3]     |  |
|  +5.61 |  +5.28 | 00:32:21.269 | Portugal Women's   | Italy Women's      | 150 | Ball Receipt*   |   -   | [77.5, 12.5]    | Incomplete |
|  +5.61 |  +5.28 | 00:32:21.269 | Italy Women's      | Italy Women's      | 150 | Ball Recovery   |   -   | [41.7, 69.1]    |  |
|  +5.61 |  +5.28 | 00:32:21.269 | Italy Women's      | Italy Women's      | 150 | Carry           |   -   | [41.7, 69.1]    |  |
|  +7.09 |  +6.75 | 00:32:22.743 | Portugal Women's   | Italy Women's      | 150 | Pressure        |   -   | [76.6, 9.9]     |  |
|  +7.46 |  +7.12 | 00:32:23.112 | Portugal Women's   | Italy Women's      | 150 | Dribbled Past   |   -   | [75.4, 8.9]     |  |
|  +7.46 |  +7.12 | 00:32:23.112 | Italy Women's      | Italy Women's      | 150 | Dribble         |   -   | [44.7, 71.2]    |  |
|  +7.46 |  +7.12 | 00:32:23.112 | Italy Women's      | Italy Women's      | 150 | Carry           |   -   | [44.7, 71.2]    |  |
|  +8.32 |  +7.99 | 00:32:23.978 | Portugal Women's   | Italy Women's      | 150 | Pressure        |   -   | [76.3, 6.9]     |  |
| +11.48 | +11.15 | 00:32:27.136 | Portugal Women's   | Italy Women's      | 150 | Pressure        |   -   | [84.3, 3.5]     |  |
| +11.96 | +11.63 | 00:32:27.615 | Italy Women's      | Italy Women's      | 150 | Pass            |   -   | [36.9, 77.5]    | Incomplete (Incomplete) |

---

### Disagreement Case 74: `3835325_p16_65524e0d`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3835325 (UEFA Women's Euro, 2022)
- **counterpressing_team**: Italy Women's
- **opponent_team_at_turnover**: France Women's
- **possession_team_at_counterpress_initiation**: France Women's
- **possession_id_at_counterpress_initiation**: 16
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:05:50.739) | **Initiation**: Duel (00:05:51.081)
- **Initiation Delay**: 0.342s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.446s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.28 |  -1.62 | 00:05:49.459 | France Women's     | Italy Women's      | 15 | Block           |   -   | [70.0, 50.8]    |  |
|  -0.13 |  -0.47 | 00:05:50.609 | Italy Women's      | Italy Women's      | 15 | Pressure        |   -   | [48.2, 32.3]    |  |
|  +0.00 |  -0.34 | 00:05:50.739 | France Women's     | France Women's     | 16 | Ball Recovery   |   -   | [70.0, 49.3]    |  |
|  +0.00 |  -0.34 | 00:05:50.739 | France Women's     | France Women's     | 16 | Carry           |   -   | [70.0, 49.3]    |  |
|  +0.34 |  +0.00 | 00:05:51.081 | France Women's     | France Women's     | 16 | Dispossessed    |   -   | [70.0, 49.8]    |  |
|  +0.34 |  +0.00 | 00:05:51.081 | Italy Women's      | France Women's     | 16 | Duel            |  Yes  | [50.1, 30.3]    | Tackle, Lost In Play |
|  +1.87 |  +1.53 | 00:05:52.609 | Italy Women's      | France Women's     | 16 | Pressure        |  Yes  | [52.4, 28.4]    |  |
|  +2.16 |  +1.82 | 00:05:52.899 | France Women's     | France Women's     | 16 | Pass            |   -   | [65.3, 51.9]    | -> Onema Grace Ge |
|  +2.28 |  +1.94 | 00:05:53.019 | France Women's     | France Women's     | 16 | Ball Receipt*   |   -   | [66.4, 49.6]    |  |
|  +2.28 |  +1.94 | 00:05:53.019 | France Women's     | France Women's     | 16 | Carry           |   -   | [66.4, 49.6]    |  |
|  +2.36 |  +2.02 | 00:05:53.099 | France Women's     | France Women's     | 16 | Miscontrol      |   -   | [65.7, 51.1]    |  |
|  +3.79 |  +3.45 | 00:05:54.527 | Italy Women's      | France Women's     | 16 | Ball Recovery   |   -   | [57.4, 15.8]    |  |
|  +3.79 |  +3.45 | 00:05:54.527 | Italy Women's      | France Women's     | 16 | Carry           |   -   | [57.4, 15.8]    |  |
|  +8.53 |  +8.19 | 00:05:59.271 | Italy Women's      | France Women's     | 16 | Pass            |   -   | [54.4, 28.0]    | Incomplete (Incomplete) |
|  +9.16 |  +8.82 | 00:05:59.899 | Italy Women's      | France Women's     | 16 | Ball Receipt*   |   -   | [68.5, 42.1]    | Incomplete |
|  +9.16 |  +8.82 | 00:05:59.899 | France Women's     | France Women's     | 16 | Interception    |   -   | [58.0, 43.1]    | Won |
|  +9.16 |  +8.82 | 00:05:59.899 | France Women's     | France Women's     | 16 | Carry           |   -   | [58.0, 43.1]    |  |

---

### Disagreement Case 75: `3857300_p5_b2b69063`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3857300 (FIFA World Cup, 2022)
- **counterpressing_team**: Saudi Arabia
- **opponent_team_at_turnover**: Argentina
- **possession_team_at_counterpress_initiation**: Argentina
- **possession_id_at_counterpress_initiation**: 5
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:02:35.558) | **Initiation**: Pressure (00:02:35.917)
- **Initiation Delay**: 0.359s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.925s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.16 |  -1.52 | 00:02:34.398 | Saudi Arabia       | Saudi Arabia       | 4 | Ball Receipt*   |   -   | [72.8, 53.2]    |  |
|  -1.16 |  -1.52 | 00:02:34.398 | Saudi Arabia       | Saudi Arabia       | 4 | Carry           |   -   | [72.8, 53.2]    |  |
|  -0.54 |  -0.90 | 00:02:35.016 | Saudi Arabia       | Saudi Arabia       | 4 | Miscontrol      |   -   | [73.9, 53.9]    |  |
|  +0.00 |  -0.36 | 00:02:35.558 | Argentina          | Argentina          | 5 | Ball Recovery   |   -   | [51.2, 24.4]    |  |
|  +0.00 |  -0.36 | 00:02:35.558 | Argentina          | Argentina          | 5 | Carry           |   -   | [51.2, 24.4]    |  |
|  +0.36 |  +0.00 | 00:02:35.917 | Saudi Arabia       | Argentina          | 5 | Pressure        |  Yes  | [73.4, 58.1]    |  |
|  +1.05 |  +0.69 | 00:02:36.607 | Argentina          | Argentina          | 5 | Dispossessed    |   -   | [50.0, 28.9]    |  |
|  +1.05 |  +0.69 | 00:02:36.607 | Saudi Arabia       | Argentina          | 5 | Duel            |  Yes  | [70.1, 51.2]    | Tackle, Lost In Play |
|  +2.27 |  +1.91 | 00:02:37.824 | Saudi Arabia       | Argentina          | 5 | Pressure        |  Yes  | [66.0, 44.8]    |  |
|  +2.50 |  +2.14 | 00:02:38.055 | Argentina          | Argentina          | 5 | Ball Recovery   |   -   | [56.6, 38.0]    |  |
|  +2.50 |  +2.14 | 00:02:38.055 | Argentina          | Argentina          | 5 | Carry           |   -   | [56.6, 38.0]    |  |
|  +3.28 |  +2.92 | 00:02:38.842 | Argentina          | Argentina          | 5 | Dribble         |   -   | [58.8, 37.5]    |  |
|  +3.28 |  +2.92 | 00:02:38.842 | Saudi Arabia       | Argentina          | 5 | Duel            |  Yes  | [61.3, 42.6]    | Tackle, Lost In Play |
|  +4.57 |  +4.21 | 00:02:40.124 | Saudi Arabia       | Argentina          | 5 | 50/50           |  Yes  | [63.5, 43.9]    |  |
|  +4.57 |  +4.21 | 00:02:40.124 | Argentina          | Argentina          | 5 | 50/50           |   -   | [56.6, 36.2]    |  |
|  +5.59 |  +5.24 | 00:02:41.153 | Argentina          | Argentina          | 5 | Pressure        |   -   | [56.6, 31.7]    |  |
|  +5.63 |  +5.27 | 00:02:41.188 | Saudi Arabia       | Argentina          | 5 | Pass            |   -   | [63.5, 48.4]    | Incomplete (Incomplete) |
|  +6.04 |  +5.68 | 00:02:41.594 | Saudi Arabia       | Argentina          | 5 | Ball Receipt*   |   -   | [71.0, 48.4]    | Incomplete |
|  +6.04 |  +5.68 | 00:02:41.594 | Argentina          | Argentina          | 5 | Foul Committed  |   -   | [52.8, 32.3]    |  |
| +29.37 | +29.01 | 00:03:04.923 | Saudi Arabia       | Saudi Arabia       | 6 | Pass            |   -   | [68.5, 49.1]    | -> Salman Mohamme |
| +30.08 | +29.72 | 00:03:05.637 | Saudi Arabia       | Saudi Arabia       | 6 | Ball Receipt*   |   -   | [69.4, 56.1]    |  |

---

### Disagreement Case 76: `3893827_p136_5abad41a`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893827 (Women's World Cup, 2023)
- **counterpressing_team**: Vietnam Women's
- **opponent_team_at_turnover**: Netherlands Women's
- **possession_team_at_counterpress_initiation**: Netherlands Women's
- **possession_id_at_counterpress_initiation**: 136
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:19:40.016) | **Initiation**: Pressure (00:19:40.398)
- **Initiation Delay**: 0.382s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.669s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.88 |  -3.26 | 00:19:37.135 | Vietnam Women's    | Vietnam Women's    | 135 | Pass            |   -   | [7.0, 36.1]     | -> Thị Vân Dương |
|  -1.09 |  -1.47 | 00:19:38.929 | Vietnam Women's    | Vietnam Women's    | 135 | Ball Receipt*   |   -   | [40.1, 19.0]    |  |
|  -1.09 |  -1.47 | 00:19:38.929 | Vietnam Women's    | Vietnam Women's    | 135 | Pass            |   -   | [38.3, 19.6]    | Incomplete (Incomplete) |
|  +0.00 |  -0.38 | 00:19:40.016 | Netherlands Women' | Netherlands Women' | 136 | Ball Recovery   |   -   | [72.8, 63.1]    |  |
|  +0.00 |  -0.38 | 00:19:40.016 | Netherlands Women' | Netherlands Women' | 136 | Carry           |   -   | [72.8, 63.1]    |  |
|  +0.38 |  +0.00 | 00:19:40.398 | Vietnam Women's    | Netherlands Women' | 136 | Pressure        |  Yes  | [47.5, 17.0]    |  |
|  +1.05 |  +0.67 | 00:19:41.067 | Netherlands Women' | Netherlands Women' | 136 | Dispossessed    |   -   | [72.5, 63.9]    |  |
|  +1.05 |  +0.67 | 00:19:41.067 | Vietnam Women's    | Netherlands Women' | 136 | Duel            |  Yes  | [47.6, 16.2]    | Tackle, Success In Play |
|  +2.28 |  +1.90 | 00:19:42.300 | Vietnam Women's    | Netherlands Women' | 136 | Pass            |   -   | [47.6, 11.8]    | Incomplete (Incomplete) |
|  +3.58 |  +3.19 | 00:19:43.592 | Vietnam Women's    | Netherlands Women' | 136 | Ball Receipt*   |   -   | [59.2, 14.9]    | Incomplete |
|  +3.58 |  +3.19 | 00:19:43.592 | Netherlands Women' | Netherlands Women' | 136 | Ball Recovery   |   -   | [58.7, 66.3]    |  |
|  +3.58 |  +3.19 | 00:19:43.592 | Netherlands Women' | Netherlands Women' | 136 | Carry           |   -   | [58.7, 66.3]    |  |
|  +6.18 |  +5.80 | 00:19:46.197 | Netherlands Women' | Netherlands Women' | 136 | Pass            |   -   | [69.8, 58.5]    | Incomplete (Incomplete) |
|  +7.99 |  +7.60 | 00:19:48.002 | Netherlands Women' | Netherlands Women' | 136 | Ball Receipt*   |   -   | [89.5, 58.8]    | Incomplete |
|  +7.99 |  +7.60 | 00:19:48.002 | Vietnam Women's    | Netherlands Women' | 136 | Pass            |   -   | [22.5, 29.8]    | Incomplete (Incomplete) |
|  +9.72 |  +9.34 | 00:19:49.735 | Vietnam Women's    | Netherlands Women' | 136 | Ball Receipt*   |   -   | [40.1, 22.7]    | Incomplete |
|  +9.72 |  +9.34 | 00:19:49.735 | Netherlands Women' | Netherlands Women' | 136 | Ball Recovery   |   -   | [74.5, 61.1]    |  |

---

### Disagreement Case 77: `3895333_p51_6cf64705`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895333 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: Eintracht Frankfurt
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 51
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:29:52.031) | **Initiation**: Pressure (00:29:52.423)
- **Initiation Delay**: 0.392s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.372s) | Evidence: `goalkeeper_control` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.68 |  -2.07 | 00:29:50.355 | Eintracht Frankfur | Eintracht Frankfur | 50 | Ball Receipt*   |   -   | [32.7, 61.7]    |  |
|  -1.68 |  -2.07 | 00:29:50.355 | Eintracht Frankfur | Eintracht Frankfur | 50 | Carry           |   -   | [32.7, 61.7]    |  |
|  +0.00 |  -0.39 | 00:29:52.031 | Eintracht Frankfur | Eintracht Frankfur | 50 | Dispossessed    |   -   | [32.7, 62.2]    |  |
|  +0.00 |  -0.39 | 00:29:52.031 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Duel            |  Yes  | [87.4, 17.9]    | Tackle, Won |
|  +0.00 |  -0.39 | 00:29:52.031 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Carry           |   -   | [87.4, 17.9]    |  |
|  +0.39 |  +0.00 | 00:29:52.423 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Pressure        |  Yes  | [33.4, 61.4]    |  |
|  +0.91 |  +0.52 | 00:29:52.940 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Pass            |   -   | [86.7, 20.8]    | -> Jonas Hofmann |
|  +2.24 |  +1.85 | 00:29:54.272 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Ball Receipt*   |   -   | [92.4, 30.1]    |  |
|  +2.24 |  +1.85 | 00:29:54.272 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Carry           |   -   | [92.4, 30.1]    |  |
|  +3.86 |  +3.47 | 00:29:55.889 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Shot            |   -   | [94.9, 37.7]    | Saved |
|  +4.01 |  +3.61 | 00:29:56.037 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Block           |  Yes  | [21.0, 41.8]    |  |
|  +4.76 |  +4.37 | 00:29:56.795 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Goal Keeper     |   -   | [1.4, 39.3]     |  |
|  +7.58 |  +7.18 | 00:29:59.606 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Ball Recovery   |   -   | [1.5, 24.2]     |  |
|  +7.58 |  +7.18 | 00:29:59.606 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Carry           |   -   | [1.5, 24.2]     |  |
| +27.15 | +26.76 | 00:30:19.185 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Pass            |   -   | [16.8, 33.3]    | Incomplete (Incomplete) |
| +30.93 | +30.54 | 00:30:22.966 | Eintracht Frankfur | Bayer Leverkusen   | 51 | Ball Receipt*   |   -   | [77.4, 27.9]    | Incomplete |
| +30.93 | +30.54 | 00:30:22.966 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Pass            |   -   | [44.1, 53.0]    | -> Exequiel Aleja |

---

### Disagreement Case 78: `3893812_p15_15b09d29`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893812 (Women's World Cup, 2023)
- **counterpressing_team**: Argentina Women's
- **opponent_team_at_turnover**: South Africa Women's
- **possession_team_at_counterpress_initiation**: South Africa Women's
- **possession_id_at_counterpress_initiation**: 15
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:04:46.278) | **Initiation**: Pressure (00:04:46.672)
- **Initiation Delay**: 0.394s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.007s) | Evidence: `completed_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.35 |  -2.75 | 00:04:43.927 | South Africa Women | Argentina Women's  | 14 | Pressure        |   -   | [55.0, 22.7]    |  |
|  -2.06 |  -2.46 | 00:04:44.215 | Argentina Women's  | Argentina Women's  | 14 | Ball Receipt*   |   -   | [62.3, 55.1]    |  |
|  -2.06 |  -2.46 | 00:04:44.215 | Argentina Women's  | Argentina Women's  | 14 | Carry           |   -   | [62.3, 55.1]    |  |
|  -1.73 |  -2.12 | 00:04:44.547 | Argentina Women's  | Argentina Women's  | 14 | Miscontrol      |   -   | [64.3, 59.4]    |  |
|  +0.00 |  -0.39 | 00:04:46.278 | South Africa Women | South Africa Women | 15 | Pass            |   -   | [49.7, 22.0]    | -> Karabo Dhlamin |
|  +0.39 |  +0.00 | 00:04:46.672 | Argentina Women's  | South Africa Women | 15 | Pressure        |  Yes  | [69.6, 62.2]    |  |
|  +0.69 |  +0.29 | 00:04:46.967 | South Africa Women | South Africa Women | 15 | Ball Receipt*   |   -   | [47.0, 14.8]    |  |
|  +0.69 |  +0.29 | 00:04:46.967 | South Africa Women | South Africa Women | 15 | Carry           |   -   | [47.0, 14.8]    |  |
|  +1.29 |  +0.89 | 00:04:47.565 | South Africa Women | South Africa Women | 15 | Pass            |   -   | [47.5, 14.8]    | -> Bongeka Gamede |
|  +2.03 |  +1.64 | 00:04:48.310 | Argentina Women's  | South Africa Women | 15 | Pressure        |  Yes  | [62.5, 58.6]    |  |
|  +2.70 |  +2.31 | 00:04:48.982 | South Africa Women | South Africa Women | 15 | Ball Receipt*   |   -   | [54.1, 19.8]    |  |
|  +2.70 |  +2.31 | 00:04:48.982 | South Africa Women | South Africa Women | 15 | Pass            |   -   | [54.4, 19.3]    | Incomplete (Incomplete) |
|  +3.40 |  +3.01 | 00:04:49.679 | South Africa Women | South Africa Women | 15 | Ball Receipt*   |   -   | [59.6, 8.3]     | Incomplete |
|  +3.40 |  +3.01 | 00:04:49.679 | Argentina Women's  | South Africa Women | 15 | Pass            |   -   | [57.2, 70.2]    | -> María Florenci |
|  +4.63 |  +4.23 | 00:04:50.906 | Argentina Women's  | South Africa Women | 15 | Ball Receipt*   |   -   | [74.8, 65.8]    |  |
|  +4.63 |  +4.23 | 00:04:50.906 | Argentina Women's  | South Africa Women | 15 | Carry           |   -   | [74.8, 65.8]    |  |
|  +5.30 |  +4.91 | 00:04:51.580 | South Africa Women | South Africa Women | 15 | Pressure        |  Yes  | [46.0, 18.3]    |  |
|  +6.17 |  +5.78 | 00:04:52.449 | Argentina Women's  | South Africa Women | 15 | Miscontrol      |   -   | [74.7, 66.8]    |  |
|  +7.01 |  +6.62 | 00:04:53.289 | South Africa Women | South Africa Women | 15 | Ball Recovery   |   -   | [46.8, 22.3]    |  |
|  +7.01 |  +6.62 | 00:04:53.289 | South Africa Women | South Africa Women | 15 | Carry           |   -   | [46.8, 22.3]    |  |
|  +8.50 |  +8.10 | 00:04:54.777 | South Africa Women | South Africa Women | 15 | Pass            |   -   | [38.0, 23.5]    | -> Karabo Dhlamin |
|  +9.36 |  +8.96 | 00:04:55.634 | South Africa Women | South Africa Women | 15 | Ball Receipt*   |   -   | [33.5, 11.5]    |  |
|  +9.36 |  +8.96 | 00:04:55.634 | South Africa Women | South Africa Women | 15 | Carry           |   -   | [33.5, 11.5]    |  |

---

### Disagreement Case 79: `3901796_p74_77886236`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3901796 (Women's World Cup, 2023)
- **counterpressing_team**: Netherlands Women's
- **opponent_team_at_turnover**: South Africa Women's
- **possession_team_at_counterpress_initiation**: South Africa Women's
- **possession_id_at_counterpress_initiation**: 74
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:47:02.509) | **Initiation**: Pressure (00:47:02.910)
- **Initiation Delay**: 0.401s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.266s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.01 |  -1.41 | 00:47:01.503 | South Africa Women | Netherlands Women' | 73 | Ball Receipt*   |   -   | [81.3, 25.2]    | Incomplete |
|  -1.01 |  -1.41 | 00:47:01.503 | Netherlands Women' | Netherlands Women' | 73 | Pass            |   -   | [39.2, 67.7]    | Incomplete (Incomplete) |
|  +0.00 |  -0.40 | 00:47:02.509 | Netherlands Women' | Netherlands Women' | 73 | Ball Receipt*   |   -   | [56.1, 58.1]    | Incomplete |
|  +0.00 |  -0.40 | 00:47:02.509 | South Africa Women | South Africa Women | 74 | Ball Recovery   |   -   | [64.0, 24.3]    |  |
|  +0.00 |  -0.40 | 00:47:02.509 | South Africa Women | South Africa Women | 74 | Carry           |   -   | [64.0, 24.3]    |  |
|  +0.40 |  +0.00 | 00:47:02.910 | Netherlands Women' | South Africa Women | 74 | Pressure        |  Yes  | [55.2, 57.3]    |  |
|  +1.35 |  +0.95 | 00:47:03.861 | Netherlands Women' | South Africa Women | 74 | Pressure        |  Yes  | [54.2, 54.5]    |  |
|  +1.67 |  +1.27 | 00:47:04.176 | South Africa Women | South Africa Women | 74 | Dispossessed    |   -   | [65.9, 23.5]    |  |
|  +1.67 |  +1.27 | 00:47:04.176 | Netherlands Women' | South Africa Women | 74 | Duel            |  Yes  | [54.2, 56.6]    | Tackle, Success In Play |
|  +2.67 |  +2.27 | 00:47:05.181 | South Africa Women | South Africa Women | 74 | Pressure        |   -   | [65.1, 19.0]    |  |
|  +3.24 |  +2.84 | 00:47:05.752 | Netherlands Women' | South Africa Women | 74 | Pass            |   -   | [58.0, 66.0]    | Incomplete (Incomplete) |
|  +3.47 |  +3.06 | 00:47:05.974 | South Africa Women | South Africa Women | 74 | Block           |   -   | [58.9, 13.9]    |  |
|  +4.50 |  +4.10 | 00:47:07.010 | South Africa Women | South Africa Women | 74 | Ball Recovery   |   -   | [79.4, 15.1]    |  |
| +21.41 | +21.01 | 00:47:23.920 | Netherlands Women' | Netherlands Women' | 75 | Pass            |   -   | [41.8, 80.0]    | Incomplete (Unknown) |
| +22.43 | +22.03 | 00:47:24.942 | South Africa Women | Netherlands Women' | 75 | Pressure        |   -   | [47.1, 8.7]     |  |
| +22.93 | +22.52 | 00:47:25.434 | Netherlands Women' | Netherlands Women' | 75 | Ball Receipt*   |   -   | [71.6, 66.6]    | Incomplete |
| +22.93 | +22.52 | 00:47:25.434 | South Africa Women | Netherlands Women' | 75 | Foul Committed  |   -   | [46.2, 8.1]     |  |

---

### Disagreement Case 80: `3901797_p103_dd1334f4`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3901797 (Women's World Cup, 2023)
- **counterpressing_team**: Sweden Women's
- **opponent_team_at_turnover**: United States Women's
- **possession_team_at_counterpress_initiation**: United States Women's
- **possession_id_at_counterpress_initiation**: 103
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:02:29.056) | **Initiation**: Pressure (00:02:29.472)
- **Initiation Delay**: 0.416s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.18s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.64 |  -3.06 | 00:02:26.413 | Sweden Women's     | Sweden Women's     | 102 | Pass            |   -   | [92.3, 80.0]    | -> Kosovare Aslla |
|  -1.27 |  -1.69 | 00:02:27.783 | Sweden Women's     | Sweden Women's     | 102 | Ball Receipt*   |   -   | [105.5, 69.2]   |  |
|  -1.27 |  -1.69 | 00:02:27.783 | Sweden Women's     | Sweden Women's     | 102 | Carry           |   -   | [105.5, 69.2]   |  |
|  -1.20 |  -1.62 | 00:02:27.852 | Sweden Women's     | Sweden Women's     | 102 | Miscontrol      |   -   | [106.4, 68.0]   |  |
|  +0.00 |  -0.42 | 00:02:29.056 | United States Wome | United States Wome | 103 | Pass            |   -   | [15.1, 8.0]     | -> Crystal Alyssi |
|  +0.42 |  +0.00 | 00:02:29.472 | Sweden Women's     | United States Wome | 103 | Pressure        |  Yes  | [105.7, 77.3]   |  |
|  +0.59 |  +0.17 | 00:02:29.645 | United States Wome | United States Wome | 103 | Ball Receipt*   |   -   | [8.5, 1.7]      |  |
|  +0.59 |  +0.17 | 00:02:29.645 | United States Wome | United States Wome | 103 | Carry           |   -   | [8.5, 1.7]      |  |
|  +0.77 |  +0.35 | 00:02:29.827 | United States Wome | United States Wome | 103 | Pass            |   -   | [11.2, 3.0]     | -> Alexandra Morg |
|  +1.65 |  +1.23 | 00:02:30.705 | United States Wome | United States Wome | 103 | Ball Receipt*   |   -   | [28.4, 4.9]     |  |
|  +1.65 |  +1.23 | 00:02:30.705 | United States Wome | United States Wome | 103 | Carry           |   -   | [28.4, 4.9]     |  |
|  +1.71 |  +1.29 | 00:02:30.762 | United States Wome | United States Wome | 103 | Miscontrol      |   -   | [28.6, 5.8]     |  |
|  +3.58 |  +3.17 | 00:02:32.638 | Sweden Women's     | United States Wome | 103 | Pass            |   -   | [80.7, 64.5]    | Incomplete (Incomplete) |
|  +3.93 |  +3.51 | 00:02:32.984 | Sweden Women's     | United States Wome | 103 | Ball Receipt*   |   -   | [87.9, 75.5]    | Incomplete |
|  +3.93 |  +3.51 | 00:02:32.984 | United States Wome | United States Wome | 103 | Interception    |   -   | [35.8, 13.6]    | Lost In Play |
|  +4.60 |  +4.18 | 00:02:33.652 | Sweden Women's     | United States Wome | 103 | Ball Recovery   |   -   | [82.5, 62.2]    |  |
|  +4.60 |  +4.18 | 00:02:33.652 | Sweden Women's     | United States Wome | 103 | Carry           |   -   | [82.5, 62.2]    |  |
|  +5.22 |  +4.81 | 00:02:34.279 | Sweden Women's     | United States Wome | 103 | Pass            |   -   | [84.2, 60.6]    | -> Fridolina Rolf |
|  +6.35 |  +5.94 | 00:02:35.411 | Sweden Women's     | United States Wome | 103 | Ball Receipt*   |   -   | [86.6, 41.4]    |  |
|  +6.35 |  +5.94 | 00:02:35.411 | Sweden Women's     | United States Wome | 103 | Carry           |   -   | [86.6, 41.4]    |  |
|  +6.51 |  +6.09 | 00:02:35.564 | United States Wome | United States Wome | 103 | Pressure        |  Yes  | [34.5, 38.4]    |  |
|  +6.81 |  +6.39 | 00:02:35.862 | Sweden Women's     | United States Wome | 103 | Miscontrol      |   -   | [87.2, 41.2]    |  |
|  +8.17 |  +7.75 | 00:02:37.223 | United States Wome | United States Wome | 103 | Ball Recovery   |   -   | [33.1, 40.4]    |  |
|  +8.17 |  +7.75 | 00:02:37.223 | United States Wome | United States Wome | 103 | Carry           |   -   | [33.1, 40.4]    |  |
|  +8.73 |  +8.32 | 00:02:37.791 | Sweden Women's     | United States Wome | 103 | Pressure        |   -   | [80.5, 34.8]    |  |
|  +9.19 |  +8.77 | 00:02:38.242 | United States Wome | United States Wome | 103 | Dispossessed    |   -   | [38.7, 43.7]    |  |
|  +9.19 |  +8.77 | 00:02:38.242 | Sweden Women's     | United States Wome | 103 | Duel            |   -   | [81.4, 36.4]    | Tackle, Lost In Play |

---

### Disagreement Case 81: `3893819_p168_73831e4f`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893819 (Women's World Cup, 2023)
- **counterpressing_team**: Morocco Women's
- **opponent_team_at_turnover**: Korea Republic Women's
- **possession_team_at_counterpress_initiation**: Korea Republic Women's
- **possession_id_at_counterpress_initiation**: 168
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:24:06.151) | **Initiation**: Pressure (00:24:06.580)
- **Initiation Delay**: 0.429s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.859s) | Evidence: `interception_plus_control` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.27 |  -0.70 | 00:24:05.878 | Morocco Women's    | Morocco Women's    | 167 | Ball Recovery   |   -   | [50.9, 16.2]    |  |
|  -0.27 |  -0.70 | 00:24:05.878 | Morocco Women's    | Morocco Women's    | 167 | Carry           |   -   | [50.9, 16.2]    |  |
|  +0.00 |  -0.43 | 00:24:06.151 | Morocco Women's    | Morocco Women's    | 167 | Dispossessed    |   -   | [51.2, 17.5]    |  |
|  +0.00 |  -0.43 | 00:24:06.151 | Korea Republic Wom | Korea Republic Wom | 168 | Duel            |  Yes  | [68.9, 62.6]    | Tackle, Won |
|  +0.00 |  -0.43 | 00:24:06.151 | Korea Republic Wom | Korea Republic Wom | 168 | Carry           |   -   | [68.9, 62.6]    |  |
|  +0.43 |  +0.00 | 00:24:06.580 | Morocco Women's    | Korea Republic Wom | 168 | Pressure        |  Yes  | [51.2, 17.5]    |  |
|  +0.69 |  +0.26 | 00:24:06.843 | Morocco Women's    | Korea Republic Wom | 168 | Foul Committed  |  Yes  | [51.2, 17.5]    |  |
|  +0.69 |  +0.26 | 00:24:06.843 | Korea Republic Wom | Korea Republic Wom | 168 | Foul Won        |   -   | [68.9, 62.6]    |  |
|  +0.69 |  +0.26 | 00:24:06.843 | Korea Republic Wom | Korea Republic Wom | 168 | Carry           |   -   | [68.9, 62.6]    |  |
|  +0.80 |  +0.37 | 00:24:06.953 | Korea Republic Wom | Korea Republic Wom | 168 | Pass            |   -   | [68.5, 65.6]    | -> Yu-Ri Choe |
|  +1.65 |  +1.22 | 00:24:07.798 | Korea Republic Wom | Korea Republic Wom | 168 | Ball Receipt*   |   -   | [64.4, 68.2]    |  |
|  +1.65 |  +1.22 | 00:24:07.798 | Korea Republic Wom | Korea Republic Wom | 168 | Carry           |   -   | [64.4, 68.2]    |  |
|  +3.79 |  +3.36 | 00:24:09.944 | Morocco Women's    | Korea Republic Wom | 168 | Pressure        |  Yes  | [44.5, 18.6]    |  |
|  +4.10 |  +3.67 | 00:24:10.254 | Korea Republic Wom | Korea Republic Wom | 168 | Pass            |   -   | [75.6, 61.5]    | Incomplete (Incomplete) |
|  +4.29 |  +3.86 | 00:24:10.439 | Korea Republic Wom | Korea Republic Wom | 168 | Ball Receipt*   |   -   | [75.4, 53.6]    | Incomplete |
|  +4.29 |  +3.86 | 00:24:10.439 | Morocco Women's    | Korea Republic Wom | 168 | Interception    |  Yes  | [44.3, 19.8]    | Success In Play |
|  +5.15 |  +4.73 | 00:24:11.305 | Morocco Women's    | Korea Republic Wom | 168 | Pass            |   -   | [40.3, 28.4]    | Incomplete (Incomplete) |
|  +9.54 |  +9.12 | 00:24:15.696 | Morocco Women's    | Korea Republic Wom | 168 | Pressure        |   -   | [73.2, 3.6]     |  |
| +10.08 |  +9.65 | 00:24:16.229 | Korea Republic Wom | Korea Republic Wom | 168 | Ball Recovery   |   -   | [46.9, 76.5]    |  |

---

### Disagreement Case 82: `3893816_p193_461337bf`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893816 (Women's World Cup, 2023)
- **counterpressing_team**: Jamaica Women's
- **opponent_team_at_turnover**: Panama Women's
- **possession_team_at_counterpress_initiation**: Panama Women's
- **possession_id_at_counterpress_initiation**: 193
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:49:30.431) | **Initiation**: Dribbled Past (00:49:30.870)
- **Initiation Delay**: 0.439s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.062s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.17 |  -1.61 | 00:49:29.265 | Jamaica Women's    | Jamaica Women's    | 192 | Ball Recovery   |   -   | [55.6, 40.8]    |  |
|  -1.17 |  -1.61 | 00:49:29.265 | Jamaica Women's    | Jamaica Women's    | 192 | Carry           |   -   | [55.6, 40.8]    |  |
|  -0.47 |  -0.91 | 00:49:29.959 | Jamaica Women's    | Jamaica Women's    | 192 | Miscontrol      |   -   | [57.7, 41.2]    |  |
|  +0.00 |  -0.44 | 00:49:30.431 | Panama Women's     | Panama Women's     | 193 | Ball Recovery   |   -   | [58.1, 37.1]    |  |
|  +0.00 |  -0.44 | 00:49:30.431 | Panama Women's     | Panama Women's     | 193 | Carry           |   -   | [58.1, 37.1]    |  |
|  +0.44 |  +0.00 | 00:49:30.870 | Jamaica Women's    | Panama Women's     | 193 | Dribbled Past   |  Yes  | [62.0, 43.0]    |  |
|  +0.44 |  +0.00 | 00:49:30.870 | Panama Women's     | Panama Women's     | 193 | Dribble         |   -   | [58.1, 37.1]    |  |
|  +0.44 |  +0.00 | 00:49:30.870 | Panama Women's     | Panama Women's     | 193 | Carry           |   -   | [58.1, 37.1]    |  |
|  +0.87 |  +0.43 | 00:49:31.303 | Jamaica Women's    | Panama Women's     | 193 | Pressure        |  Yes  | [62.0, 43.0]    |  |
|  +1.50 |  +1.06 | 00:49:31.932 | Panama Women's     | Panama Women's     | 193 | Dribble         |   -   | [62.2, 37.3]    |  |
|  +1.50 |  +1.06 | 00:49:31.932 | Jamaica Women's    | Panama Women's     | 193 | Duel            |  Yes  | [57.9, 42.8]    | Tackle, Success In Play |
|  +2.45 |  +2.01 | 00:49:32.884 | Jamaica Women's    | Panama Women's     | 193 | Pass            |   -   | [53.1, 41.6]    | Incomplete (Incomplete) |
|  +2.97 |  +2.53 | 00:49:33.404 | Jamaica Women's    | Panama Women's     | 193 | Ball Receipt*   |   -   | [64.9, 42.0]    | Incomplete |
|  +2.97 |  +2.53 | 00:49:33.404 | Panama Women's     | Panama Women's     | 193 | Block           |  Yes  | [58.3, 35.0]    |  |
|  +3.66 |  +3.22 | 00:49:34.089 | Panama Women's     | Panama Women's     | 193 | Pass            |   -   | [60.2, 37.5]    | -> Carmen Milagro |
|  +4.13 |  +3.69 | 00:49:34.561 | Panama Women's     | Panama Women's     | 193 | Ball Receipt*   |   -   | [57.9, 36.2]    |  |
|  +4.13 |  +3.69 | 00:49:34.561 | Panama Women's     | Panama Women's     | 193 | Carry           |   -   | [57.9, 36.2]    |  |
|  +4.93 |  +4.49 | 00:49:35.359 | Panama Women's     | Panama Women's     | 193 | Pass            |   -   | [62.0, 35.8]    | -> Marta Alexandr |
|  +6.07 |  +5.63 | 00:49:36.501 | Panama Women's     | Panama Women's     | 193 | Ball Receipt*   |   -   | [67.0, 28.8]    |  |
|  +6.07 |  +5.63 | 00:49:36.501 | Panama Women's     | Panama Women's     | 193 | Carry           |   -   | [67.0, 28.8]    |  |
|  +8.80 |  +8.36 | 00:49:39.226 | Panama Women's     | Panama Women's     | 193 | Pass            |   -   | [83.1, 29.6]    | Incomplete (Incomplete) |
| +11.29 | +10.85 | 00:49:41.721 | Panama Women's     | Panama Women's     | 193 | Ball Receipt*   |   -   | [108.8, 22.6]   | Incomplete |
| +11.29 | +10.85 | 00:49:41.721 | Jamaica Women's    | Panama Women's     | 193 | Interception    |   -   | [11.5, 57.5]    | Lost Out |

---

### Disagreement Case 83: `3773597_p68_da7911db`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3773597 (La Liga, 2020/2021)
- **counterpressing_team**: Barcelona
- **opponent_team_at_turnover**: Real Sociedad
- **possession_team_at_counterpress_initiation**: Real Sociedad
- **possession_id_at_counterpress_initiation**: 68
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:38:00.532) | **Initiation**: Pressure (00:38:00.978)
- **Initiation Delay**: 0.446s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.025s) | Evidence: `goalkeeper_control` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.74 |  -1.18 | 00:37:59.794 | Barcelona          | Barcelona          | 67 | Ball Receipt*   |   -   | [22.9, 47.6]    | Incomplete |
|  -0.74 |  -1.18 | 00:37:59.794 | Real Sociedad      | Real Sociedad      | 68 | Pass            |  Yes  | [93.5, 29.1]    | -> Alexander Isak |
|  -0.16 |  -0.60 | 00:38:00.374 | Barcelona          | Real Sociedad      | 68 | Error           |   -   | [25.4, 50.7]    |  |
|  +0.00 |  -0.45 | 00:38:00.532 | Real Sociedad      | Real Sociedad      | 68 | Ball Receipt*   |   -   | [103.9, 27.5]   |  |
|  +0.00 |  -0.45 | 00:38:00.532 | Real Sociedad      | Real Sociedad      | 68 | Carry           |   -   | [103.9, 27.5]   |  |
|  +0.45 |  +0.00 | 00:38:00.978 | Barcelona          | Real Sociedad      | 68 | Pressure        |  Yes  | [11.7, 56.3]    |  |
|  +0.92 |  +0.47 | 00:38:01.449 | Real Sociedad      | Real Sociedad      | 68 | Shot            |   -   | [104.1, 30.3]   | Saved |
|  +1.47 |  +1.03 | 00:38:02.003 | Barcelona          | Real Sociedad      | 68 | Goal Keeper     |   -   | [3.7, 42.0]     |  |
|  +3.74 |  +3.29 | 00:38:04.271 | Real Sociedad      | Real Sociedad      | 68 | Pass            |   -   | [117.7, 25.8]   | Incomplete (Incomplete) |
|  +4.52 |  +4.07 | 00:38:05.052 | Real Sociedad      | Real Sociedad      | 68 | Ball Receipt*   |   -   | [111.5, 40.4]   | Incomplete |
|  +4.52 |  +4.07 | 00:38:05.052 | Barcelona          | Real Sociedad      | 68 | Interception    |   -   | [9.5, 45.3]     | Won |
|  +4.52 |  +4.07 | 00:38:05.052 | Barcelona          | Real Sociedad      | 68 | Carry           |   -   | [9.5, 45.3]     |  |
|  +5.34 |  +4.90 | 00:38:05.874 | Barcelona          | Real Sociedad      | 68 | Pass            |   -   | [9.5, 43.9]     | Incomplete (Out) |
| +14.98 | +14.53 | 00:38:15.511 | Real Sociedad      | Real Sociedad      | 69 | Pass            |   -   | [79.8, 0.1]     | -> Robin Aime Rob |
| +17.11 | +16.67 | 00:38:17.646 | Real Sociedad      | Real Sociedad      | 69 | Ball Receipt*   |   -   | [56.5, 5.9]     |  |
| +17.11 | +16.67 | 00:38:17.646 | Real Sociedad      | Real Sociedad      | 69 | Carry           |   -   | [56.5, 5.9]     |  |
| +19.47 | +19.02 | 00:38:19.998 | Real Sociedad      | Real Sociedad      | 69 | Pass            |   -   | [57.4, 6.1]     | -> Martín Zubimen |

---

### Disagreement Case 84: `3837771_p140_46470595`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3837771 (Ligue 1, 2022/2023)
- **counterpressing_team**: Troyes
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 140
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:32:34.607) | **Initiation**: Pressure (00:32:35.064)
- **Initiation Delay**: 0.457s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.87s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.18 |  -2.64 | 00:32:32.423 | Troyes             | Troyes             | 139 | Carry           |   -   | [100.0, 18.3]   |  |
|  -1.18 |  -1.63 | 00:32:33.431 | Troyes             | Troyes             | 139 | Pass            |   -   | [104.8, 19.2]   | Incomplete (Incomplete) |
|  +0.00 |  -0.46 | 00:32:34.607 | Troyes             | Troyes             | 139 | Ball Receipt*   |   -   | [97.5, 28.8]    | Incomplete |
|  +0.00 |  -0.46 | 00:32:34.607 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [15.0, 48.2]    |  |
|  +0.00 |  -0.46 | 00:32:34.607 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [15.0, 48.2]    |  |
|  +0.46 |  +0.00 | 00:32:35.064 | Troyes             | Paris Saint-Germai | 140 | Pressure        |  Yes  | [105.3, 31.9]   |  |
|  +0.94 |  +0.49 | 00:32:35.550 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [12.2, 48.8]    | -> Marco Verratti |
|  +1.38 |  +0.93 | 00:32:35.992 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [14.4, 55.6]    |  |
|  +1.38 |  +0.93 | 00:32:35.992 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [14.4, 55.6]    |  |
|  +1.45 |  +1.00 | 00:32:36.062 | Troyes             | Paris Saint-Germai | 140 | Pressure        |  Yes  | [105.7, 24.5]   |  |
|  +1.73 |  +1.27 | 00:32:36.339 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [14.4, 55.6]    | -> Sergio Ramos G |
|  +2.57 |  +2.11 | 00:32:37.176 | Troyes             | Paris Saint-Germai | 140 | Pressure        |  Yes  | [113.7, 24.5]   |  |
|  +2.60 |  +2.14 | 00:32:37.202 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [6.4, 55.6]     |  |
|  +2.60 |  +2.14 | 00:32:37.202 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [6.4, 55.6]     |  |
|  +3.06 |  +2.61 | 00:32:37.671 | Paris Saint-Germai | Paris Saint-Germai | 140 | Pass            |   -   | [6.4, 55.6]     | Incomplete (Incomplete) |
|  +3.30 |  +2.84 | 00:32:37.904 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Receipt*   |   -   | [13.4, 69.8]    | Incomplete |
|  +3.30 |  +2.84 | 00:32:37.904 | Troyes             | Paris Saint-Germai | 140 | Block           |  Yes  | [112.9, 20.5]   |  |
|  +4.33 |  +3.87 | 00:32:38.934 | Troyes             | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [110.7, 30.6]   |  |
|  +4.33 |  +3.87 | 00:32:38.934 | Troyes             | Paris Saint-Germai | 140 | Carry           |   -   | [110.7, 30.6]   |  |
|  +5.14 |  +4.68 | 00:32:39.746 | Troyes             | Paris Saint-Germai | 140 | Shot            |   -   | [116.0, 29.0]   | Blocked |
|  +5.24 |  +4.79 | 00:32:39.851 | Paris Saint-Germai | Paris Saint-Germai | 140 | Block           |  Yes  | [3.7, 50.1]     |  |
|  +6.09 |  +5.63 | 00:32:40.699 | Paris Saint-Germai | Paris Saint-Germai | 140 | Goal Keeper     |   -   | [1.5, 43.9]     |  |
|  +7.55 |  +7.09 | 00:32:42.157 | Troyes             | Paris Saint-Germai | 140 | Pressure        |   -   | [114.7, 5.8]    |  |
|  +7.57 |  +7.12 | 00:32:42.180 | Paris Saint-Germai | Paris Saint-Germai | 140 | Ball Recovery   |   -   | [5.4, 74.3]     |  |
|  +7.57 |  +7.12 | 00:32:42.180 | Paris Saint-Germai | Paris Saint-Germai | 140 | Carry           |   -   | [5.4, 74.3]     |  |
| +11.42 | +10.97 | 00:32:46.032 | Troyes             | Paris Saint-Germai | 140 | Pressure        |   -   | [100.3, 8.8]    |  |
| +12.89 | +12.43 | 00:32:47.498 | Troyes             | Paris Saint-Germai | 140 | Foul Committed  |   -   | [88.4, 10.8]    |  |

---

### Disagreement Case 85: `3773586_p137_0efacb4f`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3773586 (La Liga, 2020/2021)
- **counterpressing_team**: Barcelona
- **opponent_team_at_turnover**: Granada
- **possession_team_at_counterpress_initiation**: Granada
- **possession_id_at_counterpress_initiation**: 137
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:39:25.961) | **Initiation**: Pressure (00:39:26.423)
- **Initiation Delay**: 0.462s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.783s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.06 |  -3.52 | 00:39:22.899 | Barcelona          | Barcelona          | 136 | Ball Receipt*   |   -   | [110.4, 36.2]   | Incomplete |
|  -3.06 |  -3.52 | 00:39:22.899 | Granada            | Barcelona          | 136 | Clearance       |   -   | [9.7, 50.1]     |  |
|  -1.93 |  -2.39 | 00:39:24.034 | Granada            | Barcelona          | 136 | Clearance       |   -   | [7.5, 38.2]     |  |
|  -0.22 |  -0.68 | 00:39:25.740 | Barcelona          | Barcelona          | 136 | Pressure        |   -   | [103.3, 39.3]   |  |
|  +0.00 |  -0.46 | 00:39:25.961 | Granada            | Granada            | 137 | Pass            |   -   | [16.3, 43.7]    | -> Jorge Molina V |
|  +0.46 |  +0.00 | 00:39:26.423 | Barcelona          | Granada            | 137 | Pressure        |  Yes  | [89.2, 41.4]    |  |
|  +0.81 |  +0.34 | 00:39:26.766 | Granada            | Granada            | 137 | Ball Receipt*   |   -   | [27.4, 37.0]    |  |
|  +0.81 |  +0.34 | 00:39:26.766 | Granada            | Granada            | 137 | Carry           |   -   | [27.4, 37.0]    |  |
|  +1.15 |  +0.69 | 00:39:27.111 | Barcelona          | Granada            | 137 | Dribbled Past   |  Yes  | [91.1, 43.0]    |  |
|  +1.15 |  +0.69 | 00:39:27.111 | Granada            | Granada            | 137 | Dribble         |   -   | [29.0, 37.1]    |  |
|  +1.15 |  +0.69 | 00:39:27.111 | Granada            | Granada            | 137 | Carry           |   -   | [29.0, 37.1]    |  |
|  +2.52 |  +2.06 | 00:39:28.480 | Barcelona          | Granada            | 137 | Pressure        |  Yes  | [84.4, 35.7]    |  |
|  +5.25 |  +4.78 | 00:39:31.206 | Granada            | Granada            | 137 | Dribble         |   -   | [53.9, 41.1]    |  |
|  +5.25 |  +4.78 | 00:39:31.206 | Barcelona          | Granada            | 137 | Duel            |   -   | [66.2, 39.0]    | Tackle, Won |
|  +5.25 |  +4.78 | 00:39:31.206 | Barcelona          | Granada            | 137 | Carry           |   -   | [66.2, 39.0]    |  |
|  +5.92 |  +5.46 | 00:39:31.882 | Granada            | Granada            | 137 | Pressure        |  Yes  | [54.9, 42.7]    |  |
|  +5.96 |  +5.50 | 00:39:31.922 | Barcelona          | Granada            | 137 | Pass            |   -   | [61.7, 34.8]    | Incomplete (Incomplete) |
|  +9.75 |  +9.28 | 00:39:35.706 | Barcelona          | Granada            | 137 | Ball Receipt*   |   -   | [51.8, 27.9]    | Incomplete |
|  +9.75 |  +9.28 | 00:39:35.706 | Granada            | Granada            | 137 | Ball Recovery   |   -   | [67.8, 72.8]    |  |

---

### Disagreement Case 86: `3869486_p5_b7840c1e`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3869486 (FIFA World Cup, 2022)
- **counterpressing_team**: Morocco
- **opponent_team_at_turnover**: Portugal
- **possession_team_at_counterpress_initiation**: Portugal
- **possession_id_at_counterpress_initiation**: 5
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:01:48.261) | **Initiation**: Block (00:01:48.749)
- **Initiation Delay**: 0.488s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.987s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.54 |  -3.03 | 00:01:45.717 | Morocco            | Morocco            | 4 | Pass            |   -   | [33.0, 74.6]    | Incomplete (Incomplete) |
|  +0.00 |  -0.49 | 00:01:48.261 | Morocco            | Morocco            | 4 | Ball Receipt*   |   -   | [59.7, 47.7]    | Incomplete |
|  +0.00 |  -0.49 | 00:01:48.261 | Portugal           | Portugal           | 5 | Pass            |   -   | [62.2, 27.4]    | -> Bruno Miguel B |
|  +0.49 |  +0.00 | 00:01:48.749 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [80.9, 28.9]    |  |
|  +0.49 |  +0.00 | 00:01:48.749 | Portugal           | Portugal           | 5 | Carry           |   -   | [80.9, 28.9]    |  |
|  +0.49 |  +0.00 | 00:01:48.749 | Morocco            | Portugal           | 5 | Block           |  Yes  | [46.5, 53.0]    |  |
|  +1.35 |  +0.86 | 00:01:49.611 | Portugal           | Portugal           | 5 | Pass            |   -   | [81.3, 27.2]    | -> Bernardo Mota  |
|  +1.90 |  +1.42 | 00:01:50.165 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [77.8, 23.9]    |  |
|  +1.90 |  +1.42 | 00:01:50.165 | Portugal           | Portugal           | 5 | Carry           |   -   | [77.8, 23.9]    |  |
|  +2.10 |  +1.61 | 00:01:50.362 | Portugal           | Portugal           | 5 | Pass            |   -   | [77.8, 23.9]    | -> Bruno Miguel B |
|  +2.65 |  +2.16 | 00:01:50.910 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [81.1, 27.2]    |  |
|  +2.65 |  +2.16 | 00:01:50.910 | Portugal           | Portugal           | 5 | Carry           |   -   | [81.1, 27.2]    |  |
|  +2.77 |  +2.28 | 00:01:51.030 | Portugal           | Portugal           | 5 | Miscontrol      |   -   | [81.3, 25.7]    |  |
|  +3.26 |  +2.78 | 00:01:51.525 | Portugal           | Portugal           | 5 | Pressure        |   -   | [80.6, 36.2]    |  |
|  +3.47 |  +2.99 | 00:01:51.736 | Morocco            | Portugal           | 5 | Ball Recovery   |   -   | [40.1, 46.3]    |  |
|  +3.47 |  +2.99 | 00:01:51.736 | Morocco            | Portugal           | 5 | Carry           |   -   | [40.1, 46.3]    |  |
|  +3.74 |  +3.25 | 00:01:51.997 | Morocco            | Portugal           | 5 | Dribble         |   -   | [43.0, 45.2]    |  |
|  +3.74 |  +3.25 | 00:01:51.997 | Portugal           | Portugal           | 5 | Duel            |  Yes  | [77.1, 34.9]    | Tackle, Won |
|  +3.74 |  +3.25 | 00:01:51.997 | Portugal           | Portugal           | 5 | Carry           |   -   | [77.1, 34.9]    |  |
|  +4.62 |  +4.13 | 00:01:52.876 | Morocco            | Portugal           | 5 | Pressure        |  Yes  | [42.7, 44.5]    |  |
|  +4.77 |  +4.28 | 00:01:53.026 | Portugal           | Portugal           | 5 | Pass            |   -   | [75.8, 36.5]    | -> Kléper Laveran |
|  +6.59 |  +6.10 | 00:01:54.849 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [56.3, 44.9]    |  |
|  +6.59 |  +6.10 | 00:01:54.849 | Portugal           | Portugal           | 5 | Carry           |   -   | [56.3, 44.9]    |  |
|  +6.63 |  +6.14 | 00:01:54.889 | Portugal           | Portugal           | 5 | Pass            |   -   | [54.9, 44.7]    | -> José Diogo Dal |
|  +7.79 |  +7.30 | 00:01:56.053 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [56.5, 58.9]    |  |
|  +7.79 |  +7.30 | 00:01:56.053 | Portugal           | Portugal           | 5 | Carry           |   -   | [56.5, 58.9]    |  |
|  +9.26 |  +8.78 | 00:01:57.524 | Portugal           | Portugal           | 5 | Pass            |   -   | [56.5, 58.9]    | -> Rúben Santos G |
| +10.79 | +10.31 | 00:01:59.055 | Portugal           | Portugal           | 5 | Ball Receipt*   |   -   | [47.2, 28.1]    |  |

---

### Disagreement Case 87: `3895182_p83_6308e2cb`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895182 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: Bochum
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 83
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:44:25.616) | **Initiation**: Pressure (00:44:26.121)
- **Initiation Delay**: 0.505s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.053s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| -38.68 | -39.18 | 00:43:46.941 | Bayer Leverkusen   | Bayer Leverkusen   | 81 | Pass            |   -   | [86.1, 33.1]    | Incomplete (Out) |
| -35.98 | -36.48 | 00:43:49.639 | Bayer Leverkusen   | Bayer Leverkusen   | 81 | Ball Receipt*   |   -   | [111.1, 57.8]   | Incomplete |
|  -3.01 |  -3.51 | 00:44:22.610 | Bochum             | Bochum             | 82 | Pass            |   -   | [6.5, 35.2]     | Incomplete (Incomplete) |
|  +0.00 |  -0.51 | 00:44:25.616 | Bochum             | Bochum             | 82 | Ball Receipt*   |   -   | [71.3, 24.7]    | Incomplete |
|  +0.00 |  -0.51 | 00:44:25.616 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Pass            |   -   | [49.2, 54.4]    | -> Florian Wirtz |
|  +0.51 |  +0.00 | 00:44:26.121 | Bochum             | Bayer Leverkusen   | 83 | Pressure        |  Yes  | [65.5, 27.4]    |  |
|  +0.78 |  +0.27 | 00:44:26.393 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Ball Receipt*   |   -   | [53.4, 51.8]    |  |
|  +0.78 |  +0.27 | 00:44:26.393 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Carry           |   -   | [53.4, 51.8]    |  |
|  +1.37 |  +0.86 | 00:44:26.982 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Pass            |   -   | [52.1, 52.7]    | -> Granit Xhaka |
|  +1.83 |  +1.33 | 00:44:27.450 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Ball Receipt*   |   -   | [49.7, 48.8]    |  |
|  +1.83 |  +1.33 | 00:44:27.450 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Carry           |   -   | [49.7, 48.8]    |  |
|  +2.12 |  +1.61 | 00:44:27.736 | Bochum             | Bayer Leverkusen   | 83 | Pressure        |  Yes  | [68.0, 32.7]    |  |
|  +2.56 |  +2.05 | 00:44:28.174 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Dispossessed    |   -   | [49.7, 47.7]    |  |
|  +2.56 |  +2.05 | 00:44:28.174 | Bochum             | Bayer Leverkusen   | 83 | Duel            |  Yes  | [70.4, 32.4]    | Tackle, Lost In Play |
|  +2.98 |  +2.48 | 00:44:28.597 | Bochum             | Bayer Leverkusen   | 83 | Pressure        |  Yes  | [70.9, 30.7]    |  |
|  +3.38 |  +2.87 | 00:44:28.995 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | 50/50           |   -   | [49.1, 49.4]    |  |
|  +3.38 |  +2.87 | 00:44:28.995 | Bochum             | Bayer Leverkusen   | 83 | 50/50           |  Yes  | [71.0, 30.7]    |  |
|  +4.51 |  +4.00 | 00:44:30.123 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Pressure        |   -   | [43.2, 39.9]    |  |
|  +4.58 |  +4.07 | 00:44:30.193 | Bochum             | Bayer Leverkusen   | 83 | Pass            |   -   | [74.4, 40.0]    | Incomplete (Incomplete) |
|  +5.74 |  +5.24 | 00:44:31.357 | Bochum             | Bayer Leverkusen   | 83 | Ball Receipt*   |   -   | [75.6, 35.7]    | Incomplete |
|  +5.74 |  +5.24 | 00:44:31.357 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Pass            |   -   | [47.7, 44.9]    | -> Alejandro Grim |
|  +6.91 |  +6.40 | 00:44:32.524 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Ball Receipt*   |   -   | [44.7, 23.4]    |  |
|  +6.91 |  +6.40 | 00:44:32.524 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Carry           |   -   | [44.7, 23.4]    |  |
|  +8.69 |  +8.18 | 00:44:34.306 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Pass            |   -   | [44.1, 24.7]    | -> Florian Wirtz |
|  +9.19 |  +8.68 | 00:44:34.803 | Bochum             | Bayer Leverkusen   | 83 | Pressure        |   -   | [63.1, 51.3]    |  |
|  +9.49 |  +8.99 | 00:44:35.109 | Bayer Leverkusen   | Bayer Leverkusen   | 83 | Ball Receipt*   |   -   | [56.4, 27.3]    |  |

---

### Disagreement Case 88: `3773369_p168_0bb17adb`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3773369 (La Liga, 2020/2021)
- **counterpressing_team**: Huesca
- **opponent_team_at_turnover**: Barcelona
- **possession_team_at_counterpress_initiation**: Barcelona
- **possession_id_at_counterpress_initiation**: 168
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:30:47.207) | **Initiation**: Pressure (00:30:47.722)
- **Initiation Delay**: 0.515s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.132s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.37 |  -1.88 | 00:30:45.837 | Barcelona          | Barcelona          | 167 | Pass            |   -   | [92.0, 32.1]    | -> Pedro González |
|  -0.48 |  -0.99 | 00:30:46.729 | Barcelona          | Barcelona          | 167 | Ball Receipt*   |   -   | [94.7, 44.7]    |  |
|  -0.48 |  -0.99 | 00:30:46.729 | Barcelona          | Barcelona          | 167 | Carry           |   -   | [94.7, 44.7]    |  |
|  -0.30 |  -0.82 | 00:30:46.907 | Huesca             | Barcelona          | 167 | Pressure        |  Yes  | [19.7, 39.7]    |  |
|  +0.00 |  -0.51 | 00:30:47.207 | Barcelona          | Barcelona          | 168 | Pass            |   -   | [95.7, 42.2]    | -> Francisco Antó |
|  +0.51 |  +0.00 | 00:30:47.722 | Huesca             | Barcelona          | 168 | Pressure        |  Yes  | [13.9, 36.7]    |  |
|  +0.63 |  +0.12 | 00:30:47.839 | Barcelona          | Barcelona          | 168 | Ball Receipt*   |   -   | [104.3, 45.9]   |  |
|  +0.63 |  +0.12 | 00:30:47.839 | Barcelona          | Barcelona          | 168 | Carry           |   -   | [104.3, 45.9]   |  |
|  +1.36 |  +0.85 | 00:30:48.568 | Barcelona          | Barcelona          | 168 | Miscontrol      |   -   | [104.8, 45.5]   |  |
|  +1.65 |  +1.13 | 00:30:48.854 | Huesca             | Barcelona          | 168 | Ball Recovery   |   -   | [12.3, 36.3]    |  |
|  +1.65 |  +1.13 | 00:30:48.854 | Huesca             | Barcelona          | 168 | Carry           |   -   | [12.3, 36.3]    |  |
|  +1.77 |  +1.26 | 00:30:48.982 | Barcelona          | Barcelona          | 168 | Pressure        |  Yes  | [107.4, 47.6]   |  |
|  +4.94 |  +4.43 | 00:30:52.148 | Huesca             | Barcelona          | 168 | Pass            |   -   | [11.8, 11.5]    | Incomplete (Incomplete) |
|  +8.36 |  +7.85 | 00:30:55.570 | Huesca             | Barcelona          | 168 | Pressure        |   -   | [47.7, 13.4]    |  |
|  +8.40 |  +7.88 | 00:30:55.603 | Huesca             | Barcelona          | 168 | Ball Receipt*   |   -   | [47.9, 13.6]    | Incomplete |
|  +8.40 |  +7.88 | 00:30:55.603 | Barcelona          | Barcelona          | 168 | Ball Recovery   |   -   | [69.1, 65.7]    |  |
|  +8.40 |  +7.88 | 00:30:55.603 | Barcelona          | Barcelona          | 168 | Carry           |   -   | [69.1, 65.7]    |  |
|  +9.86 |  +9.35 | 00:30:57.070 | Barcelona          | Barcelona          | 168 | Pass            |   -   | [63.4, 66.1]    | -> Moriba Kouroum |
| +11.47 | +10.96 | 00:30:58.680 | Barcelona          | Barcelona          | 168 | Ball Receipt*   |   -   | [64.2, 49.2]    |  |

---

### Disagreement Case 89: `3998838_p3_fb14381f`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3998838 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Italy Women's
- **opponent_team_at_turnover**: Belgium Women's
- **possession_team_at_counterpress_initiation**: Belgium Women's
- **possession_id_at_counterpress_initiation**: 3
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:00:09.988) | **Initiation**: Pressure (00:00:10.528)
- **Initiation Delay**: 0.54s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 14.494s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.781s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.08 |  -0.62 | 00:00:09.904 | Italy Women's      | Italy Women's      | 2 | Ball Receipt*   |   -   | [75.9, 77.8]    |  |
|  -0.08 |  -0.62 | 00:00:09.904 | Italy Women's      | Italy Women's      | 2 | Carry           |   -   | [75.9, 77.8]    |  |
|  +0.00 |  -0.54 | 00:00:09.988 | Italy Women's      | Italy Women's      | 2 | Dribble         |   -   | [79.5, 77.7]    |  |
|  +0.00 |  -0.54 | 00:00:09.988 | Belgium Women's    | Belgium Women's    | 3 | Duel            |  Yes  | [40.6, 2.4]     | Tackle, Won |
|  +0.00 |  -0.54 | 00:00:09.988 | Belgium Women's    | Belgium Women's    | 3 | Carry           |   -   | [40.6, 2.4]     |  |
|  +0.54 |  +0.00 | 00:00:10.528 | Italy Women's      | Belgium Women's    | 3 | Pressure        |  Yes  | [77.3, 77.6]    |  |
|  +3.32 |  +2.78 | 00:00:13.309 | Belgium Women's    | Belgium Women's    | 3 | Dispossessed    |   -   | [39.5, 12.4]    |  |
|  +3.32 |  +2.78 | 00:00:13.309 | Italy Women's      | Belgium Women's    | 3 | Duel            |  Yes  | [80.6, 67.7]    | Tackle, Success In Play |
|  +5.12 |  +4.58 | 00:00:15.106 | Belgium Women's    | Belgium Women's    | 3 | Pressure        |   -   | [41.5, 19.3]    |  |
|  +5.26 |  +4.72 | 00:00:15.247 | Italy Women's      | Belgium Women's    | 3 | Pass            |   -   | [79.4, 64.1]    | Incomplete (Incomplete) |
|  +5.82 |  +5.28 | 00:00:15.805 | Belgium Women's    | Belgium Women's    | 3 | Ball Recovery   |   -   | [38.7, 10.5]    |  |
|  +5.82 |  +5.28 | 00:00:15.805 | Belgium Women's    | Belgium Women's    | 3 | Carry           |   -   | [38.7, 10.5]    |  |
|  +6.78 |  +6.24 | 00:00:16.767 | Italy Women's      | Belgium Women's    | 3 | Pressure        |   -   | [80.1, 66.1]    |  |
|  +7.30 |  +6.76 | 00:00:17.291 | Belgium Women's    | Belgium Women's    | 3 | Pass            |   -   | [39.3, 13.1]    | Incomplete (Incomplete) |
|  +7.32 |  +6.78 | 00:00:17.307 | Italy Women's      | Belgium Women's    | 3 | Block           |   -   | [79.5, 65.7]    |  |
|  +7.43 |  +6.89 | 00:00:17.415 | Belgium Women's    | Belgium Women's    | 3 | Block           |   -   | [41.3, 13.8]    |  |
|  +8.35 |  +7.81 | 00:00:18.341 | Italy Women's      | Belgium Women's    | 3 | Pressure        |   -   | [76.6, 66.9]    |  |
|  +8.94 |  +8.40 | 00:00:18.925 | Belgium Women's    | Belgium Women's    | 3 | Pass            |   -   | [45.3, 10.8]    | -> Mariam Abdulai |
| +10.63 | +10.09 | 00:00:20.621 | Belgium Women's    | Belgium Women's    | 3 | Ball Receipt*   |   -   | [57.5, 3.8]     |  |
| +10.63 | +10.09 | 00:00:20.621 | Belgium Women's    | Belgium Women's    | 3 | Carry           |   -   | [57.5, 3.8]     |  |

---

### Disagreement Case 90: `3788749_p105_9602ad51`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3788749 (UEFA Euro, 2020)
- **counterpressing_team**: Poland
- **opponent_team_at_turnover**: Slovakia
- **possession_team_at_counterpress_initiation**: Slovakia
- **possession_id_at_counterpress_initiation**: 105
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:14:53.919) | **Initiation**: Pressure (00:14:54.475)
- **Initiation Delay**: 0.556s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.491s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -7.03 |  -7.58 | 00:14:46.892 | Slovakia           | Poland             | 104 | Pressure        |   -   | [78.3, 5.0]     |  |
|  -1.05 |  -1.61 | 00:14:52.867 | Poland             | Poland             | 104 | Pass            |   -   | [38.1, 77.0]    | Incomplete (Incomplete) |
|  +0.00 |  -0.56 | 00:14:53.919 | Poland             | Poland             | 104 | Ball Receipt*   |   -   | [49.2, 78.2]    | Incomplete |
|  +0.00 |  -0.56 | 00:14:53.919 | Slovakia           | Slovakia           | 105 | Interception    |   -   | [73.0, 3.1]     | Won |
|  +0.00 |  -0.56 | 00:14:53.919 | Slovakia           | Slovakia           | 105 | Carry           |   -   | [73.0, 3.1]     |  |
|  +0.56 |  +0.00 | 00:14:54.475 | Poland             | Slovakia           | 105 | Pressure        |  Yes  | [48.7, 75.9]    |  |
|  +2.19 |  +1.64 | 00:14:56.113 | Slovakia           | Slovakia           | 105 | Pass            |   -   | [72.6, 2.3]     | -> Juraj Kucka |
|  +2.52 |  +1.97 | 00:14:56.444 | Slovakia           | Slovakia           | 105 | Ball Receipt*   |   -   | [77.1, 3.1]     |  |
|  +2.52 |  +1.97 | 00:14:56.444 | Slovakia           | Slovakia           | 105 | Carry           |   -   | [77.1, 3.1]     |  |
|  +2.95 |  +2.39 | 00:14:56.867 | Slovakia           | Slovakia           | 105 | Pass            |   -   | [77.1, 3.0]     | -> Róbert Mak |
|  +3.60 |  +3.04 | 00:14:57.516 | Slovakia           | Slovakia           | 105 | Ball Receipt*   |   -   | [84.0, 2.6]     |  |
|  +3.60 |  +3.04 | 00:14:57.516 | Slovakia           | Slovakia           | 105 | Carry           |   -   | [84.0, 2.6]     |  |
|  +3.71 |  +3.15 | 00:14:57.627 | Poland             | Slovakia           | 105 | Pressure        |  Yes  | [39.4, 75.4]    |  |
|  +5.05 |  +4.49 | 00:14:58.966 | Slovakia           | Slovakia           | 105 | Dispossessed    |   -   | [78.7, 1.2]     |  |
|  +5.05 |  +4.49 | 00:14:58.966 | Poland             | Slovakia           | 105 | Duel            |   -   | [41.4, 78.9]    | Tackle, Success Out |
| +24.42 | +23.87 | 00:15:18.342 | Poland             | Poland             | 106 | Pass            |   -   | [40.4, 80.0]    | -> Grzegorz Krych |
| +25.15 | +24.59 | 00:15:19.068 | Poland             | Poland             | 106 | Ball Receipt*   |   -   | [40.7, 72.6]    |  |

---

### Disagreement Case 91: `3895194_p130_cb47b2d5`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895194 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: Augsburg
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 130
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:32:30.636) | **Initiation**: Pressure (00:32:31.231)
- **Initiation Delay**: 0.595s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.55s) | Evidence: `interception_plus_control` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.83 |  -1.42 | 00:32:29.809 | Augsburg           | Augsburg           | 129 | Ball Receipt*   |   -   | [89.6, 15.7]    |  |
|  -0.83 |  -1.42 | 00:32:29.809 | Augsburg           | Augsburg           | 129 | Carry           |   -   | [89.6, 15.7]    |  |
|  -0.74 |  -1.33 | 00:32:29.898 | Augsburg           | Augsburg           | 129 | Pass            |   -   | [90.6, 16.2]    | Incomplete (Incomplete) |
|  +0.00 |  -0.60 | 00:32:30.636 | Augsburg           | Augsburg           | 129 | Ball Receipt*   |   -   | [93.4, 11.6]    | Incomplete |
|  +0.00 |  -0.60 | 00:32:30.636 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pass            |  Yes  | [28.3, 66.8]    | -> Josip Stanišić |
|  +0.60 |  +0.00 | 00:32:31.231 | Augsburg           | Bayer Leverkusen   | 130 | Pressure        |  Yes  | [89.2, 9.7]     |  |
|  +0.71 |  +0.11 | 00:32:31.344 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Ball Receipt*   |   -   | [29.5, 70.5]    |  |
|  +0.71 |  +0.11 | 00:32:31.344 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Carry           |   -   | [29.5, 70.5]    |  |
|  +1.03 |  +0.43 | 00:32:31.661 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pass            |   -   | [30.1, 71.8]    | -> Jeremie Frimpo |
|  +1.93 |  +1.34 | 00:32:32.566 | Augsburg           | Bayer Leverkusen   | 130 | Pressure        |  Yes  | [82.4, 3.4]     |  |
|  +2.16 |  +1.56 | 00:32:32.794 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Ball Receipt*   |   -   | [36.3, 77.8]    |  |
|  +2.16 |  +1.56 | 00:32:32.794 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Carry           |   -   | [36.3, 77.8]    |  |
|  +3.06 |  +2.46 | 00:32:33.695 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pass            |   -   | [40.7, 77.3]    | Incomplete (Incomplete) |
|  +4.14 |  +3.55 | 00:32:34.781 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Ball Receipt*   |   -   | [67.0, 60.3]    | Incomplete |
|  +4.14 |  +3.55 | 00:32:34.781 | Augsburg           | Bayer Leverkusen   | 130 | Interception    |  Yes  | [58.1, 14.9]    | Success In Play |
|  +5.08 |  +4.48 | 00:32:35.716 | Augsburg           | Bayer Leverkusen   | 130 | Ball Recovery   |   -   | [58.5, 17.6]    |  |
|  +5.08 |  +4.48 | 00:32:35.716 | Augsburg           | Bayer Leverkusen   | 130 | Carry           |   -   | [58.5, 17.6]    |  |
|  +6.29 |  +5.70 | 00:32:36.930 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pressure        |  Yes  | [62.4, 65.8]    |  |
|  +6.63 |  +6.03 | 00:32:37.262 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Dribbled Past   |  Yes  | [62.1, 68.3]    |  |
|  +6.63 |  +6.03 | 00:32:37.262 | Augsburg           | Bayer Leverkusen   | 130 | Dribble         |   -   | [58.0, 11.8]    |  |
|  +6.63 |  +6.03 | 00:32:37.262 | Augsburg           | Bayer Leverkusen   | 130 | Carry           |   -   | [58.0, 11.8]    |  |
|  +7.84 |  +7.25 | 00:32:38.478 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pressure        |  Yes  | [59.3, 71.8]    |  |
|  +8.95 |  +8.36 | 00:32:39.586 | Augsburg           | Bayer Leverkusen   | 130 | Pass            |   -   | [58.9, 6.7]     | -> Felix Uduokhai |
| +10.18 |  +9.59 | 00:32:40.818 | Bayer Leverkusen   | Bayer Leverkusen   | 130 | Pressure        |   -   | [69.4, 74.9]    |  |
| +10.72 | +10.13 | 00:32:41.357 | Augsburg           | Bayer Leverkusen   | 130 | Ball Receipt*   |   -   | [46.5, 6.7]     |  |

---

### Disagreement Case 92: `3837844_p37_137921f0`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3837844 (Ligue 1, 2022/2023)
- **counterpressing_team**: Montpellier
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 37
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:24:21.941) | **Initiation**: Pressure (00:24:22.552)
- **Initiation Delay**: 0.611s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.023s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.87 |  -1.48 | 00:24:21.067 | Paris Saint-Germai | Montpellier        | 36 | Pressure        |   -   | [80.0, 76.3]    |  |
|  -0.83 |  -1.44 | 00:24:21.107 | Montpellier        | Montpellier        | 36 | Pass            |   -   | [42.2, 3.8]     | Incomplete (Incomplete) |
|  +0.00 |  -0.61 | 00:24:21.941 | Montpellier        | Montpellier        | 36 | Ball Receipt*   |   -   | [45.1, 13.7]    | Incomplete |
|  +0.00 |  -0.61 | 00:24:21.941 | Paris Saint-Germai | Paris Saint-Germai | 37 | Interception    |  Yes  | [75.6, 69.6]    | Won |
|  +0.00 |  -0.61 | 00:24:21.941 | Paris Saint-Germai | Paris Saint-Germai | 37 | Carry           |   -   | [75.6, 69.6]    |  |
|  +0.61 |  +0.00 | 00:24:22.552 | Montpellier        | Paris Saint-Germai | 37 | Pressure        |  Yes  | [44.3, 12.4]    |  |
|  +1.11 |  +0.50 | 00:24:23.047 | Paris Saint-Germai | Paris Saint-Germai | 37 | Pass            |   -   | [77.7, 66.8]    | -> Lionel Andrés  |
|  +1.86 |  +1.25 | 00:24:23.801 | Paris Saint-Germai | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [84.5, 60.5]    |  |
|  +1.86 |  +1.25 | 00:24:23.801 | Paris Saint-Germai | Paris Saint-Germai | 37 | Pass            |   -   | [85.1, 60.1]    | -> Fabián Ruiz Pe |
|  +3.18 |  +2.57 | 00:24:25.124 | Paris Saint-Germai | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [77.7, 53.3]    |  |
|  +3.18 |  +2.57 | 00:24:25.124 | Paris Saint-Germai | Paris Saint-Germai | 37 | Carry           |   -   | [77.7, 53.3]    |  |
|  +3.78 |  +3.17 | 00:24:25.718 | Paris Saint-Germai | Paris Saint-Germai | 37 | Pass            |   -   | [75.8, 50.8]    | -> Vitor Machado  |
|  +4.09 |  +3.48 | 00:24:26.030 | Paris Saint-Germai | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [83.2, 53.1]    |  |
|  +4.09 |  +3.48 | 00:24:26.030 | Paris Saint-Germai | Paris Saint-Germai | 37 | Pass            |   -   | [83.2, 53.5]    | Incomplete (Incomplete) |
|  +4.63 |  +4.02 | 00:24:26.575 | Montpellier        | Paris Saint-Germai | 37 | Ball Recovery   |   -   | [33.1, 23.8]    |  |
|  +4.63 |  +4.02 | 00:24:26.575 | Montpellier        | Paris Saint-Germai | 37 | Carry           |   -   | [33.1, 23.8]    |  |
|  +5.60 |  +4.99 | 00:24:27.542 | Montpellier        | Paris Saint-Germai | 37 | Pass            |   -   | [37.1, 21.1]    | -> Valère Germain |
|  +6.21 |  +5.60 | 00:24:28.150 | Montpellier        | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [49.8, 20.0]    |  |
|  +6.21 |  +5.60 | 00:24:28.150 | Montpellier        | Paris Saint-Germai | 37 | Carry           |   -   | [49.8, 20.0]    |  |
|  +6.71 |  +6.10 | 00:24:28.651 | Montpellier        | Paris Saint-Germai | 37 | Pass            |   -   | [49.6, 19.2]    | Incomplete (Incomplete) |
|  +6.79 |  +6.18 | 00:24:28.733 | Montpellier        | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [42.6, 13.1]    | Incomplete |
|  +6.79 |  +6.18 | 00:24:28.733 | Paris Saint-Germai | Paris Saint-Germai | 37 | Block           |  Yes  | [72.6, 63.4]    |  |
|  +7.91 |  +7.30 | 00:24:29.854 | Paris Saint-Germai | Paris Saint-Germai | 37 | Ball Recovery   |   -   | [62.7, 62.2]    |  |
|  +7.91 |  +7.30 | 00:24:29.854 | Paris Saint-Germai | Paris Saint-Germai | 37 | Carry           |   -   | [62.7, 62.2]    |  |
| +12.71 | +12.10 | 00:24:34.654 | Paris Saint-Germai | Paris Saint-Germai | 37 | Pass            |   -   | [47.1, 56.3]    | -> Carlos Soler B |
| +14.37 | +13.76 | 00:24:36.312 | Paris Saint-Germai | Paris Saint-Germai | 37 | Ball Receipt*   |   -   | [69.9, 71.7]    |  |

---

### Disagreement Case 93: `3893808_p194_6ed8c874`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893808 (Women's World Cup, 2023)
- **counterpressing_team**: United States Women's
- **opponent_team_at_turnover**: Netherlands Women's
- **possession_team_at_counterpress_initiation**: Netherlands Women's
- **possession_id_at_counterpress_initiation**: 194
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:46:06.885) | **Initiation**: Pressure (00:46:07.500)
- **Initiation Delay**: 0.615s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.622s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.48 |  -3.10 | 00:46:04.404 | United States Wome | United States Wome | 193 | Ball Receipt*   |   -   | [53.7, 30.4]    |  |
|  -2.44 |  -3.06 | 00:46:04.444 | United States Wome | United States Wome | 193 | Pass            |   -   | [53.1, 28.6]    | Incomplete (Incomplete) |
|  -0.73 |  -1.35 | 00:46:06.151 | United States Wome | United States Wome | 193 | Pressure        |   -   | [50.8, 15.3]    |  |
|  +0.00 |  -0.61 | 00:46:06.885 | United States Wome | United States Wome | 193 | Ball Receipt*   |   -   | [50.8, 15.0]    | Incomplete |
|  +0.00 |  -0.61 | 00:46:06.885 | Netherlands Women' | Netherlands Women' | 194 | Pass            |   -   | [68.0, 66.0]    | -> Danielle van d |
|  +0.61 |  +0.00 | 00:46:07.500 | United States Wome | Netherlands Women' | 194 | Pressure        |  Yes  | [51.7, 14.1]    |  |
|  +0.86 |  +0.24 | 00:46:07.745 | Netherlands Women' | Netherlands Women' | 194 | Ball Receipt*   |   -   | [69.3, 64.2]    |  |
|  +0.86 |  +0.24 | 00:46:07.745 | Netherlands Women' | Netherlands Women' | 194 | Pass            |   -   | [68.9, 64.2]    | -> Damaris Berta  |
|  +1.64 |  +1.03 | 00:46:08.527 | Netherlands Women' | Netherlands Women' | 194 | Ball Receipt*   |   -   | [62.7, 56.2]    |  |
|  +1.64 |  +1.03 | 00:46:08.527 | Netherlands Women' | Netherlands Women' | 194 | Carry           |   -   | [62.7, 56.2]    |  |
|  +1.69 |  +1.08 | 00:46:08.580 | United States Wome | Netherlands Women' | 194 | Pressure        |  Yes  | [55.1, 24.4]    |  |
|  +2.24 |  +1.62 | 00:46:09.122 | Netherlands Women' | Netherlands Women' | 194 | Dispossessed    |   -   | [64.6, 55.7]    |  |
|  +2.24 |  +1.62 | 00:46:09.122 | United States Wome | Netherlands Women' | 194 | Duel            |  Yes  | [55.5, 24.4]    | Tackle, Success In Play |
|  +3.05 |  +2.43 | 00:46:09.935 | Netherlands Women' | Netherlands Women' | 194 | Pressure        |   -   | [49.2, 60.3]    |  |
|  +3.26 |  +2.64 | 00:46:10.143 | United States Wome | Netherlands Women' | 194 | Ball Recovery   |   -   | [70.0, 22.2]    |  |
|  +3.26 |  +2.64 | 00:46:10.143 | United States Wome | Netherlands Women' | 194 | Carry           |   -   | [70.0, 22.2]    |  |
|  +4.29 |  +3.68 | 00:46:11.180 | United States Wome | Netherlands Women' | 194 | Pass            |   -   | [70.0, 24.8]    | Incomplete (Incomplete) |
|  +6.17 |  +5.55 | 00:46:13.055 | United States Wome | Netherlands Women' | 194 | Pressure        |   -   | [90.9, 44.6]    |  |
|  +6.62 |  +6.01 | 00:46:13.509 | United States Wome | Netherlands Women' | 194 | Ball Receipt*   |   -   | [88.8, 44.2]    | Incomplete |
|  +6.62 |  +6.01 | 00:46:13.509 | Netherlands Women' | Netherlands Women' | 194 | Goal Keeper     |   -   | [26.4, 39.7]    |  |
| +11.26 | +10.65 | 00:46:18.146 | Netherlands Women' | Netherlands Women' | 194 | Duel            |   -   | [37.8, 47.2]    | Aerial Lost |
| +11.26 | +10.65 | 00:46:18.146 | United States Wome | Netherlands Women' | 194 | Pass            |   -   | [82.3, 32.9]    | Incomplete (Incomplete) |

---

### Disagreement Case 94: `3895202_p7_8b054676`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895202 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: Bayer Leverkusen
- **opponent_team_at_turnover**: RB Leipzig
- **possession_team_at_counterpress_initiation**: RB Leipzig
- **possession_id_at_counterpress_initiation**: 7
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:02:15.729) | **Initiation**: Pressure (00:02:16.363)
- **Initiation Delay**: 0.634s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.707s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.36 |  -1.99 | 00:02:14.372 | Bayer Leverkusen   | Bayer Leverkusen   | 6 | Ball Receipt*   |   -   | [17.0, 73.0]    |  |
|  -1.36 |  -1.99 | 00:02:14.372 | Bayer Leverkusen   | Bayer Leverkusen   | 6 | Carry           |   -   | [17.0, 73.0]    |  |
|  -1.34 |  -1.98 | 00:02:14.384 | Bayer Leverkusen   | Bayer Leverkusen   | 6 | Miscontrol      |   -   | [18.2, 72.8]    |  |
|  -0.18 |  -0.81 | 00:02:15.549 | Bayer Leverkusen   | Bayer Leverkusen   | 6 | Pressure        |   -   | [23.1, 73.5]    |  |
|  +0.00 |  -0.63 | 00:02:15.729 | RB Leipzig         | RB Leipzig         | 7 | Pass            |   -   | [96.0, 7.5]     | -> Xavi Simons |
|  +0.63 |  +0.00 | 00:02:16.363 | Bayer Leverkusen   | RB Leipzig         | 7 | Pressure        |  Yes  | [23.6, 63.5]    |  |
|  +0.69 |  +0.06 | 00:02:16.419 | RB Leipzig         | RB Leipzig         | 7 | Ball Receipt*   |   -   | [96.5, 13.5]    |  |
|  +0.69 |  +0.06 | 00:02:16.419 | RB Leipzig         | RB Leipzig         | 7 | Carry           |   -   | [96.5, 13.5]    |  |
|  +0.89 |  +0.26 | 00:02:16.619 | RB Leipzig         | RB Leipzig         | 7 | Pass            |   -   | [95.5, 14.0]    | -> Nicolas Seiwal |
|  +1.72 |  +1.08 | 00:02:17.447 | RB Leipzig         | RB Leipzig         | 7 | Ball Receipt*   |   -   | [87.5, 14.9]    |  |
|  +1.72 |  +1.08 | 00:02:17.447 | RB Leipzig         | RB Leipzig         | 7 | Carry           |   -   | [87.5, 14.9]    |  |
|  +2.21 |  +1.58 | 00:02:17.942 | RB Leipzig         | RB Leipzig         | 7 | Pass            |   -   | [87.5, 15.9]    | -> Xavi Simons |
|  +2.54 |  +1.91 | 00:02:18.273 | Bayer Leverkusen   | RB Leipzig         | 7 | Pressure        |  Yes  | [26.2, 57.1]    |  |
|  +2.81 |  +2.18 | 00:02:18.543 | RB Leipzig         | RB Leipzig         | 7 | Ball Receipt*   |   -   | [92.2, 24.1]    |  |
|  +2.81 |  +2.18 | 00:02:18.543 | RB Leipzig         | RB Leipzig         | 7 | Carry           |   -   | [92.2, 24.1]    |  |
|  +3.14 |  +2.51 | 00:02:18.872 | Bayer Leverkusen   | RB Leipzig         | 7 | Pressure        |  Yes  | [29.7, 57.2]    |  |
|  +3.44 |  +2.81 | 00:02:19.172 | RB Leipzig         | RB Leipzig         | 7 | Miscontrol      |   -   | [89.5, 23.7]    |  |
|  +5.34 |  +4.71 | 00:02:21.070 | RB Leipzig         | RB Leipzig         | 7 | 50/50           |   -   | [89.9, 19.4]    |  |
|  +5.34 |  +4.71 | 00:02:21.070 | Bayer Leverkusen   | RB Leipzig         | 7 | 50/50           |   -   | [30.2, 60.7]    |  |
|  +6.15 |  +5.51 | 00:02:21.876 | Bayer Leverkusen   | RB Leipzig         | 7 | Ball Recovery   |   -   | [28.4, 62.6]    |  |
|  +6.15 |  +5.51 | 00:02:21.876 | Bayer Leverkusen   | RB Leipzig         | 7 | Carry           |   -   | [28.4, 62.6]    |  |
|  +6.33 |  +5.69 | 00:02:22.058 | RB Leipzig         | RB Leipzig         | 7 | Pressure        |  Yes  | [89.6, 16.8]    |  |
|  +6.61 |  +5.98 | 00:02:22.340 | Bayer Leverkusen   | RB Leipzig         | 7 | Pass            |   -   | [28.6, 63.1]    | -> Josip Stanišić |
|  +7.35 |  +6.72 | 00:02:23.081 | Bayer Leverkusen   | RB Leipzig         | 7 | Ball Receipt*   |   -   | [21.0, 59.8]    |  |
|  +7.35 |  +6.72 | 00:02:23.081 | Bayer Leverkusen   | RB Leipzig         | 7 | Carry           |   -   | [21.0, 59.8]    |  |
|  +7.36 |  +6.73 | 00:02:23.089 | Bayer Leverkusen   | RB Leipzig         | 7 | Pass            |   -   | [21.0, 59.8]    | Incomplete (Incomplete) |
| +11.68 | +11.05 | 00:02:27.410 | RB Leipzig         | RB Leipzig         | 7 | Ball Recovery   |   -   | [41.6, 21.3]    |  |
| +11.68 | +11.05 | 00:02:27.410 | RB Leipzig         | RB Leipzig         | 7 | Carry           |   -   | [41.6, 21.3]    |  |

---

### Disagreement Case 95: `3893824_p96_b141bbe2`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893824 (Women's World Cup, 2023)
- **counterpressing_team**: Republic of Ireland Women's
- **opponent_team_at_turnover**: Nigeria Women's
- **possession_team_at_counterpress_initiation**: Nigeria Women's
- **possession_id_at_counterpress_initiation**: 96
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:01:36.048) | **Initiation**: Pressure (00:01:36.684)
- **Initiation Delay**: 0.636s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.47s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.48 |  -3.12 | 00:01:33.566 | Nigeria Women's    | Republic of Irelan | 95 | Pressure        |   -   | [67.9, 5.6]     |  |
|  -2.18 |  -2.81 | 00:01:33.871 | Republic of Irelan | Republic of Irelan | 95 | Ball Receipt*   |   -   | [49.0, 76.4]    |  |
|  -2.18 |  -2.81 | 00:01:33.871 | Republic of Irelan | Republic of Irelan | 95 | Miscontrol      |   -   | [48.1, 75.6]    |  |
|  -1.35 |  -1.99 | 00:01:34.696 | Republic of Irelan | Republic of Irelan | 95 | Pressure        |   -   | [48.4, 72.9]    |  |
|  +0.00 |  -0.64 | 00:01:36.048 | Nigeria Women's    | Nigeria Women's    | 96 | Pass            |   -   | [67.4, 10.5]    | -> Christy Onyena |
|  +0.64 |  +0.00 | 00:01:36.684 | Republic of Irelan | Nigeria Women's    | 96 | Pressure        |  Yes  | [59.0, 48.8]    |  |
|  +1.09 |  +0.46 | 00:01:37.141 | Nigeria Women's    | Nigeria Women's    | 96 | Ball Receipt*   |   -   | [63.3, 26.5]    |  |
|  +1.09 |  +0.46 | 00:01:37.141 | Nigeria Women's    | Nigeria Women's    | 96 | Pass            |   -   | [62.5, 27.1]    | -> Halimatu Ibrah |
|  +1.80 |  +1.16 | 00:01:37.849 | Nigeria Women's    | Nigeria Women's    | 96 | Ball Receipt*   |   -   | [69.6, 22.9]    |  |
|  +1.80 |  +1.16 | 00:01:37.849 | Nigeria Women's    | Nigeria Women's    | 96 | Carry           |   -   | [69.6, 22.9]    |  |
|  +1.96 |  +1.32 | 00:01:38.004 | Republic of Irelan | Nigeria Women's    | 96 | Pressure        |  Yes  | [53.0, 55.8]    |  |
|  +2.54 |  +1.91 | 00:01:38.589 | Republic of Irelan | Nigeria Women's    | 96 | Pressure        |  Yes  | [48.1, 59.2]    |  |
|  +3.15 |  +2.51 | 00:01:39.194 | Nigeria Women's    | Nigeria Women's    | 96 | Miscontrol      |   -   | [69.6, 20.9]    |  |
|  +4.11 |  +3.47 | 00:01:40.154 | Republic of Irelan | Nigeria Women's    | 96 | Ball Recovery   |   -   | [50.8, 62.2]    |  |
|  +4.11 |  +3.47 | 00:01:40.154 | Republic of Irelan | Nigeria Women's    | 96 | Carry           |   -   | [50.8, 62.2]    |  |
|  +4.14 |  +3.50 | 00:01:40.187 | Nigeria Women's    | Nigeria Women's    | 96 | Pressure        |  Yes  | [67.7, 19.0]    |  |
|  +5.91 |  +5.27 | 00:01:41.954 | Republic of Irelan | Nigeria Women's    | 96 | Dispossessed    |   -   | [43.7, 63.9]    |  |
|  +5.91 |  +5.27 | 00:01:41.954 | Nigeria Women's    | Nigeria Women's    | 96 | Duel            |  Yes  | [76.4, 16.2]    | Tackle, Success In Play |
|  +6.45 |  +5.82 | 00:01:42.501 | Republic of Irelan | Nigeria Women's    | 96 | Pressure        |   -   | [40.7, 63.9]    |  |
|  +6.89 |  +6.26 | 00:01:42.943 | Nigeria Women's    | Nigeria Women's    | 96 | Pass            |   -   | [83.6, 17.0]    | -> Antionette Oye |
|  +7.98 |  +7.34 | 00:01:44.028 | Nigeria Women's    | Nigeria Women's    | 96 | Ball Receipt*   |   -   | [81.3, 27.3]    |  |
|  +7.98 |  +7.34 | 00:01:44.028 | Nigeria Women's    | Nigeria Women's    | 96 | Carry           |   -   | [81.3, 27.3]    |  |
|  +8.16 |  +7.52 | 00:01:44.204 | Republic of Irelan | Nigeria Women's    | 96 | Pressure        |   -   | [38.3, 46.8]    |  |
| +11.74 | +11.10 | 00:01:47.786 | Nigeria Women's    | Nigeria Women's    | 96 | Pass            |   -   | [85.1, 19.8]    | -> Uchenna Kanu |
| +13.04 | +12.40 | 00:01:49.088 | Nigeria Women's    | Nigeria Women's    | 96 | Ball Receipt*   |   -   | [100.5, 3.4]    |  |

---

### Disagreement Case 96: `3893796_p31_9f7e1e53`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893796 (Women's World Cup, 2023)
- **counterpressing_team**: South Africa Women's
- **opponent_team_at_turnover**: Sweden Women's
- **possession_team_at_counterpress_initiation**: Sweden Women's
- **possession_id_at_counterpress_initiation**: 31
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:16:41.853) | **Initiation**: Pressure (00:16:42.493)
- **Initiation Delay**: 0.64s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.656s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -5.76 |  -6.40 | 00:16:36.092 | South Africa Women | South Africa Women | 30 | Ball Receipt*   |   -   | [60.9, 5.4]     |  |
|  -4.56 |  -5.20 | 00:16:37.292 | South Africa Women | South Africa Women | 30 | Miscontrol      |   -   | [62.5, 5.7]     |  |
|  -0.53 |  -1.17 | 00:16:41.327 | South Africa Women | South Africa Women | 30 | Pressure        |   -   | [46.1, 13.7]    |  |
|  +0.00 |  -0.64 | 00:16:41.853 | Sweden Women's     | Sweden Women's     | 31 | Ball Recovery   |   -   | [71.4, 70.0]    |  |
|  +0.00 |  -0.64 | 00:16:41.853 | Sweden Women's     | Sweden Women's     | 31 | Carry           |   -   | [71.4, 70.0]    |  |
|  +0.64 |  +0.00 | 00:16:42.493 | South Africa Women | Sweden Women's     | 31 | Pressure        |  Yes  | [52.4, 9.6]     |  |
|  +1.30 |  +0.66 | 00:16:43.149 | Sweden Women's     | Sweden Women's     | 31 | Dispossessed    |   -   | [70.5, 70.5]    |  |
|  +1.30 |  +0.66 | 00:16:43.149 | South Africa Women | Sweden Women's     | 31 | Duel            |  Yes  | [49.6, 9.6]     | Tackle, Success In Play |
|  +2.31 |  +1.67 | 00:16:44.161 | Sweden Women's     | Sweden Women's     | 31 | Pressure        |   -   | [72.1, 64.0]    |  |
|  +2.73 |  +2.09 | 00:16:44.579 | South Africa Women | Sweden Women's     | 31 | Pass            |   -   | [43.8, 15.6]    | Incomplete (Incomplete) |
|  +8.06 |  +7.42 | 00:16:49.917 | South Africa Women | Sweden Women's     | 31 | Ball Receipt*   |   -   | [72.4, 9.6]     | Incomplete |
|  +8.06 |  +7.42 | 00:16:49.917 | Sweden Women's     | Sweden Women's     | 31 | Ball Recovery   |   -   | [33.4, 78.1]    |  |
|  +8.06 |  +7.42 | 00:16:49.917 | Sweden Women's     | Sweden Women's     | 31 | Carry           |   -   | [33.4, 78.1]    |  |
|  +9.50 |  +8.86 | 00:16:51.352 | Sweden Women's     | Sweden Women's     | 31 | Pass            |   -   | [26.4, 74.6]    | -> Amanda Ilested |
| +10.35 |  +9.71 | 00:16:52.203 | Sweden Women's     | Sweden Women's     | 31 | Ball Receipt*   |   -   | [26.4, 67.3]    |  |
| +10.35 |  +9.71 | 00:16:52.203 | Sweden Women's     | Sweden Women's     | 31 | Carry           |   -   | [26.4, 67.3]    |  |
| +12.70 | +12.06 | 00:16:54.557 | Sweden Women's     | Sweden Women's     | 31 | Pass            |   -   | [32.2, 63.7]    | -> Magdalena Lill |

---

### Disagreement Case 97: `3998841_p175_f158632a`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3998841 (UEFA Women's Euro, 2025)
- **counterpressing_team**: Denmark Women's
- **opponent_team_at_turnover**: Sweden Women's
- **possession_team_at_counterpress_initiation**: Sweden Women's
- **possession_id_at_counterpress_initiation**: 175
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:49:46.857) | **Initiation**: Pressure (00:49:47.521)
- **Initiation Delay**: 0.664s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.505s) | Evidence: `duel_plus_pass` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| -23.76 | -24.43 | 00:49:23.092 | Denmark Women's    | Sweden Women's     | 173 | Goal Keeper     |   -   | [1.3, 38.4]     |  |
|  -2.93 |  -3.59 | 00:49:43.930 | Denmark Women's    | Denmark Women's    | 174 | Pass            |   -   | [5.2, 47.2]     | Incomplete (Incomplete) |
|  +0.00 |  -0.66 | 00:49:46.857 | Denmark Women's    | Denmark Women's    | 174 | Ball Receipt*   |   -   | [51.1, 45.6]    | Incomplete |
|  +0.00 |  -0.66 | 00:49:46.857 | Denmark Women's    | Denmark Women's    | 174 | Duel            |   -   | [53.2, 46.0]    | Aerial Lost |
|  +0.00 |  -0.66 | 00:49:46.857 | Sweden Women's     | Sweden Women's     | 175 | Pass            |   -   | [66.9, 34.1]    | -> Emma Stina Bla |
|  +0.66 |  +0.00 | 00:49:47.521 | Denmark Women's    | Sweden Women's     | 175 | Pressure        |  Yes  | [44.9, 45.6]    |  |
|  +0.71 |  +0.05 | 00:49:47.569 | Sweden Women's     | Sweden Women's     | 175 | Ball Receipt*   |   -   | [75.2, 34.5]    |  |
|  +0.71 |  +0.05 | 00:49:47.569 | Sweden Women's     | Sweden Women's     | 175 | Carry           |   -   | [75.2, 34.5]    |  |
|  +1.64 |  +0.98 | 00:49:48.499 | Denmark Women's    | Sweden Women's     | 175 | Pressure        |  Yes  | [45.7, 44.5]    |  |
|  +2.17 |  +1.50 | 00:49:49.026 | Sweden Women's     | Sweden Women's     | 175 | Dispossessed    |   -   | [72.7, 36.7]    |  |
|  +2.17 |  +1.50 | 00:49:49.026 | Denmark Women's    | Sweden Women's     | 175 | Duel            |  Yes  | [47.4, 43.4]    | Tackle, Success In Play |
|  +4.17 |  +3.51 | 00:49:51.029 | Denmark Women's    | Sweden Women's     | 175 | Pass            |   -   | [40.4, 27.8]    | Incomplete (Unknown) |
|  +6.38 |  +5.71 | 00:49:53.235 | Denmark Women's    | Sweden Women's     | 175 | Ball Receipt*   |   -   | [76.9, 39.3]    | Incomplete |
|  +6.38 |  +5.71 | 00:49:53.235 | Denmark Women's    | Sweden Women's     | 175 | Foul Committed  |   -   | [79.6, 41.0]    |  |
|  +6.38 |  +5.71 | 00:49:53.235 | Sweden Women's     | Sweden Women's     | 175 | Foul Won        |   -   | [40.5, 39.1]    |  |
| +37.89 | +37.22 | 00:50:24.744 | Sweden Women's     | Sweden Women's     | 176 | Pass            |   -   | [43.6, 41.3]    | -> Emma Stina Bla |
| +43.03 | +42.37 | 00:50:29.888 | Sweden Women's     | Sweden Women's     | 176 | Ball Receipt*   |   -   | [109.0, 16.6]   |  |

---

### Disagreement Case 98: `3794685_p84_8fa318cf`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3794685 (UEFA Euro, 2020)
- **counterpressing_team**: Italy
- **opponent_team_at_turnover**: Austria
- **possession_team_at_counterpress_initiation**: Austria
- **possession_id_at_counterpress_initiation**: 84
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:00:46.780) | **Initiation**: Pressure (00:00:47.445)
- **Initiation Delay**: 0.665s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: 10.481s) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.321s) | Evidence: `interception_plus_control` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.75 |  -4.42 | 00:00:43.026 | Italy              | Italy              | 83 | Ball Receipt*   |   -   | [65.0, 7.4]     |  |
|  -3.75 |  -4.42 | 00:00:43.026 | Italy              | Italy              | 83 | Carry           |   -   | [65.0, 7.4]     |  |
|  -1.30 |  -1.97 | 00:00:45.477 | Italy              | Italy              | 83 | Pass            |   -   | [62.5, 4.3]     | Incomplete (Incomplete) |
|  +0.00 |  -0.66 | 00:00:46.780 | Italy              | Italy              | 83 | Ball Receipt*   |   -   | [50.1, 13.5]    | Incomplete |
|  +0.00 |  -0.66 | 00:00:46.780 | Austria            | Austria            | 84 | Pass            |  Yes  | [65.4, 68.1]    | -> Konrad Laimer |
|  +0.66 |  +0.00 | 00:00:47.445 | Italy              | Austria            | 84 | Pressure        |  Yes  | [51.1, 12.1]    |  |
|  +0.91 |  +0.25 | 00:00:47.693 | Austria            | Austria            | 84 | Ball Receipt*   |   -   | [65.4, 71.8]    |  |
|  +0.91 |  +0.25 | 00:00:47.693 | Austria            | Austria            | 84 | Carry           |   -   | [65.4, 71.8]    |  |
|  +0.92 |  +0.25 | 00:00:47.699 | Austria            | Austria            | 84 | Pass            |   -   | [64.8, 71.7]    | -> Florian Grilli |
|  +2.25 |  +1.59 | 00:00:49.031 | Austria            | Austria            | 84 | Ball Receipt*   |   -   | [73.7, 70.7]    |  |
|  +2.25 |  +1.59 | 00:00:49.031 | Austria            | Austria            | 84 | Pass            |   -   | [73.7, 70.7]    | Incomplete (Incomplete) |
|  +2.87 |  +2.20 | 00:00:49.648 | Austria            | Austria            | 84 | Pressure        |   -   | [63.5, 65.8]    |  |
|  +2.99 |  +2.32 | 00:00:49.766 | Austria            | Austria            | 84 | Ball Receipt*   |   -   | [65.0, 66.2]    | Incomplete |
|  +2.99 |  +2.32 | 00:00:49.766 | Italy              | Austria            | 84 | Interception    |  Yes  | [51.5, 12.5]    | Success In Play |
|  +3.97 |  +3.30 | 00:00:50.749 | Austria            | Austria            | 84 | Pressure        |   -   | [70.0, 62.5]    |  |
|  +4.11 |  +3.45 | 00:00:50.890 | Italy              | Austria            | 84 | Ball Recovery   |   -   | [47.2, 18.0]    |  |
|  +4.11 |  +3.45 | 00:00:50.890 | Italy              | Austria            | 84 | Carry           |   -   | [47.2, 18.0]    |  |
|  +4.56 |  +3.89 | 00:00:51.337 | Austria            | Austria            | 84 | Dribbled Past   |  Yes  | [72.9, 62.2]    |  |
|  +4.56 |  +3.89 | 00:00:51.337 | Italy              | Austria            | 84 | Dribble         |   -   | [47.2, 17.9]    |  |
|  +4.56 |  +3.89 | 00:00:51.337 | Italy              | Austria            | 84 | Carry           |   -   | [47.2, 17.9]    |  |
|  +4.66 |  +4.00 | 00:00:51.442 | Austria            | Austria            | 84 | Pressure        |  Yes  | [72.9, 64.3]    |  |
|  +4.98 |  +4.31 | 00:00:51.755 | Italy              | Austria            | 84 | Pass            |   -   | [48.0, 17.6]    | -> Jorge Luiz Fre |
|  +5.35 |  +4.69 | 00:00:52.132 | Austria            | Austria            | 84 | Pressure        |  Yes  | [63.5, 61.9]    |  |
|  +5.64 |  +4.98 | 00:00:52.424 | Italy              | Austria            | 84 | Ball Receipt*   |   -   | [55.6, 17.2]    |  |
|  +5.64 |  +4.98 | 00:00:52.424 | Italy              | Austria            | 84 | Carry           |   -   | [55.6, 17.2]    |  |
|  +5.70 |  +5.03 | 00:00:52.477 | Italy              | Austria            | 84 | Pass            |   -   | [55.7, 16.2]    | Incomplete (Incomplete) |
|  +5.93 |  +5.27 | 00:00:52.711 | Italy              | Austria            | 84 | Ball Receipt*   |   -   | [50.5, 12.1]    | Incomplete |
|  +5.93 |  +5.27 | 00:00:52.711 | Austria            | Austria            | 84 | Block           |  Yes  | [67.1, 65.8]    |  |
|  +6.39 |  +5.73 | 00:00:53.170 | Austria            | Austria            | 84 | Ball Recovery   |   -   | [65.5, 65.3]    |  |
|  +6.39 |  +5.73 | 00:00:53.170 | Austria            | Austria            | 84 | Carry           |   -   | [65.5, 65.3]    |  |
|  +7.00 |  +6.34 | 00:00:53.780 | Italy              | Austria            | 84 | Dribbled Past   |   -   | [57.5, 15.6]    |  |
|  +7.00 |  +6.34 | 00:00:53.780 | Austria            | Austria            | 84 | Dribble         |   -   | [62.6, 64.5]    |  |
|  +7.00 |  +6.34 | 00:00:53.780 | Austria            | Austria            | 84 | Carry           |   -   | [62.6, 64.5]    |  |
|  +8.80 |  +8.13 | 00:00:55.575 | Austria            | Austria            | 84 | Pass            |   -   | [65.2, 65.2]    | -> Stefan Lainer |
|  +9.69 |  +9.02 | 00:00:56.469 | Austria            | Austria            | 84 | Ball Receipt*   |   -   | [63.0, 69.8]    |  |
|  +9.69 |  +9.02 | 00:00:56.469 | Austria            | Austria            | 84 | Carry           |   -   | [63.0, 69.8]    |  |

---

### Disagreement Case 99: `3893832_p99_c6969471`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3893832 (Women's World Cup, 2023)
- **counterpressing_team**: Jamaica Women's
- **opponent_team_at_turnover**: Brazil Women's
- **possession_team_at_counterpress_initiation**: Brazil Women's
- **possession_id_at_counterpress_initiation**: 99
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:02:58.979) | **Initiation**: Pressure (00:02:59.647)
- **Initiation Delay**: 0.668s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.047s) | Evidence: `ball_recovery_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.95 |  -1.62 | 00:02:58.031 | Brazil Women's     | Jamaica Women's    | 98 | Duel            |   -   | [5.0, 15.5]     | Aerial Lost |
|  -0.95 |  -1.62 | 00:02:58.031 | Jamaica Women's    | Jamaica Women's    | 98 | Pass            |   -   | [115.1, 64.6]   | Incomplete (Incomplete) |
|  +0.00 |  -0.67 | 00:02:58.979 | Jamaica Women's    | Jamaica Women's    | 98 | Ball Receipt*   |   -   | [104.8, 63.4]   | Incomplete |
|  +0.00 |  -0.67 | 00:02:58.979 | Brazil Women's     | Brazil Women's     | 99 | Ball Recovery   |   -   | [11.6, 18.7]    |  |
|  +0.00 |  -0.67 | 00:02:58.979 | Brazil Women's     | Brazil Women's     | 99 | Carry           |   -   | [11.6, 18.7]    |  |
|  +0.67 |  +0.00 | 00:02:59.647 | Jamaica Women's    | Brazil Women's     | 99 | Pressure        |  Yes  | [104.8, 64.4]   |  |
|  +0.92 |  +0.25 | 00:02:59.901 | Brazil Women's     | Brazil Women's     | 99 | Pass            |   -   | [12.9, 15.7]    | -> Beatriz Zanera |
|  +1.97 |  +1.30 | 00:03:00.951 | Brazil Women's     | Brazil Women's     | 99 | Ball Receipt*   |   -   | [14.6, 5.7]     |  |
|  +1.97 |  +1.30 | 00:03:00.951 | Brazil Women's     | Brazil Women's     | 99 | Carry           |   -   | [14.6, 5.7]     |  |
|  +2.34 |  +1.67 | 00:03:01.314 | Brazil Women's     | Brazil Women's     | 99 | Pass            |   -   | [16.4, 6.7]     | -> Débora Cristia |
|  +2.59 |  +1.92 | 00:03:01.564 | Brazil Women's     | Brazil Women's     | 99 | Ball Receipt*   |   -   | [27.3, 5.1]     |  |
|  +2.59 |  +1.92 | 00:03:01.564 | Brazil Women's     | Brazil Women's     | 99 | Carry           |   -   | [27.3, 5.1]     |  |
|  +2.59 |  +1.92 | 00:03:01.564 | Jamaica Women's    | Brazil Women's     | 99 | Block           |  Yes  | [98.0, 73.6]    |  |
|  +3.80 |  +3.13 | 00:03:02.777 | Jamaica Women's    | Brazil Women's     | 99 | Pressure        |  Yes  | [91.5, 68.8]    |  |
|  +3.90 |  +3.23 | 00:03:02.877 | Brazil Women's     | Brazil Women's     | 99 | Pass            |   -   | [27.2, 7.3]     | Incomplete (Incomplete) |
|  +4.72 |  +4.05 | 00:03:03.694 | Jamaica Women's    | Brazil Women's     | 99 | Ball Recovery   |   -   | [90.6, 60.1]    |  |
|  +4.72 |  +4.05 | 00:03:03.694 | Jamaica Women's    | Brazil Women's     | 99 | Carry           |   -   | [90.6, 60.1]    |  |
|  +6.68 |  +6.01 | 00:03:05.660 | Jamaica Women's    | Brazil Women's     | 99 | Pass            |   -   | [89.9, 57.1]    | Incomplete (Incomplete) |
|  +7.15 |  +6.48 | 00:03:06.126 | Jamaica Women's    | Brazil Women's     | 99 | Ball Receipt*   |   -   | [99.8, 62.4]    | Incomplete |
|  +7.15 |  +6.48 | 00:03:06.126 | Brazil Women's     | Brazil Women's     | 99 | Interception    |  Yes  | [24.3, 19.5]    | Won |
|  +7.15 |  +6.48 | 00:03:06.126 | Brazil Women's     | Brazil Women's     | 99 | Carry           |   -   | [24.3, 19.5]    |  |
|  +7.84 |  +7.17 | 00:03:06.815 | Jamaica Women's    | Brazil Women's     | 99 | Pressure        |   -   | [90.9, 61.7]    |  |
|  +8.10 |  +7.43 | 00:03:07.080 | Brazil Women's     | Brazil Women's     | 99 | Pass            |   -   | [27.8, 18.9]    | Incomplete (Incomplete) |
|  +8.26 |  +7.59 | 00:03:07.239 | Jamaica Women's    | Brazil Women's     | 99 | Block           |   -   | [91.2, 60.9]    |  |
|  +9.60 |  +8.94 | 00:03:08.583 | Jamaica Women's    | Brazil Women's     | 99 | 50/50           |   -   | [98.6, 50.3]    |  |
|  +9.60 |  +8.94 | 00:03:08.583 | Brazil Women's     | Brazil Women's     | 99 | 50/50           |  Yes  | [21.5, 29.8]    |  |

---

### Disagreement Case 100: `3895107_p46_8aa2fa41`
**Classification**: False-Negative Candidate (Annot=0, Ctrl=1) | **Cohort Eligible**: `True`
- **Match**: 3895107 (1. Bundesliga, 2023/2024)
- **counterpressing_team**: FC Köln
- **opponent_team_at_turnover**: Bayer Leverkusen
- **possession_team_at_counterpress_initiation**: Bayer Leverkusen
- **possession_id_at_counterpress_initiation**: 46
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:23:57.263) | **Initiation**: Pressure (00:23:57.982)
- **Initiation Delay**: 0.719s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` (time: nans) | Outcome 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.952s) | Evidence: `duel_plus_carry` | Outcome 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.88 |  -2.60 | 00:23:55.378 | FC Köln            | FC Köln            | 45 | Ball Receipt*   |   -   | [41.0, 78.1]    |  |
|  -1.88 |  -2.60 | 00:23:55.378 | FC Köln            | FC Köln            | 45 | Carry           |   -   | [41.0, 78.1]    |  |
|  -1.57 |  -2.29 | 00:23:55.690 | FC Köln            | FC Köln            | 45 | Pass            |   -   | [41.2, 78.2]    | Incomplete (Incomplete) |
|  +0.00 |  -0.72 | 00:23:57.263 | FC Köln            | FC Köln            | 45 | Ball Receipt*   |   -   | [55.9, 78.2]    | Incomplete |
|  +0.00 |  -0.72 | 00:23:57.263 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Pass            |  Yes  | [66.4, 2.5]     | -> Alejandro Grim |
|  +0.72 |  +0.00 | 00:23:57.982 | FC Köln            | Bayer Leverkusen   | 46 | Pressure        |  Yes  | [44.7, 78.3]    |  |
|  +0.97 |  +0.25 | 00:23:58.228 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Ball Receipt*   |   -   | [73.2, 1.4]     |  |
|  +0.97 |  +0.25 | 00:23:58.228 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Carry           |   -   | [73.2, 1.4]     |  |
|  +1.16 |  +0.44 | 00:23:58.419 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Pass            |   -   | [72.5, 2.0]     | -> Florian Wirtz |
|  +1.73 |  +1.01 | 00:23:58.989 | FC Köln            | Bayer Leverkusen   | 46 | Pressure        |  Yes  | [51.9, 76.7]    |  |
|  +1.74 |  +1.02 | 00:23:59.004 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Ball Receipt*   |   -   | [72.7, 5.7]     |  |
|  +1.74 |  +1.02 | 00:23:59.004 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Carry           |   -   | [72.7, 5.7]     |  |
|  +2.67 |  +1.95 | 00:23:59.934 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Dispossessed    |   -   | [70.2, 3.9]     |  |
|  +2.67 |  +1.95 | 00:23:59.934 | FC Köln            | Bayer Leverkusen   | 46 | Duel            |  Yes  | [49.9, 76.2]    | Tackle, Won |
|  +2.67 |  +1.95 | 00:23:59.934 | FC Köln            | Bayer Leverkusen   | 46 | Carry           |   -   | [49.9, 76.2]    |  |
|  +4.54 |  +3.82 | 00:24:01.806 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Pressure        |  Yes  | [69.2, 5.1]     |  |
|  +5.79 |  +5.07 | 00:24:03.049 | FC Köln            | Bayer Leverkusen   | 46 | Dispossessed    |   -   | [48.8, 77.3]    |  |
|  +5.79 |  +5.07 | 00:24:03.049 | Bayer Leverkusen   | Bayer Leverkusen   | 46 | Duel            |  Yes  | [71.3, 2.8]     | Tackle, Success Out |
| +13.53 | +12.81 | 00:24:10.790 | Bayer Leverkusen   | Bayer Leverkusen   | 47 | Pass            |   -   | [75.2, 0.1]     | -> Victor Okoh Bo |
| +14.77 | +14.05 | 00:24:12.030 | Bayer Leverkusen   | Bayer Leverkusen   | 47 | Ball Receipt*   |   -   | [74.8, 9.6]     |  |

---
