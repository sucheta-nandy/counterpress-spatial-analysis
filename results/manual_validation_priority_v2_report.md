# Priority Manual Validation Sample v2 (40 Cases)

This document re-evaluates the **40 priority validation episodes** following the implementation of the evidence-based controlled possession regain detector.

## Executive Review of Key Investigated Cases

### CASE 9 (`3788766_p107_15ad5bb1`) — False Positive Resolved
- **Old Label**: `regain_5s = 1` (`seconds_to_regain = 0.25s`, `successful_regain`)
- **New Label**: `regain_5s_controlled = 0` (`controlled_regain_time = 7.33s`, `harmless_escape`)
- **Resolution Rationale**: At 00:08:11.246 (0.25s after Italy's Pressure), Wales passed the ball. StatsBomb retained `possession_team: Italy` during Wales's ongoing sequence. Italy performed no on-ball action until a Ball Recovery + Carry at 00:08:18.326 (7.33s). The new evidence-based detector rejects opponent actions and accurately labels this as 0 within the 5-second horizon.

### CASE 18 (`3857276_p12_fcc6b2e3`) — False Negative Resolved
- **Old Label**: `regain_5s = 0` (`seconds_to_regain = nan`, `harmless_escape`)
- **New Label**: `regain_5s_controlled = 1` (`controlled_regain_time = 3.892s`, `successful_regain`)
- **Resolution Rationale**: Morocco pressured at 00:05:49.485. Following a Canada miscontrol, Morocco executed a Ball Recovery + Carry at 00:05:53.377 (3.892s). Because StatsBomb left `possession_team: Canada` un-incremented until event 256, the old algorithm erroneously marked regain as 0. The new detector captures the recovery + carry under control and correctly assigns 1.

### CASE 37 (`3802805_p92_835a9886`) — Tactical Risk Precedence & Extended Trace Visibility
- **Labels**: `regain_5s_controlled = 1` (at 4.966s, `ball_recovery_plus_carry`), `dangerous_escape_15s = 1`, `outcome_3class = dangerous_escape`
- **Resolution Rationale**: Prior reporting truncated the trace at 00:40:30.326 (showing only a Nice Block). The extended trace reveals that at 00:40:33.230 (4.966s), Nice executed a Ball Recovery + Carry. Crucially, at dt = 0.002s, PSG had already penetrated into the attacking third (x = 83.3). Because tactical danger occurred before possession was established, the episode is classified as `dangerous_escape`.

### CASE 40 (`3895180_p19_f72281df`) — Trace Window Slicing Fixed & Danger Precedence
- **Labels**: `regain_5s_controlled = 1` (at 3.277s, `ball_recovery_plus_carry`), `dangerous_escape_15s = 1`, `outcome_3class = dangerous_escape`
- **Resolution Rationale**: Prior reporting truncated at 00:05:26.334 (showing only Frankfurt's miscontrol and pressure). The extended trace demonstrates that at 00:05:26.741 (3.277s), Leverkusen executed Ball Recovery + Carry + Dribble + Pass. However, Frankfurt had penetrated into the final third (x = 87.5 at dt = 1.29s). Thus, the episode is correctly classified as `dangerous_escape`.

---

### Priority Case 1: `3837827_p81_932e1ec0` [ordinary_successful_regain]
- **Match**: 3837827 (Ligue 1)
- **counterpressing_team**: Rennes
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Rennes
- **possession_id_at_counterpress_initiation**: 81
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:01:26.560) | **Initiation**: Duel (00:01:26.560)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.0s) | Evidence: `carry_control` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.46 |  -1.46 | 00:01:25.096 | Paris Saint-Germai | Paris Saint-Germai | 80 | Pass            |   -   | [61.5, 50.4]    | -> Warren Zaire E |
|  -0.73 |  -0.73 | 00:01:25.828 | Paris Saint-Germai | Paris Saint-Germai | 80 | Ball Receipt*   |   -   | [62.7, 41.2]    |  |
|  -0.73 |  -0.73 | 00:01:25.828 | Paris Saint-Germai | Paris Saint-Germai | 80 | Carry           |   -   | [62.7, 41.2]    |  |
|  -0.72 |  -0.72 | 00:01:25.840 | Rennes             | Paris Saint-Germai | 80 | Pressure        |   -   | [60.8, 37.1]    |  |
|  +0.00 |  +0.00 | 00:01:26.560 | Paris Saint-Germai | Paris Saint-Germai | 80 | Dispossessed    |   -   | [62.0, 42.1]    |  |
|  +0.00 |  +0.00 | 00:01:26.560 | Rennes             | Rennes             | 81 | Duel            |  Yes  | [58.1, 38.0]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:01:26.560 | Rennes             | Rennes             | 81 | Carry           |   -   | [58.1, 38.0]    |  |
|  +0.52 |  +0.52 | 00:01:27.081 | Paris Saint-Germai | Rennes             | 81 | Pressure        |  Yes  | [60.4, 44.8]    |  |
|  +0.82 |  +0.82 | 00:01:27.377 | Paris Saint-Germai | Rennes             | 81 | Dribbled Past   |  Yes  | [61.5, 44.3]    |  |
|  +0.82 |  +0.82 | 00:01:27.377 | Rennes             | Rennes             | 81 | Dribble         |   -   | [58.6, 35.8]    |  |
|  +0.82 |  +0.82 | 00:01:27.377 | Rennes             | Rennes             | 81 | Carry           |   -   | [58.6, 35.8]    |  |
|  +3.07 |  +3.07 | 00:01:29.627 | Paris Saint-Germai | Rennes             | 81 | Pressure        |  Yes  | [53.6, 45.3]    |  |
|  +4.50 |  +4.50 | 00:01:31.056 | Rennes             | Rennes             | 81 | Dribble         |   -   | [75.0, 33.9]    |  |
|  +4.50 |  +4.50 | 00:01:31.056 | Paris Saint-Germai | Rennes             | 81 | Duel            |  Yes  | [45.1, 46.2]    | Tackle, Lost In Play |
|  +6.32 |  +6.32 | 00:01:32.883 | Rennes             | Rennes             | 81 | Ball Recovery   |   -   | [69.0, 28.0]    |  |
|  +6.32 |  +6.32 | 00:01:32.883 | Rennes             | Rennes             | 81 | Carry           |   -   | [69.0, 28.0]    |  |
|  +6.86 |  +6.86 | 00:01:33.416 | Rennes             | Rennes             | 81 | Pass            |   -   | [67.2, 27.1]    | -> Arthur Theate |
|  +8.51 |  +8.51 | 00:01:35.069 | Rennes             | Rennes             | 81 | Ball Receipt*   |   -   | [56.5, 24.1]    |  |
|  +8.51 |  +8.51 | 00:01:35.069 | Rennes             | Rennes             | 81 | Carry           |   -   | [56.5, 24.1]    |  |

---

### Priority Case 2: `3857258_p145_a3bf4cb0` [ordinary_successful_regain]
- **Match**: 3857258 (FIFA World Cup)
- **counterpressing_team**: Brazil
- **opponent_team_at_turnover**: Serbia
- **possession_team_at_counterpress_initiation**: Brazil
- **possession_id_at_counterpress_initiation**: 145
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:37:18.826) | **Initiation**: Pass (00:37:25.209)
- **Initiation Delay**: 6.383s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.751s) | Evidence: `controlled_ball_receipt` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.47 |  -8.85 | 00:37:16.361 | Serbia             | Serbia             | 144 | Ball Receipt*   |   -   | [18.7, 34.2]    |  |
|  -1.83 |  -8.21 | 00:37:16.996 | Serbia             | Serbia             | 144 | Pass            |   -   | [20.5, 34.2]    | -> Vanja Milinkov |
|  +0.00 |  -6.38 | 00:37:18.826 | Serbia             | Serbia             | 144 | Ball Receipt*   |   -   | [9.2, 29.4]     |  |
|  +0.04 |  -6.34 | 00:37:18.867 | Serbia             | Serbia             | 144 | Pass            |   -   | [9.2, 28.8]     | -> Strahinja Pavl |
|  +1.40 |  -4.98 | 00:37:20.226 | Serbia             | Serbia             | 144 | Ball Receipt*   |   -   | [19.7, 13.5]    |  |
|  +1.40 |  -4.98 | 00:37:20.226 | Serbia             | Serbia             | 144 | Carry           |   -   | [19.7, 13.5]    |  |
|  +2.25 |  -4.14 | 00:37:21.072 | Serbia             | Serbia             | 144 | Pass            |   -   | [14.8, 3.0]     | -> Nemanja Radonj |
|  +3.47 |  -2.91 | 00:37:22.300 | Serbia             | Serbia             | 144 | Ball Receipt*   |   -   | [34.3, 1.2]     |  |
|  +3.47 |  -2.91 | 00:37:22.300 | Serbia             | Serbia             | 144 | Carry           |   -   | [34.3, 1.2]     |  |
|  +4.44 |  -1.95 | 00:37:23.263 | Serbia             | Serbia             | 144 | Pass            |   -   | [32.5, 2.4]     | Incomplete (Incomplete) |
|  +6.08 |  -0.30 | 00:37:24.905 | Serbia             | Serbia             | 144 | Pressure        |   -   | [45.6, 3.7]     |  |
|  +6.38 |  +0.00 | 00:37:25.209 | Serbia             | Serbia             | 144 | Ball Receipt*   |   -   | [45.6, 2.7]     | Incomplete |
|  +6.38 |  +0.00 | 00:37:25.209 | Brazil             | Brazil             | 145 | Pass            |  Yes  | [71.4, 77.7]    | -> Danilo Luiz da |
|  +7.13 |  +0.75 | 00:37:25.960 | Brazil             | Brazil             | 145 | Ball Receipt*   |   -   | [82.2, 75.9]    |  |
|  +7.13 |  +0.75 | 00:37:25.960 | Brazil             | Brazil             | 145 | Carry           |   -   | [82.2, 75.9]    |  |
|  +7.29 |  +0.91 | 00:37:26.120 | Brazil             | Brazil             | 145 | Pass            |   -   | [78.3, 75.3]    | -> Carlos Henriqu |
|  +8.28 |  +1.90 | 00:37:27.106 | Brazil             | Brazil             | 145 | Ball Receipt*   |   -   | [68.9, 66.9]    |  |
|  +8.28 |  +1.90 | 00:37:27.106 | Brazil             | Brazil             | 145 | Carry           |   -   | [68.9, 66.9]    |  |
| +10.33 |  +3.95 | 00:37:29.159 | Brazil             | Brazil             | 145 | Pass            |   -   | [67.6, 61.2]    | -> Frederico Rodr |
| +11.69 |  +5.31 | 00:37:30.516 | Brazil             | Brazil             | 145 | Ball Receipt*   |   -   | [87.3, 57.7]    |  |
| +11.69 |  +5.31 | 00:37:30.516 | Brazil             | Brazil             | 145 | Carry           |   -   | [87.3, 57.7]    |  |
| +13.70 |  +7.32 | 00:37:32.531 | Brazil             | Brazil             | 145 | Shot            |   -   | [95.6, 43.5]    | Saved |
| +14.29 |  +7.91 | 00:37:33.116 | Serbia             | Brazil             | 145 | Goal Keeper     |   -   | [6.2, 39.7]     |  |
| +35.76 | +29.38 | 00:37:54.585 | Serbia             | Brazil             | 145 | Substitution    |   -   | -               |  |
| +39.31 | +32.92 | 00:37:58.133 | Serbia             | Brazil             | 145 | Tactical Shift  |   -   | -               |  |

---

### Priority Case 3: `3857288_p133_70730b88` [ordinary_successful_regain]
- **Match**: 3857288 (FIFA World Cup)
- **counterpressing_team**: Tunisia
- **opponent_team_at_turnover**: Australia
- **possession_team_at_counterpress_initiation**: Tunisia
- **possession_id_at_counterpress_initiation**: 133
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:20:02.596) | **Initiation**: Duel (00:20:02.596)
- **Initiation Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.0s) | Evidence: `carry_control` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.13 |  -1.13 | 00:20:01.469 | Australia          | Australia          | 132 | Ball Receipt*   |   -   | [79.0, 39.7]    |  |
|  -1.13 |  -1.13 | 00:20:01.469 | Australia          | Australia          | 132 | Carry           |   -   | [79.0, 39.7]    |  |
|  -0.83 |  -0.83 | 00:20:01.770 | Tunisia            | Australia          | 132 | Pressure        |   -   | [38.6, 40.8]    |  |
|  -0.33 |  -0.33 | 00:20:02.271 | Tunisia            | Australia          | 132 | Pressure        |   -   | [44.3, 38.9]    |  |
|  +0.00 |  +0.00 | 00:20:02.596 | Australia          | Australia          | 132 | Dispossessed    |   -   | [76.4, 41.0]    |  |
|  +0.00 |  +0.00 | 00:20:02.596 | Tunisia            | Tunisia            | 133 | Duel            |  Yes  | [43.7, 39.1]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:20:02.596 | Tunisia            | Tunisia            | 133 | Carry           |   -   | [43.7, 39.1]    |  |
|  +1.54 |  +1.54 | 00:20:04.131 | Tunisia            | Tunisia            | 133 | Pass            |   -   | [42.6, 46.3]    | -> Naïm Sliti |
|  +3.38 |  +3.38 | 00:20:05.976 | Tunisia            | Tunisia            | 133 | Ball Receipt*   |   -   | [55.2, 72.0]    |  |
|  +3.38 |  +3.38 | 00:20:05.976 | Tunisia            | Tunisia            | 133 | Carry           |   -   | [55.2, 72.0]    |  |
|  +8.29 |  +8.29 | 00:20:10.882 | Tunisia            | Tunisia            | 133 | Pass            |   -   | [71.5, 51.1]    | -> Aïssa Bilal La |
|  +9.26 |  +9.26 | 00:20:11.858 | Tunisia            | Tunisia            | 133 | Ball Receipt*   |   -   | [75.1, 31.8]    |  |
|  +9.26 |  +9.26 | 00:20:11.858 | Tunisia            | Tunisia            | 133 | Carry           |   -   | [75.1, 31.8]    |  |
|  +9.97 |  +9.97 | 00:20:12.564 | Australia          | Tunisia            | 133 | Pressure        |   -   | [44.3, 50.2]    |  |
| +10.04 | +10.04 | 00:20:12.633 | Tunisia            | Tunisia            | 133 | Pass            |   -   | [76.9, 33.5]    | -> Youssef Msakni |
| +11.47 | +11.47 | 00:20:14.064 | Tunisia            | Tunisia            | 133 | Ball Receipt*   |   -   | [88.8, 13.4]    |  |
| +11.47 | +11.47 | 00:20:14.064 | Tunisia            | Tunisia            | 133 | Carry           |   -   | [88.8, 13.4]    |  |

---

### Priority Case 4: `3906390_p113_ba77b5bd` [ordinary_successful_regain]
- **Match**: 3906390 (Women's World Cup)
- **counterpressing_team**: Spain Women's
- **opponent_team_at_turnover**: England Women's
- **possession_team_at_counterpress_initiation**: Spain Women's
- **possession_id_at_counterpress_initiation**: 113
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:05:50.867) | **Initiation**: Pressure (00:05:52.775)
- **Initiation Delay**: 1.908s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.968s) | Evidence: `completed_pass` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.88 |  -2.79 | 00:05:49.987 | Spain Women's      | Spain Women's      | 113 | Pass            |   -   | [85.7, 17.7]    | Incomplete (Incomplete) |
|  +0.00 |  -1.91 | 00:05:50.867 | Spain Women's      | Spain Women's      | 113 | Ball Receipt*   |   -   | [85.7, 11.9]    | Incomplete |
|  +0.00 |  -1.91 | 00:05:50.867 | England Women's    | Spain Women's      | 113 | Interception    |  Yes  | [34.4, 66.0]    | Success In Play |
|  +1.43 |  -0.47 | 00:05:52.300 | England Women's    | Spain Women's      | 113 | Ball Recovery   |   -   | [39.4, 65.6]    |  |
|  +1.43 |  -0.47 | 00:05:52.300 | England Women's    | Spain Women's      | 113 | Carry           |   -   | [39.4, 65.6]    |  |
|  +1.91 |  +0.00 | 00:05:52.775 | Spain Women's      | Spain Women's      | 113 | Pressure        |  Yes  | [78.3, 9.6]     |  |
|  +2.42 |  +0.51 | 00:05:53.289 | England Women's    | Spain Women's      | 113 | Pass            |   -   | [43.2, 66.6]    | -> Lauren Hemp |
|  +3.60 |  +1.69 | 00:05:54.464 | Spain Women's      | Spain Women's      | 113 | Pressure        |  Yes  | [42.1, 22.3]    |  |
|  +3.64 |  +1.73 | 00:05:54.505 | England Women's    | Spain Women's      | 113 | Ball Receipt*   |   -   | [75.3, 59.4]    |  |
|  +3.64 |  +1.73 | 00:05:54.505 | England Women's    | Spain Women's      | 113 | Carry           |   -   | [75.3, 59.4]    |  |
|  +3.79 |  +1.88 | 00:05:54.657 | England Women's    | Spain Women's      | 113 | Pass            |   -   | [74.1, 58.8]    | Incomplete (Incomplete) |
|  +5.88 |  +3.97 | 00:05:56.743 | England Women's    | Spain Women's      | 113 | Ball Receipt*   |   -   | [69.5, 48.3]    | Incomplete |
|  +5.88 |  +3.97 | 00:05:56.743 | Spain Women's      | Spain Women's      | 113 | Pass            |   -   | [45.3, 38.9]    | -> Irene Paredes  |
|  +7.10 |  +5.20 | 00:05:57.972 | Spain Women's      | Spain Women's      | 113 | Ball Receipt*   |   -   | [34.7, 33.5]    |  |
|  +7.10 |  +5.20 | 00:05:57.972 | Spain Women's      | Spain Women's      | 113 | Carry           |   -   | [34.7, 33.5]    |  |
|  +7.17 |  +5.27 | 00:05:58.041 | Spain Women's      | Spain Women's      | 113 | Pass            |   -   | [36.1, 32.9]    | -> Teresa Abellei |
|  +8.10 |  +6.19 | 00:05:58.964 | Spain Women's      | Spain Women's      | 113 | Ball Receipt*   |   -   | [51.1, 27.1]    |  |
|  +8.10 |  +6.19 | 00:05:58.964 | Spain Women's      | Spain Women's      | 113 | Carry           |   -   | [51.1, 27.1]    |  |
|  +9.21 |  +7.31 | 00:06:00.080 | England Women's    | Spain Women's      | 113 | Pressure        |   -   | [69.3, 48.8]    |  |
|  +9.52 |  +7.61 | 00:06:00.385 | Spain Women's      | Spain Women's      | 113 | Pass            |   -   | [54.2, 25.8]    | -> Jennifer Hermo |
| +10.53 |  +8.62 | 00:06:01.398 | England Women's    | Spain Women's      | 113 | Pressure        |   -   | [60.2, 65.3]    |  |
| +10.61 |  +8.70 | 00:06:01.474 | Spain Women's      | Spain Women's      | 113 | Ball Receipt*   |   -   | [59.3, 15.9]    |  |

---

