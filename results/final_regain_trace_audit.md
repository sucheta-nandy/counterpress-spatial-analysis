# Final Controlled Regain Trace Audit Report (Iteration 2.7)

**Cohort**: 100 Stratified Positive Counterpress Regains (`regain_5s_controlled = 1`)
**Audit Execution Time**: 2026-09-18 16:23:00

## Stratification Schema
- **Ball Recovery + Control**: 25 episodes
- **Duel + Control**: 20 episodes
- **Interception + Control**: 15 episodes
- **New Possession + Control**: 20 episodes
- **Other / Opponent Turnover + Control**: 20 episodes

> [!IMPORTANT]
> All human verification fields in this report are strictly unpopulated placeholders for scientific auditing.

---

### Case 1: Episode `3857295_p55_fcbf806d`
- **Match**: `3857295` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Costa Rica** vs Possessing Team: **Costa Rica**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1754.58s` | Acquisition dt: `3.061s` | Control dt: `3.061s` | Regain dt: `3.061s`
- **Control Event**: `Carry` (ID: `b0a657bb-3754-4331-b951-79709c2826aa`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.061s)
  [ ] Controlled-possession verified (ctrl: 3.061s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.74 |  -3.92 | 00:29:10.664 | Costa Rica         | Costa Rica         | 55 | Pass            |   -   | [33.1, 31.2]    | Incomplete (Incomplete) |
|  +0.00 |  -1.17 | 00:29:13.408 | Japan              | Costa Rica         | 55 | Ball Recovery   |   -   | [79.2, 43.6]    |  |
|  +0.00 |  -1.17 | 00:29:13.408 | Japan              | Costa Rica         | 55 | Carry           |   -   | [79.2, 43.6]    | Carry under control |
|  +1.17 |  +0.00 | 00:29:14.581 | Costa Rica         | Costa Rica         | 55 | Pressure        |  Yes  | [43.2, 37.4]    |  |
|  +2.91 |  +1.73 | 00:29:16.315 | Costa Rica         | Costa Rica         | 55 | Pressure        |  Yes  | [38.8, 47.8]    |  |
|  +3.14 |  +1.97 | 00:29:16.548 | Japan              | Costa Rica         | 55 | Pass            |   -   | [81.0, 32.3]    | Incomplete (Incomplete) |
|  +3.24 |  +2.07 | 00:29:16.651 | Costa Rica         | Costa Rica         | 55 | Block           |  Yes  | [39.1, 48.8]    |  |
|  +4.23 |  +3.06 | 00:29:17.642 | Costa Rica         | Costa Rica         | 55 | Ball Recovery   |   -   | [40.7, 58.7]    |  |
|  +4.23 |  +3.06 | 00:29:17.642 | Costa Rica         | Costa Rica         | 55 | Carry           |   -   | [40.7, 58.7]    | Carry under control |
|  +6.44 |  +5.26 | 00:29:19.845 | Costa Rica         | Costa Rica         | 55 | Pass            |   -   | [42.5, 54.0]    | -> Joel Nathaniel |
|  +6.85 |  +5.67 | 00:29:20.253 | Japan              | Costa Rica         | 55 | Pressure        |   -   | [76.1, 32.9]    |  |
|  +6.94 |  +5.77 | 00:29:20.350 | Costa Rica         | Costa Rica         | 55 | Ball Receipt*   |   -   | [44.2, 47.4]    |  |
|  +6.94 |  +5.77 | 00:29:20.350 | Costa Rica         | Costa Rica         | 55 | Carry           |   -   | [44.2, 47.4]    | Carry under control |

---

### Case 2: Episode `3998849_p156_3ed428e9`
- **Match**: `3998849` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2982.66s` | Acquisition dt: `3.378s` | Control dt: `3.378s` | Regain dt: `3.378s`
- **Control Event**: `Carry` (ID: `19995ff9-6bed-4f5e-a1b5-4d987aa0d415`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.378s)
  [ ] Controlled-possession verified (ctrl: 3.378s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.78 | 00:49:41.888 | Germany Women's    | Germany Women's    | 156 | Dispossessed    |   -   | [43.8, 39.3]    | Opponent Dispossessed |
|  +0.00 |  -0.78 | 00:49:41.888 | Denmark Women's    | Germany Women's    | 156 | Duel            |   -   | [76.3, 40.8]    | Tackle, Won |
|  +0.00 |  -0.78 | 00:49:41.888 | Denmark Women's    | Germany Women's    | 156 | Carry           |   -   | [76.3, 40.8]    | Carry under control |
|  +0.78 |  +0.00 | 00:49:42.663 | Germany Women's    | Germany Women's    | 156 | Pressure        |  Yes  | [48.3, 43.8]    |  |
|  +1.29 |  +0.51 | 00:49:43.176 | Denmark Women's    | Germany Women's    | 156 | Pass            |   -   | [71.6, 33.4]    | -> Josefine Hasbo |
|  +2.37 |  +1.59 | 00:49:44.253 | Denmark Women's    | Germany Women's    | 156 | Ball Receipt*   |   -   | [63.6, 36.3]    |  |
|  +2.37 |  +1.59 | 00:49:44.253 | Denmark Women's    | Germany Women's    | 156 | Carry           |   -   | [63.6, 36.3]    | Carry under control |
|  +2.45 |  +1.68 | 00:49:44.338 | Denmark Women's    | Germany Women's    | 156 | Pass            |   -   | [63.2, 36.4]    | Incomplete (Incomplete) |
|  +3.59 |  +2.81 | 00:49:45.476 | Denmark Women's    | Germany Women's    | 156 | Ball Receipt*   |   -   | [71.2, 44.5]    | Incomplete |
|  +3.59 |  +2.81 | 00:49:45.476 | Germany Women's    | Germany Women's    | 156 | Interception    |  Yes  | [49.2, 37.8]    | Success In Play |
|  +4.15 |  +3.38 | 00:49:46.041 | Germany Women's    | Germany Women's    | 156 | Ball Recovery   |   -   | [47.9, 40.9]    |  |
|  +4.15 |  +3.38 | 00:49:46.041 | Germany Women's    | Germany Women's    | 156 | Carry           |   -   | [47.9, 40.9]    | Carry under control |
|  +5.29 |  +4.52 | 00:49:47.181 | Germany Women's    | Germany Women's    | 156 | Pass            |   -   | [47.7, 38.7]    | -> Sjoeke Nüsken |

---

### Case 3: Episode `3857282_p31_9f4c0bd8`
- **Match**: `3857282` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **United States** vs Possessing Team: **Wales**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1092.11s` | Acquisition dt: `2.003s` | Control dt: `2.003s` | Regain dt: `2.003s`
- **Control Event**: `Carry` (ID: `7bf74fec-85b6-48b9-8fbb-786bdc16613d`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.003s)
  [ ] Controlled-possession verified (ctrl: 2.003s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.86 |  -1.56 | 00:18:10.552 | Wales              | Wales              | 31 | Pass            |   -   | [11.8, 11.7]    | -> Aaron Ramsey |
|  +1.60 |  -0.83 | 00:18:11.287 | Wales              | Wales              | 31 | Ball Receipt*   |   -   | [21.6, 14.1]    |  |
|  +1.60 |  -0.83 | 00:18:11.287 | Wales              | Wales              | 31 | Carry           |   -   | [21.6, 14.1]    | Carry under control |
|  +2.42 |  +0.00 | 00:18:12.113 | United States      | Wales              | 31 | Pressure        |  Yes  | [99.3, 68.8]    |  |
|  +3.04 |  +0.62 | 00:18:12.735 | United States      | Wales              | 31 | Dribbled Past   |  Yes  | [99.5, 66.2]    |  |
|  +3.04 |  +0.62 | 00:18:12.735 | Wales              | Wales              | 31 | Dribble         |   -   | [20.6, 13.9]    |  |
|  +3.04 |  +0.62 | 00:18:12.735 | Wales              | Wales              | 31 | Carry           |   -   | [20.6, 13.9]    | Carry under control |
|  +3.62 |  +1.20 | 00:18:13.309 | Wales              | Wales              | 31 | Miscontrol      |   -   | [20.9, 14.0]    | Opponent Miscontrol |
|  +4.43 |  +2.00 | 00:18:14.116 | United States      | United States      | 32 | Ball Recovery   |   -   | [96.8, 67.5]    |  |
|  +4.43 |  +2.00 | 00:18:14.116 | United States      | United States      | 32 | Carry           |   -   | [96.8, 67.5]    | Carry under control |
|  +5.27 |  +2.85 | 00:18:14.959 | United States      | United States      | 32 | Pass            |   -   | [94.6, 67.3]    | -> Tyler Adams |
|  +6.21 |  +3.79 | 00:18:15.902 | United States      | United States      | 32 | Ball Receipt*   |   -   | [86.5, 55.8]    |  |
|  +6.21 |  +3.79 | 00:18:15.902 | United States      | United States      | 32 | Carry           |   -   | [86.5, 55.8]    | Carry under control |

---

### Case 4: Episode `3893814_p107_ade58806`
- **Match**: `3893814` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Italy Women's** vs Possessing Team: **Sweden Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `620.32s` | Acquisition dt: `2.623s` | Control dt: `2.623s` | Regain dt: `2.623s`
- **Control Event**: `Carry` (ID: `f400cbd6-c06d-453e-9139-bd37a9ce2f13`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.623s)
  [ ] Controlled-possession verified (ctrl: 2.623s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +3.97 |  -0.84 | 00:10:19.484 | Sweden Women's     | Sweden Women's     | 107 | Pass            |   -   | [38.8, 5.7]     | -> Elin Ingrid Jo |
|  +4.64 |  -0.17 | 00:10:20.157 | Sweden Women's     | Sweden Women's     | 107 | Ball Receipt*   |   -   | [43.7, 17.5]    |  |
|  +4.64 |  -0.17 | 00:10:20.157 | Sweden Women's     | Sweden Women's     | 107 | Carry           |   -   | [43.7, 17.5]    | Carry under control |
|  +4.81 |  +0.00 | 00:10:20.324 | Italy Women's      | Sweden Women's     | 107 | Pressure        |  Yes  | [76.4, 63.7]    |  |
|  +5.24 |  +0.44 | 00:10:20.759 | Sweden Women's     | Sweden Women's     | 107 | Pass            |   -   | [45.2, 14.9]    | -> Fridolina Rolf |
|  +6.12 |  +1.31 | 00:10:21.638 | Italy Women's      | Sweden Women's     | 107 | Pressure        |   -   | [68.7, 71.4]    |  |
|  +6.14 |  +1.33 | 00:10:21.658 | Sweden Women's     | Sweden Women's     | 107 | Ball Receipt*   |   -   | [49.7, 9.2]     |  |
|  +6.14 |  +1.33 | 00:10:21.658 | Sweden Women's     | Sweden Women's     | 107 | Carry           |   -   | [49.7, 9.2]     | Carry under control |
|  +6.22 |  +1.42 | 00:10:21.739 | Sweden Women's     | Sweden Women's     | 107 | Dispossessed    |   -   | [50.5, 7.9]     | Opponent Dispossessed |
|  +6.22 |  +1.42 | 00:10:21.739 | Italy Women's      | Sweden Women's     | 107 | Duel            |   -   | [69.6, 72.2]    | Tackle, Success In Play |
|  +7.43 |  +2.62 | 00:10:22.947 | Italy Women's      | Sweden Women's     | 107 | Ball Recovery   |   -   | [76.0, 74.8]    |  |
|  +7.43 |  +2.62 | 00:10:22.947 | Italy Women's      | Sweden Women's     | 107 | Carry           |   -   | [76.0, 74.8]    | Carry under control |
|  +7.62 |  +2.82 | 00:10:23.143 | Sweden Women's     | Sweden Women's     | 107 | Pressure        |  Yes  | [44.1, 5.9]     |  |

---

### Case 5: Episode `3835323_p101_cec4bae1`
- **Match**: `3835323` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal Women's** vs Possessing Team: **Portugal Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `194.38s` | Acquisition dt: `4.387s` | Control dt: `4.387s` | Regain dt: `4.387s`
- **Control Event**: `Carry` (ID: `4e264e67-eade-4785-a8d3-0b720f1aa5df`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.387s)
  [ ] Controlled-possession verified (ctrl: 4.387s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.73 |  -0.82 | 00:03:13.563 | Portugal Women's   | Portugal Women's   | 101 | Miscontrol      |   -   | [84.2, 58.8]    | Opponent Miscontrol |
|  +0.00 |  -0.09 | 00:03:14.296 | Switzerland Women' | Portugal Women's   | 101 | Ball Recovery   |   -   | [35.0, 23.1]    |  |
|  +0.00 |  -0.09 | 00:03:14.296 | Switzerland Women' | Portugal Women's   | 101 | Carry           |   -   | [35.0, 23.1]    | Carry under control |
|  +0.09 |  +0.00 | 00:03:14.385 | Portugal Women's   | Portugal Women's   | 101 | Pressure        |  Yes  | [85.6, 56.4]    |  |
|  +1.63 |  +1.54 | 00:03:15.926 | Portugal Women's   | Portugal Women's   | 101 | Pressure        |  Yes  | [97.1, 55.8]    |  |
|  +2.66 |  +2.57 | 00:03:16.951 | Portugal Women's   | Portugal Women's   | 101 | Pressure        |  Yes  | [97.1, 55.8]    |  |
|  +2.80 |  +2.71 | 00:03:17.091 | Switzerland Women' | Portugal Women's   | 101 | Pass            |   -   | [21.9, 24.7]    | Incomplete (Incomplete) |
|  +3.03 |  +2.94 | 00:03:17.326 | Portugal Women's   | Portugal Women's   | 101 | Block           |  Yes  | [95.5, 56.0]    |  |
|  +4.48 |  +4.39 | 00:03:18.772 | Portugal Women's   | Portugal Women's   | 101 | Ball Recovery   |   -   | [97.6, 64.3]    |  |
|  +4.48 |  +4.39 | 00:03:18.772 | Portugal Women's   | Portugal Women's   | 101 | Carry           |   -   | [97.6, 64.3]    | Carry under control |
|  +6.40 |  +6.31 | 00:03:20.698 | Portugal Women's   | Portugal Women's   | 101 | Pass            |   -   | [98.7, 67.5]    | -> Diana Micaela  |
|  +8.37 |  +8.28 | 00:03:22.667 | Portugal Women's   | Portugal Women's   | 101 | Ball Receipt*   |   -   | [114.8, 65.1]   |  |
|  +8.37 |  +8.28 | 00:03:22.667 | Portugal Women's   | Portugal Women's   | 101 | Carry           |   -   | [114.8, 65.1]   | Carry under control |

---

### Case 6: Episode `3895074_p10_52efe327`
- **Match**: `3895074` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Bayern Munich** vs Possessing Team: **Bayern Munich**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `188.78s` | Acquisition dt: `1.291s` | Control dt: `1.291s` | Regain dt: `1.291s`
- **Control Event**: `Carry` (ID: `23a3e1e8-7679-4bf7-920e-8ad00c6c47c4`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.291s)
  [ ] Controlled-possession verified (ctrl: 1.291s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.11 | 00:03:08.672 | Bayer Leverkusen   | Bayer Leverkusen   | 9 | Dribble         |   -   | [56.7, 13.6]    |  |
|  +0.00 |  -0.11 | 00:03:08.672 | Bayer Leverkusen   | Bayer Leverkusen   | 9 | Carry           |   -   | [56.7, 13.6]    | Carry under control |
|  +0.11 |  +0.00 | 00:03:08.778 | Bayer Leverkusen   | Bayer Leverkusen   | 9 | Dispossessed    |   -   | [57.9, 14.3]    | Opponent Dispossessed |
|  +0.11 |  +0.00 | 00:03:08.778 | Bayern Munich      | Bayern Munich      | 10 | Duel            |  Yes  | [62.2, 65.8]    | Tackle, Success In Play |
|  +1.23 |  +1.13 | 00:03:09.906 | Bayer Leverkusen   | Bayern Munich      | 10 | Pressure        |  Yes  | [54.3, 18.0]    |  |
|  +1.40 |  +1.29 | 00:03:10.069 | Bayern Munich      | Bayern Munich      | 10 | Ball Recovery   |   -   | [65.8, 65.8]    |  |
|  +1.40 |  +1.29 | 00:03:10.069 | Bayern Munich      | Bayern Munich      | 10 | Carry           |   -   | [65.8, 65.8]    | Carry under control |
|  +2.44 |  +2.33 | 00:03:11.107 | Bayern Munich      | Bayern Munich      | 10 | Pass            |   -   | [68.2, 69.1]    | -> Leroy Sané |
|  +3.47 |  +3.36 | 00:03:12.139 | Bayern Munich      | Bayern Munich      | 10 | Ball Receipt*   |   -   | [64.3, 75.3]    |  |
|  +3.47 |  +3.36 | 00:03:12.139 | Bayern Munich      | Bayern Munich      | 10 | Pass            |   -   | [64.3, 75.3]    | -> Konrad Laimer |
|  +4.13 |  +4.02 | 00:03:12.800 | Bayern Munich      | Bayern Munich      | 10 | Ball Receipt*   |   -   | [60.0, 71.8]    |  |
|  +4.13 |  +4.02 | 00:03:12.800 | Bayern Munich      | Bayern Munich      | 10 | Carry           |   -   | [60.0, 71.8]    | Carry under control |
|  +4.91 |  +4.80 | 00:03:13.578 | Bayern Munich      | Bayern Munich      | 10 | Pass            |   -   | [59.1, 70.0]    | -> Joshua Kimmich |

---

### Case 7: Episode `3788752_p201_3a7755c6`
- **Match**: `3788752` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Hungary** vs Possessing Team: **Hungary**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2730.48s` | Acquisition dt: `1.642s` | Control dt: `1.642s` | Regain dt: `1.642s`
- **Control Event**: `Carry` (ID: `3336534c-141b-4c5b-a964-dafdc371b23d`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.642s)
  [ ] Controlled-possession verified (ctrl: 1.642s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.20 |  -1.59 | 00:45:28.888 | Hungary            | Hungary            | 201 | Pressure        |   -   | [18.6, 13.1]    |  |
|  +0.00 |  -0.39 | 00:45:30.087 | Portugal           | Hungary            | 201 | Ball Recovery   |   -   | [100.5, 68.6]   |  |
|  +0.00 |  -0.39 | 00:45:30.087 | Portugal           | Hungary            | 201 | Carry           |   -   | [100.5, 68.6]   | Carry under control |
|  +0.39 |  +0.00 | 00:45:30.482 | Hungary            | Hungary            | 201 | Pressure        |  Yes  | [18.6, 11.0]    |  |
|  +1.04 |  +0.64 | 00:45:31.125 | Portugal           | Hungary            | 201 | Dribble         |   -   | [102.3, 69.1]   |  |
|  +1.04 |  +0.64 | 00:45:31.125 | Hungary            | Hungary            | 201 | Duel            |  Yes  | [17.8, 11.0]    | Tackle, Success In Play |
|  +2.04 |  +1.64 | 00:45:32.124 | Hungary            | Hungary            | 201 | Ball Recovery   |   -   | [22.0, 9.1]     |  |
|  +2.04 |  +1.64 | 00:45:32.124 | Hungary            | Hungary            | 201 | Carry           |   -   | [22.0, 9.1]     | Carry under control |
|  +4.01 |  +3.61 | 00:45:34.096 | Hungary            | Hungary            | 201 | Pass            |   -   | [15.5, 6.9]     | Incomplete (Incomplete) |
|  +5.19 |  +4.80 | 00:45:35.281 | Portugal           | Portugal           | 202 | Ball Recovery   |   -   | [83.4, 64.9]    |  |
|  +5.19 |  +4.80 | 00:45:35.281 | Portugal           | Portugal           | 202 | Carry           |   -   | [83.4, 64.9]    | Carry under control |
|  +5.62 |  +5.22 | 00:45:35.704 | Portugal           | Portugal           | 202 | Pass            |   -   | [83.4, 64.9]    | -> Rafael Alexand |
|  +6.60 |  +6.20 | 00:45:36.687 | Portugal           | Portugal           | 202 | Ball Receipt*   |   -   | [92.2, 71.8]    |  |

---

### Case 8: Episode `3895194_p55_9783cceb`
- **Match**: `3895194` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Bayer Leverkusen** vs Possessing Team: **Bayer Leverkusen**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1640.97s` | Acquisition dt: `1.723s` | Control dt: `1.723s` | Regain dt: `1.723s`
- **Control Event**: `Carry` (ID: `138378dc-c704-44f0-a98b-4f606eeb5bb1`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.723s)
  [ ] Controlled-possession verified (ctrl: 1.723s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.44 |  -1.10 | 00:27:19.874 | Augsburg           | Bayer Leverkusen   | 55 | Pass            |   -   | [42.7, 11.2]    | -> Elvis Rexhbeça |
|  +6.13 |  -0.40 | 00:27:20.567 | Augsburg           | Bayer Leverkusen   | 55 | Ball Receipt*   |   -   | [45.8, 19.6]    |  |
|  +6.13 |  -0.40 | 00:27:20.567 | Augsburg           | Bayer Leverkusen   | 55 | Carry           |   -   | [45.8, 19.6]    | Carry under control |
|  +6.54 |  +0.00 | 00:27:20.969 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Pressure        |  Yes  | [70.7, 67.0]    |  |
|  +7.36 |  +0.83 | 00:27:21.796 | Augsburg           | Bayer Leverkusen   | 55 | Pass            |   -   | [47.5, 17.7]    | Incomplete (Incomplete) |
|  +8.26 |  +1.72 | 00:27:22.692 | Augsburg           | Bayer Leverkusen   | 55 | Ball Receipt*   |   -   | [68.0, 4.8]     | Incomplete |
|  +8.26 |  +1.72 | 00:27:22.692 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Ball Recovery   |   -   | [62.9, 65.8]    |  |
|  +8.26 |  +1.72 | 00:27:22.692 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Carry           |   -   | [62.9, 65.8]    | Carry under control |
|  +9.14 |  +2.61 | 00:27:23.575 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Pass            |   -   | [62.9, 66.4]    | -> Jonas Hofmann |
| +10.74 |  +4.21 | 00:27:25.175 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Ball Receipt*   |   -   | [76.2, 69.5]    |  |
| +10.74 |  +4.21 | 00:27:25.175 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Carry           |   -   | [76.2, 69.5]    | Carry under control |
| +13.57 |  +7.03 | 00:27:28.000 | Bayer Leverkusen   | Bayer Leverkusen   | 55 | Pass            |   -   | [79.3, 69.5]    | -> Adam Hložek |
| +14.76 |  +8.22 | 00:27:29.194 | Augsburg           | Bayer Leverkusen   | 55 | Pressure        |   -   | [36.3, 37.0]    |  |

---

### Case 9: Episode `3895167_p36_da4d28bb`
- **Match**: `3895167` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Bayer Leverkusen** vs Possessing Team: **Bayer Leverkusen**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1140.71s` | Acquisition dt: `3.29s` | Control dt: `3.29s` | Regain dt: `3.29s`
- **Control Event**: `Carry` (ID: `bdd9ff44-d636-4989-86d3-89cb4adb6e19`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.29s)
  [ ] Controlled-possession verified (ctrl: 3.29s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +3.80 |  -0.94 | 00:18:59.769 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Carry           |   -   | [91.7, 44.7]    | Carry under control |
|  +4.09 |  -0.65 | 00:19:00.064 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Pass            |   -   | [92.1, 45.1]    | Incomplete (Incomplete) |
|  +4.74 |  +0.00 | 00:19:00.712 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Ball Receipt*   |   -   | [90.0, 37.5]    | Incomplete |
|  +4.74 |  +0.00 | 00:19:00.712 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Block           |  Yes  | [27.5, 43.4]    |  |
|  +8.03 |  +3.29 | 00:19:04.002 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Ball Recovery   |   -   | [12.6, 20.0]    |  |
|  +8.03 |  +3.29 | 00:19:04.002 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Carry           |   -   | [12.6, 20.0]    | Carry under control |
|  +8.56 |  +3.82 | 00:19:04.529 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Pressure        |   -   | [109.8, 65.8]   |  |
| +10.10 |  +5.36 | 00:19:06.073 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Pass            |   -   | [7.3, 2.3]      | Incomplete (Incomplete) |
| +10.33 |  +5.59 | 00:19:06.300 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Block           |   -   | [110.2, 78.0]   |  |
| +11.48 |  +6.74 | 00:19:07.448 | VfB Stuttgart      | Bayer Leverkusen   | 36 | Pressure        |   -   | [116.0, 77.8]   |  |
| +12.21 |  +7.46 | 00:19:08.177 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Ball Recovery   |   -   | [2.4, 5.2]      |  |
| +12.21 |  +7.46 | 00:19:08.177 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Carry           |   -   | [2.4, 5.2]      | Carry under control |
| +13.70 |  +8.96 | 00:19:09.668 | Bayer Leverkusen   | Bayer Leverkusen   | 36 | Pass            |   -   | [4.6, 10.5]     | -> Amine Adli |

---

### Case 10: Episode `3857300_p53_81f557ef`
- **Match**: `3857300` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Argentina** vs Possessing Team: **Argentina**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2044.22s` | Acquisition dt: `1.022s` | Control dt: `1.022s` | Regain dt: `1.022s`
- **Control Event**: `Carry` (ID: `d3ff9f7b-7065-4492-83ae-a80d796c17da`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.022s)
  [ ] Controlled-possession verified (ctrl: 1.022s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +7.44 |  -0.49 | 00:34:03.731 | Saudi Arabia       | Saudi Arabia       | 52 | Carry           |   -   | [70.0, 13.0]    | Carry under control |
|  +7.48 |  -0.44 | 00:34:03.774 | Saudi Arabia       | Saudi Arabia       | 52 | Pass            |   -   | [70.0, 13.0]    | Incomplete (Incomplete) |
|  +7.92 |  +0.00 | 00:34:04.217 | Saudi Arabia       | Saudi Arabia       | 52 | Ball Receipt*   |   -   | [64.5, 7.0]     | Incomplete |
|  +7.92 |  +0.00 | 00:34:04.217 | Argentina          | Argentina          | 53 | Pass            |  Yes  | [53.2, 70.5]    | -> Rodrigo Javier |
|  +8.06 |  +0.14 | 00:34:04.355 | Argentina          | Argentina          | 53 | Ball Receipt*   |   -   | [52.6, 65.0]    |  |
|  +8.06 |  +0.14 | 00:34:04.355 | Argentina          | Argentina          | 53 | Carry           |   -   | [52.6, 65.0]    | Carry under control |
|  +8.22 |  +0.30 | 00:34:04.515 | Argentina          | Argentina          | 53 | Miscontrol      |   -   | [52.6, 65.0]    | Opponent Miscontrol |
|  +8.94 |  +1.02 | 00:34:05.239 | Argentina          | Argentina          | 53 | Ball Recovery   |   -   | [56.7, 72.5]    |  |
|  +8.94 |  +1.02 | 00:34:05.239 | Argentina          | Argentina          | 53 | Carry           |   -   | [56.7, 72.5]    | Carry under control |
|  +9.54 |  +1.62 | 00:34:05.837 | Argentina          | Argentina          | 53 | Pass            |   -   | [57.6, 66.1]    | -> Lionel Andrés  |
| +10.66 |  +2.74 | 00:34:06.953 | Argentina          | Argentina          | 53 | Ball Receipt*   |   -   | [68.5, 53.7]    |  |
| +10.66 |  +2.74 | 00:34:06.953 | Argentina          | Argentina          | 53 | Carry           |   -   | [68.5, 53.7]    | Carry under control |
| +12.85 |  +4.93 | 00:34:09.147 | Argentina          | Argentina          | 53 | Pass            |   -   | [80.6, 41.7]    | Incomplete (Pass Offside) |

---

### Case 11: Episode `3998852_p67_a575aa1c`
- **Match**: `3998852` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **WNT Finland** vs Possessing Team: **WNT Finland**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1797.96s` | Acquisition dt: `2.328s` | Control dt: `2.328s` | Regain dt: `2.328s`
- **Control Event**: `Carry` (ID: `940d4e79-3eb0-46c2-954f-9280e48aa79f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.328s)
  [ ] Controlled-possession verified (ctrl: 2.328s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.80 | 00:29:57.159 | WNT Finland        | WNT Finland        | 67 | Ball Receipt*   |   -   | [57.3, 49.8]    | Incomplete |
|  +0.00 |  -0.80 | 00:29:57.159 | Switzerland Women' | WNT Finland        | 67 | Interception    |   -   | [67.3, 33.4]    | Won |
|  +0.00 |  -0.80 | 00:29:57.159 | Switzerland Women' | WNT Finland        | 67 | Carry           |   -   | [67.3, 33.4]    | Carry under control |
|  +0.80 |  +0.00 | 00:29:57.963 | WNT Finland        | WNT Finland        | 67 | Pressure        |  Yes  | [54.0, 52.6]    |  |
|  +1.42 |  +0.61 | 00:29:58.575 | Switzerland Women' | WNT Finland        | 67 | Pass            |   -   | [68.7, 28.3]    | Incomplete (Incomplete) |
|  +3.13 |  +2.33 | 00:30:00.291 | WNT Finland        | WNT Finland        | 67 | Ball Recovery   |   -   | [39.0, 51.2]    |  |
|  +3.13 |  +2.33 | 00:30:00.291 | WNT Finland        | WNT Finland        | 67 | Carry           |   -   | [39.0, 51.2]    | Carry under control |
|  +5.97 |  +5.17 | 00:30:03.133 | WNT Finland        | WNT Finland        | 67 | Pass            |   -   | [45.6, 58.6]    | -> Emma Wilhelmin |
|  +7.35 |  +6.55 | 00:30:04.513 | WNT Finland        | WNT Finland        | 67 | Ball Receipt*   |   -   | [42.5, 69.7]    |  |
|  +7.35 |  +6.55 | 00:30:04.513 | WNT Finland        | WNT Finland        | 67 | Carry           |   -   | [42.5, 69.7]    | Carry under control |
|  +8.50 |  +7.70 | 00:30:05.660 | WNT Finland        | WNT Finland        | 67 | Pass            |   -   | [44.9, 71.3]    | -> Linda Sällströ |
|  +9.81 |  +9.00 | 00:30:06.965 | WNT Finland        | WNT Finland        | 67 | Ball Receipt*   |   -   | [63.2, 77.9]    |  |
|  +9.81 |  +9.00 | 00:30:06.965 | WNT Finland        | WNT Finland        | 67 | Carry           |   -   | [63.2, 77.9]    | Carry under control |

---

### Case 12: Episode `3930163_p82_43d968ea`
- **Match**: `3930163` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Serbia** vs Possessing Team: **Serbia**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_pass`
- **Timestamps**: Initiation: `666.33s` | Acquisition dt: `0.626s` | Control dt: `1.905s` | Regain dt: `1.905s`
- **Control Event**: `Pass` (ID: `c6d99fec-0d98-4241-9436-d52f6453a73f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.626s)
  [ ] Controlled-possession verified (ctrl: 1.905s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.85 |  -0.90 | 00:11:05.426 | England            | England            | 81 | Ball Receipt*   |   -   | [106.1, 44.9]   |  |
|  +0.85 |  -0.90 | 00:11:05.426 | England            | England            | 81 | Carry           |   -   | [106.1, 44.9]   | Carry under control |
|  +1.76 |  +0.00 | 00:11:06.330 | England            | England            | 81 | Dribble         |   -   | [111.1, 43.6]   |  |
|  +1.76 |  +0.00 | 00:11:06.330 | Serbia             | Serbia             | 82 | Duel            |  Yes  | [9.0, 36.5]     | Tackle, Success In Play |
|  +2.38 |  +0.63 | 00:11:06.956 | Serbia             | Serbia             | 82 | Ball Recovery   |   -   | [15.0, 32.0]    |  |
|  +3.66 |  +1.90 | 00:11:08.235 | Serbia             | Serbia             | 82 | Pass            |   -   | [18.7, 30.6]    | -> Sergej Milinko |
|  +4.58 |  +2.83 | 00:11:09.156 | Serbia             | Serbia             | 82 | Ball Receipt*   |   -   | [20.0, 22.1]    |  |
|  +5.09 |  +3.33 | 00:11:09.664 | Serbia             | Serbia             | 82 | Pass            |   -   | [23.3, 22.9]    | -> Andrija Živkov |
|  +8.06 |  +6.30 | 00:11:12.635 | England            | Serbia             | 82 | Pressure        |   -   | [96.4, 12.8]    |  |
|  +8.62 |  +6.87 | 00:11:13.197 | Serbia             | Serbia             | 82 | Ball Receipt*   |   -   | [22.0, 70.4]    |  |
|  +8.62 |  +6.87 | 00:11:13.197 | Serbia             | Serbia             | 82 | Carry           |   -   | [22.0, 70.4]    | Carry under control |
|  +8.64 |  +6.89 | 00:11:13.218 | Serbia             | Serbia             | 82 | Pass            |   -   | [21.2, 72.0]    | -> Milos Veljkovi |
| +10.18 |  +8.42 | 00:11:14.752 | Serbia             | Serbia             | 82 | Ball Receipt*   |   -   | [9.4, 63.8]     |  |

---

### Case 13: Episode `3930167_p23_a617aea6`
- **Match**: `3930167` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Possessing Team: **Croatia**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `969.79s` | Acquisition dt: `1.128s` | Control dt: `1.128s` | Regain dt: `1.128s`
- **Control Event**: `Carry` (ID: `0480162a-c620-473c-84a2-4b887e336963`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.128s)
  [ ] Controlled-possession verified (ctrl: 1.128s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.54 |  -2.54 | 00:16:07.257 | Albania            | Albania            | 22 | Carry           |   -   | [50.6, 8.7]     | Carry under control |
|  -0.48 |  -0.48 | 00:16:09.310 | Croatia            | Albania            | 22 | Pressure        |   -   | [78.7, 70.8]    |  |
|  +0.00 |  +0.00 | 00:16:09.792 | Albania            | Albania            | 22 | Dispossessed    |   -   | [39.7, 10.4]    | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:16:09.792 | Croatia            | Croatia            | 23 | Duel            |  Yes  | [80.4, 69.7]    | Tackle, Success In Play |
|  +1.13 |  +1.13 | 00:16:10.920 | Croatia            | Croatia            | 23 | Ball Recovery   |   -   | [86.2, 62.5]    |  |
|  +1.13 |  +1.13 | 00:16:10.920 | Croatia            | Croatia            | 23 | Carry           |   -   | [86.2, 62.5]    | Carry under control |
|  +1.58 |  +1.58 | 00:16:11.374 | Croatia            | Croatia            | 23 | Pass            |   -   | [91.8, 65.0]    | Incomplete (Incomplete) |
|  +2.09 |  +2.09 | 00:16:11.885 | Croatia            | Croatia            | 23 | Ball Receipt*   |   -   | [98.1, 54.9]    | Incomplete |
|  +2.09 |  +2.09 | 00:16:11.885 | Albania            | Croatia            | 23 | Block           |  Yes  | [26.5, 18.7]    |  |
| +32.23 | +32.23 | 00:16:42.023 | Croatia            | Croatia            | 24 | Pass            |   -   | [102.9, 80.0]   | Incomplete (Incomplete) |
| +34.00 | +34.00 | 00:16:43.797 | Croatia            | Croatia            | 24 | Ball Receipt*   |   -   | [111.8, 47.5]   | Incomplete |
| +34.00 | +34.00 | 00:16:43.797 | Albania            | Croatia            | 24 | Clearance       |   -   | [8.7, 29.9]     |  |
| +35.88 | +35.88 | 00:16:45.669 | Albania            | Croatia            | 24 | Clearance       |   -   | [16.9, 41.3]    |  |

---

### Case 14: Episode `3802802_p150_aca7c73a`
- **Match**: `3802802` (Ligue 1) | **Period**: 2
- **Counterpressing Team**: **Stade de Reims** vs Possessing Team: **Stade de Reims**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1522.59s` | Acquisition dt: `1.843s` | Control dt: `1.843s` | Regain dt: `1.843s`
- **Control Event**: `Carry` (ID: `443e4ba4-9b34-43fa-9ce0-c433546aca3d`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.843s)
  [ ] Controlled-possession verified (ctrl: 1.843s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.35 | 00:25:22.240 | Paris Saint-Germai | Paris Saint-Germai | 149 | Ball Receipt*   |   -   | [108.1, 72.0]   |  |
|  +0.00 |  -0.35 | 00:25:22.240 | Paris Saint-Germai | Paris Saint-Germai | 149 | Carry           |   -   | [108.1, 72.0]   | Carry under control |
|  +0.35 |  +0.00 | 00:25:22.588 | Paris Saint-Germai | Paris Saint-Germai | 149 | Dribble         |   -   | [108.6, 70.5]   |  |
|  +0.35 |  +0.00 | 00:25:22.588 | Stade de Reims     | Stade de Reims     | 150 | Duel            |  Yes  | [11.5, 9.6]     | Tackle, Success In Play |
|  +2.19 |  +1.84 | 00:25:24.431 | Stade de Reims     | Stade de Reims     | 150 | Ball Recovery   |   -   | [5.1, 7.7]      |  |
|  +2.19 |  +1.84 | 00:25:24.431 | Stade de Reims     | Stade de Reims     | 150 | Carry           |   -   | [5.1, 7.7]      | Carry under control |
|  +2.99 |  +2.64 | 00:25:25.229 | Stade de Reims     | Stade de Reims     | 150 | Pass            |   -   | [5.1, 7.7]      | Incomplete (Incomplete) |
|  +5.65 |  +5.31 | 00:25:27.894 | Stade de Reims     | Stade de Reims     | 150 | Ball Receipt*   |   -   | [44.8, 12.4]    | Incomplete |
|  +5.65 |  +5.31 | 00:25:27.894 | Paris Saint-Germai | Stade de Reims     | 150 | Pass            |   -   | [73.1, 64.5]    | Incomplete (Incomplete) |
|  +7.58 |  +7.23 | 00:25:29.821 | Paris Saint-Germai | Stade de Reims     | 150 | Ball Receipt*   |   -   | [75.1, 69.9]    | Incomplete |
|  +7.58 |  +7.23 | 00:25:29.821 | Paris Saint-Germai | Stade de Reims     | 150 | Duel            |   -   | [75.1, 69.9]    | Aerial Lost |
|  +7.58 |  +7.23 | 00:25:29.821 | Stade de Reims     | Stade de Reims     | 150 | Pass            |   -   | [45.0, 10.2]    | -> Hugo Ekitike |
|  +8.69 |  +8.34 | 00:25:30.932 | Paris Saint-Germai | Stade de Reims     | 150 | Pressure        |   -   | [60.4, 62.4]    |  |

---

### Case 15: Episode `3998837_p35_12d67dff`
- **Match**: `3998837` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Switzerland Women's** vs Possessing Team: **Switzerland Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `949.26s` | Acquisition dt: `0.701s` | Control dt: `0.701s` | Regain dt: `0.701s`
- **Control Event**: `Carry` (ID: `cc64da9c-fb2f-4cf7-a3f7-964530f2d5c6`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.701s)
  [ ] Controlled-possession verified (ctrl: 0.701s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.51 | 00:15:48.755 | Norway Women's     | Switzerland Women' | 35 | Interception    |   -   | [35.8, 12.7]    | Won |
|  +0.00 |  -0.51 | 00:15:48.755 | Norway Women's     | Switzerland Women' | 35 | Carry           |   -   | [35.8, 12.7]    | Carry under control |
|  +0.51 |  +0.00 | 00:15:49.265 | Norway Women's     | Switzerland Women' | 35 | Dribble         |   -   | [35.5, 16.9]    |  |
|  +0.51 |  +0.00 | 00:15:49.265 | Switzerland Women' | Switzerland Women' | 35 | Duel            |  Yes  | [84.6, 63.2]    | Tackle, Success In Play |
|  +1.21 |  +0.70 | 00:15:49.966 | Switzerland Women' | Switzerland Women' | 35 | Ball Recovery   |   -   | [90.8, 68.2]    |  |
|  +1.21 |  +0.70 | 00:15:49.966 | Switzerland Women' | Switzerland Women' | 35 | Carry           |   -   | [90.8, 68.2]    | Carry under control |
|  +2.64 |  +2.13 | 00:15:51.394 | Switzerland Women' | Switzerland Women' | 35 | Pass            |   -   | [92.3, 58.7]    | Incomplete (Incomplete) |
|  +3.66 |  +3.15 | 00:15:52.412 | Switzerland Women' | Switzerland Women' | 35 | Ball Receipt*   |   -   | [101.7, 43.4]   | Incomplete |
|  +3.66 |  +3.15 | 00:15:52.412 | Norway Women's     | Switzerland Women' | 35 | Interception    |   -   | [14.6, 31.0]    | Won |
|  +3.66 |  +3.15 | 00:15:52.412 | Norway Women's     | Switzerland Women' | 35 | Carry           |   -   | [14.6, 31.0]    | Carry under control |
|  +3.98 |  +3.47 | 00:15:52.735 | Switzerland Women' | Switzerland Women' | 35 | Pressure        |  Yes  | [108.0, 49.1]   |  |
|  +4.56 |  +4.05 | 00:15:53.312 | Norway Women's     | Switzerland Women' | 35 | Pass            |   -   | [11.1, 27.7]    | -> Marit Bratberg |
|  +4.91 |  +4.40 | 00:15:53.670 | Norway Women's     | Switzerland Women' | 35 | Ball Receipt*   |   -   | [16.9, 16.9]    |  |

---

### Case 16: Episode `3893813_p99_49589f0d`
- **Match**: `3893813` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Haiti Women's** vs Possessing Team: **Haiti Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `111.38s` | Acquisition dt: `3.701s` | Control dt: `3.701s` | Regain dt: `3.701s`
- **Control Event**: `Carry` (ID: `1242b941-cba7-453e-b070-740f24fe3f8e`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.701s)
  [ ] Controlled-possession verified (ctrl: 3.701s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.59 | 00:01:49.789 | China PR Women's   | China PR Women's   | 98 | Carry           |   -   | [81.0, 10.1]    | Carry under control |
|  +1.17 |  -0.42 | 00:01:50.958 | China PR Women's   | China PR Women's   | 98 | Pass            |   -   | [83.9, 10.7]    | Incomplete (Incomplete) |
|  +1.59 |  +0.00 | 00:01:51.382 | China PR Women's   | China PR Women's   | 98 | Ball Receipt*   |   -   | [84.4, 15.2]    | Incomplete |
|  +1.59 |  +0.00 | 00:01:51.382 | Haiti Women's      | Haiti Women's      | 99 | Pass            |  Yes  | [35.9, 66.6]    | -> Kethna Louis |
|  +3.31 |  +1.71 | 00:01:53.096 | Haiti Women's      | Haiti Women's      | 99 | Ball Receipt*   |   -   | [24.9, 63.4]    |  |
|  +3.31 |  +1.71 | 00:01:53.096 | Haiti Women's      | Haiti Women's      | 99 | Pass            |   -   | [24.9, 63.4]    | Incomplete (Incomplete) |
|  +4.19 |  +2.60 | 00:01:53.982 | Haiti Women's      | Haiti Women's      | 99 | Ball Receipt*   |   -   | [37.2, 62.5]    | Incomplete |
|  +4.19 |  +2.60 | 00:01:53.982 | China PR Women's   | Haiti Women's      | 99 | Block           |  Yes  | [82.5, 14.5]    |  |
|  +4.87 |  +3.27 | 00:01:54.656 | China PR Women's   | Haiti Women's      | 99 | Ball Recovery   |   -   | [83.9, 16.3]    |  |
|  +5.29 |  +3.70 | 00:01:55.083 | Haiti Women's      | Haiti Women's      | 99 | Ball Recovery   |   -   | [35.3, 62.1]    |  |
|  +5.29 |  +3.70 | 00:01:55.083 | Haiti Women's      | Haiti Women's      | 99 | Carry           |   -   | [35.3, 62.1]    | Carry under control |
|  +6.16 |  +4.57 | 00:01:55.953 | China PR Women's   | Haiti Women's      | 99 | Pressure        |  Yes  | [89.3, 22.1]    |  |
|  +6.88 |  +5.28 | 00:01:56.665 | Haiti Women's      | Haiti Women's      | 99 | Pass            |   -   | [36.6, 54.6]    | -> Melchie Daëlle |

---

### Case 17: Episode `3773474_p59_46b1d5f0`
- **Match**: `3773474` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Real Valladolid** vs Possessing Team: **Real Valladolid**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1238.43s` | Acquisition dt: `3.034s` | Control dt: `3.034s` | Regain dt: `3.034s`
- **Control Event**: `Carry` (ID: `ffbbf25b-d0af-46fc-8c91-9c1dea3836f3`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.034s)
  [ ] Controlled-possession verified (ctrl: 3.034s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -3.30 | 00:20:35.128 | Barcelona          | Real Valladolid    | 59 | Pass            |   -   | [29.9, 13.8]    | -> Marc-André ter |
|  +2.57 |  -0.73 | 00:20:37.699 | Barcelona          | Real Valladolid    | 59 | Ball Receipt*   |   -   | [8.5, 34.5]     |  |
|  +2.57 |  -0.73 | 00:20:37.699 | Barcelona          | Real Valladolid    | 59 | Carry           |   -   | [8.5, 34.5]     | Carry under control |
|  +3.30 |  +0.00 | 00:20:38.426 | Real Valladolid    | Real Valladolid    | 59 | Pressure        |  Yes  | [103.3, 49.6]   |  |
|  +4.22 |  +0.92 | 00:20:39.346 | Barcelona          | Real Valladolid    | 59 | Pass            |   -   | [11.4, 42.1]    | Incomplete (Incomplete) |
|  +6.33 |  +3.03 | 00:20:41.460 | Barcelona          | Real Valladolid    | 59 | Ball Receipt*   |   -   | [55.1, 18.3]    | Incomplete |
|  +6.33 |  +3.03 | 00:20:41.460 | Real Valladolid    | Real Valladolid    | 59 | Ball Recovery   |   -   | [72.7, 60.4]    |  |
|  +6.33 |  +3.03 | 00:20:41.460 | Real Valladolid    | Real Valladolid    | 59 | Carry           |   -   | [72.7, 60.4]    | Carry under control |
|  +6.84 |  +3.54 | 00:20:41.965 | Barcelona          | Real Valladolid    | 59 | Pressure        |   -   | [43.7, 15.7]    |  |
|  +9.15 |  +5.85 | 00:20:44.280 | Real Valladolid    | Real Valladolid    | 59 | Pass            |   -   | [66.2, 62.9]    | -> Rubén Alcaraz  |
| +10.15 |  +6.85 | 00:20:45.274 | Real Valladolid    | Real Valladolid    | 59 | Ball Receipt*   |   -   | [69.3, 52.2]    |  |
| +10.15 |  +6.85 | 00:20:45.274 | Real Valladolid    | Real Valladolid    | 59 | Carry           |   -   | [69.3, 52.2]    | Carry under control |
| +10.86 |  +7.56 | 00:20:45.984 | Real Valladolid    | Real Valladolid    | 59 | Pass            |   -   | [69.3, 52.2]    | -> José Ignacio M |

---

### Case 18: Episode `3857256_p58_d6e254db`
- **Match**: `3857256` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Serbia** vs Possessing Team: **Serbia**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1725.89s` | Acquisition dt: `3.139s` | Control dt: `3.139s` | Regain dt: `3.139s`
- **Control Event**: `Carry` (ID: `a715fcdf-02ca-4515-86c1-e5a444664e82`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.139s)
  [ ] Controlled-possession verified (ctrl: 3.139s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.89 | 00:28:45.004 | Serbia             | Serbia             | 58 | Ball Receipt*   |   -   | [79.0, 61.7]    | Incomplete |
|  +0.00 |  -0.89 | 00:28:45.004 | Switzerland        | Serbia             | 58 | Ball Recovery   |   -   | [43.9, 36.5]    |  |
|  +0.00 |  -0.89 | 00:28:45.004 | Switzerland        | Serbia             | 58 | Carry           |   -   | [43.9, 36.5]    | Carry under control |
|  +0.89 |  +0.00 | 00:28:45.892 | Serbia             | Serbia             | 58 | Pressure        |  Yes  | [72.3, 46.0]    |  |
|  +1.03 |  +0.15 | 00:28:46.038 | Switzerland        | Serbia             | 58 | Pass            |   -   | [47.8, 32.7]    | -> Remo Freuler |
|  +1.86 |  +0.97 | 00:28:46.866 | Switzerland        | Serbia             | 58 | Ball Receipt*   |   -   | [45.5, 29.1]    |  |
|  +1.86 |  +0.97 | 00:28:46.866 | Switzerland        | Serbia             | 58 | Pass            |   -   | [44.5, 29.1]    | Incomplete (Incomplete) |
|  +4.03 |  +3.14 | 00:28:49.031 | Switzerland        | Serbia             | 58 | Ball Receipt*   |   -   | [42.7, 57.6]    | Incomplete |
|  +4.03 |  +3.14 | 00:28:49.031 | Serbia             | Serbia             | 58 | Ball Recovery   |   -   | [71.1, 21.1]    |  |
|  +4.03 |  +3.14 | 00:28:49.031 | Serbia             | Serbia             | 58 | Carry           |   -   | [71.1, 21.1]    | Carry under control |
|  +7.65 |  +6.76 | 00:28:52.652 | Switzerland        | Serbia             | 58 | Pressure        |   -   | [32.3, 60.6]    |  |
|  +8.87 |  +7.98 | 00:28:53.872 | Switzerland        | Serbia             | 58 | Pressure        |   -   | [32.1, 61.2]    |  |
|  +9.79 |  +8.90 | 00:28:54.797 | Serbia             | Serbia             | 58 | Dispossessed    |   -   | [87.0, 18.5]    | Opponent Dispossessed |

---

### Case 19: Episode `3857258_p121_79506c50`
- **Match**: `3857258` (FIFA World Cup) | **Period**: 2
- **Counterpressing Team**: **Serbia** vs Possessing Team: **Serbia**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1257.97s` | Acquisition dt: `3.935s` | Control dt: `3.935s` | Regain dt: `3.935s`
- **Control Event**: `Carry` (ID: `c355c4f9-aec3-4e37-b371-df9e75bc1cdb`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.935s)
  [ ] Controlled-possession verified (ctrl: 3.935s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.67 |  -2.54 | 00:20:55.435 | Serbia             | Serbia             | 121 | Ball Recovery   |   -   | [75.1, 18.1]    |  |
|  +0.00 |  -0.87 | 00:20:57.109 | Brazil             | Serbia             | 121 | Ball Recovery   |   -   | [35.5, 63.0]    |  |
|  +0.00 |  -0.87 | 00:20:57.109 | Brazil             | Serbia             | 121 | Carry           |   -   | [35.5, 63.0]    | Carry under control |
|  +0.87 |  +0.00 | 00:20:57.975 | Serbia             | Serbia             | 121 | Pressure        |  Yes  | [84.6, 17.1]    |  |
|  +2.58 |  +1.72 | 00:20:59.691 | Serbia             | Serbia             | 121 | Pressure        |  Yes  | [80.5, 18.1]    |  |
|  +3.50 |  +2.63 | 00:21:00.606 | Serbia             | Serbia             | 121 | Pressure        |  Yes  | [75.6, 16.0]    |  |
|  +3.91 |  +3.05 | 00:21:01.022 | Brazil             | Serbia             | 121 | Miscontrol      |   -   | [46.8, 63.6]    | Opponent Miscontrol |
|  +4.31 |  +3.45 | 00:21:01.422 | Brazil             | Serbia             | 121 | Pressure        |   -   | [47.3, 67.4]    |  |
|  +4.80 |  +3.94 | 00:21:01.910 | Serbia             | Serbia             | 121 | Ball Recovery   |   -   | [68.9, 14.2]    |  |
|  +4.80 |  +3.94 | 00:21:01.910 | Serbia             | Serbia             | 121 | Carry           |   -   | [68.9, 14.2]    | Carry under control |
|  +5.52 |  +4.66 | 00:21:02.632 | Serbia             | Serbia             | 121 | Pass            |   -   | [70.5, 13.2]    | -> Milos Veljkovi |
|  +7.18 |  +6.31 | 00:21:04.287 | Serbia             | Serbia             | 121 | Ball Receipt*   |   -   | [49.2, 22.4]    |  |
|  +7.18 |  +6.31 | 00:21:04.287 | Serbia             | Serbia             | 121 | Carry           |   -   | [49.2, 22.4]    | Carry under control |

---

### Case 20: Episode `3857275_p40_71c05cab`
- **Match**: `3857275` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Tunisia** vs Possessing Team: **Tunisia**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1161.97s` | Acquisition dt: `1.059s` | Control dt: `1.059s` | Regain dt: `1.059s`
- **Control Event**: `Carry` (ID: `7abc82de-4bc8-4f73-8ac4-248e9285c8b9`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.059s)
  [ ] Controlled-possession verified (ctrl: 1.059s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -2.12 | 00:19:19.847 | France             | Tunisia            | 40 | Ball Recovery   |   -   | [82.0, 7.3]     |  |
|  +0.00 |  -2.12 | 00:19:19.847 | France             | Tunisia            | 40 | Carry           |   -   | [82.0, 7.3]     | Carry under control |
|  +1.85 |  -0.27 | 00:19:21.698 | France             | Tunisia            | 40 | Pass            |   -   | [82.0, 7.3]     | Incomplete (Incomplete) |
|  +2.12 |  +0.00 | 00:19:21.967 | Tunisia            | Tunisia            | 40 | Block           |  Yes  | [41.6, 72.6]    |  |
|  +3.18 |  +1.06 | 00:19:23.026 | Tunisia            | Tunisia            | 40 | Ball Recovery   |   -   | [37.5, 64.6]    |  |
|  +3.18 |  +1.06 | 00:19:23.026 | Tunisia            | Tunisia            | 40 | Carry           |   -   | [37.5, 64.6]    | Carry under control |
|  +3.48 |  +1.36 | 00:19:23.329 | Tunisia            | Tunisia            | 40 | Pass            |   -   | [33.3, 60.2]    | -> Aïssa Bilal La |
|  +4.51 |  +2.39 | 00:19:24.354 | Tunisia            | Tunisia            | 40 | Ball Receipt*   |   -   | [39.4, 74.0]    |  |
|  +4.51 |  +2.39 | 00:19:24.354 | Tunisia            | Tunisia            | 40 | Carry           |   -   | [39.4, 74.0]    | Carry under control |
|  +4.93 |  +2.81 | 00:19:24.779 | Tunisia            | Tunisia            | 40 | Pass            |   -   | [39.4, 74.0]    | -> Anis Ben Slima |
|  +5.93 |  +3.81 | 00:19:25.774 | Tunisia            | Tunisia            | 40 | Ball Receipt*   |   -   | [49.8, 70.2]    |  |
|  +5.93 |  +3.81 | 00:19:25.774 | Tunisia            | Tunisia            | 40 | Carry           |   -   | [49.8, 70.2]    | Carry under control |
|  +8.33 |  +6.21 | 00:19:28.173 | France             | Tunisia            | 40 | Pressure        |   -   | [58.5, 4.3]     |  |

---

### Case 21: Episode `3893812_p198_12b04bfb`
- **Match**: `3893812` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Argentina Women's** vs Possessing Team: **Argentina Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2690.98s` | Acquisition dt: `3.415s` | Control dt: `3.415s` | Regain dt: `3.415s`
- **Control Event**: `Carry` (ID: `456f4663-80d8-469d-871a-8bec93365685`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.415s)
  [ ] Controlled-possession verified (ctrl: 3.415s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.22 | 00:44:50.763 | Argentina Women's  | Argentina Women's  | 198 | Ball Receipt*   |   -   | [84.2, 56.6]    | Incomplete |
|  +0.00 |  -0.22 | 00:44:50.763 | South Africa Women | Argentina Women's  | 198 | Ball Recovery   |   -   | [35.9, 21.3]    |  |
|  +0.00 |  -0.22 | 00:44:50.763 | South Africa Women | Argentina Women's  | 198 | Carry           |   -   | [35.9, 21.3]    | Carry under control |
|  +0.22 |  +0.00 | 00:44:50.984 | Argentina Women's  | Argentina Women's  | 198 | Pressure        |  Yes  | [84.2, 56.3]    |  |
|  +0.32 |  +0.10 | 00:44:51.083 | South Africa Women | Argentina Women's  | 198 | Pass            |   -   | [35.9, 24.5]    | -> Melinda Kgadie |
|  +2.40 |  +2.18 | 00:44:53.162 | South Africa Women | Argentina Women's  | 198 | Ball Receipt*   |   -   | [51.1, 16.7]    |  |
|  +2.40 |  +2.18 | 00:44:53.162 | South Africa Women | Argentina Women's  | 198 | Carry           |   -   | [51.1, 16.7]    | Carry under control |
|  +2.46 |  +2.24 | 00:44:53.224 | South Africa Women | Argentina Women's  | 198 | Miscontrol      |   -   | [51.1, 16.7]    | Opponent Miscontrol |
|  +2.93 |  +2.70 | 00:44:53.689 | South Africa Women | Argentina Women's  | 198 | Pressure        |   -   | [51.1, 15.3]    |  |
|  +3.64 |  +3.41 | 00:44:54.399 | Argentina Women's  | Argentina Women's  | 198 | Ball Recovery   |   -   | [69.0, 65.9]    |  |
|  +3.64 |  +3.41 | 00:44:54.399 | Argentina Women's  | Argentina Women's  | 198 | Carry           |   -   | [69.0, 65.9]    | Carry under control |
|  +5.29 |  +5.07 | 00:44:56.054 | South Africa Women | Argentina Women's  | 198 | Pressure        |   -   | [55.4, 14.9]    |  |
|  +5.40 |  +5.18 | 00:44:56.166 | Argentina Women's  | Argentina Women's  | 198 | Pass            |   -   | [62.9, 66.3]    | -> Miriam Anahí M |

---

### Case 22: Episode `3877090_p39_1a523055`
- **Match**: `3877090` (Major League Soccer) | **Period**: 1
- **Counterpressing Team**: **Inter Miami** vs Possessing Team: **Inter Miami**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1180.60s` | Acquisition dt: `1.803s` | Control dt: `1.803s` | Regain dt: `1.803s`
- **Control Event**: `Carry` (ID: `f31675e9-3e1c-4200-96a8-7c82d1e73d7a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.803s)
  [ ] Controlled-possession verified (ctrl: 1.803s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.62 |  -1.42 | 00:19:39.174 | LAFC               | Inter Miami        | 39 | Pass            |   -   | [57.2, 75.9]    | -> Kellyn Kai Per |
|  +1.05 |  -1.00 | 00:19:39.603 | LAFC               | Inter Miami        | 39 | Ball Receipt*   |   -   | [58.4, 74.1]    |  |
|  +1.05 |  -1.00 | 00:19:39.603 | LAFC               | Inter Miami        | 39 | Carry           |   -   | [58.4, 74.1]    | Carry under control |
|  +2.05 |  +0.00 | 00:19:40.599 | Inter Miami        | Inter Miami        | 39 | Pressure        |  Yes  | [57.9, 7.4]     |  |
|  +2.28 |  +0.23 | 00:19:40.831 | LAFC               | Inter Miami        | 39 | Pass            |   -   | [57.9, 69.1]    | Incomplete (Incomplete) |
|  +3.85 |  +1.80 | 00:19:42.402 | LAFC               | Inter Miami        | 39 | Ball Receipt*   |   -   | [79.5, 58.3]    | Incomplete |
|  +3.85 |  +1.80 | 00:19:42.402 | Inter Miami        | Inter Miami        | 39 | Ball Recovery   |   -   | [43.5, 18.6]    |  |
|  +3.85 |  +1.80 | 00:19:42.402 | Inter Miami        | Inter Miami        | 39 | Carry           |   -   | [43.5, 18.6]    | Carry under control |
|  +5.50 |  +3.46 | 00:19:44.056 | Inter Miami        | Inter Miami        | 39 | Pass            |   -   | [51.2, 20.4]    | -> Lionel Andrés  |
|  +6.84 |  +4.80 | 00:19:45.395 | Inter Miami        | Inter Miami        | 39 | Ball Receipt*   |   -   | [62.9, 48.5]    |  |
|  +6.84 |  +4.80 | 00:19:45.395 | Inter Miami        | Inter Miami        | 39 | Carry           |   -   | [62.9, 48.5]    | Carry under control |
|  +8.56 |  +6.51 | 00:19:47.112 | Inter Miami        | Inter Miami        | 39 | Pass            |   -   | [63.2, 40.6]    | -> Facundo Farías |
|  +9.58 |  +7.53 | 00:19:48.132 | Inter Miami        | Inter Miami        | 39 | Ball Receipt*   |   -   | [75.4, 41.8]    |  |

---

### Case 23: Episode `3835322_p97_4cd6a799`
- **Match**: `3835322` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2619.06s` | Acquisition dt: `1.671s` | Control dt: `1.671s` | Regain dt: `1.671s`
- **Control Event**: `Carry` (ID: `bfc16518-2276-4283-9002-b2fd6743fc81`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.671s)
  [ ] Controlled-possession verified (ctrl: 1.671s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.82 | 00:43:37.237 | Denmark Women's    | Germany Women's    | 97 | Pass            |   -   | [48.7, 31.3]    | -> Signe Kallesøe |
|  +1.44 |  -0.38 | 00:43:38.679 | Denmark Women's    | Germany Women's    | 97 | Ball Receipt*   |   -   | [55.4, 40.7]    |  |
|  +1.44 |  -0.38 | 00:43:38.679 | Denmark Women's    | Germany Women's    | 97 | Carry           |   -   | [55.4, 40.7]    | Carry under control |
|  +1.82 |  +0.00 | 00:43:39.056 | Germany Women's    | Germany Women's    | 97 | Pressure        |  Yes  | [64.9, 36.7]    |  |
|  +2.37 |  +0.55 | 00:43:39.609 | Denmark Women's    | Germany Women's    | 97 | Dispossessed    |   -   | [55.2, 44.3]    | Opponent Dispossessed |
|  +2.37 |  +0.55 | 00:43:39.609 | Germany Women's    | Germany Women's    | 97 | Duel            |  Yes  | [64.9, 35.8]    | Tackle, Success In Play |
|  +3.49 |  +1.67 | 00:43:40.727 | Germany Women's    | Germany Women's    | 97 | Ball Recovery   |   -   | [64.9, 37.6]    |  |
|  +3.49 |  +1.67 | 00:43:40.727 | Germany Women's    | Germany Women's    | 97 | Carry           |   -   | [64.9, 37.6]    | Carry under control |
|  +8.15 |  +6.33 | 00:43:45.388 | Germany Women's    | Germany Women's    | 97 | Pass            |   -   | [66.4, 27.1]    | -> Marina Hegerin |
|  +9.45 |  +7.63 | 00:43:46.688 | Germany Women's    | Germany Women's    | 97 | Ball Receipt*   |   -   | [50.5, 21.7]    |  |
|  +9.45 |  +7.63 | 00:43:46.688 | Germany Women's    | Germany Women's    | 97 | Carry           |   -   | [50.5, 21.7]    | Carry under control |
| +10.90 |  +9.09 | 00:43:48.141 | Germany Women's    | Germany Women's    | 97 | Pass            |   -   | [50.8, 22.4]    | -> Felicitas Rauc |
| +13.10 | +11.28 | 00:43:50.337 | Germany Women's    | Germany Women's    | 97 | Ball Receipt*   |   -   | [64.4, 7.2]     |  |

---

### Case 24: Episode `3998858_p69_b113d291`
- **Match**: `3998858` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **England Women's** vs Possessing Team: **England Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `2436.26s` | Acquisition dt: `2.361s` | Control dt: `2.361s` | Regain dt: `2.361s`
- **Control Event**: `Carry` (ID: `1cc21dde-580f-4b9f-8c85-06e712e1d380`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.361s)
  [ ] Controlled-possession verified (ctrl: 2.361s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.08 |  -3.14 | 00:40:33.125 | Wales W            | England Women's    | 69 | Goal Keeper     |   -   | [2.6, 37.6]     |  |
|  +1.31 |  -1.91 | 00:40:34.354 | Wales W            | England Women's    | 69 | Ball Recovery   |   -   | [6.1, 23.2]     |  |
|  +1.31 |  -1.91 | 00:40:34.354 | Wales W            | England Women's    | 69 | Carry           |   -   | [6.1, 23.2]     | Carry under control |
|  +3.22 |  +0.00 | 00:40:36.260 | England Women's    | England Women's    | 69 | Pressure        |  Yes  | [114.3, 66.7]   |  |
|  +3.35 |  +0.13 | 00:40:36.395 | Wales W            | England Women's    | 69 | Pass            |   -   | [4.5, 14.2]     | Incomplete (Incomplete) |
|  +3.59 |  +0.38 | 00:40:36.638 | England Women's    | England Women's    | 69 | Block           |  Yes  | [112.6, 66.5]   |  |
|  +5.58 |  +2.36 | 00:40:38.621 | England Women's    | England Women's    | 69 | Ball Recovery   |   -   | [94.5, 61.0]    |  |
|  +5.58 |  +2.36 | 00:40:38.621 | England Women's    | England Women's    | 69 | Carry           |   -   | [94.5, 61.0]    | Carry under control |
|  +6.55 |  +3.34 | 00:40:39.598 | England Women's    | England Women's    | 69 | Pass            |   -   | [94.5, 61.0]    | -> Georgia Stanwa |
|  +9.02 |  +5.80 | 00:40:42.062 | England Women's    | England Women's    | 69 | Ball Receipt*   |   -   | [118.5, 52.2]   |  |
|  +9.02 |  +5.80 | 00:40:42.062 | England Women's    | England Women's    | 69 | Pass            |   -   | [118.1, 52.6]   | Incomplete (Incomplete) |
|  +9.46 |  +6.25 | 00:40:42.508 | Wales W            | England Women's    | 69 | Block           |   -   | [2.3, 34.2]     |  |
|  +9.91 |  +6.70 | 00:40:42.960 | Wales W            | England Women's    | 69 | Block           |   -   | [0.9, 31.2]     |  |

---

### Case 25: Episode `3835330_p105_a689d7fa`
- **Match**: `3835330` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `ball_recovery` | **Evidence String**: `ball_recovery_plus_carry`
- **Timestamps**: Initiation: `1089.97s` | Acquisition dt: `0.588s` | Control dt: `0.588s` | Regain dt: `0.588s`
- **Control Event**: `Carry` (ID: `401b09ec-aefa-4a96-9e02-44b3559f6c36`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.588s)
  [ ] Controlled-possession verified (ctrl: 0.588s <= 5.0s)
  [ ] Evidence categorization valid (ball_recovery_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.56 |  -1.56 | 00:18:08.417 | Spain Women's      | Spain Women's      | 104 | Carry           |   -   | [97.2, 60.8]    | Carry under control |
|  -0.72 |  -0.72 | 00:18:09.252 | Germany Women's    | Spain Women's      | 104 | Pressure        |   -   | [24.5, 16.5]    |  |
|  +0.00 |  +0.00 | 00:18:09.972 | Spain Women's      | Spain Women's      | 104 | Dribble         |   -   | [97.5, 64.1]    |  |
|  +0.00 |  +0.00 | 00:18:09.972 | Germany Women's    | Germany Women's    | 105 | Duel            |  Yes  | [22.6, 16.0]    | Tackle, Success In Play |
|  +0.59 |  +0.59 | 00:18:10.560 | Germany Women's    | Germany Women's    | 105 | Ball Recovery   |   -   | [20.3, 20.7]    |  |
|  +0.59 |  +0.59 | 00:18:10.560 | Germany Women's    | Germany Women's    | 105 | Carry           |   -   | [20.3, 20.7]    | Carry under control |
|  +2.56 |  +2.56 | 00:18:12.535 | Spain Women's      | Germany Women's    | 105 | Dribbled Past   |  Yes  | [95.0, 59.1]    |  |
|  +2.56 |  +2.56 | 00:18:12.535 | Germany Women's    | Germany Women's    | 105 | Dribble         |   -   | [25.1, 21.0]    |  |
|  +2.56 |  +2.56 | 00:18:12.535 | Germany Women's    | Germany Women's    | 105 | Carry           |   -   | [25.1, 21.0]    | Carry under control |
|  +3.88 |  +3.88 | 00:18:13.851 | Germany Women's    | Germany Women's    | 105 | Pass            |   -   | [25.1, 21.0]    | -> Sophia Kleinhe |
|  +4.92 |  +4.92 | 00:18:14.895 | Germany Women's    | Germany Women's    | 105 | Ball Receipt*   |   -   | [20.1, 7.0]     |  |
|  +4.92 |  +4.92 | 00:18:14.895 | Germany Women's    | Germany Women's    | 105 | Carry           |   -   | [20.1, 7.0]     | Carry under control |
|  +6.07 |  +6.07 | 00:18:16.038 | Germany Women's    | Germany Women's    | 105 | Pass            |   -   | [19.8, 4.5]     | -> Merle Frohms |

---

### Case 26: Episode `3940878_p13_3cd0e781`
- **Match**: `3940878` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Italy** vs Possessing Team: **Italy**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `305.83s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `767fc00a-07a5-42ec-8bc4-046fc1d1e690`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.96 |  -0.96 | 00:05:04.868 | Switzerland        | Switzerland        | 12 | Carry           |   -   | [45.5, 78.2]    | Carry under control |
|  -0.84 |  -0.84 | 00:05:04.995 | Italy              | Switzerland        | 12 | Pressure        |   -   | [72.3, 2.1]     |  |
|  +0.00 |  +0.00 | 00:05:05.832 | Switzerland        | Switzerland        | 12 | Dispossessed    |   -   | [49.5, 79.0]    | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:05:05.832 | Italy              | Italy              | 13 | Duel            |  Yes  | [70.6, 1.1]     | Tackle, Won |
|  +0.00 |  +0.00 | 00:05:05.832 | Italy              | Italy              | 13 | Carry           |   -   | [70.6, 1.1]     | Carry under control |
|  +0.40 |  +0.40 | 00:05:06.230 | Switzerland        | Italy              | 13 | Pressure        |  Yes  | [51.3, 79.7]    |  |
|  +0.93 |  +0.93 | 00:05:06.760 | Switzerland        | Italy              | 13 | Foul Committed  |  Yes  | [55.2, 79.5]    |  |
|  +0.93 |  +0.93 | 00:05:06.760 | Italy              | Italy              | 13 | Foul Won        |   -   | [64.9, 0.6]     |  |
|  +6.92 |  +6.92 | 00:05:12.756 | Italy              | Italy              | 14 | Pass            |   -   | [64.9, 0.6]     | -> Alessandro Bas |
|  +8.65 |  +8.65 | 00:05:14.478 | Italy              | Italy              | 14 | Ball Receipt*   |   -   | [46.0, 6.5]     |  |
|  +8.65 |  +8.65 | 00:05:14.478 | Italy              | Italy              | 14 | Carry           |   -   | [46.0, 6.5]     | Carry under control |
| +10.19 | +10.19 | 00:05:16.019 | Italy              | Italy              | 14 | Pass            |   -   | [47.3, 10.3]    | -> Gianluca Manci |
| +12.71 | +12.71 | 00:05:18.543 | Italy              | Italy              | 14 | Ball Receipt*   |   -   | [34.8, 37.7]    |  |

---

### Case 27: Episode `3893829_p111_54f4234f`
- **Match**: `3893829` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **France Women's** vs Possessing Team: **France Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `666.10s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `a3306284-fd19-40b1-9176-248ef4ce8aab`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -3.24 | 00:11:02.857 | Panama Women's     | France Women's     | 111 | Ball Recovery   |   -   | [37.9, 9.8]     |  |
|  +0.00 |  -3.24 | 00:11:02.857 | Panama Women's     | France Women's     | 111 | Carry           |   -   | [37.9, 9.8]     | Carry under control |
|  +3.24 |  +0.00 | 00:11:06.099 | Panama Women's     | France Women's     | 111 | Dribble         |   -   | [45.4, 10.9]    |  |
|  +3.24 |  +0.00 | 00:11:06.099 | France Women's     | France Women's     | 111 | Duel            |  Yes  | [74.7, 69.2]    | Tackle, Won |
|  +3.24 |  +0.00 | 00:11:06.099 | France Women's     | France Women's     | 111 | Carry           |   -   | [74.7, 69.2]    | Carry under control |
|  +3.70 |  +0.46 | 00:11:06.556 | France Women's     | France Women's     | 111 | Pass            |   -   | [75.6, 71.6]    | -> Léa Le Garrec |
|  +4.61 |  +1.36 | 00:11:07.462 | France Women's     | France Women's     | 111 | Ball Receipt*   |   -   | [70.6, 63.2]    |  |
|  +4.61 |  +1.36 | 00:11:07.462 | France Women's     | France Women's     | 111 | Carry           |   -   | [70.6, 63.2]    | Carry under control |
|  +7.55 |  +4.31 | 00:11:10.406 | France Women's     | France Women's     | 111 | Pass            |   -   | [84.3, 61.3]    | -> Clara Mateo |
|  +8.60 |  +5.35 | 00:11:11.452 | France Women's     | France Women's     | 111 | Ball Receipt*   |   -   | [96.3, 72.2]    |  |
|  +8.60 |  +5.35 | 00:11:11.452 | France Women's     | France Women's     | 111 | Carry           |   -   | [96.3, 72.2]    | Carry under control |
| +12.15 |  +8.91 | 00:11:15.006 | France Women's     | France Women's     | 111 | Pass            |   -   | [107.9, 70.7]   | Incomplete (Out) |
| +17.84 | +14.60 | 00:11:20.699 | France Women's     | France Women's     | 111 | Ball Receipt*   |   -   | [112.6, 12.6]   | Incomplete |

---

### Case 28: Episode `3835324_p33_abf0d42a`
- **Match**: `3835324` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Sweden Women's** vs Possessing Team: **Sweden Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `947.69s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `0f6af0a1-e0d0-48fb-9669-bd8caf292f10`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.05 |  -2.05 | 00:15:45.640 | Netherlands Women' | Netherlands Women' | 32 | Carry           |   -   | [42.0, 68.4]    | Carry under control |
|  -1.69 |  -1.69 | 00:15:46.000 | Sweden Women's     | Netherlands Women' | 32 | Pressure        |  Yes  | [79.8, 11.3]    |  |
|  +0.00 |  +0.00 | 00:15:47.694 | Netherlands Women' | Netherlands Women' | 32 | Dispossessed    |   -   | [43.7, 75.0]    | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:15:47.694 | Sweden Women's     | Sweden Women's     | 33 | Duel            |  Yes  | [76.4, 5.1]     | Tackle, Won |
|  +0.00 |  +0.00 | 00:15:47.694 | Sweden Women's     | Sweden Women's     | 33 | Carry           |   -   | [76.4, 5.1]     | Carry under control |
|  +1.43 |  +1.43 | 00:15:49.121 | Netherlands Women' | Sweden Women's     | 33 | Pressure        |  Yes  | [42.6, 73.1]    |  |
|  +1.77 |  +1.77 | 00:15:49.464 | Netherlands Women' | Sweden Women's     | 33 | Pressure        |  Yes  | [49.9, 72.4]    |  |
|  +1.83 |  +1.83 | 00:15:49.526 | Sweden Women's     | Sweden Women's     | 33 | Pass            |   -   | [73.0, 7.0]     | -> Sara Caroline  |
|  +3.20 |  +3.20 | 00:15:50.894 | Sweden Women's     | Sweden Women's     | 33 | Ball Receipt*   |   -   | [68.3, 4.9]     |  |
|  +3.20 |  +3.20 | 00:15:50.894 | Sweden Women's     | Sweden Women's     | 33 | Pass            |   -   | [68.3, 4.9]     | -> Magdalena Lill |
|  +4.80 |  +4.80 | 00:15:52.495 | Sweden Women's     | Sweden Women's     | 33 | Ball Receipt*   |   -   | [56.5, 6.4]     |  |
|  +4.80 |  +4.80 | 00:15:52.495 | Sweden Women's     | Sweden Women's     | 33 | Pass            |   -   | [56.5, 6.4]     | -> Gun Nathalie B |
|  +5.97 |  +5.97 | 00:15:53.661 | Sweden Women's     | Sweden Women's     | 33 | Ball Receipt*   |   -   | [48.0, 12.6]    |  |

---

### Case 29: Episode `3773415_p86_9f471e5a`
- **Match**: `3773415` (La Liga) | **Period**: 2
- **Counterpressing Team**: **Cádiz** vs Possessing Team: **Cádiz**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_pass`
- **Timestamps**: Initiation: `10.79s` | Acquisition dt: `0.0s` | Control dt: `1.687s` | Regain dt: `1.687s`
- **Control Event**: `Pass` (ID: `9e9b5278-5d53-457a-bbf6-4d597a5d4ad3`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 1.687s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.35 |  -3.35 | 00:00:07.445 | Cádiz              | Cádiz              | 86 | Pass            |   -   | [42.0, 49.4]    | Incomplete (Incomplete) |
|  +0.00 |  +0.00 | 00:00:10.791 | Cádiz              | Cádiz              | 86 | Ball Receipt*   |   -   | [85.0, 34.0]    | Incomplete |
|  +0.00 |  +0.00 | 00:00:10.791 | Barcelona          | Cádiz              | 86 | Pass            |   -   | [36.4, 45.7]    | Incomplete (Incomplete) |
|  +0.00 |  +0.00 | 00:00:10.791 | Cádiz              | Cádiz              | 86 | Duel            |  Yes  | [83.7, 34.4]    | Aerial Lost |
|  +1.69 |  +1.69 | 00:00:12.478 | Barcelona          | Cádiz              | 86 | Ball Receipt*   |   -   | [44.1, 49.3]    | Incomplete |
|  +1.69 |  +1.69 | 00:00:12.478 | Cádiz              | Cádiz              | 86 | Pass            |   -   | [68.9, 29.9]    | -> Jairo Izquierd |
|  +3.66 |  +3.66 | 00:00:14.448 | Cádiz              | Cádiz              | 86 | Ball Receipt*   |   -   | [93.5, 26.3]    |  |
|  +3.66 |  +3.66 | 00:00:14.448 | Cádiz              | Cádiz              | 86 | Carry           |   -   | [93.5, 26.3]    | Carry under control |
|  +3.68 |  +3.68 | 00:00:14.474 | Cádiz              | Cádiz              | 86 | Pass            |   -   | [93.5, 26.3]    | -> Luis Alfonso E |
|  +5.77 |  +5.77 | 00:00:16.560 | Cádiz              | Cádiz              | 86 | Ball Receipt*   |   -   | [98.0, 7.7]     |  |
|  +5.77 |  +5.77 | 00:00:16.560 | Cádiz              | Cádiz              | 86 | Carry           |   -   | [98.0, 7.7]     | Carry under control |
|  +5.89 |  +5.89 | 00:00:16.680 | Cádiz              | Cádiz              | 86 | Pass            |   -   | [98.0, 7.7]     | Incomplete (Incomplete) |
|  +7.54 |  +7.54 | 00:00:18.327 | Barcelona          | Barcelona          | 87 | Goal Keeper     |   -   | [7.8, 42.1]     |  |

---

### Case 30: Episode `3845507_p171_a9d3df86`
- **Match**: `3845507` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `2665.21s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `3378e1c8-86c8-490b-995d-c67dbcba6524`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.59 | 00:44:24.622 | France Women's     | France Women's     | 170 | Interception    |  Yes  | [58.8, 65.3]    | Won |
|  +0.00 |  -0.59 | 00:44:24.622 | France Women's     | France Women's     | 170 | Carry           |   -   | [58.8, 65.3]    | Carry under control |
|  +0.59 |  +0.00 | 00:44:25.213 | France Women's     | France Women's     | 170 | Dispossessed    |   -   | [56.9, 65.8]    | Opponent Dispossessed |
|  +0.59 |  +0.00 | 00:44:25.213 | Germany Women's    | Germany Women's    | 171 | Duel            |  Yes  | [63.2, 14.3]    | Tackle, Won |
|  +0.59 |  +0.00 | 00:44:25.213 | Germany Women's    | Germany Women's    | 171 | Carry           |   -   | [63.2, 14.3]    | Carry under control |
|  +1.43 |  +0.84 | 00:44:26.057 | France Women's     | Germany Women's    | 171 | Pressure        |  Yes  | [54.0, 68.3]    |  |
|  +3.40 |  +2.81 | 00:44:28.019 | France Women's     | Germany Women's    | 171 | Dribbled Past   |  Yes  | [54.7, 70.1]    |  |
|  +3.40 |  +2.81 | 00:44:28.019 | Germany Women's    | Germany Women's    | 171 | Dribble         |   -   | [65.4, 10.0]    |  |
|  +3.40 |  +2.81 | 00:44:28.019 | Germany Women's    | Germany Women's    | 171 | Carry           |   -   | [65.4, 10.0]    | Carry under control |
|  +4.14 |  +3.55 | 00:44:28.765 | Germany Women's    | Germany Women's    | 171 | Ball Recovery   |   -   | [68.1, 6.0]     |  |
|  +4.14 |  +3.55 | 00:44:28.765 | Germany Women's    | Germany Women's    | 171 | Carry           |   -   | [68.1, 6.0]     | Carry under control |
|  +7.38 |  +6.79 | 00:44:32.003 | Germany Women's    | Germany Women's    | 171 | Pass            |   -   | [93.8, 2.8]     | -> Linda Dallmann |
|  +9.35 |  +8.76 | 00:44:33.970 | Germany Women's    | Germany Women's    | 171 | Ball Receipt*   |   -   | [103.9, 39.2]   |  |

---

### Case 31: Episode `3857277_p98_77b9c072`
- **Match**: `3857277` (FIFA World Cup) | **Period**: 2
- **Counterpressing Team**: **Croatia** vs Possessing Team: **Morocco**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_pass`
- **Timestamps**: Initiation: `593.70s` | Acquisition dt: `2.001s` | Control dt: `3.697s` | Regain dt: `3.697s`
- **Control Event**: `Pass` (ID: `d1235c23-c557-494f-ae45-1763a1cfbc72`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.001s)
  [ ] Controlled-possession verified (ctrl: 3.697s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.98 | 00:09:51.715 | Morocco            | Morocco            | 98 | Ball Recovery   |   -   | [43.4, 68.0]    |  |
|  +0.00 |  -1.98 | 00:09:51.715 | Morocco            | Morocco            | 98 | Carry           |   -   | [43.4, 68.0]    | Carry under control |
|  +1.34 |  -0.64 | 00:09:53.055 | Morocco            | Morocco            | 98 | Pass            |   -   | [43.4, 68.0]    | -> Sofyan Amrabat |
|  +1.98 |  +0.00 | 00:09:53.699 | Croatia            | Morocco            | 98 | Pressure        |  Yes  | [69.2, 29.9]    |  |
|  +2.18 |  +0.19 | 00:09:53.891 | Morocco            | Morocco            | 98 | Ball Receipt*   |   -   | [46.3, 57.3]    |  |
|  +2.18 |  +0.19 | 00:09:53.891 | Morocco            | Morocco            | 98 | Pass            |   -   | [48.9, 53.0]    | -> Hakim Ziyech |
|  +3.99 |  +2.00 | 00:09:55.700 | Morocco            | Morocco            | 98 | Ball Receipt*   |   -   | [74.9, 69.4]    |  |
|  +3.99 |  +2.00 | 00:09:55.700 | Morocco            | Morocco            | 98 | Pass            |   -   | [74.9, 69.4]    | Incomplete (Incomplete) |
|  +3.99 |  +2.00 | 00:09:55.700 | Croatia            | Morocco            | 98 | Duel            |  Yes  | [45.2, 10.7]    | Aerial Lost |
|  +4.24 |  +2.26 | 00:09:55.958 | Croatia            | Morocco            | 98 | Block           |  Yes  | [42.3, 10.9]    |  |
|  +5.68 |  +3.70 | 00:09:57.396 | Croatia            | Croatia            | 99 | Pass            |   -   | [45.9, 28.5]    | -> Dejan Lovren |
|  +6.88 |  +4.90 | 00:09:58.598 | Croatia            | Croatia            | 99 | Ball Receipt*   |   -   | [37.7, 31.5]    |  |
|  +6.88 |  +4.90 | 00:09:58.598 | Croatia            | Croatia            | 99 | Carry           |   -   | [37.7, 31.5]    | Carry under control |

---

### Case 32: Episode `3930166_p138_a6e3a34c`
- **Match**: `3930166` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Portugal** vs Possessing Team: **Portugal**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `2403.17s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `1ac6422e-786c-4c6f-bafe-803a9e131b25`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.30 | 00:40:02.873 | Czech Republic     | Czech Republic     | 137 | Ball Receipt*   |   -   | [115.2, 69.1]   |  |
|  +0.00 |  -0.30 | 00:40:02.873 | Czech Republic     | Czech Republic     | 137 | Carry           |   -   | [115.2, 69.1]   | Carry under control |
|  +0.30 |  +0.00 | 00:40:03.173 | Czech Republic     | Czech Republic     | 137 | Dribble         |   -   | [114.5, 69.1]   |  |
|  +0.30 |  +0.00 | 00:40:03.173 | Portugal           | Portugal           | 138 | Duel            |  Yes  | [5.6, 11.0]     | Tackle, Won |
|  +0.30 |  +0.00 | 00:40:03.173 | Portugal           | Portugal           | 138 | Carry           |   -   | [5.6, 11.0]     | Carry under control |
|  +1.87 |  +1.57 | 00:40:04.745 | Portugal           | Portugal           | 138 | Pass            |   -   | [5.8, 19.5]     | -> Gonçalo Bernar |
|  +2.72 |  +2.43 | 00:40:05.598 | Portugal           | Portugal           | 138 | Ball Receipt*   |   -   | [15.5, 11.0]    |  |
|  +2.72 |  +2.43 | 00:40:05.598 | Portugal           | Portugal           | 138 | Carry           |   -   | [15.5, 11.0]    | Carry under control |
|  +3.53 |  +3.23 | 00:40:06.398 | Portugal           | Portugal           | 138 | Pass            |   -   | [15.5, 11.0]    | -> Bruno Miguel B |
|  +4.19 |  +3.89 | 00:40:07.064 | Portugal           | Portugal           | 138 | Ball Receipt*   |   -   | [20.0, 16.9]    |  |
|  +4.19 |  +3.89 | 00:40:07.064 | Portugal           | Portugal           | 138 | Carry           |   -   | [20.0, 16.9]    | Carry under control |
|  +4.43 |  +4.13 | 00:40:07.306 | Czech Republic     | Portugal           | 138 | Pressure        |  Yes  | [103.2, 57.7]   |  |
|  +5.33 |  +5.03 | 00:40:08.201 | Czech Republic     | Portugal           | 138 | Dribbled Past   |   -   | [96.3, 60.6]    |  |

---

### Case 33: Episode `3837706_p24_bf1a1a55`
- **Match**: `3837706` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Stade Brestois** vs Possessing Team: **Stade Brestois**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `555.59s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `684d8217-3209-46aa-a3ad-7aa11313154a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.97 |  -0.97 | 00:09:14.622 | Stade Brestois     | Paris Saint-Germai | 23 | Pressure        |   -   | [63.3, 44.8]    |  |
|  -0.41 |  -0.41 | 00:09:15.179 | Stade Brestois     | Paris Saint-Germai | 23 | Pressure        |   -   | [63.6, 49.1]    |  |
|  +0.00 |  +0.00 | 00:09:15.593 | Paris Saint-Germai | Paris Saint-Germai | 23 | Dribble         |   -   | [56.3, 32.1]    |  |
|  +0.00 |  +0.00 | 00:09:15.593 | Stade Brestois     | Stade Brestois     | 24 | Duel            |  Yes  | [63.8, 48.0]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:09:15.593 | Stade Brestois     | Stade Brestois     | 24 | Carry           |   -   | [63.8, 48.0]    | Carry under control |
|  +0.70 |  +0.70 | 00:09:16.297 | Stade Brestois     | Stade Brestois     | 24 | Pass            |   -   | [64.1, 47.9]    | -> Pierre Lees Me |
|  +1.77 |  +1.77 | 00:09:17.364 | Stade Brestois     | Stade Brestois     | 24 | Ball Receipt*   |   -   | [65.9, 35.0]    |  |
|  +1.77 |  +1.77 | 00:09:17.364 | Stade Brestois     | Stade Brestois     | 24 | Carry           |   -   | [65.9, 35.0]    | Carry under control |
|  +2.80 |  +2.80 | 00:09:18.394 | Stade Brestois     | Stade Brestois     | 24 | Pass            |   -   | [70.4, 32.3]    | -> Islam Slimani |
|  +3.29 |  +3.29 | 00:09:18.886 | Stade Brestois     | Stade Brestois     | 24 | Ball Receipt*   |   -   | [81.3, 39.2]    |  |
|  +3.29 |  +3.29 | 00:09:18.886 | Stade Brestois     | Stade Brestois     | 24 | Pass            |   -   | [80.9, 38.5]    | Incomplete (Incomplete) |
|  +3.51 |  +3.51 | 00:09:19.104 | Stade Brestois     | Stade Brestois     | 24 | Ball Receipt*   |   -   | [72.3, 37.1]    | Incomplete |
|  +3.51 |  +3.51 | 00:09:19.104 | Paris Saint-Germai | Stade Brestois     | 24 | Block           |  Yes  | [44.5, 42.6]    |  |

---

### Case 34: Episode `4018356_p125_17b5eeaf`
- **Match**: `4018356` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Spain Women's** vs Possessing Team: **Spain Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `1092.57s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `39a6dffa-9ba8-488d-8b8d-7c6b3560a67b`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.75 |  -2.75 | 00:18:09.817 | Switzerland Women' | Switzerland Women' | 124 | Carry           |   -   | [47.5, 3.8]     | Carry under control |
|  -1.55 |  -1.55 | 00:18:11.019 | Spain Women's      | Switzerland Women' | 124 | Pressure        |   -   | [64.0, 75.2]    |  |
|  +0.00 |  +0.00 | 00:18:12.569 | Switzerland Women' | Switzerland Women' | 124 | Dribble         |   -   | [64.7, 5.9]     |  |
|  +0.00 |  +0.00 | 00:18:12.569 | Spain Women's      | Spain Women's      | 125 | Duel            |  Yes  | [55.4, 74.2]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:18:12.569 | Spain Women's      | Spain Women's      | 125 | Carry           |   -   | [55.4, 74.2]    | Carry under control |
|  +3.49 |  +3.49 | 00:18:16.058 | Switzerland Women' | Spain Women's      | 125 | Pressure        |  Yes  | [76.4, 2.9]     |  |
|  +3.82 |  +3.82 | 00:18:16.384 | Switzerland Women' | Spain Women's      | 125 | Dribbled Past   |  Yes  | [80.2, 3.1]     |  |
|  +3.82 |  +3.82 | 00:18:16.384 | Spain Women's      | Spain Women's      | 125 | Dribble         |   -   | [39.9, 77.0]    |  |
|  +3.82 |  +3.82 | 00:18:16.384 | Spain Women's      | Spain Women's      | 125 | Carry           |   -   | [39.9, 77.0]    | Carry under control |
|  +4.76 |  +4.76 | 00:18:17.333 | Switzerland Women' | Spain Women's      | 125 | Pressure        |  Yes  | [78.6, 9.3]     |  |
|  +5.09 |  +5.09 | 00:18:17.660 | Switzerland Women' | Spain Women's      | 125 | Foul Committed  |   -   | [78.1, 8.1]     |  |
|  +5.09 |  +5.09 | 00:18:17.660 | Spain Women's      | Spain Women's      | 125 | Foul Won        |   -   | [42.0, 72.0]    |  |
| +34.95 | +34.95 | 00:18:47.520 | Spain Women's      | Spain Women's      | 126 | Pass            |   -   | [42.0, 72.0]    | -> Laia Aleixandr |

---

### Case 35: Episode `3893831_p36_75493f1f`
- **Match**: `3893831` (Women's World Cup) | **Period**: 1
- **Counterpressing Team**: **South Africa Women's** vs Possessing Team: **South Africa Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `1075.56s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `866ddc49-3277-4ffe-90d9-70b0ebaff71a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.34 | 00:17:55.221 | Italy Women's      | Italy Women's      | 35 | Ball Receipt*   |   -   | [116.6, 15.1]   |  |
|  +0.00 |  -0.34 | 00:17:55.221 | Italy Women's      | Italy Women's      | 35 | Carry           |   -   | [116.6, 15.1]   | Carry under control |
|  +0.34 |  +0.00 | 00:17:55.558 | Italy Women's      | Italy Women's      | 35 | Dispossessed    |   -   | [115.5, 13.9]   | Opponent Dispossessed |
|  +0.34 |  +0.00 | 00:17:55.558 | South Africa Women | South Africa Women | 36 | Duel            |  Yes  | [4.6, 66.2]     | Tackle, Won |
|  +0.34 |  +0.00 | 00:17:55.558 | South Africa Women | South Africa Women | 36 | Carry           |   -   | [4.6, 66.2]     | Carry under control |
|  +2.66 |  +2.33 | 00:17:57.884 | Italy Women's      | South Africa Women | 36 | Pressure        |  Yes  | [117.3, 17.1]   |  |
|  +3.24 |  +2.90 | 00:17:58.457 | South Africa Women | South Africa Women | 36 | Pass            |   -   | [8.2, 66.2]     | -> Jermaine Seopo |
|  +5.20 |  +4.87 | 00:18:00.423 | Italy Women's      | South Africa Women | 36 | Pressure        |  Yes  | [86.2, 8.9]     |  |
|  +5.28 |  +4.94 | 00:18:00.503 | South Africa Women | South Africa Women | 36 | Ball Receipt*   |   -   | [32.6, 72.9]    |  |
|  +5.28 |  +4.94 | 00:18:00.503 | South Africa Women | South Africa Women | 36 | Pass            |   -   | [33.0, 72.9]    | -> Lebogang Ramal |
|  +6.24 |  +5.90 | 00:18:01.462 | Italy Women's      | South Africa Women | 36 | Pressure        |   -   | [91.4, 8.9]     |  |
|  +6.37 |  +6.03 | 00:18:01.587 | South Africa Women | South Africa Women | 36 | Ball Receipt*   |   -   | [27.0, 70.9]    |  |
|  +6.37 |  +6.03 | 00:18:01.587 | South Africa Women | South Africa Women | 36 | Carry           |   -   | [27.0, 70.9]    | Carry under control |

---

### Case 36: Episode `3895220_p104_6f1e0283`
- **Match**: `3895220` (1. Bundesliga) | **Period**: 2
- **Counterpressing Team**: **Bayer Leverkusen** vs Possessing Team: **Bayer Leverkusen**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `166.58s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `6135e16b-cc4b-49c3-a9d2-d41a6ec73dcc`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.13 |  -1.13 | 00:02:45.456 | Darmstadt 98       | Darmstadt 98       | 103 | Carry           |   -   | [54.9, 67.7]    | Carry under control |
|  -1.03 |  -1.03 | 00:02:45.547 | Bayer Leverkusen   | Darmstadt 98       | 103 | Pressure        |   -   | [65.0, 17.9]    |  |
|  +0.00 |  +0.00 | 00:02:46.582 | Darmstadt 98       | Darmstadt 98       | 103 | Dispossessed    |   -   | [54.9, 58.4]    | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:02:46.582 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Duel            |  Yes  | [65.2, 21.7]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:02:46.582 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Carry           |   -   | [65.2, 21.7]    | Carry under control |
|  +1.24 |  +1.24 | 00:02:47.821 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Pass            |   -   | [67.2, 23.4]    | -> Borja Iglesias |
|  +1.70 |  +1.70 | 00:02:48.278 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Ball Receipt*   |   -   | [71.9, 27.3]    |  |
|  +1.70 |  +1.70 | 00:02:48.278 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Carry           |   -   | [71.9, 27.3]    | Carry under control |
|  +1.77 |  +1.77 | 00:02:48.356 | Darmstadt 98       | Bayer Leverkusen   | 104 | Pressure        |  Yes  | [48.0, 51.3]    |  |
|  +2.33 |  +2.33 | 00:02:48.910 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Pass            |   -   | [71.1, 27.8]    | -> Robert Andrich |
|  +3.21 |  +3.21 | 00:02:49.789 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Ball Receipt*   |   -   | [65.2, 36.4]    |  |
|  +3.21 |  +3.21 | 00:02:49.789 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Carry           |   -   | [65.2, 36.4]    | Carry under control |
|  +4.73 |  +4.73 | 00:02:51.309 | Bayer Leverkusen   | Bayer Leverkusen   | 104 | Pass            |   -   | [65.2, 41.8]    | -> Nathan Tella |

---

### Case 37: Episode `3802676_p47_76f6f696`
- **Match**: `3802676` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Paris Saint-Germain**
- **Stratum**: `duel` | **Evidence String**: `50_50_plus_carry`
- **Timestamps**: Initiation: `1342.74s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `513ba5a7-b06a-40a0-82b2-dd769d79d732`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (50_50_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.69 | 00:22:21.051 | Paris Saint-Germai | Lens               | 46 | Ball Receipt*   |   -   | [62.4, 37.4]    | Incomplete |
|  +0.00 |  -1.69 | 00:22:21.051 | Lens               | Lens               | 46 | Block           |   -   | [64.6, 42.0]    |  |
|  +1.69 |  +0.00 | 00:22:22.742 | Lens               | Lens               | 46 | 50/50           |   -   | [64.2, 31.4]    |  |
|  +1.69 |  +0.00 | 00:22:22.742 | Paris Saint-Germai | Paris Saint-Germai | 47 | 50/50           |  Yes  | [55.9, 48.7]    |  |
|  +1.69 |  +0.00 | 00:22:22.742 | Paris Saint-Germai | Paris Saint-Germai | 47 | Carry           |   -   | [55.9, 48.7]    | Carry under control |
|  +3.78 |  +2.08 | 00:22:24.826 | Lens               | Paris Saint-Germai | 47 | Pressure        |  Yes  | [56.7, 32.9]    |  |
|  +5.65 |  +3.96 | 00:22:26.698 | Lens               | Paris Saint-Germai | 47 | Dribbled Past   |  Yes  | [44.0, 31.1]    |  |
|  +5.65 |  +3.96 | 00:22:26.698 | Paris Saint-Germai | Paris Saint-Germai | 47 | Dribble         |   -   | [76.1, 49.0]    |  |
|  +8.13 |  +6.44 | 00:22:29.180 | Lens               | Paris Saint-Germai | 47 | Clearance       |   -   | [20.4, 24.4]    |  |
| +12.72 | +11.03 | 00:22:33.771 | Paris Saint-Germai | Paris Saint-Germai | 48 | Pass            |   -   | [103.8, 80.0]   | -> Kylian Mbappé  |
| +13.85 | +12.16 | 00:22:34.902 | Paris Saint-Germai | Paris Saint-Germai | 48 | Ball Receipt*   |   -   | [114.6, 70.8]   |  |
| +13.85 | +12.16 | 00:22:34.902 | Paris Saint-Germai | Paris Saint-Germai | 48 | Carry           |   -   | [114.6, 70.8]   | Carry under control |
| +18.54 | +16.85 | 00:22:39.588 | Paris Saint-Germai | Paris Saint-Germai | 48 | Pass            |   -   | [112.9, 68.2]   | -> Achraf Hakimi  |

---

### Case 38: Episode `4018356_p82_3f2d3aa9`
- **Match**: `4018356` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Spain Women's** vs Possessing Team: **Spain Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `2695.97s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `56d0de53-7e9e-45af-89b9-1769d12854a5`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.72 |  -0.98 | 00:44:54.986 | Switzerland Women' | Switzerland Women' | 81 | Ball Receipt*   |   -   | [108.7, 57.7]   |  |
|  +5.72 |  -0.98 | 00:44:54.986 | Switzerland Women' | Switzerland Women' | 81 | Carry           |   -   | [108.7, 57.7]   | Carry under control |
|  +6.70 |  +0.00 | 00:44:55.970 | Switzerland Women' | Switzerland Women' | 81 | Dribble         |   -   | [111.3, 55.8]   |  |
|  +6.70 |  +0.00 | 00:44:55.970 | Spain Women's      | Spain Women's      | 82 | Duel            |  Yes  | [8.8, 24.3]     | Tackle, Won |
|  +6.70 |  +0.00 | 00:44:55.970 | Spain Women's      | Spain Women's      | 82 | Carry           |   -   | [8.8, 24.3]     | Carry under control |
|  +7.71 |  +1.01 | 00:44:56.983 | Switzerland Women' | Spain Women's      | 82 | Pressure        |  Yes  | [113.6, 57.3]   |  |
|  +8.03 |  +1.33 | 00:44:57.302 | Spain Women's      | Spain Women's      | 82 | Pass            |   -   | [6.3, 24.1]     | Incomplete (Out) |
| +37.32 | +30.62 | 00:45:26.590 | Switzerland Women' | Switzerland Women' | 83 | Pass            |   -   | [86.2, 80.0]    | Incomplete (Out) |
| +39.31 | +32.60 | 00:45:28.574 | Switzerland Women' | Switzerland Women' | 83 | Pressure        |   -   | [119.4, 72.7]   |  |
| +40.57 | +33.87 | 00:45:29.842 | Switzerland Women' | Switzerland Women' | 83 | Ball Receipt*   |   -   | [117.5, 72.5]   | Incomplete |
| +50.01 | +43.31 | 00:45:39.279 | Spain Women's      | Spain Women's      | 84 | Pass            |   -   | [2.6, 33.9]     | -> Irene Paredes  |
| +51.50 | +44.80 | 00:45:40.768 | Spain Women's      | Spain Women's      | 84 | Ball Receipt*   |   -   | [18.2, 50.2]    |  |
| +51.50 | +44.80 | 00:45:40.768 | Spain Women's      | Spain Women's      | 84 | Carry           |   -   | [18.2, 50.2]    | Carry under control |

---

### Case 39: Episode `3773466_p127_0299b356`
- **Match**: `3773466` (La Liga) | **Period**: 2
- **Counterpressing Team**: **Celta Vigo** vs Possessing Team: **Celta Vigo**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `1652.56s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `babe8b33-da89-410d-8861-8f4cdc695236`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.67 | 00:27:31.892 | Barcelona          | Barcelona          | 126 | Ball Receipt*   |   -   | [61.8, 70.3]    |  |
|  +0.00 |  -0.67 | 00:27:31.892 | Barcelona          | Barcelona          | 126 | Carry           |   -   | [61.8, 70.3]    | Carry under control |
|  +0.67 |  +0.00 | 00:27:32.561 | Barcelona          | Barcelona          | 126 | Dispossessed    |   -   | [63.7, 73.4]    | Opponent Dispossessed |
|  +0.67 |  +0.00 | 00:27:32.561 | Celta Vigo         | Celta Vigo         | 127 | Duel            |  Yes  | [56.4, 6.7]     | Tackle, Won |
|  +0.67 |  +0.00 | 00:27:32.561 | Celta Vigo         | Celta Vigo         | 127 | Carry           |   -   | [56.4, 6.7]     | Carry under control |
|  +5.07 |  +4.40 | 00:27:36.957 | Celta Vigo         | Celta Vigo         | 127 | Pass            |   -   | [66.7, 17.6]    | -> Iago Aspas Jun |
|  +5.94 |  +5.27 | 00:27:37.832 | Celta Vigo         | Celta Vigo         | 127 | Ball Receipt*   |   -   | [74.6, 38.4]    |  |
|  +5.94 |  +5.27 | 00:27:37.832 | Celta Vigo         | Celta Vigo         | 127 | Carry           |   -   | [74.6, 38.4]    | Carry under control |
|  +7.86 |  +7.19 | 00:27:39.750 | Barcelona          | Celta Vigo         | 127 | Pressure        |   -   | [45.9, 35.3]    |  |
|  +8.66 |  +8.00 | 00:27:40.556 | Celta Vigo         | Celta Vigo         | 127 | Pass            |   -   | [73.1, 38.8]    | -> Manuel Agudo D |
| +10.24 |  +9.58 | 00:27:42.137 | Celta Vigo         | Celta Vigo         | 127 | Ball Receipt*   |   -   | [95.2, 6.5]     |  |
| +10.24 |  +9.58 | 00:27:42.137 | Celta Vigo         | Celta Vigo         | 127 | Carry           |   -   | [95.2, 6.5]     | Carry under control |
| +13.60 | +12.93 | 00:27:45.490 | Celta Vigo         | Celta Vigo         | 127 | Shot            |   -   | [105.4, 18.7]   | Blocked |

---

### Case 40: Episode `3837839_p82_6fb33f04`
- **Match**: `3837839` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Stade de Reims**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `2705.45s` | Acquisition dt: `4.363s` | Control dt: `4.363s` | Regain dt: `4.363s`
- **Control Event**: `Carry` (ID: `a6d7f81b-b30e-491c-8ed7-35561b965dc6`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.363s)
  [ ] Controlled-possession verified (ctrl: 4.363s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.23 | 00:45:05.222 | Paris Saint-Germai | Paris Saint-Germai | 81 | Ball Receipt*   |   -   | [96.5, 18.0]    | Incomplete |
|  +0.00 |  -0.23 | 00:45:05.222 | Stade de Reims     | Stade de Reims     | 82 | Interception    |  Yes  | [26.4, 69.9]    | Won |
|  +0.00 |  -0.23 | 00:45:05.222 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [26.4, 69.9]    | Carry under control |
|  +0.23 |  +0.00 | 00:45:05.453 | Paris Saint-Germai | Stade de Reims     | 82 | Pressure        |  Yes  | [95.1, 14.6]    |  |
|  +0.43 |  +0.20 | 00:45:05.652 | Stade de Reims     | Stade de Reims     | 82 | Pass            |   -   | [25.2, 65.8]    | -> Junya Ito |
|  +1.05 |  +0.82 | 00:45:06.269 | Stade de Reims     | Stade de Reims     | 82 | Ball Receipt*   |   -   | [28.3, 62.1]    |  |
|  +1.05 |  +0.82 | 00:45:06.269 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [28.3, 62.1]    | Carry under control |
|  +3.36 |  +3.13 | 00:45:08.584 | Stade de Reims     | Stade de Reims     | 82 | Pass            |   -   | [37.0, 64.1]    | -> Marshall Nyash |
|  +4.35 |  +4.12 | 00:45:09.569 | Stade de Reims     | Stade de Reims     | 82 | Ball Receipt*   |   -   | [40.4, 55.6]    |  |
|  +4.35 |  +4.12 | 00:45:09.569 | Stade de Reims     | Stade de Reims     | 82 | Carry           |   -   | [40.4, 55.6]    | Carry under control |
|  +4.59 |  +4.36 | 00:45:09.816 | Stade de Reims     | Stade de Reims     | 82 | Dribble         |   -   | [41.8, 55.2]    |  |
|  +4.59 |  +4.36 | 00:45:09.816 | Paris Saint-Germai | Stade de Reims     | 82 | Duel            |  Yes  | [78.3, 24.9]    | Tackle, Won |
|  +4.59 |  +4.36 | 00:45:09.816 | Paris Saint-Germai | Stade de Reims     | 82 | Carry           |   -   | [78.3, 24.9]    | Carry under control |

---

### Case 41: Episode `3788774_p93_eef22393`
- **Match**: `3788774` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Hungary** vs Possessing Team: **Hungary**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_pass`
- **Timestamps**: Initiation: `2783.61s` | Acquisition dt: `0.0s` | Control dt: `0.742s` | Regain dt: `0.742s`
- **Control Event**: `Pass` (ID: `6cefdd65-6b45-480d-a3db-710f7fad6a25`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.742s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.91 |  -0.91 | 00:46:22.696 | Germany            | Germany            | 92 | Carry           |   -   | [95.5, 21.1]    | Carry under control |
|  -0.70 |  -0.70 | 00:46:22.913 | Hungary            | Germany            | 92 | Pressure        |   -   | [21.0, 59.6]    |  |
|  +0.00 |  +0.00 | 00:46:23.609 | Germany            | Germany            | 92 | Dispossessed    |   -   | [98.0, 20.5]    | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:46:23.609 | Hungary            | Hungary            | 93 | Duel            |  Yes  | [22.1, 59.6]    | Tackle, Success In Play |
|  +0.74 |  +0.74 | 00:46:24.351 | Hungary            | Hungary            | 93 | Pass            |   -   | [20.8, 59.4]    | -> Ádám Nagy |
|  +1.22 |  +1.22 | 00:46:24.831 | Hungary            | Hungary            | 93 | Ball Receipt*   |   -   | [22.7, 56.9]    |  |
|  +1.22 |  +1.22 | 00:46:24.831 | Hungary            | Hungary            | 93 | Carry           |   -   | [22.7, 56.9]    | Carry under control |
|  +1.30 |  +1.30 | 00:46:24.911 | Hungary            | Hungary            | 93 | Pass            |   -   | [22.7, 56.9]    | -> Ádám Szalai |
|  +2.64 |  +2.64 | 00:46:26.246 | Hungary            | Hungary            | 93 | Ball Receipt*   |   -   | [28.5, 76.1]    |  |
|  +2.64 |  +2.64 | 00:46:26.246 | Hungary            | Hungary            | 93 | Carry           |   -   | [28.5, 76.1]    | Carry under control |
|  +3.16 |  +3.16 | 00:46:26.770 | Germany            | Hungary            | 93 | Pressure        |  Yes  | [94.2, 5.7]     |  |
|  +4.31 |  +4.31 | 00:46:27.922 | Hungary            | Hungary            | 93 | Pass            |   -   | [33.6, 76.7]    | -> Loïc Négo |
|  +5.11 |  +5.11 | 00:46:28.715 | Germany            | Hungary            | 93 | Pressure        |   -   | [74.9, 5.3]     |  |

---

### Case 42: Episode `3857269_p19_d97740dc`
- **Match**: `3857269` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Switzerland** vs Possessing Team: **Switzerland**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_pass`
- **Timestamps**: Initiation: `478.12s` | Acquisition dt: `0.419s` | Control dt: `2.213s` | Regain dt: `2.213s`
- **Control Event**: `Pass` (ID: `c41f8a3a-93a3-4d88-9f99-b8f2ad86d597`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.419s)
  [ ] Controlled-possession verified (ctrl: 2.213s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.97 | 00:07:57.149 | Brazil             | Switzerland        | 19 | Duel            |   -   | [38.8, 3.2]     | Tackle, Success In Play |
|  +0.69 |  -0.28 | 00:07:57.839 | Brazil             | Switzerland        | 19 | Ball Recovery   |   -   | [38.8, 3.2]     |  |
|  +0.69 |  -0.28 | 00:07:57.839 | Brazil             | Switzerland        | 19 | Carry           |   -   | [38.8, 3.2]     | Carry under control |
|  +0.97 |  +0.00 | 00:07:58.120 | Switzerland        | Switzerland        | 19 | Pressure        |  Yes  | [84.5, 74.6]    |  |
|  +1.39 |  +0.42 | 00:07:58.539 | Brazil             | Switzerland        | 19 | Dispossessed    |   -   | [35.6, 5.5]     | Opponent Dispossessed |
|  +1.39 |  +0.42 | 00:07:58.539 | Switzerland        | Switzerland        | 19 | Duel            |  Yes  | [84.5, 74.6]    | Tackle, Success In Play |
|  +3.18 |  +2.21 | 00:08:00.333 | Switzerland        | Switzerland        | 19 | Pass            |   -   | [76.2, 65.6]    | -> Granit Xhaka |
|  +3.76 |  +2.79 | 00:08:00.910 | Switzerland        | Switzerland        | 19 | Ball Receipt*   |   -   | [72.0, 56.8]    |  |
|  +3.76 |  +2.79 | 00:08:00.910 | Switzerland        | Switzerland        | 19 | Carry           |   -   | [72.0, 56.8]    | Carry under control |
|  +5.14 |  +4.17 | 00:08:02.288 | Switzerland        | Switzerland        | 19 | Pass            |   -   | [77.2, 43.8]    | -> Ricardo Iván R |
|  +6.90 |  +5.93 | 00:08:04.053 | Switzerland        | Switzerland        | 19 | Ball Receipt*   |   -   | [82.4, 18.8]    |  |
|  +6.90 |  +5.93 | 00:08:04.053 | Switzerland        | Switzerland        | 19 | Carry           |   -   | [82.4, 18.8]    | Carry under control |
|  +8.75 |  +7.78 | 00:08:05.901 | Switzerland        | Switzerland        | 19 | Pass            |   -   | [89.0, 12.1]    | Incomplete (Incomplete) |

---

### Case 43: Episode `3942752_p84_e18c5038`
- **Match**: `3942752` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **France** vs Possessing Team: **France**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `426.24s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `35df733d-7e97-4a07-af20-c38c43472f37`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -3.04 |  -3.04 | 00:07:03.202 | Spain              | Spain              | 83 | Carry           |   -   | [48.1, 17.2]    | Carry under control |
|  -2.81 |  -2.81 | 00:07:03.434 | France             | Spain              | 83 | Pressure        |   -   | [71.2, 62.3]    |  |
|  +0.00 |  +0.00 | 00:07:06.242 | Spain              | Spain              | 83 | Dispossessed    |   -   | [42.6, 5.7]     | Opponent Dispossessed |
|  +0.00 |  +0.00 | 00:07:06.242 | France             | France             | 84 | Duel            |  Yes  | [77.5, 74.4]    | Tackle, Won |
|  +0.00 |  +0.00 | 00:07:06.242 | France             | France             | 84 | Carry           |   -   | [77.5, 74.4]    | Carry under control |
|  +2.52 |  +2.52 | 00:07:08.765 | France             | France             | 84 | Pass            |   -   | [86.0, 72.2]    | -> N'Golo Kanté |
|  +3.81 |  +3.81 | 00:07:10.057 | France             | France             | 84 | Ball Receipt*   |   -   | [85.8, 52.0]    |  |
|  +3.81 |  +3.81 | 00:07:10.057 | France             | France             | 84 | Carry           |   -   | [85.8, 52.0]    | Carry under control |
|  +4.52 |  +4.52 | 00:07:10.763 | France             | France             | 84 | Pass            |   -   | [90.2, 53.0]    | -> Jules Koundé |
|  +6.06 |  +6.06 | 00:07:12.299 | France             | France             | 84 | Ball Receipt*   |   -   | [107.7, 65.7]   |  |
|  +6.06 |  +6.06 | 00:07:12.299 | France             | France             | 84 | Carry           |   -   | [107.7, 65.7]   | Carry under control |
|  +6.73 |  +6.73 | 00:07:12.970 | France             | France             | 84 | Pass            |   -   | [111.9, 59.4]   | Incomplete (Incomplete) |
|  +6.84 |  +6.84 | 00:07:13.078 | Spain              | France             | 84 | Pressure        |   -   | [8.4, 22.5]     |  |

---

### Case 44: Episode `3788772_p43_91f272a6`
- **Match**: `3788772` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Czech Republic** vs Possessing Team: **Czech Republic**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_pass`
- **Timestamps**: Initiation: `1614.37s` | Acquisition dt: `0.0s` | Control dt: `0.836s` | Regain dt: `0.836s`
- **Control Event**: `Pass` (ID: `5becb5ab-5b4b-4b73-b33a-a1a525720c61`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.836s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.15 | 00:26:54.223 | England            | Czech Republic     | 43 | Ball Recovery   |   -   | [26.4, 29.2]    |  |
|  +0.00 |  -0.15 | 00:26:54.223 | England            | Czech Republic     | 43 | Carry           |   -   | [26.4, 29.2]    | Carry under control |
|  +0.15 |  +0.00 | 00:26:54.371 | England            | Czech Republic     | 43 | Dribble         |   -   | [27.6, 28.7]    |  |
|  +0.15 |  +0.00 | 00:26:54.371 | Czech Republic     | Czech Republic     | 43 | Duel            |  Yes  | [92.5, 51.4]    | Tackle, Success In Play |
|  +0.98 |  +0.84 | 00:26:55.207 | Czech Republic     | Czech Republic     | 43 | Pass            |   -   | [96.1, 58.8]    | -> Jakub Jankto |
|  +1.99 |  +1.84 | 00:26:56.211 | Czech Republic     | Czech Republic     | 43 | Ball Receipt*   |   -   | [102.4, 50.0]   |  |
|  +1.99 |  +1.84 | 00:26:56.211 | Czech Republic     | Czech Republic     | 43 | Pass            |   -   | [102.4, 50.0]   | -> Tomáš Souček |
|  +3.09 |  +2.95 | 00:26:57.317 | Czech Republic     | Czech Republic     | 43 | Ball Receipt*   |   -   | [92.3, 45.3]    |  |
|  +3.09 |  +2.95 | 00:26:57.317 | Czech Republic     | Czech Republic     | 43 | Carry           |   -   | [92.3, 45.3]    | Carry under control |
|  +3.81 |  +3.66 | 00:26:58.031 | Czech Republic     | Czech Republic     | 43 | Pass            |   -   | [91.3, 46.2]    | -> Tomáš Holeš |
|  +4.97 |  +4.82 | 00:26:59.193 | Czech Republic     | Czech Republic     | 43 | Ball Receipt*   |   -   | [88.5, 28.5]    |  |
|  +4.97 |  +4.82 | 00:26:59.193 | Czech Republic     | Czech Republic     | 43 | Carry           |   -   | [88.5, 28.5]    | Carry under control |
|  +5.03 |  +4.88 | 00:26:59.251 | England            | Czech Republic     | 43 | Pressure        |   -   | [29.6, 49.5]    |  |

---

### Case 45: Episode `3893788_p106_812a1c94`
- **Match**: `3893788` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Australia Women's** vs Possessing Team: **Australia Women's**
- **Stratum**: `duel` | **Evidence String**: `duel_plus_carry`
- **Timestamps**: Initiation: `578.50s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `94f874fc-3512-4832-ab52-26e3dcd3645f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (duel_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.50 | 00:09:37.993 | Republic of Irelan | Republic of Irelan | 105 | Ball Receipt*   |   -   | [95.7, 48.5]    |  |
|  +0.00 |  -0.50 | 00:09:37.993 | Republic of Irelan | Republic of Irelan | 105 | Carry           |   -   | [95.7, 48.5]    | Carry under control |
|  +0.50 |  +0.00 | 00:09:38.496 | Republic of Irelan | Republic of Irelan | 105 | Dispossessed    |   -   | [96.3, 48.7]    | Opponent Dispossessed |
|  +0.50 |  +0.00 | 00:09:38.496 | Australia Women's  | Australia Women's  | 106 | Duel            |  Yes  | [23.8, 31.4]    | Tackle, Won |
|  +0.50 |  +0.00 | 00:09:38.496 | Australia Women's  | Australia Women's  | 106 | Carry           |   -   | [23.8, 31.4]    | Carry under control |
|  +1.85 |  +1.34 | 00:09:39.840 | Republic of Irelan | Australia Women's  | 106 | Pressure        |  Yes  | [96.3, 49.2]    |  |
|  +3.74 |  +3.24 | 00:09:41.737 | Australia Women's  | Australia Women's  | 106 | Pass            |   -   | [21.4, 28.3]    | -> Stephanie-Elis |
|  +5.25 |  +4.75 | 00:09:43.241 | Australia Women's  | Australia Women's  | 106 | Ball Receipt*   |   -   | [20.9, 12.1]    |  |
|  +5.25 |  +4.75 | 00:09:43.241 | Australia Women's  | Australia Women's  | 106 | Carry           |   -   | [20.9, 12.1]    | Carry under control |
|  +5.33 |  +4.83 | 00:09:43.321 | Australia Women's  | Australia Women's  | 106 | Pass            |   -   | [20.9, 12.1]    | Incomplete (Incomplete) |
|  +7.48 |  +6.97 | 00:09:45.470 | Australia Women's  | Australia Women's  | 106 | Ball Receipt*   |   -   | [51.9, 21.3]    | Incomplete |
|  +7.48 |  +6.97 | 00:09:45.470 | Republic of Irelan | Australia Women's  | 106 | Pass            |   -   | [61.3, 56.4]    | Incomplete (Incomplete) |
|  +8.62 |  +8.11 | 00:09:46.610 | Australia Women's  | Australia Women's  | 106 | Ball Recovery   |   -   | [45.6, 30.4]    |  |

---

### Case 46: Episode `3942819_p36_d4b345b5`
- **Match**: `3942819` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **England** vs Possessing Team: **England**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_pass`
- **Timestamps**: Initiation: `1853.00s` | Acquisition dt: `0.0s` | Control dt: `2.425s` | Regain dt: `2.425s`
- **Control Event**: `Pass` (ID: `897cca11-9e83-4d61-aec7-2399fff962eb`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 2.425s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +1.13 |  -0.89 | 00:30:52.111 | Netherlands        | England            | 36 | Ball Receipt*   |   -   | [16.1, 49.4]    |  |
|  +1.13 |  -0.89 | 00:30:52.111 | Netherlands        | England            | 36 | Pass            |   -   | [15.5, 49.1]    | Incomplete (Incomplete) |
|  +2.02 |  +0.00 | 00:30:53.004 | Netherlands        | England            | 36 | Ball Receipt*   |   -   | [30.1, 34.6]    | Incomplete |
|  +2.02 |  +0.00 | 00:30:53.004 | England            | England            | 36 | Interception    |  Yes  | [91.4, 45.5]    | Success In Play |
|  +4.45 |  +2.43 | 00:30:55.429 | England            | England            | 36 | Pass            |   -   | [87.0, 61.2]    | -> Bukayo Saka |
|  +5.29 |  +3.27 | 00:30:56.270 | England            | England            | 36 | Ball Receipt*   |   -   | [104.0, 66.0]   |  |
|  +5.29 |  +3.27 | 00:30:56.270 | England            | England            | 36 | Carry           |   -   | [104.0, 66.0]   | Carry under control |
|  +8.31 |  +6.29 | 00:30:59.297 | Netherlands        | England            | 36 | Pressure        |   -   | [4.0, 22.3]     |  |
|  +8.66 |  +6.64 | 00:30:59.640 | England            | England            | 36 | Pass            |   -   | [117.5, 59.2]   | -> Kieran Trippie |
| +13.20 | +11.18 | 00:31:04.181 | England            | England            | 36 | Ball Receipt*   |   -   | [103.0, 11.6]   |  |
| +13.20 | +11.18 | 00:31:04.181 | England            | England            | 36 | Carry           |   -   | [103.0, 11.6]   | Carry under control |
| +16.26 | +14.24 | 00:31:07.244 | England            | England            | 36 | Pass            |   -   | [90.6, 6.7]     | -> Declan Rice |
| +17.83 | +15.81 | 00:31:08.816 | England            | England            | 36 | Ball Receipt*   |   -   | [75.5, 16.8]    |  |

---

### Case 47: Episode `3835321_p139_80fbf3d2`
- **Match**: `3835321` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **WNT Finland** vs Possessing Team: **WNT Finland**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `1858.86s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `00253ada-06ce-4fa7-8529-bebb087414f2`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.36 |  -2.04 | 00:30:56.825 | Spain Women's      | Spain Women's      | 138 | Pass            |   -   | [79.9, 2.9]     | Incomplete (Incomplete) |
|  +7.34 |  -0.06 | 00:30:58.801 | Spain Women's      | Spain Women's      | 138 | Pressure        |   -   | [107.3, 4.0]    |  |
|  +7.40 |  +0.00 | 00:30:58.863 | Spain Women's      | Spain Women's      | 138 | Ball Receipt*   |   -   | [107.3, 4.0]    | Incomplete |
|  +7.40 |  +0.00 | 00:30:58.863 | WNT Finland        | WNT Finland        | 139 | Interception    |  Yes  | [11.7, 76.3]    | Won |
|  +7.40 |  +0.00 | 00:30:58.863 | WNT Finland        | WNT Finland        | 139 | Carry           |   -   | [11.7, 76.3]    | Carry under control |
|  +7.85 |  +0.45 | 00:30:59.311 | Spain Women's      | WNT Finland        | 139 | Foul Committed  |  Yes  | [107.6, 4.0]    |  |
|  +7.85 |  +0.45 | 00:30:59.311 | WNT Finland        | WNT Finland        | 139 | Foul Won        |   -   | [12.5, 76.1]    |  |
| +41.24 | +33.84 | 00:31:32.701 | WNT Finland        | WNT Finland        | 140 | Pass            |   -   | [12.5, 76.1]    | -> Eveliina Summa |
| +44.05 | +36.65 | 00:31:35.513 | WNT Finland        | WNT Finland        | 140 | Ball Receipt*   |   -   | [56.1, 72.7]    |  |
| +44.05 | +36.65 | 00:31:35.513 | WNT Finland        | WNT Finland        | 140 | Pass            |   -   | [56.1, 72.7]    | Incomplete (Incomplete) |
| +44.05 | +36.65 | 00:31:35.513 | Spain Women's      | WNT Finland        | 140 | Duel            |   -   | [64.0, 7.4]     | Aerial Lost |
| +44.70 | +37.30 | 00:31:36.164 | Spain Women's      | Spain Women's      | 141 | Ball Recovery   |   -   | [58.0, 8.3]     |  |
| +44.70 | +37.30 | 00:31:36.164 | Spain Women's      | Spain Women's      | 141 | Carry           |   -   | [58.0, 8.3]     | Carry under control |

---

### Case 48: Episode `3802930_p60_7f498d3a`
- **Match**: `3802930` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Troyes** vs Possessing Team: **Troyes**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `1845.61s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `7d72c700-436d-4d18-a1de-50ea04c7eba9`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.95 |  -3.69 | 00:30:41.927 | Paris Saint-Germai | Paris Saint-Germai | 59 | Carry           |   -   | [50.8, 42.4]    | Carry under control |
|  +4.10 |  -0.54 | 00:30:45.070 | Paris Saint-Germai | Paris Saint-Germai | 59 | Pass            |   -   | [56.7, 31.0]    | Incomplete (Incomplete) |
|  +4.64 |  +0.00 | 00:30:45.614 | Paris Saint-Germai | Paris Saint-Germai | 59 | Ball Receipt*   |   -   | [68.9, 33.1]    | Incomplete |
|  +4.64 |  +0.00 | 00:30:45.614 | Troyes             | Troyes             | 60 | Interception    |  Yes  | [55.6, 48.2]    | Won |
|  +4.64 |  +0.00 | 00:30:45.614 | Troyes             | Troyes             | 60 | Carry           |   -   | [55.6, 48.2]    | Carry under control |
|  +7.96 |  +3.32 | 00:30:48.933 | Troyes             | Troyes             | 60 | Pass            |   -   | [48.8, 32.2]    | -> Abdu Conté |
|  +9.16 |  +4.52 | 00:30:50.133 | Troyes             | Troyes             | 60 | Ball Receipt*   |   -   | [39.9, 24.4]    |  |
|  +9.16 |  +4.52 | 00:30:50.133 | Troyes             | Troyes             | 60 | Carry           |   -   | [39.9, 24.4]    | Carry under control |
| +10.41 |  +5.77 | 00:30:51.386 | Paris Saint-Germai | Troyes             | 60 | Pressure        |   -   | [78.1, 65.3]    |  |
| +11.87 |  +7.22 | 00:30:52.837 | Troyes             | Troyes             | 60 | Pass            |   -   | [35.0, 13.0]    | -> Jessy Moulin |
| +14.56 |  +9.92 | 00:30:55.535 | Troyes             | Troyes             | 60 | Ball Receipt*   |   -   | [5.6, 43.3]     |  |
| +14.56 |  +9.92 | 00:30:55.535 | Troyes             | Troyes             | 60 | Carry           |   -   | [5.6, 43.3]     | Carry under control |
| +15.14 | +10.50 | 00:30:56.112 | Paris Saint-Germai | Troyes             | 60 | Pressure        |   -   | [111.9, 37.8]   |  |

---

### Case 49: Episode `3837963_p103_44382fa8`
- **Match**: `3837963` (Ligue 1) | **Period**: 2
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Paris Saint-Germain**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `955.81s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `53cf77ed-722d-4351-b4a4-d7d2485a543f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.67 |  -4.44 | 00:15:51.369 | Lorient            | Lorient            | 102 | Pass            |   -   | [31.7, 61.6]    | Incomplete (Incomplete) |
|  +6.52 |  -0.59 | 00:15:55.219 | Lorient            | Lorient            | 102 | Pressure        |   -   | [85.0, 69.9]    |  |
|  +7.11 |  +0.00 | 00:15:55.813 | Lorient            | Lorient            | 102 | Ball Receipt*   |   -   | [82.6, 67.5]    | Incomplete |
|  +7.11 |  +0.00 | 00:15:55.813 | Paris Saint-Germai | Paris Saint-Germai | 103 | Interception    |  Yes  | [31.7, 12.8]    | Won |
|  +7.11 |  +0.00 | 00:15:55.813 | Paris Saint-Germai | Paris Saint-Germai | 103 | Carry           |   -   | [31.7, 12.8]    | Carry under control |
|  +9.31 |  +2.20 | 00:15:58.010 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [21.5, 3.8]     | -> Gianluigi Donn |
| +11.67 |  +4.56 | 00:16:00.374 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [8.8, 23.2]     |  |
| +11.67 |  +4.56 | 00:16:00.374 | Paris Saint-Germai | Paris Saint-Germai | 103 | Carry           |   -   | [8.8, 23.2]     | Carry under control |
| +14.92 |  +7.81 | 00:16:03.618 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [11.8, 26.7]    | -> Marcos Aoás Co |
| +16.61 |  +9.50 | 00:16:05.308 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [14.4, 18.1]    |  |
| +16.61 |  +9.50 | 00:16:05.308 | Paris Saint-Germai | Paris Saint-Germai | 103 | Pass            |   -   | [14.4, 18.1]    | -> Sergio Ramos G |
| +18.23 | +11.12 | 00:16:06.930 | Paris Saint-Germai | Paris Saint-Germai | 103 | Ball Receipt*   |   -   | [20.0, 26.5]    |  |
| +18.23 | +11.12 | 00:16:06.930 | Paris Saint-Germai | Paris Saint-Germai | 103 | Carry           |   -   | [20.0, 26.5]    | Carry under control |

---

### Case 50: Episode `3802696_p16_dc0a828b`
- **Match**: `3802696` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Stade de Reims** vs Possessing Team: **Stade de Reims**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `370.78s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `1e9de919-4d24-4e2d-9c91-e3746540a5f3`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.46 |  -1.19 | 00:06:09.589 | Paris Saint-Germai | Paris Saint-Germai | 15 | Pass            |   -   | [77.0, 58.5]    | Incomplete (Incomplete) |
|  +6.48 |  -0.18 | 00:06:10.608 | Paris Saint-Germai | Paris Saint-Germai | 15 | Pressure        |   -   | [97.6, 57.4]    |  |
|  +6.66 |  +0.00 | 00:06:10.783 | Paris Saint-Germai | Paris Saint-Germai | 15 | Ball Receipt*   |   -   | [97.2, 57.4]    | Incomplete |
|  +6.66 |  +0.00 | 00:06:10.783 | Stade de Reims     | Stade de Reims     | 16 | Interception    |  Yes  | [22.9, 22.7]    | Won |
|  +6.66 |  +0.00 | 00:06:10.783 | Stade de Reims     | Stade de Reims     | 16 | Carry           |   -   | [22.9, 22.7]    | Carry under control |
|  +7.69 |  +1.03 | 00:06:11.815 | Paris Saint-Germai | Stade de Reims     | 16 | Pressure        |  Yes  | [97.2, 57.9]    |  |
|  +7.95 |  +1.29 | 00:06:12.074 | Stade de Reims     | Stade de Reims     | 16 | Pass            |   -   | [23.9, 22.8]    | -> Marshall Nyash |
|  +8.74 |  +2.09 | 00:06:12.869 | Stade de Reims     | Stade de Reims     | 16 | Ball Receipt*   |   -   | [27.0, 29.4]    |  |
|  +8.74 |  +2.09 | 00:06:12.869 | Stade de Reims     | Stade de Reims     | 16 | Carry           |   -   | [27.0, 29.4]    | Carry under control |
|  +9.19 |  +2.53 | 00:06:13.313 | Stade de Reims     | Stade de Reims     | 16 | Pass            |   -   | [27.0, 29.4]    | -> Nathanaël Mbuk |
| +11.00 |  +4.34 | 00:06:15.125 | Stade de Reims     | Stade de Reims     | 16 | Ball Receipt*   |   -   | [25.1, 10.5]    |  |
| +11.00 |  +4.34 | 00:06:15.125 | Stade de Reims     | Stade de Reims     | 16 | Carry           |   -   | [25.1, 10.5]    | Carry under control |
| +13.12 |  +6.46 | 00:06:17.248 | Stade de Reims     | Stade de Reims     | 16 | Pass            |   -   | [26.1, 7.7]     | -> Dion Lopy |

---

### Case 51: Episode `3895202_p57_38116434`
- **Match**: `3895202` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Bayer Leverkusen** vs Possessing Team: **Bayer Leverkusen**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `2289.59s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `327b182c-741b-4814-b8e0-01b6d13a3e98`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.68 |  -3.79 | 00:38:05.806 | RB Leipzig         | RB Leipzig         | 56 | Carry           |   -   | [63.2, 31.2]    | Carry under control |
|  +5.72 |  -0.74 | 00:38:08.854 | RB Leipzig         | RB Leipzig         | 56 | Pass            |   -   | [77.6, 40.9]    | Incomplete (Incomplete) |
|  +6.46 |  +0.00 | 00:38:09.594 | RB Leipzig         | RB Leipzig         | 56 | Ball Receipt*   |   -   | [95.3, 44.5]    | Incomplete |
|  +6.46 |  +0.00 | 00:38:09.594 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Interception    |  Yes  | [27.7, 35.6]    | Won |
|  +6.46 |  +0.00 | 00:38:09.594 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Carry           |   -   | [27.7, 35.6]    | Carry under control |
|  +7.96 |  +1.49 | 00:38:11.087 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Pass            |   -   | [29.0, 40.2]    | -> Josip Stanišić |
|  +9.05 |  +2.59 | 00:38:12.179 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Ball Receipt*   |   -   | [19.3, 56.4]    |  |
|  +9.05 |  +2.59 | 00:38:12.179 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Carry           |   -   | [19.3, 56.4]    | Carry under control |
| +10.73 |  +4.27 | 00:38:13.860 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Pass            |   -   | [20.1, 59.5]    | -> Patrik Schick |
| +12.83 |  +6.36 | 00:38:15.956 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Ball Receipt*   |   -   | [50.3, 63.3]    |  |
| +12.83 |  +6.36 | 00:38:15.956 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Pass            |   -   | [51.3, 63.1]    | -> Jonas Hofmann |
| +15.10 |  +8.63 | 00:38:18.226 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Ball Receipt*   |   -   | [67.8, 65.4]    |  |
| +15.10 |  +8.63 | 00:38:18.226 | Bayer Leverkusen   | Bayer Leverkusen   | 57 | Carry           |   -   | [67.8, 65.4]    | Carry under control |

---

### Case 52: Episode `3941022_p158_f50e4993`
- **Match**: `3941022` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Austria** vs Possessing Team: **Austria**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `2478.84s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `baffd0d6-fade-4e0b-b7dc-baa3ee7d3f25`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.38 | 00:41:17.461 | Turkey             | Turkey             | 157 | Carry           |   -   | [64.0, 78.0]    | Carry under control |
|  +0.86 |  -0.52 | 00:41:18.320 | Turkey             | Turkey             | 157 | Pass            |   -   | [63.1, 79.1]    | Incomplete (Incomplete) |
|  +1.38 |  +0.00 | 00:41:18.845 | Turkey             | Turkey             | 157 | Ball Receipt*   |   -   | [55.6, 78.5]    | Incomplete |
|  +1.38 |  +0.00 | 00:41:18.845 | Austria            | Austria            | 158 | Interception    |  Yes  | [60.9, 1.0]     | Won |
|  +1.38 |  +0.00 | 00:41:18.845 | Austria            | Austria            | 158 | Carry           |   -   | [60.9, 1.0]     | Carry under control |
|  +1.80 |  +0.41 | 00:41:19.259 | Turkey             | Austria            | 158 | Pressure        |  Yes  | [56.6, 78.4]    |  |
|  +2.02 |  +0.64 | 00:41:19.481 | Austria            | Austria            | 158 | Dribble         |   -   | [62.6, 1.6]     |  |
|  +2.02 |  +0.64 | 00:41:19.481 | Turkey             | Austria            | 158 | Duel            |  Yes  | [57.5, 78.5]    | Tackle, Lost In Play |
|  +2.41 |  +1.02 | 00:41:19.866 | Austria            | Austria            | 158 | Block           |  Yes  | [57.0, 2.5]     |  |
|  +2.80 |  +1.41 | 00:41:20.258 | Austria            | Austria            | 158 | Pass            |   -   | [58.6, 3.5]     | -> Nicolas Seiwal |
|  +3.59 |  +2.21 | 00:41:21.050 | Austria            | Austria            | 158 | Ball Receipt*   |   -   | [57.0, 8.2]     |  |
|  +3.59 |  +2.21 | 00:41:21.050 | Austria            | Austria            | 158 | Carry           |   -   | [57.0, 8.2]     | Carry under control |
|  +5.46 |  +4.07 | 00:41:22.919 | Austria            | Austria            | 158 | Pass            |   -   | [55.1, 13.7]    | -> Kevin Danso |

---

### Case 53: Episode `3857256_p120_738d7a80`
- **Match**: `3857256` (FIFA World Cup) | **Period**: 2
- **Counterpressing Team**: **Serbia** vs Possessing Team: **Serbia**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `791.29s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `dcb68b06-d805-4906-abea-482bb189d452`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.37 |  -1.96 | 00:13:09.330 | Switzerland        | Switzerland        | 119 | Carry           |   -   | [81.4, 70.4]    | Carry under control |
|  +7.13 |  -0.20 | 00:13:11.089 | Switzerland        | Switzerland        | 119 | Pass            |   -   | [91.2, 63.9]    | Incomplete (Incomplete) |
|  +7.33 |  +0.00 | 00:13:11.292 | Switzerland        | Switzerland        | 119 | Ball Receipt*   |   -   | [98.7, 49.8]    | Incomplete |
|  +7.33 |  +0.00 | 00:13:11.292 | Serbia             | Serbia             | 120 | Interception    |  Yes  | [24.9, 19.2]    | Won |
|  +7.33 |  +0.00 | 00:13:11.292 | Serbia             | Serbia             | 120 | Carry           |   -   | [24.9, 19.2]    | Carry under control |
|  +9.26 |  +1.93 | 00:13:13.219 | Serbia             | Serbia             | 120 | Pass            |   -   | [15.4, 11.0]    | -> Filip Kostić |
| +10.23 |  +2.90 | 00:13:14.195 | Serbia             | Serbia             | 120 | Ball Receipt*   |   -   | [33.0, 11.6]    |  |
| +10.23 |  +2.90 | 00:13:14.195 | Serbia             | Serbia             | 120 | Carry           |   -   | [33.0, 11.6]    | Carry under control |
| +11.58 |  +4.25 | 00:13:15.541 | Serbia             | Serbia             | 120 | Pass            |   -   | [35.5, 9.4]     | -> Dušan Tadić |
| +13.03 |  +5.70 | 00:13:16.993 | Serbia             | Serbia             | 120 | Ball Receipt*   |   -   | [40.9, 32.8]    |  |
| +13.03 |  +5.70 | 00:13:16.993 | Serbia             | Serbia             | 120 | Carry           |   -   | [40.9, 32.8]    | Carry under control |
| +15.57 |  +8.24 | 00:13:19.531 | Switzerland        | Serbia             | 120 | Pressure        |   -   | [73.5, 43.6]    |  |
| +16.28 |  +8.94 | 00:13:20.237 | Serbia             | Serbia             | 120 | Pass            |   -   | [46.3, 34.1]    | -> Sergej Milinko |

---

### Case 54: Episode `3893806_p147_c97fe2fa`
- **Match**: `3893806` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Zambia W** vs Possessing Team: **Zambia W**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `1141.71s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `4e462c30-dc74-40b3-bb88-70f20abae883`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +4.70 |  -2.38 | 00:18:59.323 | Spain Women's      | Spain Women's      | 146 | Carry           |   -   | [67.0, 60.5]    | Carry under control |
|  +4.74 |  -2.34 | 00:18:59.363 | Spain Women's      | Spain Women's      | 146 | Pass            |   -   | [67.2, 61.1]    | Incomplete (Incomplete) |
|  +7.08 |  +0.00 | 00:19:01.706 | Spain Women's      | Spain Women's      | 146 | Ball Receipt*   |   -   | [76.0, 73.1]    | Incomplete |
|  +7.08 |  +0.00 | 00:19:01.706 | Zambia W           | Zambia W           | 147 | Interception    |  Yes  | [38.3, 16.2]    | Won |
|  +7.08 |  +0.00 | 00:19:01.706 | Zambia W           | Zambia W           | 147 | Carry           |   -   | [38.3, 16.2]    | Carry under control |
|  +7.27 |  +0.18 | 00:19:01.889 | Spain Women's      | Zambia W           | 147 | Pressure        |  Yes  | [79.6, 67.5]    |  |
|  +8.94 |  +1.86 | 00:19:03.567 | Zambia W           | Zambia W           | 147 | Pass            |   -   | [38.8, 15.6]    | -> Lushomo Mweemb |
|  +9.69 |  +2.61 | 00:19:04.317 | Spain Women's      | Zambia W           | 147 | Pressure        |  Yes  | [87.3, 59.0]    |  |
| +10.38 |  +3.30 | 00:19:05.008 | Zambia W           | Zambia W           | 147 | Ball Receipt*   |   -   | [31.5, 21.8]    |  |
| +10.38 |  +3.30 | 00:19:05.008 | Zambia W           | Zambia W           | 147 | Pass            |   -   | [30.0, 23.1]    | -> Racheal Kundan |
| +11.23 |  +4.14 | 00:19:05.850 | Zambia W           | Zambia W           | 147 | Ball Receipt*   |   -   | [50.3, 18.1]    |  |
| +11.23 |  +4.14 | 00:19:05.850 | Zambia W           | Zambia W           | 147 | Carry           |   -   | [50.3, 18.1]    | Carry under control |
| +11.40 |  +4.32 | 00:19:06.027 | Spain Women's      | Zambia W           | 147 | Pressure        |  Yes  | [69.8, 62.0]    |  |

---

### Case 55: Episode `3773631_p56_f916975d`
- **Match**: `3773631` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Barcelona** vs Possessing Team: **Barcelona**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `2062.31s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `4371db69-c7d1-4392-a1d0-1843dcb282d7`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.79 |  -2.74 | 00:34:19.571 | Real Betis         | Barcelona          | 56 | Carry           |   -   | [48.4, 11.0]    | Carry under control |
|  +3.21 |  -0.32 | 00:34:21.990 | Real Betis         | Barcelona          | 56 | Pass            |   -   | [52.3, 14.9]    | Incomplete (Incomplete) |
|  +3.53 |  +0.00 | 00:34:22.310 | Real Betis         | Barcelona          | 56 | Ball Receipt*   |   -   | [49.0, 2.6]     | Incomplete |
|  +3.53 |  +0.00 | 00:34:22.310 | Barcelona          | Barcelona          | 56 | Interception    |  Yes  | [69.4, 69.3]    | Won |
|  +3.53 |  +0.00 | 00:34:22.310 | Barcelona          | Barcelona          | 56 | Carry           |   -   | [69.4, 69.3]    | Carry under control |
|  +6.55 |  +3.01 | 00:34:25.323 | Barcelona          | Barcelona          | 56 | Pass            |   -   | [77.1, 54.0]    | -> Ricard Puig Ma |
|  +7.55 |  +4.01 | 00:34:26.324 | Barcelona          | Barcelona          | 56 | Ball Receipt*   |   -   | [71.7, 45.5]    |  |
|  +7.55 |  +4.01 | 00:34:26.324 | Barcelona          | Barcelona          | 56 | Carry           |   -   | [71.7, 45.5]    | Carry under control |
|  +8.89 |  +5.36 | 00:34:27.668 | Barcelona          | Barcelona          | 56 | Pass            |   -   | [76.6, 48.6]    | Incomplete (Incomplete) |
| +11.43 |  +7.89 | 00:34:30.204 | Barcelona          | Barcelona          | 56 | Ball Receipt*   |   -   | [104.8, 45.0]   | Incomplete |
| +11.43 |  +7.89 | 00:34:30.204 | Real Betis         | Real Betis         | 57 | Ball Recovery   |   -   | [13.4, 35.7]    |  |
| +11.43 |  +7.89 | 00:34:30.204 | Real Betis         | Real Betis         | 57 | Carry           |   -   | [13.4, 35.7]    | Carry under control |
| +19.43 | +15.90 | 00:34:38.207 | Real Betis         | Real Betis         | 57 | Pass            |   -   | [13.2, 37.5]    | -> Alejandro More |

---

### Case 56: Episode `3938643_p115_6236351b`
- **Match**: `3938643` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **France** vs Possessing Team: **France**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `1288.03s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `91c5dfb2-f762-489a-94c6-77e19be7dfc3`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.52 |  -0.94 | 00:21:27.086 | Poland             | Poland             | 114 | Pass            |   -   | [91.9, 19.3]    | Incomplete (Incomplete) |
|  +0.97 |  -0.48 | 00:21:27.544 | Poland             | Poland             | 114 | Pressure        |   -   | [91.6, 14.7]    |  |
|  +1.46 |  +0.00 | 00:21:28.027 | Poland             | Poland             | 114 | Ball Receipt*   |   -   | [94.0, 14.7]    | Incomplete |
|  +1.46 |  +0.00 | 00:21:28.027 | France             | France             | 115 | Interception    |  Yes  | [25.7, 63.3]    | Won |
|  +1.46 |  +0.00 | 00:21:28.027 | France             | France             | 115 | Carry           |   -   | [25.7, 63.3]    | Carry under control |
|  +3.61 |  +2.15 | 00:21:30.180 | Poland             | France             | 115 | Pressure        |  Yes  | [98.6, 11.2]    |  |
| +11.15 |  +9.70 | 00:21:37.723 | France             | France             | 115 | Pass            |   -   | [51.9, 58.5]    | Incomplete (Incomplete) |
| +13.21 | +11.75 | 00:21:39.777 | France             | France             | 115 | Ball Receipt*   |   -   | [89.9, 47.8]    | Incomplete |
| +13.21 | +11.75 | 00:21:39.777 | Poland             | France             | 115 | Goal Keeper     |   -   | [28.8, 31.1]    |  |
| +17.06 | +15.61 | 00:21:43.633 | France             | France             | 115 | Pass            |   -   | [51.9, 17.6]    | -> Eduardo Camavi |
| +18.29 | +16.84 | 00:21:44.862 | France             | France             | 115 | Ball Receipt*   |   -   | [63.3, 18.9]    |  |
| +18.29 | +16.84 | 00:21:44.862 | France             | France             | 115 | Carry           |   -   | [63.3, 18.9]    | Carry under control |
| +19.05 | +17.59 | 00:21:45.620 | Poland             | France             | 115 | Pressure        |   -   | [58.0, 60.7]    |  |

---

### Case 57: Episode `3837662_p29_dfed3d1c`
- **Match**: `3837662` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Lille** vs Possessing Team: **Paris Saint-Germain**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `376.08s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `7a501a20-dcb0-43f9-95cf-c7bb5ca4c03a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +5.08 |  -1.95 | 00:06:14.132 | Paris Saint-Germai | Paris Saint-Germai | 28 | Carry           |   -   | [65.3, 74.3]    | Carry under control |
|  +6.85 |  -0.18 | 00:06:15.899 | Paris Saint-Germai | Paris Saint-Germai | 29 | Pass            |   -   | [77.9, 73.7]    | Incomplete (Incomplete) |
|  +7.03 |  -0.00 | 00:06:16.083 | Paris Saint-Germai | Paris Saint-Germai | 29 | Ball Receipt*   |   -   | [93.4, 60.5]    | Incomplete |
|  +7.03 |  -0.00 | 00:06:16.083 | Lille              | Paris Saint-Germai | 29 | Interception    |  Yes  | [34.8, 9.0]     | Won |
|  +7.03 |  -0.00 | 00:06:16.083 | Lille              | Paris Saint-Germai | 29 | Carry           |   -   | [34.8, 9.0]     | Carry under control |
| +10.39 |  +3.35 | 00:06:19.438 | Paris Saint-Germai | Paris Saint-Germai | 29 | Dribbled Past   |  Yes  | [65.7, 77.6]    |  |
| +10.39 |  +3.35 | 00:06:19.438 | Lille              | Paris Saint-Germai | 29 | Dribble         |   -   | [54.4, 2.5]     |  |
| +10.39 |  +3.35 | 00:06:19.438 | Lille              | Paris Saint-Germai | 29 | Carry           |   -   | [54.4, 2.5]     | Carry under control |
| +13.90 |  +6.87 | 00:06:22.950 | Paris Saint-Germai | Paris Saint-Germai | 29 | Pressure        |   -   | [46.3, 66.0]    |  |
| +19.09 | +12.05 | 00:06:28.138 | Lille              | Paris Saint-Germai | 29 | Pass            |   -   | [74.5, 24.3]    | Incomplete (Pass Offside) |
| +21.66 | +14.62 | 00:06:30.707 | Lille              | Paris Saint-Germai | 29 | Ball Receipt*   |   -   | [97.3, 3.5]     | Incomplete |
| +34.49 | +27.45 | 00:06:43.538 | Paris Saint-Germai | Paris Saint-Germai | 30 | Pass            |   -   | [22.8, 76.6]    | -> Marcos Aoás Co |
| +37.17 | +30.14 | 00:06:46.220 | Paris Saint-Germai | Paris Saint-Germai | 30 | Ball Receipt*   |   -   | [22.6, 57.8]    |  |

---

### Case 58: Episode `3901733_p111_c8513914`
- **Match**: `3901733` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Switzerland Women's** vs Possessing Team: **Switzerland Women's**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `934.44s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `ffd31460-87f6-4aea-b449-cb4053fd5eb6`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.17 |  -2.03 | 00:15:32.409 | Switzerland Women' | Spain Women's      | 110 | Pressure        |   -   | [53.1, 15.0]    |  |
|  +0.00 |  -0.86 | 00:15:33.581 | Spain Women's      | Spain Women's      | 110 | Pass            |   -   | [68.7, 74.0]    | Incomplete (Incomplete) |
|  +0.86 |  +0.00 | 00:15:34.443 | Spain Women's      | Spain Women's      | 110 | Ball Receipt*   |   -   | [80.3, 77.4]    | Incomplete |
|  +0.86 |  +0.00 | 00:15:34.443 | Switzerland Women' | Switzerland Women' | 111 | Interception    |  Yes  | [43.9, 3.4]     | Won |
|  +0.86 |  +0.00 | 00:15:34.443 | Switzerland Women' | Switzerland Women' | 111 | Carry           |   -   | [43.9, 3.4]     | Carry under control |
|  +6.18 |  +5.32 | 00:15:39.763 | Switzerland Women' | Switzerland Women' | 111 | Pass            |   -   | [62.0, 13.1]    | -> Ramona Bachman |
|  +7.15 |  +6.29 | 00:15:40.733 | Switzerland Women' | Switzerland Women' | 111 | Ball Receipt*   |   -   | [75.2, 4.0]     |  |
|  +7.15 |  +6.29 | 00:15:40.733 | Switzerland Women' | Switzerland Women' | 111 | Carry           |   -   | [75.2, 4.0]     | Carry under control |
| +10.63 |  +9.77 | 00:15:44.210 | Spain Women's      | Switzerland Women' | 111 | Pressure        |   -   | [43.0, 74.0]    |  |
| +10.98 | +10.12 | 00:15:44.561 | Switzerland Women' | Switzerland Women' | 111 | Pass            |   -   | [83.8, 3.7]     | -> Viola Calligar |
| +12.09 | +11.23 | 00:15:45.674 | Switzerland Women' | Switzerland Women' | 111 | Ball Receipt*   |   -   | [69.8, 5.0]     |  |
| +12.09 | +11.23 | 00:15:45.674 | Switzerland Women' | Switzerland Women' | 111 | Carry           |   -   | [69.8, 5.0]     | Carry under control |
| +12.19 | +11.33 | 00:15:45.774 | Spain Women's      | Switzerland Women' | 111 | Pressure        |   -   | [54.1, 73.7]    |  |

---

### Case 59: Episode `3895275_p57_340033b2`
- **Match**: `3895275` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Freiburg** vs Possessing Team: **Freiburg**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `2265.28s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `41ce2974-777f-4553-89cf-f57efba6057e`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +6.74 |  -0.67 | 00:37:44.608 | Bayer Leverkusen   | Bayer Leverkusen   | 56 | Ball Receipt*   |   -   | [71.8, 51.1]    |  |
|  +6.74 |  -0.67 | 00:37:44.608 | Bayer Leverkusen   | Bayer Leverkusen   | 56 | Pass            |   -   | [72.0, 52.3]    | Incomplete (Incomplete) |
|  +7.40 |  +0.00 | 00:37:45.275 | Bayer Leverkusen   | Bayer Leverkusen   | 56 | Ball Receipt*   |   -   | [78.1, 62.8]    | Incomplete |
|  +7.40 |  +0.00 | 00:37:45.275 | Freiburg           | Freiburg           | 57 | Interception    |  Yes  | [41.8, 21.3]    | Won |
|  +7.40 |  +0.00 | 00:37:45.275 | Freiburg           | Freiburg           | 57 | Carry           |   -   | [41.8, 21.3]    | Carry under control |
|  +7.79 |  +0.39 | 00:37:45.663 | Bayer Leverkusen   | Freiburg           | 57 | Pressure        |  Yes  | [78.5, 58.2]    |  |
|  +8.38 |  +0.97 | 00:37:46.248 | Freiburg           | Freiburg           | 57 | Pass            |   -   | [41.4, 23.3]    | -> Merlin Röhl |
|  +9.07 |  +1.66 | 00:37:46.940 | Freiburg           | Freiburg           | 57 | Ball Receipt*   |   -   | [50.8, 23.1]    |  |
|  +9.07 |  +1.66 | 00:37:46.940 | Freiburg           | Freiburg           | 57 | Carry           |   -   | [50.8, 23.1]    | Carry under control |
| +10.36 |  +2.95 | 00:37:48.229 | Freiburg           | Freiburg           | 57 | Pass            |   -   | [50.8, 23.7]    | -> Vincenzo Grifo |
| +11.49 |  +4.09 | 00:37:49.361 | Freiburg           | Freiburg           | 57 | Ball Receipt*   |   -   | [49.5, 33.1]    |  |
| +11.49 |  +4.09 | 00:37:49.361 | Freiburg           | Freiburg           | 57 | Carry           |   -   | [49.5, 33.1]    | Carry under control |
| +11.79 |  +4.39 | 00:37:49.666 | Freiburg           | Freiburg           | 57 | Pass            |   -   | [49.5, 33.1]    | -> Lucas Höler |

---

### Case 60: Episode `3857297_p126_adbbd377`
- **Match**: `3857297` (FIFA World Cup) | **Period**: 2
- **Counterpressing Team**: **Poland** vs Possessing Team: **Poland**
- **Stratum**: `interception` | **Evidence String**: `interception_plus_carry`
- **Timestamps**: Initiation: `1122.71s` | Acquisition dt: `0.0s` | Control dt: `0.0s` | Regain dt: `0.0s`
- **Control Event**: `Carry` (ID: `20a50fd4-40c2-4358-9019-4cfdf5c57d3b`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.0s)
  [ ] Controlled-possession verified (ctrl: 0.0s <= 5.0s)
  [ ] Evidence categorization valid (interception_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +1.39 |  -1.63 | 00:18:41.077 | Saudi Arabia       | Saudi Arabia       | 125 | Ball Receipt*   |   -   | [68.1, 8.1]     |  |
|  +1.87 |  -1.16 | 00:18:41.549 | Saudi Arabia       | Saudi Arabia       | 125 | Pass            |   -   | [67.4, 6.1]     | Incomplete (Incomplete) |
|  +3.03 |  +0.00 | 00:18:42.708 | Saudi Arabia       | Saudi Arabia       | 125 | Ball Receipt*   |   -   | [65.5, 1.4]     | Incomplete |
|  +3.03 |  +0.00 | 00:18:42.708 | Poland             | Poland             | 126 | Interception    |  Yes  | [52.4, 78.4]    | Won |
|  +3.03 |  +0.00 | 00:18:42.708 | Poland             | Poland             | 126 | Carry           |   -   | [52.4, 78.4]    | Carry under control |
|  +3.08 |  +0.05 | 00:18:42.762 | Saudi Arabia       | Poland             | 126 | Pressure        |  Yes  | [67.1, 1.4]     |  |
|  +3.88 |  +0.86 | 00:18:43.567 | Saudi Arabia       | Poland             | 126 | Foul Committed  |  Yes  | [69.3, 2.0]     |  |
|  +3.88 |  +0.86 | 00:18:43.567 | Poland             | Poland             | 126 | Foul Won        |   -   | [50.8, 78.1]    |  |
| +28.34 | +25.31 | 00:19:08.021 | Poland             | Poland             | 127 | Pass            |   -   | [50.5, 77.8]    | -> Jakub Piotr Ki |
| +30.44 | +27.42 | 00:19:10.126 | Poland             | Poland             | 127 | Ball Receipt*   |   -   | [31.8, 45.6]    |  |
| +30.44 | +27.42 | 00:19:10.126 | Poland             | Poland             | 127 | Carry           |   -   | [31.8, 45.6]    | Carry under control |
| +34.07 | +31.04 | 00:19:13.749 | Poland             | Poland             | 127 | Pass            |   -   | [31.4, 43.8]    | -> Wojciech Szczę |
| +36.16 | +33.13 | 00:19:15.840 | Poland             | Poland             | 127 | Ball Receipt*   |   -   | [13.6, 46.6]    |  |

---

### Case 61: Episode `3869420_p42_6cb0234d`
- **Match**: `3869420` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Brazil** vs Possessing Team: **Croatia**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1230.90s` | Acquisition dt: `1.64s` | Control dt: `1.64s` | Regain dt: `1.64s`
- **Control Event**: `Pass` (ID: `43580e77-14b0-410b-bf32-ba16d30408d1`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.64s)
  [ ] Controlled-possession verified (ctrl: 1.64s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +3.62 |  -0.24 | 00:20:30.654 | Croatia            | Croatia            | 41 | Ball Receipt*   |   -   | [39.4, 8.0]     |  |
|  +3.70 |  -0.16 | 00:20:30.734 | Croatia            | Croatia            | 42 | Pass            |   -   | [39.4, 8.0]     | Incomplete (Incomplete) |
|  +3.87 |  +0.00 | 00:20:30.899 | Croatia            | Croatia            | 42 | Ball Receipt*   |   -   | [66.3, 15.7]    | Incomplete |
|  +3.87 |  +0.00 | 00:20:30.899 | Brazil             | Croatia            | 42 | Block           |  Yes  | [77.9, 71.1]    |  |
|  +5.51 |  +1.64 | 00:20:32.539 | Brazil             | Brazil             | 43 | Pass            |   -   | [75.4, 68.2]    | -> Lucas Tolentin |
|  +6.17 |  +2.30 | 00:20:33.201 | Brazil             | Brazil             | 43 | Ball Receipt*   |   -   | [80.7, 57.2]    |  |
|  +6.17 |  +2.30 | 00:20:33.201 | Brazil             | Brazil             | 43 | Carry           |   -   | [80.7, 57.2]    | Carry under control |
|  +8.38 |  +4.51 | 00:20:35.411 | Brazil             | Brazil             | 43 | Pass            |   -   | [80.7, 57.2]    | -> Neymar da Silv |
|  +9.16 |  +5.29 | 00:20:36.192 | Brazil             | Brazil             | 43 | Ball Receipt*   |   -   | [93.7, 40.1]    |  |
|  +9.16 |  +5.29 | 00:20:36.192 | Brazil             | Brazil             | 43 | Carry           |   -   | [93.7, 40.1]    | Carry under control |
| +10.03 |  +6.16 | 00:20:37.060 | Brazil             | Brazil             | 43 | Pass            |   -   | [94.9, 37.4]    | -> Vinícius José  |
| +10.51 |  +6.65 | 00:20:37.544 | Brazil             | Brazil             | 43 | Ball Receipt*   |   -   | [103.8, 34.0]   |  |
| +10.51 |  +6.65 | 00:20:37.544 | Brazil             | Brazil             | 43 | Miscontrol      |   -   | [103.8, 34.0]   | Opponent Miscontrol |

---

### Case 62: Episode `3835334_p172_f4cc91b8`
- **Match**: `3835334` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Italy Women's** vs Possessing Team: **Iceland Women's**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2208.81s` | Acquisition dt: `1.56s` | Control dt: `1.56s` | Regain dt: `1.56s`
- **Control Event**: `Pass` (ID: `8df9371b-7f06-4844-811a-fedcfdaf43ae`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.56s)
  [ ] Controlled-possession verified (ctrl: 1.56s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.31 |  -2.47 | 00:36:46.331 | Iceland Women's    | Iceland Women's    | 172 | Pass            |   -   | [11.3, 64.8]    | -> Sveindís Jane  |
|  +4.57 |  -0.22 | 00:36:48.589 | Iceland Women's    | Iceland Women's    | 172 | Ball Receipt*   |   -   | [55.2, 69.1]    |  |
|  +4.57 |  -0.22 | 00:36:48.589 | Iceland Women's    | Iceland Women's    | 172 | Miscontrol      |   -   | [55.2, 69.1]    | Opponent Miscontrol |
|  +4.78 |  +0.00 | 00:36:48.806 | Italy Women's      | Iceland Women's    | 172 | Block           |  Yes  | [61.2, 12.1]    |  |
|  +5.85 |  +1.07 | 00:36:49.871 | Iceland Women's    | Iceland Women's    | 172 | Pressure        |   -   | [65.3, 66.4]    |  |
|  +6.34 |  +1.56 | 00:36:50.366 | Italy Women's      | Italy Women's      | 173 | Pass            |   -   | [53.2, 18.0]    | -> Laura Giuliani |
|  +9.70 |  +4.92 | 00:36:53.725 | Italy Women's      | Italy Women's      | 173 | Ball Receipt*   |   -   | [20.5, 39.0]    |  |
|  +9.70 |  +4.92 | 00:36:53.725 | Italy Women's      | Italy Women's      | 173 | Carry           |   -   | [20.5, 39.0]    | Carry under control |
| +11.06 |  +6.28 | 00:36:55.084 | Iceland Women's    | Italy Women's      | 173 | Pressure        |  Yes  | [94.8, 39.0]    |  |
| +11.21 |  +6.43 | 00:36:55.238 | Italy Women's      | Italy Women's      | 173 | Pass            |   -   | [19.2, 44.5]    | -> Elena Linari |
| +13.07 |  +8.29 | 00:36:57.094 | Italy Women's      | Italy Women's      | 173 | Ball Receipt*   |   -   | [28.5, 21.7]    |  |
| +13.07 |  +8.29 | 00:36:57.094 | Italy Women's      | Italy Women's      | 173 | Carry           |   -   | [28.5, 21.7]    | Carry under control |
| +17.20 | +12.42 | 00:37:01.223 | Italy Women's      | Italy Women's      | 173 | Pass            |   -   | [47.1, 26.2]    | -> Flaminia Simon |

---

### Case 63: Episode `3788769_p11_eeff3c23`
- **Match**: `3788769` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Denmark** vs Possessing Team: **Russia**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `149.98s` | Acquisition dt: `2.829s` | Control dt: `2.829s` | Regain dt: `2.829s`
- **Control Event**: `Pass` (ID: `8ff60f74-ac31-41db-9639-e2c70e9661da`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.829s)
  [ ] Controlled-possession verified (ctrl: 2.829s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.39 |  -1.69 | 00:02:28.291 | Russia             | Russia             | 11 | Ball Receipt*   |   -   | [43.9, 3.7]     |  |
|  +2.39 |  -1.69 | 00:02:28.291 | Russia             | Russia             | 11 | Carry           |   -   | [43.9, 3.7]     | Carry under control |
|  +3.16 |  -0.92 | 00:02:29.061 | Russia             | Russia             | 11 | Pass            |   -   | [49.6, 2.5]     | -> Artem Dzyuba |
|  +4.08 |  +0.00 | 00:02:29.980 | Denmark            | Russia             | 11 | Pressure        |  Yes  | [50.8, 68.6]    |  |
|  +4.59 |  +0.52 | 00:02:30.498 | Russia             | Russia             | 11 | Ball Receipt*   |   -   | [65.9, 8.7]     |  |
|  +4.59 |  +0.52 | 00:02:30.498 | Russia             | Russia             | 11 | Carry           |   -   | [65.9, 8.7]     | Carry under control |
|  +4.81 |  +0.74 | 00:02:30.715 | Russia             | Russia             | 11 | Miscontrol      |   -   | [68.4, 10.1]    | Opponent Miscontrol |
|  +4.88 |  +0.81 | 00:02:30.787 | Denmark            | Russia             | 11 | Pressure        |  Yes  | [48.9, 68.4]    |  |
|  +6.09 |  +2.01 | 00:02:31.992 | Denmark            | Russia             | 11 | Pressure        |   -   | [53.7, 70.9]    |  |
|  +6.26 |  +2.19 | 00:02:32.167 | Russia             | Russia             | 11 | Ball Recovery   |   -   | [65.0, 11.9]    |  |
|  +6.91 |  +2.83 | 00:02:32.809 | Denmark            | Denmark            | 12 | Pass            |   -   | [54.9, 70.7]    | -> Andreas Christ |
|  +7.61 |  +3.53 | 00:02:33.509 | Denmark            | Denmark            | 12 | Ball Receipt*   |   -   | [43.4, 70.5]    |  |
|  +7.61 |  +3.53 | 00:02:33.509 | Denmark            | Denmark            | 12 | Carry           |   -   | [43.4, 70.5]    | Carry under control |

---

### Case 64: Episode `3773387_p86_3090614c`
- **Match**: `3773387` (La Liga) | **Period**: 2
- **Counterpressing Team**: **Levante UD** vs Possessing Team: **Barcelona**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `347.79s` | Acquisition dt: `1.65s` | Control dt: `1.65s` | Regain dt: `1.65s`
- **Control Event**: `Pass` (ID: `dd005b68-3758-464d-aee3-a203972ac8ef`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.65s)
  [ ] Controlled-possession verified (ctrl: 1.65s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.84 |  -0.67 | 00:05:47.121 | Barcelona          | Barcelona          | 86 | Carry           |   -   | [49.5, 18.2]    | Carry under control |
|  +1.19 |  -0.32 | 00:05:47.476 | Barcelona          | Barcelona          | 86 | Pass            |   -   | [49.5, 18.2]    | Incomplete (Incomplete) |
|  +1.51 |  +0.00 | 00:05:47.793 | Barcelona          | Barcelona          | 86 | Ball Receipt*   |   -   | [64.7, 17.7]    | Incomplete |
|  +1.51 |  +0.00 | 00:05:47.793 | Levante UD         | Barcelona          | 86 | Block           |  Yes  | [65.3, 61.3]    |  |
|  +3.16 |  +1.65 | 00:05:49.443 | Levante UD         | Levante UD         | 87 | Pass            |   -   | [61.5, 59.5]    | -> Rúben Miguel N |
|  +4.03 |  +2.52 | 00:05:50.310 | Levante UD         | Levante UD         | 87 | Ball Receipt*   |   -   | [50.7, 64.2]    |  |
|  +4.03 |  +2.52 | 00:05:50.310 | Levante UD         | Levante UD         | 87 | Pass            |   -   | [50.7, 64.2]    | -> Jorge De Fruto |
|  +5.11 |  +3.60 | 00:05:51.389 | Levante UD         | Levante UD         | 87 | Ball Receipt*   |   -   | [61.5, 75.9]    |  |
|  +5.11 |  +3.60 | 00:05:51.389 | Levante UD         | Levante UD         | 87 | Carry           |   -   | [61.5, 75.9]    | Carry under control |
|  +6.68 |  +5.17 | 00:05:52.962 | Barcelona          | Levante UD         | 87 | Pressure        |  Yes  | [62.7, 6.9]     |  |
|  +7.71 |  +6.20 | 00:05:53.996 | Levante UD         | Levante UD         | 87 | Pass            |   -   | [63.6, 76.1]    | Incomplete (Incomplete) |
|  +9.34 |  +7.83 | 00:05:55.622 | Levante UD         | Levante UD         | 87 | Ball Receipt*   |   -   | [88.9, 56.3]    | Incomplete |
|  +9.34 |  +7.83 | 00:05:55.622 | Barcelona          | Barcelona          | 88 | Pass            |  Yes  | [31.8, 20.0]    | -> Jordi Alba Ram |

---

### Case 65: Episode `3802930_p145_4b8096a7`
- **Match**: `3802930` (Ligue 1) | **Period**: 2
- **Counterpressing Team**: **Troyes** vs Possessing Team: **Paris Saint-Germain**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2025.46s` | Acquisition dt: `2.142s` | Control dt: `2.142s` | Regain dt: `2.142s`
- **Control Event**: `Pass` (ID: `5c60b80c-0acd-4af3-9b52-8d8b4adcb4e6`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.142s)
  [ ] Controlled-possession verified (ctrl: 2.142s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.72 |  -2.55 | 00:33:42.911 | Troyes             | Troyes             | 144 | Miscontrol      |   -   | [12.1, 15.9]    | Opponent Miscontrol |
|  -0.68 |  -1.50 | 00:33:43.954 | Troyes             | Troyes             | 144 | Pressure        |   -   | [14.5, 17.2]    |  |
|  +0.00 |  -0.83 | 00:33:44.632 | Paris Saint-Germai | Paris Saint-Germai | 145 | Pass            |   -   | [104.9, 60.5]   | -> Idrissa Gana G |
|  +0.83 |  +0.00 | 00:33:45.457 | Troyes             | Paris Saint-Germai | 145 | Pressure        |  Yes  | [26.6, 18.3]    |  |
|  +0.92 |  +0.09 | 00:33:45.548 | Paris Saint-Germai | Paris Saint-Germai | 145 | Ball Receipt*   |   -   | [93.4, 59.5]    |  |
|  +0.92 |  +0.09 | 00:33:45.548 | Paris Saint-Germai | Paris Saint-Germai | 145 | Carry           |   -   | [93.4, 59.5]    | Carry under control |
|  +1.62 |  +0.80 | 00:33:46.254 | Paris Saint-Germai | Paris Saint-Germai | 145 | Shot            |   -   | [96.5, 59.1]    | Blocked |
|  +1.88 |  +1.06 | 00:33:46.515 | Troyes             | Paris Saint-Germai | 145 | Block           |  Yes  | [19.3, 24.1]    |  |
|  +2.30 |  +1.48 | 00:33:46.936 | Troyes             | Paris Saint-Germai | 145 | Goal Keeper     |   -   | [3.0, 37.5]     |  |
|  +2.97 |  +2.14 | 00:33:47.599 | Troyes             | Troyes             | 146 | Pass            |   -   | [19.2, 29.8]    | -> Florian Tardie |
|  +4.04 |  +3.22 | 00:33:48.674 | Troyes             | Troyes             | 146 | Ball Receipt*   |   -   | [21.5, 24.7]    |  |
|  +4.04 |  +3.22 | 00:33:48.674 | Troyes             | Troyes             | 146 | Carry           |   -   | [21.5, 24.7]    | Carry under control |
|  +4.15 |  +3.33 | 00:33:48.787 | Paris Saint-Germai | Troyes             | 146 | Pressure        |  Yes  | [96.9, 55.4]    |  |

---

### Case 66: Episode `3837827_p33_a118a717`
- **Match**: `3837827` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Rennes**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1114.61s` | Acquisition dt: `1.101s` | Control dt: `1.101s` | Regain dt: `1.101s`
- **Control Event**: `Pass` (ID: `69c55c30-1e03-4179-9da0-240d9ebe2e34`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.101s)
  [ ] Controlled-possession verified (ctrl: 1.101s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.69 | 00:18:33.925 | Rennes             | Rennes             | 33 | Ball Recovery   |   -   | [66.2, 40.0]    |  |
|  +0.00 |  -0.69 | 00:18:33.925 | Rennes             | Rennes             | 33 | Carry           |   -   | [66.2, 40.0]    | Carry under control |
|  +0.69 |  +0.00 | 00:18:34.613 | Rennes             | Rennes             | 33 | Dispossessed    |   -   | [71.5, 39.4]    | Opponent Dispossessed |
|  +0.69 |  +0.00 | 00:18:34.613 | Paris Saint-Germai | Rennes             | 33 | Duel            |  Yes  | [48.6, 40.7]    | Tackle, Lost In Play |
|  +1.38 |  +0.69 | 00:18:35.300 | Rennes             | Rennes             | 33 | Ball Recovery   |   -   | [78.9, 38.9]    |  |
|  +1.38 |  +0.69 | 00:18:35.300 | Rennes             | Rennes             | 33 | Carry           |   -   | [78.9, 38.9]    | Carry under control |
|  +1.79 |  +1.10 | 00:18:35.714 | Paris Saint-Germai | Paris Saint-Germai | 34 | Pass            |   -   | [43.1, 40.9]    | -> Marcos Aoás Co |
|  +1.93 |  +1.24 | 00:18:35.855 | Paris Saint-Germai | Paris Saint-Germai | 34 | Ball Receipt*   |   -   | [34.1, 41.1]    |  |
|  +1.93 |  +1.24 | 00:18:35.855 | Paris Saint-Germai | Paris Saint-Germai | 34 | Carry           |   -   | [34.1, 41.1]    | Carry under control |
|  +1.93 |  +1.24 | 00:18:35.855 | Rennes             | Paris Saint-Germai | 34 | Miscontrol      |   -   | [78.9, 38.6]    | Opponent Miscontrol |
|  +4.99 |  +4.30 | 00:18:38.912 | Paris Saint-Germai | Paris Saint-Germai | 34 | Pass            |   -   | [35.9, 47.6]    | -> Vitor Machado  |
|  +5.77 |  +5.08 | 00:18:39.695 | Paris Saint-Germai | Paris Saint-Germai | 34 | Ball Receipt*   |   -   | [42.8, 40.7]    |  |
|  +5.77 |  +5.08 | 00:18:39.695 | Paris Saint-Germai | Paris Saint-Germai | 34 | Carry           |   -   | [42.8, 40.7]    | Carry under control |

---

### Case 67: Episode `3930171_p134_38336005`
- **Match**: `3930171` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **England** vs Possessing Team: **Denmark**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2473.47s` | Acquisition dt: `1.369s` | Control dt: `1.369s` | Regain dt: `1.369s`
- **Control Event**: `Pass` (ID: `762b2d61-b88e-4ab5-8ada-75653cb14448`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.369s)
  [ ] Controlled-possession verified (ctrl: 1.369s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.13 |  -0.16 | 00:41:13.314 | Denmark            | Denmark            | 134 | Ball Receipt*   |   -   | [76.4, 62.5]    |  |
|  +2.13 |  -0.16 | 00:41:13.314 | Denmark            | Denmark            | 134 | Pass            |   -   | [77.5, 63.0]    | Incomplete (Incomplete) |
|  +2.29 |  +0.00 | 00:41:13.469 | Denmark            | Denmark            | 134 | Ball Receipt*   |   -   | [85.7, 63.9]    | Incomplete |
|  +2.29 |  +0.00 | 00:41:13.469 | England            | Denmark            | 134 | Block           |  Yes  | [39.2, 17.1]    |  |
|  +3.66 |  +1.37 | 00:41:14.838 | England            | England            | 135 | Pass            |   -   | [43.7, 11.8]    | -> Declan Rice |
|  +4.24 |  +1.95 | 00:41:15.419 | England            | England            | 135 | Ball Receipt*   |   -   | [40.9, 14.5]    |  |
|  +4.24 |  +1.95 | 00:41:15.419 | England            | England            | 135 | Pass            |   -   | [40.4, 15.1]    | -> Eberechi Eze |
|  +4.98 |  +2.69 | 00:41:16.161 | England            | England            | 135 | Ball Receipt*   |   -   | [42.3, 7.6]     |  |
|  +4.98 |  +2.69 | 00:41:16.161 | England            | England            | 135 | Carry           |   -   | [42.3, 7.6]     | Carry under control |
|  +5.83 |  +3.54 | 00:41:17.009 | England            | England            | 135 | Pass            |   -   | [42.2, 7.6]     | Incomplete (Incomplete) |
|  +6.15 |  +3.87 | 00:41:17.335 | England            | England            | 135 | Ball Receipt*   |   -   | [32.0, 14.9]    | Incomplete |
|  +6.15 |  +3.87 | 00:41:17.335 | Denmark            | England            | 135 | Pass            |  Yes  | [84.5, 67.7]    | Incomplete (Incomplete) |
|  +7.97 |  +5.69 | 00:41:19.156 | Denmark            | England            | 135 | Pressure        |  Yes  | [70.0, 59.1]    |  |

---

### Case 68: Episode `3773403_p166_8fad00e5`
- **Match**: `3773403` (La Liga) | **Period**: 2
- **Counterpressing Team**: **Athletic Club** vs Possessing Team: **Barcelona**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2427.84s` | Acquisition dt: `4.252s` | Control dt: `4.252s` | Regain dt: `4.252s`
- **Control Event**: `Pass` (ID: `e6c621d5-275d-45ad-8e4b-bb9fac66068c`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.252s)
  [ ] Controlled-possession verified (ctrl: 4.252s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -3.85 | 00:40:23.984 | Barcelona          | Barcelona          | 166 | Pass            |   -   | [22.5, 52.3]    | -> Marc-André ter |
|  +2.32 |  -1.53 | 00:40:26.306 | Barcelona          | Barcelona          | 166 | Ball Receipt*   |   -   | [2.7, 40.5]     |  |
|  +2.32 |  -1.53 | 00:40:26.306 | Barcelona          | Barcelona          | 166 | Carry           |   -   | [2.7, 40.5]     | Carry under control |
|  +3.85 |  +0.00 | 00:40:27.837 | Athletic Club      | Barcelona          | 166 | Pressure        |  Yes  | [112.6, 41.4]   |  |
|  +4.46 |  +0.61 | 00:40:28.443 | Barcelona          | Barcelona          | 166 | Pass            |   -   | [8.6, 36.4]     | -> Jordi Alba Ram |
|  +6.88 |  +3.03 | 00:40:30.867 | Barcelona          | Barcelona          | 166 | Ball Receipt*   |   -   | [35.4, 6.4]     |  |
|  +6.88 |  +3.03 | 00:40:30.867 | Barcelona          | Barcelona          | 166 | Pass            |   -   | [36.6, 6.4]     | -> Pedro González |
|  +8.10 |  +4.24 | 00:40:32.081 | Barcelona          | Barcelona          | 166 | Ball Receipt*   |   -   | [43.9, 15.0]    |  |
|  +8.10 |  +4.24 | 00:40:32.081 | Barcelona          | Barcelona          | 166 | Carry           |   -   | [43.9, 15.0]    | Carry under control |
|  +8.11 |  +4.25 | 00:40:32.089 | Athletic Club      | Athletic Club      | 167 | Pass            |  Yes  | [74.5, 63.3]    | -> Alejandro Bere |
|  +8.14 |  +4.28 | 00:40:32.121 | Athletic Club      | Athletic Club      | 167 | Ball Receipt*   |   -   | [85.6, 62.9]    |  |
|  +8.14 |  +4.28 | 00:40:32.121 | Athletic Club      | Athletic Club      | 167 | Carry           |   -   | [85.6, 62.9]    | Carry under control |
|  +8.14 |  +4.28 | 00:40:32.121 | Barcelona          | Athletic Club      | 167 | Miscontrol      |   -   | [35.4, 21.2]    | Opponent Miscontrol |

---

### Case 69: Episode `3835324_p94_5383d6fe`
- **Match**: `3835324` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Netherlands Women's** vs Possessing Team: **Netherlands Women's**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2825.72s` | Acquisition dt: `4.319s` | Control dt: `4.319s` | Regain dt: `4.319s`
- **Control Event**: `Pass` (ID: `7dd483a3-bf51-445d-9bbb-3a379c08d17f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.319s)
  [ ] Controlled-possession verified (ctrl: 4.319s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.00 |  -1.89 | 00:47:03.829 | Netherlands Women' | Netherlands Women' | 94 | Ball Receipt*   |   -   | [50.5, 2.3]     |  |
|  -0.00 |  -1.89 | 00:47:03.829 | Netherlands Women' | Netherlands Women' | 94 | Carry           |   -   | [50.5, 2.3]     | Carry under control |
|  +0.00 |  -1.89 | 00:47:03.834 | Netherlands Women' | Netherlands Women' | 94 | Miscontrol      |   -   | [49.9, 2.0]     | Opponent Miscontrol |
|  +1.89 |  +0.00 | 00:47:05.721 | Netherlands Women' | Netherlands Women' | 94 | Pressure        |  Yes  | [42.2, 2.1]     |  |
|  +1.97 |  +0.08 | 00:47:05.801 | Sweden Women's     | Netherlands Women' | 94 | Ball Recovery   |   -   | [76.2, 77.6]    |  |
|  +6.21 |  +4.32 | 00:47:10.040 | Netherlands Women' | Netherlands Women' | 95 | Pass            |   -   | [44.8, 0.1]     | -> Dominique Joha |
|  +7.94 |  +6.05 | 00:47:11.774 | Netherlands Women' | Netherlands Women' | 95 | Ball Receipt*   |   -   | [28.9, 15.1]    |  |
|  +7.94 |  +6.05 | 00:47:11.774 | Netherlands Women' | Netherlands Women' | 95 | Carry           |   -   | [28.9, 15.1]    | Carry under control |
| +12.18 | +10.29 | 00:47:16.009 | Netherlands Women' | Netherlands Women' | 95 | Pass            |   -   | [25.9, 19.6]    | -> Sherida Spitse |
| +13.10 | +11.21 | 00:47:16.929 | Netherlands Women' | Netherlands Women' | 95 | Ball Receipt*   |   -   | [30.6, 14.5]    |  |
| +13.10 | +11.21 | 00:47:16.929 | Netherlands Women' | Netherlands Women' | 95 | Carry           |   -   | [30.6, 14.5]    | Carry under control |
| +13.18 | +11.29 | 00:47:17.009 | Netherlands Women' | Netherlands Women' | 95 | Pass            |   -   | [30.6, 14.5]    | -> Dominique Joha |
| +14.25 | +12.36 | 00:47:18.080 | Netherlands Women' | Netherlands Women' | 95 | Ball Receipt*   |   -   | [26.8, 23.0]    |  |

---

### Case 70: Episode `3844385_p59_8ae70983`
- **Match**: `3844385` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Austria Women's** vs Possessing Team: **Austria Women's**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1436.03s` | Acquisition dt: `4.992s` | Control dt: `4.992s` | Regain dt: `4.992s`
- **Control Event**: `Pass` (ID: `d6d99466-9f04-4c33-89a5-fde1397ec385`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.992s)
  [ ] Controlled-possession verified (ctrl: 4.992s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.60 |  -1.97 | 00:23:54.059 | Austria Women's    | Austria Women's    | 59 | Miscontrol      |   -   | [43.0, 10.4]    | Opponent Miscontrol |
|  +0.00 |  -0.36 | 00:23:55.662 | Germany Women's    | Austria Women's    | 59 | Ball Recovery   |   -   | [79.6, 69.5]    |  |
|  +0.00 |  -0.36 | 00:23:55.662 | Germany Women's    | Austria Women's    | 59 | Carry           |   -   | [79.6, 69.5]    | Carry under control |
|  +0.36 |  +0.00 | 00:23:56.025 | Austria Women's    | Austria Women's    | 59 | Pressure        |  Yes  | [41.5, 7.9]     |  |
|  +1.76 |  +1.40 | 00:23:57.427 | Germany Women's    | Austria Women's    | 59 | Dispossessed    |   -   | [78.6, 73.9]    | Opponent Dispossessed |
|  +1.76 |  +1.40 | 00:23:57.427 | Austria Women's    | Austria Women's    | 59 | Duel            |  Yes  | [41.5, 6.2]     | Tackle, Lost In Play |
|  +2.22 |  +1.86 | 00:23:57.883 | Germany Women's    | Austria Women's    | 59 | Ball Recovery   |   -   | [80.7, 74.2]    |  |
|  +5.36 |  +4.99 | 00:24:01.017 | Austria Women's    | Austria Women's    | 60 | Pass            |   -   | [36.2, 0.1]     | -> Barbara Dunst |
|  +6.16 |  +5.80 | 00:24:01.823 | Austria Women's    | Austria Women's    | 60 | Ball Receipt*   |   -   | [48.0, 5.1]     |  |
|  +6.16 |  +5.80 | 00:24:01.823 | Austria Women's    | Austria Women's    | 60 | Miscontrol      |   -   | [48.0, 5.1]     | Opponent Miscontrol |
|  +7.89 |  +7.52 | 00:24:03.550 | Germany Women's    | Austria Women's    | 60 | Clearance       |   -   | [63.4, 74.2]    |  |
| +26.04 | +25.68 | 00:24:21.706 | Austria Women's    | Austria Women's    | 61 | Pass            |   -   | [56.7, 0.1]     | -> Laura Feiersin |
| +26.80 | +26.43 | 00:24:22.457 | Austria Women's    | Austria Women's    | 61 | Ball Receipt*   |   -   | [64.4, 10.2]    |  |

---

### Case 71: Episode `3788761_p65_e834ba0d`
- **Match**: `3788761` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Slovakia** vs Possessing Team: **Sweden**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2635.89s` | Acquisition dt: `2.848s` | Control dt: `2.848s` | Regain dt: `2.848s`
- **Control Event**: `Pass` (ID: `47827745-1880-4165-9adf-54a843919052`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.848s)
  [ ] Controlled-possession verified (ctrl: 2.848s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.06 |  -2.16 | 00:43:53.728 | Sweden             | Sweden             | 65 | Ball Receipt*   |   -   | [15.4, 49.5]    |  |
|  +2.06 |  -2.16 | 00:43:53.728 | Sweden             | Sweden             | 65 | Carry           |   -   | [15.4, 49.5]    | Carry under control |
|  +3.44 |  -0.78 | 00:43:55.103 | Sweden             | Sweden             | 65 | Pass            |   -   | [20.1, 52.1]    | -> Marcus Berg |
|  +4.22 |  +0.00 | 00:43:55.885 | Slovakia           | Sweden             | 65 | Pressure        |  Yes  | [72.6, 22.5]    |  |
|  +5.14 |  +0.92 | 00:43:56.808 | Sweden             | Sweden             | 65 | Ball Receipt*   |   -   | [44.5, 57.0]    |  |
|  +5.14 |  +0.92 | 00:43:56.808 | Sweden             | Sweden             | 65 | Pass            |   -   | [44.2, 56.4]    | Incomplete (Incomplete) |
|  +5.14 |  +0.92 | 00:43:56.808 | Slovakia           | Sweden             | 65 | Duel            |  Yes  | [75.9, 23.7]    | Aerial Lost |
|  +5.96 |  +1.74 | 00:43:57.624 | Sweden             | Sweden             | 65 | Ball Receipt*   |   -   | [44.6, 65.8]    | Incomplete |
|  +5.96 |  +1.74 | 00:43:57.624 | Slovakia           | Sweden             | 65 | Clearance       |   -   | [71.2, 10.7]    |  |
|  +7.07 |  +2.85 | 00:43:58.733 | Slovakia           | Slovakia           | 66 | Pass            |   -   | [86.6, 21.1]    | -> Róbert Mak |
|  +8.33 |  +4.11 | 00:43:59.997 | Slovakia           | Slovakia           | 66 | Ball Receipt*   |   -   | [85.8, 8.0]     |  |
|  +8.33 |  +4.11 | 00:43:59.997 | Slovakia           | Slovakia           | 66 | Carry           |   -   | [85.8, 8.0]     | Carry under control |
| +11.41 |  +7.19 | 00:44:03.080 | Slovakia           | Slovakia           | 66 | Pass            |   -   | [94.1, 13.8]    | -> Ondrej Duda |

---

### Case 72: Episode `3773372_p103_2d41b247`
- **Match**: `3773372` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Barcelona** vs Possessing Team: **Barcelona**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `2067.53s` | Acquisition dt: `4.531s` | Control dt: `4.531s` | Regain dt: `4.531s`
- **Control Event**: `Pass` (ID: `d47e19da-7649-413b-b2f4-d7478f8fd0f1`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.531s)
  [ ] Controlled-possession verified (ctrl: 4.531s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.32 |  -3.59 | 00:34:23.944 | Barcelona          | Barcelona          | 103 | Pass            |   -   | [4.6, 46.4]     | Incomplete (Incomplete) |
|  +0.00 |  -1.27 | 00:34:26.259 | Barcelona          | Barcelona          | 103 | Ball Receipt*   |   -   | [53.2, 24.5]    | Incomplete |
|  +0.00 |  -1.27 | 00:34:26.259 | Atlético Madrid    | Barcelona          | 103 | Pass            |   -   | [70.9, 50.2]    | -> Jorge Resurrec |
|  +1.27 |  +0.00 | 00:34:27.530 | Barcelona          | Barcelona          | 103 | Pressure        |  Yes  | [39.3, 40.4]    |  |
|  +1.74 |  +0.47 | 00:34:28.002 | Atlético Madrid    | Barcelona          | 103 | Ball Receipt*   |   -   | [80.1, 43.8]    |  |
|  +1.74 |  +0.47 | 00:34:28.002 | Atlético Madrid    | Barcelona          | 103 | Carry           |   -   | [80.1, 43.8]    | Carry under control |
|  +2.43 |  +1.16 | 00:34:28.688 | Atlético Madrid    | Barcelona          | 103 | Foul Committed  |   -   | [80.8, 45.2]    |  |
|  +5.80 |  +4.53 | 00:34:32.061 | Barcelona          | Barcelona          | 104 | Pass            |   -   | [34.2, 43.8]    | -> Sergino Dest |
|  +7.04 |  +5.77 | 00:34:33.301 | Barcelona          | Barcelona          | 104 | Ball Receipt*   |   -   | [36.5, 57.2]    |  |
|  +7.04 |  +5.77 | 00:34:33.301 | Barcelona          | Barcelona          | 104 | Carry           |   -   | [36.5, 57.2]    | Carry under control |
|  +7.86 |  +6.59 | 00:34:34.123 | Barcelona          | Barcelona          | 104 | Pass            |   -   | [37.6, 59.7]    | -> Lionel Andrés  |
|  +9.12 |  +7.85 | 00:34:35.376 | Barcelona          | Barcelona          | 104 | Ball Receipt*   |   -   | [55.3, 72.7]    |  |
|  +9.12 |  +7.85 | 00:34:35.376 | Barcelona          | Barcelona          | 104 | Carry           |   -   | [55.3, 72.7]    | Carry under control |

---

### Case 73: Episode `3802690_p31_b8cf0496`
- **Match**: `3802690` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Lorient** vs Possessing Team: **Paris Saint-Germain**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `963.76s` | Acquisition dt: `1.908s` | Control dt: `1.908s` | Regain dt: `1.908s`
- **Control Event**: `Pass` (ID: `86006a7a-d220-43ef-a9a0-76d83e04eea3`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.908s)
  [ ] Controlled-possession verified (ctrl: 1.908s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +4.47 |  -2.99 | 00:16:00.778 | Paris Saint-Germai | Paris Saint-Germai | 30 | Carry           |   -   | [47.5, 48.1]    | Carry under control |
|  +7.33 |  -0.13 | 00:16:03.635 | Paris Saint-Germai | Paris Saint-Germai | 31 | Pass            |   -   | [62.9, 43.6]    | Incomplete (Incomplete) |
|  +7.46 |  +0.00 | 00:16:03.763 | Paris Saint-Germai | Paris Saint-Germai | 31 | Ball Receipt*   |   -   | [76.9, 47.8]    | Incomplete |
|  +7.46 |  +0.00 | 00:16:03.763 | Lorient            | Paris Saint-Germai | 31 | Block           |  Yes  | [53.5, 36.5]    |  |
|  +9.37 |  +1.91 | 00:16:05.671 | Lorient            | Lorient            | 32 | Pass            |   -   | [67.4, 34.8]    | -> Laurent Aberge |
| +10.35 |  +2.89 | 00:16:06.650 | Lorient            | Lorient            | 32 | Ball Receipt*   |   -   | [62.7, 33.3]    |  |
| +10.35 |  +2.89 | 00:16:06.650 | Lorient            | Lorient            | 32 | Carry           |   -   | [62.7, 33.3]    | Carry under control |
| +12.72 |  +5.26 | 00:16:09.021 | Lorient            | Lorient            | 32 | Pass            |   -   | [81.3, 37.2]    | -> Armand Laurien |
| +14.34 |  +6.89 | 00:16:10.649 | Lorient            | Lorient            | 32 | Ball Receipt*   |   -   | [99.3, 23.5]    |  |
| +14.34 |  +6.89 | 00:16:10.649 | Lorient            | Lorient            | 32 | Carry           |   -   | [99.3, 23.5]    | Carry under control |
| +18.96 | +11.50 | 00:16:15.264 | Lorient            | Lorient            | 32 | Shot            |   -   | [113.8, 22.3]   | Saved |
| +19.80 | +12.34 | 00:16:16.106 | Paris Saint-Germai | Lorient            | 32 | Goal Keeper     |   -   | [2.0, 44.1]     |  |
| +54.67 | +47.21 | 00:16:50.976 | Lorient            | Lorient            | 33 | Pass            |   -   | [120.0, 0.1]    | Incomplete (Incomplete) |

---

### Case 74: Episode `3835341_p133_574c166a`
- **Match**: `3835341` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Italy Women's** vs Possessing Team: **Belgium Women's**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `921.32s` | Acquisition dt: `1.553s` | Control dt: `1.553s` | Regain dt: `1.553s`
- **Control Event**: `Pass` (ID: `4265ab58-96c4-4c4e-b249-242fa404ad09`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.553s)
  [ ] Controlled-possession verified (ctrl: 1.553s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.38 |  -1.40 | 00:15:19.916 | Belgium Women's    | Belgium Women's    | 133 | Ball Receipt*   |   -   | [95.4, 41.3]    |  |
|  +2.38 |  -1.40 | 00:15:19.916 | Belgium Women's    | Belgium Women's    | 133 | Carry           |   -   | [95.4, 41.3]    | Carry under control |
|  +3.62 |  -0.17 | 00:15:21.151 | Belgium Women's    | Belgium Women's    | 133 | Shot            |   -   | [98.8, 45.3]    | Blocked |
|  +3.78 |  +0.00 | 00:15:21.316 | Italy Women's      | Belgium Women's    | 133 | Block           |  Yes  | [17.8, 35.8]    |  |
|  +3.86 |  +0.08 | 00:15:21.396 | Italy Women's      | Belgium Women's    | 133 | Goal Keeper     |   -   | [2.8, 39.4]     |  |
|  +5.33 |  +1.55 | 00:15:22.869 | Italy Women's      | Italy Women's      | 134 | Pass            |   -   | [14.9, 38.5]    | -> Manuela Giugli |
|  +6.07 |  +2.29 | 00:15:23.605 | Italy Women's      | Italy Women's      | 134 | Ball Receipt*   |   -   | [28.3, 30.6]    |  |
|  +6.07 |  +2.29 | 00:15:23.605 | Italy Women's      | Italy Women's      | 134 | Carry           |   -   | [28.3, 30.6]    | Carry under control |
|  +7.75 |  +3.97 | 00:15:25.287 | Italy Women's      | Italy Women's      | 134 | Pass            |   -   | [34.4, 29.7]    | Incomplete (Incomplete) |
|  +9.91 |  +6.13 | 00:15:27.443 | Italy Women's      | Italy Women's      | 134 | Ball Receipt*   |   -   | [78.3, 8.4]     | Incomplete |
|  +9.91 |  +6.13 | 00:15:27.443 | Belgium Women's    | Italy Women's      | 134 | Interception    |  Yes  | [47.9, 66.7]    | Lost In Play |
| +11.78 |  +8.00 | 00:15:29.318 | Italy Women's      | Italy Women's      | 134 | Ball Recovery   |   -   | [71.8, 20.3]    |  |
| +11.78 |  +8.00 | 00:15:29.318 | Italy Women's      | Italy Women's      | 134 | Carry           |   -   | [71.8, 20.3]    | Carry under control |

---

### Case 75: Episode `3773369_p65_f3b460ba`
- **Match**: `3773369` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Barcelona** vs Possessing Team: **Huesca**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1796.87s` | Acquisition dt: `3.501s` | Control dt: `3.501s` | Regain dt: `3.501s`
- **Control Event**: `Pass` (ID: `64947bc8-e58e-4b17-a10f-9f2adef50509`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.501s)
  [ ] Controlled-possession verified (ctrl: 3.501s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.64 |  -0.76 | 00:29:56.110 | Huesca             | Huesca             | 65 | Ball Receipt*   |   -   | [25.7, 15.1]    |  |
|  +2.64 |  -0.76 | 00:29:56.110 | Huesca             | Huesca             | 65 | Carry           |   -   | [25.7, 15.1]    | Carry under control |
|  +2.68 |  -0.72 | 00:29:56.150 | Huesca             | Huesca             | 65 | Pass            |   -   | [26.9, 15.9]    | -> Mikel Rico Mor |
|  +3.41 |  +0.00 | 00:29:56.874 | Barcelona          | Huesca             | 65 | Pressure        |  Yes  | [76.2, 62.5]    |  |
|  +3.66 |  +0.25 | 00:29:57.123 | Huesca             | Huesca             | 65 | Ball Receipt*   |   -   | [42.4, 17.6]    |  |
|  +3.66 |  +0.25 | 00:29:57.123 | Huesca             | Huesca             | 65 | Carry           |   -   | [42.4, 17.6]    | Carry under control |
|  +4.35 |  +0.94 | 00:29:57.817 | Huesca             | Huesca             | 65 | Dribble         |   -   | [43.9, 17.6]    |  |
|  +4.35 |  +0.94 | 00:29:57.817 | Barcelona          | Huesca             | 65 | Duel            |  Yes  | [76.2, 62.5]    | Tackle, Lost In Play |
|  +4.45 |  +1.05 | 00:29:57.921 | Barcelona          | Huesca             | 65 | Pressure        |  Yes  | [76.5, 58.7]    |  |
|  +4.74 |  +1.34 | 00:29:58.210 | Huesca             | Huesca             | 65 | Ball Recovery   |   -   | [43.3, 24.2]    |  |
|  +6.91 |  +3.50 | 00:30:00.375 | Barcelona          | Barcelona          | 66 | Pass            |   -   | [60.3, 49.5]    | -> Sergio Busquet |
|  +8.36 |  +4.95 | 00:30:01.825 | Barcelona          | Barcelona          | 66 | Ball Receipt*   |   -   | [67.3, 66.2]    |  |
|  +8.36 |  +4.95 | 00:30:01.825 | Barcelona          | Barcelona          | 66 | Carry           |   -   | [67.3, 66.2]    | Carry under control |

---

### Case 76: Episode `3941018_p49_ef55234d`
- **Match**: `3941018` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Possessing Team: **Georgia**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1770.31s` | Acquisition dt: `4.176s` | Control dt: `4.176s` | Regain dt: `4.176s`
- **Control Event**: `Pass` (ID: `b722d32a-e74a-4022-bee2-64d5829b85fb`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 4.176s)
  [ ] Controlled-possession verified (ctrl: 4.176s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.22 |  -0.55 | 00:29:29.764 | Spain              | Spain              | 48 | Pressure        |   -   | [20.8, 54.6]    |  |
|  +0.00 |  -0.33 | 00:29:29.981 | Georgia            | Georgia            | 49 | Ball Recovery   |   -   | [98.0, 24.7]    |  |
|  +0.00 |  -0.33 | 00:29:29.981 | Georgia            | Georgia            | 49 | Carry           |   -   | [98.0, 24.7]    | Carry under control |
|  +0.33 |  +0.00 | 00:29:30.309 | Spain              | Georgia            | 49 | Dribbled Past   |  Yes  | [22.8, 52.5]    |  |
|  +0.33 |  +0.00 | 00:29:30.309 | Georgia            | Georgia            | 49 | Dribble         |   -   | [97.3, 27.6]    |  |
|  +0.33 |  +0.00 | 00:29:30.309 | Georgia            | Georgia            | 49 | Carry           |   -   | [97.3, 27.6]    | Carry under control |
|  +1.30 |  +0.97 | 00:29:31.278 | Georgia            | Georgia            | 49 | Pass            |   -   | [95.0, 31.3]    | -> Giorgi Kochora |
|  +2.58 |  +2.25 | 00:29:32.563 | Georgia            | Georgia            | 49 | Ball Receipt*   |   -   | [96.8, 41.8]    |  |
|  +2.58 |  +2.25 | 00:29:32.563 | Georgia            | Georgia            | 49 | Carry           |   -   | [96.8, 41.8]    | Carry under control |
|  +3.29 |  +2.96 | 00:29:33.268 | Georgia            | Georgia            | 49 | Shot            |   -   | [99.6, 43.4]    | Blocked |
|  +3.39 |  +3.06 | 00:29:33.367 | Spain              | Georgia            | 49 | Block           |  Yes  | [18.4, 36.7]    |  |
|  +3.51 |  +3.18 | 00:29:33.487 | Spain              | Georgia            | 49 | Goal Keeper     |   -   | [2.4, 39.9]     |  |
|  +4.50 |  +4.18 | 00:29:34.485 | Spain              | Spain              | 50 | Pass            |   -   | [12.2, 47.8]    | -> Unai Simón Men |

---

### Case 77: Episode `3803000_p35_df42b9d6`
- **Match**: `3803000` (Ligue 1) | **Period**: 1
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Clermont Foot**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1042.26s` | Acquisition dt: `1.268s` | Control dt: `1.268s` | Regain dt: `1.268s`
- **Control Event**: `Pass` (ID: `81b30f00-fa61-4029-8420-ca00a701f68a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.268s)
  [ ] Controlled-possession verified (ctrl: 1.268s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.87 |  -2.51 | 00:17:19.751 | Paris Saint-Germai | Paris Saint-Germai | 34 | Dribble         |   -   | [58.5, 16.1]    |  |
|  -0.71 |  -1.34 | 00:17:20.916 | Paris Saint-Germai | Paris Saint-Germai | 34 | Pressure        |   -   | [62.8, 4.7]     |  |
|  +0.00 |  -0.63 | 00:17:21.625 | Clermont Foot      | Clermont Foot      | 35 | Pass            |   -   | [58.5, 72.6]    | -> Akim Zedadka |
|  +0.63 |  +0.00 | 00:17:22.257 | Paris Saint-Germai | Clermont Foot      | 35 | Pressure        |  Yes  | [66.9, 10.2]    |  |
|  +0.85 |  +0.22 | 00:17:22.474 | Clermont Foot      | Clermont Foot      | 35 | Ball Receipt*   |   -   | [50.1, 74.8]    |  |
|  +0.85 |  +0.22 | 00:17:22.474 | Clermont Foot      | Clermont Foot      | 35 | Carry           |   -   | [50.1, 74.8]    | Carry under control |
|  +1.35 |  +0.71 | 00:17:22.972 | Clermont Foot      | Clermont Foot      | 35 | Pass            |   -   | [51.0, 73.0]    | -> Jason Berthomi |
|  +1.90 |  +1.27 | 00:17:23.525 | Clermont Foot      | Clermont Foot      | 35 | Ball Receipt*   |   -   | [66.3, 64.7]    |  |
|  +1.90 |  +1.27 | 00:17:23.525 | Clermont Foot      | Clermont Foot      | 35 | Carry           |   -   | [66.3, 64.7]    | Carry under control |
|  +1.90 |  +1.27 | 00:17:23.525 | Paris Saint-Germai | Paris Saint-Germai | 36 | Pass            |   -   | [55.8, 13.6]    | -> Presnel Kimpem |
|  +2.50 |  +1.87 | 00:17:24.124 | Paris Saint-Germai | Paris Saint-Germai | 36 | Ball Receipt*   |   -   | [44.6, 18.3]    |  |
|  +2.50 |  +1.87 | 00:17:24.124 | Paris Saint-Germai | Paris Saint-Germai | 36 | Carry           |   -   | [44.6, 18.3]    | Carry under control |
|  +2.50 |  +1.87 | 00:17:24.124 | Clermont Foot      | Paris Saint-Germai | 36 | Miscontrol      |   -   | [66.5, 62.6]    | Opponent Miscontrol |

---

### Case 78: Episode `3938641_p25_99626a8d`
- **Match**: `3938641` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Poland** vs Possessing Team: **Austria**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `595.24s` | Acquisition dt: `3.287s` | Control dt: `3.287s` | Regain dt: `3.287s`
- **Control Event**: `Pass` (ID: `7468f252-7081-4c91-af14-3375f0189779`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.287s)
  [ ] Controlled-possession verified (ctrl: 3.287s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -2.05 | 00:09:53.185 | Austria            | Poland             | 24 | Block           |   -   | [116.0, 77.5]   |  |
|  +1.75 |  -0.30 | 00:09:54.934 | Austria            | Austria            | 25 | Ball Recovery   |   -   | [114.1, 77.5]   |  |
|  +1.75 |  -0.30 | 00:09:54.934 | Austria            | Austria            | 25 | Carry           |   -   | [114.1, 77.5]   | Carry under control |
|  +2.05 |  +0.00 | 00:09:55.235 | Poland             | Austria            | 25 | Pressure        |  Yes  | [6.8, 3.4]      |  |
|  +2.52 |  +0.47 | 00:09:55.700 | Austria            | Austria            | 25 | Pass            |   -   | [111.4, 73.7]   | -> Marcel Sabitze |
|  +3.92 |  +1.87 | 00:09:57.109 | Austria            | Austria            | 25 | Ball Receipt*   |   -   | [107.5, 45.2]   |  |
|  +4.11 |  +2.06 | 00:09:57.297 | Austria            | Austria            | 25 | Shot            |   -   | [107.5, 45.2]   | Blocked |
|  +4.22 |  +2.17 | 00:09:57.404 | Poland             | Austria            | 25 | Block           |  Yes  | [9.9, 36.2]     |  |
|  +4.26 |  +2.21 | 00:09:57.444 | Poland             | Austria            | 25 | Goal Keeper     |   -   | [2.2, 38.1]     |  |
|  +5.34 |  +3.29 | 00:09:58.522 | Poland             | Poland             | 26 | Pass            |   -   | [15.3, 35.9]    | -> Przemysław Fra |
|  +6.86 |  +4.81 | 00:10:00.046 | Poland             | Poland             | 26 | Ball Receipt*   |   -   | [12.6, 47.2]    |  |
|  +6.86 |  +4.81 | 00:10:00.046 | Poland             | Poland             | 26 | Carry           |   -   | [12.6, 47.2]    | Carry under control |
|  +7.43 |  +5.38 | 00:10:00.614 | Austria            | Poland             | 26 | Pressure        |  Yes  | [105.1, 31.5]   |  |

---

### Case 79: Episode `3788760_p47_b635d07b`
- **Match**: `3788760` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Possessing Team: **Czech Republic**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `1387.68s` | Acquisition dt: `2.518s` | Control dt: `2.518s` | Regain dt: `2.518s`
- **Control Event**: `Pass` (ID: `999d1b58-28d2-4f4a-b6b8-bd06a8ca7bab`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.518s)
  [ ] Controlled-possession verified (ctrl: 2.518s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| -19.03 | -22.93 | 00:22:44.742 | Croatia            | Croatia            | 46 | Shot            |   -   | [104.8, 37.1]   | Saved |
| -18.20 | -22.11 | 00:22:45.564 | Czech Republic     | Croatia            | 46 | Goal Keeper     |   -   | [2.3, 41.5]     |  |
|  +0.00 |  -3.91 | 00:23:03.769 | Czech Republic     | Czech Republic     | 47 | Pass            |   -   | [13.8, 42.3]    | Incomplete (Incomplete) |
|  +3.91 |  +0.00 | 00:23:07.677 | Croatia            | Czech Republic     | 47 | Pressure        |  Yes  | [32.3, 34.4]    |  |
|  +6.43 |  +2.52 | 00:23:10.195 | Czech Republic     | Czech Republic     | 47 | Ball Receipt*   |   -   | [87.2, 45.4]    | Incomplete |
|  +6.43 |  +2.52 | 00:23:10.195 | Croatia            | Croatia            | 48 | Pass            |   -   | [26.4, 34.2]    | -> Dominik Livako |
|  +7.72 |  +3.82 | 00:23:11.494 | Croatia            | Croatia            | 48 | Ball Receipt*   |   -   | [14.9, 36.9]    |  |
|  +7.72 |  +3.82 | 00:23:11.494 | Croatia            | Croatia            | 48 | Carry           |   -   | [14.9, 36.9]    | Carry under control |
| +11.90 |  +7.99 | 00:23:15.667 | Croatia            | Croatia            | 48 | Pass            |   -   | [16.2, 37.6]    | -> Dejan Lovren |
| +13.36 |  +9.46 | 00:23:17.132 | Croatia            | Croatia            | 48 | Ball Receipt*   |   -   | [20.0, 48.4]    |  |
| +13.36 |  +9.46 | 00:23:17.132 | Croatia            | Croatia            | 48 | Carry           |   -   | [20.0, 48.4]    | Carry under control |
| +14.21 | +10.30 | 00:23:17.976 | Croatia            | Croatia            | 48 | Pass            |   -   | [20.0, 48.4]    | -> Domagoj Vida |
| +15.53 | +11.62 | 00:23:19.302 | Croatia            | Croatia            | 48 | Ball Receipt*   |   -   | [20.8, 29.1]    |  |

---

### Case 80: Episode `3837876_p85_d4a64339`
- **Match**: `3837876` (Ligue 1) | **Period**: 2
- **Counterpressing Team**: **Paris Saint-Germain** vs Possessing Team: **Lille**
- **Stratum**: `new_possession` | **Evidence String**: `new_possession_completed_pass`
- **Timestamps**: Initiation: `12.84s` | Acquisition dt: `1.762s` | Control dt: `1.762s` | Regain dt: `1.762s`
- **Control Event**: `Pass` (ID: `27a6388d-e8fe-4ffb-bfa9-257c1ed40e7e`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.762s)
  [ ] Controlled-possession verified (ctrl: 1.762s <= 5.0s)
  [ ] Evidence categorization valid (new_possession_completed_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +3.58 |  -0.19 | 00:00:12.655 | Lille              | Lille              | 85 | Carry           |   -   | [106.3, 60.4]   | Carry under control |
|  +3.64 |  -0.12 | 00:00:12.716 | Lille              | Lille              | 85 | Pass            |   -   | [106.3, 60.4]   | Incomplete (Incomplete) |
|  +3.77 |  +0.00 | 00:00:12.840 | Lille              | Lille              | 85 | Ball Receipt*   |   -   | [109.7, 48.5]   | Incomplete |
|  +3.77 |  +0.00 | 00:00:12.840 | Paris Saint-Germai | Lille              | 85 | Block           |  Yes  | [12.8, 22.8]    |  |
|  +5.53 |  +1.76 | 00:00:14.602 | Paris Saint-Germai | Paris Saint-Germai | 86 | Pass            |   -   | [11.6, 19.1]    | -> Neymar da Silv |
|  +7.25 |  +3.49 | 00:00:16.329 | Paris Saint-Germai | Paris Saint-Germai | 86 | Ball Receipt*   |   -   | [28.2, 13.8]    |  |
|  +7.25 |  +3.49 | 00:00:16.329 | Paris Saint-Germai | Paris Saint-Germai | 86 | Carry           |   -   | [28.2, 13.8]    | Carry under control |
|  +7.42 |  +3.66 | 00:00:16.499 | Paris Saint-Germai | Paris Saint-Germai | 86 | Pass            |   -   | [28.2, 13.8]    | -> Fabián Ruiz Pe |
|  +8.16 |  +4.40 | 00:00:17.236 | Paris Saint-Germai | Paris Saint-Germai | 86 | Ball Receipt*   |   -   | [27.0, 19.1]    |  |
|  +8.16 |  +4.40 | 00:00:17.236 | Paris Saint-Germai | Paris Saint-Germai | 86 | Carry           |   -   | [27.0, 19.1]    | Carry under control |
|  +9.69 |  +5.93 | 00:00:18.767 | Paris Saint-Germai | Paris Saint-Germai | 86 | Pass            |   -   | [32.7, 16.6]    | Incomplete (Incomplete) |
| +13.23 |  +9.46 | 00:00:22.303 | Paris Saint-Germai | Paris Saint-Germai | 86 | Ball Receipt*   |   -   | [55.2, 53.7]    | Incomplete |
| +13.23 |  +9.46 | 00:00:22.303 | Lille              | Lille              | 87 | Ball Recovery   |   -   | [59.0, 23.3]    |  |

---

### Case 81: Episode `3857279_p97_54e479c5`
- **Match**: `3857279` (FIFA World Cup) | **Period**: 2
- **Counterpressing Team**: **France** vs Possessing Team: **Australia**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1112.87s` | Acquisition dt: `3.257s` | Control dt: `4.685s` | Regain dt: `4.685s`
- **Control Event**: `Pass` (ID: `3b8ca95c-3fcf-4c26-9dbd-b7a09e68aaae`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.257s)
  [ ] Controlled-possession verified (ctrl: 4.685s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +3.25 |  -0.46 | 00:18:32.408 | Australia          | Australia          | 97 | Pass            |   -   | [55.8, 0.4]     | -> Aaron Mooy |
|  +3.72 |  +0.00 | 00:18:32.872 | Australia          | Australia          | 97 | Ball Receipt*   |   -   | [60.5, 10.5]    |  |
|  +3.72 |  +0.00 | 00:18:32.872 | Australia          | Australia          | 97 | Carry           |   -   | [60.5, 10.5]    | Carry under control |
|  +3.72 |  +0.00 | 00:18:32.872 | France             | Australia          | 97 | Block           |  Yes  | [63.6, 77.5]    |  |
|  +5.87 |  +2.15 | 00:18:35.018 | France             | Australia          | 97 | Pressure        |   -   | [61.4, 67.7]    |  |
|  +6.16 |  +2.44 | 00:18:35.312 | France             | Australia          | 97 | Dribbled Past   |   -   | [58.0, 67.7]    |  |
|  +6.16 |  +2.44 | 00:18:35.312 | Australia          | Australia          | 97 | Dribble         |   -   | [62.1, 12.4]    |  |
|  +6.16 |  +2.44 | 00:18:35.312 | Australia          | Australia          | 97 | Carry           |   -   | [62.1, 12.4]    | Carry under control |
|  +6.63 |  +2.91 | 00:18:35.786 | France             | Australia          | 97 | Pressure        |   -   | [62.8, 68.5]    |  |
|  +6.98 |  +3.26 | 00:18:36.129 | France             | Australia          | 97 | Dribbled Past   |   -   | [59.4, 68.5]    |  |
|  +6.98 |  +3.26 | 00:18:36.129 | Australia          | Australia          | 97 | Dribble         |   -   | [60.7, 11.6]    |  |
|  +8.28 |  +4.56 | 00:18:37.431 | Australia          | Australia          | 97 | Pressure        |   -   | [64.1, 1.5]     |  |
|  +8.40 |  +4.68 | 00:18:37.557 | France             | France             | 98 | Pass            |  Yes  | [56.0, 76.5]    | -> Antoine Griezm |

---

### Case 82: Episode `3893814_p107_646b4072`
- **Match**: `3893814` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Sweden Women's** vs Possessing Team: **Sweden Women's**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `623.14s` | Acquisition dt: `0.276s` | Control dt: `1.306s` | Regain dt: `1.306s`
- **Control Event**: `Pass` (ID: `f2f21d39-1450-4960-b440-4b5e7854182b`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.276s)
  [ ] Controlled-possession verified (ctrl: 1.306s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.40 | 00:10:21.739 | Italy Women's      | Sweden Women's     | 107 | Duel            |   -   | [69.6, 72.2]    | Tackle, Success In Play |
|  +1.21 |  -0.20 | 00:10:22.947 | Italy Women's      | Sweden Women's     | 107 | Ball Recovery   |   -   | [76.0, 74.8]    |  |
|  +1.21 |  -0.20 | 00:10:22.947 | Italy Women's      | Sweden Women's     | 107 | Carry           |   -   | [76.0, 74.8]    | Carry under control |
|  +1.40 |  +0.00 | 00:10:23.143 | Sweden Women's     | Sweden Women's     | 107 | Pressure        |  Yes  | [44.1, 5.9]     |  |
|  +1.68 |  +0.28 | 00:10:23.419 | Italy Women's      | Sweden Women's     | 107 | Pass            |   -   | [76.6, 75.9]    | Incomplete (Incomplete) |
|  +1.93 |  +0.53 | 00:10:23.670 | Italy Women's      | Sweden Women's     | 107 | Ball Receipt*   |   -   | [74.5, 64.3]    | Incomplete |
|  +1.93 |  +0.53 | 00:10:23.670 | Sweden Women's     | Sweden Women's     | 107 | Block           |  Yes  | [44.5, 10.2]    |  |
|  +2.71 |  +1.31 | 00:10:24.449 | Sweden Women's     | Sweden Women's     | 107 | Pass            |   -   | [46.9, 12.8]    | -> Jonna Ann-Char |
|  +3.84 |  +2.43 | 00:10:25.577 | Italy Women's      | Sweden Women's     | 107 | Pressure        |   -   | [77.9, 64.3]    |  |
|  +3.92 |  +2.51 | 00:10:25.655 | Sweden Women's     | Sweden Women's     | 107 | Ball Receipt*   |   -   | [39.8, 14.7]    |  |
|  +3.92 |  +2.51 | 00:10:25.655 | Sweden Women's     | Sweden Women's     | 107 | Pass            |   -   | [38.5, 14.1]    | Incomplete (Incomplete) |
|  +4.07 |  +2.67 | 00:10:25.810 | Italy Women's      | Sweden Women's     | 107 | Block           |   -   | [74.9, 66.0]    |  |
| +16.01 | +14.60 | 00:10:37.747 | Sweden Women's     | Sweden Women's     | 108 | Pass            |   -   | [45.4, 0.1]     | -> Fridolina Rolf |

---

### Case 83: Episode `3844385_p17_6e759ec3`
- **Match**: `3844385` (UEFA Women's Euro) | **Period**: 1
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `303.01s` | Acquisition dt: `3.387s` | Control dt: `4.493s` | Regain dt: `4.493s`
- **Control Event**: `Pass` (ID: `452ec3fa-12db-44e9-ab6e-c07fbd01a3e4`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.387s)
  [ ] Controlled-possession verified (ctrl: 4.493s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.14 |  -0.22 | 00:05:02.787 | Germany Women's    | Germany Women's    | 17 | Pass            |   -   | [10.5, 7.8]     | Incomplete (Incomplete) |
|  +0.00 |  -0.08 | 00:05:02.926 | Germany Women's    | Germany Women's    | 17 | Ball Receipt*   |   -   | [15.2, 5.1]     | Incomplete |
|  +0.00 |  -0.08 | 00:05:02.926 | Austria Women's    | Germany Women's    | 17 | Block           |  Yes  | [107.0, 73.7]   |  |
|  +0.08 |  +0.00 | 00:05:03.008 | Germany Women's    | Germany Women's    | 17 | Block           |  Yes  | [9.9, 5.5]      |  |
|  +2.48 |  +2.40 | 00:05:05.406 | Austria Women's    | Austria Women's    | 18 | Pass            |   -   | [107.6, 80.0]   | -> Julia Hickelsb |
|  +3.19 |  +3.11 | 00:05:06.121 | Germany Women's    | Austria Women's    | 18 | Pressure        |   -   | [10.8, 7.6]     |  |
|  +3.25 |  +3.17 | 00:05:06.180 | Austria Women's    | Austria Women's    | 18 | Ball Receipt*   |   -   | [108.7, 75.0]   |  |
|  +3.25 |  +3.17 | 00:05:06.180 | Austria Women's    | Austria Women's    | 18 | Carry           |   -   | [108.7, 75.0]   | Carry under control |
|  +3.47 |  +3.39 | 00:05:06.395 | Austria Women's    | Austria Women's    | 18 | Pass            |   -   | [108.7, 74.6]   | Incomplete (Incomplete) |
|  +4.52 |  +4.44 | 00:05:07.448 | Austria Women's    | Austria Women's    | 18 | Pressure        |   -   | [106.6, 80.0]   |  |
|  +4.57 |  +4.49 | 00:05:07.501 | Austria Women's    | Austria Women's    | 18 | Ball Receipt*   |   -   | [107.0, 79.3]   | Incomplete |
|  +4.57 |  +4.49 | 00:05:07.501 | Germany Women's    | Germany Women's    | 19 | Pass            |  Yes  | [12.9, 1.9]     | -> Lina Magull |
|  +6.08 |  +6.00 | 00:05:09.004 | Germany Women's    | Germany Women's    | 19 | Ball Receipt*   |   -   | [26.8, 4.4]     |  |

---

### Case 84: Episode `3895194_p50_fc1a2c64`
- **Match**: `3895194` (1. Bundesliga) | **Period**: 1
- **Counterpressing Team**: **Bayer Leverkusen** vs Possessing Team: **Augsburg**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1410.70s` | Acquisition dt: `0.994s` | Control dt: `2.149s` | Regain dt: `2.149s`
- **Control Event**: `Pass` (ID: `eee0e667-d66e-46e4-8122-95cf01a25514`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.994s)
  [ ] Controlled-possession verified (ctrl: 2.149s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -2.74 | 00:23:27.959 | Augsburg           | Augsburg           | 50 | Pass            |   -   | [75.8, 59.8]    | -> Ruben Vargas |
|  +1.70 |  -1.04 | 00:23:29.656 | Augsburg           | Augsburg           | 50 | Ball Receipt*   |   -   | [81.7, 63.8]    |  |
|  +1.70 |  -1.04 | 00:23:29.656 | Augsburg           | Augsburg           | 50 | Pass            |   -   | [81.7, 64.0]    | -> Jeffrey Gouwel |
|  +2.74 |  +0.00 | 00:23:30.699 | Bayer Leverkusen   | Augsburg           | 50 | Pressure        |  Yes  | [52.3, 17.2]    |  |
|  +3.02 |  +0.28 | 00:23:30.975 | Augsburg           | Augsburg           | 50 | Ball Receipt*   |   -   | [67.4, 66.1]    |  |
|  +3.02 |  +0.28 | 00:23:30.975 | Augsburg           | Augsburg           | 50 | Pass            |   -   | [67.8, 67.1]    | -> Niklas Dorsch |
|  +3.73 |  +0.99 | 00:23:31.693 | Augsburg           | Augsburg           | 50 | Ball Receipt*   |   -   | [78.8, 59.3]    |  |
|  +3.73 |  +0.99 | 00:23:31.693 | Augsburg           | Augsburg           | 50 | Miscontrol      |   -   | [78.8, 59.3]    | Opponent Miscontrol |
|  +4.89 |  +2.15 | 00:23:32.848 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Pass            |   -   | [34.1, 24.1]    | -> Granit Xhaka |
|  +5.87 |  +3.13 | 00:23:33.825 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Ball Receipt*   |   -   | [37.1, 19.1]    |  |
|  +5.87 |  +3.13 | 00:23:33.825 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Pass            |   -   | [37.1, 22.3]    | -> Piero Martín H |
|  +6.58 |  +3.84 | 00:23:34.539 | Augsburg           | Bayer Leverkusen   | 51 | Pressure        |  Yes  | [86.6, 57.4]    |  |
|  +6.77 |  +4.03 | 00:23:34.733 | Bayer Leverkusen   | Bayer Leverkusen   | 51 | Ball Receipt*   |   -   | [31.8, 22.9]    |  |

---

### Case 85: Episode `3835339_p101_f0783118`
- **Match**: `3835339` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Netherlands Women's** vs Possessing Team: **Switzerland Women's**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `342.58s` | Acquisition dt: `2.781s` | Control dt: `4.301s` | Regain dt: `4.301s`
- **Control Event**: `Pass` (ID: `66e53f24-d777-4cd5-a4e4-55f490c16b67`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.781s)
  [ ] Controlled-possession verified (ctrl: 4.301s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +1.27 |  -3.37 | 00:05:39.216 | Switzerland Women' | Switzerland Women' | 101 | Pass            |   -   | [37.6, 25.1]    | -> Géraldine Reut |
|  +3.21 |  -1.43 | 00:05:41.158 | Switzerland Women' | Switzerland Women' | 101 | Ball Receipt*   |   -   | [50.7, 5.7]     |  |
|  +3.21 |  -1.43 | 00:05:41.158 | Switzerland Women' | Switzerland Women' | 101 | Carry           |   -   | [50.7, 5.7]     | Carry under control |
|  +4.64 |  +0.00 | 00:05:42.585 | Netherlands Women' | Switzerland Women' | 101 | Pressure        |  Yes  | [64.3, 74.7]    |  |
|  +7.42 |  +2.78 | 00:05:45.366 | Switzerland Women' | Switzerland Women' | 101 | Pass            |   -   | [64.0, 20.7]    | Incomplete (Incomplete) |
|  +8.94 |  +4.30 | 00:05:46.886 | Switzerland Women' | Switzerland Women' | 101 | Ball Receipt*   |   -   | [91.7, 39.7]    | Incomplete |
|  +8.94 |  +4.30 | 00:05:46.886 | Netherlands Women' | Netherlands Women' | 102 | Pass            |   -   | [33.3, 45.3]    | -> Danielle van d |
| +10.45 |  +5.81 | 00:05:48.396 | Netherlands Women' | Netherlands Women' | 102 | Ball Receipt*   |   -   | [49.9, 50.1]    |  |
| +10.45 |  +5.81 | 00:05:48.396 | Netherlands Women' | Netherlands Women' | 102 | Pass            |   -   | [50.2, 49.9]    | -> Jackie Groenen |
| +11.30 |  +6.66 | 00:05:49.246 | Switzerland Women' | Netherlands Women' | 102 | Pressure        |  Yes  | [71.6, 28.5]    |  |
| +11.42 |  +6.78 | 00:05:49.368 | Netherlands Women' | Netherlands Women' | 102 | Ball Receipt*   |   -   | [47.6, 51.2]    |  |
| +11.42 |  +6.78 | 00:05:49.368 | Netherlands Women' | Netherlands Women' | 102 | Pass            |   -   | [47.6, 51.4]    | -> Danielle van d |
| +12.07 |  +7.43 | 00:05:50.016 | Netherlands Women' | Netherlands Women' | 102 | Ball Receipt*   |   -   | [50.4, 47.7]    |  |

---

### Case 86: Episode `3837859_p81_a8178c67`
- **Match**: `3837859` (Ligue 1) | **Period**: 2
- **Counterpressing Team**: **Toulouse** vs Possessing Team: **Toulouse**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `196.19s` | Acquisition dt: `0.692s` | Control dt: `4.302s` | Regain dt: `4.302s`
- **Control Event**: `Pass` (ID: `5bd74fc6-8922-4891-927b-70b44245e6a4`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.692s)
  [ ] Controlled-possession verified (ctrl: 4.302s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -2.71 |  -3.64 | 00:03:12.549 | Paris Saint-Germai | Toulouse           | 81 | Interception    |   -   | [32.2, 3.2]     | Success In Play |
|  -0.66 |  -1.60 | 00:03:14.592 | Toulouse           | Toulouse           | 81 | Pressure        |   -   | [106.6, 65.3]   |  |
|  +0.00 |  -0.93 | 00:03:15.256 | Paris Saint-Germai | Toulouse           | 81 | Pass            |   -   | [12.6, 20.6]    | -> Gianluigi Donn |
|  +0.93 |  +0.00 | 00:03:16.188 | Toulouse           | Toulouse           | 81 | Pressure        |  Yes  | [112.8, 54.7]   |  |
|  +1.62 |  +0.69 | 00:03:16.880 | Paris Saint-Germai | Toulouse           | 81 | Ball Receipt*   |   -   | [4.0, 31.4]     |  |
|  +1.62 |  +0.69 | 00:03:16.880 | Paris Saint-Germai | Toulouse           | 81 | Pass            |   -   | [4.9, 31.6]     | Incomplete (Incomplete) |
|  +5.23 |  +4.30 | 00:03:20.490 | Toulouse           | Toulouse           | 81 | Pass            |   -   | [76.1, 62.5]    | -> Brecht Dejaege |
|  +7.11 |  +6.18 | 00:03:22.370 | Paris Saint-Germai | Toulouse           | 81 | Pressure        |   -   | [32.5, 16.2]    |  |
|  +7.47 |  +6.53 | 00:03:22.722 | Toulouse           | Toulouse           | 81 | Ball Receipt*   |   -   | [87.4, 63.9]    |  |
|  +7.47 |  +6.53 | 00:03:22.722 | Toulouse           | Toulouse           | 81 | Carry           |   -   | [87.4, 63.9]    | Carry under control |
| +11.07 | +10.14 | 00:03:26.327 | Toulouse           | Toulouse           | 81 | Pass            |   -   | [100.1, 57.6]   | -> Fares Chaïbi |
| +13.92 | +12.99 | 00:03:29.175 | Toulouse           | Toulouse           | 81 | Ball Receipt*   |   -   | [112.5, 23.3]   |  |
| +13.94 | +13.00 | 00:03:29.192 | Toulouse           | Toulouse           | 81 | Shot            |   -   | [112.5, 23.3]   | Off T |

---

### Case 87: Episode `3893793_p183_659785db`
- **Match**: `3893793` (Women's World Cup) | **Period**: 2
- **Counterpressing Team**: **Japan Women's** vs Possessing Team: **Japan Women's**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `2433.95s` | Acquisition dt: `0.647s` | Control dt: `2.735s` | Regain dt: `2.735s`
- **Control Event**: `Pass` (ID: `bdc46d30-2886-4361-b81d-3651414bc486`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.647s)
  [ ] Controlled-possession verified (ctrl: 2.735s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.62 | 00:40:33.329 | Japan Women's      | Japan Women's      | 183 | Ball Receipt*   |   -   | [82.3, 44.4]    | Incomplete |
|  +0.00 |  -0.62 | 00:40:33.329 | Zambia W           | Japan Women's      | 183 | Ball Recovery   |   -   | [40.4, 33.4]    |  |
|  +0.00 |  -0.62 | 00:40:33.329 | Zambia W           | Japan Women's      | 183 | Carry           |   -   | [40.4, 33.4]    | Carry under control |
|  +0.62 |  +0.00 | 00:40:33.952 | Japan Women's      | Japan Women's      | 183 | Pressure        |  Yes  | [80.8, 44.2]    |  |
|  +1.27 |  +0.65 | 00:40:34.599 | Zambia W           | Japan Women's      | 183 | Pass            |   -   | [40.7, 34.5]    | Incomplete (Incomplete) |
|  +3.36 |  +2.73 | 00:40:36.687 | Zambia W           | Japan Women's      | 183 | Ball Receipt*   |   -   | [70.4, 33.6]    | Incomplete |
|  +3.36 |  +2.73 | 00:40:36.687 | Japan Women's      | Japan Women's      | 183 | Pass            |   -   | [45.4, 50.5]    | -> Hikaru Naomoto |
|  +4.04 |  +3.42 | 00:40:37.369 | Japan Women's      | Japan Women's      | 183 | Ball Receipt*   |   -   | [68.8, 60.0]    |  |
|  +4.04 |  +3.42 | 00:40:37.369 | Japan Women's      | Japan Women's      | 183 | Carry           |   -   | [68.8, 60.0]    | Carry under control |
|  +4.04 |  +3.42 | 00:40:37.369 | Zambia W           | Japan Women's      | 183 | Block           |   -   | [57.4, 25.8]    |  |
|  +5.54 |  +4.91 | 00:40:38.865 | Zambia W           | Japan Women's      | 183 | Pressure        |   -   | [50.8, 16.5]    |  |
|  +8.41 |  +7.79 | 00:40:41.742 | Zambia W           | Japan Women's      | 183 | Pressure        |   -   | [48.0, 19.2]    |  |
| +10.04 |  +9.42 | 00:40:43.368 | Japan Women's      | Japan Women's      | 183 | Pass            |   -   | [80.4, 63.1]    | -> Risa Shimizu |

---

### Case 88: Episode `3794685_p130_e642a64e`
- **Match**: `3794685` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Italy** vs Possessing Team: **Italy**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1407.34s` | Acquisition dt: `0.364s` | Control dt: `2.289s` | Regain dt: `2.289s`
- **Control Event**: `Pass` (ID: `96ff6296-66ff-404e-bef0-a92104deb1e5`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.364s)
  [ ] Controlled-possession verified (ctrl: 2.289s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -2.33 | 00:23:25.010 | Austria            | Italy              | 130 | Clearance       |   -   | [11.8, 52.9]    |  |
|  +1.04 |  -1.29 | 00:23:26.048 | Austria            | Italy              | 130 | Ball Recovery   |   -   | [23.0, 49.4]    |  |
|  +1.04 |  -1.29 | 00:23:26.048 | Austria            | Italy              | 130 | Carry           |   -   | [23.0, 49.4]    | Carry under control |
|  +2.33 |  +0.00 | 00:23:27.340 | Italy              | Italy              | 130 | Pressure        |  Yes  | [91.7, 32.1]    |  |
|  +2.69 |  +0.36 | 00:23:27.704 | Austria            | Italy              | 130 | Pass            |   -   | [25.4, 50.4]    | Incomplete (Incomplete) |
|  +2.84 |  +0.51 | 00:23:27.852 | Italy              | Italy              | 130 | Block           |  Yes  | [92.1, 29.9]    |  |
|  +4.32 |  +1.99 | 00:23:29.328 | Austria            | Italy              | 130 | Pressure        |   -   | [25.7, 56.8]    |  |
|  +4.62 |  +2.29 | 00:23:29.629 | Italy              | Italy              | 130 | Pass            |   -   | [91.1, 22.5]    | -> Jorge Luiz Fre |
|  +5.47 |  +3.14 | 00:23:30.478 | Italy              | Italy              | 130 | Ball Receipt*   |   -   | [87.1, 28.5]    |  |
|  +5.47 |  +3.14 | 00:23:30.478 | Italy              | Italy              | 130 | Pass            |   -   | [87.1, 28.5]    | -> Manuel Locatel |
|  +6.44 |  +4.11 | 00:23:31.447 | Italy              | Italy              | 130 | Ball Receipt*   |   -   | [83.9, 18.3]    |  |
|  +6.44 |  +4.11 | 00:23:31.447 | Italy              | Italy              | 130 | Carry           |   -   | [83.9, 18.3]    | Carry under control |
|  +8.04 |  +5.71 | 00:23:33.052 | Italy              | Italy              | 130 | Pass            |   -   | [83.7, 18.3]    | -> Domenico Berar |

---

### Case 89: Episode `3773587_p7_a89c236d`
- **Match**: `3773587` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Barcelona** vs Possessing Team: **Barcelona**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `197.87s` | Acquisition dt: `0.209s` | Control dt: `1.707s` | Regain dt: `1.707s`
- **Control Event**: `Pass` (ID: `dc390dfe-af9e-45e5-8f3a-7a7f79358c29`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.209s)
  [ ] Controlled-possession verified (ctrl: 1.707s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -4.08 | 00:03:13.792 | Getafe             | Barcelona          | 7 | Duel            |   -   | [59.6, 68.0]    | Tackle, Won |
|  +0.00 |  -4.08 | 00:03:13.792 | Getafe             | Barcelona          | 7 | Carry           |   -   | [59.6, 68.0]    | Carry under control |
|  +2.53 |  -1.55 | 00:03:16.322 | Getafe             | Barcelona          | 7 | Pass            |   -   | [70.1, 67.0]    | -> Jaime Mata Arn |
|  +4.08 |  +0.00 | 00:03:17.871 | Barcelona          | Barcelona          | 7 | Pressure        |  Yes  | [25.6, 28.3]    |  |
|  +4.12 |  +0.04 | 00:03:17.909 | Getafe             | Barcelona          | 7 | Ball Receipt*   |   -   | [93.5, 55.4]    |  |
|  +4.12 |  +0.04 | 00:03:17.909 | Getafe             | Barcelona          | 7 | Carry           |   -   | [93.5, 55.4]    | Carry under control |
|  +4.29 |  +0.21 | 00:03:18.080 | Getafe             | Barcelona          | 7 | Pass            |   -   | [95.5, 55.2]    | Incomplete (Incomplete) |
|  +4.70 |  +0.62 | 00:03:18.488 | Getafe             | Barcelona          | 7 | Ball Receipt*   |   -   | [86.3, 53.4]    | Incomplete |
|  +4.70 |  +0.62 | 00:03:18.488 | Barcelona          | Barcelona          | 7 | Block           |  Yes  | [23.6, 28.6]    |  |
|  +5.79 |  +1.71 | 00:03:19.578 | Barcelona          | Barcelona          | 7 | Pass            |   -   | [17.7, 39.7]    | -> Sergi Roberto  |
|  +6.95 |  +2.87 | 00:03:20.745 | Barcelona          | Barcelona          | 7 | Ball Receipt*   |   -   | [26.5, 54.9]    |  |
|  +6.95 |  +2.87 | 00:03:20.745 | Barcelona          | Barcelona          | 7 | Carry           |   -   | [26.5, 54.9]    | Carry under control |
|  +7.31 |  +3.23 | 00:03:21.103 | Barcelona          | Barcelona          | 7 | Pass            |   -   | [26.5, 54.9]    | -> Sergio Busquet |

---

### Case 90: Episode `3773585_p36_9f401aeb`
- **Match**: `3773585` (La Liga) | **Period**: 1
- **Counterpressing Team**: **Real Madrid** vs Possessing Team: **Real Madrid**
- **Stratum**: `other` | **Evidence String**: `goalkeeper_plus_pass`
- **Timestamps**: Initiation: `1116.97s` | Acquisition dt: `2.238s` | Control dt: `4.927s` | Regain dt: `4.927s`
- **Control Event**: `Pass` (ID: `1f62e510-24a3-4850-9a4c-9668633d19ad`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.238s)
  [ ] Controlled-possession verified (ctrl: 4.927s <= 5.0s)
  [ ] Evidence categorization valid (goalkeeper_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.15 |  -1.16 | 00:18:35.811 | Real Madrid        | Real Madrid        | 36 | Pressure        |   -   | [46.1, 50.4]    |  |
|  +0.00 |  -1.01 | 00:18:35.961 | Barcelona          | Real Madrid        | 36 | Ball Recovery   |   -   | [77.4, 31.1]    |  |
|  +0.00 |  -1.01 | 00:18:35.961 | Barcelona          | Real Madrid        | 36 | Carry           |   -   | [77.4, 31.1]    | Carry under control |
|  +1.01 |  +0.00 | 00:18:36.972 | Real Madrid        | Real Madrid        | 36 | Dribbled Past   |  Yes  | [36.6, 49.6]    |  |
|  +1.01 |  +0.00 | 00:18:36.972 | Barcelona          | Real Madrid        | 36 | Dribble         |   -   | [83.5, 30.5]    |  |
|  +1.01 |  +0.00 | 00:18:36.972 | Barcelona          | Real Madrid        | 36 | Carry           |   -   | [83.5, 30.5]    | Carry under control |
|  +1.21 |  +0.20 | 00:18:37.176 | Real Madrid        | Real Madrid        | 36 | Foul Committed  |  Yes  | [37.3, 49.2]    |  |
|  +1.21 |  +0.20 | 00:18:37.176 | Barcelona          | Real Madrid        | 36 | Foul Won        |   -   | [82.8, 30.9]    |  |
|  +1.21 |  +0.20 | 00:18:37.176 | Barcelona          | Real Madrid        | 36 | Carry           |   -   | [82.8, 30.9]    | Carry under control |
|  +2.04 |  +1.03 | 00:18:38.003 | Real Madrid        | Real Madrid        | 36 | Pressure        |  Yes  | [28.3, 56.2]    |  |
|  +2.60 |  +1.58 | 00:18:38.556 | Barcelona          | Real Madrid        | 36 | Shot            |   -   | [94.3, 31.8]    | Saved |
|  +3.25 |  +2.24 | 00:18:39.210 | Real Madrid        | Real Madrid        | 36 | Goal Keeper     |   -   | [5.0, 40.7]     |  |
|  +5.94 |  +4.93 | 00:18:41.899 | Real Madrid        | Real Madrid        | 37 | Pass            |   -   | [11.7, 35.7]    | -> Toni Kroos |

---

### Case 91: Episode `3857257_p46_1cc4ad0d`
- **Match**: `3857257` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Denmark** vs Possessing Team: **Denmark**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1328.98s` | Acquisition dt: `0.322s` | Control dt: `2.117s` | Regain dt: `2.117s`
- **Control Event**: `Pass` (ID: `c844d7f0-ea3b-4d7d-ac10-967ba599e5c4`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.322s)
  [ ] Controlled-possession verified (ctrl: 2.117s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -1.66 |  -2.82 | 00:22:06.160 | Denmark            | Denmark            | 46 | Pass            |   -   | [21.7, 73.6]    | Incomplete (Incomplete) |
|  +0.00 |  -1.17 | 00:22:07.819 | Australia          | Denmark            | 46 | Ball Recovery   |   -   | [69.0, 23.6]    |  |
|  +0.00 |  -1.17 | 00:22:07.819 | Australia          | Denmark            | 46 | Carry           |   -   | [69.0, 23.6]    | Carry under control |
|  +1.17 |  +0.00 | 00:22:08.985 | Denmark            | Denmark            | 46 | Pressure        |  Yes  | [47.0, 54.5]    |  |
|  +1.49 |  +0.32 | 00:22:09.307 | Australia          | Denmark            | 46 | Pass            |   -   | [69.3, 20.1]    | Incomplete (Incomplete) |
|  +3.28 |  +2.12 | 00:22:11.102 | Australia          | Denmark            | 46 | Ball Receipt*   |   -   | [96.0, 33.9]    | Incomplete |
|  +3.28 |  +2.12 | 00:22:11.102 | Australia          | Denmark            | 46 | Duel            |   -   | [95.4, 31.9]    | Aerial Lost |
|  +3.28 |  +2.12 | 00:22:11.102 | Denmark            | Denmark            | 46 | Pass            |   -   | [24.7, 48.2]    | -> Mathias Jensen |
|  +4.54 |  +3.38 | 00:22:12.362 | Australia          | Denmark            | 46 | Pressure        |   -   | [83.6, 23.6]    |  |
|  +5.02 |  +3.86 | 00:22:12.842 | Denmark            | Denmark            | 46 | Ball Receipt*   |   -   | [33.8, 53.7]    |  |
|  +5.02 |  +3.86 | 00:22:12.842 | Denmark            | Denmark            | 46 | Carry           |   -   | [33.8, 53.7]    | Carry under control |
|  +5.05 |  +3.89 | 00:22:12.873 | Denmark            | Denmark            | 46 | Miscontrol      |   -   | [33.5, 58.0]    | Opponent Miscontrol |
|  +6.19 |  +5.03 | 00:22:14.014 | Denmark            | Denmark            | 46 | Pressure        |   -   | [29.4, 58.0]    |  |

---

### Case 92: Episode `3794689_p124_46c3e822`
- **Match**: `3794689` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Wales** vs Possessing Team: **Wales**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1720.01s` | Acquisition dt: `0.793s` | Control dt: `2.986s` | Regain dt: `2.986s`
- **Control Event**: `Pass` (ID: `8e9de08e-2509-4a22-960f-90fb948e2b9c`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.793s)
  [ ] Controlled-possession verified (ctrl: 2.986s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -5.40 | 00:28:34.614 | Denmark            | Wales              | 124 | Clearance       |   -   | [6.5, 44.1]     |  |
|  +3.82 |  -1.58 | 00:28:38.429 | Denmark            | Wales              | 124 | Ball Recovery   |   -   | [11.5, 76.0]    |  |
|  +3.82 |  -1.58 | 00:28:38.429 | Denmark            | Wales              | 124 | Carry           |   -   | [11.5, 76.0]    | Carry under control |
|  +5.40 |  +0.00 | 00:28:40.010 | Wales              | Wales              | 124 | Pressure        |  Yes  | [100.0, 7.1]    |  |
|  +6.19 |  +0.79 | 00:28:40.803 | Denmark            | Wales              | 124 | Pass            |   -   | [21.1, 77.3]    | Incomplete (Incomplete) |
|  +8.38 |  +2.99 | 00:28:42.996 | Wales              | Wales              | 124 | Pass            |   -   | [69.0, 19.3]    | -> Joe Allen |
|  +9.59 |  +4.19 | 00:28:44.203 | Wales              | Wales              | 124 | Ball Receipt*   |   -   | [77.8, 11.0]    |  |
|  +9.59 |  +4.19 | 00:28:44.203 | Wales              | Wales              | 124 | Carry           |   -   | [77.8, 11.0]    | Carry under control |
| +13.46 |  +8.07 | 00:28:48.078 | Wales              | Wales              | 124 | Pass            |   -   | [90.9, 24.1]    | Incomplete (Incomplete) |
| +15.61 | +10.21 | 00:28:50.222 | Wales              | Wales              | 124 | Ball Receipt*   |   -   | [106.2, 49.8]   | Incomplete |
| +15.61 | +10.21 | 00:28:50.222 | Denmark            | Wales              | 124 | Clearance       |   -   | [14.4, 32.7]    |  |
| +17.13 | +11.73 | 00:28:51.743 | Wales              | Wales              | 124 | Ball Recovery   |   -   | [92.4, 56.9]    |  |
| +17.13 | +11.73 | 00:28:51.743 | Wales              | Wales              | 124 | Carry           |   -   | [92.4, 56.9]    | Carry under control |

---

### Case 93: Episode `3835322_p102_df13a2f3`
- **Match**: `3835322` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Denmark Women's** vs Possessing Team: **Denmark Women's**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `6.32s` | Acquisition dt: `1.946s` | Control dt: `3.446s` | Regain dt: `3.446s`
- **Control Event**: `Pass` (ID: `2cfeb1df-8282-46a6-9fff-4ed3ae857623`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 1.946s)
  [ ] Controlled-possession verified (ctrl: 3.446s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  -0.79 |  -3.09 | 00:00:03.230 | Denmark Women's    | Denmark Women's    | 102 | Carry           |   -   | [35.8, 32.4]    | Carry under control |
|  +0.00 |  -2.30 | 00:00:04.020 | Denmark Women's    | Denmark Women's    | 102 | Pass            |   -   | [37.9, 32.4]    | Incomplete (Incomplete) |
|  +2.30 |  +0.00 | 00:00:06.324 | Denmark Women's    | Denmark Women's    | 102 | Ball Receipt*   |   -   | [62.7, 16.4]    | Incomplete |
|  +2.30 |  +0.00 | 00:00:06.324 | Denmark Women's    | Denmark Women's    | 102 | Duel            |  Yes  | [63.2, 16.4]    | Aerial Lost |
|  +2.30 |  +0.00 | 00:00:06.324 | Germany Women's    | Denmark Women's    | 102 | Pass            |   -   | [56.9, 63.7]    | -> Lina Magull |
|  +3.63 |  +1.33 | 00:00:07.654 | Germany Women's    | Denmark Women's    | 102 | Ball Receipt*   |   -   | [64.6, 58.1]    |  |
|  +3.63 |  +1.33 | 00:00:07.654 | Germany Women's    | Denmark Women's    | 102 | Carry           |   -   | [64.6, 58.1]    | Carry under control |
|  +4.25 |  +1.95 | 00:00:08.270 | Germany Women's    | Denmark Women's    | 102 | Pass            |   -   | [63.6, 59.2]    | Incomplete (Incomplete) |
|  +5.75 |  +3.45 | 00:00:09.770 | Germany Women's    | Denmark Women's    | 102 | Ball Receipt*   |   -   | [77.5, 54.9]    | Incomplete |
|  +5.75 |  +3.45 | 00:00:09.770 | Denmark Women's    | Denmark Women's    | 102 | Pass            |   -   | [37.5, 20.0]    | -> Rikke Læntver  |
|  +7.20 |  +4.90 | 00:00:11.224 | Germany Women's    | Denmark Women's    | 102 | Pressure        |   -   | [93.1, 47.1]    |  |
|  +7.91 |  +5.61 | 00:00:11.934 | Denmark Women's    | Denmark Women's    | 102 | Ball Receipt*   |   -   | [29.8, 32.0]    |  |
|  +7.91 |  +5.61 | 00:00:11.934 | Denmark Women's    | Denmark Women's    | 102 | Carry           |   -   | [29.8, 32.0]    | Carry under control |

---

### Case 94: Episode `3788741_p29_b3cdb2f5`
- **Match**: `3788741` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Turkey** vs Possessing Team: **Italy**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `747.84s` | Acquisition dt: `2.612s` | Control dt: `4.386s` | Regain dt: `4.386s`
- **Control Event**: `Pass` (ID: `5b4d0ce1-653b-4380-80f6-b5c1f8206707`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.612s)
  [ ] Controlled-possession verified (ctrl: 4.386s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -0.91 | 00:12:26.930 | Italy              | Italy              | 29 | Duel            |  Yes  | [37.6, 41.5]    | Tackle, Success In Play |
|  +0.52 |  -0.39 | 00:12:27.450 | Italy              | Italy              | 29 | Ball Recovery   |   -   | [41.8, 41.5]    |  |
|  +0.52 |  -0.39 | 00:12:27.450 | Italy              | Italy              | 29 | Carry           |   -   | [41.8, 41.5]    | Carry under control |
|  +0.91 |  +0.00 | 00:12:27.836 | Turkey             | Italy              | 29 | Pressure        |  Yes  | [83.4, 31.9]    |  |
|  +1.29 |  +0.38 | 00:12:28.216 | Italy              | Italy              | 29 | Pass            |   -   | [36.0, 44.1]    | -> Alessandro Flo |
|  +2.25 |  +1.34 | 00:12:29.177 | Italy              | Italy              | 29 | Ball Receipt*   |   -   | [28.1, 59.0]    |  |
|  +2.25 |  +1.34 | 00:12:29.177 | Italy              | Italy              | 29 | Pass            |   -   | [28.1, 59.0]    | -> Nicolò Barella |
|  +3.09 |  +2.19 | 00:12:30.024 | Turkey             | Italy              | 29 | Pressure        |  Yes  | [70.4, 24.7]    |  |
|  +3.17 |  +2.27 | 00:12:30.103 | Italy              | Italy              | 29 | Ball Receipt*   |   -   | [42.9, 55.7]    |  |
|  +3.17 |  +2.27 | 00:12:30.103 | Italy              | Italy              | 29 | Carry           |   -   | [42.9, 55.7]    | Carry under control |
|  +3.52 |  +2.61 | 00:12:30.448 | Italy              | Italy              | 29 | Pass            |   -   | [43.9, 55.2]    | Incomplete (Incomplete) |
|  +5.09 |  +4.18 | 00:12:32.018 | Italy              | Italy              | 29 | Pressure        |   -   | [57.1, 45.3]    |  |
|  +5.29 |  +4.39 | 00:12:32.222 | Italy              | Italy              | 29 | Ball Receipt*   |   -   | [55.4, 44.9]    | Incomplete |

---

### Case 95: Episode `3869219_p40_69886a0f`
- **Match**: `3869219` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Croatia** vs Possessing Team: **Croatia**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1779.74s` | Acquisition dt: `0.496s` | Control dt: `2.881s` | Regain dt: `2.881s`
- **Control Event**: `Pass` (ID: `c50232d6-f9ca-4e04-bf38-766074eabdde`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.496s)
  [ ] Controlled-possession verified (ctrl: 2.881s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.40 | 00:29:38.347 | Japan              | Croatia            | 40 | Pass            |   -   | [16.4, 40.7]    | -> Daizen Maeda |
|  +1.17 |  -0.23 | 00:29:39.513 | Japan              | Croatia            | 40 | Ball Receipt*   |   -   | [38.8, 44.9]    |  |
|  +1.17 |  -0.23 | 00:29:39.513 | Japan              | Croatia            | 40 | Carry           |   -   | [38.8, 44.9]    | Carry under control |
|  +1.40 |  +0.00 | 00:29:39.743 | Croatia            | Croatia            | 40 | Pressure        |  Yes  | [77.3, 35.5]    |  |
|  +1.89 |  +0.50 | 00:29:40.239 | Japan              | Croatia            | 40 | Pass            |   -   | [40.2, 44.2]    | Incomplete (Incomplete) |
|  +4.28 |  +2.88 | 00:29:42.624 | Japan              | Croatia            | 40 | Ball Receipt*   |   -   | [38.1, 29.2]    | Incomplete |
|  +4.28 |  +2.88 | 00:29:42.624 | Croatia            | Croatia            | 40 | Pass            |   -   | [84.1, 53.2]    | -> Josip Juranovi |
|  +6.38 |  +4.99 | 00:29:44.732 | Croatia            | Croatia            | 40 | Ball Receipt*   |   -   | [64.2, 53.2]    |  |
|  +6.38 |  +4.99 | 00:29:44.732 | Croatia            | Croatia            | 40 | Pass            |   -   | [64.2, 53.2]    | -> Marcelo Brozov |
|  +7.27 |  +5.87 | 00:29:45.613 | Croatia            | Croatia            | 40 | Ball Receipt*   |   -   | [73.7, 53.6]    |  |
|  +7.27 |  +5.87 | 00:29:45.613 | Croatia            | Croatia            | 40 | Carry           |   -   | [73.7, 53.6]    | Carry under control |
|  +8.45 |  +7.05 | 00:29:46.795 | Croatia            | Croatia            | 40 | Pass            |   -   | [73.7, 53.6]    | -> Luka Modrić |
|  +9.90 |  +8.50 | 00:29:48.243 | Croatia            | Croatia            | 40 | Ball Receipt*   |   -   | [75.4, 28.3]    |  |

---

### Case 96: Episode `3857254_p94_8c2f0327`
- **Match**: `3857254` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Denmark** vs Possessing Team: **Tunisia**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `2786.95s` | Acquisition dt: `0.333s` | Control dt: `2.973s` | Regain dt: `2.973s`
- **Control Event**: `Pass` (ID: `e6013bce-924e-4f54-8560-afcd75fed2af`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.333s)
  [ ] Controlled-possession verified (ctrl: 2.973s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +1.99 |  -1.82 | 00:46:25.132 | Tunisia            | Tunisia            | 94 | Pass            |   -   | [27.2, 36.0]    | -> Anis Ben Slima |
|  +3.02 |  -0.79 | 00:46:26.168 | Tunisia            | Tunisia            | 94 | Ball Receipt*   |   -   | [31.1, 52.0]    |  |
|  +3.02 |  -0.79 | 00:46:26.168 | Tunisia            | Tunisia            | 94 | Carry           |   -   | [31.1, 52.0]    | Carry under control |
|  +3.81 |  +0.00 | 00:46:26.954 | Denmark            | Tunisia            | 94 | Pressure        |  Yes  | [89.0, 28.1]    |  |
|  +4.14 |  +0.33 | 00:46:27.287 | Tunisia            | Tunisia            | 94 | Pass            |   -   | [31.1, 52.0]    | Incomplete (Incomplete) |
|  +6.78 |  +2.97 | 00:46:29.927 | Tunisia            | Tunisia            | 94 | Ball Receipt*   |   -   | [67.6, 35.0]    | Incomplete |
|  +6.78 |  +2.97 | 00:46:29.927 | Denmark            | Denmark            | 95 | Pass            |   -   | [51.3, 51.2]    | -> Andreas Christ |
|  +8.11 |  +4.30 | 00:46:31.257 | Denmark            | Denmark            | 95 | Ball Receipt*   |   -   | [53.2, 29.9]    |  |
|  +8.11 |  +4.30 | 00:46:31.257 | Denmark            | Denmark            | 95 | Carry           |   -   | [53.2, 29.9]    | Carry under control |
|  +8.95 |  +5.14 | 00:46:32.090 | Denmark            | Denmark            | 95 | Pass            |   -   | [55.0, 32.4]    | -> Simon Thorup K |
| +13.15 |  +9.34 | 00:46:36.294 | Denmark            | Denmark            | 95 | Ball Receipt*   |   -   | [23.3, 53.7]    |  |
| +13.15 |  +9.34 | 00:46:36.294 | Denmark            | Denmark            | 95 | Carry           |   -   | [23.3, 53.7]    | Carry under control |
| +13.23 |  +9.42 | 00:46:36.374 | Denmark            | Denmark            | 95 | Pass            |   -   | [20.8, 53.5]    | -> Kasper Schmeic |

---

### Case 97: Episode `3857263_p47_8f818c5b`
- **Match**: `3857263` (FIFA World Cup) | **Period**: 1
- **Counterpressing Team**: **Spain** vs Possessing Team: **Germany**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1442.47s` | Acquisition dt: `3.801s` | Control dt: `4.356s` | Regain dt: `4.356s`
- **Control Event**: `Pass` (ID: `a4019e5b-b60a-4393-80f7-f9dd1835f668`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 3.801s)
  [ ] Controlled-possession verified (ctrl: 4.356s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +0.00 |  -1.00 | 00:24:01.468 | Spain              | Spain              | 46 | Dispossessed    |   -   | [44.7, 49.1]    | Opponent Dispossessed |
|  +0.00 |  -1.00 | 00:24:01.468 | Germany            | Germany            | 47 | Duel            |  Yes  | [75.9, 31.0]    | Tackle, Won |
|  +0.00 |  -1.00 | 00:24:01.468 | Germany            | Germany            | 47 | Carry           |   -   | [75.9, 31.0]    | Carry under control |
|  +1.00 |  +0.00 | 00:24:02.473 | Spain              | Germany            | 47 | Pressure        |  Yes  | [38.1, 53.5]    |  |
|  +1.28 |  +0.28 | 00:24:02.751 | Germany            | Germany            | 47 | Pass            |   -   | [81.9, 30.7]    | -> Jamal Musiala |
|  +1.91 |  +0.90 | 00:24:03.374 | Germany            | Germany            | 47 | Ball Receipt*   |   -   | [91.8, 28.4]    |  |
|  +1.91 |  +0.90 | 00:24:03.374 | Germany            | Germany            | 47 | Pass            |   -   | [91.8, 28.4]    | -> Thomas Müller |
|  +2.47 |  +1.47 | 00:24:03.943 | Germany            | Germany            | 47 | Ball Receipt*   |   -   | [93.8, 35.5]    |  |
|  +2.47 |  +1.47 | 00:24:03.943 | Germany            | Germany            | 47 | Carry           |   -   | [93.8, 35.5]    | Carry under control |
|  +3.10 |  +2.09 | 00:24:04.567 | Spain              | Germany            | 47 | Pressure        |  Yes  | [27.6, 46.2]    |  |
|  +3.43 |  +2.43 | 00:24:04.901 | Germany            | Germany            | 47 | Pass            |   -   | [94.5, 38.5]    | -> İlkay Gündoğan |
|  +4.20 |  +3.19 | 00:24:05.664 | Spain              | Germany            | 47 | Pressure        |  Yes  | [13.6, 36.7]    |  |
|  +4.32 |  +3.32 | 00:24:05.792 | Germany            | Germany            | 47 | Ball Receipt*   |   -   | [103.5, 43.1]   |  |

---

### Case 98: Episode `3794690_p119_8da7ad1c`
- **Match**: `3794690` (UEFA Euro) | **Period**: 2
- **Counterpressing Team**: **Netherlands** vs Possessing Team: **Netherlands**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `1477.21s` | Acquisition dt: `0.446s` | Control dt: `4.419s` | Regain dt: `4.419s`
- **Control Event**: `Pass` (ID: `f6be0219-958b-4ba9-aa6d-003be774646a`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.446s)
  [ ] Controlled-possession verified (ctrl: 4.419s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +2.80 |  -1.63 | 00:24:35.578 | Czech Republic     | Netherlands        | 119 | Pass            |   -   | [5.6, 14.1]     | -> Petr Ševčík |
|  +4.06 |  -0.37 | 00:24:36.842 | Czech Republic     | Netherlands        | 119 | Ball Receipt*   |   -   | [21.0, 6.2]     |  |
|  +4.06 |  -0.37 | 00:24:36.842 | Czech Republic     | Netherlands        | 119 | Carry           |   -   | [21.0, 6.2]     | Carry under control |
|  +4.43 |  +0.00 | 00:24:37.213 | Netherlands        | Netherlands        | 119 | Pressure        |  Yes  | [96.7, 73.9]    |  |
|  +4.88 |  +0.45 | 00:24:37.659 | Czech Republic     | Netherlands        | 119 | Pass            |   -   | [21.2, 5.9]     | Incomplete (Incomplete) |
|  +8.85 |  +4.42 | 00:24:41.632 | Czech Republic     | Netherlands        | 119 | Ball Receipt*   |   -   | [55.2, 25.4]    | Incomplete |
|  +8.85 |  +4.42 | 00:24:41.632 | Netherlands        | Netherlands        | 119 | Pass            |   -   | [63.4, 51.5]    | -> Patrick van Aa |
| +11.92 |  +7.49 | 00:24:44.700 | Netherlands        | Netherlands        | 119 | Ball Receipt*   |   -   | [61.7, 24.7]    |  |
| +11.92 |  +7.49 | 00:24:44.700 | Netherlands        | Netherlands        | 119 | Carry           |   -   | [61.7, 24.7]    | Carry under control |
| +14.39 |  +9.95 | 00:24:47.165 | Netherlands        | Netherlands        | 119 | Pass            |   -   | [69.4, 4.9]     | -> Quincy Anton P |
| +15.51 | +11.08 | 00:24:48.291 | Netherlands        | Netherlands        | 119 | Ball Receipt*   |   -   | [82.6, 4.6]     |  |
| +15.51 | +11.08 | 00:24:48.291 | Netherlands        | Netherlands        | 119 | Carry           |   -   | [82.6, 4.6]     | Carry under control |
| +15.75 | +11.32 | 00:24:48.528 | Netherlands        | Netherlands        | 119 | Pass            |   -   | [82.4, 4.9]     | -> Patrick van Aa |

---

### Case 99: Episode `3998849_p153_01da6d28`
- **Match**: `3998849` (UEFA Women's Euro) | **Period**: 2
- **Counterpressing Team**: **Germany Women's** vs Possessing Team: **Germany Women's**
- **Stratum**: `other` | **Evidence String**: `goalkeeper_plus_carry`
- **Timestamps**: Initiation: `2901.46s` | Acquisition dt: `2.383s` | Control dt: `2.383s` | Regain dt: `2.383s`
- **Control Event**: `Carry` (ID: `8c70ab77-d56a-48d9-9b22-320d804f1444`)
- **Tactical Outcome 3-Class**: `dangerous_escape` | Dangerous Escape: `1`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 2.383s)
  [ ] Controlled-possession verified (ctrl: 2.383s <= 5.0s)
  [ ] Evidence categorization valid (goalkeeper_plus_carry)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
|  +1.35 |  -6.34 | 00:48:15.127 | Denmark Women's    | Germany Women's    | 153 | Pass            |   -   | [63.2, 43.9]    | -> Pernille Moseg |
|  +2.83 |  -4.86 | 00:48:16.607 | Denmark Women's    | Germany Women's    | 153 | Ball Receipt*   |   -   | [77.7, 67.1]    |  |
|  +2.83 |  -4.86 | 00:48:16.607 | Denmark Women's    | Germany Women's    | 153 | Carry           |   -   | [77.7, 67.1]    | Carry under control |
|  +7.68 |  +0.00 | 00:48:21.462 | Germany Women's    | Germany Women's    | 153 | Pressure        |  Yes  | [20.2, 10.8]    |  |
|  +8.13 |  +0.45 | 00:48:21.914 | Denmark Women's    | Germany Women's    | 153 | Pass            |   -   | [104.4, 69.5]   | Incomplete (Incomplete) |
|  +8.34 |  +0.66 | 00:48:22.120 | Germany Women's    | Germany Women's    | 153 | Block           |   -   | [13.9, 14.1]    |  |
| +10.06 |  +2.38 | 00:48:23.845 | Germany Women's    | Germany Women's    | 154 | Goal Keeper     |   -   | [4.0, 37.8]     |  |
| +10.06 |  +2.38 | 00:48:23.845 | Germany Women's    | Germany Women's    | 154 | Carry           |   -   | [4.0, 37.8]     | Carry under control |
| +24.50 | +16.82 | 00:48:38.278 | Germany Women's    | Germany Women's    | 154 | Pass            |   -   | [16.7, 38.2]    | Incomplete (Incomplete) |
| +28.22 | +20.54 | 00:48:41.998 | Denmark Women's    | Germany Women's    | 154 | Pass            |   -   | [47.4, 56.4]    | -> Pernille Moseg |
| +29.35 | +21.67 | 00:48:43.130 | Germany Women's    | Germany Women's    | 154 | Pressure        |  Yes  | [51.1, 23.7]    |  |
| +29.67 | +21.99 | 00:48:43.450 | Denmark Women's    | Germany Women's    | 154 | Ball Receipt*   |   -   | [69.0, 56.4]    |  |
| +29.71 | +22.03 | 00:48:43.490 | Denmark Women's    | Germany Women's    | 154 | Pass            |   -   | [69.0, 56.4]    | Incomplete (Pass Offside) |

---

### Case 100: Episode `3794687_p61_649b451e`
- **Match**: `3794687` (UEFA Euro) | **Period**: 1
- **Counterpressing Team**: **Belgium** vs Possessing Team: **Belgium**
- **Stratum**: `other` | **Evidence String**: `opponent_turnover_plus_pass`
- **Timestamps**: Initiation: `2647.02s` | Acquisition dt: `0.498s` | Control dt: `1.948s` | Regain dt: `1.948s`
- **Control Event**: `Pass` (ID: `57a6178c-d0ff-492c-b6d4-7c62bcefd51f`)
- **Tactical Outcome 3-Class**: `successful_regain` | Dangerous Escape: `0`

```text
Verification Checklist:
  [ ] Possession-transition verified (acq: 0.498s)
  [ ] Controlled-possession verified (ctrl: 1.948s <= 5.0s)
  [ ] Evidence categorization valid (opponent_turnover_plus_pass)
  Notes: 
```

| Rel TO (s) | Rel Init (s) | Timestamp | Team | Poss Team | Poss ID | Event Type | CP? | Location [x, y] | Outcome / Details |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| -23.42 | -24.46 | 00:43:42.565 | Portugal           | Belgium            | 60 | Block           |   -   | [110.8, 76.7]   |  |
|  -2.40 |  -3.44 | 00:44:03.588 | Belgium            | Belgium            | 61 | Pass            |   -   | [11.2, 0.1]     | Incomplete (Incomplete) |
|  +0.00 |  -1.04 | 00:44:05.987 | Portugal           | Belgium            | 61 | Pass            |   -   | [87.3, 71.4]    | -> Cristiano Rona |
|  +1.04 |  +0.00 | 00:44:07.024 | Belgium            | Belgium            | 61 | Pressure        |  Yes  | [20.4, 17.3]    |  |
|  +1.53 |  +0.50 | 00:44:07.522 | Portugal           | Belgium            | 61 | Ball Receipt*   |   -   | [98.2, 60.7]    |  |
|  +1.53 |  +0.50 | 00:44:07.522 | Portugal           | Belgium            | 61 | Miscontrol      |   -   | [97.8, 60.3]    | Opponent Miscontrol |
|  +2.99 |  +1.95 | 00:44:08.972 | Belgium            | Belgium            | 61 | Pass            |   -   | [29.8, 16.6]    | -> Kevin De Bruyn |
|  +3.76 |  +2.72 | 00:44:09.743 | Belgium            | Belgium            | 61 | Ball Receipt*   |   -   | [36.0, 28.4]    |  |
|  +3.76 |  +2.72 | 00:44:09.743 | Belgium            | Belgium            | 61 | Carry           |   -   | [36.0, 28.4]    | Carry under control |
|  +4.57 |  +3.53 | 00:44:10.558 | Portugal           | Belgium            | 61 | Pressure        |   -   | [79.2, 51.5]    |  |
|  +5.89 |  +4.86 | 00:44:11.879 | Belgium            | Belgium            | 61 | Dispossessed    |   -   | [53.1, 32.4]    | Opponent Dispossessed |
|  +5.89 |  +4.86 | 00:44:11.879 | Portugal           | Belgium            | 61 | Duel            |   -   | [67.0, 47.7]    | Tackle, Lost In Play |
|  +5.93 |  +4.90 | 00:44:11.922 | Portugal           | Belgium            | 61 | Foul Committed  |   -   | [68.5, 49.2]    |  |

---