### Priority Case 5: `3893790_p172_aea04013` [ordinary_successful_regain]
- **Match**: 3893790 (Women's World Cup)
- **counterpressing_team**: Nigeria Women's
- **opponent_team_at_turnover**: Canada Women's
- **possession_team_at_counterpress_initiation**: Nigeria Women's
- **possession_id_at_counterpress_initiation**: 172
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:47:04.421) | **Initiation**: Duel (00:47:12.107)
- **Initiation Delay**: 7.686s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.235s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.83 |  -9.51 | 00:47:02.592 | Canada Women's     | Nigeria Women's    | 172 | Pressure        |   -   | [62.2, 41.4]    |  |
|  -1.35 |  -9.03 | 00:47:03.073 | Nigeria Women's    | Nigeria Women's    | 172 | Pass            |   -   | [53.3, 44.1]    | Incomplete (Incomplete) |
|  +0.00 |  -7.69 | 00:47:04.421 | Canada Women's     | Nigeria Women's    | 172 | Ball Recovery   |   -   | [48.1, 26.3]    |  |
|  +0.00 |  -7.69 | 00:47:04.421 | Canada Women's     | Nigeria Women's    | 172 | Carry           |   -   | [48.1, 26.3]    |  |
|  +1.12 |  -6.57 | 00:47:05.541 | Canada Women's     | Nigeria Women's    | 172 | Pass            |   -   | [50.5, 27.3]    | -> Cloé Zoé Eyja  |
|  +3.56 |  -4.13 | 00:47:07.980 | Canada Women's     | Nigeria Women's    | 172 | Ball Receipt*   |   -   | [80.8, 54.9]    |  |
|  +3.56 |  -4.13 | 00:47:07.980 | Canada Women's     | Nigeria Women's    | 172 | Carry           |   -   | [80.8, 54.9]    |  |
|  +7.69 |  +0.00 | 00:47:12.107 | Canada Women's     | Nigeria Women's    | 172 | Dribble         |   -   | [104.6, 51.0]   |  |
|  +7.69 |  +0.00 | 00:47:12.107 | Nigeria Women's    | Nigeria Women's    | 172 | Duel            |  Yes  | [15.5, 29.1]    | Tackle, Lost In Play |
|  +8.83 |  +1.15 | 00:47:13.254 | Canada Women's     | Nigeria Women's    | 172 | Ball Recovery   |   -   | [103.9, 54.3]   |  |
|  +9.92 |  +2.24 | 00:47:14.342 | Nigeria Women's    | Nigeria Women's    | 172 | Ball Recovery   |   -   | [18.8, 24.2]    |  |
|  +9.92 |  +2.24 | 00:47:14.342 | Nigeria Women's    | Nigeria Women's    | 172 | Carry           |   -   | [18.8, 24.2]    |  |
| +11.83 |  +4.14 | 00:47:16.251 | Nigeria Women's    | Nigeria Women's    | 172 | Pass            |   -   | [26.1, 22.2]    | -> Jennifer Onyi  |
| +13.19 |  +5.50 | 00:47:17.606 | Nigeria Women's    | Nigeria Women's    | 172 | Ball Receipt*   |   -   | [34.2, 5.8]     |  |
| +13.19 |  +5.50 | 00:47:17.606 | Nigeria Women's    | Nigeria Women's    | 172 | Carry           |   -   | [34.2, 5.8]     |  |
| +15.96 |  +8.28 | 00:47:20.384 | Nigeria Women's    | Nigeria Women's    | 172 | Pass            |   -   | [45.9, 5.0]     | -> Uchenna Kanu |
| +16.83 |  +9.14 | 00:47:21.252 | Nigeria Women's    | Nigeria Women's    | 172 | Ball Receipt*   |   -   | [65.8, 6.3]     |  |
| +16.83 |  +9.14 | 00:47:21.252 | Nigeria Women's    | Nigeria Women's    | 172 | Carry           |   -   | [65.8, 6.3]     |  |
| +17.50 |  +9.82 | 00:47:21.924 | Nigeria Women's    | Nigeria Women's    | 172 | Pass            |   -   | [67.6, 7.3]     | Incomplete (Incomplete) |
| +17.76 | +10.08 | 00:47:22.184 | Nigeria Women's    | Nigeria Women's    | 172 | Ball Receipt*   |   -   | [78.2, 15.5]    | Incomplete |

---

### Priority Case 6: `3998847_p26_e3799406` [ordinary_successful_regain]
- **Match**: 3998847 (UEFA Women's Euro)
- **counterpressing_team**: Spain Women's
- **opponent_team_at_turnover**: Belgium Women's
- **possession_team_at_counterpress_initiation**: Spain Women's
- **possession_id_at_counterpress_initiation**: 26
- **Turnover Context**: immediate_restart_phase (Origin: From Corner)
- **Turnover**: 50/50 (00:09:04.827) | **Initiation**: Pressure (00:09:06.288)
- **Initiation Delay**: 1.461s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 5.0s) | Evidence: `completed_pass` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -4.51 |  -5.97 | 00:09:00.315 | Spain Women's      | Spain Women's      | 26 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete) |
|  -2.83 |  -4.29 | 00:09:02.002 | Belgium Women's    | Spain Women's      | 26 | Clearance       |   -   | [6.0, 39.5]     |  |
|  +0.00 |  -1.46 | 00:09:04.827 | Spain Women's      | Spain Women's      | 26 | 50/50           |   -   | [97.0, 59.4]    |  |
|  +0.00 |  -1.46 | 00:09:04.827 | Belgium Women's    | Spain Women's      | 26 | 50/50           |   -   | [23.1, 20.7]    |  |
|  +0.00 |  -1.46 | 00:09:04.827 | Belgium Women's    | Spain Women's      | 26 | Carry           |   -   | [23.1, 20.7]    |  |
|  +1.46 |  +0.00 | 00:09:06.288 | Spain Women's      | Spain Women's      | 26 | Pressure        |  Yes  | [97.0, 59.4]    |  |
|  +3.63 |  +2.17 | 00:09:08.455 | Belgium Women's    | Spain Women's      | 26 | Pass            |   -   | [21.0, 21.3]    | -> Jarne Teulings |
|  +4.62 |  +3.16 | 00:09:09.445 | Belgium Women's    | Spain Women's      | 26 | Ball Receipt*   |   -   | [27.8, 8.9]     |  |
|  +4.62 |  +3.16 | 00:09:09.445 | Belgium Women's    | Spain Women's      | 26 | Carry           |   -   | [27.8, 8.9]     |  |
|  +4.75 |  +3.29 | 00:09:09.580 | Spain Women's      | Spain Women's      | 26 | Pressure        |  Yes  | [92.3, 72.1]    |  |
|  +5.19 |  +3.73 | 00:09:10.018 | Belgium Women's    | Spain Women's      | 26 | Pass            |   -   | [27.8, 8.4]     | Incomplete (Incomplete) |
|  +6.46 |  +5.00 | 00:09:11.288 | Spain Women's      | Spain Women's      | 26 | Pass            |  Yes  | [83.8, 62.9]    | -> María Francesc |
|  +8.19 |  +6.73 | 00:09:13.016 | Spain Women's      | Spain Women's      | 26 | Ball Receipt*   |   -   | [87.6, 72.4]    |  |
|  +8.19 |  +6.73 | 00:09:13.016 | Spain Women's      | Spain Women's      | 26 | Carry           |   -   | [87.6, 72.4]    |  |
|  +8.20 |  +6.74 | 00:09:13.031 | Belgium Women's    | Spain Women's      | 26 | Pressure        |   -   | [32.5, 7.7]     |  |
|  +8.39 |  +6.93 | 00:09:13.214 | Spain Women's      | Spain Women's      | 26 | Dribble         |   -   | [87.6, 72.4]    |  |
|  +8.39 |  +6.93 | 00:09:13.214 | Belgium Women's    | Spain Women's      | 26 | Duel            |   -   | [32.5, 7.7]     | Tackle, Success Out |
| +26.67 | +25.21 | 00:09:31.498 | Belgium Women's    | Belgium Women's    | 27 | Pass            |   -   | [41.7, 0.1]     | -> Hannah Eurling |
| +27.13 | +25.67 | 00:09:31.954 | Spain Women's      | Belgium Women's    | 27 | Pressure        |   -   | [69.4, 74.5]    |  |

---

### Priority Case 7: `3837938_p7_bb63490a` [ordinary_successful_regain]
- **Match**: 3837938 (Ligue 1)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: OGC Nice
- **possession_team_at_counterpress_initiation**: OGC Nice
- **possession_id_at_counterpress_initiation**: 7
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:03:34.248) | **Initiation**: Pressure (00:03:36.952)
- **Initiation Delay**: 2.704s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.827s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.86 |  -5.56 | 00:03:31.388 | Paris Saint-Germai | Paris Saint-Germai | 6 | Pass            |   -   | [43.6, 58.1]    | Incomplete (Incomplete) |
|  +0.00 |  -2.70 | 00:03:34.248 | Paris Saint-Germai | Paris Saint-Germai | 6 | Ball Receipt*   |   -   | [96.0, 37.9]    | Incomplete |
|  +0.00 |  -2.70 | 00:03:34.248 | OGC Nice           | OGC Nice           | 7 | Pass            |  Yes  | [27.2, 34.8]    | -> Dante Bonfim d |
|  +1.22 |  -1.49 | 00:03:35.465 | OGC Nice           | OGC Nice           | 7 | Ball Receipt*   |   -   | [31.3, 26.6]    |  |
|  +1.40 |  -1.31 | 00:03:35.644 | OGC Nice           | OGC Nice           | 7 | Pass            |   -   | [31.3, 25.7]    | -> Khéphren Thura |
|  +2.70 |  +0.00 | 00:03:36.952 | Paris Saint-Germai | OGC Nice           | 7 | Pressure        |  Yes  | [74.1, 55.9]    |  |
|  +2.76 |  +0.06 | 00:03:37.010 | OGC Nice           | OGC Nice           | 7 | Ball Receipt*   |   -   | [42.5, 24.2]    |  |
|  +2.76 |  +0.06 | 00:03:37.010 | OGC Nice           | OGC Nice           | 7 | Carry           |   -   | [42.5, 24.2]    |  |
|  +4.88 |  +2.18 | 00:03:39.129 | OGC Nice           | OGC Nice           | 7 | Pass            |   -   | [39.7, 34.1]    | Incomplete (Incomplete) |
|  +7.53 |  +4.83 | 00:03:41.779 | OGC Nice           | OGC Nice           | 7 | Ball Receipt*   |   -   | [74.4, 60.4]    | Incomplete |
|  +7.53 |  +4.83 | 00:03:41.779 | Paris Saint-Germai | Paris Saint-Germai | 8 | Ball Recovery   |   -   | [49.0, 18.9]    |  |
|  +7.53 |  +4.83 | 00:03:41.779 | Paris Saint-Germai | Paris Saint-Germai | 8 | Carry           |   -   | [49.0, 18.9]    |  |
|  +8.71 |  +6.01 | 00:03:42.958 | OGC Nice           | Paris Saint-Germai | 8 | Pressure        |  Yes  | [72.4, 48.2]    |  |
|  +9.19 |  +6.49 | 00:03:43.443 | Paris Saint-Germai | Paris Saint-Germai | 8 | Pass            |   -   | [47.2, 30.8]    | -> Sergio Ramos G |
| +10.15 |  +7.45 | 00:03:44.398 | Paris Saint-Germai | Paris Saint-Germai | 8 | Ball Receipt*   |   -   | [41.8, 41.0]    |  |
| +10.15 |  +7.45 | 00:03:44.398 | Paris Saint-Germai | Paris Saint-Germai | 8 | Carry           |   -   | [41.8, 41.0]    |  |
| +11.54 |  +8.83 | 00:03:45.783 | Paris Saint-Germai | Paris Saint-Germai | 8 | Pass            |   -   | [41.4, 41.8]    | -> Achraf Hakimi  |
| +13.17 | +10.46 | 00:03:47.414 | OGC Nice           | Paris Saint-Germai | 8 | Pressure        |   -   | [57.5, 10.7]    |  |

---

### Priority Case 8: `3802665_p95_879d7810` [ordinary_successful_regain]
- **Match**: 3802665 (Ligue 1)
- **counterpressing_team**: Montpellier
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Montpellier
- **possession_id_at_counterpress_initiation**: 95
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:45:12.088) | **Initiation**: Duel (00:45:12.487)
- **Initiation Delay**: 0.399s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 1.348s) | Evidence: `completed_pass` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.48 |  -0.88 | 00:45:11.609 | Paris Saint-Germai | Paris Saint-Germai | 94 | Pass            |   -   | [29.5, 2.0]     | -> Sergio Ramos G |
|  -0.26 |  -0.66 | 00:45:11.831 | Montpellier        | Paris Saint-Germai | 94 | Pressure        |   -   | [82.2, 76.4]    |  |
|  +0.00 |  -0.40 | 00:45:12.088 | Paris Saint-Germai | Paris Saint-Germai | 94 | Ball Receipt*   |   -   | [35.8, 3.7]     |  |
|  +0.00 |  -0.40 | 00:45:12.088 | Paris Saint-Germai | Paris Saint-Germai | 94 | Carry           |   -   | [35.8, 3.7]     |  |
|  +0.40 |  +0.00 | 00:45:12.487 | Paris Saint-Germai | Paris Saint-Germai | 94 | Dispossessed    |   -   | [34.9, 5.5]     |  |
|  +0.40 |  +0.00 | 00:45:12.487 | Montpellier        | Montpellier        | 95 | Duel            |  Yes  | [85.2, 74.6]    | Tackle, Success In Play |
|  +1.75 |  +1.35 | 00:45:13.835 | Montpellier        | Montpellier        | 95 | Pass            |   -   | [79.3, 74.4]    | -> Joris Chotard |
|  +2.44 |  +2.04 | 00:45:14.531 | Montpellier        | Montpellier        | 95 | Ball Receipt*   |   -   | [87.0, 75.6]    |  |
|  +2.44 |  +2.04 | 00:45:14.531 | Montpellier        | Montpellier        | 95 | Carry           |   -   | [87.0, 75.6]    |  |
|  +2.61 |  +2.22 | 00:45:14.703 | Montpellier        | Montpellier        | 95 | Pass            |   -   | [87.0, 75.6]    | -> Sacha Delaye |
|  +3.11 |  +2.72 | 00:45:15.203 | Montpellier        | Montpellier        | 95 | Ball Receipt*   |   -   | [86.4, 69.6]    |  |
|  +3.11 |  +2.72 | 00:45:15.203 | Montpellier        | Montpellier        | 95 | Carry           |   -   | [86.4, 69.6]    |  |
|  +3.54 |  +3.14 | 00:45:15.624 | Montpellier        | Montpellier        | 95 | Pass            |   -   | [86.4, 69.6]    | Incomplete (Incomplete) |
|  +5.67 |  +5.28 | 00:45:17.763 | Montpellier        | Montpellier        | 95 | Ball Receipt*   |   -   | [90.8, 74.6]    | Incomplete |
|  +5.67 |  +5.28 | 00:45:17.763 | Paris Saint-Germai | Montpellier        | 95 | Ball Recovery   |   -   | [22.6, 10.7]    |  |
|  +5.67 |  +5.28 | 00:45:17.763 | Paris Saint-Germai | Montpellier        | 95 | Carry           |   -   | [22.6, 10.7]    |  |
|  +6.15 |  +5.75 | 00:45:18.236 | Montpellier        | Montpellier        | 95 | Pressure        |  Yes  | [98.5, 65.4]    |  |
|  +9.37 |  +8.97 | 00:45:21.454 | Paris Saint-Germai | Montpellier        | 95 | Pass            |   -   | [14.3, 21.2]    | -> Ander Herrera  |
| +10.31 |  +9.91 | 00:45:22.401 | Paris Saint-Germai | Montpellier        | 95 | Ball Receipt*   |   -   | [22.9, 19.9]    |  |

---

### Priority Case 9: `3788766_p107_15ad5bb1` [ordinary_successful_regain]
- **Match**: 3788766 (UEFA Euro)
- **counterpressing_team**: Italy
- **opponent_team_at_turnover**: Wales
- **possession_team_at_counterpress_initiation**: Italy
- **possession_id_at_counterpress_initiation**: 107
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:08:10.036) | **Initiation**: Pressure (00:08:10.996)
- **Initiation Delay**: 0.96s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `0` (time: 7.33s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.06 |  -3.01 | 00:08:07.981 | Italy              | Italy              | 107 | Ball Receipt*   |   -   | [62.2, 27.2]    |  |
|  -2.06 |  -3.01 | 00:08:07.981 | Italy              | Italy              | 107 | Carry           |   -   | [62.2, 27.2]    |  |
|  -2.02 |  -2.98 | 00:08:08.018 | Italy              | Italy              | 107 | Miscontrol      |   -   | [61.8, 26.8]    |  |
|  +0.00 |  -0.96 | 00:08:10.036 | Wales              | Italy              | 107 | Ball Recovery   |   -   | [63.0, 76.1]    |  |
|  +0.00 |  -0.96 | 00:08:10.036 | Wales              | Italy              | 107 | Carry           |   -   | [63.0, 76.1]    |  |
|  +0.96 |  +0.00 | 00:08:10.996 | Italy              | Italy              | 107 | Pressure        |  Yes  | [56.1, 8.0]     |  |
|  +1.21 |  +0.25 | 00:08:11.246 | Wales              | Italy              | 107 | Pass            |   -   | [63.7, 76.1]    | -> Aaron Ramsey |
|  +6.06 |  +5.10 | 00:08:16.091 | Wales              | Italy              | 107 | Ball Receipt*   |   -   | [116.6, 52.1]   |  |
|  +6.06 |  +5.10 | 00:08:16.091 | Wales              | Italy              | 107 | Carry           |   -   | [116.6, 52.1]   |  |
|  +7.89 |  +6.93 | 00:08:17.929 | Wales              | Italy              | 107 | Pass            |   -   | [116.3, 51.4]   | Incomplete (Incomplete) |
|  +8.29 |  +7.33 | 00:08:18.326 | Wales              | Italy              | 107 | Ball Receipt*   |   -   | [109.3, 41.2]   | Incomplete |
|  +8.29 |  +7.33 | 00:08:18.326 | Italy              | Italy              | 107 | Ball Recovery   |   -   | [7.7, 32.7]     |  |
|  +8.29 |  +7.33 | 00:08:18.326 | Italy              | Italy              | 107 | Carry           |   -   | [7.7, 32.7]     |  |
| +10.01 |  +9.05 | 00:08:20.050 | Wales              | Italy              | 107 | Pressure        |   -   | [115.7, 63.9]   |  |
| +11.75 | +10.79 | 00:08:21.781 | Wales              | Italy              | 107 | Dribbled Past   |   -   | [116.6, 63.8]   |  |
| +11.75 | +10.79 | 00:08:21.781 | Italy              | Italy              | 107 | Dribble         |   -   | [3.5, 16.3]     |  |
| +11.75 | +10.79 | 00:08:21.781 | Italy              | Italy              | 107 | Carry           |   -   | [3.5, 16.3]     |  |

---

### Priority Case 10: `3893795_p122_8d11ca97` [ordinary_successful_regain]
- **Match**: 3893795 (Women's World Cup)
- **counterpressing_team**: Denmark Women's
- **opponent_team_at_turnover**: China PR Women's
- **possession_team_at_counterpress_initiation**: Denmark Women's
- **possession_id_at_counterpress_initiation**: 122
- **Turnover Context**: immediate_restart_phase (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:11:32.017) | **Initiation**: Pressure (00:11:38.881)
- **Initiation Delay**: 6.864s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.864s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.19 |  -9.05 | 00:11:29.830 | Denmark Women's    | Denmark Women's    | 122 | Pass            |   -   | [105.7, 80.0]   | Incomplete (Incomplete) |
|  +0.00 |  -6.86 | 00:11:32.017 | Denmark Women's    | Denmark Women's    | 122 | Ball Receipt*   |   -   | [109.7, 54.8]   | Incomplete |
|  +0.00 |  -6.86 | 00:11:32.017 | China PR Women's   | Denmark Women's    | 122 | Ball Recovery   |   -   | [9.0, 32.1]     |  |
|  +2.23 |  -4.63 | 00:11:34.249 | China PR Women's   | Denmark Women's    | 122 | Ball Recovery   |   -   | [19.5, 41.2]    |  |
|  +2.23 |  -4.63 | 00:11:34.249 | China PR Women's   | Denmark Women's    | 122 | Carry           |   -   | [19.5, 41.2]    |  |
|  +6.86 |  +0.00 | 00:11:38.881 | Denmark Women's    | Denmark Women's    | 122 | Pressure        |  Yes  | [75.8, 14.5]    |  |
|  +8.33 |  +1.46 | 00:11:40.343 | China PR Women's   | Denmark Women's    | 122 | Pass            |   -   | [55.9, 72.7]    | Incomplete (Incomplete) |
| +10.73 |  +3.86 | 00:11:42.745 | China PR Women's   | Denmark Women's    | 122 | Ball Receipt*   |   -   | [78.1, 68.5]    | Incomplete |
| +10.73 |  +3.86 | 00:11:42.745 | Denmark Women's    | Denmark Women's    | 122 | Ball Recovery   |   -   | [45.1, 8.8]     |  |
| +10.73 |  +3.86 | 00:11:42.745 | Denmark Women's    | Denmark Women's    | 122 | Carry           |   -   | [45.1, 8.8]     |  |
| +10.89 |  +4.02 | 00:11:42.905 | China PR Women's   | Denmark Women's    | 122 | Dribbled Past   |   -   | [75.2, 70.2]    |  |
| +10.89 |  +4.02 | 00:11:42.905 | Denmark Women's    | Denmark Women's    | 122 | Dribble         |   -   | [44.9, 9.9]     |  |
| +10.89 |  +4.02 | 00:11:42.905 | Denmark Women's    | Denmark Women's    | 122 | Carry           |   -   | [44.9, 9.9]     |  |
| +12.47 |  +5.61 | 00:11:44.487 | Denmark Women's    | Denmark Women's    | 122 | Pass            |   -   | [37.8, 16.8]    | -> Katrine Veje |
| +13.82 |  +6.96 | 00:11:45.836 | Denmark Women's    | Denmark Women's    | 122 | Ball Receipt*   |   -   | [25.0, 15.0]    |  |
| +13.82 |  +6.96 | 00:11:45.836 | Denmark Women's    | Denmark Women's    | 122 | Carry           |   -   | [25.0, 15.0]    |  |
| +14.67 |  +7.81 | 00:11:46.691 | Denmark Women's    | Denmark Women's    | 122 | Pass            |   -   | [25.0, 15.4]    | -> Simone Boye-Sø |
| +16.51 |  +9.64 | 00:11:48.524 | Denmark Women's    | Denmark Women's    | 122 | Ball Receipt*   |   -   | [20.4, 32.4]    |  |
| +16.51 |  +9.64 | 00:11:48.524 | Denmark Women's    | Denmark Women's    | 122 | Carry           |   -   | [20.4, 32.4]    |  |

---

### Priority Case 11: `3837662_p13_fa9edc11` [ordinary_unsuccessful_regain]
- **Match**: 3837662 (Ligue 1)
- **counterpressing_team**: Lille
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 13
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:05:06.508) | **Initiation**: Pressure (00:05:07.379)
- **Initiation Delay**: 0.871s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.63 |  -2.50 | 00:05:04.876 | Paris Saint-Germai | Paris Saint-Germai | 12 | Carry           |   -   | [19.2, 50.9]    |  |
|  -0.79 |  -1.66 | 00:05:05.720 | Lille              | Paris Saint-Germai | 12 | Pressure        |  Yes  | [93.2, 27.5]    |  |
|  +0.00 |  -0.87 | 00:05:06.508 | Paris Saint-Germai | Paris Saint-Germai | 13 | Pass            |   -   | [27.5, 53.0]    | -> Vitor Machado  |
|  +0.40 |  -0.47 | 00:05:06.908 | Paris Saint-Germai | Paris Saint-Germai | 13 | Ball Receipt*   |   -   | [42.2, 51.3]    |  |
|  +0.40 |  -0.47 | 00:05:06.908 | Paris Saint-Germai | Paris Saint-Germai | 13 | Carry           |   -   | [42.2, 51.3]    |  |
|  +0.87 |  +0.00 | 00:05:07.379 | Lille              | Paris Saint-Germai | 13 | Pressure        |  Yes  | [77.5, 29.2]    |  |
|  +1.72 |  +0.84 | 00:05:08.224 | Paris Saint-Germai | Paris Saint-Germai | 14 | Pass            |   -   | [37.8, 51.3]    | -> Marcos Aoás Co |
|  +2.45 |  +1.58 | 00:05:08.956 | Paris Saint-Germai | Paris Saint-Germai | 14 | Ball Receipt*   |   -   | [30.7, 56.4]    |  |
|  +2.45 |  +1.58 | 00:05:08.956 | Paris Saint-Germai | Paris Saint-Germai | 14 | Carry           |   -   | [30.7, 56.4]    |  |
|  +5.07 |  +4.19 | 00:05:11.574 | Paris Saint-Germai | Paris Saint-Germai | 15 | Pass            |   -   | [30.7, 56.4]    | -> Sergio Ramos G |
|  +6.31 |  +5.44 | 00:05:12.820 | Paris Saint-Germai | Paris Saint-Germai | 15 | Ball Receipt*   |   -   | [23.8, 69.7]    |  |
|  +6.31 |  +5.44 | 00:05:12.820 | Paris Saint-Germai | Paris Saint-Germai | 15 | Carry           |   -   | [23.8, 69.7]    |  |
|  +7.07 |  +6.20 | 00:05:13.577 | Paris Saint-Germai | Paris Saint-Germai | 16 | Pass            |   -   | [23.8, 69.7]    | -> Vitor Machado  |
|  +7.93 |  +7.05 | 00:05:14.433 | Paris Saint-Germai | Paris Saint-Germai | 16 | Ball Receipt*   |   -   | [36.7, 63.2]    |  |
|  +7.93 |  +7.05 | 00:05:14.433 | Paris Saint-Germai | Paris Saint-Germai | 16 | Carry           |   -   | [36.7, 63.2]    |  |
| +10.89 | +10.02 | 00:05:17.397 | Paris Saint-Germai | Paris Saint-Germai | 17 | Pass            |   -   | [49.6, 61.5]    | -> Kylian Mbappé  |
| +11.62 | +10.75 | 00:05:18.124 | Paris Saint-Germai | Paris Saint-Germai | 17 | Ball Receipt*   |   -   | [59.9, 62.3]    |  |

---

### Priority Case 12: `3998840_p8_887bac36` [ordinary_unsuccessful_regain]
- **Match**: 3998840 (UEFA Women's Euro)
- **counterpressing_team**: Poland Women's
- **opponent_team_at_turnover**: Germany Women's
- **possession_team_at_counterpress_initiation**: Germany Women's
- **possession_id_at_counterpress_initiation**: 8
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:03:25.853) | **Initiation**: Pressure (00:03:28.464)
- **Initiation Delay**: 2.611s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -7.82 | -10.43 | 00:03:18.031 | Poland Women's     | Poland Women's     | 7 | Carry           |   -   | [19.6, 31.2]    |  |
|  -3.01 |  -5.62 | 00:03:22.845 | Poland Women's     | Poland Women's     | 7 | Pass            |   -   | [37.7, 31.8]    | Incomplete (Incomplete) |
|  +0.00 |  -2.61 | 00:03:25.853 | Germany Women's    | Germany Women's    | 8 | Pass            |   -   | [41.1, 8.0]     | -> Klara Bühl |
|  +1.36 |  -1.25 | 00:03:27.211 | Germany Women's    | Germany Women's    | 8 | Ball Receipt*   |   -   | [50.2, 11.7]    |  |
|  +1.36 |  -1.25 | 00:03:27.211 | Germany Women's    | Germany Women's    | 8 | Pass            |   -   | [50.4, 12.1]    | -> Sjoeke Nüsken |
|  +2.06 |  -0.55 | 00:03:27.914 | Germany Women's    | Germany Women's    | 8 | Ball Receipt*   |   -   | [43.3, 23.5]    |  |
|  +2.06 |  -0.55 | 00:03:27.914 | Germany Women's    | Germany Women's    | 8 | Carry           |   -   | [43.3, 23.5]    |  |
|  +2.61 |  +0.00 | 00:03:28.464 | Poland Women's     | Germany Women's    | 8 | Pressure        |  Yes  | [76.1, 58.5]    |  |
|  +4.76 |  +2.15 | 00:03:30.617 | Germany Women's    | Germany Women's    | 8 | Pass            |   -   | [42.6, 30.1]    | Incomplete (Out) |
|  +8.77 |  +6.16 | 00:03:34.619 | Germany Women's    | Germany Women's    | 8 | Ball Receipt*   |   -   | [76.8, 14.8]    | Incomplete |
| +30.34 | +27.73 | 00:03:56.195 | Poland Women's     | Poland Women's     | 9 | Pass            |   -   | [37.3, 80.0]    | Incomplete (Incomplete) |
| +32.33 | +29.72 | 00:03:58.180 | Germany Women's    | Poland Women's     | 9 | Clearance       |   -   | [62.7, 2.9]     |  |
| +32.85 | +30.24 | 00:03:58.707 | Poland Women's     | Poland Women's     | 9 | Pressure        |   -   | [58.1, 77.2]    |  |
| +33.15 | +30.54 | 00:03:59.007 | Germany Women's    | Poland Women's     | 9 | Pass            |   -   | [61.9, 1.9]     | Incomplete (Incomplete) |
| +35.36 | +32.75 | 00:04:01.211 | Poland Women's     | Poland Women's     | 9 | Pass            |   -   | [41.8, 76.1]    | Incomplete (Incomplete) |
| +36.90 | +34.29 | 00:04:02.757 | Germany Women's    | Germany Women's    | 10 | Pass            |   -   | [57.4, 3.1]     | -> Lea Schüller |
| +38.99 | +36.38 | 00:04:04.839 | Germany Women's    | Germany Women's    | 10 | Ball Receipt*   |   -   | [81.1, 11.9]    |  |
| +38.99 | +36.38 | 00:04:04.839 | Germany Women's    | Germany Women's    | 10 | Pass            |   -   | [81.1, 11.9]    | Incomplete (Incomplete) |
| +39.14 | +36.53 | 00:04:04.997 | Poland Women's     | Germany Women's    | 10 | Block           |  Yes  | [37.5, 69.9]    |  |

---

### Priority Case 13: `3998838_p98_25bcc2e1` [ordinary_unsuccessful_regain]
- **Match**: 3998838 (UEFA Women's Euro)
- **counterpressing_team**: Belgium Women's
- **opponent_team_at_turnover**: Italy Women's
- **possession_team_at_counterpress_initiation**: Italy Women's
- **possession_id_at_counterpress_initiation**: 98
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Block (00:02:42.241) | **Initiation**: Pressure (00:02:48.406)
- **Initiation Delay**: 6.165s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.12 |  -6.28 | 00:02:42.121 | Belgium Women's    | Belgium Women's    | 97 | Carry           |   -   | [119.4, 72.7]   |  |
|  -0.07 |  -6.23 | 00:02:42.176 | Belgium Women's    | Belgium Women's    | 97 | Pass            |   -   | [119.4, 72.7]   | Incomplete (Incomplete) |
|  -0.00 |  -6.17 | 00:02:42.241 | Italy Women's      | Belgium Women's    | 97 | Block           |   -   | [1.3, 9.1]      |  |
|  +1.71 |  -4.46 | 00:02:43.947 | Italy Women's      | Italy Women's      | 98 | Pass            |   -   | [11.0, 31.5]    | -> Lisa Boattin |
|  +2.95 |  -3.22 | 00:02:45.190 | Italy Women's      | Italy Women's      | 98 | Ball Receipt*   |   -   | [9.0, 19.9]     |  |
|  +2.95 |  -3.22 | 00:02:45.190 | Italy Women's      | Italy Women's      | 98 | Carry           |   -   | [9.0, 19.9]     |  |
|  +6.16 |  +0.00 | 00:02:48.406 | Belgium Women's    | Italy Women's      | 98 | Pressure        |  Yes  | [103.2, 71.2]   |  |
|  +6.94 |  +0.78 | 00:02:49.182 | Italy Women's      | Italy Women's      | 98 | Pass            |   -   | [19.8, 8.0]     | -> Emma Severini |
|  +8.14 |  +1.97 | 00:02:50.379 | Italy Women's      | Italy Women's      | 98 | Ball Receipt*   |   -   | [29.0, 16.0]    |  |
|  +8.14 |  +1.97 | 00:02:50.379 | Italy Women's      | Italy Women's      | 98 | Carry           |   -   | [29.0, 16.0]    |  |
| +13.96 |  +7.79 | 00:02:56.197 | Italy Women's      | Italy Women's      | 98 | Pass            |   -   | [58.5, 22.1]    | -> Sofia Cantore |
| +15.30 |  +9.14 | 00:02:57.544 | Italy Women's      | Italy Women's      | 98 | Ball Receipt*   |   -   | [75.5, 4.0]     |  |
| +15.30 |  +9.14 | 00:02:57.544 | Italy Women's      | Italy Women's      | 98 | Carry           |   -   | [75.5, 4.0]     |  |
| +17.32 | +11.15 | 00:02:59.559 | Belgium Women's    | Italy Women's      | 98 | Pressure        |   -   | [40.7, 76.1]    |  |
| +18.33 | +12.17 | 00:03:00.576 | Italy Women's      | Italy Women's      | 98 | Pass            |   -   | [75.3, 4.2]     | -> Manuela Giugli |
| +19.47 | +13.31 | 00:03:01.714 | Italy Women's      | Italy Women's      | 98 | Ball Receipt*   |   -   | [68.5, 21.4]    |  |
| +19.47 | +13.31 | 00:03:01.714 | Italy Women's      | Italy Women's      | 98 | Carry           |   -   | [68.5, 21.4]    |  |
| +21.20 | +15.03 | 00:03:03.440 | Italy Women's      | Italy Women's      | 98 | Pass            |   -   | [74.2, 23.6]    | -> Lucia Di Gugli |

---

### Priority Case 14: `3788754_p120_f8d30c17` [ordinary_unsuccessful_regain]
- **Match**: 3788754 (UEFA Euro)
- **counterpressing_team**: Switzerland
- **opponent_team_at_turnover**: Italy
- **possession_team_at_counterpress_initiation**: Italy
- **possession_id_at_counterpress_initiation**: 120
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:18:58.351) | **Initiation**: Pressure (00:18:59.411)
- **Initiation Delay**: 1.06s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.64 |  -3.70 | 00:18:55.714 | Italy              | Switzerland        | 119 | Pressure        |   -   | [30.6, 50.2]    |  |
|  -1.96 |  -3.02 | 00:18:56.391 | Switzerland        | Switzerland        | 119 | Pass            |   -   | [91.0, 26.5]    | Incomplete (Incomplete) |
|  +0.00 |  -1.06 | 00:18:58.351 | Switzerland        | Switzerland        | 119 | Ball Receipt*   |   -   | [111.6, 32.8]   | Incomplete |
|  +0.00 |  -1.06 | 00:18:58.351 | Italy              | Italy              | 120 | Ball Recovery   |   -   | [1.4, 46.8]     |  |
|  +0.00 |  -1.06 | 00:18:58.351 | Italy              | Italy              | 120 | Carry           |   -   | [1.4, 46.8]     |  |
|  +1.06 |  +0.00 | 00:18:59.411 | Switzerland        | Italy              | 120 | Pressure        |  Yes  | [111.6, 29.9]   |  |
| +13.15 | +12.09 | 00:19:11.505 | Italy              | Italy              | 120 | Pass            |   -   | [8.5, 49.0]     | -> Jorge Luiz Fre |
| +14.87 | +13.81 | 00:19:13.220 | Italy              | Italy              | 120 | Ball Receipt*   |   -   | [24.0, 33.1]    |  |
| +16.74 | +15.68 | 00:19:15.096 | Italy              | Italy              | 120 | Pass            |   -   | [14.9, 30.9]    | -> Gianluigi Donn |
| +20.17 | +19.12 | 00:19:18.526 | Italy              | Italy              | 120 | Ball Receipt*   |   -   | [3.0, 37.3]     |  |
| +20.74 | +19.68 | 00:19:19.088 | Switzerland        | Italy              | 120 | Pressure        |   -   | [110.9, 45.3]   |  |
| +21.37 | +20.31 | 00:19:19.724 | Italy              | Italy              | 120 | Pass            |   -   | [7.1, 41.5]     | -> Jorge Luiz Fre |
| +23.93 | +22.87 | 00:19:22.277 | Italy              | Italy              | 120 | Ball Receipt*   |   -   | [31.7, 23.5]    |  |
| +23.93 | +22.87 | 00:19:22.277 | Italy              | Italy              | 120 | Carry           |   -   | [31.7, 23.5]    |  |
| +24.82 | +23.76 | 00:19:23.170 | Italy              | Italy              | 120 | Pass            |   -   | [38.2, 26.3]    | -> Manuel Locatel |
| +26.24 | +25.18 | 00:19:24.590 | Italy              | Italy              | 120 | Ball Receipt*   |   -   | [55.4, 35.2]    |  |
| +26.24 | +25.18 | 00:19:24.590 | Italy              | Italy              | 120 | Carry           |   -   | [55.4, 35.2]    |  |

---

### Priority Case 15: `3837896_p87_6d38cf89` [ordinary_unsuccessful_regain]
- **Match**: 3837896 (Ligue 1)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Nantes
- **possession_team_at_counterpress_initiation**: Nantes
- **possession_id_at_counterpress_initiation**: 87
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Block (00:05:18.423) | **Initiation**: Pressure (00:05:19.948)
- **Initiation Delay**: 1.525s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.41 |  -1.93 | 00:05:18.014 | Paris Saint-Germai | Paris Saint-Germai | 86 | Pass            |   -   | [88.0, 52.2]    | Incomplete (Incomplete) |
|  +0.00 |  -1.52 | 00:05:18.423 | Paris Saint-Germai | Paris Saint-Germai | 86 | Ball Receipt*   |   -   | [97.8, 38.5]    | Incomplete |
|  +0.00 |  -1.52 | 00:05:18.423 | Nantes             | Paris Saint-Germai | 86 | Block           |   -   | [29.0, 30.6]    |  |
|  +0.78 |  -0.74 | 00:05:19.207 | Nantes             | Nantes             | 87 | Ball Recovery   |   -   | [25.6, 45.0]    |  |
|  +0.78 |  -0.74 | 00:05:19.207 | Nantes             | Nantes             | 87 | Carry           |   -   | [25.6, 45.0]    |  |
|  +1.34 |  -0.19 | 00:05:19.761 | Nantes             | Nantes             | 87 | Pass            |   -   | [27.0, 46.7]    | -> Ignatius Kpene |
|  +1.52 |  +0.00 | 00:05:19.948 | Paris Saint-Germai | Nantes             | 87 | Pressure        |  Yes  | [88.0, 27.3]    |  |
|  +4.96 |  +3.44 | 00:05:23.384 | Nantes             | Nantes             | 87 | Ball Receipt*   |   -   | [38.7, 71.0]    |  |
|  +4.96 |  +3.44 | 00:05:23.384 | Nantes             | Nantes             | 87 | Carry           |   -   | [38.7, 71.0]    |  |
|  +5.79 |  +4.27 | 00:05:24.216 | Paris Saint-Germai | Nantes             | 87 | Pressure        |   -   | [72.8, 9.1]     |  |
|  +5.94 |  +4.42 | 00:05:24.368 | Nantes             | Nantes             | 87 | Pass            |   -   | [47.7, 75.3]    | -> Florent Mollet |
|  +6.69 |  +5.16 | 00:05:25.108 | Paris Saint-Germai | Nantes             | 87 | Pressure        |   -   | [66.9, 14.2]    |  |
|  +7.21 |  +5.69 | 00:05:25.636 | Nantes             | Nantes             | 87 | Ball Receipt*   |   -   | [51.8, 63.5]    |  |
|  +7.21 |  +5.69 | 00:05:25.636 | Nantes             | Nantes             | 87 | Carry           |   -   | [51.8, 63.5]    |  |
|  +8.41 |  +6.88 | 00:05:26.831 | Nantes             | Nantes             | 87 | Pass            |   -   | [50.6, 63.5]    | -> Fabien Centonz |
|  +9.34 |  +7.81 | 00:05:27.760 | Nantes             | Nantes             | 87 | Ball Receipt*   |   -   | [40.0, 64.8]    |  |
|  +9.34 |  +7.81 | 00:05:27.760 | Nantes             | Nantes             | 87 | Carry           |   -   | [40.0, 64.8]    |  |
|  +9.49 |  +7.97 | 00:05:27.914 | Nantes             | Nantes             | 87 | Pass            |   -   | [40.0, 64.8]    | -> Moussa Sissoko |
| +10.43 |  +8.90 | 00:05:28.849 | Nantes             | Nantes             | 87 | Ball Receipt*   |   -   | [39.6, 74.9]    |  |
| +10.43 |  +8.90 | 00:05:28.849 | Nantes             | Nantes             | 87 | Carry           |   -   | [39.6, 74.9]    |  |

---

### Priority Case 16: `3893801_p46_531f18b3` [ordinary_unsuccessful_regain]
- **Match**: 3893801 (Women's World Cup)
- **counterpressing_team**: Brazil Women's
- **opponent_team_at_turnover**: Panama Women's
- **possession_team_at_counterpress_initiation**: Panama Women's
- **possession_id_at_counterpress_initiation**: 46
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:24:15.178) | **Initiation**: Pressure (00:24:15.778)
- **Initiation Delay**: 0.6s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.953s) | Evidence: `new_possession_completed_pass` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.18 |  -1.78 | 00:24:14.000 | Brazil Women's     | Brazil Women's     | 45 | Carry           |   -   | [104.9, 73.1]   |  |
|  -0.80 |  -1.40 | 00:24:14.375 | Panama Women's     | Brazil Women's     | 45 | Pressure        |   -   | [15.0, 8.1]     |  |
|  +0.00 |  -0.60 | 00:24:15.178 | Brazil Women's     | Brazil Women's     | 45 | Dribble         |   -   | [104.7, 71.6]   |  |
|  +0.00 |  -0.60 | 00:24:15.178 | Panama Women's     | Panama Women's     | 46 | Duel            |  Yes  | [15.4, 8.5]     | Tackle, Won |
|  +0.00 |  -0.60 | 00:24:15.178 | Panama Women's     | Panama Women's     | 46 | Carry           |   -   | [15.4, 8.5]     |  |
|  +0.60 |  +0.00 | 00:24:15.778 | Brazil Women's     | Panama Women's     | 46 | Pressure        |  Yes  | [104.9, 71.6]   |  |
|  +3.69 |  +3.09 | 00:24:18.872 | Panama Women's     | Panama Women's     | 46 | Pass            |   -   | [10.7, 7.2]     | -> Schiandra Yael |
|  +4.96 |  +4.36 | 00:24:20.134 | Panama Women's     | Panama Women's     | 46 | Ball Receipt*   |   -   | [15.7, 15.8]    |  |
|  +4.96 |  +4.36 | 00:24:20.134 | Panama Women's     | Panama Women's     | 46 | Pass            |   -   | [15.7, 13.6]    | -> Marta Alexandr |
|  +6.29 |  +5.69 | 00:24:21.470 | Panama Women's     | Panama Women's     | 46 | Ball Receipt*   |   -   | [24.6, 5.5]     |  |
|  +6.29 |  +5.69 | 00:24:21.470 | Panama Women's     | Panama Women's     | 46 | Carry           |   -   | [24.6, 5.5]     |  |
|  +6.61 |  +6.01 | 00:24:21.785 | Panama Women's     | Panama Women's     | 46 | Pass            |   -   | [25.1, 6.8]     | Incomplete (Incomplete) |
|  +7.55 |  +6.95 | 00:24:22.731 | Panama Women's     | Panama Women's     | 46 | Ball Receipt*   |   -   | [35.3, 15.1]    | Incomplete |
|  +7.55 |  +6.95 | 00:24:22.731 | Brazil Women's     | Brazil Women's     | 47 | Pass            |   -   | [85.8, 64.1]    | -> Antonia Ronnyc |
|  +8.85 |  +8.25 | 00:24:24.029 | Brazil Women's     | Brazil Women's     | 47 | Ball Receipt*   |   -   | [86.7, 69.7]    |  |
|  +8.85 |  +8.25 | 00:24:24.029 | Brazil Women's     | Brazil Women's     | 47 | Carry           |   -   | [86.7, 69.7]    |  |
|  +8.90 |  +8.30 | 00:24:24.076 | Brazil Women's     | Brazil Women's     | 47 | Pass            |   -   | [86.7, 68.2]    | -> Luana Bertoluc |
| +10.05 |  +9.45 | 00:24:25.231 | Brazil Women's     | Brazil Women's     | 47 | Ball Receipt*   |   -   | [86.3, 60.3]    |  |
| +10.05 |  +9.45 | 00:24:25.231 | Brazil Women's     | Brazil Women's     | 47 | Carry           |   -   | [86.3, 60.3]    |  |

---

### Priority Case 17: `3788741_p35_447ab819` [ordinary_unsuccessful_regain]
- **Match**: 3788741 (UEFA Euro)
- **counterpressing_team**: Italy
- **opponent_team_at_turnover**: Turkey
- **possession_team_at_counterpress_initiation**: Turkey
- **possession_id_at_counterpress_initiation**: 35
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:14:33.536) | **Initiation**: Foul Committed (00:14:33.831)
- **Initiation Delay**: 0.295s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.64 |  -0.94 | 00:14:32.895 | Italy              | Italy              | 34 | Carry           |   -   | [97.1, 10.1]    |  |
|  -0.48 |  -0.77 | 00:14:33.059 | Turkey             | Italy              | 34 | Pressure        |   -   | [27.5, 68.9]    |  |
|  +0.00 |  -0.29 | 00:14:33.536 | Italy              | Italy              | 34 | Dispossessed    |   -   | [95.7, 14.6]    |  |
|  +0.00 |  -0.29 | 00:14:33.536 | Turkey             | Turkey             | 35 | Duel            |  Yes  | [24.4, 65.5]    | Tackle, Won |
|  +0.00 |  -0.29 | 00:14:33.536 | Turkey             | Turkey             | 35 | Carry           |   -   | [24.4, 65.5]    |  |
|  +0.29 |  +0.00 | 00:14:33.831 | Italy              | Turkey             | 35 | Foul Committed  |  Yes  | [95.7, 13.9]    |  |
|  +0.29 |  +0.00 | 00:14:33.831 | Turkey             | Turkey             | 35 | Foul Won        |   -   | [24.4, 66.2]    |  |
| +40.92 | +40.63 | 00:15:14.458 | Turkey             | Turkey             | 36 | Pass            |   -   | [26.6, 61.7]    | Incomplete (Incomplete) |
| +44.91 | +44.62 | 00:15:18.448 | Turkey             | Turkey             | 36 | Ball Receipt*   |   -   | [90.1, 75.1]    | Incomplete |
| +44.91 | +44.62 | 00:15:18.448 | Turkey             | Turkey             | 36 | Duel            |   -   | [91.8, 74.9]    | Aerial Lost |
| +44.91 | +44.62 | 00:15:18.448 | Italy              | Turkey             | 36 | Clearance       |   -   | [28.3, 5.2]     |  |
| +46.02 | +45.72 | 00:15:19.553 | Italy              | Turkey             | 36 | Pressure        |   -   | [34.1, 20.4]    |  |
| +46.21 | +45.92 | 00:15:19.747 | Turkey             | Turkey             | 36 | Pass            |   -   | [84.6, 56.6]    | -> Ozan Tufan |
| +47.09 | +46.79 | 00:15:20.626 | Turkey             | Turkey             | 36 | Ball Receipt*   |   -   | [81.2, 65.5]    |  |
| +47.09 | +46.79 | 00:15:20.626 | Turkey             | Turkey             | 36 | Carry           |   -   | [81.2, 65.5]    |  |
| +47.45 | +47.15 | 00:15:20.984 | Italy              | Turkey             | 36 | Pressure        |   -   | [35.7, 17.3]    |  |
| +47.66 | +47.37 | 00:15:21.199 | Turkey             | Turkey             | 36 | Pass            |   -   | [80.7, 66.5]    | -> Mehmet Zeki Çe |

---

### Priority Case 18: `3857276_p12_fcc6b2e3` [ordinary_unsuccessful_regain]
- **Match**: 3857276 (FIFA World Cup)
- **counterpressing_team**: Morocco
- **opponent_team_at_turnover**: Canada
- **possession_team_at_counterpress_initiation**: Canada
- **possession_id_at_counterpress_initiation**: 12
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:05:49.229) | **Initiation**: Pressure (00:05:49.485)
- **Initiation Delay**: 0.256s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.892s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `successful_regain`
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

### Priority Case 19: `3837954_p102_c3d7ac6b` [ordinary_unsuccessful_regain]
- **Match**: 3837954 (Ligue 1)
- **counterpressing_team**: Paris Saint-Germain
- **opponent_team_at_turnover**: Angers
- **possession_team_at_counterpress_initiation**: Angers
- **possession_id_at_counterpress_initiation**: 102
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:20:08.392) | **Initiation**: Pressure (00:20:09.388)
- **Initiation Delay**: 0.996s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.73 |  -1.73 | 00:20:07.661 | Paris Saint-Germai | Paris Saint-Germai | 101 | Carry           |   -   | [102.1, 44.1]   |  |
|  -0.36 |  -1.36 | 00:20:08.029 | Paris Saint-Germai | Paris Saint-Germai | 101 | Pass            |   -   | [102.1, 44.1]   | Incomplete (Incomplete) |
|  +0.00 |  -1.00 | 00:20:08.392 | Paris Saint-Germai | Paris Saint-Germai | 101 | Ball Receipt*   |   -   | [107.1, 46.1]   | Incomplete |
|  +0.00 |  -1.00 | 00:20:08.392 | Angers             | Angers             | 102 | Interception    |  Yes  | [15.1, 34.3]    | Won |
|  +0.00 |  -1.00 | 00:20:08.392 | Angers             | Angers             | 102 | Carry           |   -   | [15.1, 34.3]    |  |
|  +1.00 |  +0.00 | 00:20:09.388 | Paris Saint-Germai | Angers             | 102 | Pressure        |  Yes  | [104.1, 42.4]   |  |
|  +1.63 |  +0.63 | 00:20:10.023 | Angers             | Angers             | 102 | Pass            |   -   | [15.1, 38.1]    | -> Abdoulaye Bamb |
|  +3.63 |  +2.64 | 00:20:12.027 | Angers             | Angers             | 102 | Ball Receipt*   |   -   | [21.0, 61.9]    |  |
|  +3.63 |  +2.64 | 00:20:12.027 | Angers             | Angers             | 102 | Carry           |   -   | [21.0, 61.9]    |  |
|  +5.17 |  +4.17 | 00:20:13.559 | Angers             | Angers             | 102 | Pass            |   -   | [24.4, 68.1]    | -> Himad Abdelli |
|  +6.15 |  +5.15 | 00:20:14.542 | Angers             | Angers             | 102 | Ball Receipt*   |   -   | [38.3, 61.9]    |  |
|  +6.15 |  +5.15 | 00:20:14.542 | Angers             | Angers             | 102 | Carry           |   -   | [38.3, 61.9]    |  |
|  +8.17 |  +7.18 | 00:20:16.565 | Angers             | Angers             | 102 | Pass            |   -   | [51.0, 71.7]    | -> Batista Mendy |
|  +9.61 |  +8.61 | 00:20:17.997 | Angers             | Angers             | 102 | Ball Receipt*   |   -   | [43.2, 61.0]    |  |
|  +9.61 |  +8.61 | 00:20:17.997 | Angers             | Angers             | 102 | Carry           |   -   | [43.2, 61.0]    |  |
| +13.59 | +12.59 | 00:20:21.981 | Angers             | Angers             | 102 | Pass            |   -   | [45.5, 59.8]    | -> Ousmane Camara |
| +15.50 | +14.51 | 00:20:23.895 | Angers             | Angers             | 102 | Ball Receipt*   |   -   | [43.1, 27.6]    |  |

---

### Priority Case 20: `3895167_p51_d51517b5` [ordinary_unsuccessful_regain]
- **Match**: 3895167 (1. Bundesliga)
- **counterpressing_team**: Bayer Leverkusen
- **opponent_team_at_turnover**: VfB Stuttgart
- **possession_team_at_counterpress_initiation**: VfB Stuttgart
- **possession_id_at_counterpress_initiation**: 51
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:27:43.575) | **Initiation**: Pressure (00:27:47.559)
- **Initiation Delay**: 3.984s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `harmless_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `harmless_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.77 |  -6.75 | 00:27:40.808 | Bayer Leverkusen   | Bayer Leverkusen   | 50 | Pass            |   -   | [11.8, 47.2]    | Incomplete (Incomplete) |
|  +0.00 |  -3.98 | 00:27:43.575 | Bayer Leverkusen   | Bayer Leverkusen   | 50 | Ball Receipt*   |   -   | [56.9, 52.5]    | Incomplete |
|  +0.00 |  -3.98 | 00:27:43.575 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [68.9, 26.1]    | -> Angelo Stiller |
|  +1.37 |  -2.62 | 00:27:44.944 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [67.9, 38.8]    |  |
|  +1.37 |  -2.62 | 00:27:44.944 | VfB Stuttgart      | VfB Stuttgart      | 51 | Carry           |   -   | [67.9, 38.8]    |  |
|  +2.11 |  -1.88 | 00:27:45.681 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [64.1, 36.2]    | -> Dan-Axel Zagad |
|  +3.23 |  -0.75 | 00:27:46.805 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [55.6, 26.8]    |  |
|  +3.23 |  -0.75 | 00:27:46.805 | VfB Stuttgart      | VfB Stuttgart      | 51 | Carry           |   -   | [55.6, 26.8]    |  |
|  +3.98 |  +0.00 | 00:27:47.559 | Bayer Leverkusen   | VfB Stuttgart      | 51 | Pressure        |  Yes  | [63.0, 55.0]    |  |
|  +4.19 |  +0.21 | 00:27:47.767 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [55.4, 27.0]    | -> Alexander Nübe |
|  +6.50 |  +2.51 | 00:27:50.072 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [19.3, 37.7]    |  |
|  +6.50 |  +2.51 | 00:27:50.072 | VfB Stuttgart      | VfB Stuttgart      | 51 | Carry           |   -   | [19.3, 37.7]    |  |
| +10.78 |  +6.80 | 00:27:54.355 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [20.3, 38.2]    | -> Dan-Axel Zagad |
| +12.04 |  +8.06 | 00:27:55.620 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [24.2, 23.9]    |  |
| +12.04 |  +8.06 | 00:27:55.620 | VfB Stuttgart      | VfB Stuttgart      | 51 | Carry           |   -   | [24.2, 23.9]    |  |
| +14.57 | +10.59 | 00:27:58.147 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [23.5, 23.2]    | -> Alexander Nübe |
| +16.76 | +12.78 | 00:28:00.335 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [12.1, 37.7]    |  |
| +16.76 | +12.78 | 00:28:00.335 | VfB Stuttgart      | VfB Stuttgart      | 51 | Carry           |   -   | [12.1, 37.7]    |  |
| +26.28 | +22.30 | 00:28:09.857 | VfB Stuttgart      | VfB Stuttgart      | 51 | Pass            |   -   | [15.5, 39.4]    | -> Atakan Karazor |
| +27.41 | +23.43 | 00:28:10.985 | VfB Stuttgart      | VfB Stuttgart      | 51 | Ball Receipt*   |   -   | [34.3, 51.7]    |  |

---

### Priority Case 21: `3788755_p18_b58f036d` [dangerous_shot]
- **Match**: 3788755 (UEFA Euro)
- **counterpressing_team**: Wales
- **opponent_team_at_turnover**: Turkey
- **possession_team_at_counterpress_initiation**: Turkey
- **possession_id_at_counterpress_initiation**: 18
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:08:20.865) | **Initiation**: Pressure (00:08:22.961)
- **Initiation Delay**: 2.096s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.46 |  -3.56 | 00:08:19.401 | Wales              | Wales              | 17 | Pass            |   -   | [48.5, 0.1]     | Incomplete (Incomplete) |
|  +0.00 |  -2.10 | 00:08:20.865 | Wales              | Wales              | 17 | Ball Receipt*   |   -   | [65.1, 7.9]     | Incomplete |
|  +0.00 |  -2.10 | 00:08:20.865 | Turkey             | Turkey             | 18 | Pass            |   -   | [54.7, 71.0]    | -> Okay Yokuşlu |
|  +1.41 |  -0.68 | 00:08:22.279 | Turkey             | Turkey             | 18 | Ball Receipt*   |   -   | [57.9, 64.5]    |  |
|  +1.41 |  -0.68 | 00:08:22.279 | Turkey             | Turkey             | 18 | Carry           |   -   | [57.9, 64.5]    |  |
|  +2.10 |  +0.00 | 00:08:22.961 | Wales              | Turkey             | 18 | Pressure        |  Yes  | [56.6, 13.6]    |  |
|  +2.17 |  +0.08 | 00:08:23.038 | Turkey             | Turkey             | 18 | Pass            |   -   | [62.0, 64.2]    | -> Hakan Çalhanoğ |
|  +2.56 |  +0.46 | 00:08:23.425 | Wales              | Turkey             | 18 | Pressure        |  Yes  | [50.9, 21.9]    |  |
|  +2.75 |  +0.65 | 00:08:23.613 | Turkey             | Turkey             | 18 | Ball Receipt*   |   -   | [67.4, 58.9]    |  |
|  +2.75 |  +0.65 | 00:08:23.613 | Turkey             | Turkey             | 18 | Carry           |   -   | [67.4, 58.9]    |  |
|  +3.15 |  +1.06 | 00:08:24.018 | Wales              | Turkey             | 18 | Foul Committed  |  Yes  | [52.4, 13.2]    |  |
|  +3.15 |  +1.06 | 00:08:24.018 | Turkey             | Turkey             | 18 | Foul Won        |   -   | [67.7, 66.9]    |  |
|  +6.66 |  +4.56 | 00:08:27.525 | Turkey             | Turkey             | 19 | Pass            |   -   | [67.4, 75.5]    | -> Cengiz Ünder |
|  +9.65 |  +7.56 | 00:08:30.519 | Turkey             | Turkey             | 19 | Ball Receipt*   |   -   | [98.5, 72.8]    |  |
| +11.22 |  +9.13 | 00:08:32.088 | Turkey             | Turkey             | 19 | Pass            |   -   | [108.2, 71.0]   | -> Burak Yılmaz |
| +12.13 | +10.03 | 00:08:32.994 | Turkey             | Turkey             | 19 | Ball Receipt*   |   -   | [104.9, 49.7]   |  |
| +12.17 | +10.07 | 00:08:33.034 | Turkey             | Turkey             | 19 | Shot            |   -   | [104.0, 47.1]   | Blocked |

---

### Priority Case 22: `3893805_p151_f4fb206d` [dangerous_shot]
- **Match**: 3893805 (Women's World Cup)
- **counterpressing_team**: Costa Rica Women's
- **opponent_team_at_turnover**: Japan Women's
- **possession_team_at_counterpress_initiation**: Japan Women's
- **possession_id_at_counterpress_initiation**: 151
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:31:35.148) | **Initiation**: Pressure (00:31:37.646)
- **Initiation Delay**: 2.498s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.986s) | Evidence: `goalkeeper_control` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.22 |  -3.72 | 00:31:33.930 | Costa Rica Women's | Costa Rica Women's | 150 | Pass            |   -   | [33.4, 66.4]    | Incomplete (Incomplete) |
|  +0.00 |  -2.50 | 00:31:35.148 | Costa Rica Women's | Costa Rica Women's | 150 | Ball Receipt*   |   -   | [44.0, 74.0]    | Incomplete |
|  +0.00 |  -2.50 | 00:31:35.148 | Japan Women's      | Japan Women's      | 151 | Interception    |  Yes  | [77.3, 9.1]     | Won |
|  +0.00 |  -2.50 | 00:31:35.148 | Japan Women's      | Japan Women's      | 151 | Carry           |   -   | [77.3, 9.1]     |  |
|  +1.59 |  -0.90 | 00:31:36.742 | Japan Women's      | Japan Women's      | 151 | Pass            |   -   | [85.8, 13.0]    | -> Riko Ueki |
|  +2.50 |  +0.00 | 00:31:37.646 | Costa Rica Women's | Japan Women's      | 151 | Pressure        |  Yes  | [32.6, 54.4]    |  |
|  +2.58 |  +0.09 | 00:31:37.731 | Japan Women's      | Japan Women's      | 151 | Ball Receipt*   |   -   | [88.9, 28.6]    |  |
|  +2.58 |  +0.09 | 00:31:37.731 | Japan Women's      | Japan Women's      | 151 | Carry           |   -   | [88.9, 28.6]    |  |
|  +3.98 |  +1.48 | 00:31:39.124 | Japan Women's      | Japan Women's      | 151 | Pass            |   -   | [93.8, 33.0]    | -> Hinata Miyazaw |
|  +4.90 |  +2.40 | 00:31:40.049 | Japan Women's      | Japan Women's      | 151 | Ball Receipt*   |   -   | [101.0, 41.1]   |  |
|  +4.90 |  +2.40 | 00:31:40.049 | Japan Women's      | Japan Women's      | 151 | Carry           |   -   | [101.0, 41.1]   |  |
|  +6.39 |  +3.89 | 00:31:41.534 | Japan Women's      | Japan Women's      | 151 | Shot            |   -   | [101.3, 43.2]   | Saved |
|  +7.48 |  +4.99 | 00:31:42.632 | Costa Rica Women's | Costa Rica Women's | 152 | Goal Keeper     |   -   | [2.1, 39.5]     |  |
| +30.91 | +28.41 | 00:32:06.060 | Costa Rica Women's | Costa Rica Women's | 153 | Pass            |   -   | [14.6, 39.3]    | Incomplete (Incomplete) |
| +36.62 | +34.12 | 00:32:11.769 | Costa Rica Women's | Costa Rica Women's | 153 | Ball Receipt*   |   -   | [79.2, 47.0]    | Incomplete |
| +36.62 | +34.12 | 00:32:11.769 | Japan Women's      | Costa Rica Women's | 153 | Pass            |   -   | [38.0, 27.6]    | Incomplete (Incomplete) |
| +39.79 | +37.29 | 00:32:14.933 | Japan Women's      | Costa Rica Women's | 153 | Ball Receipt*   |   -   | [62.7, 20.7]    | Incomplete |

---

### Priority Case 23: `3802793_p128_5060fc9f` [dangerous_shot]
- **Match**: 3802793 (Ligue 1)
- **counterpressing_team**: OGC Nice
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 128
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:18:44.071) | **Initiation**: Pressure (00:18:47.101)
- **Initiation Delay**: 3.03s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.18 |  -4.21 | 00:18:42.894 | Paris Saint-Germai | OGC Nice           | 127 | Pressure        |   -   | [65.1, 49.1]    |  |
|  -0.64 |  -3.67 | 00:18:43.435 | OGC Nice           | OGC Nice           | 127 | Pass            |   -   | [57.4, 28.6]    | Incomplete (Incomplete) |
|  +0.00 |  -3.03 | 00:18:44.071 | OGC Nice           | OGC Nice           | 127 | Ball Receipt*   |   -   | [41.5, 25.0]    | Incomplete |
|  +0.00 |  -3.03 | 00:18:44.071 | Paris Saint-Germai | Paris Saint-Germai | 128 | Interception    |  Yes  | [68.5, 51.9]    | Won |
|  +0.00 |  -3.03 | 00:18:44.071 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [68.5, 51.9]    |  |
|  +3.03 |  +0.00 | 00:18:47.101 | OGC Nice           | Paris Saint-Germai | 128 | Pressure        |  Yes  | [27.6, 30.5]    |  |
|  +4.01 |  +0.98 | 00:18:48.080 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [93.7, 50.4]    | Incomplete (Incomplete) |
|  +4.23 |  +1.20 | 00:18:48.300 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [101.2, 56.2]   | Incomplete |
|  +4.23 |  +1.20 | 00:18:48.300 | OGC Nice           | Paris Saint-Germai | 128 | Interception    |  Yes  | [22.9, 28.8]    | Lost In Play |
|  +6.24 |  +3.21 | 00:18:50.314 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [89.0, 55.8]    | -> Lionel Andrés  |
|  +7.20 |  +4.17 | 00:18:51.273 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [94.0, 37.8]    |  |
|  +7.20 |  +4.17 | 00:18:51.273 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [94.0, 37.8]    |  |
|  +7.84 |  +4.81 | 00:18:51.911 | OGC Nice           | Paris Saint-Germai | 128 | Pressure        |   -   | [19.5, 44.7]    |  |
|  +8.57 |  +5.54 | 00:18:52.638 | Paris Saint-Germai | Paris Saint-Germai | 128 | Pass            |   -   | [93.1, 35.4]    | -> Kylian Mbappé  |
|  +9.19 |  +6.16 | 00:18:53.264 | Paris Saint-Germai | Paris Saint-Germai | 128 | Ball Receipt*   |   -   | [108.1, 32.2]   |  |
|  +9.19 |  +6.16 | 00:18:53.264 | Paris Saint-Germai | Paris Saint-Germai | 128 | Carry           |   -   | [108.1, 32.2]   |  |
| +10.01 |  +6.98 | 00:18:54.084 | Paris Saint-Germai | Paris Saint-Germai | 128 | Shot            |   -   | [108.9, 32.9]   | Off T |
| +10.65 |  +7.62 | 00:18:54.723 | OGC Nice           | Paris Saint-Germai | 128 | Goal Keeper     |   -   | [5.4, 44.6]     |  |
| +52.20 | +49.17 | 00:19:36.270 | OGC Nice           | OGC Nice           | 129 | Pass            |   -   | [7.0, 44.1]     | Incomplete (Incomplete) |
| +56.48 | +53.45 | 00:19:40.551 | OGC Nice           | OGC Nice           | 129 | Ball Receipt*   |   -   | [71.3, 51.5]    | Incomplete |

---

### Priority Case 24: `3773597_p26_7e73f311` [dangerous_shot]
- **Match**: 3773597 (La Liga)
- **counterpressing_team**: Real Sociedad
- **opponent_team_at_turnover**: Barcelona
- **possession_team_at_counterpress_initiation**: Barcelona
- **possession_id_at_counterpress_initiation**: 26
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:16:33.884) | **Initiation**: Pressure (00:16:34.284)
- **Initiation Delay**: 0.4s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 6.716s) | Evidence: `new_possession_completed_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.76 |  -3.16 | 00:16:31.127 | Real Sociedad      | Real Sociedad      | 25 | Carry           |   -   | [44.2, 13.4]    |  |
|  -2.76 |  -3.16 | 00:16:31.127 | Barcelona          | Real Sociedad      | 25 | Block           |   -   | [100.2, 53.5]   |  |
|  -1.00 |  -1.40 | 00:16:32.883 | Barcelona          | Real Sociedad      | 25 | Pressure        |   -   | [77.9, 67.2]    |  |
|  -0.56 |  -0.96 | 00:16:33.322 | Real Sociedad      | Real Sociedad      | 25 | Miscontrol      |   -   | [39.4, 12.7]    |  |
|  +0.00 |  -0.40 | 00:16:33.884 | Barcelona          | Barcelona          | 26 | Pass            |   -   | [79.6, 67.4]    | -> Sergio Busquet |
|  +0.40 |  +0.00 | 00:16:34.284 | Real Sociedad      | Barcelona          | 26 | Pressure        |  Yes  | [32.9, 17.7]    |  |
|  +0.74 |  +0.34 | 00:16:34.620 | Barcelona          | Barcelona          | 26 | Ball Receipt*   |   -   | [85.3, 64.3]    |  |
|  +0.74 |  +0.34 | 00:16:34.620 | Barcelona          | Barcelona          | 26 | Carry           |   -   | [85.3, 64.3]    |  |
|  +2.22 |  +1.82 | 00:16:36.101 | Barcelona          | Barcelona          | 26 | Pass            |   -   | [88.2, 67.4]    | -> Lionel Andrés  |
|  +2.81 |  +2.41 | 00:16:36.690 | Barcelona          | Barcelona          | 26 | Ball Receipt*   |   -   | [94.4, 55.0]    |  |
|  +2.81 |  +2.41 | 00:16:36.690 | Barcelona          | Barcelona          | 26 | Carry           |   -   | [94.4, 55.0]    |  |
|  +3.17 |  +2.77 | 00:16:37.052 | Real Sociedad      | Barcelona          | 26 | Pressure        |  Yes  | [29.1, 24.4]    |  |
|  +4.78 |  +4.38 | 00:16:38.662 | Barcelona          | Barcelona          | 26 | Shot            |   -   | [99.5, 45.1]    | Blocked |
|  +5.06 |  +4.66 | 00:16:38.943 | Real Sociedad      | Barcelona          | 26 | Block           |   -   | [18.4, 35.5]    |  |
|  +5.76 |  +5.36 | 00:16:39.642 | Real Sociedad      | Barcelona          | 26 | Goal Keeper     |   -   | [4.5, 38.9]     |  |
|  +7.12 |  +6.72 | 00:16:41.000 | Real Sociedad      | Real Sociedad      | 27 | Pass            |   -   | [0.7, 31.8]     | -> Robin Aime Rob |
|  +9.36 |  +8.96 | 00:16:43.248 | Real Sociedad      | Real Sociedad      | 27 | Ball Receipt*   |   -   | [7.5, 26.6]     |  |
|  +9.36 |  +8.96 | 00:16:43.248 | Real Sociedad      | Real Sociedad      | 27 | Pass            |   -   | [5.9, 24.6]     | -> Martín Merquel |

---

### Priority Case 25: `3837859_p152_f43e1242` [dangerous_shot]
- **Match**: 3837859 (Ligue 1)
- **counterpressing_team**: Toulouse
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 152
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:46:19.850) | **Initiation**: Pressure (00:46:21.412)
- **Initiation Delay**: 1.562s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.15 |  -3.71 | 00:46:17.702 | Paris Saint-Germai | Toulouse           | 151 | Pressure        |   -   | [103.6, 58.6]   |  |
|  -2.00 |  -3.56 | 00:46:17.852 | Toulouse           | Toulouse           | 151 | Pass            |   -   | [16.2, 22.8]    | Incomplete (Incomplete) |
|  +0.00 |  -1.56 | 00:46:19.850 | Paris Saint-Germai | Paris Saint-Germai | 152 | Pass            |   -   | [85.1, 59.2]    | -> Lionel Andrés  |
|  +1.36 |  -0.20 | 00:46:21.213 | Paris Saint-Germai | Paris Saint-Germai | 152 | Ball Receipt*   |   -   | [99.7, 65.3]    |  |
|  +1.36 |  -0.20 | 00:46:21.213 | Paris Saint-Germai | Paris Saint-Germai | 152 | Carry           |   -   | [99.7, 65.3]    |  |
|  +1.56 |  +0.00 | 00:46:21.412 | Toulouse           | Paris Saint-Germai | 152 | Pressure        |  Yes  | [22.2, 14.2]    |  |
|  +5.81 |  +4.25 | 00:46:25.659 | Toulouse           | Paris Saint-Germai | 152 | Pressure        |   -   | [21.5, 39.3]    |  |
|  +6.25 |  +4.69 | 00:46:26.102 | Paris Saint-Germai | Paris Saint-Germai | 152 | Pass            |   -   | [96.4, 38.8]    | -> Ismaël Gharbi |
|  +7.48 |  +5.92 | 00:46:27.332 | Paris Saint-Germai | Paris Saint-Germai | 152 | Ball Receipt*   |   -   | [103.9, 21.8]   |  |
|  +7.48 |  +5.92 | 00:46:27.332 | Paris Saint-Germai | Paris Saint-Germai | 152 | Carry           |   -   | [103.9, 21.8]   |  |
| +10.20 |  +8.63 | 00:46:30.046 | Paris Saint-Germai | Paris Saint-Germai | 152 | Shot            |   -   | [102.9, 34.2]   | Blocked |
| +10.26 |  +8.70 | 00:46:30.108 | Paris Saint-Germai | Paris Saint-Germai | 152 | Block           |   -   | [104.4, 34.8]   |  |
| +10.49 |  +8.93 | 00:46:30.339 | Toulouse           | Paris Saint-Germai | 152 | Goal Keeper     |   -   | [3.0, 41.6]     |  |
| +20.63 | +19.07 | 00:46:40.482 | Toulouse           | Toulouse           | 153 | Pass            |   -   | [7.0, 44.1]     | -> Anthony Rouaul |
| +22.63 | +21.07 | 00:46:42.482 | Toulouse           | Toulouse           | 153 | Ball Receipt*   |   -   | [15.7, 29.9]    |  |
| +23.68 | +22.12 | 00:46:43.535 | Toulouse           | Toulouse           | 153 | Pass            |   -   | [15.7, 29.9]    | -> Vincent Sierro |
| +28.34 | +26.78 | 00:46:48.192 | Toulouse           | Toulouse           | 153 | Ball Receipt*   |   -   | [39.4, 37.9]    |  |

---

### Priority Case 26: `3930176_p61_41cce0ac` [final_third_penetration]
- **Match**: 3930176 (UEFA Euro)
- **counterpressing_team**: Switzerland
- **opponent_team_at_turnover**: Germany
- **possession_team_at_counterpress_initiation**: Germany
- **possession_id_at_counterpress_initiation**: 61
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:39:01.356) | **Initiation**: Pressure (00:39:02.576)
- **Initiation Delay**: 1.22s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 5.256s) | Evidence: `completed_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.85 |  -3.07 | 00:38:59.509 | Switzerland        | Switzerland        | 60 | Ball Receipt*   |   -   | [73.4, 68.6]    |  |
|  -1.85 |  -3.07 | 00:38:59.509 | Switzerland        | Switzerland        | 60 | Pass            |   -   | [73.7, 69.1]    | Incomplete (Incomplete) |
|  -1.65 |  -2.87 | 00:38:59.708 | Germany            | Switzerland        | 60 | Block           |   -   | [45.0, 12.6]    |  |
|  -0.48 |  -1.70 | 00:39:00.873 | Switzerland        | Switzerland        | 60 | Pressure        |   -   | [66.8, 70.5]    |  |
|  +0.00 |  -1.22 | 00:39:01.356 | Germany            | Germany            | 61 | Pass            |   -   | [51.4, 7.1]     | -> Kai Havertz |
|  +1.22 |  +0.00 | 00:39:02.576 | Switzerland        | Germany            | 61 | Pressure        |  Yes  | [57.8, 63.1]    |  |
|  +1.37 |  +0.15 | 00:39:02.722 | Germany            | Germany            | 61 | Ball Receipt*   |   -   | [59.4, 15.7]    |  |
|  +1.37 |  +0.15 | 00:39:02.722 | Germany            | Germany            | 61 | Carry           |   -   | [59.4, 15.7]    |  |
|  +1.42 |  +0.20 | 00:39:02.776 | Germany            | Germany            | 61 | Pass            |   -   | [59.0, 15.6]    | -> Maximilian Mit |
|  +3.28 |  +2.06 | 00:39:04.637 | Germany            | Germany            | 61 | Ball Receipt*   |   -   | [69.7, 7.1]     |  |
|  +3.28 |  +2.06 | 00:39:04.637 | Germany            | Germany            | 61 | Carry           |   -   | [69.7, 7.1]     |  |
|  +3.48 |  +2.26 | 00:39:04.832 | Germany            | Germany            | 61 | Pass            |   -   | [71.5, 7.6]     | Incomplete (Incomplete) |
|  +5.79 |  +4.57 | 00:39:07.142 | Germany            | Germany            | 61 | Pressure        |   -   | [99.2, 15.7]    |  |
|  +6.48 |  +5.26 | 00:39:07.832 | Germany            | Germany            | 61 | Ball Receipt*   |   -   | [98.3, 17.0]    | Incomplete |
|  +6.48 |  +5.26 | 00:39:07.832 | Switzerland        | Germany            | 61 | Pass            |   -   | [15.7, 63.1]    | -> Yann Sommer |
|  +7.64 |  +6.42 | 00:39:08.995 | Germany            | Germany            | 61 | Pressure        |  Yes  | [114.2, 28.1]   |  |
|  +8.35 |  +7.13 | 00:39:09.707 | Switzerland        | Germany            | 61 | Ball Receipt*   |   -   | [3.6, 44.7]     |  |
|  +8.35 |  +7.13 | 00:39:09.707 | Switzerland        | Germany            | 61 | Carry           |   -   | [3.6, 44.7]     |  |
| +10.36 |  +9.14 | 00:39:11.718 | Switzerland        | Germany            | 61 | Pass            |   -   | [6.7, 35.5]     | Incomplete (Incomplete) |
| +12.95 | +11.73 | 00:39:14.302 | Germany            | Germany            | 61 | Ball Recovery   |   -   | [63.1, 41.3]    |  |

---

### Priority Case 27: `3788771_p151_5d4cb613` [final_third_penetration]
- **Match**: 3788771 (UEFA Euro)
- **counterpressing_team**: Scotland
- **opponent_team_at_turnover**: Croatia
- **possession_team_at_counterpress_initiation**: Croatia
- **possession_id_at_counterpress_initiation**: 151
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:34:02.319) | **Initiation**: Pressure (00:34:07.023)
- **Initiation Delay**: 4.704s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 9.895s) | Evidence: `interception_plus_control` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.61 |  -6.31 | 00:34:00.713 | Croatia            | Scotland           | 150 | Clearance       |   -   | [7.2, 40.3]     |  |
|  -0.24 |  -4.95 | 00:34:02.076 | Scotland           | Scotland           | 150 | Pressure        |   -   | [91.2, 29.4]    |  |
|  +0.00 |  -4.70 | 00:34:02.319 | Croatia            | Croatia            | 151 | Pass            |   -   | [29.9, 57.7]    | -> Andrej Kramari |
|  +1.20 |  -3.51 | 00:34:03.515 | Croatia            | Croatia            | 151 | Ball Receipt*   |   -   | [39.6, 50.9]    |  |
|  +1.20 |  -3.51 | 00:34:03.515 | Croatia            | Croatia            | 151 | Carry           |   -   | [39.6, 50.9]    |  |
|  +4.70 |  +0.00 | 00:34:07.023 | Scotland           | Croatia            | 151 | Pressure        |  Yes  | [61.6, 51.4]    |  |
|  +7.64 |  +2.93 | 00:34:09.955 | Croatia            | Croatia            | 151 | Pass            |   -   | [73.3, 18.9]    | -> Ivan Perišić |
|  +8.50 |  +3.80 | 00:34:10.818 | Croatia            | Croatia            | 151 | Ball Receipt*   |   -   | [68.7, 14.9]    |  |
|  +8.50 |  +3.80 | 00:34:10.818 | Croatia            | Croatia            | 151 | Carry           |   -   | [68.7, 14.9]    |  |
| +11.30 |  +6.59 | 00:34:13.617 | Scotland           | Croatia            | 151 | Pressure        |   -   | [41.0, 60.7]    |  |
| +14.01 |  +9.31 | 00:34:16.329 | Croatia            | Croatia            | 151 | Pass            |   -   | [93.1, 25.4]    | Incomplete (Incomplete) |
| +14.60 |  +9.90 | 00:34:16.918 | Croatia            | Croatia            | 151 | Ball Receipt*   |   -   | [92.1, 36.9]    | Incomplete |
| +14.60 |  +9.90 | 00:34:16.918 | Scotland           | Croatia            | 151 | Interception    |   -   | [27.0, 49.7]    | Success In Play |
| +16.35 | +11.65 | 00:34:18.669 | Croatia            | Croatia            | 151 | Pressure        |   -   | [106.1, 34.2]   |  |
| +17.11 | +12.40 | 00:34:19.428 | Scotland           | Scotland           | 152 | Pass            |   -   | [9.4, 38.5]     | -> Lyndon Dykes |
| +19.63 | +14.92 | 00:34:21.947 | Scotland           | Scotland           | 152 | Ball Receipt*   |   -   | [56.9, 43.2]    |  |
| +19.63 | +14.92 | 00:34:21.947 | Scotland           | Scotland           | 152 | Pass            |   -   | [56.9, 43.2]    | -> Ryan Fraser |

---

### Priority Case 28: `3901832_p94_db3966bf` [final_third_penetration]
- **Match**: 3901832 (Women's World Cup)
- **counterpressing_team**: Colombia Women's
- **opponent_team_at_turnover**: Jamaica Women's
- **possession_team_at_counterpress_initiation**: Jamaica Women's
- **possession_id_at_counterpress_initiation**: 94
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:00:18.266) | **Initiation**: Block (00:00:22.658)
- **Initiation Delay**: 4.392s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.98 |  -5.38 | 00:00:17.282 | Jamaica Women's    | Colombia Women's   | 93 | Pressure        |   -   | [32.7, 64.1]    |  |
|  +0.00 |  -4.39 | 00:00:18.266 | Colombia Women's   | Colombia Women's   | 93 | Duel            |  Yes  | [87.4, 16.0]    | Aerial Lost |
|  +0.00 |  -4.39 | 00:00:18.266 | Jamaica Women's    | Jamaica Women's    | 94 | Pass            |   -   | [32.7, 64.1]    | -> Allyson Swaby |
|  +1.32 |  -3.07 | 00:00:19.590 | Jamaica Women's    | Jamaica Women's    | 94 | Ball Receipt*   |   -   | [27.1, 64.4]    |  |
|  +1.32 |  -3.07 | 00:00:19.590 | Jamaica Women's    | Jamaica Women's    | 94 | Pass            |   -   | [25.4, 64.4]    | -> Khadija Monifa |
|  +4.39 |  +0.00 | 00:00:22.658 | Jamaica Women's    | Jamaica Women's    | 94 | Ball Receipt*   |   -   | [70.7, 61.3]    |  |
|  +4.39 |  +0.00 | 00:00:22.658 | Jamaica Women's    | Jamaica Women's    | 94 | Carry           |   -   | [70.7, 61.3]    |  |
|  +4.39 |  +0.00 | 00:00:22.658 | Colombia Women's   | Jamaica Women's    | 94 | Block           |  Yes  | [48.6, 18.0]    |  |
|  +7.13 |  +2.74 | 00:00:25.396 | Colombia Women's   | Jamaica Women's    | 94 | Pressure        |   -   | [46.7, 29.1]    |  |
|  +7.62 |  +3.23 | 00:00:25.887 | Jamaica Women's    | Jamaica Women's    | 94 | Pass            |   -   | [72.8, 51.5]    | -> Jody Brown |
|  +9.70 |  +5.30 | 00:00:27.962 | Jamaica Women's    | Jamaica Women's    | 94 | Ball Receipt*   |   -   | [70.7, 31.5]    |  |
|  +9.70 |  +5.30 | 00:00:27.962 | Jamaica Women's    | Jamaica Women's    | 94 | Carry           |   -   | [70.7, 31.5]    |  |
| +10.79 |  +6.40 | 00:00:29.059 | Jamaica Women's    | Jamaica Women's    | 94 | Pass            |   -   | [73.8, 31.8]    | -> Drew Spence |
| +11.85 |  +7.45 | 00:00:30.111 | Jamaica Women's    | Jamaica Women's    | 94 | Ball Receipt*   |   -   | [80.4, 49.6]    |  |
| +11.85 |  +7.45 | 00:00:30.111 | Jamaica Women's    | Jamaica Women's    | 94 | Carry           |   -   | [80.4, 49.6]    |  |
| +13.98 |  +9.59 | 00:00:32.251 | Jamaica Women's    | Jamaica Women's    | 94 | Pass            |   -   | [87.6, 53.3]    | -> Trudi Sudan Ca |
| +15.14 | +10.75 | 00:00:33.410 | Jamaica Women's    | Jamaica Women's    | 94 | Ball Receipt*   |   -   | [98.9, 70.0]    |  |
| +15.14 | +10.75 | 00:00:33.410 | Jamaica Women's    | Jamaica Women's    | 94 | Carry           |   -   | [98.9, 70.0]    |  |
| +15.20 | +10.80 | 00:00:33.462 | Jamaica Women's    | Jamaica Women's    | 94 | Miscontrol      |   -   | [98.9, 70.0]    |  |

---

### Priority Case 29: `3938639_p152_b585e681` [final_third_penetration]
- **Match**: 3938639 (UEFA Euro)
- **counterpressing_team**: Turkey
- **opponent_team_at_turnover**: Georgia
- **possession_team_at_counterpress_initiation**: Georgia
- **possession_id_at_counterpress_initiation**: 152
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:48:39.961) | **Initiation**: Pressure (00:48:41.688)
- **Initiation Delay**: 1.727s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.73 | 00:48:39.961 | Turkey             | Turkey             | 151 | Ball Receipt*   |   -   | [78.7, 41.4]    | Incomplete |
|  +0.00 |  -1.73 | 00:48:39.961 | Turkey             | Turkey             | 151 | Duel            |   -   | [79.7, 41.4]    | Aerial Lost |
|  +0.00 |  -1.73 | 00:48:39.961 | Georgia            | Georgia            | 152 | Pass            |   -   | [40.4, 38.7]    | -> Sandro Altunas |
|  +0.73 |  -0.99 | 00:48:40.695 | Georgia            | Georgia            | 152 | Ball Receipt*   |   -   | [49.4, 29.2]    |  |
|  +0.73 |  -0.99 | 00:48:40.695 | Georgia            | Georgia            | 152 | Carry           |   -   | [49.4, 29.2]    |  |
|  +0.75 |  -0.98 | 00:48:40.708 | Georgia            | Georgia            | 152 | Pass            |   -   | [49.6, 29.2]    | -> Giorgi Kochora |
|  +1.54 |  -0.18 | 00:48:41.505 | Georgia            | Georgia            | 152 | Ball Receipt*   |   -   | [44.4, 32.1]    |  |
|  +1.54 |  -0.18 | 00:48:41.505 | Georgia            | Georgia            | 152 | Carry           |   -   | [44.4, 32.1]    |  |
|  +1.73 |  +0.00 | 00:48:41.688 | Turkey             | Georgia            | 152 | Pressure        |  Yes  | [77.6, 46.8]    |  |
|  +2.34 |  +0.61 | 00:48:42.303 | Turkey             | Georgia            | 152 | Foul Committed  |  Yes  | [71.4, 50.4]    |  |
|  +2.34 |  +0.61 | 00:48:42.303 | Georgia            | Georgia            | 152 | Foul Won        |   -   | [48.7, 29.7]    |  |
|  +9.49 |  +7.77 | 00:48:49.455 | Georgia            | Georgia            | 153 | Pass            |   -   | [51.8, 31.8]    | -> Otar Kakabadze |
| +12.09 | +10.36 | 00:48:52.047 | Georgia            | Georgia            | 153 | Ball Receipt*   |   -   | [63.6, 73.0]    |  |
| +12.09 | +10.36 | 00:48:52.047 | Georgia            | Georgia            | 153 | Carry           |   -   | [63.6, 73.0]    |  |
| +13.88 | +12.15 | 00:48:53.837 | Georgia            | Georgia            | 153 | Pass            |   -   | [82.0, 72.5]    | -> Budu Zivzivadz |
| +14.99 | +13.26 | 00:48:54.951 | Turkey             | Georgia            | 153 | Pressure        |   -   | [13.5, 31.0]    |  |
| +15.32 | +13.59 | 00:48:55.279 | Georgia            | Georgia            | 153 | Ball Receipt*   |   -   | [105.7, 51.2]   |  |
| +15.32 | +13.59 | 00:48:55.279 | Georgia            | Georgia            | 153 | Carry           |   -   | [105.7, 51.2]   |  |
| +15.36 | +13.63 | 00:48:55.319 | Georgia            | Georgia            | 153 | Miscontrol      |   -   | [106.2, 51.2]   |  |
| +47.38 | +45.65 | 00:49:27.339 | Turkey             | Turkey             | 154 | Pass            |   -   | [6.0, 33.3]     | -> Yusuf Yazıcı |

---

### Priority Case 30: `3877090_p118_ddf5c3ae` [final_third_penetration]
- **Match**: 3877090 (Major League Soccer)
- **counterpressing_team**: LAFC
- **opponent_team_at_turnover**: Inter Miami
- **possession_team_at_counterpress_initiation**: Inter Miami
- **possession_id_at_counterpress_initiation**: 118
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:12:54.258) | **Initiation**: Pressure (00:12:58.119)
- **Initiation Delay**: 3.861s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 13.626s) | Evidence: `duel_plus_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.99 |  -5.85 | 00:12:52.270 | Inter Miami        | LAFC               | 117 | Pressure        |  Yes  | [44.5, 20.5]    |  |
|  +0.00 |  -3.86 | 00:12:54.258 | LAFC               | LAFC               | 117 | Dribble         |   -   | [86.5, 55.0]    |  |
|  +0.00 |  -3.86 | 00:12:54.258 | Inter Miami        | Inter Miami        | 118 | Duel            |  Yes  | [33.6, 25.1]    | Tackle, Success In Play |
|  +1.79 |  -2.07 | 00:12:56.045 | Inter Miami        | Inter Miami        | 118 | Ball Recovery   |   -   | [38.0, 29.4]    |  |
|  +1.79 |  -2.07 | 00:12:56.045 | Inter Miami        | Inter Miami        | 118 | Carry           |   -   | [38.0, 29.4]    |  |
|  +3.86 |  +0.00 | 00:12:58.119 | LAFC               | Inter Miami        | 118 | Pressure        |  Yes  | [75.2, 47.2]    |  |
|  +4.77 |  +0.91 | 00:12:59.028 | Inter Miami        | Inter Miami        | 118 | Pass            |   -   | [42.2, 26.7]    | -> Facundo Farías |
|  +7.30 |  +3.44 | 00:13:01.562 | Inter Miami        | Inter Miami        | 118 | Ball Receipt*   |   -   | [46.3, 3.1]     |  |
|  +7.30 |  +3.44 | 00:13:01.562 | Inter Miami        | Inter Miami        | 118 | Carry           |   -   | [46.3, 3.1]     |  |
|  +9.18 |  +5.32 | 00:13:03.442 | Inter Miami        | Inter Miami        | 118 | Pass            |   -   | [50.0, 1.7]     | -> Jordi Alba Ram |
| +11.33 |  +7.47 | 00:13:05.588 | Inter Miami        | Inter Miami        | 118 | Ball Receipt*   |   -   | [87.9, 16.5]    |  |
| +11.33 |  +7.47 | 00:13:05.588 | Inter Miami        | Inter Miami        | 118 | Carry           |   -   | [87.9, 16.5]    |  |
| +15.23 | +11.37 | 00:13:09.484 | Inter Miami        | Inter Miami        | 118 | Pass            |   -   | [99.7, 8.5]     | -> Benjamin Crema |
| +16.24 | +12.38 | 00:13:10.502 | LAFC               | Inter Miami        | 118 | Pressure        |   -   | [21.0, 56.3]    |  |
| +16.43 | +12.57 | 00:13:10.686 | Inter Miami        | Inter Miami        | 118 | Ball Receipt*   |   -   | [99.7, 19.9]    |  |
| +16.43 | +12.57 | 00:13:10.686 | Inter Miami        | Inter Miami        | 118 | Carry           |   -   | [99.7, 19.9]    |  |
| +17.49 | +13.63 | 00:13:11.745 | Inter Miami        | Inter Miami        | 118 | Dispossessed    |   -   | [104.0, 20.2]   |  |

---

### Priority Case 31: `3930162_p126_6e7317f9` [initiation_delay_over_5s]
- **Match**: 3930162 (UEFA Euro)
- **counterpressing_team**: Slovenia
- **opponent_team_at_turnover**: Denmark
- **possession_team_at_counterpress_initiation**: Slovenia
- **possession_id_at_counterpress_initiation**: 126
- **Turnover Context**: open_play (Origin: From Goal Kick)
- **Turnover**: Ball Recovery (00:38:34.190) | **Initiation**: Pressure (00:38:41.935)
- **Initiation Delay**: 7.745s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.827s) | Evidence: `completed_pass` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.36 | -11.10 | 00:38:30.833 | Slovenia           | Slovenia           | 126 | Pass            |   -   | [37.5, 76.7]    | Incomplete (Incomplete) |
|  +0.00 |  -7.74 | 00:38:34.190 | Slovenia           | Slovenia           | 126 | Ball Receipt*   |   -   | [69.0, 60.9]    | Incomplete |
|  +0.00 |  -7.74 | 00:38:34.190 | Denmark            | Slovenia           | 126 | Ball Recovery   |   -   | [44.5, 7.1]     |  |
|  +0.00 |  -7.74 | 00:38:34.190 | Denmark            | Slovenia           | 126 | Carry           |   -   | [44.5, 7.1]     |  |
|  +3.30 |  -4.44 | 00:38:37.491 | Denmark            | Slovenia           | 126 | Pass            |   -   | [35.0, 6.4]     | -> Kasper Schmeic |
|  +5.53 |  -2.21 | 00:38:39.722 | Denmark            | Slovenia           | 126 | Ball Receipt*   |   -   | [7.8, 34.0]     |  |
|  +5.53 |  -2.21 | 00:38:39.722 | Denmark            | Slovenia           | 126 | Carry           |   -   | [7.8, 34.0]     |  |
|  +7.74 |  +0.00 | 00:38:41.935 | Slovenia           | Slovenia           | 126 | Pressure        |  Yes  | [100.6, 44.0]   |  |
|  +8.53 |  +0.78 | 00:38:42.715 | Denmark            | Slovenia           | 126 | Pass            |   -   | [8.5, 39.1]     | Incomplete (Incomplete) |
| +11.57 |  +3.83 | 00:38:45.762 | Denmark            | Slovenia           | 126 | Ball Receipt*   |   -   | [69.2, 38.7]    | Incomplete |
| +11.57 |  +3.83 | 00:38:45.762 | Slovenia           | Slovenia           | 126 | Pass            |   -   | [57.0, 45.8]    | -> Jon Gorenc Sta |
| +12.27 |  +4.53 | 00:38:46.464 | Slovenia           | Slovenia           | 126 | Ball Receipt*   |   -   | [60.2, 39.2]    |  |
| +12.27 |  +4.53 | 00:38:46.464 | Slovenia           | Slovenia           | 126 | Carry           |   -   | [60.2, 39.2]    |  |
| +13.01 |  +5.26 | 00:38:47.195 | Slovenia           | Slovenia           | 126 | Pass            |   -   | [60.2, 39.9]    | Incomplete (Incomplete) |
| +14.29 |  +6.54 | 00:38:48.478 | Slovenia           | Slovenia           | 126 | Ball Receipt*   |   -   | [83.2, 39.9]    | Incomplete |
| +14.29 |  +6.54 | 00:38:48.478 | Denmark            | Denmark            | 127 | Pass            |  Yes  | [40.5, 37.5]    | -> Christian Dann |
| +15.01 |  +7.26 | 00:38:49.200 | Denmark            | Denmark            | 127 | Ball Receipt*   |   -   | [51.1, 27.5]    |  |
| +15.01 |  +7.26 | 00:38:49.200 | Denmark            | Denmark            | 127 | Carry           |   -   | [51.1, 27.5]    |  |
| +16.45 |  +8.71 | 00:38:50.643 | Slovenia           | Denmark            | 127 | Pressure        |  Yes  | [67.6, 59.1]    |  |
| +18.05 | +10.30 | 00:38:52.237 | Slovenia           | Denmark            | 127 | Foul Committed  |  Yes  | [56.4, 55.5]    |  |

---

### Priority Case 32: `3857290_p22_379d5832` [initiation_delay_over_5s]
- **Match**: 3857290 (FIFA World Cup)
- **counterpressing_team**: Switzerland
- **opponent_team_at_turnover**: Cameroon
- **possession_team_at_counterpress_initiation**: Switzerland
- **possession_id_at_counterpress_initiation**: 22
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:11:06.904) | **Initiation**: Interception (00:11:13.634)
- **Initiation Delay**: 6.73s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.0s) | Evidence: `carry_control` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -6.73 | 00:11:06.904 | Switzerland        | Cameroon           | 21 | Ball Receipt*   |   -   | [99.5, 43.0]    | Incomplete |
|  +0.00 |  -6.73 | 00:11:06.904 | Switzerland        | Cameroon           | 21 | Duel            |   -   | [97.6, 43.0]    | Aerial Lost |
|  +0.00 |  -6.73 | 00:11:06.904 | Cameroon           | Cameroon           | 21 | Pass            |   -   | [22.5, 37.1]    | -> Jean-Charles C |
|  +1.15 |  -5.58 | 00:11:08.050 | Cameroon           | Cameroon           | 21 | Ball Receipt*   |   -   | [21.4, 33.7]    |  |
|  +1.15 |  -5.58 | 00:11:08.050 | Cameroon           | Cameroon           | 21 | Carry           |   -   | [21.4, 33.7]    |  |
|  +1.24 |  -5.49 | 00:11:08.147 | Cameroon           | Cameroon           | 21 | Pass            |   -   | [21.4, 33.7]    | -> Nouhou Tolo |
|  +2.70 |  -4.03 | 00:11:09.601 | Cameroon           | Cameroon           | 21 | Ball Receipt*   |   -   | [27.0, 21.9]    |  |
|  +2.70 |  -4.03 | 00:11:09.601 | Cameroon           | Cameroon           | 21 | Pass            |   -   | [26.4, 21.7]    | -> Jean-Eric Maxi |
|  +4.21 |  -2.52 | 00:11:11.109 | Cameroon           | Cameroon           | 21 | Ball Receipt*   |   -   | [53.5, 38.7]    |  |
|  +5.01 |  -1.72 | 00:11:11.915 | Cameroon           | Cameroon           | 21 | Pass            |   -   | [50.6, 35.2]    | -> Martin Hongla  |
|  +6.14 |  -0.59 | 00:11:13.046 | Cameroon           | Cameroon           | 21 | Ball Receipt*   |   -   | [41.8, 38.9]    |  |
|  +6.14 |  -0.59 | 00:11:13.046 | Cameroon           | Cameroon           | 21 | Carry           |   -   | [41.8, 38.9]    |  |
|  +6.18 |  -0.55 | 00:11:13.080 | Cameroon           | Cameroon           | 21 | Pass            |   -   | [41.0, 38.9]    | Incomplete (Incomplete) |
|  +6.73 |  +0.00 | 00:11:13.634 | Switzerland        | Switzerland        | 22 | Interception    |  Yes  | [73.7, 47.0]    | Won |
|  +6.73 |  +0.00 | 00:11:13.634 | Switzerland        | Switzerland        | 22 | Carry           |   -   | [73.7, 47.0]    |  |
|  +7.68 |  +0.95 | 00:11:14.588 | Cameroon           | Switzerland        | 22 | Pressure        |  Yes  | [43.7, 34.6]    |  |
|  +7.85 |  +1.12 | 00:11:14.754 | Switzerland        | Switzerland        | 22 | Pass            |   -   | [75.6, 47.2]    | -> Djibril Sow |
|  +8.42 |  +1.69 | 00:11:15.326 | Switzerland        | Switzerland        | 22 | Ball Receipt*   |   -   | [84.5, 47.0]    |  |
|  +8.42 |  +1.69 | 00:11:15.326 | Switzerland        | Switzerland        | 22 | Carry           |   -   | [84.5, 47.0]    |  |
|  +9.14 |  +2.41 | 00:11:16.043 | Switzerland        | Switzerland        | 22 | Pass            |   -   | [85.3, 45.5]    | -> Granit Xhaka |
| +10.02 |  +3.29 | 00:11:16.929 | Switzerland        | Switzerland        | 22 | Ball Receipt*   |   -   | [83.9, 28.7]    |  |
| +10.02 |  +3.29 | 00:11:16.929 | Switzerland        | Switzerland        | 22 | Carry           |   -   | [83.9, 28.7]    |  |
| +11.74 |  +5.01 | 00:11:18.640 | Switzerland        | Switzerland        | 22 | Shot            |   -   | [88.1, 28.2]    | Off T |
| +12.87 |  +6.14 | 00:11:19.771 | Cameroon           | Switzerland        | 22 | Goal Keeper     |   -   | [1.7, 39.7]     |  |
| +23.77 | +17.04 | 00:11:30.671 | Cameroon           | Cameroon           | 23 | Pass            |   -   | [7.0, 36.1]     | -> Jean-Charles C |
| +25.82 | +19.09 | 00:11:32.728 | Cameroon           | Cameroon           | 23 | Ball Receipt*   |   -   | [14.3, 63.9]    |  |

---

### Priority Case 33: `3773547_p123_7978608c` [initiation_delay_over_5s]
- **Match**: 3773547 (La Liga)
- **counterpressing_team**: Osasuna
- **opponent_team_at_turnover**: Barcelona
- **possession_team_at_counterpress_initiation**: Barcelona
- **possession_id_at_counterpress_initiation**: 123
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:05:10.117) | **Initiation**: Pressure (00:05:17.799)
- **Initiation Delay**: 7.682s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: nans) | Evidence: `nan` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.78 |  -8.46 | 00:05:09.339 | Barcelona          | Barcelona          | 120 | Ball Receipt*   |   -   | [44.2, 25.8]    |  |
|  -0.78 |  -8.46 | 00:05:09.339 | Barcelona          | Barcelona          | 120 | Carry           |   -   | [44.2, 25.8]    |  |
|  +0.00 |  -7.68 | 00:05:10.117 | Barcelona          | Barcelona          | 121 | Pass            |   -   | [44.2, 23.4]    | -> Jordi Alba Ram |
|  +1.16 |  -6.52 | 00:05:11.282 | Barcelona          | Barcelona          | 121 | Ball Receipt*   |   -   | [56.5, 7.4]     |  |
|  +1.16 |  -6.52 | 00:05:11.282 | Barcelona          | Barcelona          | 121 | Carry           |   -   | [56.5, 7.4]     |  |
|  +3.41 |  -4.27 | 00:05:13.526 | Barcelona          | Barcelona          | 122 | Pass            |   -   | [64.1, 12.9]    | -> Philippe Couti |
|  +4.27 |  -3.41 | 00:05:14.392 | Barcelona          | Barcelona          | 122 | Ball Receipt*   |   -   | [72.7, 23.6]    |  |
|  +4.27 |  -3.41 | 00:05:14.392 | Barcelona          | Barcelona          | 122 | Carry           |   -   | [72.7, 23.6]    |  |
|  +5.24 |  -2.44 | 00:05:15.356 | Barcelona          | Barcelona          | 123 | Pass            |   -   | [76.2, 28.9]    | -> Lionel Andrés  |
|  +6.20 |  -1.48 | 00:05:16.314 | Barcelona          | Barcelona          | 123 | Ball Receipt*   |   -   | [88.6, 39.9]    |  |
|  +6.20 |  -1.48 | 00:05:16.314 | Barcelona          | Barcelona          | 123 | Carry           |   -   | [88.6, 39.9]    |  |
|  +7.68 |  +0.00 | 00:05:17.799 | Osasuna            | Barcelona          | 123 | Pressure        |  Yes  | [27.2, 40.2]    |  |
|  +8.16 |  +0.48 | 00:05:18.274 | Osasuna            | Barcelona          | 123 | Dribbled Past   |  Yes  | [29.7, 40.2]    |  |
|  +8.16 |  +0.48 | 00:05:18.274 | Barcelona          | Barcelona          | 123 | Dribble         |   -   | [90.4, 39.9]    |  |
|  +8.16 |  +0.48 | 00:05:18.274 | Barcelona          | Barcelona          | 123 | Carry           |   -   | [90.4, 39.9]    |  |
|  +9.22 |  +1.54 | 00:05:19.341 | Osasuna            | Barcelona          | 123 | Pressure        |  Yes  | [22.3, 47.4]    |  |
|  +9.60 |  +1.92 | 00:05:19.720 | Barcelona          | Barcelona          | 124 | Pass            |   -   | [95.7, 32.7]    | -> Martin Braithw |
| +10.91 |  +3.23 | 00:05:21.032 | Barcelona          | Barcelona          | 124 | Ball Receipt*   |   -   | [110.1, 25.0]   |  |
| +10.91 |  +3.23 | 00:05:21.032 | Barcelona          | Barcelona          | 124 | Carry           |   -   | [110.1, 25.0]   |  |
| +11.00 |  +3.31 | 00:05:21.112 | Barcelona          | Barcelona          | 125 | Pass            |   -   | [110.1, 25.0]   | Incomplete (Incomplete) |
| +11.82 |  +4.14 | 00:05:21.942 | Barcelona          | Barcelona          | 125 | Ball Receipt*   |   -   | [112.7, 45.9]   | Incomplete |
| +11.82 |  +4.14 | 00:05:21.942 | Osasuna            | Barcelona          | 125 | Clearance       |   -   | [7.4, 36.6]     |  |
| +36.22 | +28.54 | 00:05:46.334 | Barcelona          | Barcelona          | 126 | Pass            |   -   | [120.0, 80.0]   | -> Antoine Griezm |
| +37.58 | +29.90 | 00:05:47.702 | Barcelona          | Barcelona          | 126 | Ball Receipt*   |   -   | [117.8, 65.1]   |  |

---

### Priority Case 34: `3803000_p18_8d0b4f71` [initiation_delay_over_5s]
- **Match**: 3803000 (Ligue 1)
- **counterpressing_team**: Clermont Foot
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 18
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:10:16.205) | **Initiation**: Pressure (00:10:22.603)
- **Initiation Delay**: 6.398s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `0` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `0` (time: 11.332s) | Evidence: `new_possession_completed_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -8.46 | -14.86 | 00:10:07.746 | Clermont Foot      | Clermont Foot      | 14 | Shot            |   -   | [115.7, 53.0]   | Saved |
|  -7.75 | -14.15 | 00:10:08.456 | Paris Saint-Germai | Paris Saint-Germai | 15 | Goal Keeper     |   -   | [1.3, 36.6]     |  |
|  +0.00 |  -6.40 | 00:10:16.205 | Paris Saint-Germai | Paris Saint-Germai | 16 | Pass            |   -   | [8.7, 41.0]     | -> Marco Verratti |
|  +0.92 |  -5.48 | 00:10:17.123 | Paris Saint-Germai | Paris Saint-Germai | 16 | Ball Receipt*   |   -   | [32.7, 37.0]    |  |
|  +2.29 |  -4.11 | 00:10:18.493 | Paris Saint-Germai | Paris Saint-Germai | 17 | Pass            |   -   | [34.2, 37.0]    | -> Idrissa Gana G |
|  +3.13 |  -3.27 | 00:10:19.337 | Paris Saint-Germai | Paris Saint-Germai | 17 | Ball Receipt*   |   -   | [42.6, 18.3]    |  |
|  +4.12 |  -2.28 | 00:10:20.324 | Paris Saint-Germai | Paris Saint-Germai | 18 | Pass            |   -   | [42.6, 18.3]    | -> Kylian Mbappé  |
|  +4.85 |  -1.54 | 00:10:21.058 | Paris Saint-Germai | Paris Saint-Germai | 18 | Ball Receipt*   |   -   | [51.4, 22.3]    |  |
|  +4.85 |  -1.54 | 00:10:21.058 | Paris Saint-Germai | Paris Saint-Germai | 18 | Carry           |   -   | [51.4, 22.3]    |  |
|  +6.40 |  +0.00 | 00:10:22.603 | Clermont Foot      | Paris Saint-Germai | 18 | Pressure        |  Yes  | [62.7, 58.6]    |  |
|  +8.11 |  +1.72 | 00:10:24.319 | Paris Saint-Germai | Paris Saint-Germai | 19 | Pass            |   -   | [74.0, 12.3]    | Incomplete (Out) |
| +10.30 |  +3.91 | 00:10:26.508 | Paris Saint-Germai | Paris Saint-Germai | 19 | Ball Receipt*   |   -   | [81.5, 4.1]     | Incomplete |
| +17.73 | +11.33 | 00:10:33.935 | Clermont Foot      | Clermont Foot      | 20 | Pass            |   -   | [19.8, 80.0]    | -> Johan Gastien |
| +18.44 | +12.04 | 00:10:34.644 | Clermont Foot      | Clermont Foot      | 20 | Ball Receipt*   |   -   | [25.4, 71.4]    |  |
| +20.95 | +14.55 | 00:10:37.153 | Clermont Foot      | Clermont Foot      | 20 | Pass            |   -   | [31.0, 70.1]    | -> Jason Berthomi |
| +21.97 | +15.58 | 00:10:38.180 | Clermont Foot      | Clermont Foot      | 20 | Ball Receipt*   |   -   | [32.1, 60.7]    |  |
| +21.97 | +15.58 | 00:10:38.180 | Clermont Foot      | Clermont Foot      | 20 | Pass            |   -   | [32.1, 60.7]    | -> Johan Gastien |
| +22.61 | +16.21 | 00:10:38.814 | Clermont Foot      | Clermont Foot      | 20 | Ball Receipt*   |   -   | [35.9, 66.0]    |  |
| +22.61 | +16.21 | 00:10:38.814 | Clermont Foot      | Clermont Foot      | 20 | Carry           |   -   | [35.9, 66.0]    |  |
| +23.68 | +17.29 | 00:10:39.888 | Clermont Foot      | Clermont Foot      | 20 | Pass            |   -   | [35.9, 66.0]    | -> Akim Zedadka |
| +25.78 | +19.38 | 00:10:41.981 | Clermont Foot      | Clermont Foot      | 20 | Ball Receipt*   |   -   | [59.5, 80.0]    |  |

---

### Priority Case 35: `3877115_p58_e75ec80b` [initiation_delay_over_5s]
- **Match**: 3877115 (Major League Soccer)
- **counterpressing_team**: Toronto FC
- **opponent_team_at_turnover**: Inter Miami
- **possession_team_at_counterpress_initiation**: Toronto FC
- **possession_id_at_counterpress_initiation**: 58
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:35:14.711) | **Initiation**: Pass (00:35:22.283)
- **Initiation Delay**: 7.572s (Quality: `invalid`, Latency Valid: `False`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `successful_regain`
- **New Controlled Labels**: Regain 5s: `1` (time: 2.423s) | Evidence: `controlled_ball_receipt` | 3-Class: `successful_regain`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.29 |  -8.86 | 00:35:13.425 | Toronto FC         | Toronto FC         | 58 | Ball Receipt*   |   -   | [96.4, 33.7]    | Incomplete |
|  -1.29 |  -8.86 | 00:35:13.425 | Inter Miami        | Toronto FC         | 58 | Block           |   -   | [25.1, 53.6]    |  |
|  +0.00 |  -7.57 | 00:35:14.711 | Inter Miami        | Toronto FC         | 58 | Ball Recovery   |   -   | [29.1, 54.7]    |  |
|  +0.00 |  -7.57 | 00:35:14.711 | Inter Miami        | Toronto FC         | 58 | Carry           |   -   | [29.1, 54.7]    |  |
|  +4.03 |  -3.54 | 00:35:18.745 | Inter Miami        | Toronto FC         | 58 | Pass            |   -   | [46.2, 55.5]    | -> Lionel Andrés  |
|  +5.11 |  -2.46 | 00:35:19.820 | Inter Miami        | Toronto FC         | 58 | Ball Receipt*   |   -   | [57.4, 45.9]    |  |
|  +5.11 |  -2.46 | 00:35:19.820 | Inter Miami        | Toronto FC         | 58 | Carry           |   -   | [57.4, 45.9]    |  |
|  +6.56 |  -1.02 | 00:35:21.266 | Inter Miami        | Toronto FC         | 58 | Pass            |   -   | [57.2, 42.0]    | Incomplete (Incomplete) |
|  +7.57 |  +0.00 | 00:35:22.283 | Inter Miami        | Toronto FC         | 58 | Ball Receipt*   |   -   | [73.5, 29.9]    | Incomplete |
|  +7.57 |  +0.00 | 00:35:22.283 | Toronto FC         | Toronto FC         | 58 | Pass            |  Yes  | [42.7, 45.4]    | -> Alonso Coello  |
| +10.00 |  +2.42 | 00:35:24.706 | Toronto FC         | Toronto FC         | 58 | Ball Receipt*   |   -   | [39.3, 27.1]    |  |
| +10.00 |  +2.42 | 00:35:24.706 | Toronto FC         | Toronto FC         | 58 | Carry           |   -   | [39.3, 27.1]    |  |
| +11.44 |  +3.87 | 00:35:26.150 | Toronto FC         | Toronto FC         | 58 | Pass            |   -   | [36.2, 27.3]    | -> Franco Ibarra |
| +12.32 |  +4.75 | 00:35:27.030 | Toronto FC         | Toronto FC         | 58 | Ball Receipt*   |   -   | [43.3, 35.0]    |  |
| +12.32 |  +4.75 | 00:35:27.030 | Toronto FC         | Toronto FC         | 58 | Carry           |   -   | [43.3, 35.0]    |  |
| +12.36 |  +4.79 | 00:35:27.070 | Toronto FC         | Toronto FC         | 58 | Pass            |   -   | [43.1, 34.6]    | -> Michael Bradle |
| +14.69 |  +7.11 | 00:35:29.396 | Toronto FC         | Toronto FC         | 58 | Ball Receipt*   |   -   | [40.2, 19.8]    |  |
| +14.69 |  +7.11 | 00:35:29.396 | Toronto FC         | Toronto FC         | 58 | Carry           |   -   | [40.2, 19.8]    |  |
| +14.95 |  +7.38 | 00:35:29.658 | Toronto FC         | Toronto FC         | 58 | Pass            |   -   | [40.2, 19.8]    | -> Raoul Petretta |
| +16.22 |  +8.65 | 00:35:30.929 | Toronto FC         | Toronto FC         | 58 | Ball Receipt*   |   -   | [53.3, 7.3]     |  |
| +16.22 |  +8.65 | 00:35:30.929 | Toronto FC         | Toronto FC         | 58 | Carry           |   -   | [53.3, 7.3]     |  |

---

### Priority Case 36: `3998858_p130_97541a12` [regain_danger_overlap]
- **Match**: 3998858 (UEFA Women's Euro)
- **counterpressing_team**: England Women's
- **opponent_team_at_turnover**: Wales W
- **possession_team_at_counterpress_initiation**: Wales W
- **possession_id_at_counterpress_initiation**: 130
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:24:10.700) | **Initiation**: Pressure (00:24:14.871)
- **Initiation Delay**: 4.171s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.358s) | Evidence: `duel_plus_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.53 |  -5.70 | 00:24:09.171 | England Women's    | England Women's    | 129 | Pass            |   -   | [21.9, 62.5]    | Incomplete (Incomplete) |
|  +0.00 |  -4.17 | 00:24:10.700 | England Women's    | England Women's    | 129 | Ball Receipt*   |   -   | [47.2, 53.7]    | Incomplete |
|  +0.00 |  -4.17 | 00:24:10.700 | Wales W            | Wales W            | 130 | Pass            |  Yes  | [77.1, 23.8]    | -> Jessica Fishlo |
|  +0.84 |  -3.33 | 00:24:11.538 | Wales W            | Wales W            | 130 | Ball Receipt*   |   -   | [84.0, 32.7]    |  |
|  +0.84 |  -3.33 | 00:24:11.538 | Wales W            | Wales W            | 130 | Carry           |   -   | [84.0, 32.7]    |  |
|  +3.44 |  -0.73 | 00:24:14.139 | Wales W            | Wales W            | 130 | Pass            |   -   | [83.5, 34.8]    | -> Carrie Jones |
|  +4.17 |  +0.00 | 00:24:14.871 | England Women's    | Wales W            | 130 | Pressure        |  Yes  | [23.7, 31.8]    |  |
|  +4.21 |  +0.04 | 00:24:14.908 | Wales W            | Wales W            | 130 | Ball Receipt*   |   -   | [93.9, 48.1]    |  |
|  +4.21 |  +0.04 | 00:24:14.908 | Wales W            | Wales W            | 130 | Carry           |   -   | [93.9, 48.1]    |  |
|  +4.53 |  +0.36 | 00:24:15.229 | Wales W            | Wales W            | 130 | Dribble         |   -   | [95.1, 45.4]    |  |
|  +4.53 |  +0.36 | 00:24:15.229 | England Women's    | England Women's    | 131 | Duel            |  Yes  | [25.0, 34.7]    | Tackle, Success In Play |
|  +6.89 |  +2.72 | 00:24:17.592 | England Women's    | England Women's    | 131 | Pass            |   -   | [31.2, 27.1]    | -> Bethany Mead |
|  +7.97 |  +3.80 | 00:24:18.671 | England Women's    | England Women's    | 131 | Ball Receipt*   |   -   | [27.4, 18.0]    |  |
|  +7.97 |  +3.80 | 00:24:18.671 | England Women's    | England Women's    | 131 | Carry           |   -   | [27.4, 18.0]    |  |
|  +8.37 |  +4.20 | 00:24:19.072 | Wales W            | England Women's    | 131 | Pressure        |  Yes  | [89.9, 62.9]    |  |
|  +8.98 |  +4.81 | 00:24:19.682 | England Women's    | England Women's    | 131 | Pass            |   -   | [27.9, 18.8]    | -> Alex Greenwood |
|  +9.77 |  +5.60 | 00:24:20.473 | England Women's    | England Women's    | 131 | Ball Receipt*   |   -   | [20.2, 25.4]    |  |
|  +9.77 |  +5.60 | 00:24:20.473 | England Women's    | England Women's    | 131 | Carry           |   -   | [20.2, 25.4]    |  |
|  +9.85 |  +5.68 | 00:24:20.553 | England Women's    | England Women's    | 131 | Pass            |   -   | [20.2, 25.4]    | -> Georgia Stanwa |
| +10.85 |  +6.68 | 00:24:21.552 | England Women's    | England Women's    | 131 | Ball Receipt*   |   -   | [36.1, 22.5]    |  |
| +10.85 |  +6.68 | 00:24:21.552 | England Women's    | England Women's    | 131 | Carry           |   -   | [36.1, 22.5]    |  |
| +11.41 |  +7.24 | 00:24:22.111 | Wales W            | England Women's    | 131 | Pressure        |   -   | [81.0, 59.6]    |  |
| +12.13 |  +7.96 | 00:24:22.835 | Wales W            | England Women's    | 131 | Foul Committed  |   -   | [83.6, 58.2]    |  |
| +12.13 |  +7.96 | 00:24:22.835 | England Women's    | England Women's    | 131 | Foul Won        |   -   | [36.5, 21.9]    |  |
| +24.67 | +20.50 | 00:24:35.369 | England Women's    | England Women's    | 132 | Pass            |   -   | [38.6, 25.0]    | -> Jessica Carter |
| +26.17 | +22.00 | 00:24:36.867 | England Women's    | England Women's    | 132 | Ball Receipt*   |   -   | [29.1, 34.7]    |  |

---

### Priority Case 37: `3802805_p92_835a9886` [regain_danger_overlap]
- **Match**: 3802805 (Ligue 1)
- **counterpressing_team**: OGC Nice
- **opponent_team_at_turnover**: Paris Saint-Germain
- **possession_team_at_counterpress_initiation**: Paris Saint-Germain
- **possession_id_at_counterpress_initiation**: 92
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:40:26.550) | **Initiation**: Pressure (00:40:28.264)
- **Initiation Delay**: 1.714s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.966s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.00 |  -2.71 | 00:40:25.554 | Paris Saint-Germai | Paris Saint-Germai | 90 | Carry           |   -   | [71.5, 32.0]    |  |
|  -0.31 |  -2.03 | 00:40:26.238 | OGC Nice           | Paris Saint-Germai | 90 | Pressure        |  Yes  | [48.6, 48.1]    |  |
|  +0.00 |  -1.71 | 00:40:26.550 | Paris Saint-Germai | Paris Saint-Germai | 91 | Pass            |   -   | [71.5, 32.4]    | -> Lionel Andrés  |
|  +0.50 |  -1.22 | 00:40:27.047 | Paris Saint-Germai | Paris Saint-Germai | 91 | Ball Receipt*   |   -   | [76.9, 36.1]    |  |
|  +0.50 |  -1.22 | 00:40:27.047 | Paris Saint-Germai | Paris Saint-Germai | 91 | Carry           |   -   | [76.9, 36.1]    |  |
|  +0.63 |  -1.09 | 00:40:27.179 | Paris Saint-Germai | Paris Saint-Germai | 92 | Pass            |   -   | [75.8, 34.4]    | -> Marco Verratti |
|  +1.71 |  +0.00 | 00:40:28.264 | OGC Nice           | Paris Saint-Germai | 92 | Pressure        |  Yes  | [43.5, 57.5]    |  |
|  +1.72 |  +0.00 | 00:40:28.266 | Paris Saint-Germai | Paris Saint-Germai | 92 | Ball Receipt*   |   -   | [76.6, 22.6]    |  |
|  +1.72 |  +0.00 | 00:40:28.266 | Paris Saint-Germai | Paris Saint-Germai | 92 | Carry           |   -   | [76.6, 22.6]    |  |
|  +2.23 |  +0.51 | 00:40:28.777 | Paris Saint-Germai | Paris Saint-Germai | 93 | Pass            |   -   | [76.6, 22.6]    | -> Lionel Andrés  |
|  +2.83 |  +1.12 | 00:40:29.384 | Paris Saint-Germai | Paris Saint-Germai | 93 | Ball Receipt*   |   -   | [79.2, 27.5]    |  |
|  +2.83 |  +1.12 | 00:40:29.384 | Paris Saint-Germai | Paris Saint-Germai | 93 | Carry           |   -   | [79.2, 27.5]    |  |
|  +3.51 |  +1.79 | 00:40:30.058 | Paris Saint-Germai | Paris Saint-Germai | 94 | Pass            |   -   | [81.3, 24.7]    | Incomplete (Incomplete) |
|  +3.78 |  +2.06 | 00:40:30.326 | Paris Saint-Germai | Paris Saint-Germai | 94 | Ball Receipt*   |   -   | [93.1, 22.0]    | Incomplete |
|  +3.78 |  +2.06 | 00:40:30.326 | OGC Nice           | Paris Saint-Germai | 94 | Block           |  Yes  | [34.3, 57.5]    |  |
|  +6.68 |  +4.97 | 00:40:33.230 | OGC Nice           | OGC Nice           | 95 | Ball Recovery   |   -   | [41.8, 77.4]    |  |
|  +6.68 |  +4.97 | 00:40:33.230 | OGC Nice           | OGC Nice           | 95 | Carry           |   -   | [41.8, 77.4]    |  |
|  +6.95 |  +5.23 | 00:40:33.496 | Paris Saint-Germai | OGC Nice           | 95 | Pressure        |  Yes  | [77.7, 2.9]     |  |
|  +7.64 |  +5.93 | 00:40:34.191 | OGC Nice           | OGC Nice           | 95 | Dispossessed    |   -   | [43.8, 77.4]    |  |
|  +7.64 |  +5.93 | 00:40:34.191 | Paris Saint-Germai | OGC Nice           | 95 | Duel            |  Yes  | [76.3, 2.7]     | Tackle, Lost Out |
| +29.24 | +27.53 | 00:40:55.792 | OGC Nice           | OGC Nice           | 96 | Pass            |   -   | [43.9, 80.0]    | -> Kasper Dolberg |
| +29.87 | +28.15 | 00:40:56.417 | Paris Saint-Germai | OGC Nice           | 96 | Pressure        |   -   | [63.6, 4.2]     |  |

---

### Priority Case 38: `3893819_p175_a0c43844` [regain_danger_overlap]
- **Match**: 3893819 (Women's World Cup)
- **counterpressing_team**: Korea Republic Women's
- **opponent_team_at_turnover**: Morocco Women's
- **possession_team_at_counterpress_initiation**: Morocco Women's
- **possession_id_at_counterpress_initiation**: 175
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:26:44.087) | **Initiation**: Dribbled Past (00:26:48.805)
- **Initiation Delay**: 4.718s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 4.685s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.34 |  -6.05 | 00:26:42.751 | Morocco Women's    | Korea Republic Wom | 174 | Pressure        |   -   | [64.0, 30.3]    |  |
|  -0.08 |  -4.80 | 00:26:44.010 | Korea Republic Wom | Korea Republic Wom | 174 | Pressure        |   -   | [53.3, 43.1]    |  |
|  +0.00 |  -4.72 | 00:26:44.087 | Morocco Women's    | Morocco Women's    | 175 | Pass            |   -   | [66.8, 37.0]    | -> Ibtissam Jraïd |
|  +1.48 |  -3.24 | 00:26:45.565 | Morocco Women's    | Morocco Women's    | 175 | Ball Receipt*   |   -   | [74.5, 23.9]    |  |
|  +1.48 |  -3.24 | 00:26:45.565 | Morocco Women's    | Morocco Women's    | 175 | Carry           |   -   | [74.5, 23.9]    |  |
|  +4.72 |  +0.00 | 00:26:48.805 | Korea Republic Wom | Morocco Women's    | 175 | Dribbled Past   |  Yes  | [30.9, 50.0]    |  |
|  +4.72 |  +0.00 | 00:26:48.805 | Morocco Women's    | Morocco Women's    | 175 | Dribble         |   -   | [89.2, 30.1]    |  |
|  +4.72 |  +0.00 | 00:26:48.805 | Morocco Women's    | Morocco Women's    | 175 | Carry           |   -   | [89.2, 30.1]    |  |
|  +6.83 |  +2.11 | 00:26:50.914 | Morocco Women's    | Morocco Women's    | 175 | Pass            |   -   | [92.2, 38.9]    | Incomplete (Incomplete) |
|  +6.97 |  +2.25 | 00:26:51.059 | Korea Republic Wom | Morocco Women's    | 175 | Block           |   -   | [26.8, 39.5]    |  |
|  +9.40 |  +4.68 | 00:26:53.490 | Korea Republic Wom | Korea Republic Wom | 176 | Ball Recovery   |   -   | [35.6, 43.6]    |  |
|  +9.40 |  +4.68 | 00:26:53.490 | Korea Republic Wom | Korea Republic Wom | 176 | Carry           |   -   | [35.6, 43.6]    |  |
|  +9.49 |  +4.77 | 00:26:53.572 | Morocco Women's    | Korea Republic Wom | 176 | Pressure        |  Yes  | [81.1, 33.5]    |  |
| +13.15 |  +8.43 | 00:26:57.239 | Morocco Women's    | Korea Republic Wom | 176 | Foul Committed  |  Yes  | [71.9, 21.1]    |  |
| +13.15 |  +8.43 | 00:26:57.239 | Korea Republic Wom | Korea Republic Wom | 176 | Foul Won        |   -   | [48.2, 59.0]    |  |
| +64.01 | +59.29 | 00:27:48.095 | Morocco Women's    | Korea Republic Wom | 176 | Substitution    |   -   | -               |  |
| +97.31 | +92.59 | 00:28:21.397 | Korea Republic Wom | Korea Republic Wom | 177 | Pass            |   -   | [53.7, 54.5]    | Incomplete (Incomplete) |

---

### Priority Case 39: `3788754_p52_796d3382` [regain_danger_overlap]
- **Match**: 3788754 (UEFA Euro)
- **counterpressing_team**: Switzerland
- **opponent_team_at_turnover**: Italy
- **possession_team_at_counterpress_initiation**: Italy
- **possession_id_at_counterpress_initiation**: 52
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:32:21.854) | **Initiation**: Pressure (00:32:25.722)
- **Initiation Delay**: 3.868s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 0.165s) | Evidence: `duel_plus_pass` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.51 |  -5.38 | 00:32:20.342 | Switzerland        | Switzerland        | 51 | Pass            |   -   | [55.4, 80.0]    | Incomplete (Incomplete) |
|  +0.00 |  -3.87 | 00:32:21.854 | Switzerland        | Switzerland        | 51 | Ball Receipt*   |   -   | [70.4, 67.0]    | Incomplete |
|  +0.00 |  -3.87 | 00:32:21.854 | Italy              | Italy              | 52 | Pass            |   -   | [48.3, 14.6]    | -> Ciro Immobile |
|  +1.49 |  -2.38 | 00:32:23.346 | Italy              | Italy              | 52 | Ball Receipt*   |   -   | [71.9, 10.1]    |  |
|  +1.49 |  -2.38 | 00:32:23.346 | Italy              | Italy              | 52 | Pass            |   -   | [71.9, 10.1]    | -> Lorenzo Insign |
|  +3.12 |  -0.74 | 00:32:24.979 | Italy              | Italy              | 52 | Ball Receipt*   |   -   | [77.7, 3.3]     |  |
|  +3.12 |  -0.74 | 00:32:24.979 | Italy              | Italy              | 52 | Carry           |   -   | [77.7, 3.3]     |  |
|  +3.87 |  +0.00 | 00:32:25.722 | Switzerland        | Italy              | 52 | Pressure        |  Yes  | [36.3, 76.0]    |  |
|  +4.03 |  +0.16 | 00:32:25.887 | Italy              | Italy              | 52 | Dispossessed    |   -   | [83.3, 2.6]     |  |
|  +4.03 |  +0.16 | 00:32:25.887 | Switzerland        | Switzerland        | 53 | Duel            |  Yes  | [36.8, 77.5]    | Tackle, Success In Play |
|  +5.17 |  +1.31 | 00:32:27.029 | Italy              | Switzerland        | 53 | Pressure        |  Yes  | [74.3, 3.6]     |  |
|  +5.84 |  +1.97 | 00:32:27.691 | Switzerland        | Switzerland        | 53 | Pass            |   -   | [45.2, 77.0]    | Incomplete (Incomplete) |
|  +5.90 |  +2.03 | 00:32:27.756 | Italy              | Switzerland        | 53 | Block           |  Yes  | [73.4, 3.3]     |  |
| +14.65 | +10.78 | 00:32:36.504 | Switzerland        | Switzerland        | 54 | Pass            |   -   | [55.8, 80.0]    | -> Fabian Lukas S |
| +17.59 | +13.72 | 00:32:39.442 | Switzerland        | Switzerland        | 54 | Ball Receipt*   |   -   | [26.8, 59.6]    |  |
| +17.59 | +13.72 | 00:32:39.442 | Switzerland        | Switzerland        | 54 | Carry           |   -   | [26.8, 59.6]    |  |
| +19.20 | +15.33 | 00:32:41.056 | Switzerland        | Switzerland        | 54 | Pass            |   -   | [27.2, 50.5]    | -> Manuel Obafemi |
| +21.01 | +17.14 | 00:32:42.862 | Switzerland        | Switzerland        | 54 | Ball Receipt*   |   -   | [33.1, 26.5]    |  |
| +21.01 | +17.14 | 00:32:42.862 | Switzerland        | Switzerland        | 54 | Carry           |   -   | [33.1, 26.5]    |  |

---

### Priority Case 40: `3895180_p19_f72281df` [regain_danger_overlap]
- **Match**: 3895180 (1. Bundesliga)
- **counterpressing_team**: Bayer Leverkusen
- **opponent_team_at_turnover**: Eintracht Frankfurt
- **possession_team_at_counterpress_initiation**: Eintracht Frankfurt
- **possession_id_at_counterpress_initiation**: 19
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:05:21.317) | **Initiation**: Pressure (00:05:23.464)
- **Initiation Delay**: 2.147s (Quality: `high`, Latency Valid: `True`)
- **Old Annotation Labels**: Regain 5s: `1` | 3-Class: `dangerous_escape`
- **New Controlled Labels**: Regain 5s: `1` (time: 3.277s) | Evidence: `ball_recovery_plus_carry` | 3-Class: `dangerous_escape`
- **Human Verification**: `human_counterpress_valid`: [ ] | `human_turnover_valid`: [ ] | `human_regain_5s`: [ ] | `human_dangerous_escape_15s`: [ ] | `human_outcome_3class`: [ ]

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.89 |  -6.03 | 00:05:17.431 | Bayer Leverkusen   | Bayer Leverkusen   | 18 | Carry           |   -   | [41.1, 23.1]    |  |
|  -0.60 |  -2.74 | 00:05:20.721 | Bayer Leverkusen   | Bayer Leverkusen   | 18 | Pass            |   -   | [34.3, 33.7]    | Incomplete (Incomplete) |
|  +0.00 |  -2.15 | 00:05:21.317 | Bayer Leverkusen   | Bayer Leverkusen   | 18 | Ball Receipt*   |   -   | [55.0, 53.1]    | Incomplete |
|  +0.00 |  -2.15 | 00:05:21.317 | Eintracht Frankfur | Eintracht Frankfur | 19 | Interception    |  Yes  | [70.6, 30.2]    | Won |
|  +0.00 |  -2.15 | 00:05:21.317 | Eintracht Frankfur | Eintracht Frankfur | 19 | Carry           |   -   | [70.6, 30.2]    |  |
|  +2.15 |  +0.00 | 00:05:23.464 | Bayer Leverkusen   | Eintracht Frankfur | 19 | Pressure        |  Yes  | [41.1, 49.3]    |  |
|  +2.83 |  +0.68 | 00:05:24.144 | Eintracht Frankfur | Eintracht Frankfur | 19 | Pass            |   -   | [79.4, 28.3]    | -> Fares Chaïbi |
|  +3.44 |  +1.29 | 00:05:24.754 | Eintracht Frankfur | Eintracht Frankfur | 19 | Ball Receipt*   |   -   | [87.5, 30.8]    |  |
|  +3.44 |  +1.29 | 00:05:24.754 | Eintracht Frankfur | Eintracht Frankfur | 19 | Carry           |   -   | [87.5, 30.8]    |  |
|  +3.49 |  +1.34 | 00:05:24.802 | Eintracht Frankfur | Eintracht Frankfur | 19 | Pass            |   -   | [87.0, 31.2]    | -> Ansgar Knauff |
|  +3.95 |  +1.81 | 00:05:25.272 | Eintracht Frankfur | Eintracht Frankfur | 19 | Ball Receipt*   |   -   | [79.4, 31.4]    |  |
|  +3.95 |  +1.81 | 00:05:25.272 | Eintracht Frankfur | Eintracht Frankfur | 19 | Carry           |   -   | [79.4, 31.4]    |  |
|  +4.38 |  +2.23 | 00:05:25.696 | Eintracht Frankfur | Eintracht Frankfur | 19 | Miscontrol      |   -   | [79.4, 31.2]    |  |
|  +5.02 |  +2.87 | 00:05:26.334 | Eintracht Frankfur | Eintracht Frankfur | 19 | Pressure        |   -   | [82.0, 29.1]    |  |
|  +5.42 |  +3.28 | 00:05:26.741 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Ball Recovery   |   -   | [33.1, 54.2]    |  |
|  +5.42 |  +3.28 | 00:05:26.741 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Carry           |   -   | [33.1, 54.2]    |  |
|  +5.88 |  +3.73 | 00:05:27.195 | Eintracht Frankfur | Bayer Leverkusen   | 20 | Dribbled Past   |  Yes  | [85.8, 27.6]    |  |
|  +5.88 |  +3.73 | 00:05:27.195 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Dribble         |   -   | [34.3, 52.5]    |  |
|  +5.88 |  +3.73 | 00:05:27.195 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Carry           |   -   | [34.3, 52.5]    |  |
|  +7.31 |  +5.16 | 00:05:28.624 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Pass            |   -   | [36.2, 51.8]    | -> Jonas Hofmann |
|  +8.05 |  +5.90 | 00:05:29.362 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Ball Receipt*   |   -   | [44.0, 55.4]    |  |
|  +8.05 |  +5.90 | 00:05:29.362 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Carry           |   -   | [44.0, 55.4]    |  |
|  +9.05 |  +6.91 | 00:05:30.369 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Pass            |   -   | [45.9, 55.4]    | Incomplete (Incomplete) |
|  +9.24 |  +7.09 | 00:05:30.554 | Bayer Leverkusen   | Bayer Leverkusen   | 20 | Ball Receipt*   |   -   | [56.9, 74.2]    | Incomplete |
|  +9.24 |  +7.09 | 00:05:30.554 | Eintracht Frankfur | Bayer Leverkusen   | 20 | Block           |  Yes  | [69.3, 20.4]    |  |
| +11.11 |  +8.96 | 00:05:32.426 | Eintracht Frankfur | Bayer Leverkusen   | 20 | Pass            |   -   | [70.6, 11.1]    | Incomplete (Out) |
| +20.45 | +18.30 | 00:05:41.767 | Bayer Leverkusen   | Bayer Leverkusen   | 21 | Pass            |   -   | [26.9, 80.0]    | -> Granit Xhaka |

---
