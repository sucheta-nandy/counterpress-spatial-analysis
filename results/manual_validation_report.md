# Manual Episode Validation Report

This report documents a stratified sample of 100 counterpress episodes for manual tactical and chronological verification.

## Validation Summary Statistics
- Total Sampled Episodes: 100
- Competitions Represented: 8 (1. Bundesliga, FIFA World Cup, La Liga, Ligue 1, Major League Soccer, UEFA Euro, UEFA Women's Euro, Women's World Cup)
- Outcomes in Sample: Successful Regains = 40, Harmless Escapes = 30, Dangerous Escapes = 30
- Episodes with Usable Initiation 360: 82 (82.0%)

---

### Episode 1: `3877090_p93_ea7525a6`
- **Match**: `3877090` | **Competition**: Major League Soccer (2023)
- **Context**: Period 2, Pressing Team: **Inter Miami** vs. Possession Team: **LAFC**
- **Initiation Action**: `Pressure` by **Diego Alexander Gómez Amarilla** at `00:02:17.990` (Turnover delay: 0.552s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=0.552s). Dangerous transition triggered by: Final third entry at dt=5.164s (initial x=63.2, max x=111.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.90 | -2.45 | 00:02:15.538 | Inter Miami | Inter Miami | Pass | - | [32.6, 38.4] |  |
| -0.91 | -1.46 | 00:02:16.529 | LAFC | Inter Miami | Pressure | - | [62.9, 46.7] |  |
| -0.83 | -1.38 | 00:02:16.606 | Inter Miami | Inter Miami | Ball Receipt* | - | [55.8, 35.4] |  |
| -0.83 | -1.38 | 00:02:16.606 | Inter Miami | Inter Miami | Carry | - | [55.8, 35.4] |  |
| +0.00 | -0.55 | 00:02:17.438 | Inter Miami | Inter Miami | Dispossessed | - | [56.9, 36.1] |  |
| +0.00 | -0.55 | 00:02:17.438 | LAFC | LAFC | Duel | **YES** | [63.2, 44.0] | 🔄 **TURNOVER** |
| +0.55 | +0.00 | 00:02:17.990 | Inter Miami | LAFC | Pressure | **YES** | [58.0, 37.1] | ⭐ **CP INITIATION** |
| +0.76 | +0.20 | 00:02:18.193 | LAFC | LAFC | Pass | - | [60.8, 40.7] |  |
| +1.46 | +0.91 | 00:02:18.895 | LAFC | LAFC | Ball Receipt* | - | [59.8, 45.7] |  |
| +1.46 | +0.91 | 00:02:18.895 | LAFC | LAFC | Pass | - | [58.5, 46.7] |  |
| +3.88 | +3.32 | 00:02:21.315 | LAFC | LAFC | Ball Receipt* | - | [57.5, 23.7] |  |
| +3.88 | +3.32 | 00:02:21.315 | LAFC | LAFC | Carry | - | [57.5, 23.7] |  |
| +4.61 | +4.06 | 00:02:22.048 | LAFC | LAFC | Pass | - | [65.0, 27.2] |  |
| +5.72 | +5.16 | 00:02:23.154 | LAFC | LAFC | Ball Receipt* | - | [84.6, 22.1] |  |
| +5.72 | +5.16 | 00:02:23.154 | LAFC | LAFC | Carry | - | [84.6, 22.1] |  |
| +6.43 | +5.88 | 00:02:23.866 | LAFC | LAFC | Pass | - | [87.2, 21.3] |  |
| +7.90 | +7.34 | 00:02:25.333 | LAFC | LAFC | Ball Receipt* | - | [104.1, 12.1] |  |
| +7.90 | +7.34 | 00:02:25.333 | LAFC | LAFC | Carry | - | [104.1, 12.1] |  |
| +8.98 | +8.43 | 00:02:26.420 | LAFC | LAFC | Pass | - | [109.6, 13.1] |  |
| +9.73 | +9.18 | 00:02:27.172 | LAFC | LAFC | Ball Receipt* | - | [111.9, 40.2] |  |
| +9.73 | +9.18 | 00:02:27.172 | Inter Miami | LAFC | Clearance | - | [8.2, 43.6] |  |
| +11.43 | +10.87 | 00:02:28.864 | Inter Miami | LAFC | Clearance | - | [0.1, 60.1] |  |
| +17.18 | +16.63 | 00:02:34.619 | LAFC | LAFC | Pass | - | [106.9, 0.1] |  |
| +18.92 | +18.37 | 00:02:36.361 | LAFC | LAFC | Ball Receipt* | - | [92.0, 7.4] |  |
| +18.92 | +18.37 | 00:02:36.361 | LAFC | LAFC | Carry | - | [92.0, 7.4] |  |

---

### Episode 2: `3877170_p13_00347b22`
- **Match**: `3877170` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Inter Miami** vs. Possession Team: **Cincinnati**
- **Initiation Action**: `Pressure` by **Facundo Farías** at `00:07:12.838` (Turnover delay: 0.976s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=0.976s). Harmless transition (opp max progression x=28.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.37 | -2.35 | 00:07:10.491 | Inter Miami | Inter Miami | Pass | - | [88.4, 20.1] |  |
| +0.00 | -0.98 | 00:07:11.862 | Inter Miami | Inter Miami | Ball Receipt* | - | [97.0, 19.8] |  |
| +0.00 | -0.98 | 00:07:11.862 | Cincinnati | Cincinnati | Pass | - | [21.5, 55.1] | 🔄 **TURNOVER** |
| +0.98 | +0.00 | 00:07:12.838 | Inter Miami | Cincinnati | Pressure | **YES** | [90.8, 19.2] | ⭐ **CP INITIATION** |
| +1.00 | +0.03 | 00:07:12.864 | Cincinnati | Cincinnati | Ball Receipt* | - | [28.3, 60.9] |  |
| +1.00 | +0.03 | 00:07:12.864 | Cincinnati | Cincinnati | Pass | - | [28.9, 60.3] |  |
| +1.14 | +0.16 | 00:07:12.998 | Inter Miami | Cincinnati | Block | **YES** | [91.2, 20.7] |  |
| +2.81 | +1.84 | 00:07:14.676 | Inter Miami | Cincinnati | Foul Committed | **YES** | [97.2, 27.1] |  |
| +2.81 | +1.84 | 00:07:14.676 | Cincinnati | Cincinnati | Foul Won | - | [22.9, 53.0] |  |

---

### Episode 3: `3895244_p33_43ad9a28`
- **Match**: `3895244` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **FC Heidenheim** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Pressure` by **Lennard Maloney** at `00:17:41.196` (Turnover delay: 1.858s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.858s). Dangerous transition triggered by: Final third entry at dt=13.706s (initial x=7.4, max x=85.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.63 | -3.48 | 00:17:37.712 | FC Heidenheim | FC Heidenheim | Pass | - | [99.0, 69.1] |  |
| +0.00 | -1.86 | 00:17:39.338 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [7.4, 43.7] | 🔄 **TURNOVER** |
| +1.60 | -0.26 | 00:17:40.934 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [22.8, 31.1] |  |
| +1.60 | -0.26 | 00:17:40.934 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [22.8, 31.1] |  |
| +1.86 | +0.00 | 00:17:41.196 | FC Heidenheim | Bayer Leverkusen | Pressure | **YES** | [95.7, 50.1] | ⭐ **CP INITIATION** |
| +3.33 | +1.47 | 00:17:42.668 | FC Heidenheim | Bayer Leverkusen | Foul Committed | **YES** | [90.3, 56.4] |  |
| +3.33 | +1.47 | 00:17:42.668 | Bayer Leverkusen | Bayer Leverkusen | Foul Won | - | [29.8, 23.7] |  |
| +6.69 | +4.84 | 00:17:46.032 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [32.2, 24.8] |  |
| +7.83 | +5.97 | 00:17:47.166 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [42.1, 42.1] |  |
| +8.04 | +6.18 | 00:17:47.377 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [43.8, 37.7] |  |
| +8.69 | +6.84 | 00:17:48.031 | FC Heidenheim | Bayer Leverkusen | Pressure | - | [72.0, 57.5] |  |
| +9.14 | +7.28 | 00:17:48.480 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [49.1, 26.3] |  |
| +9.14 | +7.28 | 00:17:48.480 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [49.2, 25.6] |  |
| +10.24 | +8.38 | 00:17:49.573 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [45.1, 21.3] |  |
| +10.24 | +8.38 | 00:17:49.573 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [45.1, 21.3] |  |
| +10.33 | +8.47 | 00:17:49.666 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [45.1, 21.3] |  |
| +11.86 | +10.01 | 00:17:51.201 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [62.4, 5.2] |  |
| +11.86 | +10.01 | 00:17:51.201 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [61.9, 5.9] |  |
| +12.94 | +11.08 | 00:17:52.276 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [57.5, 13.6] |  |
| +12.94 | +11.08 | 00:17:52.276 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [57.5, 13.6] |  |
| +13.97 | +12.11 | 00:17:53.307 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [65.4, 11.5] |  |
| +15.31 | +13.45 | 00:17:54.650 | FC Heidenheim | Bayer Leverkusen | Pressure | - | [34.8, 69.5] |  |
| +15.56 | +13.71 | 00:17:54.902 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [84.9, 9.8] |  |
| +15.56 | +13.71 | 00:17:54.902 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [84.9, 9.8] |  |
| +15.72 | +13.86 | 00:17:55.054 | Bayer Leverkusen | Bayer Leverkusen | Dribble | - | [85.3, 11.5] |  |
| +15.72 | +13.86 | 00:17:55.054 | FC Heidenheim | FC Heidenheim | Duel | **YES** | [34.8, 68.6] |  |
| +17.69 | +15.84 | 00:17:57.031 | FC Heidenheim | FC Heidenheim | Pass | - | [35.2, 55.6] |  |
| +20.00 | +18.14 | 00:17:59.339 | FC Heidenheim | FC Heidenheim | Ball Receipt* | - | [7.2, 39.1] |  |
| +20.00 | +18.14 | 00:17:59.339 | FC Heidenheim | FC Heidenheim | Carry | - | [7.2, 39.1] |  |

---

### Episode 4: `3857257_p91_d2c41bf1`
- **Match**: `3857257` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 1, Pressing Team: **Australia** vs. Possession Team: **Denmark**
- **Initiation Action**: `Pressure` by **Riley McGree** at `00:44:07.079` (Turnover delay: 1.27s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.27s). Harmless transition (opp max progression x=46.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.27 | 00:44:05.809 | Australia | Australia | Dribble | - | [93.6, 65.3] |  |
| +0.00 | -1.27 | 00:44:05.809 | Denmark | Denmark | Duel | **YES** | [26.5, 14.8] | 🔄 **TURNOVER** |
| +1.20 | -0.07 | 00:44:07.009 | Denmark | Denmark | Ball Recovery | - | [27.1, 26.9] |  |
| +1.20 | -0.07 | 00:44:07.009 | Denmark | Denmark | Carry | - | [27.1, 26.9] |  |
| +1.27 | +0.00 | 00:44:07.079 | Australia | Denmark | Pressure | **YES** | [92.7, 53.2] | ⭐ **CP INITIATION** |
| +2.47 | +1.20 | 00:44:08.276 | Denmark | Denmark | Pass | - | [28.8, 24.2] |  |
| +3.07 | +1.80 | 00:44:08.880 | Denmark | Denmark | Ball Receipt* | - | [28.3, 11.8] |  |
| +3.07 | +1.80 | 00:44:08.880 | Denmark | Denmark | Carry | - | [28.3, 11.8] |  |
| +4.28 | +3.01 | 00:44:10.086 | Denmark | Denmark | Pass | - | [34.5, 11.2] |  |
| +5.46 | +4.19 | 00:44:11.271 | Australia | Denmark | Pressure | - | [75.0, 48.8] |  |
| +5.54 | +4.27 | 00:44:11.354 | Denmark | Denmark | Ball Receipt* | - | [45.1, 27.2] |  |
| +5.54 | +4.27 | 00:44:11.354 | Denmark | Denmark | Carry | - | [45.1, 27.2] |  |
| +6.02 | +4.75 | 00:44:11.828 | Australia | Denmark | Pressure | - | [74.7, 42.2] |  |
| +6.40 | +5.13 | 00:44:12.208 | Denmark | Denmark | Pass | - | [46.7, 36.9] |  |
| +6.77 | +5.50 | 00:44:12.579 | Denmark | Denmark | Ball Receipt* | - | [44.5, 52.3] |  |
| +6.77 | +5.50 | 00:44:12.579 | Australia | Denmark | Block | - | [74.1, 39.1] |  |
| +8.66 | +7.39 | 00:44:14.471 | Australia | Australia | Pass | - | [62.3, 53.8] |  |
| +9.17 | +7.90 | 00:44:14.980 | Denmark | Australia | Pressure | **YES** | [49.0, 20.9] |  |
| +9.62 | +8.35 | 00:44:15.427 | Australia | Australia | Ball Receipt* | - | [72.6, 58.6] |  |
| +9.62 | +8.35 | 00:44:15.427 | Australia | Australia | Carry | - | [72.6, 58.6] |  |
| +11.22 | +9.95 | 00:44:17.032 | Australia | Australia | Pass | - | [74.7, 59.2] |  |
| +11.76 | +10.49 | 00:44:17.574 | Australia | Australia | Ball Receipt* | - | [83.8, 43.8] |  |
| +11.76 | +10.49 | 00:44:17.574 | Denmark | Australia | Interception | **YES** | [40.7, 31.6] |  |
| +13.17 | +11.90 | 00:44:18.981 | Australia | Australia | Pass | - | [74.1, 48.8] |  |
| +13.41 | +12.14 | 00:44:19.220 | Australia | Australia | Ball Receipt* | - | [81.1, 41.9] |  |
| +13.41 | +12.14 | 00:44:19.220 | Denmark | Australia | Block | **YES** | [41.8, 34.0] |  |
| +15.21 | +13.94 | 00:44:21.023 | Australia | Australia | Pass | - | [59.0, 55.1] |  |
| +16.52 | +15.25 | 00:44:22.325 | Denmark | Australia | Pressure | - | [36.0, 15.3] |  |
| +16.95 | +15.68 | 00:44:22.764 | Australia | Australia | Ball Receipt* | - | [81.1, 67.8] |  |
| +16.95 | +15.68 | 00:44:22.764 | Australia | Australia | Carry | - | [81.1, 67.8] |  |
| +16.99 | +15.72 | 00:44:22.804 | Australia | Australia | Pass | - | [81.4, 70.3] |  |
| +18.51 | +17.24 | 00:44:24.322 | Australia | Australia | Ball Receipt* | - | [89.1, 66.2] |  |
| +18.51 | +17.24 | 00:44:24.322 | Denmark | Australia | Clearance | - | [25.5, 17.3] |  |

---

### Episode 5: `3857290_p140_d128b172`
- **Match**: `3857290` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **Switzerland** vs. Possession Team: **Cameroon**
- **Initiation Action**: `Pressure` by **Ruben Vargas** at `00:33:55.078` (Turnover delay: 1.381s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.381s). Harmless transition (opp max progression x=27.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.38 | 00:33:53.697 | Switzerland | Switzerland | Ball Receipt* | - | [99.8, 16.1] |  |
| +0.00 | -1.38 | 00:33:53.697 | Cameroon | Cameroon | Interception | **YES** | [20.3, 64.0] | 🔄 **TURNOVER** |
| +0.00 | -1.38 | 00:33:53.697 | Cameroon | Cameroon | Carry | - | [20.3, 64.0] |  |
| +1.38 | +0.00 | 00:33:55.078 | Switzerland | Cameroon | Pressure | **YES** | [110.6, 18.4] | ⭐ **CP INITIATION** |
| +6.36 | +4.98 | 00:34:00.061 | Cameroon | Cameroon | Pass | - | [17.7, 59.3] |  |
| +7.76 | +6.38 | 00:34:01.457 | Cameroon | Cameroon | Ball Receipt* | - | [27.1, 76.1] |  |
| +7.76 | +6.38 | 00:34:01.457 | Cameroon | Cameroon | Carry | - | [27.1, 76.1] |  |
| +8.88 | +7.50 | 00:34:02.575 | Cameroon | Cameroon | Pass | - | [24.9, 75.4] |  |
| +10.83 | +9.45 | 00:34:04.528 | Cameroon | Cameroon | Ball Receipt* | - | [9.2, 56.7] |  |
| +10.83 | +9.45 | 00:34:04.528 | Cameroon | Cameroon | Carry | - | [9.2, 56.7] |  |
| +11.41 | +10.02 | 00:34:05.102 | Cameroon | Cameroon | Pass | - | [9.2, 56.7] |  |
| +13.62 | +12.24 | 00:34:07.320 | Cameroon | Cameroon | Ball Receipt* | - | [7.9, 35.0] |  |
| +13.62 | +12.24 | 00:34:07.320 | Cameroon | Cameroon | Carry | - | [7.9, 35.0] |  |
| +19.85 | +18.47 | 00:34:13.544 | Cameroon | Cameroon | Pass | - | [26.0, 31.5] |  |
| +21.17 | +19.78 | 00:34:14.862 | Cameroon | Cameroon | Ball Receipt* | - | [30.9, 24.2] |  |
| +21.17 | +19.78 | 00:34:14.862 | Cameroon | Cameroon | Carry | - | [30.9, 24.2] |  |

---

### Episode 6: `3893819_p52_866ac308`
- **Match**: `3893819` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Morocco Women's** vs. Possession Team: **Morocco Women's**
- **Initiation Action**: `Duel` by **Hanane Aït El Haj** at `00:21:07.372` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Morocco Women's. Harmless transition (opp max progression x=10.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.25 | -2.25 | 00:21:05.126 | Morocco Women's | Korea Republic Women's | Pressure | - | [11.6, 65.2] |  |
| -2.12 | -2.12 | 00:21:05.247 | Korea Republic Women's | Korea Republic Women's | Ball Recovery | - | [108.3, 12.9] |  |
| -2.12 | -2.12 | 00:21:05.247 | Korea Republic Women's | Korea Republic Women's | Carry | - | [108.3, 12.9] |  |
| -0.50 | -0.50 | 00:21:06.872 | Morocco Women's | Korea Republic Women's | Pressure | - | [13.4, 69.6] |  |
| +0.00 | +0.00 | 00:21:07.372 | Korea Republic Women's | Korea Republic Women's | Dispossessed | - | [109.5, 10.3] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:21:07.372 | Morocco Women's | Morocco Women's | Duel | **YES** | [10.6, 69.8] | ⭐ **CP INITIATION** |
| +0.00 | +0.00 | 00:21:07.372 | Morocco Women's | Morocco Women's | Carry | - | [10.6, 69.8] |  |
| +1.71 | +1.71 | 00:21:09.081 | Morocco Women's | Morocco Women's | Pass | - | [10.0, 73.2] |  |
| +6.61 | +6.61 | 00:21:13.984 | Korea Republic Women's | Morocco Women's | Pass | - | [55.2, 6.9] |  |
| +8.59 | +8.59 | 00:21:15.965 | Korea Republic Women's | Morocco Women's | Ball Receipt* | - | [87.6, 12.7] |  |

---

### Episode 7: `3877060_p106_c43f1586`
- **Match**: `3877060` | **Competition**: Major League Soccer (2023)
- **Context**: Period 2, Pressing Team: **New York Red Bulls** vs. Possession Team: **New York Red Bulls**
- **Initiation Action**: `Pressure` by **Cameron Harper** at `00:15:45.793` (Turnover delay: 0.543s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.616s by New York Red Bulls. Harmless transition (opp max progression x=73.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -0.54 | 00:15:45.250 | New York Red Bulls | New York Red Bulls | Ball Receipt* | - | [102.9, 40.2] |  |
| +0.00 | -0.54 | 00:15:45.250 | Inter Miami | New York Red Bulls | Ball Recovery | - | [14.2, 23.5] | 🔄 **TURNOVER** |
| +0.00 | -0.54 | 00:15:45.250 | Inter Miami | New York Red Bulls | Carry | - | [14.2, 23.5] |  |
| +0.54 | +0.00 | 00:15:45.793 | New York Red Bulls | New York Red Bulls | Pressure | **YES** | [104.7, 57.4] | ⭐ **CP INITIATION** |
| +2.16 | +1.62 | 00:15:47.409 | Inter Miami | New York Red Bulls | Pass | - | [3.1, 13.8] |  |
| +4.40 | +3.86 | 00:15:49.648 | New York Red Bulls | New York Red Bulls | Pressure | **YES** | [95.4, 74.5] |  |
| +4.83 | +4.29 | 00:15:50.080 | Inter Miami | New York Red Bulls | Ball Receipt* | - | [21.9, 5.5] |  |
| +4.83 | +4.29 | 00:15:50.080 | Inter Miami | New York Red Bulls | Miscontrol | - | [22.3, 6.9] |  |
| +6.08 | +5.53 | 00:15:51.326 | New York Red Bulls | New York Red Bulls | Ball Recovery | - | [104.6, 73.1] |  |
| +6.08 | +5.53 | 00:15:51.326 | New York Red Bulls | New York Red Bulls | Carry | - | [104.6, 73.1] |  |
| +7.97 | +7.42 | 00:15:53.216 | New York Red Bulls | New York Red Bulls | Pass | - | [109.4, 71.3] |  |
| +9.22 | +8.67 | 00:15:54.467 | Inter Miami | New York Red Bulls | Clearance | - | [12.3, 35.2] |  |
| +10.50 | +9.95 | 00:15:55.747 | New York Red Bulls | New York Red Bulls | Ball Recovery | - | [93.6, 28.5] |  |
| +10.50 | +9.95 | 00:15:55.747 | New York Red Bulls | New York Red Bulls | Carry | - | [93.6, 28.5] |  |
| +11.72 | +11.18 | 00:15:56.970 | New York Red Bulls | New York Red Bulls | Shot | - | [93.3, 37.1] |  |
| +12.98 | +12.44 | 00:15:58.230 | Inter Miami | New York Red Bulls | Goal Keeper | - | [1.6, 40.2] |  |

---

### Episode 8: `3837662_p104_c3c8ffb7`
- **Match**: `3837662` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 1, Pressing Team: **Lille** vs. Possession Team: **Paris Saint-Germain**
- **Initiation Action**: `Pressure` by **Benjamin André** at `00:38:08.287` (Turnover delay: 4.925s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=4.925s). Dangerous transition triggered by: Shot at dt=5.889s; Final third entry at dt=0.121s (initial x=79.3, max x=112.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.60 | -6.52 | 00:38:01.762 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [70.0, 40.7] |  |
| +0.00 | -4.92 | 00:38:03.362 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [71.4, 61.8] | 🔄 **TURNOVER** |
| +0.00 | -4.92 | 00:38:03.362 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [71.4, 61.8] |  |
| +0.32 | -4.60 | 00:38:03.684 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [71.4, 61.8] |  |
| +0.93 | -4.00 | 00:38:04.290 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [79.3, 61.5] |  |
| +0.93 | -4.00 | 00:38:04.290 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [79.3, 61.5] |  |
| +1.02 | -3.90 | 00:38:04.385 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [79.3, 61.5] |  |
| +3.19 | -1.73 | 00:38:06.554 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [86.9, 75.7] |  |
| +3.19 | -1.73 | 00:38:06.554 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [86.9, 75.7] |  |
| +4.92 | +0.00 | 00:38:08.287 | Lille | Paris Saint-Germain | Pressure | **YES** | [28.0, 2.8] | ⭐ **CP INITIATION** |
| +5.05 | +0.12 | 00:38:08.408 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [92.1, 73.7] |  |
| +5.46 | +0.53 | 00:38:08.818 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [92.1, 73.7] |  |
| +5.46 | +0.53 | 00:38:08.818 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [92.1, 73.7] |  |
| +5.50 | +0.57 | 00:38:08.861 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [90.3, 63.7] |  |
| +5.50 | +0.57 | 00:38:08.861 | Lille | Paris Saint-Germain | Foul Committed | **YES** | [33.0, 11.1] |  |
| +5.50 | +0.57 | 00:38:08.861 | Paris Saint-Germain | Paris Saint-Germain | Foul Won | - | [87.1, 69.0] |  |
| +8.82 | +3.89 | 00:38:12.182 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [99.9, 55.8] |  |
| +9.93 | +5.01 | 00:38:13.292 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [107.9, 60.6] |  |
| +9.93 | +5.01 | 00:38:13.292 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [107.9, 60.6] |  |
| +10.81 | +5.89 | 00:38:14.176 | Paris Saint-Germain | Paris Saint-Germain | Shot | - | [112.8, 50.5] |  |
| +11.36 | +6.44 | 00:38:14.722 | Lille | Paris Saint-Germain | Goal Keeper | - | [3.3, 35.8] |  |

---

### Episode 9: `3773625_p117_968d0a80`
- **Match**: `3773625` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Barcelona** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Sergio Busquets i Burgos** at `00:07:54.542` (Turnover delay: 1.048s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.869s by Barcelona. Harmless transition (opp max progression x=18.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.37 | -3.41 | 00:07:51.128 | Sevilla | Barcelona | Ball Receipt* | - | [62.5, 34.8] |  |
| -2.37 | -3.41 | 00:07:51.128 | Barcelona | Barcelona | Clearance | - | [56.7, 45.5] |  |
| -0.55 | -1.60 | 00:07:52.941 | Barcelona | Barcelona | Ball Recovery | - | [84.5, 45.5] |  |
| -0.55 | -1.60 | 00:07:52.941 | Barcelona | Barcelona | Carry | - | [84.5, 45.5] |  |
| -0.50 | -1.55 | 00:07:52.994 | Sevilla | Barcelona | Pressure | - | [35.4, 38.0] |  |
| +0.00 | -1.05 | 00:07:53.494 | Barcelona | Barcelona | Dispossessed | - | [84.7, 48.3] |  |
| +0.00 | -1.05 | 00:07:53.494 | Sevilla | Barcelona | Duel | - | [35.4, 31.8] | 🔄 **TURNOVER** |
| +1.00 | -0.05 | 00:07:54.494 | Sevilla | Barcelona | Ball Recovery | - | [47.5, 30.9] |  |
| +1.00 | -0.05 | 00:07:54.494 | Sevilla | Barcelona | Carry | - | [47.5, 30.9] |  |
| +1.05 | +0.00 | 00:07:54.542 | Barcelona | Barcelona | Pressure | **YES** | [69.8, 51.5] | ⭐ **CP INITIATION** |
| +1.92 | +0.87 | 00:07:55.411 | Sevilla | Barcelona | Pass | - | [47.3, 33.5] |  |
| +2.52 | +1.47 | 00:07:56.011 | Sevilla | Barcelona | Ball Receipt* | - | [43.1, 28.0] |  |
| +2.52 | +1.47 | 00:07:56.011 | Sevilla | Barcelona | Carry | - | [43.1, 28.0] |  |
| +4.66 | +3.61 | 00:07:58.156 | Sevilla | Barcelona | Pass | - | [54.8, 23.7] |  |
| +6.57 | +5.52 | 00:08:00.065 | Sevilla | Barcelona | Ball Receipt* | - | [82.6, 47.6] |  |
| +6.57 | +5.52 | 00:08:00.065 | Barcelona | Barcelona | Interception | **YES** | [35.1, 33.5] |  |
| +8.83 | +7.78 | 00:08:02.326 | Barcelona | Barcelona | Ball Recovery | - | [56.3, 46.6] |  |
| +8.83 | +7.78 | 00:08:02.326 | Barcelona | Barcelona | Carry | - | [56.3, 46.6] |  |
| +9.42 | +8.37 | 00:08:02.914 | Barcelona | Barcelona | Pass | - | [56.9, 44.0] |  |
| +10.82 | +9.77 | 00:08:04.312 | Barcelona | Barcelona | Ball Receipt* | - | [57.6, 35.5] |  |
| +10.82 | +9.77 | 00:08:04.312 | Barcelona | Barcelona | Carry | - | [57.6, 35.5] |  |
| +11.68 | +10.63 | 00:08:05.170 | Barcelona | Barcelona | Pass | - | [60.1, 39.3] |  |
| +11.85 | +10.80 | 00:08:05.343 | Barcelona | Barcelona | Ball Receipt* | - | [64.2, 48.1] |  |
| +11.85 | +10.80 | 00:08:05.343 | Sevilla | Barcelona | Block | - | [58.2, 36.3] |  |
| +14.12 | +13.07 | 00:08:07.615 | Sevilla | Sevilla | Ball Recovery | - | [65.3, 33.5] |  |
| +14.12 | +13.07 | 00:08:07.615 | Sevilla | Sevilla | Carry | - | [65.3, 33.5] |  |
| +14.45 | +13.40 | 00:08:07.940 | Barcelona | Sevilla | Pressure | **YES** | [49.7, 49.2] |  |
| +14.57 | +13.52 | 00:08:08.061 | Barcelona | Sevilla | Foul Committed | **YES** | [50.5, 52.4] |  |
| +14.57 | +13.52 | 00:08:08.061 | Sevilla | Sevilla | Foul Won | - | [69.6, 27.7] |  |
| +14.57 | +13.52 | 00:08:08.061 | Sevilla | Sevilla | Carry | - | [69.6, 27.7] |  |
| +15.79 | +14.74 | 00:08:09.285 | Barcelona | Sevilla | Pressure | **YES** | [50.3, 50.4] |  |
| +16.74 | +15.70 | 00:08:10.237 | Barcelona | Sevilla | Foul Committed | **YES** | [50.1, 50.2] |  |
| +16.74 | +15.70 | 00:08:10.237 | Sevilla | Sevilla | Foul Won | - | [70.0, 29.9] |  |

---

### Episode 10: `3895153_p92_cc974c4e`
- **Match**: `3895153` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 2, Pressing Team: **Bayer Leverkusen** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Interception` by **Odilon Kossonou** at `00:07:46.027` (Turnover delay: 1.608s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Bayer Leverkusen. Harmless transition (opp max progression x=35.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.92 | -2.53 | 00:07:43.501 | Werder Bremen | Werder Bremen | Pass | - | [62.5, 27.7] |  |
| -0.18 | -1.79 | 00:07:44.239 | Bayer Leverkusen | Werder Bremen | Pressure | - | [45.8, 40.3] |  |
| +0.00 | -1.61 | 00:07:44.419 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [76.0, 35.7] | 🔄 **TURNOVER** |
| +0.00 | -1.61 | 00:07:44.419 | Werder Bremen | Werder Bremen | Carry | - | [76.0, 35.7] |  |
| +0.79 | -0.82 | 00:07:45.208 | Werder Bremen | Werder Bremen | Pass | - | [76.3, 34.5] |  |
| +1.61 | +0.00 | 00:07:46.027 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [86.3, 26.5] |  |
| +1.61 | +0.00 | 00:07:46.027 | Bayer Leverkusen | Bayer Leverkusen | Interception | **YES** | [35.6, 53.4] | ⭐ **CP INITIATION** |
| +1.61 | +0.00 | 00:07:46.027 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [35.6, 53.4] |  |
| +4.73 | +3.12 | 00:07:49.144 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [44.3, 58.8] |  |
| +5.67 | +4.06 | 00:07:50.084 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [55.5, 58.3] |  |
| +5.67 | +4.06 | 00:07:50.084 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [55.6, 58.9] |  |
| +6.83 | +5.22 | 00:07:51.249 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [50.0, 47.9] |  |
| +6.83 | +5.22 | 00:07:51.249 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [50.0, 47.9] |  |
| +10.55 | +8.94 | 00:07:54.967 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [51.1, 38.1] |  |
| +11.72 | +10.11 | 00:07:56.140 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [53.8, 24.6] |  |
| +11.72 | +10.11 | 00:07:56.140 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [53.8, 24.6] |  |
| +12.97 | +11.37 | 00:07:57.392 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [52.5, 23.6] |  |
| +13.66 | +12.05 | 00:07:58.074 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [53.5, 29.1] |  |
| +13.66 | +12.05 | 00:07:58.074 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [53.5, 29.1] |  |
| +13.96 | +12.35 | 00:07:58.374 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [52.8, 29.1] |  |
| +15.56 | +13.96 | 00:07:59.984 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [35.8, 29.7] |  |
| +15.56 | +13.96 | 00:07:59.984 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [35.8, 29.7] |  |
| +16.70 | +15.09 | 00:08:01.116 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [35.1, 31.1] |  |
| +18.15 | +16.54 | 00:08:02.571 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [40.6, 62.4] |  |
| +18.15 | +16.54 | 00:08:02.571 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [40.6, 62.4] |  |
| +20.44 | +18.83 | 00:08:04.859 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [39.9, 61.9] |  |
| +21.54 | +19.93 | 00:08:05.958 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [42.3, 52.9] |  |
| +21.54 | +19.93 | 00:08:05.958 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [42.3, 52.9] |  |

---

### Episode 11: `3802795_p132_a56f87fa`
- **Match**: `3802795` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 2, Pressing Team: **Rennes** vs. Possession Team: **Rennes**
- **Initiation Action**: `Duel` by **Birger Meling** at `00:37:07.331` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.35s by Rennes. Harmless transition (opp max progression x=12.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.41 | -1.41 | 00:37:05.924 | Rennes | Paris Saint-Germain | Pressure | - | [12.9, 15.3] |  |
| -0.74 | -0.74 | 00:37:06.596 | Rennes | Paris Saint-Germain | Dribbled Past | - | [14.5, 19.8] |  |
| -0.74 | -0.74 | 00:37:06.596 | Paris Saint-Germain | Paris Saint-Germain | Dribble | - | [105.6, 60.3] |  |
| -0.74 | -0.74 | 00:37:06.596 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [105.6, 60.3] |  |
| -0.49 | -0.49 | 00:37:06.842 | Rennes | Paris Saint-Germain | Pressure | - | [12.9, 17.0] |  |
| +0.00 | +0.00 | 00:37:07.331 | Paris Saint-Germain | Paris Saint-Germain | Dispossessed | - | [107.2, 59.4] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:37:07.331 | Rennes | Rennes | Duel | **YES** | [12.9, 20.7] | ⭐ **CP INITIATION** |
| +0.35 | +0.35 | 00:37:07.681 | Rennes | Rennes | Ball Recovery | - | [21.5, 25.7] |  |
| +0.35 | +0.35 | 00:37:07.681 | Rennes | Rennes | Carry | - | [21.5, 25.7] |  |
| +1.27 | +1.27 | 00:37:08.604 | Paris Saint-Germain | Rennes | Pressure | **YES** | [97.7, 54.4] |  |
| +1.81 | +1.81 | 00:37:09.138 | Rennes | Rennes | Pass | - | [22.4, 25.7] |  |
| +3.08 | +3.08 | 00:37:10.412 | Rennes | Rennes | Ball Receipt* | - | [40.5, 27.7] |  |
| +3.08 | +3.08 | 00:37:10.412 | Rennes | Rennes | Carry | - | [40.5, 27.7] |  |
| +3.29 | +3.29 | 00:37:10.623 | Paris Saint-Germain | Rennes | Pressure | **YES** | [78.5, 53.1] |  |
| +6.37 | +6.37 | 00:37:13.705 | Paris Saint-Germain | Rennes | Pressure | - | [66.8, 64.1] |  |
| +9.14 | +9.14 | 00:37:16.470 | Rennes | Rennes | Pass | - | [52.2, 7.5] |  |
| +10.13 | +10.13 | 00:37:17.460 | Rennes | Rennes | Ball Receipt* | - | [47.6, 13.6] |  |
| +10.13 | +10.13 | 00:37:17.460 | Rennes | Rennes | Carry | - | [47.6, 13.6] |  |
| +11.57 | +11.57 | 00:37:18.896 | Paris Saint-Germain | Rennes | Pressure | - | [67.5, 70.7] |  |
| +12.31 | +12.31 | 00:37:19.643 | Rennes | Rennes | Pass | - | [54.2, 9.0] |  |
| +12.92 | +12.92 | 00:37:20.256 | Rennes | Rennes | Ball Receipt* | - | [62.2, 3.1] |  |
| +12.92 | +12.92 | 00:37:20.256 | Rennes | Rennes | Carry | - | [62.2, 3.1] |  |
| +14.42 | +14.42 | 00:37:21.754 | Rennes | Rennes | Pass | - | [62.2, 3.1] |  |
| +15.15 | +15.15 | 00:37:22.480 | Rennes | Rennes | Ball Receipt* | - | [55.9, 13.6] |  |
| +15.15 | +15.15 | 00:37:22.480 | Rennes | Rennes | Pass | - | [55.6, 12.1] |  |
| +15.55 | +15.55 | 00:37:22.880 | Rennes | Rennes | Ball Receipt* | - | [51.5, 15.9] |  |
| +15.55 | +15.55 | 00:37:22.880 | Rennes | Rennes | Carry | - | [51.5, 15.9] |  |
| +15.72 | +15.72 | 00:37:23.050 | Paris Saint-Germain | Rennes | Pressure | - | [61.8, 62.2] |  |

---

### Episode 12: `3998842_p19_448e1e7c`
- **Match**: `3998842` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Netherlands Women's** vs. Possession Team: **Netherlands Women's**
- **Initiation Action**: `Pressure` by **Jill Roord** at `00:08:40.284` (Turnover delay: 0.175s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.977s by Netherlands Women's. Harmless transition (opp max progression x=57.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.43 | -2.61 | 00:08:37.679 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [64.4, 1.0] |  |
| -2.43 | -2.61 | 00:08:37.679 | Netherlands Women's | Netherlands Women's | Carry | - | [64.4, 1.0] |  |
| -1.83 | -2.00 | 00:08:38.282 | Netherlands Women's | Netherlands Women's | Pass | - | [64.1, 1.2] |  |
| +0.00 | -0.17 | 00:08:40.109 | Wales W | Netherlands Women's | Ball Recovery | - | [51.6, 67.7] | 🔄 **TURNOVER** |
| +0.00 | -0.17 | 00:08:40.109 | Wales W | Netherlands Women's | Carry | - | [51.6, 67.7] |  |
| +0.17 | +0.00 | 00:08:40.284 | Netherlands Women's | Netherlands Women's | Pressure | **YES** | [71.3, 8.1] | ⭐ **CP INITIATION** |
| +1.15 | +0.98 | 00:08:41.261 | Wales W | Netherlands Women's | Pass | - | [54.7, 67.5] |  |
| +2.35 | +2.18 | 00:08:42.464 | Netherlands Women's | Netherlands Women's | Pressure | **YES** | [46.7, 46.4] |  |
| +3.13 | +2.96 | 00:08:43.240 | Wales W | Netherlands Women's | Ball Receipt* | - | [67.8, 39.4] |  |
| +3.13 | +2.96 | 00:08:43.240 | Wales W | Netherlands Women's | Carry | - | [67.8, 39.4] |  |
| +3.17 | +3.00 | 00:08:43.280 | Wales W | Netherlands Women's | Pass | - | [68.5, 39.8] |  |
| +3.45 | +3.27 | 00:08:43.558 | Netherlands Women's | Netherlands Women's | Block | **YES** | [48.1, 38.8] |  |
| +4.96 | +4.79 | 00:08:45.071 | Wales W | Netherlands Women's | Pressure | - | [70.9, 48.8] |  |
| +5.19 | +5.02 | 00:08:45.301 | Netherlands Women's | Netherlands Women's | Ball Recovery | - | [50.8, 25.4] |  |
| +5.19 | +5.02 | 00:08:45.301 | Netherlands Women's | Netherlands Women's | Carry | - | [50.8, 25.4] |  |
| +6.67 | +6.49 | 00:08:46.776 | Netherlands Women's | Netherlands Women's | Pass | - | [46.0, 23.5] |  |
| +8.97 | +8.79 | 00:08:49.079 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [19.6, 39.7] |  |
| +8.97 | +8.79 | 00:08:49.079 | Netherlands Women's | Netherlands Women's | Pass | - | [19.4, 39.7] |  |
| +10.19 | +10.01 | 00:08:50.298 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [31.9, 22.6] |  |
| +10.19 | +10.01 | 00:08:50.298 | Netherlands Women's | Netherlands Women's | Carry | - | [31.9, 22.6] |  |
| +13.28 | +13.11 | 00:08:53.394 | Netherlands Women's | Netherlands Women's | Pass | - | [37.3, 17.8] |  |
| +14.20 | +14.02 | 00:08:54.307 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [47.1, 21.5] |  |
| +14.20 | +14.02 | 00:08:54.307 | Netherlands Women's | Netherlands Women's | Carry | - | [47.1, 21.5] |  |
| +16.59 | +16.42 | 00:08:56.702 | Netherlands Women's | Netherlands Women's | Pass | - | [46.7, 33.8] |  |
| +18.14 | +17.97 | 00:08:58.253 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [49.5, 63.0] |  |
| +18.14 | +17.97 | 00:08:58.253 | Netherlands Women's | Netherlands Women's | Carry | - | [49.5, 63.0] |  |
| +19.72 | +19.54 | 00:08:59.828 | Netherlands Women's | Netherlands Women's | Pass | - | [56.2, 66.3] |  |

---

### Episode 13: `3857266_p76_cf089ca2`
- **Match**: `3857266` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 1, Pressing Team: **Denmark** vs. Possession Team: **France**
- **Initiation Action**: `Pressure` by **Andreas Evald Cornelius** at `00:45:29.060` (Turnover delay: 2.915s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.915s). Dangerous transition triggered by: Final third entry at dt=7.071s (initial x=51.6, max x=97.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.29 | -5.21 | 00:45:23.851 | Denmark | Denmark | Ball Receipt* | - | [57.3, 8.1] |  |
| -2.29 | -5.21 | 00:45:23.851 | Denmark | Denmark | Carry | - | [57.3, 8.1] |  |
| -2.13 | -5.05 | 00:45:24.015 | Denmark | Denmark | Pass | - | [57.3, 8.1] |  |
| -1.31 | -4.22 | 00:45:24.836 | Denmark | Denmark | Ball Receipt* | - | [67.6, 19.4] |  |
| -1.31 | -4.22 | 00:45:24.836 | Denmark | Denmark | Carry | - | [67.6, 19.4] |  |
| -0.63 | -3.55 | 00:45:25.510 | France | Denmark | Pressure | **YES** | [52.1, 56.8] |  |
| +0.00 | -2.91 | 00:45:26.145 | Denmark | Denmark | Dispossessed | - | [68.5, 16.3] |  |
| +0.00 | -2.91 | 00:45:26.145 | France | France | Duel | **YES** | [51.6, 63.8] | 🔄 **TURNOVER** |
| +0.29 | -2.63 | 00:45:26.434 | France | France | Pass | - | [50.0, 62.4] |  |
| +2.13 | -0.79 | 00:45:28.271 | France | France | Ball Receipt* | - | [41.8, 55.9] |  |
| +2.13 | -0.79 | 00:45:28.271 | France | France | Carry | - | [41.8, 55.9] |  |
| +2.91 | +0.00 | 00:45:29.060 | Denmark | France | Pressure | **YES** | [77.9, 28.4] | ⭐ **CP INITIATION** |
| +3.45 | +0.54 | 00:45:29.596 | France | France | Pass | - | [45.6, 52.2] |  |
| +3.98 | +1.06 | 00:45:30.121 | France | France | Ball Receipt* | - | [52.4, 51.4] |  |
| +3.98 | +1.06 | 00:45:30.121 | France | France | Carry | - | [52.4, 51.4] |  |
| +4.02 | +1.10 | 00:45:30.161 | France | France | Pass | - | [53.3, 51.2] |  |
| +5.89 | +2.98 | 00:45:32.040 | France | France | Ball Receipt* | - | [45.5, 23.6] |  |
| +5.89 | +2.98 | 00:45:32.040 | France | France | Carry | - | [45.5, 23.6] |  |
| +9.99 | +7.07 | 00:45:36.131 | France | France | Pass | - | [83.6, 16.9] |  |
| +11.14 | +8.22 | 00:45:37.285 | France | France | Ball Receipt* | - | [92.3, 5.4] |  |
| +11.14 | +8.22 | 00:45:37.285 | France | France | Carry | - | [92.3, 5.4] |  |
| +13.88 | +10.97 | 00:45:40.029 | France | France | Pass | - | [97.8, 8.2] |  |
| +15.15 | +12.23 | 00:45:41.291 | France | France | Ball Receipt* | - | [85.7, 12.2] |  |
| +15.15 | +12.23 | 00:45:41.291 | France | France | Carry | - | [85.7, 12.2] |  |
| +15.63 | +12.72 | 00:45:41.776 | Denmark | France | Pressure | - | [31.2, 66.0] |  |
| +15.84 | +12.93 | 00:45:41.986 | France | France | Pass | - | [84.0, 13.3] |  |
| +16.73 | +13.81 | 00:45:42.874 | France | France | Ball Receipt* | - | [82.8, 25.7] |  |
| +16.73 | +13.81 | 00:45:42.874 | France | France | Carry | - | [82.8, 25.7] |  |
| +18.45 | +15.54 | 00:45:44.598 | France | France | Pass | - | [82.4, 27.1] |  |
| +18.89 | +15.98 | 00:45:45.036 | France | France | Ball Receipt* | - | [89.1, 28.8] |  |
| +18.89 | +15.98 | 00:45:45.036 | France | France | Carry | - | [89.1, 28.8] |  |
| +18.97 | +16.06 | 00:45:45.116 | France | France | Pass | - | [89.3, 28.8] |  |
| +19.67 | +16.76 | 00:45:45.818 | France | France | Ball Receipt* | - | [83.6, 22.0] |  |
| +19.67 | +16.76 | 00:45:45.818 | France | France | Carry | - | [83.6, 22.0] |  |
| +20.89 | +17.97 | 00:45:47.033 | France | France | Pass | - | [83.6, 17.7] |  |
| +22.18 | +19.26 | 00:45:48.323 | France | France | Ball Receipt* | - | [99.6, 7.3] |  |
| +22.18 | +19.26 | 00:45:48.323 | France | France | Carry | - | [99.6, 7.3] |  |

---

### Episode 14: `3998846_p15_78410598`
- **Match**: `3998846` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Italy Women's** vs. Possession Team: **Italy Women's**
- **Initiation Action**: `Duel` by **Manuela Giugliano** at `00:05:35.266` (Turnover delay: 1.004s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.62s by Italy Women's. Harmless transition (opp max progression x=35.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.80 | -3.80 | 00:05:31.465 | Portugal Women's | Portugal Women's | Pressure | **YES** | [81.6, 75.8] |  |
| -2.61 | -3.61 | 00:05:31.654 | Portugal Women's | Portugal Women's | Dribbled Past | **YES** | [83.2, 77.4] |  |
| -2.61 | -3.61 | 00:05:31.654 | Italy Women's | Portugal Women's | Dribble | - | [36.9, 2.7] |  |
| -2.61 | -3.61 | 00:05:31.654 | Italy Women's | Portugal Women's | Carry | - | [36.9, 2.7] |  |
| -1.63 | -2.64 | 00:05:32.631 | Italy Women's | Portugal Women's | Dispossessed | - | [37.7, 6.6] |  |
| -1.63 | -2.64 | 00:05:32.631 | Portugal Women's | Portugal Women's | Duel | **YES** | [82.4, 73.5] |  |
| -0.10 | -1.11 | 00:05:34.159 | Italy Women's | Portugal Women's | Pressure | - | [33.6, 4.7] |  |
| +0.00 | -1.00 | 00:05:34.262 | Portugal Women's | Portugal Women's | Ball Recovery | - | [84.8, 75.6] | 🔄 **TURNOVER** |
| +0.00 | -1.00 | 00:05:34.262 | Portugal Women's | Portugal Women's | Carry | - | [84.8, 75.6] |  |
| +1.00 | +0.00 | 00:05:35.266 | Portugal Women's | Portugal Women's | Dispossessed | - | [84.8, 74.4] |  |
| +1.00 | +0.00 | 00:05:35.266 | Italy Women's | Italy Women's | Duel | **YES** | [35.3, 5.7] | ⭐ **CP INITIATION** |
| +1.62 | +0.62 | 00:05:35.886 | Italy Women's | Italy Women's | Ball Recovery | - | [38.9, 7.0] |  |
| +1.62 | +0.62 | 00:05:35.886 | Italy Women's | Italy Women's | Carry | - | [38.9, 7.0] |  |
| +2.23 | +1.22 | 00:05:36.490 | Italy Women's | Italy Women's | Pass | - | [38.3, 7.7] |  |
| +3.21 | +2.21 | 00:05:37.474 | Italy Women's | Italy Women's | Ball Receipt* | - | [27.2, 8.2] |  |
| +3.21 | +2.21 | 00:05:37.474 | Italy Women's | Italy Women's | Carry | - | [27.2, 8.2] |  |
| +4.92 | +3.91 | 00:05:39.180 | Italy Women's | Italy Women's | Pass | - | [26.9, 8.2] |  |
| +5.75 | +4.74 | 00:05:40.008 | Italy Women's | Italy Women's | Ball Receipt* | - | [29.5, 14.3] |  |
| +5.75 | +4.74 | 00:05:40.008 | Italy Women's | Italy Women's | Carry | - | [29.5, 14.3] |  |
| +6.68 | +5.68 | 00:05:40.943 | Italy Women's | Italy Women's | Pass | - | [27.2, 19.5] |  |
| +9.14 | +8.14 | 00:05:43.403 | Italy Women's | Italy Women's | Ball Receipt* | - | [36.5, 68.4] |  |
| +9.14 | +8.14 | 00:05:43.403 | Italy Women's | Italy Women's | Carry | - | [36.5, 68.4] |  |
| +16.94 | +15.93 | 00:05:51.199 | Italy Women's | Italy Women's | Pass | - | [88.1, 72.6] |  |
| +17.56 | +16.56 | 00:05:51.826 | Italy Women's | Italy Women's | Ball Receipt* | - | [91.7, 76.7] |  |
| +17.56 | +16.56 | 00:05:51.826 | Italy Women's | Italy Women's | Carry | - | [91.7, 76.7] |  |
| +17.90 | +16.90 | 00:05:52.165 | Italy Women's | Italy Women's | Pass | - | [91.7, 76.4] |  |

---

### Episode 15: `4020077_p51_28e0ed26`
- **Match**: `4020077` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Germany Women's** vs. Possession Team: **Spain Women's**
- **Initiation Action**: `Pressure` by **Jule Brand** at `00:22:18.235` (Turnover delay: 1.301s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.301s). Dangerous transition triggered by: Final third entry at dt=10.887s (initial x=35.2, max x=86.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.07 | -3.37 | 00:22:14.867 | Germany Women's | Germany Women's | Pass | - | [78.4, 45.3] |  |
| -1.28 | -2.58 | 00:22:15.653 | Germany Women's | Germany Women's | Ball Receipt* | - | [68.3, 38.3] |  |
| -1.28 | -2.58 | 00:22:15.653 | Germany Women's | Germany Women's | Carry | - | [68.3, 38.3] |  |
| -1.24 | -2.54 | 00:22:15.698 | Germany Women's | Germany Women's | Pass | - | [68.3, 38.3] |  |
| +0.00 | -1.30 | 00:22:16.934 | Spain Women's | Spain Women's | Ball Recovery | - | [35.2, 57.1] | 🔄 **TURNOVER** |
| +0.00 | -1.30 | 00:22:16.934 | Spain Women's | Spain Women's | Carry | - | [35.2, 57.1] |  |
| +1.30 | +0.00 | 00:22:18.235 | Germany Women's | Spain Women's | Pressure | **YES** | [81.5, 17.6] | ⭐ **CP INITIATION** |
| +2.25 | +0.95 | 00:22:19.186 | Spain Women's | Spain Women's | Pass | - | [44.2, 56.9] |  |
| +2.76 | +1.46 | 00:22:19.694 | Spain Women's | Spain Women's | Ball Receipt* | - | [45.1, 51.5] |  |
| +2.76 | +1.46 | 00:22:19.694 | Spain Women's | Spain Women's | Carry | - | [45.1, 51.5] |  |
| +3.37 | +2.06 | 00:22:20.299 | Spain Women's | Spain Women's | Pass | - | [42.5, 53.8] |  |
| +4.62 | +3.32 | 00:22:21.556 | Germany Women's | Spain Women's | Pressure | **YES** | [79.7, 16.8] |  |
| +5.21 | +3.91 | 00:22:22.148 | Spain Women's | Spain Women's | Ball Receipt* | - | [40.2, 68.7] |  |
| +5.21 | +3.91 | 00:22:22.148 | Spain Women's | Spain Women's | Carry | - | [40.2, 68.7] |  |
| +11.32 | +10.02 | 00:22:28.255 | Germany Women's | Spain Women's | Pressure | - | [43.6, 9.4] |  |
| +12.19 | +10.89 | 00:22:29.122 | Spain Women's | Spain Women's | Pass | - | [80.9, 75.2] |  |
| +12.91 | +11.61 | 00:22:29.842 | Spain Women's | Spain Women's | Ball Receipt* | - | [86.3, 79.0] |  |
| +12.91 | +11.61 | 00:22:29.842 | Spain Women's | Spain Women's | Carry | - | [86.3, 79.0] |  |
| +13.37 | +12.07 | 00:22:30.305 | Germany Women's | Spain Women's | Pressure | - | [32.4, 2.4] |  |
| +13.65 | +12.35 | 00:22:30.580 | Spain Women's | Spain Women's | Pass | - | [84.6, 78.3] |  |

---

### Episode 16: `3895167_p93_36cfb088`
- **Match**: `3895167` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 2, Pressing Team: **VfB Stuttgart** vs. Possession Team: **VfB Stuttgart**
- **Initiation Action**: `Duel` by **Josha Mamadou Karaboue Vagnoman** at `00:02:28.358` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by VfB Stuttgart. Harmless transition (opp max progression x=40.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.50 | -2.50 | 00:02:25.860 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [63.6, 23.4] |  |
| -1.41 | -1.41 | 00:02:26.946 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [71.8, 19.8] |  |
| -1.41 | -1.41 | 00:02:26.946 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [71.8, 19.8] |  |
| -0.94 | -0.94 | 00:02:27.415 | VfB Stuttgart | Bayer Leverkusen | Pressure | - | [49.2, 61.6] |  |
| +0.00 | +0.00 | 00:02:28.358 | Bayer Leverkusen | Bayer Leverkusen | Dribble | - | [79.8, 24.4] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:02:28.358 | VfB Stuttgart | VfB Stuttgart | Duel | **YES** | [40.3, 55.7] | ⭐ **CP INITIATION** |
| +0.00 | +0.00 | 00:02:28.358 | VfB Stuttgart | VfB Stuttgart | Carry | - | [40.3, 55.7] |  |
| +2.82 | +2.82 | 00:02:31.180 | VfB Stuttgart | VfB Stuttgart | Pass | - | [36.8, 63.7] |  |
| +3.92 | +3.92 | 00:02:32.277 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [38.4, 76.3] |  |
| +3.92 | +3.92 | 00:02:32.277 | VfB Stuttgart | VfB Stuttgart | Carry | - | [38.4, 76.3] |  |
| +4.03 | +4.03 | 00:02:32.386 | VfB Stuttgart | VfB Stuttgart | Pass | - | [38.4, 76.3] |  |
| +5.80 | +5.80 | 00:02:34.159 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [22.1, 62.8] |  |
| +5.80 | +5.80 | 00:02:34.159 | VfB Stuttgart | VfB Stuttgart | Carry | - | [22.1, 62.8] |  |
| +8.64 | +8.64 | 00:02:37.000 | VfB Stuttgart | VfB Stuttgart | Pass | - | [19.9, 57.5] |  |
| +10.84 | +10.84 | 00:02:39.202 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [4.8, 39.7] |  |
| +10.84 | +10.84 | 00:02:39.202 | VfB Stuttgart | VfB Stuttgart | Carry | - | [4.8, 39.7] |  |

---

### Episode 17: `3773386_p126_912ddd86`
- **Match**: `3773386` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Deportivo Alavés** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Tomas Franco Tavares** at `00:30:13.593` (Turnover delay: 2.98s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.98s). Dangerous transition triggered by: Final third entry at dt=13.087s (initial x=29.6, max x=93.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.04 | -5.02 | 00:30:08.577 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [69.8, 52.5] |  |
| -1.96 | -4.94 | 00:30:08.657 | Deportivo Alavés | Deportivo Alavés | Pass | - | [69.8, 52.5] |  |
| +0.00 | -2.98 | 00:30:10.613 | Barcelona | Barcelona | Ball Recovery | - | [29.6, 21.4] | 🔄 **TURNOVER** |
| +0.00 | -2.98 | 00:30:10.613 | Barcelona | Barcelona | Carry | - | [29.6, 21.4] |  |
| +0.89 | -2.09 | 00:30:11.500 | Barcelona | Barcelona | Pass | - | [22.3, 21.8] |  |
| +2.38 | -0.60 | 00:30:12.992 | Barcelona | Barcelona | Ball Receipt* | - | [9.1, 33.3] |  |
| +2.38 | -0.60 | 00:30:12.992 | Barcelona | Barcelona | Carry | - | [9.1, 33.3] |  |
| +2.98 | +0.00 | 00:30:13.593 | Deportivo Alavés | Barcelona | Pressure | **YES** | [108.1, 48.2] | ⭐ **CP INITIATION** |
| +3.48 | +0.50 | 00:30:14.092 | Barcelona | Barcelona | Pass | - | [8.1, 36.6] |  |
| +4.55 | +1.57 | 00:30:15.165 | Barcelona | Barcelona | Ball Receipt* | - | [19.2, 39.3] |  |
| +4.55 | +1.57 | 00:30:15.165 | Barcelona | Barcelona | Carry | - | [19.2, 39.3] |  |
| +6.62 | +3.64 | 00:30:17.232 | Barcelona | Barcelona | Pass | - | [27.3, 39.8] |  |
| +8.97 | +5.99 | 00:30:19.585 | Barcelona | Barcelona | Ball Receipt* | - | [47.4, 8.7] |  |
| +8.97 | +5.99 | 00:30:19.585 | Barcelona | Barcelona | Carry | - | [47.4, 8.7] |  |
| +16.07 | +13.09 | 00:30:26.680 | Barcelona | Barcelona | Pass | - | [81.7, 10.5] |  |
| +17.20 | +14.22 | 00:30:27.814 | Barcelona | Barcelona | Ball Receipt* | - | [93.9, 6.0] |  |
| +17.20 | +14.22 | 00:30:27.814 | Barcelona | Barcelona | Carry | - | [93.9, 6.0] |  |
| +19.53 | +16.55 | 00:30:30.144 | Barcelona | Barcelona | Pass | - | [102.7, 12.6] |  |
| +20.18 | +17.20 | 00:30:30.796 | Barcelona | Barcelona | Pressure | - | [105.2, 22.7] |  |
| +20.33 | +17.35 | 00:30:30.944 | Barcelona | Barcelona | Ball Receipt* | - | [105.2, 22.7] |  |
| +20.33 | +17.35 | 00:30:30.944 | Deportivo Alavés | Barcelona | Clearance | - | [14.9, 57.4] |  |

---

### Episode 18: `3773625_p166_59d717c7`
- **Match**: `3773625` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Sevilla** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Óscar Rodríguez Arnaiz** at `00:39:30.329` (Turnover delay: 4.572s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=4.572s). Dangerous transition triggered by: Final third entry at dt=12.151s (initial x=47.1, max x=97.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.67 | -7.25 | 00:39:23.084 | Sevilla | Sevilla | Shot | - | [91.2, 46.6] |  |
| -2.18 | -6.76 | 00:39:23.574 | Barcelona | Sevilla | Block | - | [13.4, 37.9] |  |
| -2.14 | -6.72 | 00:39:23.614 | Barcelona | Sevilla | Goal Keeper | - | [2.1, 39.8] |  |
| +0.00 | -4.57 | 00:39:25.757 | Barcelona | Barcelona | Ball Recovery | - | [47.1, 34.6] | 🔄 **TURNOVER** |
| +0.00 | -4.57 | 00:39:25.757 | Barcelona | Barcelona | Carry | - | [47.1, 34.6] |  |
| +3.55 | -1.02 | 00:39:29.309 | Barcelona | Barcelona | Pass | - | [50.7, 63.3] |  |
| +4.53 | -0.05 | 00:39:30.283 | Barcelona | Barcelona | Ball Receipt* | - | [47.5, 57.7] |  |
| +4.53 | -0.05 | 00:39:30.283 | Barcelona | Barcelona | Carry | - | [47.5, 57.7] |  |
| +4.57 | +0.00 | 00:39:30.329 | Sevilla | Barcelona | Pressure | **YES** | [72.4, 24.1] | ⭐ **CP INITIATION** |
| +5.46 | +0.89 | 00:39:31.221 | Barcelona | Barcelona | Pass | - | [51.2, 57.5] |  |
| +6.72 | +2.15 | 00:39:32.476 | Barcelona | Barcelona | Ball Receipt* | - | [67.4, 73.1] |  |
| +6.72 | +2.15 | 00:39:32.476 | Barcelona | Barcelona | Carry | - | [67.4, 73.1] |  |
| +8.44 | +3.87 | 00:39:34.198 | Barcelona | Barcelona | Pass | - | [73.6, 72.9] |  |
| +11.49 | +6.92 | 00:39:37.245 | Barcelona | Barcelona | Ball Receipt* | - | [77.9, 6.8] |  |
| +11.49 | +6.92 | 00:39:37.245 | Barcelona | Barcelona | Carry | - | [77.9, 6.8] |  |
| +14.81 | +10.23 | 00:39:40.564 | Sevilla | Barcelona | Pressure | - | [22.9, 56.0] |  |
| +16.72 | +12.15 | 00:39:42.480 | Barcelona | Barcelona | Pass | - | [97.8, 18.1] |  |
| +18.55 | +13.98 | 00:39:44.307 | Barcelona | Barcelona | Ball Receipt* | - | [70.8, 5.3] |  |
| +18.55 | +13.98 | 00:39:44.307 | Barcelona | Barcelona | Carry | - | [70.8, 5.3] |  |
| +19.45 | +14.88 | 00:39:45.209 | Barcelona | Barcelona | Pass | - | [70.8, 5.3] |  |
| +20.71 | +16.13 | 00:39:46.464 | Barcelona | Barcelona | Ball Receipt* | - | [70.2, 28.0] |  |
| +20.71 | +16.13 | 00:39:46.464 | Barcelona | Barcelona | Carry | - | [70.2, 28.0] |  |
| +21.75 | +17.18 | 00:39:47.509 | Barcelona | Barcelona | Pass | - | [70.2, 28.0] |  |
| +22.99 | +18.41 | 00:39:48.742 | Barcelona | Barcelona | Ball Receipt* | - | [77.7, 36.3] |  |
| +22.99 | +18.41 | 00:39:48.742 | Barcelona | Barcelona | Carry | - | [77.7, 36.3] |  |

---

### Episode 19: `3773593_p47_ae97833a`
- **Match**: `3773593` | **Competition**: La Liga (2020/2021)
- **Context**: Period 1, Pressing Team: **Villarreal** vs. Possession Team: **Villarreal**
- **Initiation Action**: `Pressure` by **Daniel Parejo Muñoz** at `00:28:53.843` (Turnover delay: 1.134s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.402s by Villarreal. Harmless transition (opp max progression x=27.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.00 | -3.14 | 00:28:50.705 | Villarreal | Villarreal | Pass | - | [36.8, 38.5] |  |
| -1.04 | -2.18 | 00:28:51.667 | Barcelona | Villarreal | Pressure | - | [74.7, 23.7] |  |
| -0.64 | -1.77 | 00:28:52.070 | Villarreal | Villarreal | Ball Receipt* | - | [43.0, 51.5] |  |
| -0.64 | -1.77 | 00:28:52.070 | Villarreal | Villarreal | Carry | - | [43.0, 51.5] |  |
| +0.00 | -1.13 | 00:28:52.709 | Villarreal | Villarreal | Dispossessed | - | [41.1, 53.6] |  |
| +0.00 | -1.13 | 00:28:52.709 | Barcelona | Villarreal | Duel | - | [79.0, 26.5] | 🔄 **TURNOVER** |
| +0.00 | -1.13 | 00:28:52.709 | Barcelona | Villarreal | Carry | - | [79.0, 26.5] |  |
| +1.13 | +0.00 | 00:28:53.843 | Villarreal | Villarreal | Pressure | **YES** | [39.6, 53.4] | ⭐ **CP INITIATION** |
| +1.54 | +0.40 | 00:28:54.245 | Barcelona | Villarreal | Pass | - | [82.8, 27.3] |  |
| +2.51 | +1.38 | 00:28:55.221 | Barcelona | Villarreal | Pressure | - | [93.1, 30.9] |  |
| +3.00 | +1.87 | 00:28:55.710 | Barcelona | Villarreal | Ball Receipt* | - | [93.7, 30.7] |  |
| +3.00 | +1.87 | 00:28:55.710 | Villarreal | Villarreal | Interception | **YES** | [23.4, 50.4] |  |
| +3.00 | +1.87 | 00:28:55.710 | Villarreal | Villarreal | Carry | - | [23.4, 50.4] |  |
| +4.09 | +2.95 | 00:28:56.796 | Villarreal | Villarreal | Pass | - | [18.9, 37.4] |  |
| +5.25 | +4.11 | 00:28:57.955 | Villarreal | Villarreal | Ball Receipt* | - | [4.7, 39.3] |  |
| +5.25 | +4.11 | 00:28:57.955 | Villarreal | Villarreal | Pass | - | [5.2, 39.3] |  |
| +8.65 | +7.51 | 00:29:01.358 | Villarreal | Villarreal | Ball Receipt* | - | [35.8, 12.4] |  |
| +8.65 | +7.51 | 00:29:01.358 | Villarreal | Villarreal | Carry | - | [35.8, 12.4] |  |
| +8.78 | +7.65 | 00:29:01.490 | Barcelona | Villarreal | Block | - | [81.6, 68.0] |  |
| +8.84 | +7.70 | 00:29:01.548 | Villarreal | Villarreal | Miscontrol | - | [38.3, 12.1] |  |
| +9.59 | +8.46 | 00:29:02.303 | Villarreal | Villarreal | Pressure | - | [35.3, 15.8] |  |
| +10.55 | +9.42 | 00:29:03.260 | Barcelona | Barcelona | Ball Recovery | - | [85.2, 55.1] |  |
| +10.55 | +9.42 | 00:29:03.260 | Barcelona | Barcelona | Carry | - | [85.2, 55.1] |  |
| +10.81 | +9.67 | 00:29:03.518 | Barcelona | Barcelona | Dispossessed | - | [84.8, 55.3] |  |
| +10.81 | +9.67 | 00:29:03.518 | Villarreal | Barcelona | Duel | **YES** | [35.3, 24.8] |  |
| +12.06 | +10.92 | 00:29:04.768 | Barcelona | Barcelona | Ball Recovery | - | [84.3, 54.7] |  |
| +12.06 | +10.92 | 00:29:04.768 | Barcelona | Barcelona | Carry | - | [84.3, 54.7] |  |
| +14.09 | +12.95 | 00:29:06.795 | Villarreal | Barcelona | Pressure | **YES** | [35.8, 40.6] |  |
| +14.61 | +13.47 | 00:29:07.318 | Barcelona | Barcelona | Pass | - | [85.2, 32.0] |  |
| +15.55 | +14.41 | 00:29:08.256 | Barcelona | Barcelona | Ball Receipt* | - | [83.9, 22.4] |  |
| +15.55 | +14.41 | 00:29:08.256 | Barcelona | Barcelona | Carry | - | [83.9, 22.4] |  |
| +17.11 | +15.97 | 00:29:09.818 | Barcelona | Barcelona | Pass | - | [92.7, 23.5] |  |
| +18.62 | +17.48 | 00:29:11.328 | Barcelona | Barcelona | Ball Receipt* | - | [112.8, 21.5] |  |
| +18.62 | +17.48 | 00:29:11.328 | Barcelona | Barcelona | Carry | - | [112.8, 21.5] |  |
| +18.80 | +17.67 | 00:29:11.510 | Barcelona | Barcelona | Pass | - | [114.5, 22.6] |  |
| +19.01 | +17.88 | 00:29:11.721 | Villarreal | Barcelona | Block | - | [8.8, 53.4] |  |
| +19.67 | +18.53 | 00:29:12.376 | Barcelona | Barcelona | Ball Recovery | - | [109.1, 30.5] |  |
| +19.95 | +18.82 | 00:29:12.662 | Villarreal | Villarreal | Pass | - | [11.0, 45.9] |  |
| +20.03 | +18.90 | 00:29:12.743 | Barcelona | Villarreal | Pressure | **YES** | [108.1, 31.8] |  |
| +20.67 | +19.54 | 00:29:13.383 | Villarreal | Villarreal | Ball Receipt* | - | [12.0, 50.4] |  |
| +20.67 | +19.54 | 00:29:13.383 | Villarreal | Villarreal | Carry | - | [12.0, 50.4] |  |

---

### Episode 20: `3998852_p116_0d2a6821`
- **Match**: `3998852` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 2, Pressing Team: **Switzerland Women's** vs. Possession Team: **Switzerland Women's**
- **Initiation Action**: `Pressure` by **Géraldine Reuteler** at `00:06:14.281` (Turnover delay: 0.524s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.482s by Switzerland Women's. Harmless transition (opp max progression x=43.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.23 | -1.75 | 00:06:12.527 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [43.7, 62.2] |  |
| -1.23 | -1.75 | 00:06:12.527 | Switzerland Women's | Switzerland Women's | Carry | - | [43.7, 62.2] |  |
| -1.21 | -1.73 | 00:06:12.549 | WNT Finland | Switzerland Women's | Pressure | - | [72.6, 20.9] |  |
| -0.87 | -1.39 | 00:06:12.891 | Switzerland Women's | Switzerland Women's | Pass | - | [44.4, 66.7] |  |
| +0.00 | -0.52 | 00:06:13.757 | WNT Finland | Switzerland Women's | Interception | - | [70.8, 15.5] | 🔄 **TURNOVER** |
| +0.00 | -0.52 | 00:06:13.757 | WNT Finland | Switzerland Women's | Carry | - | [70.8, 15.5] |  |
| +0.52 | +0.00 | 00:06:14.281 | Switzerland Women's | Switzerland Women's | Pressure | **YES** | [50.6, 64.0] | ⭐ **CP INITIATION** |
| +1.01 | +0.48 | 00:06:14.763 | WNT Finland | Switzerland Women's | Dispossessed | - | [70.8, 15.3] |  |
| +1.01 | +0.48 | 00:06:14.763 | Switzerland Women's | Switzerland Women's | Duel | **YES** | [49.3, 64.8] |  |
| +1.01 | +0.48 | 00:06:14.763 | Switzerland Women's | Switzerland Women's | Carry | - | [49.3, 64.8] |  |
| +5.88 | +5.36 | 00:06:19.640 | Switzerland Women's | Switzerland Women's | Pass | - | [51.4, 41.1] |  |
| +7.98 | +7.45 | 00:06:21.735 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [54.5, 10.1] |  |
| +7.98 | +7.45 | 00:06:21.735 | Switzerland Women's | Switzerland Women's | Carry | - | [54.5, 10.1] |  |
| +9.19 | +8.66 | 00:06:22.942 | Switzerland Women's | Switzerland Women's | Pass | - | [57.8, 7.0] |  |
| +10.36 | +9.84 | 00:06:24.121 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [76.0, 2.4] |  |
| +10.36 | +9.84 | 00:06:24.121 | Switzerland Women's | Switzerland Women's | Carry | - | [76.0, 2.4] |  |
| +14.59 | +14.07 | 00:06:28.352 | Switzerland Women's | Switzerland Women's | Pass | - | [85.3, 6.1] |  |
| +15.65 | +15.12 | 00:06:29.403 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [76.0, 15.9] |  |
| +15.65 | +15.12 | 00:06:29.403 | Switzerland Women's | Switzerland Women's | Carry | - | [76.0, 15.9] |  |
| +18.32 | +17.80 | 00:06:32.080 | Switzerland Women's | Switzerland Women's | Pass | - | [71.2, 19.5] |  |
| +20.01 | +19.49 | 00:06:33.771 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [62.4, 15.2] |  |
| +20.01 | +19.49 | 00:06:33.771 | Switzerland Women's | Switzerland Women's | Carry | - | [62.4, 15.2] |  |
| +20.05 | +19.53 | 00:06:33.811 | Switzerland Women's | Switzerland Women's | Pass | - | [62.4, 15.2] |  |

---

### Episode 21: `3788741_p101_4bc13596`
- **Match**: `3788741` | **Competition**: UEFA Euro (2020)
- **Context**: Period 1, Pressing Team: **Turkey** vs. Possession Team: **Italy**
- **Initiation Action**: `Pressure` by **Hakan Çalhanoğlu** at `00:39:19.408` (Turnover delay: 2.281s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.281s). Harmless transition (opp max progression x=57.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.86 | -3.15 | 00:39:16.262 | Italy | Turkey | Pressure | - | [36.0, 10.3] |  |
| -0.79 | -3.07 | 00:39:16.333 | Turkey | Turkey | Ball Recovery | - | [83.6, 70.0] |  |
| -0.79 | -3.07 | 00:39:16.333 | Turkey | Turkey | Carry | - | [83.6, 70.0] |  |
| +0.00 | -2.28 | 00:39:17.127 | Turkey | Turkey | Dribble | - | [84.9, 70.7] |  |
| +0.00 | -2.28 | 00:39:17.127 | Italy | Italy | Duel | **YES** | [35.2, 9.4] | 🔄 **TURNOVER** |
| +0.92 | -1.36 | 00:39:18.050 | Italy | Italy | Pass | - | [37.1, 10.5] |  |
| +1.65 | -0.63 | 00:39:18.778 | Italy | Italy | Ball Receipt* | - | [35.0, 20.7] |  |
| +1.65 | -0.63 | 00:39:18.778 | Italy | Italy | Carry | - | [35.0, 20.7] |  |
| +2.28 | +0.00 | 00:39:19.408 | Turkey | Italy | Pressure | **YES** | [84.4, 53.0] | ⭐ **CP INITIATION** |
| +3.43 | +1.15 | 00:39:20.559 | Italy | Italy | Pass | - | [35.7, 20.4] |  |
| +4.31 | +2.03 | 00:39:21.436 | Italy | Italy | Ball Receipt* | - | [26.8, 21.8] |  |
| +4.31 | +2.03 | 00:39:21.436 | Italy | Italy | Carry | - | [26.8, 21.8] |  |
| +5.33 | +3.04 | 00:39:22.452 | Italy | Italy | Pass | - | [23.0, 22.0] |  |
| +6.59 | +4.31 | 00:39:23.718 | Turkey | Italy | Pressure | - | [105.0, 44.4] |  |
| +6.91 | +4.63 | 00:39:24.041 | Italy | Italy | Ball Receipt* | - | [4.3, 37.9] |  |
| +6.91 | +4.63 | 00:39:24.041 | Italy | Italy | Carry | - | [4.3, 37.9] |  |
| +7.66 | +5.38 | 00:39:24.784 | Italy | Italy | Pass | - | [4.1, 38.4] |  |
| +10.41 | +8.13 | 00:39:27.539 | Italy | Italy | Ball Receipt* | - | [17.8, 68.6] |  |
| +10.41 | +8.13 | 00:39:27.539 | Italy | Italy | Carry | - | [17.8, 68.6] |  |
| +12.32 | +10.04 | 00:39:29.451 | Italy | Italy | Pass | - | [28.8, 72.7] |  |
| +13.85 | +11.57 | 00:39:30.976 | Turkey | Italy | Pressure | - | [69.3, 6.7] |  |
| +14.28 | +12.00 | 00:39:31.405 | Italy | Italy | Ball Receipt* | - | [57.8, 77.3] |  |
| +14.28 | +12.00 | 00:39:31.405 | Italy | Italy | Pass | - | [56.6, 76.5] |  |
| +16.51 | +14.22 | 00:39:33.632 | Italy | Italy | Ball Receipt* | - | [45.1, 74.8] |  |
| +16.51 | +14.22 | 00:39:33.632 | Italy | Italy | Carry | - | [45.1, 74.8] |  |
| +20.41 | +18.12 | 00:39:37.532 | Italy | Italy | Pass | - | [55.4, 75.3] |  |
| +21.41 | +19.12 | 00:39:38.532 | Italy | Italy | Ball Receipt* | - | [71.3, 70.5] |  |
| +21.41 | +19.12 | 00:39:38.532 | Italy | Italy | Carry | - | [71.3, 70.5] |  |

---

### Episode 22: `3835331_p195_6834628d`
- **Match**: `3835331` | **Competition**: UEFA Women's Euro (2022)
- **Context**: Period 2, Pressing Team: **Switzerland Women's** vs. Possession Team: **Sweden Women's**
- **Initiation Action**: `Pressure` by **Rachel Rinast** at `00:42:09.496` (Turnover delay: 3.017s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.017s). Dangerous transition triggered by: Final third entry at dt=0.466s (initial x=62.1, max x=102.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.06 | -5.08 | 00:42:04.419 | Sweden Women's | Switzerland Women's | Pressure | - | [60.4, 71.2] |  |
| -1.84 | -4.86 | 00:42:04.636 | Switzerland Women's | Switzerland Women's | Ball Receipt* | - | [54.6, 8.1] |  |
| -1.84 | -4.86 | 00:42:04.636 | Switzerland Women's | Switzerland Women's | Pass | - | [53.9, 8.3] |  |
| +0.00 | -3.02 | 00:42:06.479 | Sweden Women's | Sweden Women's | Pass | - | [62.1, 55.8] | 🔄 **TURNOVER** |
| +0.85 | -2.17 | 00:42:07.324 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [71.1, 47.8] |  |
| +0.85 | -2.17 | 00:42:07.324 | Sweden Women's | Sweden Women's | Carry | - | [71.1, 47.8] |  |
| +1.83 | -1.19 | 00:42:08.308 | Sweden Women's | Sweden Women's | Pass | - | [71.1, 47.8] |  |
| +3.02 | +0.00 | 00:42:09.496 | Switzerland Women's | Sweden Women's | Pressure | **YES** | [28.9, 23.3] | ⭐ **CP INITIATION** |
| +3.48 | +0.47 | 00:42:09.962 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [92.0, 53.4] |  |
| +3.48 | +0.47 | 00:42:09.962 | Sweden Women's | Sweden Women's | Carry | - | [92.0, 53.4] |  |
| +3.70 | +0.68 | 00:42:10.177 | Sweden Women's | Sweden Women's | Pass | - | [92.0, 54.9] |  |
| +5.37 | +2.36 | 00:42:11.853 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [102.9, 37.6] |  |

---

### Episode 23: `3788757_p82_dbc2fb05`
- **Match**: `3788757` | **Competition**: UEFA Euro (2020)
- **Context**: Period 1, Pressing Team: **Denmark** vs. Possession Team: **Denmark**
- **Initiation Action**: `Duel` by **Andreas Christensen** at `00:35:36.984` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Denmark. Harmless transition (opp max progression x=42.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.33 | -2.33 | 00:35:34.653 | Belgium | Belgium | Pass | - | [63.6, 36.1] |  |
| -1.36 | -1.36 | 00:35:35.627 | Belgium | Belgium | Ball Receipt* | - | [72.3, 31.4] |  |
| -1.36 | -1.36 | 00:35:35.627 | Belgium | Belgium | Carry | - | [72.3, 31.4] |  |
| -1.04 | -1.04 | 00:35:35.947 | Denmark | Belgium | Pressure | - | [49.0, 50.2] |  |
| +0.00 | +0.00 | 00:35:36.984 | Belgium | Belgium | Dribble | - | [77.5, 34.2] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:35:36.984 | Denmark | Denmark | Duel | **YES** | [42.6, 45.9] | ⭐ **CP INITIATION** |
| +0.00 | +0.00 | 00:35:36.984 | Denmark | Denmark | Carry | - | [42.6, 45.9] |  |
| +1.37 | +1.37 | 00:35:38.352 | Denmark | Denmark | Pass | - | [37.3, 39.9] |  |
| +2.51 | +2.51 | 00:35:39.494 | Denmark | Denmark | Ball Receipt* | - | [32.1, 33.5] |  |
| +2.51 | +2.51 | 00:35:39.494 | Denmark | Denmark | Carry | - | [32.1, 33.5] |  |
| +3.03 | +3.03 | 00:35:40.009 | Denmark | Denmark | Pass | - | [32.4, 32.0] |  |
| +4.57 | +4.57 | 00:35:41.556 | Denmark | Denmark | Ball Receipt* | - | [37.1, 12.8] |  |
| +4.57 | +4.57 | 00:35:41.556 | Denmark | Denmark | Carry | - | [37.1, 12.8] |  |
| +7.90 | +7.90 | 00:35:44.880 | Denmark | Denmark | Pass | - | [63.8, 8.3] |  |
| +8.08 | +8.08 | 00:35:45.062 | Denmark | Denmark | Ball Receipt* | - | [69.6, 2.7] |  |
| +8.08 | +8.08 | 00:35:45.062 | Belgium | Denmark | Interception | - | [54.4, 73.3] |  |

---

### Episode 24: `3895139_p41_e94fca89`
- **Match**: `3895139` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Union Berlin** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Pressure` by **Sheraldo Becker** at `00:21:26.219` (Turnover delay: 1.609s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.609s). Harmless transition (opp max progression x=72.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.74 | -3.35 | 00:21:22.870 | Union Berlin | Union Berlin | Pass | - | [67.1, 21.4] |  |
| +0.00 | -1.61 | 00:21:24.610 | Union Berlin | Union Berlin | Ball Receipt* | - | [87.6, 14.5] |  |
| +0.00 | -1.61 | 00:21:24.610 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [38.3, 64.1] | 🔄 **TURNOVER** |
| +1.21 | -0.40 | 00:21:25.822 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [49.7, 69.1] |  |
| +1.21 | -0.40 | 00:21:25.822 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [49.7, 69.1] |  |
| +1.61 | +0.00 | 00:21:26.219 | Union Berlin | Bayer Leverkusen | Pressure | **YES** | [76.5, 11.0] | ⭐ **CP INITIATION** |
| +3.25 | +1.64 | 00:21:27.863 | Union Berlin | Bayer Leverkusen | Foul Committed | **YES** | [71.0, 13.1] |  |
| +3.25 | +1.64 | 00:21:27.863 | Bayer Leverkusen | Bayer Leverkusen | Foul Won | - | [49.1, 67.0] |  |
| +11.11 | +9.50 | 00:21:35.723 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [50.1, 69.4] |  |
| +12.66 | +11.05 | 00:21:37.274 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [55.4, 59.0] |  |
| +12.66 | +11.05 | 00:21:37.274 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [55.4, 59.0] |  |
| +13.62 | +12.01 | 00:21:38.226 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [55.1, 57.4] |  |
| +14.68 | +13.07 | 00:21:39.286 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [53.9, 37.3] |  |
| +14.68 | +13.07 | 00:21:39.286 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [53.9, 37.3] |  |
| +15.70 | +14.09 | 00:21:40.305 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [54.8, 36.8] |  |
| +16.44 | +14.83 | 00:21:41.046 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [72.1, 44.2] |  |
| +16.44 | +14.83 | 00:21:41.046 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [72.1, 44.2] |  |
| +16.59 | +14.98 | 00:21:41.197 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [71.9, 45.6] |  |
| +17.48 | +15.88 | 00:21:42.094 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [64.4, 53.3] |  |
| +17.48 | +15.88 | 00:21:42.094 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [64.4, 53.3] |  |

---

### Episode 25: `3901736_p138_25424aa8`
- **Match**: `3901736` | **Competition**: Women's World Cup (2023)
- **Context**: Period 2, Pressing Team: **Denmark Women's** vs. Possession Team: **Australia Women's**
- **Initiation Action**: `Dribbled Past` by **Mille Gejl Jensen** at `00:18:37.594` (Turnover delay: 0.634s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=0.634s). Harmless transition (opp max progression x=56.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.25 | -0.88 | 00:18:36.714 | Denmark Women's | Denmark Women's | Pressure | - | [99.5, 18.0] |  |
| +0.00 | -0.63 | 00:18:36.960 | Australia Women's | Australia Women's | Ball Recovery | - | [17.2, 54.3] | 🔄 **TURNOVER** |
| +0.00 | -0.63 | 00:18:36.960 | Australia Women's | Australia Women's | Carry | - | [17.2, 54.3] |  |
| +0.63 | +0.00 | 00:18:37.594 | Denmark Women's | Australia Women's | Dribbled Past | **YES** | [109.2, 20.6] | ⭐ **CP INITIATION** |
| +0.63 | +0.00 | 00:18:37.594 | Australia Women's | Australia Women's | Dribble | - | [10.9, 59.5] |  |
| +0.63 | +0.00 | 00:18:37.594 | Australia Women's | Australia Women's | Carry | - | [10.9, 59.5] |  |
| +3.17 | +2.53 | 00:18:40.128 | Denmark Women's | Australia Women's | Pressure | **YES** | [105.2, 8.5] |  |
| +3.91 | +3.28 | 00:18:40.872 | Australia Women's | Australia Women's | Pass | - | [11.6, 71.8] |  |
| +5.19 | +4.55 | 00:18:42.146 | Australia Women's | Australia Women's | Ball Receipt* | - | [30.3, 75.4] |  |
| +5.19 | +4.55 | 00:18:42.146 | Australia Women's | Australia Women's | Carry | - | [30.3, 75.4] |  |
| +5.36 | +4.73 | 00:18:42.323 | Australia Women's | Australia Women's | Pass | - | [30.5, 72.6] |  |
| +6.31 | +5.68 | 00:18:43.274 | Australia Women's | Australia Women's | Ball Receipt* | - | [20.1, 67.1] |  |
| +6.31 | +5.68 | 00:18:43.274 | Australia Women's | Australia Women's | Carry | - | [20.1, 67.1] |  |
| +6.93 | +6.30 | 00:18:43.893 | Denmark Women's | Australia Women's | Pressure | - | [92.2, 17.5] |  |
| +7.09 | +6.45 | 00:18:44.046 | Australia Women's | Australia Women's | Pass | - | [23.4, 63.5] |  |
| +8.39 | +7.75 | 00:18:45.349 | Australia Women's | Australia Women's | Ball Receipt* | - | [33.5, 62.9] |  |
| +8.39 | +7.75 | 00:18:45.349 | Australia Women's | Australia Women's | Carry | - | [33.5, 62.9] |  |
| +10.10 | +9.47 | 00:18:47.063 | Australia Women's | Australia Women's | Pass | - | [41.3, 66.2] |  |
| +11.23 | +10.59 | 00:18:48.187 | Australia Women's | Australia Women's | Ball Receipt* | - | [53.9, 47.5] |  |
| +11.23 | +10.59 | 00:18:48.187 | Australia Women's | Australia Women's | Carry | - | [53.9, 47.5] |  |
| +11.45 | +10.82 | 00:18:48.410 | Australia Women's | Australia Women's | Miscontrol | - | [54.4, 51.0] |  |
| +11.87 | +11.24 | 00:18:48.833 | Australia Women's | Australia Women's | Pressure | - | [55.6, 53.8] |  |
| +12.36 | +11.72 | 00:18:49.317 | Denmark Women's | Australia Women's | Ball Recovery | - | [65.5, 27.2] |  |
| +12.36 | +11.72 | 00:18:49.317 | Denmark Women's | Australia Women's | Carry | - | [65.5, 27.2] |  |
| +12.40 | +11.77 | 00:18:49.365 | Denmark Women's | Australia Women's | Dispossessed | - | [65.5, 27.2] |  |
| +12.40 | +11.77 | 00:18:49.365 | Australia Women's | Australia Women's | Duel | **YES** | [54.6, 52.9] |  |
| +13.66 | +13.03 | 00:18:50.620 | Denmark Women's | Australia Women's | 50/50 | - | [67.4, 26.0] |  |
| +13.66 | +13.03 | 00:18:50.620 | Australia Women's | Australia Women's | 50/50 | **YES** | [52.7, 54.1] |  |
| +15.24 | +14.60 | 00:18:52.196 | Australia Women's | Australia Women's | Ball Recovery | - | [56.7, 63.5] |  |
| +15.24 | +14.60 | 00:18:52.196 | Australia Women's | Australia Women's | Carry | - | [56.7, 63.5] |  |
| +16.76 | +16.12 | 00:18:53.716 | Australia Women's | Australia Women's | Pass | - | [64.6, 66.6] |  |
| +19.45 | +18.82 | 00:18:56.415 | Australia Women's | Australia Women's | Ball Receipt* | - | [99.5, 25.7] |  |
| +19.45 | +18.82 | 00:18:56.415 | Australia Women's | Australia Women's | Carry | - | [99.5, 25.7] |  |

---

### Episode 26: `3837683_p191_31def767`
- **Match**: `3837683` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 2, Pressing Team: **Paris Saint-Germain** vs. Possession Team: **Paris Saint-Germain**
- **Initiation Action**: `Duel` by **Vitor Machado Ferreira** at `00:41:06.736` (Turnover delay: 0.614s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Paris Saint-Germain. Harmless transition (opp max progression x=48.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.34 | -2.95 | 00:41:03.784 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [61.9, 9.7] |  |
| -2.34 | -2.95 | 00:41:03.784 | Toulouse | Toulouse | Pass | **YES** | [59.8, 70.4] |  |
| -1.50 | -2.12 | 00:41:04.619 | Toulouse | Toulouse | Ball Receipt* | - | [62.9, 71.3] |  |
| -1.50 | -2.12 | 00:41:04.619 | Toulouse | Toulouse | Carry | - | [62.9, 71.3] |  |
| -0.94 | -1.55 | 00:41:05.186 | Toulouse | Toulouse | Pass | - | [65.5, 72.6] |  |
| -0.26 | -0.88 | 00:41:05.861 | Paris Saint-Germain | Toulouse | Pressure | **YES** | [54.8, 10.5] |  |
| -0.11 | -0.72 | 00:41:06.012 | Paris Saint-Germain | Toulouse | Pressure | **YES** | [51.5, 9.2] |  |
| +0.00 | -0.61 | 00:41:06.122 | Toulouse | Toulouse | Ball Receipt* | - | [68.1, 68.5] | 🔄 **TURNOVER** |
| +0.00 | -0.61 | 00:41:06.122 | Toulouse | Toulouse | Carry | - | [68.1, 68.5] |  |
| +0.61 | +0.00 | 00:41:06.736 | Toulouse | Toulouse | Dispossessed | - | [71.2, 70.2] |  |
| +0.61 | +0.00 | 00:41:06.736 | Paris Saint-Germain | Paris Saint-Germain | Duel | **YES** | [48.9, 9.9] | ⭐ **CP INITIATION** |
| +0.61 | +0.00 | 00:41:06.736 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [48.9, 9.9] |  |
| +4.48 | +3.87 | 00:41:10.602 | Toulouse | Paris Saint-Germain | Pressure | **YES** | [68.8, 61.7] |  |
| +4.72 | +4.11 | 00:41:10.842 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [45.4, 22.8] |  |
| +6.45 | +5.84 | 00:41:12.573 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [34.0, 38.5] |  |
| +6.45 | +5.84 | 00:41:12.573 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [34.0, 38.5] |  |
| +11.85 | +11.24 | 00:41:17.973 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [34.3, 39.0] |  |
| +13.78 | +13.16 | 00:41:19.901 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [33.0, 18.1] |  |
| +13.78 | +13.16 | 00:41:19.901 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [33.0, 18.1] |  |
| +14.88 | +14.27 | 00:41:21.002 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [31.9, 16.4] |  |
| +16.32 | +15.71 | 00:41:22.445 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [49.2, 22.3] |  |
| +16.32 | +15.71 | 00:41:22.445 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [49.2, 22.3] |  |
| +19.84 | +19.22 | 00:41:25.958 | Toulouse | Paris Saint-Germain | Pressure | - | [52.1, 73.1] |  |

---

### Episode 27: `3895232_p17_d662eb55`
- **Match**: `3895232` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Bayer Leverkusen** vs. Possession Team: **Bayern Munich**
- **Initiation Action**: `Pressure` by **Florian Wirtz** at `00:05:40.013` (Turnover delay: 0.325s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=0.325s). Harmless transition (opp max progression x=66.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.48 | -1.81 | 00:05:38.208 | Bayern Munich | Bayer Leverkusen | Pressure | - | [72.5, 57.0] |  |
| -1.28 | -1.61 | 00:05:38.404 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [46.5, 21.4] |  |
| -1.28 | -1.61 | 00:05:38.404 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [46.5, 21.4] |  |
| -0.81 | -1.14 | 00:05:38.876 | Bayer Leverkusen | Bayer Leverkusen | Miscontrol | - | [50.1, 24.3] |  |
| +0.00 | -0.32 | 00:05:39.688 | Bayern Munich | Bayern Munich | Ball Recovery | - | [64.3, 53.2] | 🔄 **TURNOVER** |
| +0.00 | -0.32 | 00:05:39.688 | Bayern Munich | Bayern Munich | Carry | - | [64.3, 53.2] |  |
| +0.32 | +0.00 | 00:05:40.013 | Bayer Leverkusen | Bayern Munich | Pressure | **YES** | [58.3, 27.1] | ⭐ **CP INITIATION** |
| +1.47 | +1.15 | 00:05:41.162 | Bayern Munich | Bayern Munich | Pass | - | [57.6, 56.2] |  |
| +2.31 | +1.98 | 00:05:41.997 | Bayern Munich | Bayern Munich | Ball Receipt* | - | [65.0, 62.4] |  |
| +2.31 | +1.98 | 00:05:41.997 | Bayern Munich | Bayern Munich | Carry | - | [65.0, 62.4] |  |
| +4.75 | +4.42 | 00:05:44.434 | Bayern Munich | Bayern Munich | Pass | - | [66.2, 74.1] |  |
| +6.13 | +5.81 | 00:05:45.822 | Bayern Munich | Bayern Munich | Ball Receipt* | - | [50.3, 75.7] |  |
| +6.13 | +5.81 | 00:05:45.822 | Bayern Munich | Bayern Munich | Carry | - | [50.3, 75.7] |  |
| +7.01 | +6.68 | 00:05:46.694 | Bayern Munich | Bayern Munich | Pass | - | [43.2, 74.1] |  |
| +9.76 | +9.44 | 00:05:49.451 | Bayern Munich | Bayern Munich | Ball Receipt* | - | [36.9, 50.4] |  |
| +9.76 | +9.44 | 00:05:49.451 | Bayern Munich | Bayern Munich | Carry | - | [36.9, 50.4] |  |
| +13.76 | +13.44 | 00:05:53.449 | Bayern Munich | Bayern Munich | Pass | - | [43.8, 41.1] |  |
| +16.65 | +16.33 | 00:05:56.341 | Bayern Munich | Bayern Munich | Ball Receipt* | - | [83.4, 47.0] |  |
| +16.65 | +16.33 | 00:05:56.341 | Bayer Leverkusen | Bayer Leverkusen | Ball Recovery | - | [15.6, 41.9] |  |
| +16.65 | +16.33 | 00:05:56.341 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [15.6, 41.9] |  |
| +17.31 | +16.98 | 00:05:56.994 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [15.4, 41.9] |  |
| +18.83 | +18.50 | 00:05:58.515 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [28.2, 52.1] |  |
| +18.83 | +18.50 | 00:05:58.515 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [28.2, 52.1] |  |

---

### Episode 28: `3802809_p9_2d601a0b`
- **Match**: `3802809` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 1, Pressing Team: **Paris Saint-Germain** vs. Possession Team: **Rennes**
- **Initiation Action**: `Pressure` by **Lionel Andrés Messi Cuccittini** at `00:03:40.230` (Turnover delay: 3.339s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.339s). Dangerous transition triggered by: Final third entry at dt=14.802s (initial x=11.4, max x=113.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.95 | -4.29 | 00:03:35.943 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [108.7, 7.8] |  |
| +0.00 | -3.34 | 00:03:36.891 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [107.9, 35.0] |  |
| +0.00 | -3.34 | 00:03:36.891 | Rennes | Paris Saint-Germain | Block | - | [13.3, 47.2] | 🔄 **TURNOVER** |
| +0.01 | -3.33 | 00:03:36.903 | Rennes | Paris Saint-Germain | Interception | - | [10.1, 44.4] |  |
| +2.33 | -1.01 | 00:03:39.224 | Rennes | Rennes | Ball Recovery | - | [11.4, 52.1] |  |
| +2.33 | -1.01 | 00:03:39.224 | Rennes | Rennes | Carry | - | [11.4, 52.1] |  |
| +3.34 | +0.00 | 00:03:40.230 | Paris Saint-Germain | Rennes | Pressure | **YES** | [108.5, 28.0] | ⭐ **CP INITIATION** |
| +4.00 | +0.67 | 00:03:40.895 | Rennes | Rennes | Pass | - | [9.7, 58.3] |  |
| +4.97 | +1.63 | 00:03:41.861 | Rennes | Rennes | Ball Receipt* | - | [22.3, 66.9] |  |
| +4.97 | +1.63 | 00:03:41.861 | Rennes | Rennes | Pass | - | [22.3, 66.9] |  |
| +6.07 | +2.73 | 00:03:42.960 | Rennes | Rennes | Ball Receipt* | - | [20.1, 56.0] |  |
| +6.07 | +2.73 | 00:03:42.960 | Rennes | Rennes | Carry | - | [20.1, 56.0] |  |
| +8.77 | +5.43 | 00:03:45.658 | Paris Saint-Germain | Rennes | Pressure | - | [88.2, 31.2] |  |
| +9.09 | +5.76 | 00:03:45.985 | Rennes | Rennes | Pass | - | [28.5, 46.6] |  |
| +11.19 | +7.85 | 00:03:48.078 | Rennes | Rennes | Ball Receipt* | - | [32.3, 21.3] |  |
| +11.19 | +7.85 | 00:03:48.078 | Rennes | Rennes | Carry | - | [32.3, 21.3] |  |
| +12.74 | +9.40 | 00:03:49.626 | Rennes | Rennes | Pass | - | [48.9, 12.4] |  |
| +13.74 | +10.41 | 00:03:50.635 | Rennes | Rennes | Ball Receipt* | - | [77.9, 15.4] |  |
| +13.74 | +10.41 | 00:03:50.635 | Paris Saint-Germain | Rennes | Interception | - | [45.2, 69.1] |  |
| +18.14 | +14.80 | 00:03:55.032 | Rennes | Rennes | Ball Recovery | - | [113.2, 8.9] |  |
| +18.14 | +14.80 | 00:03:55.032 | Rennes | Rennes | Carry | - | [113.2, 8.9] |  |
| +18.86 | +15.52 | 00:03:55.750 | Paris Saint-Germain | Rennes | Pressure | - | [7.3, 68.8] |  |
| +19.35 | +16.01 | 00:03:56.238 | Paris Saint-Germain | Rennes | Dribbled Past | - | [5.8, 70.1] |  |
| +19.35 | +16.01 | 00:03:56.238 | Rennes | Rennes | Dribble | - | [114.3, 10.0] |  |
| +20.45 | +17.12 | 00:03:57.345 | Rennes | Rennes | Pressure | - | [113.6, 14.3] |  |
| +20.63 | +17.30 | 00:03:57.525 | Paris Saint-Germain | Paris Saint-Germain | Ball Recovery | - | [3.1, 61.8] |  |
| +20.63 | +17.30 | 00:03:57.525 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [3.1, 61.8] |  |
| +20.88 | +17.54 | 00:03:57.767 | Paris Saint-Germain | Paris Saint-Germain | Dribble | - | [3.1, 61.8] |  |
| +20.88 | +17.54 | 00:03:57.767 | Rennes | Paris Saint-Germain | Duel | **YES** | [117.0, 18.3] |  |

---

### Episode 29: `3869519_p23_270160e6`
- **Match**: `3869519` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 1, Pressing Team: **Argentina** vs. Possession Team: **Argentina**
- **Initiation Action**: `Duel` by **Cristian Gabriel Romero** at `00:12:15.321` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.014s by Argentina. Harmless transition (opp max progression x=36.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.92 | -1.92 | 00:12:13.398 | Croatia | Croatia | Pass | - | [69.0, 12.6] |  |
| -0.70 | -0.70 | 00:12:14.622 | Croatia | Croatia | Ball Receipt* | - | [81.4, 19.9] |  |
| -0.70 | -0.70 | 00:12:14.622 | Croatia | Croatia | Carry | - | [81.4, 19.9] |  |
| -0.66 | -0.66 | 00:12:14.658 | Argentina | Croatia | Pressure | - | [35.8, 59.6] |  |
| +0.00 | +0.00 | 00:12:15.321 | Croatia | Croatia | Dispossessed | - | [83.3, 20.9] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:12:15.321 | Argentina | Argentina | Duel | **YES** | [36.8, 59.2] | ⭐ **CP INITIATION** |
| +1.01 | +1.01 | 00:12:16.335 | Argentina | Argentina | Ball Recovery | - | [41.1, 53.2] |  |
| +1.01 | +1.01 | 00:12:16.335 | Argentina | Argentina | Carry | - | [41.1, 53.2] |  |
| +1.95 | +1.95 | 00:12:17.270 | Argentina | Argentina | Pass | - | [41.1, 53.2] |  |
| +3.21 | +3.21 | 00:12:18.532 | Argentina | Argentina | Ball Receipt* | - | [48.7, 35.7] |  |
| +3.21 | +3.21 | 00:12:18.532 | Argentina | Argentina | Carry | - | [48.7, 35.7] |  |
| +5.31 | +5.31 | 00:12:20.627 | Croatia | Argentina | Pressure | - | [52.8, 40.4] |  |
| +5.87 | +5.87 | 00:12:21.195 | Croatia | Argentina | Foul Committed | - | [54.3, 46.6] |  |
| +5.87 | +5.87 | 00:12:21.195 | Argentina | Argentina | Foul Won | - | [65.8, 33.5] |  |
| +17.98 | +17.98 | 00:12:33.303 | Argentina | Argentina | Pass | - | [65.8, 33.5] |  |
| +19.40 | +19.40 | 00:12:34.723 | Argentina | Argentina | Ball Receipt* | - | [64.5, 45.9] |  |
| +19.92 | +19.92 | 00:12:35.237 | Argentina | Argentina | Pass | - | [64.1, 43.9] |  |

---

### Episode 30: `3895134_p65_b3e03700`
- **Match**: `3895134` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Hoffenheim** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Dribbled Past` by **Grischa Prömel** at `00:35:35.055` (Turnover delay: 0.347s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=0.347s). Dangerous transition triggered by: Shot at dt=11.057s; Final third entry at dt=11.057s (initial x=13.8, max x=114.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.31 | -2.66 | 00:35:32.396 | Bayer Leverkusen | Hoffenheim | Pressure | - | [15.6, 8.6] |  |
| -2.20 | -2.55 | 00:35:32.508 | Hoffenheim | Hoffenheim | Pass | - | [104.8, 70.1] |  |
| -0.92 | -1.27 | 00:35:33.787 | Bayer Leverkusen | Hoffenheim | Pressure | - | [14.9, 28.2] |  |
| -0.42 | -0.77 | 00:35:34.286 | Hoffenheim | Hoffenheim | Ball Receipt* | - | [105.2, 51.9] |  |
| -0.42 | -0.77 | 00:35:34.286 | Hoffenheim | Hoffenheim | Carry | - | [105.2, 51.9] |  |
| -0.36 | -0.71 | 00:35:34.348 | Hoffenheim | Hoffenheim | Miscontrol | - | [105.2, 51.9] |  |
| +0.00 | -0.35 | 00:35:34.708 | Bayer Leverkusen | Bayer Leverkusen | Ball Recovery | - | [13.8, 27.3] | 🔄 **TURNOVER** |
| +0.00 | -0.35 | 00:35:34.708 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [13.8, 27.3] |  |
| +0.35 | +0.00 | 00:35:35.055 | Hoffenheim | Bayer Leverkusen | Dribbled Past | **YES** | [106.2, 51.9] | ⭐ **CP INITIATION** |
| +0.35 | +0.00 | 00:35:35.055 | Bayer Leverkusen | Bayer Leverkusen | Dribble | - | [13.9, 28.2] |  |
| +0.35 | +0.00 | 00:35:35.055 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [13.9, 28.2] |  |
| +1.37 | +1.03 | 00:35:36.080 | Hoffenheim | Bayer Leverkusen | Pressure | **YES** | [104.9, 47.6] |  |
| +1.94 | +1.59 | 00:35:36.647 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [13.9, 33.1] |  |
| +6.23 | +5.89 | 00:35:40.941 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [71.3, 65.9] |  |
| +6.23 | +5.89 | 00:35:40.941 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [71.3, 65.9] |  |
| +8.00 | +7.65 | 00:35:42.706 | Hoffenheim | Bayer Leverkusen | Pressure | - | [19.5, 17.1] |  |
| +11.40 | +11.06 | 00:35:46.112 | Bayer Leverkusen | Bayer Leverkusen | Shot | - | [114.8, 51.5] |  |
| +11.92 | +11.58 | 00:35:46.632 | Hoffenheim | Bayer Leverkusen | Goal Keeper | - | [2.7, 35.7] |  |

---

### Episode 31: `3773526_p111_693f6d82`
- **Match**: `3773526` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Deportivo Alavés** vs. Possession Team: **Deportivo Alavés**
- **Initiation Action**: `Pass` by **Rubén Duarte Sánchez** at `00:27:39.000` (Turnover delay: 4.874s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.586s by Deportivo Alavés. Harmless transition (opp max progression x=23.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -4.87 | 00:27:34.126 | Barcelona | Barcelona | Pass | - | [102.9, 80.0] | 🔄 **TURNOVER** |
| +1.94 | -2.94 | 00:27:36.062 | Barcelona | Barcelona | Ball Receipt* | - | [88.4, 73.0] |  |
| +1.94 | -2.94 | 00:27:36.062 | Barcelona | Barcelona | Carry | - | [88.4, 73.0] |  |
| +4.32 | -0.55 | 00:27:38.447 | Barcelona | Barcelona | Pass | - | [87.5, 58.2] |  |
| +4.87 | +0.00 | 00:27:39.000 | Barcelona | Barcelona | Ball Receipt* | - | [108.2, 52.2] |  |
| +4.87 | +0.00 | 00:27:39.000 | Deportivo Alavés | Deportivo Alavés | Pass | **YES** | [23.1, 23.8] | ⭐ **CP INITIATION** |
| +5.46 | +0.59 | 00:27:39.586 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [29.8, 26.9] |  |
| +5.46 | +0.59 | 00:27:39.586 | Deportivo Alavés | Deportivo Alavés | Carry | - | [29.8, 26.9] |  |
| +6.13 | +1.26 | 00:27:40.259 | Barcelona | Deportivo Alavés | Pressure | **YES** | [88.4, 56.0] |  |
| +8.86 | +3.98 | 00:27:42.983 | Deportivo Alavés | Deportivo Alavés | Pass | - | [42.9, 19.5] |  |
| +9.66 | +4.79 | 00:27:43.789 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [44.4, 11.8] |  |
| +9.66 | +4.79 | 00:27:43.789 | Deportivo Alavés | Deportivo Alavés | Carry | - | [44.4, 11.8] |  |
| +10.47 | +5.59 | 00:27:44.594 | Deportivo Alavés | Deportivo Alavés | Pass | - | [44.4, 11.8] |  |
| +12.24 | +7.36 | 00:27:46.363 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [63.6, 33.4] |  |
| +12.24 | +7.36 | 00:27:46.363 | Deportivo Alavés | Deportivo Alavés | Pass | - | [63.6, 33.4] |  |
| +14.31 | +9.43 | 00:27:48.433 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [78.4, 5.3] |  |
| +14.31 | +9.43 | 00:27:48.433 | Deportivo Alavés | Deportivo Alavés | Pass | - | [78.7, 8.7] |  |
| +17.53 | +12.65 | 00:27:51.654 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [105.7, 55.1] |  |
| +17.53 | +12.65 | 00:27:51.654 | Deportivo Alavés | Deportivo Alavés | Carry | - | [105.7, 55.1] |  |
| +19.09 | +14.21 | 00:27:53.214 | Deportivo Alavés | Deportivo Alavés | Pass | - | [109.7, 58.2] |  |
| +23.20 | +18.33 | 00:27:57.325 | Deportivo Alavés | Deportivo Alavés | Ball Receipt* | - | [106.9, 17.0] |  |

---

### Episode 32: `3773661_p85_41deac2d`
- **Match**: `3773661` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Getafe** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Djené Dakonam Ortega** at `00:14:48.849` (Turnover delay: 1.677s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.677s). Harmless transition (opp max progression x=57.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.58 | -4.25 | 00:14:44.596 | Getafe | Getafe | Ball Receipt* | - | [111.5, 38.3] |  |
| -2.58 | -4.25 | 00:14:44.596 | Barcelona | Getafe | Clearance | - | [9.3, 36.5] |  |
| -1.42 | -3.10 | 00:14:45.748 | Barcelona | Getafe | Pressure | - | [14.2, 27.1] |  |
| -1.19 | -2.87 | 00:14:45.980 | Getafe | Getafe | Ball Recovery | - | [102.6, 53.4] |  |
| -1.19 | -2.87 | 00:14:45.980 | Getafe | Getafe | Carry | - | [102.6, 53.4] |  |
| +0.00 | -1.68 | 00:14:47.172 | Getafe | Getafe | Dribble | - | [99.5, 54.2] |  |
| +0.00 | -1.68 | 00:14:47.172 | Barcelona | Barcelona | Duel | **YES** | [20.6, 25.9] | 🔄 **TURNOVER** |
| +0.00 | -1.68 | 00:14:47.172 | Barcelona | Barcelona | Carry | - | [20.6, 25.9] |  |
| +1.68 | +0.00 | 00:14:48.849 | Getafe | Barcelona | Pressure | **YES** | [87.9, 53.4] | ⭐ **CP INITIATION** |
| +3.02 | +1.34 | 00:14:50.190 | Barcelona | Barcelona | Dispossessed | - | [33.3, 23.5] |  |
| +3.02 | +1.34 | 00:14:50.190 | Getafe | Barcelona | Duel | **YES** | [86.8, 56.6] |  |
| +3.84 | +2.16 | 00:14:51.009 | Barcelona | Barcelona | Ball Recovery | - | [30.1, 20.6] |  |
| +3.84 | +2.16 | 00:14:51.009 | Barcelona | Barcelona | Carry | - | [30.1, 20.6] |  |
| +3.85 | +2.17 | 00:14:51.024 | Getafe | Barcelona | Pressure | **YES** | [91.6, 59.9] |  |
| +4.73 | +3.05 | 00:14:51.899 | Barcelona | Barcelona | Pass | - | [27.5, 21.5] |  |
| +5.47 | +3.79 | 00:14:52.640 | Barcelona | Barcelona | Ball Receipt* | - | [19.6, 22.6] |  |
| +5.47 | +3.79 | 00:14:52.640 | Barcelona | Barcelona | Carry | - | [19.6, 22.6] |  |
| +5.60 | +3.92 | 00:14:52.769 | Barcelona | Barcelona | Pass | - | [19.6, 22.3] |  |
| +7.08 | +5.40 | 00:14:54.251 | Barcelona | Barcelona | Ball Receipt* | - | [30.2, 6.8] |  |
| +7.08 | +5.40 | 00:14:54.251 | Barcelona | Barcelona | Carry | - | [30.2, 6.8] |  |
| +8.50 | +6.82 | 00:14:55.670 | Barcelona | Barcelona | Pass | - | [34.6, 8.9] |  |
| +11.91 | +10.24 | 00:14:59.084 | Barcelona | Barcelona | Ball Receipt* | - | [44.2, 69.5] |  |
| +11.91 | +10.24 | 00:14:59.084 | Barcelona | Barcelona | Pass | - | [44.8, 70.4] |  |
| +13.41 | +11.74 | 00:15:00.586 | Barcelona | Barcelona | Ball Receipt* | - | [48.4, 54.3] |  |
| +13.41 | +11.74 | 00:15:00.586 | Barcelona | Barcelona | Carry | - | [48.4, 54.3] |  |
| +15.19 | +13.51 | 00:15:02.364 | Barcelona | Barcelona | Pass | - | [57.0, 59.8] |  |
| +17.19 | +15.52 | 00:15:04.365 | Barcelona | Barcelona | Ball Receipt* | - | [83.3, 75.0] |  |
| +17.19 | +15.52 | 00:15:04.365 | Barcelona | Barcelona | Carry | - | [83.3, 75.0] |  |
| +19.36 | +17.68 | 00:15:06.529 | Barcelona | Barcelona | Pass | - | [93.2, 70.9] |  |
| +21.14 | +19.46 | 00:15:08.312 | Getafe | Barcelona | Pressure | - | [8.0, 24.1] |  |
| +21.41 | +19.73 | 00:15:08.579 | Barcelona | Barcelona | Ball Receipt* | - | [112.4, 59.2] |  |
| +21.41 | +19.73 | 00:15:08.579 | Barcelona | Barcelona | Carry | - | [112.4, 59.2] |  |

---

### Episode 33: `3943043_p15_7708c8e5`
- **Match**: `3943043` | **Competition**: UEFA Euro (2024)
- **Context**: Period 1, Pressing Team: **England** vs. Possession Team: **Spain**
- **Initiation Action**: `Duel` by **Kobbie Mainoo** at `00:07:51.585` (Turnover delay: 3.421s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.421s). Dangerous transition triggered by: Final third entry at dt=8.965s (initial x=63.4, max x=92.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.08 | -4.50 | 00:07:47.080 | England | England | Ball Receipt* | - | [45.2, 69.3] |  |
| -1.08 | -4.50 | 00:07:47.080 | Spain | England | Duel | - | [74.9, 10.8] |  |
| -1.08 | -4.50 | 00:07:47.080 | England | England | Pass | - | [45.2, 69.3] |  |
| +0.00 | -3.42 | 00:07:48.164 | England | England | Ball Receipt* | - | [50.1, 65.8] |  |
| +0.00 | -3.42 | 00:07:48.164 | Spain | Spain | Pass | - | [63.4, 14.9] | 🔄 **TURNOVER** |
| +1.11 | -2.31 | 00:07:49.277 | Spain | Spain | Ball Receipt* | - | [77.7, 12.6] |  |
| +1.11 | -2.31 | 00:07:49.277 | Spain | Spain | Pass | - | [77.7, 12.6] |  |
| +2.18 | -1.25 | 00:07:50.339 | Spain | Spain | Ball Receipt* | - | [70.6, 20.0] |  |
| +2.23 | -1.19 | 00:07:50.395 | Spain | Spain | Pass | - | [69.8, 21.6] |  |
| +3.42 | +0.00 | 00:07:51.585 | Spain | Spain | Ball Receipt* | - | [76.3, 6.5] |  |
| +3.42 | +0.00 | 00:07:51.585 | England | Spain | Duel | **YES** | [44.2, 73.9] | ⭐ **CP INITIATION** |
| +3.42 | +0.00 | 00:07:51.585 | Spain | Spain | Pass | - | [75.9, 6.2] |  |
| +4.29 | +0.87 | 00:07:52.458 | Spain | Spain | Ball Receipt* | - | [77.1, 15.7] |  |
| +4.29 | +0.87 | 00:07:52.458 | Spain | Spain | Carry | - | [77.1, 15.7] |  |
| +4.67 | +1.25 | 00:07:52.830 | England | Spain | Pressure | **YES** | [42.8, 63.0] |  |
| +5.83 | +2.41 | 00:07:53.990 | Spain | Spain | Pass | - | [70.7, 19.6] |  |
| +7.28 | +3.86 | 00:07:55.446 | Spain | Spain | Ball Receipt* | - | [61.9, 36.3] |  |
| +7.28 | +3.86 | 00:07:55.446 | Spain | Spain | Carry | - | [61.9, 36.3] |  |
| +9.32 | +5.90 | 00:07:57.489 | Spain | Spain | Pass | - | [63.5, 41.1] |  |
| +10.44 | +7.02 | 00:07:58.604 | Spain | Spain | Ball Receipt* | - | [63.9, 24.3] |  |
| +10.44 | +7.02 | 00:07:58.604 | Spain | Spain | Carry | - | [63.9, 24.3] |  |
| +11.36 | +7.94 | 00:07:59.526 | Spain | Spain | Pass | - | [63.4, 24.3] |  |
| +12.39 | +8.97 | 00:08:00.550 | Spain | Spain | Ball Receipt* | - | [84.4, 25.2] |  |
| +12.39 | +8.97 | 00:08:00.550 | Spain | Spain | Pass | - | [84.4, 25.2] |  |
| +14.04 | +10.62 | 00:08:02.208 | Spain | Spain | Ball Receipt* | - | [92.4, 28.3] |  |
| +14.04 | +10.62 | 00:08:02.208 | England | England | Pass | - | [20.5, 54.6] |  |
| +15.01 | +11.59 | 00:08:03.175 | England | England | Ball Receipt* | - | [31.5, 58.2] |  |
| +15.01 | +11.59 | 00:08:03.175 | England | England | Carry | - | [31.5, 58.2] |  |
| +15.48 | +12.06 | 00:08:03.645 | Spain | England | Pressure | **YES** | [83.0, 23.2] |  |
| +15.65 | +12.23 | 00:08:03.817 | England | England | Pass | - | [34.8, 56.4] |  |
| +16.24 | +12.81 | 00:08:04.399 | England | England | Ball Receipt* | - | [43.4, 56.9] |  |
| +16.24 | +12.81 | 00:08:04.399 | England | England | Pass | - | [42.8, 56.9] |  |
| +18.31 | +14.89 | 00:08:06.472 | England | England | Ball Receipt* | - | [40.8, 69.9] |  |
| +22.28 | +18.86 | 00:08:10.441 | Spain | Spain | Pass | - | [67.8, 0.1] |  |

---

### Episode 34: `3788746_p90_26467725`
- **Match**: `3788746` | **Competition**: UEFA Euro (2020)
- **Context**: Period 2, Pressing Team: **Netherlands** vs. Possession Team: **Netherlands**
- **Initiation Action**: `Pressure` by **Memphis Depay** at `00:02:52.864` (Turnover delay: 1.949s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.599s by Netherlands. Harmless transition (opp max progression x=27.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.95 | 00:02:50.915 | Ukraine | Netherlands | Pass | - | [14.6, 11.4] | 🔄 **TURNOVER** |
| +1.62 | -0.33 | 00:02:52.539 | Ukraine | Netherlands | Ball Receipt* | - | [2.3, 27.4] |  |
| +1.62 | -0.33 | 00:02:52.539 | Ukraine | Netherlands | Carry | - | [2.3, 27.4] |  |
| +1.95 | +0.00 | 00:02:52.864 | Netherlands | Netherlands | Pressure | **YES** | [111.7, 50.9] | ⭐ **CP INITIATION** |
| +2.55 | +0.60 | 00:02:53.463 | Ukraine | Netherlands | Pass | - | [2.2, 24.9] |  |
| +5.17 | +3.22 | 00:02:56.089 | Netherlands | Netherlands | Ball Recovery | - | [81.8, 76.7] |  |
| +5.17 | +3.22 | 00:02:56.089 | Netherlands | Netherlands | Carry | - | [81.8, 76.7] |  |
| +6.54 | +4.59 | 00:02:57.459 | Netherlands | Netherlands | Pass | - | [82.9, 76.7] |  |
| +7.74 | +5.79 | 00:02:58.652 | Netherlands | Netherlands | Ball Receipt* | - | [99.5, 77.5] |  |
| +7.74 | +5.79 | 00:02:58.652 | Netherlands | Netherlands | Carry | - | [99.5, 77.5] |  |
| +10.02 | +8.07 | 00:03:00.937 | Netherlands | Netherlands | Pass | - | [101.9, 77.5] |  |
| +11.68 | +9.73 | 00:03:02.599 | Netherlands | Netherlands | Ball Receipt* | - | [83.4, 59.7] |  |
| +11.68 | +9.73 | 00:03:02.599 | Netherlands | Netherlands | Carry | - | [83.4, 59.7] |  |
| +13.45 | +11.50 | 00:03:04.362 | Netherlands | Netherlands | Pass | - | [78.6, 54.1] |  |
| +15.57 | +13.62 | 00:03:06.488 | Netherlands | Netherlands | Ball Receipt* | - | [74.0, 35.3] |  |
| +15.57 | +13.62 | 00:03:06.488 | Netherlands | Netherlands | Carry | - | [74.0, 35.3] |  |
| +19.04 | +17.09 | 00:03:09.958 | Netherlands | Netherlands | Pass | - | [82.3, 37.5] |  |
| +20.40 | +18.45 | 00:03:11.316 | Netherlands | Netherlands | Ball Receipt* | - | [80.0, 53.0] |  |
| +20.40 | +18.45 | 00:03:11.316 | Netherlands | Netherlands | Carry | - | [80.0, 53.0] |  |
| +21.79 | +19.84 | 00:03:12.709 | Netherlands | Netherlands | Pass | - | [78.1, 51.9] |  |

---

### Episode 35: `3906390_p66_48d40627`
- **Match**: `3906390` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **England Women's** vs. Possession Team: **Spain Women's**
- **Initiation Action**: `Pressure` by **Rachel Daly** at `00:28:21.862` (Turnover delay: 3.404s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.404s). Dangerous transition triggered by: Shot at dt=7.98s; Final third entry at dt=3.003s (initial x=56.6, max x=107.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.14 | -3.54 | 00:28:18.320 | England Women's | England Women's | Pass | - | [62.3, 38.4] |  |
| +0.00 | -3.40 | 00:28:18.458 | England Women's | England Women's | Ball Receipt* | - | [64.6, 28.7] |  |
| +0.00 | -3.40 | 00:28:18.458 | Spain Women's | England Women's | Block | - | [55.1, 44.2] | 🔄 **TURNOVER** |
| +1.52 | -1.89 | 00:28:19.975 | Spain Women's | Spain Women's | Ball Recovery | - | [56.6, 49.8] |  |
| +1.52 | -1.89 | 00:28:19.975 | Spain Women's | Spain Women's | Carry | - | [56.6, 49.8] |  |
| +3.40 | +0.00 | 00:28:21.862 | England Women's | Spain Women's | Pressure | **YES** | [50.3, 26.3] | ⭐ **CP INITIATION** |
| +3.76 | +0.36 | 00:28:22.222 | Spain Women's | Spain Women's | Pass | - | [68.8, 52.5] |  |
| +6.41 | +3.00 | 00:28:24.865 | Spain Women's | Spain Women's | Ball Receipt* | - | [82.9, 12.2] |  |
| +6.41 | +3.00 | 00:28:24.865 | Spain Women's | Spain Women's | Carry | - | [82.9, 12.2] |  |
| +9.25 | +5.85 | 00:28:27.712 | Spain Women's | Spain Women's | Pass | - | [92.9, 22.7] |  |
| +10.37 | +6.96 | 00:28:28.825 | Spain Women's | Spain Women's | Ball Receipt* | - | [107.1, 24.5] |  |
| +10.48 | +7.07 | 00:28:28.937 | England Women's | Spain Women's | Pressure | - | [22.2, 56.9] |  |
| +11.38 | +7.98 | 00:28:29.842 | Spain Women's | Spain Women's | Shot | - | [107.1, 24.5] |  |
| +12.30 | +8.89 | 00:28:30.755 | England Women's | Spain Women's | Goal Keeper | - | [2.1, 43.7] |  |

---

### Episode 36: `3869354_p105_1d7044d4`
- **Match**: `3869354` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **France** vs. Possession Team: **France**
- **Initiation Action**: `Duel` by **Adrien Rabiot** at `00:10:43.473` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=2.525s by France. Harmless transition (opp max progression x=33.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.16 | -2.16 | 00:10:41.314 | England | England | Pass | - | [95.0, 23.3] |  |
| -1.17 | -1.17 | 00:10:42.298 | England | England | Ball Receipt* | - | [85.4, 27.1] |  |
| -1.17 | -1.17 | 00:10:42.298 | England | England | Carry | - | [85.4, 27.1] |  |
| -0.51 | -0.51 | 00:10:42.961 | France | England | Pressure | - | [31.5, 45.7] |  |
| +0.00 | +0.00 | 00:10:43.473 | England | England | Dispossessed | - | [87.1, 35.2] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:10:43.473 | France | France | Duel | **YES** | [33.0, 44.9] | ⭐ **CP INITIATION** |
| +2.53 | +2.53 | 00:10:45.998 | France | France | Ball Recovery | - | [47.3, 11.3] |  |
| +2.53 | +2.53 | 00:10:45.998 | France | France | Carry | - | [47.3, 11.3] |  |
| +7.16 | +7.16 | 00:10:50.635 | England | France | Pressure | - | [35.1, 75.9] |  |
| +10.85 | +10.85 | 00:10:54.323 | England | France | Dribbled Past | - | [6.5, 64.6] |  |
| +10.85 | +10.85 | 00:10:54.323 | France | France | Dribble | - | [113.6, 15.5] |  |
| +10.85 | +10.85 | 00:10:54.323 | France | France | Carry | - | [113.6, 15.5] |  |
| +11.25 | +11.25 | 00:10:54.722 | France | France | Pass | - | [115.6, 19.0] |  |
| +12.03 | +12.03 | 00:10:55.506 | France | France | Ball Receipt* | - | [108.7, 35.9] |  |
| +12.03 | +12.03 | 00:10:55.506 | France | France | Carry | - | [108.7, 35.9] |  |
| +14.95 | +14.95 | 00:10:58.427 | France | France | Pass | - | [115.4, 56.6] |  |
| +16.27 | +16.27 | 00:10:59.740 | France | France | Ball Receipt* | - | [102.9, 55.8] |  |
| +16.27 | +16.27 | 00:10:59.740 | France | France | Carry | - | [102.9, 55.8] |  |
| +16.49 | +16.49 | 00:10:59.959 | France | France | Pass | - | [102.9, 55.8] |  |
| +17.37 | +17.37 | 00:11:00.847 | England | France | Ball Recovery | - | [15.4, 40.0] |  |
| +17.37 | +17.37 | 00:11:00.847 | England | France | Carry | - | [15.4, 40.0] |  |
| +19.30 | +19.30 | 00:11:02.770 | England | France | Pass | - | [22.7, 37.2] |  |

---

### Episode 37: `3930166_p136_bd5a7dea`
- **Match**: `3930166` | **Competition**: UEFA Euro (2024)
- **Context**: Period 2, Pressing Team: **Portugal** vs. Possession Team: **Czech Republic**
- **Initiation Action**: `Pressure` by **Diogo José Teixeira da Silva** at `00:39:14.805` (Turnover delay: 2.034s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.034s). Harmless transition (opp max progression x=23.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.19 | -4.22 | 00:39:10.580 | Czech Republic | Portugal | Pressure | - | [25.6, 61.4] |  |
| -1.82 | -3.85 | 00:39:10.954 | Portugal | Portugal | Ball Receipt* | - | [94.5, 14.5] |  |
| -1.82 | -3.85 | 00:39:10.954 | Portugal | Portugal | Carry | - | [94.5, 14.5] |  |
| -1.51 | -3.54 | 00:39:11.266 | Czech Republic | Portugal | Dribbled Past | - | [23.5, 64.6] |  |
| -1.51 | -3.54 | 00:39:11.266 | Portugal | Portugal | Dribble | - | [96.6, 15.5] |  |
| -1.51 | -3.54 | 00:39:11.266 | Portugal | Portugal | Carry | - | [96.6, 15.5] |  |
| -0.61 | -2.65 | 00:39:12.159 | Czech Republic | Portugal | Pressure | - | [18.7, 56.7] |  |
| +0.00 | -2.03 | 00:39:12.771 | Portugal | Portugal | Dribble | - | [106.7, 24.0] |  |
| +0.00 | -2.03 | 00:39:12.771 | Czech Republic | Czech Republic | Duel | **YES** | [13.4, 56.1] | 🔄 **TURNOVER** |
| +2.03 | +0.00 | 00:39:14.805 | Portugal | Czech Republic | Pressure | **YES** | [107.3, 20.1] | ⭐ **CP INITIATION** |
| +2.11 | +0.07 | 00:39:14.876 | Czech Republic | Czech Republic | Ball Recovery | - | [11.4, 64.0] |  |
| +2.11 | +0.07 | 00:39:14.876 | Czech Republic | Czech Republic | Carry | - | [11.4, 64.0] |  |
| +3.21 | +1.18 | 00:39:15.981 | Czech Republic | Czech Republic | Pass | - | [8.8, 68.5] |  |
| +4.63 | +2.59 | 00:39:17.397 | Czech Republic | Czech Republic | Ball Receipt* | - | [23.3, 76.5] |  |
| +4.63 | +2.59 | 00:39:17.397 | Czech Republic | Czech Republic | Carry | - | [23.3, 76.5] |  |
| +4.83 | +2.79 | 00:39:17.597 | Portugal | Czech Republic | Pressure | **YES** | [102.8, 5.7] |  |
| +5.64 | +3.60 | 00:39:18.408 | Portugal | Czech Republic | Foul Committed | - | [97.6, 3.6] |  |
| +5.64 | +3.60 | 00:39:18.408 | Czech Republic | Czech Republic | Foul Won | - | [22.5, 76.5] |  |

---

### Episode 38: `3895167_p84_73db9a0d`
- **Match**: `3895167` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Bayer Leverkusen** vs. Possession Team: **VfB Stuttgart**
- **Initiation Action**: `Pressure` by **Victor Okoh Boniface** at `00:45:43.098` (Turnover delay: 2.314s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.314s). Harmless transition (opp max progression x=62.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.11 | -2.42 | 00:45:40.674 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [52.2, 5.4] |  |
| -0.03 | -2.34 | 00:45:40.754 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [51.4, 5.2] |  |
| -0.03 | -2.34 | 00:45:40.754 | VfB Stuttgart | Bayer Leverkusen | Duel | - | [68.7, 74.9] |  |
| +0.00 | -2.31 | 00:45:40.784 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [63.5, 16.0] |  |
| +0.00 | -2.31 | 00:45:40.784 | VfB Stuttgart | Bayer Leverkusen | Block | - | [66.8, 74.9] | 🔄 **TURNOVER** |
| +2.21 | -0.11 | 00:45:42.990 | VfB Stuttgart | VfB Stuttgart | Ball Recovery | - | [48.6, 75.3] |  |
| +2.21 | -0.11 | 00:45:42.990 | VfB Stuttgart | VfB Stuttgart | Carry | - | [48.6, 75.3] |  |
| +2.31 | +0.00 | 00:45:43.098 | Bayer Leverkusen | VfB Stuttgart | Pressure | **YES** | [70.8, 6.5] | ⭐ **CP INITIATION** |
| +2.96 | +0.65 | 00:45:43.747 | VfB Stuttgart | VfB Stuttgart | Pass | - | [43.8, 77.4] |  |
| +6.53 | +4.22 | 00:45:47.317 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [10.9, 58.7] |  |
| +6.53 | +4.22 | 00:45:47.317 | VfB Stuttgart | VfB Stuttgart | Carry | - | [10.9, 58.7] |  |
| +7.50 | +5.19 | 00:45:48.284 | VfB Stuttgart | VfB Stuttgart | Pass | - | [10.9, 58.7] |  |
| +9.14 | +6.82 | 00:45:49.921 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [34.1, 63.1] |  |
| +9.14 | +6.82 | 00:45:49.921 | VfB Stuttgart | VfB Stuttgart | Carry | - | [34.1, 63.1] |  |
| +9.20 | +6.89 | 00:45:49.984 | VfB Stuttgart | VfB Stuttgart | Pass | - | [34.1, 63.1] |  |
| +10.20 | +7.89 | 00:45:50.986 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [26.9, 76.3] |  |
| +10.20 | +7.89 | 00:45:50.986 | VfB Stuttgart | VfB Stuttgart | Carry | - | [26.9, 76.3] |  |
| +11.16 | +8.85 | 00:45:51.943 | VfB Stuttgart | VfB Stuttgart | Pass | - | [25.2, 75.1] |  |
| +12.93 | +10.62 | 00:45:53.719 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [4.4, 62.4] |  |
| +12.93 | +10.62 | 00:45:53.719 | VfB Stuttgart | VfB Stuttgart | Carry | - | [4.4, 62.4] |  |
| +13.13 | +10.82 | 00:45:53.919 | VfB Stuttgart | VfB Stuttgart | Pass | - | [5.4, 62.4] |  |
| +17.09 | +14.78 | 00:45:57.877 | VfB Stuttgart | VfB Stuttgart | Ball Receipt* | - | [62.8, 44.5] |  |
| +17.09 | +14.78 | 00:45:57.877 | Bayer Leverkusen | VfB Stuttgart | Pass | - | [58.0, 23.8] |  |
| +19.92 | +17.60 | 00:46:00.701 | Bayer Leverkusen | VfB Stuttgart | Ball Receipt* | - | [90.4, 27.6] |  |
| +19.92 | +17.60 | 00:46:00.701 | VfB Stuttgart | VfB Stuttgart | Ball Recovery | - | [30.0, 45.9] |  |
| +19.92 | +17.60 | 00:46:00.701 | VfB Stuttgart | VfB Stuttgart | Carry | - | [30.0, 45.9] |  |
| +21.90 | +19.59 | 00:46:02.683 | VfB Stuttgart | VfB Stuttgart | Pass | - | [22.0, 49.5] |  |

---

### Episode 39: `3902968_p97_20fdd315`
- **Match**: `3902968` | **Competition**: Women's World Cup (2023)
- **Context**: Period 2, Pressing Team: **Australia Women's** vs. Possession Team: **Australia Women's**
- **Initiation Action**: `Block` by **Emily Louise van Egmond** at `00:01:45.407` (Turnover delay: 0.466s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.069s by Australia Women's. Harmless transition (opp max progression x=94.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -0.47 | 00:01:44.941 | Australia Women's | Australia Women's | Shot | - | [94.6, 29.3] | 🔄 **TURNOVER** |
| +0.47 | +0.00 | 00:01:45.407 | Australia Women's | Australia Women's | Block | **YES** | [103.1, 32.9] | ⭐ **CP INITIATION** |
| +0.53 | +0.07 | 00:01:45.476 | France Women's | Australia Women's | Goal Keeper | - | [1.6, 40.1] |  |
| +4.00 | +3.53 | 00:01:48.941 | Australia Women's | Australia Women's | Pass | - | [82.6, 40.0] |  |
| +5.73 | +5.27 | 00:01:50.674 | Australia Women's | Australia Women's | Ball Receipt* | - | [100.0, 64.9] |  |
| +5.73 | +5.27 | 00:01:50.674 | Australia Women's | Australia Women's | Carry | - | [100.0, 64.9] |  |
| +7.14 | +6.67 | 00:01:52.077 | Australia Women's | Australia Women's | Pass | - | [104.9, 66.3] |  |
| +8.36 | +7.90 | 00:01:53.306 | Australia Women's | Australia Women's | Ball Receipt* | - | [111.1, 40.2] |  |
| +8.36 | +7.90 | 00:01:53.306 | France Women's | Australia Women's | Clearance | - | [9.0, 37.9] |  |
| +10.82 | +10.35 | 00:01:55.758 | Australia Women's | Australia Women's | Ball Recovery | - | [94.1, 50.2] |  |
| +10.82 | +10.35 | 00:01:55.758 | Australia Women's | Australia Women's | Carry | - | [94.1, 50.2] |  |
| +11.57 | +11.11 | 00:01:56.512 | France Women's | Australia Women's | Pressure | - | [25.8, 30.2] |  |
| +11.88 | +11.41 | 00:01:56.818 | Australia Women's | Australia Women's | Pass | - | [91.8, 52.2] |  |
| +15.19 | +14.73 | 00:02:00.134 | Australia Women's | Australia Women's | Ball Receipt* | - | [82.2, 77.9] |  |
| +15.19 | +14.73 | 00:02:00.134 | Australia Women's | Australia Women's | Carry | - | [82.2, 77.9] |  |
| +17.29 | +16.82 | 00:02:02.229 | France Women's | Australia Women's | Pressure | - | [50.3, 2.6] |  |

---

### Episode 40: `3837954_p100_dc48c3ba`
- **Match**: `3837954` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 2, Pressing Team: **Angers** vs. Possession Team: **Angers**
- **Initiation Action**: `Interception` by **Adrien Hunou** at `00:19:54.689` (Turnover delay: 5.569s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Angers. Harmless transition (opp max progression x=26.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.81 | -7.38 | 00:19:47.305 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [63.2, 9.5] |  |
| -1.81 | -7.38 | 00:19:47.305 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [63.2, 9.5] |  |
| -1.72 | -7.29 | 00:19:47.396 | Angers | Paris Saint-Germain | Pressure | **YES** | [55.1, 69.8] |  |
| -0.75 | -6.32 | 00:19:48.371 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [68.9, 8.2] |  |
| +0.00 | -5.57 | 00:19:49.120 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [76.0, 16.6] | 🔄 **TURNOVER** |
| +0.00 | -5.57 | 00:19:49.120 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [76.0, 16.6] |  |
| +0.36 | -5.21 | 00:19:49.480 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [76.0, 16.6] |  |
| +1.12 | -4.45 | 00:19:50.243 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [75.5, 28.5] |  |
| +1.12 | -4.45 | 00:19:50.243 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [75.5, 28.5] |  |
| +2.03 | -3.54 | 00:19:51.154 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [76.3, 28.7] |  |
| +2.84 | -2.73 | 00:19:51.958 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [81.3, 45.2] |  |
| +2.84 | -2.73 | 00:19:51.958 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [81.3, 45.2] |  |
| +4.80 | -0.77 | 00:19:53.923 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [81.3, 33.5] |  |
| +5.57 | +0.00 | 00:19:54.689 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [95.0, 30.8] |  |
| +5.57 | +0.00 | 00:19:54.689 | Angers | Angers | Interception | **YES** | [26.9, 48.7] | ⭐ **CP INITIATION** |
| +5.57 | +0.00 | 00:19:54.689 | Angers | Angers | Carry | - | [26.9, 48.7] |  |
| +6.72 | +1.15 | 00:19:55.844 | Angers | Angers | Pass | - | [26.0, 39.5] |  |
| +7.93 | +2.36 | 00:19:57.050 | Paris Saint-Germain | Angers | Pressure | **YES** | [91.5, 61.2] |  |
| +8.08 | +2.51 | 00:19:57.204 | Angers | Angers | Ball Receipt* | - | [24.2, 15.5] |  |
| +8.08 | +2.51 | 00:19:57.204 | Angers | Angers | Carry | - | [24.2, 15.5] |  |
| +11.05 | +5.48 | 00:20:00.173 | Angers | Angers | Pass | - | [21.2, 9.5] |  |
| +12.35 | +6.78 | 00:20:01.473 | Angers | Angers | Ball Receipt* | - | [14.8, 15.0] |  |
| +12.35 | +6.78 | 00:20:01.473 | Angers | Angers | Carry | - | [14.8, 15.0] |  |
| +12.50 | +6.93 | 00:20:01.615 | Paris Saint-Germain | Angers | Pressure | - | [102.5, 65.6] |  |
| +12.98 | +7.41 | 00:20:02.097 | Angers | Angers | Pass | - | [14.1, 14.8] |  |
| +13.52 | +7.95 | 00:20:02.643 | Paris Saint-Germain | Angers | Pressure | - | [97.5, 61.9] |  |
| +13.83 | +8.26 | 00:20:02.950 | Angers | Angers | Ball Receipt* | - | [21.5, 18.2] |  |
| +13.83 | +8.26 | 00:20:02.950 | Angers | Angers | Pass | - | [20.8, 18.3] |  |
| +16.12 | +10.55 | 00:20:05.243 | Angers | Angers | Ball Receipt* | - | [29.7, 3.1] |  |
| +16.12 | +10.55 | 00:20:05.243 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [86.3, 64.4] |  |
| +16.98 | +11.41 | 00:20:06.098 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [99.7, 56.0] |  |
| +16.98 | +11.41 | 00:20:06.098 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [99.7, 56.0] |  |
| +17.69 | +12.12 | 00:20:06.807 | Angers | Paris Saint-Germain | Pressure | **YES** | [17.8, 24.4] |  |
| +17.92 | +12.36 | 00:20:07.044 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [101.4, 53.1] |  |
| +18.54 | +12.97 | 00:20:07.661 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [102.1, 44.1] |  |
| +18.54 | +12.97 | 00:20:07.661 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [102.1, 44.1] |  |
| +18.91 | +13.34 | 00:20:08.029 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [102.1, 44.1] |  |
| +19.27 | +13.70 | 00:20:08.392 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [107.1, 46.1] |  |
| +19.27 | +13.70 | 00:20:08.392 | Angers | Angers | Interception | **YES** | [15.1, 34.3] |  |
| +19.27 | +13.70 | 00:20:08.392 | Angers | Angers | Carry | - | [15.1, 34.3] |  |
| +20.27 | +14.70 | 00:20:09.388 | Paris Saint-Germain | Angers | Pressure | **YES** | [104.1, 42.4] |  |
| +20.90 | +15.33 | 00:20:10.023 | Angers | Angers | Pass | - | [15.1, 38.1] |  |
| +22.91 | +17.34 | 00:20:12.027 | Angers | Angers | Ball Receipt* | - | [21.0, 61.9] |  |
| +22.91 | +17.34 | 00:20:12.027 | Angers | Angers | Carry | - | [21.0, 61.9] |  |
| +24.44 | +18.87 | 00:20:13.559 | Angers | Angers | Pass | - | [24.4, 68.1] |  |
| +25.42 | +19.85 | 00:20:14.542 | Angers | Angers | Ball Receipt* | - | [38.3, 61.9] |  |
| +25.42 | +19.85 | 00:20:14.542 | Angers | Angers | Carry | - | [38.3, 61.9] |  |

---

### Episode 41: `3838017_p66_aa822c3f`
- **Match**: `3838017` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 2, Pressing Team: **Clermont Foot** vs. Possession Team: **Paris Saint-Germain**
- **Initiation Action**: `Pressure` by **Vivaldo Borges dos Santos Neto** at `00:00:50.509` (Turnover delay: 1.928s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.928s). Harmless transition (opp max progression x=35.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.75 | -3.68 | 00:00:46.830 | Clermont Foot | Clermont Foot | Ball Receipt* | - | [112.5, 7.9] |  |
| -1.75 | -3.68 | 00:00:46.830 | Clermont Foot | Clermont Foot | Carry | - | [112.5, 7.9] |  |
| -0.83 | -2.76 | 00:00:47.748 | Clermont Foot | Clermont Foot | Pass | - | [116.1, 10.2] |  |
| +0.00 | -1.93 | 00:00:48.581 | Clermont Foot | Clermont Foot | Ball Receipt* | - | [112.5, 38.6] |  |
| +0.00 | -1.93 | 00:00:48.581 | Paris Saint-Germain | Clermont Foot | Clearance | - | [7.6, 44.1] | 🔄 **TURNOVER** |
| +1.66 | -0.27 | 00:00:50.237 | Paris Saint-Germain | Paris Saint-Germain | Ball Recovery | - | [10.8, 53.6] |  |
| +1.66 | -0.27 | 00:00:50.237 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [10.8, 53.6] |  |
| +1.93 | +0.00 | 00:00:50.509 | Clermont Foot | Paris Saint-Germain | Pressure | **YES** | [108.5, 27.6] | ⭐ **CP INITIATION** |
| +2.12 | +0.19 | 00:00:50.699 | Clermont Foot | Paris Saint-Germain | Pressure | **YES** | [109.4, 24.4] |  |
| +2.81 | +0.88 | 00:00:51.394 | Paris Saint-Germain | Paris Saint-Germain | Dispossessed | - | [11.5, 55.1] |  |
| +2.81 | +0.88 | 00:00:51.394 | Clermont Foot | Paris Saint-Germain | Duel | **YES** | [108.6, 25.0] |  |
| +4.95 | +3.02 | 00:00:53.530 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [6.1, 54.4] |  |
| +6.72 | +4.79 | 00:00:55.299 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [35.7, 57.2] |  |
| +6.72 | +4.79 | 00:00:55.299 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [35.7, 57.2] |  |
| +7.49 | +5.56 | 00:00:56.073 | Clermont Foot | Paris Saint-Germain | Pressure | - | [85.0, 25.0] |  |
| +8.43 | +6.51 | 00:00:57.015 | Paris Saint-Germain | Paris Saint-Germain | Miscontrol | - | [32.8, 52.8] |  |
| +8.81 | +6.89 | 00:00:57.396 | Clermont Foot | Clermont Foot | Ball Recovery | - | [87.0, 28.3] |  |
| +8.81 | +6.89 | 00:00:57.396 | Clermont Foot | Clermont Foot | Carry | - | [87.0, 28.3] |  |
| +9.39 | +7.46 | 00:00:57.971 | Paris Saint-Germain | Clermont Foot | Pressure | **YES** | [32.5, 47.5] |  |
| +9.56 | +7.63 | 00:00:58.142 | Clermont Foot | Clermont Foot | Pass | - | [87.1, 30.5] |  |
| +10.40 | +8.47 | 00:00:58.978 | Clermont Foot | Clermont Foot | Ball Receipt* | - | [86.8, 44.1] |  |
| +10.40 | +8.47 | 00:00:58.978 | Clermont Foot | Clermont Foot | Carry | - | [86.8, 44.1] |  |
| +11.24 | +9.32 | 00:00:59.826 | Clermont Foot | Clermont Foot | Pass | - | [88.9, 41.8] |  |
| +12.61 | +10.69 | 00:01:01.196 | Clermont Foot | Clermont Foot | Ball Receipt* | - | [104.7, 39.9] |  |
| +12.61 | +10.69 | 00:01:01.196 | Clermont Foot | Clermont Foot | Carry | - | [104.7, 39.9] |  |
| +13.08 | +11.16 | 00:01:01.664 | Paris Saint-Germain | Clermont Foot | Pressure | **YES** | [13.1, 40.0] |  |
| +13.87 | +11.94 | 00:01:02.447 | Clermont Foot | Clermont Foot | Dribble | - | [106.2, 40.4] |  |
| +13.87 | +11.94 | 00:01:02.447 | Paris Saint-Germain | Paris Saint-Germain | Duel | **YES** | [13.9, 39.7] |  |
| +13.87 | +11.94 | 00:01:02.447 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [13.9, 39.7] |  |
| +14.59 | +12.66 | 00:01:03.169 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [13.9, 39.5] |  |
| +15.10 | +13.17 | 00:01:03.681 | Clermont Foot | Paris Saint-Germain | Pressure | **YES** | [104.7, 37.3] |  |
| +15.22 | +13.29 | 00:01:03.801 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [14.9, 42.1] |  |
| +15.22 | +13.29 | 00:01:03.801 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [14.9, 42.1] |  |
| +15.40 | +13.48 | 00:01:03.986 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [15.0, 41.2] |  |
| +17.49 | +15.56 | 00:01:06.072 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [20.5, 21.8] |  |
| +17.49 | +15.56 | 00:01:06.072 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [20.5, 21.8] |  |
| +17.86 | +15.93 | 00:01:06.443 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [23.1, 20.8] |  |
| +19.72 | +17.80 | 00:01:08.305 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [39.3, 21.1] |  |
| +19.72 | +17.80 | 00:01:08.305 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [39.3, 21.1] |  |
| +20.05 | +18.12 | 00:01:08.632 | Clermont Foot | Paris Saint-Germain | Pressure | - | [74.4, 61.4] |  |

---

### Episode 42: `3998859_p19_2232d685`
- **Match**: `3998859` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Netherlands Women's** vs. Possession Team: **Netherlands Women's**
- **Initiation Action**: `Pressure` by **Danielle van de Donk** at `00:08:12.066` (Turnover delay: 3.531s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.008s by Netherlands Women's. Harmless transition (opp max progression x=48.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.68 | -5.21 | 00:08:06.851 | France Women's | Netherlands Women's | Pressure | - | [55.6, 63.3] |  |
| -1.18 | -4.71 | 00:08:07.359 | France Women's | Netherlands Women's | Pressure | - | [58.2, 58.3] |  |
| -0.78 | -4.31 | 00:08:07.755 | Netherlands Women's | Netherlands Women's | Pass | - | [61.4, 22.2] |  |
| +0.00 | -3.53 | 00:08:08.535 | France Women's | Netherlands Women's | Interception | - | [47.3, 56.2] | 🔄 **TURNOVER** |
| +0.00 | -3.53 | 00:08:08.535 | France Women's | Netherlands Women's | Carry | - | [47.3, 56.2] |  |
| +1.50 | -2.03 | 00:08:10.037 | France Women's | Netherlands Women's | Pass | - | [52.4, 59.2] |  |
| +3.53 | +0.00 | 00:08:12.066 | Netherlands Women's | Netherlands Women's | Pressure | **YES** | [54.2, 13.6] | ⭐ **CP INITIATION** |
| +3.54 | +0.01 | 00:08:12.074 | France Women's | Netherlands Women's | Ball Receipt* | - | [64.9, 66.5] |  |
| +3.54 | +0.01 | 00:08:12.074 | France Women's | Netherlands Women's | Carry | - | [64.9, 66.5] |  |
| +4.58 | +1.05 | 00:08:13.112 | France Women's | Netherlands Women's | Dispossessed | - | [70.0, 68.6] |  |
| +4.58 | +1.05 | 00:08:13.112 | Netherlands Women's | Netherlands Women's | Duel | **YES** | [50.1, 11.5] |  |
| +6.86 | +3.33 | 00:08:15.395 | Netherlands Women's | Netherlands Women's | Ball Recovery | - | [33.4, 14.1] |  |
| +6.86 | +3.33 | 00:08:15.395 | Netherlands Women's | Netherlands Women's | Carry | - | [33.4, 14.1] |  |
| +7.45 | +3.92 | 00:08:15.985 | France Women's | Netherlands Women's | Pressure | - | [84.1, 69.3] |  |
| +7.77 | +4.24 | 00:08:16.302 | Netherlands Women's | Netherlands Women's | Pass | - | [32.8, 13.4] |  |
| +8.64 | +5.11 | 00:08:17.175 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [34.3, 26.2] |  |
| +8.64 | +5.11 | 00:08:17.175 | Netherlands Women's | Netherlands Women's | Carry | - | [34.3, 26.2] |  |
| +9.44 | +5.91 | 00:08:17.975 | Netherlands Women's | Netherlands Women's | Pass | - | [34.3, 22.4] |  |
| +10.47 | +6.94 | 00:08:19.002 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [54.4, 11.5] |  |
| +10.47 | +6.94 | 00:08:19.002 | Netherlands Women's | Netherlands Women's | Carry | - | [54.4, 11.5] |  |
| +11.38 | +7.85 | 00:08:19.918 | Netherlands Women's | Netherlands Women's | Pass | - | [53.5, 11.5] |  |
| +12.43 | +8.90 | 00:08:20.961 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [46.3, 3.4] |  |
| +12.43 | +8.90 | 00:08:20.961 | Netherlands Women's | Netherlands Women's | Carry | - | [46.3, 3.4] |  |
| +14.92 | +11.39 | 00:08:23.456 | Netherlands Women's | Netherlands Women's | Pass | - | [46.3, 3.4] |  |
| +16.15 | +12.62 | 00:08:24.682 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [37.1, 7.2] |  |
| +16.15 | +12.62 | 00:08:24.682 | Netherlands Women's | Netherlands Women's | Carry | - | [37.1, 7.2] |  |
| +17.43 | +13.90 | 00:08:25.969 | Netherlands Women's | Netherlands Women's | Pass | - | [37.1, 7.2] |  |
| +18.64 | +15.11 | 00:08:27.180 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [24.7, 17.9] |  |
| +18.64 | +15.11 | 00:08:27.180 | Netherlands Women's | Netherlands Women's | Carry | - | [24.7, 17.9] |  |
| +19.80 | +16.27 | 00:08:28.339 | Netherlands Women's | Netherlands Women's | Pass | - | [23.6, 17.9] |  |
| +21.53 | +18.00 | 00:08:30.067 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [8.6, 38.9] |  |
| +21.53 | +18.00 | 00:08:30.067 | Netherlands Women's | Netherlands Women's | Carry | - | [8.6, 38.9] |  |

---

### Episode 43: `3857286_p31_dae26577`
- **Match**: `3857286` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 1, Pressing Team: **Qatar** vs. Possession Team: **Qatar**
- **Initiation Action**: `Foul Committed` by **Almoez Ali Zainalabiddin Abdulla** at `00:21:06.016` (Turnover delay: 0.08s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Qatar. Harmless transition (opp max progression x=46.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.63 | -1.71 | 00:21:04.310 | Qatar | Qatar | Pass | - | [46.3, 0.1] |  |
| -0.43 | -0.51 | 00:21:05.508 | Qatar | Qatar | Pressure | - | [44.6, 13.0] |  |
| +0.00 | -0.08 | 00:21:05.936 | Ecuador | Qatar | Ball Recovery | - | [76.2, 67.1] | 🔄 **TURNOVER** |
| +0.00 | -0.08 | 00:21:05.936 | Ecuador | Qatar | Carry | - | [76.2, 67.1] |  |
| +0.08 | +0.00 | 00:21:06.016 | Qatar | Qatar | Foul Committed | **YES** | [43.9, 13.0] | ⭐ **CP INITIATION** |
| +0.08 | +0.00 | 00:21:06.016 | Ecuador | Qatar | Foul Won | - | [76.2, 67.1] |  |

---

### Episode 44: `3837727_p66_ef8b7b34`
- **Match**: `3837727` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 1, Pressing Team: **OGC Nice** vs. Possession Team: **Paris Saint-Germain**
- **Initiation Action**: `Pressure` by **Dante Bonfim da Costa Santos** at `00:45:00.085` (Turnover delay: 3.768s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.768s). Dangerous transition triggered by: Shot at dt=4.469s.

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.98 | -6.74 | 00:44:53.340 | OGC Nice | OGC Nice | Pass | - | [20.6, 65.6] |  |
| -2.11 | -5.88 | 00:44:54.207 | OGC Nice | OGC Nice | Ball Receipt* | - | [15.4, 56.2] |  |
| -2.11 | -5.88 | 00:44:54.207 | OGC Nice | OGC Nice | Carry | - | [15.4, 56.2] |  |
| -1.97 | -5.74 | 00:44:54.345 | Paris Saint-Germain | OGC Nice | Pressure | - | [100.9, 21.5] |  |
| -1.45 | -5.22 | 00:44:54.868 | OGC Nice | OGC Nice | Pass | - | [15.4, 56.4] |  |
| +0.00 | -3.77 | 00:44:56.317 | OGC Nice | OGC Nice | Ball Receipt* | - | [33.0, 49.9] |  |
| +0.00 | -3.77 | 00:44:56.317 | Paris Saint-Germain | Paris Saint-Germain | Ball Recovery | - | [93.6, 28.3] | 🔄 **TURNOVER** |
| +0.00 | -3.77 | 00:44:56.317 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [93.6, 28.3] |  |
| +1.95 | -1.81 | 00:44:58.271 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [101.3, 29.9] |  |
| +2.43 | -1.34 | 00:44:58.749 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [100.7, 39.2] |  |
| +2.43 | -1.34 | 00:44:58.749 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [100.7, 39.2] |  |
| +3.77 | +0.00 | 00:45:00.085 | OGC Nice | Paris Saint-Germain | Pressure | **YES** | [17.6, 44.7] | ⭐ **CP INITIATION** |
| +4.72 | +0.95 | 00:45:01.037 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [100.1, 28.7] |  |
| +6.54 | +2.77 | 00:45:02.857 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [112.4, 22.7] |  |
| +6.54 | +2.77 | 00:45:02.857 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [112.4, 22.7] |  |
| +7.39 | +3.62 | 00:45:03.705 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [105.3, 25.0] |  |
| +7.39 | +3.62 | 00:45:03.705 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [105.3, 25.0] |  |
| +8.24 | +4.47 | 00:45:04.554 | Paris Saint-Germain | Paris Saint-Germain | Shot | - | [106.2, 25.2] |  |
| +8.67 | +4.90 | 00:45:04.990 | OGC Nice | Paris Saint-Germain | Goal Keeper | - | [2.1, 43.3] |  |

---

### Episode 45: `3788759_p102_2270d960`
- **Match**: `3788759` | **Competition**: UEFA Euro (2020)
- **Context**: Period 2, Pressing Team: **Scotland** vs. Possession Team: **Scotland**
- **Initiation Action**: `Pressure` by **Billy Gilmour** at `00:24:14.743` (Turnover delay: 0.353s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.533s by Scotland. Harmless transition (opp max progression x=24.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.52 | -1.87 | 00:24:12.869 | Scotland | Scotland | Ball Receipt* | - | [69.2, 39.1] |  |
| -1.52 | -1.87 | 00:24:12.869 | England | Scotland | Pass | - | [48.9, 39.8] |  |
| -1.52 | -1.87 | 00:24:12.869 | Scotland | Scotland | Duel | - | [71.2, 40.3] |  |
| -0.77 | -1.12 | 00:24:13.623 | Scotland | Scotland | Ball Recovery | - | [56.7, 44.0] |  |
| +0.00 | -0.35 | 00:24:14.390 | England | Scotland | Ball Recovery | - | [65.1, 30.3] | 🔄 **TURNOVER** |
| +0.00 | -0.35 | 00:24:14.390 | England | Scotland | Carry | - | [65.1, 30.3] |  |
| +0.35 | +0.00 | 00:24:14.743 | Scotland | Scotland | Pressure | **YES** | [52.9, 51.6] | ⭐ **CP INITIATION** |
| +0.89 | +0.53 | 00:24:15.276 | Scotland | Scotland | Pressure | **YES** | [55.2, 44.6] |  |
| +1.18 | +0.83 | 00:24:15.572 | England | Scotland | Dribble | - | [65.4, 33.7] |  |
| +1.18 | +0.83 | 00:24:15.572 | Scotland | Scotland | Duel | **YES** | [54.7, 46.4] |  |
| +1.18 | +0.83 | 00:24:15.572 | Scotland | Scotland | Carry | - | [54.7, 46.4] |  |
| +2.24 | +1.88 | 00:24:16.628 | England | Scotland | Pressure | - | [66.1, 39.3] |  |
| +3.03 | +2.68 | 00:24:17.419 | Scotland | Scotland | Pass | - | [52.3, 44.0] |  |
| +4.45 | +4.10 | 00:24:18.840 | Scotland | Scotland | Ball Receipt* | - | [48.1, 53.7] |  |
| +4.45 | +4.10 | 00:24:18.840 | Scotland | Scotland | Pass | - | [48.1, 53.7] |  |
| +5.32 | +4.96 | 00:24:19.707 | Scotland | Scotland | Ball Receipt* | - | [57.4, 57.1] |  |
| +5.32 | +4.96 | 00:24:19.707 | Scotland | Scotland | Carry | - | [57.4, 57.1] |  |
| +5.98 | +5.63 | 00:24:20.370 | England | Scotland | Pressure | - | [66.9, 25.3] |  |
| +8.44 | +8.09 | 00:24:22.831 | Scotland | Scotland | Pass | - | [67.5, 40.1] |  |
| +10.08 | +9.73 | 00:24:24.472 | Scotland | Scotland | Ball Receipt* | - | [70.4, 17.4] |  |
| +10.08 | +9.73 | 00:24:24.472 | Scotland | Scotland | Carry | - | [70.4, 17.4] |  |
| +14.01 | +13.66 | 00:24:28.404 | Scotland | Scotland | Pass | - | [78.3, 14.6] |  |
| +15.03 | +14.68 | 00:24:29.420 | Scotland | Scotland | Ball Receipt* | - | [82.5, 8.6] |  |
| +15.03 | +14.68 | 00:24:29.420 | Scotland | Scotland | Carry | - | [82.5, 8.6] |  |
| +15.83 | +15.48 | 00:24:30.220 | Scotland | Scotland | Pass | - | [83.8, 9.8] |  |
| +17.18 | +16.83 | 00:24:31.574 | Scotland | Scotland | Ball Receipt* | - | [72.7, 23.9] |  |
| +17.18 | +16.83 | 00:24:31.574 | Scotland | Scotland | Carry | - | [72.7, 23.9] |  |
| +18.38 | +18.03 | 00:24:32.774 | Scotland | Scotland | Pass | - | [72.7, 23.9] |  |
| +19.37 | +19.02 | 00:24:33.764 | Scotland | Scotland | Ball Receipt* | - | [77.7, 33.1] |  |
| +19.37 | +19.02 | 00:24:33.764 | Scotland | Scotland | Carry | - | [77.7, 33.1] |  |

---

### Episode 46: `3802805_p23_158bd435`
- **Match**: `3802805` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 1, Pressing Team: **OGC Nice** vs. Possession Team: **OGC Nice**
- **Initiation Action**: `Duel` by **Kasper Dolberg** at `00:10:56.127` (Turnover delay: 0.244s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.811s by OGC Nice. Harmless transition (opp max progression x=7.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.14 | -1.38 | 00:10:54.746 | Paris Saint-Germain | OGC Nice | Pressure | - | [62.9, 34.4] |  |
| -1.03 | -1.27 | 00:10:54.855 | OGC Nice | OGC Nice | Ball Receipt* | - | [57.2, 45.7] |  |
| -1.03 | -1.27 | 00:10:54.855 | OGC Nice | OGC Nice | Carry | - | [57.2, 45.7] |  |
| -1.01 | -1.26 | 00:10:54.870 | OGC Nice | OGC Nice | Miscontrol | - | [56.5, 45.7] |  |
| -0.12 | -0.36 | 00:10:55.767 | OGC Nice | OGC Nice | Pressure | - | [55.2, 44.4] |  |
| +0.00 | -0.24 | 00:10:55.883 | Paris Saint-Germain | OGC Nice | Ball Recovery | - | [64.9, 35.7] | 🔄 **TURNOVER** |
| +0.00 | -0.24 | 00:10:55.883 | Paris Saint-Germain | OGC Nice | Carry | - | [64.9, 35.7] |  |
| +0.24 | +0.00 | 00:10:56.127 | Paris Saint-Germain | OGC Nice | Dribble | - | [65.1, 36.3] |  |
| +0.24 | +0.00 | 00:10:56.127 | OGC Nice | OGC Nice | Duel | **YES** | [55.0, 43.8] | ⭐ **CP INITIATION** |
| +1.05 | +0.81 | 00:10:56.938 | OGC Nice | OGC Nice | Ball Recovery | - | [51.8, 42.3] |  |
| +1.05 | +0.81 | 00:10:56.938 | OGC Nice | OGC Nice | Carry | - | [51.8, 42.3] |  |
| +3.25 | +3.00 | 00:10:59.128 | Paris Saint-Germain | OGC Nice | Pressure | - | [68.3, 37.8] |  |
| +3.60 | +3.36 | 00:10:59.482 | OGC Nice | OGC Nice | Pass | - | [52.2, 42.3] |  |
| +4.24 | +4.00 | 00:11:00.124 | OGC Nice | OGC Nice | Ball Receipt* | - | [44.7, 45.5] |  |
| +4.24 | +4.00 | 00:11:00.124 | OGC Nice | OGC Nice | Carry | - | [44.7, 45.5] |  |
| +4.32 | +4.08 | 00:11:00.204 | OGC Nice | OGC Nice | Pass | - | [44.7, 45.5] |  |
| +6.43 | +6.19 | 00:11:02.313 | OGC Nice | OGC Nice | Ball Receipt* | - | [51.4, 10.0] |  |
| +6.43 | +6.19 | 00:11:02.313 | OGC Nice | OGC Nice | Carry | - | [51.4, 10.0] |  |
| +6.77 | +6.52 | 00:11:02.651 | OGC Nice | OGC Nice | Pass | - | [49.9, 10.0] |  |
| +7.90 | +7.65 | 00:11:03.779 | OGC Nice | OGC Nice | Ball Receipt* | - | [64.0, 6.6] |  |
| +7.90 | +7.65 | 00:11:03.779 | OGC Nice | OGC Nice | Carry | - | [64.0, 6.6] |  |
| +11.55 | +11.30 | 00:11:07.430 | OGC Nice | OGC Nice | Pass | - | [81.8, 15.4] |  |
| +12.24 | +11.99 | 00:11:08.120 | OGC Nice | OGC Nice | Ball Receipt* | - | [79.6, 24.8] |  |
| +12.24 | +11.99 | 00:11:08.120 | OGC Nice | OGC Nice | Carry | - | [79.6, 24.8] |  |
| +15.62 | +15.38 | 00:11:11.504 | OGC Nice | OGC Nice | Pass | - | [105.5, 24.1] |  |
| +16.89 | +16.65 | 00:11:12.778 | OGC Nice | OGC Nice | Ball Receipt* | - | [111.5, 17.7] |  |
| +16.89 | +16.65 | 00:11:12.778 | OGC Nice | OGC Nice | Carry | - | [111.5, 17.7] |  |
| +17.03 | +16.79 | 00:11:12.914 | OGC Nice | OGC Nice | Pass | - | [117.0, 17.7] |  |

---

### Episode 47: `3837876_p60_9aba1cc0`
- **Match**: `3837876` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 1, Pressing Team: **Paris Saint-Germain** vs. Possession Team: **Lille**
- **Initiation Action**: `Pressure` by **Juan Bernat Velasco** at `00:35:09.868` (Turnover delay: 0.749s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=0.749s). Dangerous transition triggered by: Final third entry at dt=14.342s (initial x=76.0, max x=86.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.59 | -3.34 | 00:35:06.529 | Lille | Paris Saint-Germain | Pressure | - | [101.3, 49.6] |  |
| -1.72 | -2.47 | 00:35:07.402 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [6.3, 35.4] |  |
| -1.72 | -2.47 | 00:35:07.402 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [7.5, 34.5] |  |
| +0.00 | -0.75 | 00:35:09.119 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [44.1, 7.4] |  |
| +0.00 | -0.75 | 00:35:09.119 | Lille | Lille | Ball Recovery | - | [76.0, 69.4] | 🔄 **TURNOVER** |
| +0.00 | -0.75 | 00:35:09.119 | Lille | Lille | Carry | - | [76.0, 69.4] |  |
| +0.75 | +0.00 | 00:35:09.868 | Paris Saint-Germain | Lille | Pressure | **YES** | [42.3, 12.6] | ⭐ **CP INITIATION** |
| +1.20 | +0.45 | 00:35:10.315 | Lille | Lille | Pass | - | [78.1, 62.0] |  |
| +2.85 | +2.10 | 00:35:11.968 | Paris Saint-Germain | Lille | Pressure | **YES** | [51.4, 34.6] |  |
| +3.21 | +2.46 | 00:35:12.331 | Lille | Lille | Ball Receipt* | - | [71.6, 47.5] |  |
| +3.21 | +2.46 | 00:35:12.331 | Lille | Lille | Pass | - | [70.6, 46.5] |  |
| +5.38 | +4.63 | 00:35:14.498 | Lille | Lille | Ball Receipt* | - | [49.9, 30.7] |  |
| +5.38 | +4.63 | 00:35:14.498 | Lille | Lille | Carry | - | [49.9, 30.7] |  |
| +10.61 | +9.86 | 00:35:19.727 | Lille | Lille | Pass | - | [52.1, 29.4] |  |
| +11.39 | +10.64 | 00:35:20.508 | Lille | Lille | Ball Receipt* | - | [62.7, 25.3] |  |
| +11.39 | +10.64 | 00:35:20.508 | Lille | Lille | Carry | - | [62.7, 25.3] |  |
| +13.08 | +12.33 | 00:35:22.196 | Lille | Lille | Pass | - | [69.5, 21.3] |  |
| +15.09 | +14.34 | 00:35:24.210 | Lille | Lille | Ball Receipt* | - | [86.2, 7.7] |  |
| +15.09 | +14.34 | 00:35:24.210 | Lille | Lille | Carry | - | [86.2, 7.7] |  |
| +16.17 | +15.43 | 00:35:25.294 | Paris Saint-Germain | Lille | Pressure | - | [29.4, 62.8] |  |
| +16.68 | +15.93 | 00:35:25.800 | Lille | Lille | Pass | - | [93.8, 16.3] |  |
| +17.67 | +16.92 | 00:35:26.789 | Lille | Lille | Ball Receipt* | - | [99.1, 33.2] |  |
| +17.67 | +16.92 | 00:35:26.789 | Lille | Lille | Carry | - | [99.1, 33.2] |  |
| +17.86 | +17.11 | 00:35:26.978 | Paris Saint-Germain | Lille | Pressure | - | [20.2, 49.8] |  |
| +19.08 | +18.33 | 00:35:28.197 | Lille | Lille | Shot | - | [102.9, 38.5] |  |
| +19.11 | +18.37 | 00:35:28.233 | Paris Saint-Germain | Lille | Block | - | [16.0, 41.5] |  |
| +19.19 | +18.44 | 00:35:28.306 | Paris Saint-Germain | Lille | Goal Keeper | - | [2.2, 40.5] |  |

---

### Episode 48: `3788767_p136_ed227f40`
- **Match**: `3788767` | **Competition**: UEFA Euro (2020)
- **Context**: Period 2, Pressing Team: **Ukraine** vs. Possession Team: **Ukraine**
- **Initiation Action**: `Duel` by **Andriy Yarmolenko** at `00:14:14.050` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Ukraine. Harmless transition (opp max progression x=65.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.71 | -2.71 | 00:14:11.338 | Ukraine | Austria | Pressure | **YES** | [72.7, 68.5] |  |
| -0.83 | -0.83 | 00:14:13.221 | Ukraine | Austria | Pressure | **YES** | [65.8, 68.9] |  |
| +0.00 | +0.00 | 00:14:14.050 | Austria | Austria | Dispossessed | - | [54.8, 13.2] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:14:14.050 | Ukraine | Ukraine | Duel | **YES** | [65.3, 66.9] | ⭐ **CP INITIATION** |
| +0.00 | +0.00 | 00:14:14.050 | Ukraine | Ukraine | Carry | - | [65.3, 66.9] |  |
| +4.53 | +4.53 | 00:14:18.583 | Ukraine | Ukraine | Pass | - | [50.8, 62.3] |  |
| +6.10 | +6.10 | 00:14:20.145 | Ukraine | Ukraine | Ball Receipt* | - | [51.4, 48.7] |  |
| +6.10 | +6.10 | 00:14:20.145 | Ukraine | Ukraine | Carry | - | [51.4, 48.7] |  |
| +7.97 | +7.97 | 00:14:22.016 | Ukraine | Ukraine | Pass | - | [50.6, 46.2] |  |
| +9.34 | +9.34 | 00:14:23.389 | Ukraine | Ukraine | Ball Receipt* | - | [50.6, 21.3] |  |
| +9.34 | +9.34 | 00:14:23.389 | Ukraine | Ukraine | Carry | - | [50.6, 21.3] |  |
| +10.63 | +10.63 | 00:14:24.680 | Ukraine | Ukraine | Pass | - | [50.8, 19.3] |  |
| +11.78 | +11.78 | 00:14:25.833 | Ukraine | Ukraine | Ball Receipt* | - | [63.2, 5.8] |  |
| +11.78 | +11.78 | 00:14:25.833 | Ukraine | Ukraine | Carry | - | [63.2, 5.8] |  |
| +15.81 | +15.81 | 00:14:29.860 | Ukraine | Ukraine | Pass | - | [73.7, 9.1] |  |
| +16.58 | +16.58 | 00:14:30.634 | Austria | Ukraine | Pressure | - | [36.1, 55.8] |  |
| +17.02 | +17.02 | 00:14:31.067 | Ukraine | Ukraine | Ball Receipt* | - | [80.5, 21.6] |  |
| +17.02 | +17.02 | 00:14:31.067 | Ukraine | Ukraine | Carry | - | [80.5, 21.6] |  |
| +17.06 | +17.06 | 00:14:31.107 | Ukraine | Ukraine | Pass | - | [80.5, 23.1] |  |
| +18.68 | +18.68 | 00:14:32.732 | Ukraine | Ukraine | Ball Receipt* | - | [58.2, 18.5] |  |
| +18.68 | +18.68 | 00:14:32.732 | Ukraine | Ukraine | Carry | - | [58.2, 18.5] |  |

---

### Episode 49: `3893810_p95_1ce696ed`
- **Match**: `3893810` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Portugal Women's** vs. Possession Team: **Vietnam Women's**
- **Initiation Action**: `Pressure` by **Ana Rita Silva Seiça** at `00:43:05.404` (Turnover delay: 2.124s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.124s). Harmless transition (opp max progression x=66.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.61 | -4.73 | 00:43:00.675 | Vietnam Women's | Portugal Women's | Pressure | - | [28.9, 31.8] |  |
| -2.25 | -4.37 | 00:43:01.032 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [91.2, 48.3] |  |
| -2.25 | -4.37 | 00:43:01.032 | Portugal Women's | Portugal Women's | Carry | - | [91.2, 48.3] |  |
| -2.07 | -4.19 | 00:43:01.210 | Portugal Women's | Portugal Women's | Miscontrol | - | [91.2, 48.3] |  |
| +0.00 | -2.12 | 00:43:03.280 | Vietnam Women's | Vietnam Women's | Pass | - | [38.3, 37.5] | 🔄 **TURNOVER** |
| +1.33 | -0.80 | 00:43:04.606 | Vietnam Women's | Vietnam Women's | Ball Receipt* | - | [39.4, 47.1] |  |
| +1.33 | -0.80 | 00:43:04.606 | Vietnam Women's | Vietnam Women's | Carry | - | [39.4, 47.1] |  |
| +1.42 | -0.71 | 00:43:04.698 | Vietnam Women's | Vietnam Women's | Pass | - | [41.2, 47.1] |  |
| +2.12 | +0.00 | 00:43:05.404 | Portugal Women's | Vietnam Women's | Pressure | **YES** | [66.3, 38.1] | ⭐ **CP INITIATION** |
| +2.37 | +0.24 | 00:43:05.648 | Vietnam Women's | Vietnam Women's | Ball Receipt* | - | [54.8, 41.3] |  |
| +2.37 | +0.24 | 00:43:05.648 | Vietnam Women's | Vietnam Women's | Carry | - | [54.8, 41.3] |  |
| +2.42 | +0.30 | 00:43:05.701 | Vietnam Women's | Vietnam Women's | Pass | - | [53.8, 42.0] |  |
| +3.00 | +0.88 | 00:43:06.279 | Vietnam Women's | Vietnam Women's | Ball Receipt* | - | [52.3, 36.2] |  |
| +3.00 | +0.88 | 00:43:06.279 | Vietnam Women's | Vietnam Women's | Carry | - | [52.3, 36.2] |  |
| +4.26 | +2.14 | 00:43:07.544 | Vietnam Women's | Vietnam Women's | Pass | - | [52.0, 38.5] |  |
| +4.54 | +2.42 | 00:43:07.822 | Vietnam Women's | Vietnam Women's | Ball Receipt* | - | [60.7, 44.6] |  |
| +4.54 | +2.42 | 00:43:07.822 | Portugal Women's | Vietnam Women's | Block | **YES** | [62.7, 39.4] |  |
| +6.69 | +4.56 | 00:43:09.967 | Vietnam Women's | Vietnam Women's | Pressure | - | [66.6, 60.2] |  |
| +7.45 | +5.33 | 00:43:10.730 | Portugal Women's | Portugal Women's | Ball Recovery | - | [50.9, 20.7] |  |
| +7.45 | +5.33 | 00:43:10.730 | Portugal Women's | Portugal Women's | Carry | - | [50.9, 20.7] |  |
| +7.99 | +5.87 | 00:43:11.272 | Vietnam Women's | Portugal Women's | Foul Committed | **YES** | [69.2, 59.4] |  |
| +7.99 | +5.87 | 00:43:11.272 | Portugal Women's | Portugal Women's | Foul Won | - | [50.9, 20.7] |  |
| +15.59 | +13.47 | 00:43:18.874 | Portugal Women's | Portugal Women's | Pass | - | [50.9, 20.7] |  |
| +17.34 | +15.22 | 00:43:20.623 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [39.4, 34.1] |  |
| +17.48 | +15.36 | 00:43:20.763 | Portugal Women's | Portugal Women's | Pass | - | [40.2, 31.5] |  |
| +19.05 | +16.93 | 00:43:22.335 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [42.2, 50.9] |  |
| +19.05 | +16.93 | 00:43:22.335 | Portugal Women's | Portugal Women's | Carry | - | [42.2, 50.9] |  |
| +20.76 | +18.63 | 00:43:24.037 | Portugal Women's | Portugal Women's | Pass | - | [46.8, 52.5] |  |

---

### Episode 50: `3773661_p131_97a99e33`
- **Match**: `3773661` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Barcelona** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pass` by **Sergio Busquets i Burgos** at `00:42:59.472` (Turnover delay: 4.953s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.851s by Barcelona. Harmless transition (opp max progression x=21.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -4.95 | 00:42:54.519 | Getafe | Getafe | Ball Receipt* | - | [63.5, 11.1] |  |
| +0.00 | -4.95 | 00:42:54.519 | Barcelona | Getafe | Duel | - | [56.6, 69.0] |  |
| +0.00 | -4.95 | 00:42:54.519 | Getafe | Getafe | Pass | - | [63.5, 11.1] | 🔄 **TURNOVER** |
| +2.16 | -2.79 | 00:42:56.678 | Getafe | Getafe | Ball Receipt* | - | [85.1, 18.1] |  |
| +2.16 | -2.79 | 00:42:56.678 | Getafe | Getafe | Carry | - | [85.1, 18.1] |  |
| +3.82 | -1.14 | 00:42:58.335 | Getafe | Getafe | Pass | - | [100.1, 20.2] |  |
| +4.95 | +0.00 | 00:42:59.472 | Getafe | Getafe | Ball Receipt* | - | [99.0, 33.4] |  |
| +4.95 | +0.00 | 00:42:59.472 | Barcelona | Barcelona | Pass | **YES** | [21.1, 50.0] | ⭐ **CP INITIATION** |
| +5.80 | +0.85 | 00:43:00.323 | Getafe | Barcelona | Pressure | **YES** | [110.5, 35.4] |  |
| +6.01 | +1.06 | 00:43:00.530 | Barcelona | Barcelona | Ball Receipt* | - | [3.4, 42.1] |  |
| +6.01 | +1.06 | 00:43:00.530 | Barcelona | Barcelona | Carry | - | [3.4, 42.1] |  |
| +8.70 | +3.74 | 00:43:03.217 | Barcelona | Barcelona | Pass | - | [3.5, 33.8] |  |
| +10.17 | +5.21 | 00:43:04.687 | Getafe | Barcelona | Pressure | - | [94.2, 67.3] |  |
| +10.48 | +5.53 | 00:43:05.001 | Barcelona | Barcelona | Ball Receipt* | - | [22.0, 12.8] |  |
| +10.48 | +5.53 | 00:43:05.001 | Barcelona | Barcelona | Carry | - | [22.0, 12.8] |  |
| +10.65 | +5.70 | 00:43:05.169 | Getafe | Barcelona | Foul Committed | - | [97.7, 67.7] |  |
| +10.65 | +5.70 | 00:43:05.169 | Barcelona | Barcelona | Foul Won | - | [22.4, 12.4] |  |

---

### Episode 51: `3877090_p141_16f2185d`
- **Match**: `3877090` | **Competition**: Major League Soccer (2023)
- **Context**: Period 2, Pressing Team: **LAFC** vs. Possession Team: **LAFC**
- **Initiation Action**: `Duel` by **Jesús David Murillo Largacha** at `00:23:11.946` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.713s by LAFC. Harmless transition (opp max progression x=78.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.76 | -1.76 | 00:23:10.189 | Inter Miami | Inter Miami | Ball Receipt* | - | [50.1, 7.2] |  |
| -1.76 | -1.76 | 00:23:10.189 | Inter Miami | Inter Miami | Carry | - | [50.1, 7.2] |  |
| -1.02 | -1.02 | 00:23:10.929 | LAFC | Inter Miami | Pressure | - | [68.1, 73.3] |  |
| +0.00 | +0.00 | 00:23:11.946 | Inter Miami | Inter Miami | Dispossessed | - | [41.4, 7.2] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:23:11.946 | LAFC | LAFC | Duel | **YES** | [78.7, 72.9] | ⭐ **CP INITIATION** |
| +1.71 | +1.71 | 00:23:13.659 | LAFC | LAFC | Ball Recovery | - | [75.0, 75.9] |  |
| +1.71 | +1.71 | 00:23:13.659 | LAFC | LAFC | Carry | - | [75.0, 75.9] |  |
| +2.05 | +2.05 | 00:23:13.994 | Inter Miami | LAFC | Pressure | **YES** | [46.9, 8.5] |  |
| +2.59 | +2.59 | 00:23:14.537 | LAFC | LAFC | Pass | - | [68.1, 77.3] |  |
| +4.37 | +4.37 | 00:23:16.317 | LAFC | LAFC | Ball Receipt* | - | [50.5, 54.0] |  |
| +4.37 | +4.37 | 00:23:16.317 | LAFC | LAFC | Carry | - | [50.5, 54.0] |  |
| +6.18 | +6.18 | 00:23:18.126 | LAFC | LAFC | Pass | - | [50.6, 51.7] |  |
| +7.55 | +7.55 | 00:23:19.499 | LAFC | LAFC | Ball Receipt* | - | [63.9, 48.5] |  |
| +7.55 | +7.55 | 00:23:19.499 | LAFC | LAFC | Carry | - | [63.9, 48.5] |  |
| +11.52 | +11.52 | 00:23:23.463 | LAFC | LAFC | Pass | - | [64.3, 41.6] |  |
| +14.77 | +14.77 | 00:23:26.711 | LAFC | LAFC | Ball Receipt* | - | [87.0, 8.4] |  |
| +14.77 | +14.77 | 00:23:26.711 | LAFC | LAFC | Carry | - | [87.0, 8.4] |  |
| +16.02 | +16.02 | 00:23:27.968 | LAFC | LAFC | Pass | - | [91.3, 6.2] |  |
| +17.26 | +17.26 | 00:23:29.207 | LAFC | LAFC | Ball Receipt* | - | [82.1, 20.0] |  |
| +17.26 | +17.26 | 00:23:29.207 | LAFC | LAFC | Carry | - | [82.1, 20.0] |  |
| +17.95 | +17.95 | 00:23:29.896 | LAFC | LAFC | Pass | - | [82.1, 20.3] |  |
| +18.94 | +18.94 | 00:23:30.886 | LAFC | LAFC | Ball Receipt* | - | [81.8, 35.5] |  |
| +18.94 | +18.94 | 00:23:30.886 | LAFC | LAFC | Carry | - | [81.8, 35.5] |  |
| +19.38 | +19.38 | 00:23:31.329 | LAFC | LAFC | Pass | - | [81.4, 38.2] |  |

---

### Episode 52: `3895309_p70_aa212a3b`
- **Match**: `3895309` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Borussia Dortmund** vs. Possession Team: **Borussia Dortmund**
- **Initiation Action**: `Duel` by **Mats Hummels** at `00:46:21.374` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.542s by Borussia Dortmund. Harmless transition (opp max progression x=18.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.72 | -2.72 | 00:46:18.652 | Bayer Leverkusen | Bayer Leverkusen | Ball Recovery | - | [100.5, 55.7] |  |
| -2.72 | -2.72 | 00:46:18.652 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [100.5, 55.7] |  |
| -0.32 | -0.32 | 00:46:21.057 | Borussia Dortmund | Bayer Leverkusen | Pressure | - | [15.4, 30.0] |  |
| +0.00 | +0.00 | 00:46:21.374 | Bayer Leverkusen | Bayer Leverkusen | Dispossessed | - | [102.1, 49.9] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:46:21.374 | Borussia Dortmund | Borussia Dortmund | Duel | **YES** | [18.0, 30.2] | ⭐ **CP INITIATION** |
| +0.54 | +0.54 | 00:46:21.916 | Borussia Dortmund | Borussia Dortmund | Ball Recovery | - | [29.1, 28.4] |  |
| +0.54 | +0.54 | 00:46:21.916 | Borussia Dortmund | Borussia Dortmund | Carry | - | [29.1, 28.4] |  |
| +2.40 | +2.40 | 00:46:23.777 | Bayer Leverkusen | Borussia Dortmund | Pressure | **YES** | [100.0, 55.1] |  |
| +2.65 | +2.65 | 00:46:24.022 | Borussia Dortmund | Borussia Dortmund | Dispossessed | - | [20.1, 25.0] |  |
| +2.65 | +2.65 | 00:46:24.022 | Bayer Leverkusen | Borussia Dortmund | Duel | **YES** | [100.0, 55.1] |  |
| +3.74 | +3.74 | 00:46:25.113 | Bayer Leverkusen | Borussia Dortmund | Offside | - | [104.3, 55.1] |  |

---

### Episode 53: `3837752_p68_e9277ea6`
- **Match**: `3837752` | **Competition**: Ligue 1 (2022/2023)
- **Context**: Period 1, Pressing Team: **AC Ajaccio** vs. Possession Team: **AC Ajaccio**
- **Initiation Action**: `Duel` by **Youssouf Koné** at `00:33:53.610` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.76s by AC Ajaccio. Harmless transition (opp max progression x=48.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.71 | -1.71 | 00:33:51.904 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [63.5, 72.0] |  |
| -0.85 | -0.85 | 00:33:52.755 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [70.0, 73.9] |  |
| -0.85 | -0.85 | 00:33:52.755 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [70.0, 73.9] |  |
| -0.69 | -0.69 | 00:33:52.921 | AC Ajaccio | Paris Saint-Germain | Pressure | - | [47.4, 7.5] |  |
| +0.00 | +0.00 | 00:33:53.610 | Paris Saint-Germain | Paris Saint-Germain | Dispossessed | - | [71.3, 72.9] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:33:53.610 | AC Ajaccio | AC Ajaccio | Duel | **YES** | [48.8, 7.2] | ⭐ **CP INITIATION** |
| +1.76 | +1.76 | 00:33:55.370 | AC Ajaccio | AC Ajaccio | Pass | - | [62.1, 12.9] |  |
| +2.28 | +2.28 | 00:33:55.887 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [56.4, 13.2] |  |
| +2.28 | +2.28 | 00:33:55.887 | AC Ajaccio | AC Ajaccio | Pass | - | [56.4, 13.2] |  |
| +2.97 | +2.97 | 00:33:56.580 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [58.3, 7.0] |  |
| +2.97 | +2.97 | 00:33:56.580 | AC Ajaccio | AC Ajaccio | Pass | - | [57.4, 7.0] |  |
| +3.66 | +3.66 | 00:33:57.272 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [62.6, 16.2] |  |
| +3.66 | +3.66 | 00:33:57.272 | AC Ajaccio | AC Ajaccio | Carry | - | [62.6, 16.2] |  |
| +4.19 | +4.19 | 00:33:57.797 | AC Ajaccio | AC Ajaccio | Pass | - | [62.6, 16.2] |  |
| +4.96 | +4.96 | 00:33:58.565 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [57.4, 17.8] |  |
| +4.96 | +4.96 | 00:33:58.565 | AC Ajaccio | AC Ajaccio | Pass | - | [57.4, 17.0] |  |
| +5.82 | +5.82 | 00:33:59.434 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [64.2, 29.8] |  |
| +5.82 | +5.82 | 00:33:59.434 | AC Ajaccio | AC Ajaccio | Pass | - | [64.2, 29.8] |  |
| +7.06 | +7.06 | 00:34:00.674 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [71.6, 22.2] |  |
| +7.06 | +7.06 | 00:34:00.674 | AC Ajaccio | AC Ajaccio | Carry | - | [71.6, 22.2] |  |
| +8.58 | +8.58 | 00:34:02.187 | AC Ajaccio | AC Ajaccio | Pass | - | [71.8, 14.3] |  |
| +9.78 | +9.78 | 00:34:03.394 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [78.9, 7.2] |  |
| +9.78 | +9.78 | 00:34:03.394 | AC Ajaccio | AC Ajaccio | Carry | - | [78.9, 7.2] |  |
| +13.06 | +13.06 | 00:34:06.670 | Paris Saint-Germain | AC Ajaccio | Pressure | - | [42.6, 67.2] |  |
| +14.36 | +14.36 | 00:34:07.967 | AC Ajaccio | AC Ajaccio | Pass | - | [69.7, 14.8] |  |
| +15.69 | +15.69 | 00:34:09.305 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [55.0, 26.5] |  |
| +15.69 | +15.69 | 00:34:09.305 | AC Ajaccio | AC Ajaccio | Carry | - | [55.0, 26.5] |  |
| +16.34 | +16.34 | 00:34:09.950 | AC Ajaccio | AC Ajaccio | Pass | - | [55.0, 26.8] |  |
| +17.35 | +17.35 | 00:34:10.960 | AC Ajaccio | AC Ajaccio | Ball Receipt* | - | [67.2, 32.8] |  |
| +17.35 | +17.35 | 00:34:10.960 | AC Ajaccio | AC Ajaccio | Carry | - | [67.2, 32.8] |  |
| +19.48 | +19.48 | 00:34:13.091 | Paris Saint-Germain | AC Ajaccio | Dribbled Past | - | [51.0, 34.6] |  |
| +19.48 | +19.48 | 00:34:13.091 | AC Ajaccio | AC Ajaccio | Dribble | - | [69.1, 45.5] |  |
| +19.48 | +19.48 | 00:34:13.091 | AC Ajaccio | AC Ajaccio | Carry | - | [69.1, 45.5] |  |

---

### Episode 54: `3893806_p44_f78bc44a`
- **Match**: `3893806` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Zambia W** vs. Possession Team: **Zambia W**
- **Initiation Action**: `Pass` by **Ireen Lungu** at `00:19:35.344` (Turnover delay: 1.049s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.962s by Zambia W. Harmless transition (opp max progression x=63.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.71 | -1.76 | 00:19:33.583 | Spain Women's | Spain Women's | Ball Receipt* | - | [48.0, 40.4] |  |
| -0.71 | -1.76 | 00:19:33.583 | Spain Women's | Spain Women's | Carry | - | [48.0, 40.4] |  |
| -0.27 | -1.32 | 00:19:34.027 | Zambia W | Spain Women's | Pressure | - | [70.4, 38.6] |  |
| +0.00 | -1.05 | 00:19:34.295 | Spain Women's | Spain Women's | Pass | - | [50.7, 42.9] | 🔄 **TURNOVER** |
| +1.05 | +0.00 | 00:19:35.344 | Spain Women's | Spain Women's | Ball Receipt* | - | [60.1, 41.5] |  |
| +1.05 | +0.00 | 00:19:35.344 | Zambia W | Zambia W | Pass | **YES** | [63.8, 37.8] | ⭐ **CP INITIATION** |
| +3.01 | +1.96 | 00:19:37.306 | Zambia W | Zambia W | Ball Receipt* | - | [49.0, 32.2] |  |
| +3.01 | +1.96 | 00:19:37.306 | Zambia W | Zambia W | Carry | - | [49.0, 32.2] |  |
| +4.13 | +3.08 | 00:19:38.427 | Zambia W | Zambia W | Pass | - | [53.1, 35.0] |  |
| +5.45 | +4.40 | 00:19:39.743 | Zambia W | Zambia W | Ball Receipt* | - | [64.7, 49.6] |  |
| +5.45 | +4.40 | 00:19:39.743 | Zambia W | Zambia W | Carry | - | [64.7, 49.6] |  |
| +5.65 | +4.60 | 00:19:39.943 | Zambia W | Zambia W | Miscontrol | - | [64.7, 49.6] |  |
| +7.87 | +6.82 | 00:19:42.161 | Zambia W | Zambia W | Pressure | - | [65.7, 60.9] |  |
| +7.90 | +6.85 | 00:19:42.193 | Spain Women's | Spain Women's | Pass | - | [54.2, 16.2] |  |
| +8.75 | +7.70 | 00:19:43.042 | Spain Women's | Spain Women's | Ball Receipt* | - | [40.3, 19.8] |  |
| +8.75 | +7.70 | 00:19:43.042 | Spain Women's | Spain Women's | Carry | - | [40.3, 19.8] |  |
| +10.62 | +9.57 | 00:19:44.915 | Spain Women's | Spain Women's | Pass | - | [40.0, 13.9] |  |
| +11.85 | +10.80 | 00:19:46.143 | Spain Women's | Spain Women's | Ball Receipt* | - | [57.8, 23.5] |  |
| +11.85 | +10.80 | 00:19:46.143 | Spain Women's | Spain Women's | Carry | - | [57.8, 23.5] |  |
| +13.05 | +12.01 | 00:19:47.350 | Zambia W | Spain Women's | Pressure | - | [61.0, 57.7] |  |
| +14.48 | +13.43 | 00:19:48.773 | Spain Women's | Spain Women's | Pass | - | [60.1, 20.7] |  |
| +15.44 | +14.39 | 00:19:49.737 | Spain Women's | Spain Women's | Ball Receipt* | - | [66.8, 9.8] |  |
| +15.44 | +14.39 | 00:19:49.737 | Spain Women's | Spain Women's | Carry | - | [66.8, 9.8] |  |
| +15.82 | +14.77 | 00:19:50.115 | Zambia W | Spain Women's | Pressure | - | [53.1, 70.9] |  |
| +16.62 | +15.57 | 00:19:50.913 | Spain Women's | Spain Women's | Pass | - | [63.8, 9.2] |  |
| +17.27 | +16.22 | 00:19:51.565 | Spain Women's | Spain Women's | Ball Receipt* | - | [59.1, 17.3] |  |
| +17.27 | +16.22 | 00:19:51.565 | Spain Women's | Spain Women's | Pass | - | [59.1, 17.3] |  |
| +18.44 | +17.39 | 00:19:52.739 | Spain Women's | Spain Women's | Ball Receipt* | - | [56.1, 7.7] |  |
| +18.44 | +17.39 | 00:19:52.739 | Spain Women's | Spain Women's | Carry | - | [56.1, 7.7] |  |
| +18.48 | +17.43 | 00:19:52.776 | Spain Women's | Spain Women's | Pass | - | [56.5, 7.9] |  |
| +19.54 | +18.49 | 00:19:53.831 | Spain Women's | Spain Women's | Ball Receipt* | - | [61.9, 18.3] |  |
| +19.54 | +18.49 | 00:19:53.831 | Spain Women's | Spain Women's | Carry | - | [61.9, 18.3] |  |

---

### Episode 55: `3857301_p161_27a6e4f3`
- **Match**: `3857301` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **Senegal** vs. Possession Team: **Qatar**
- **Initiation Action**: `Pressure` by **Cheikh Ahmadou Bamba Mbacke Dieng** at `00:41:36.341` (Turnover delay: 0.16s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=3.02s by Senegal. Harmless transition (opp max progression x=68.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.47 | -1.63 | 00:41:34.709 | Senegal | Senegal | Ball Receipt* | - | [56.7, 34.0] |  |
| -1.47 | -1.63 | 00:41:34.709 | Senegal | Senegal | Miscontrol | - | [56.7, 34.0] |  |
| +0.00 | -0.16 | 00:41:36.181 | Qatar | Qatar | Ball Recovery | - | [64.4, 55.1] | 🔄 **TURNOVER** |
| +0.00 | -0.16 | 00:41:36.181 | Qatar | Qatar | Carry | - | [64.4, 55.1] |  |
| +0.16 | +0.00 | 00:41:36.341 | Senegal | Qatar | Pressure | **YES** | [50.3, 27.5] | ⭐ **CP INITIATION** |
| +0.50 | +0.34 | 00:41:36.681 | Qatar | Qatar | Pass | - | [62.3, 55.1] |  |
| +2.04 | +1.88 | 00:41:38.220 | Qatar | Qatar | Ball Receipt* | - | [62.3, 44.4] |  |
| +2.04 | +1.88 | 00:41:38.220 | Qatar | Qatar | Pass | - | [62.3, 44.4] |  |
| +2.38 | +2.22 | 00:41:38.556 | Senegal | Qatar | Pressure | **YES** | [51.6, 28.2] |  |
| +2.89 | +2.73 | 00:41:39.068 | Qatar | Qatar | Ball Receipt* | - | [68.3, 48.9] |  |
| +2.89 | +2.73 | 00:41:39.068 | Qatar | Qatar | Carry | - | [68.3, 48.9] |  |
| +3.18 | +3.02 | 00:41:39.361 | Qatar | Qatar | Dispossessed | - | [68.9, 50.0] |  |
| +3.18 | +3.02 | 00:41:39.361 | Senegal | Senegal | Duel | **YES** | [51.2, 30.1] |  |
| +4.07 | +3.91 | 00:41:40.246 | Qatar | Senegal | Pressure | **YES** | [66.6, 49.3] |  |
| +4.22 | +4.06 | 00:41:40.404 | Senegal | Senegal | Pass | - | [55.4, 36.5] |  |
| +4.86 | +4.70 | 00:41:41.037 | Senegal | Senegal | Ball Receipt* | - | [57.8, 32.3] |  |
| +4.86 | +4.70 | 00:41:41.037 | Senegal | Senegal | Pass | - | [57.8, 32.3] |  |
| +5.63 | +5.47 | 00:41:41.809 | Senegal | Senegal | Ball Receipt* | - | [52.2, 35.5] |  |
| +5.63 | +5.47 | 00:41:41.809 | Senegal | Senegal | Carry | - | [52.2, 35.5] |  |
| +7.72 | +7.56 | 00:41:43.903 | Qatar | Senegal | Pressure | **YES** | [74.5, 54.1] |  |
| +7.98 | +7.82 | 00:41:44.157 | Senegal | Senegal | Pass | - | [46.5, 28.4] |  |
| +9.09 | +8.93 | 00:41:45.274 | Senegal | Senegal | Ball Receipt* | - | [43.7, 15.8] |  |
| +9.09 | +8.93 | 00:41:45.274 | Qatar | Qatar | Ball Recovery | - | [73.4, 63.2] |  |
| +9.09 | +8.93 | 00:41:45.274 | Qatar | Qatar | Carry | - | [73.4, 63.2] |  |
| +10.93 | +10.77 | 00:41:47.109 | Senegal | Qatar | Pressure | **YES** | [32.6, 21.8] |  |
| +11.51 | +11.35 | 00:41:47.689 | Senegal | Qatar | Foul Committed | **YES** | [28.3, 23.7] |  |
| +11.51 | +11.35 | 00:41:47.689 | Qatar | Qatar | Foul Won | - | [91.8, 56.4] |  |

---

### Episode 56: `3773415_p41_2b9a118c`
- **Match**: `3773415` | **Competition**: La Liga (2020/2021)
- **Context**: Period 1, Pressing Team: **Cádiz** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Jon Ander Garrido Moracia** at `00:21:19.575` (Turnover delay: 3.336s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.336s). Dangerous transition triggered by: Shot at dt=10.368s; Final third entry at dt=8.369s (initial x=24.5, max x=106.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.46 | -3.80 | 00:21:15.779 | Barcelona | Cádiz | Pressure | - | [22.3, 64.1] |  |
| +0.00 | -3.34 | 00:21:16.239 | Cádiz | Cádiz | Dispossessed | - | [95.6, 17.0] |  |
| +0.00 | -3.34 | 00:21:16.239 | Barcelona | Barcelona | Duel | - | [24.5, 63.1] | 🔄 **TURNOVER** |
| +1.25 | -2.08 | 00:21:17.493 | Barcelona | Barcelona | Ball Recovery | - | [33.1, 60.5] |  |
| +1.25 | -2.08 | 00:21:17.493 | Barcelona | Barcelona | Carry | - | [33.1, 60.5] |  |
| +3.34 | +0.00 | 00:21:19.575 | Cádiz | Barcelona | Pressure | **YES** | [68.8, 6.0] | ⭐ **CP INITIATION** |
| +4.14 | +0.81 | 00:21:20.382 | Barcelona | Barcelona | Pass | - | [54.0, 75.3] |  |
| +4.95 | +1.61 | 00:21:21.187 | Cádiz | Barcelona | Pressure | **YES** | [67.3, 1.8] |  |
| +5.20 | +1.87 | 00:21:21.440 | Barcelona | Barcelona | Ball Receipt* | - | [52.8, 78.3] |  |
| +5.20 | +1.87 | 00:21:21.440 | Barcelona | Barcelona | Carry | - | [52.8, 78.3] |  |
| +5.56 | +2.23 | 00:21:21.802 | Barcelona | Barcelona | Pass | - | [56.4, 78.4] |  |
| +6.52 | +3.18 | 00:21:22.755 | Barcelona | Barcelona | Ball Receipt* | - | [64.3, 77.5] |  |
| +6.52 | +3.18 | 00:21:22.755 | Barcelona | Barcelona | Carry | - | [64.3, 77.5] |  |
| +7.14 | +3.80 | 00:21:23.375 | Cádiz | Barcelona | Pressure | - | [53.4, 2.6] |  |
| +7.29 | +3.95 | 00:21:23.525 | Cádiz | Barcelona | Foul Committed | - | [49.3, 2.6] |  |
| +7.29 | +3.95 | 00:21:23.525 | Barcelona | Barcelona | Foul Won | - | [70.8, 77.5] |  |
| +7.29 | +3.95 | 00:21:23.525 | Barcelona | Barcelona | Carry | - | [70.8, 77.5] |  |
| +7.31 | +3.98 | 00:21:23.551 | Barcelona | Barcelona | Pass | - | [69.4, 77.5] |  |
| +8.60 | +5.26 | 00:21:24.834 | Barcelona | Barcelona | Ball Receipt* | - | [74.9, 74.3] |  |
| +8.60 | +5.26 | 00:21:24.834 | Barcelona | Barcelona | Carry | - | [74.9, 74.3] |  |
| +11.70 | +8.37 | 00:21:27.944 | Barcelona | Barcelona | Pass | - | [96.8, 50.1] |  |
| +12.93 | +9.60 | 00:21:29.174 | Barcelona | Barcelona | Ball Receipt* | - | [105.9, 33.9] |  |
| +12.93 | +9.60 | 00:21:29.174 | Barcelona | Barcelona | Carry | - | [105.9, 33.9] |  |
| +13.70 | +10.37 | 00:21:29.943 | Barcelona | Barcelona | Shot | - | [106.9, 29.7] |  |
| +13.79 | +10.46 | 00:21:30.032 | Cádiz | Barcelona | Block | - | [12.2, 49.4] |  |
| +13.89 | +10.56 | 00:21:30.132 | Cádiz | Barcelona | Goal Keeper | - | [3.5, 42.9] |  |

---

### Episode 57: `3869151_p99_64449636`
- **Match**: `3869151` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **Argentina** vs. Possession Team: **Argentina**
- **Initiation Action**: `Pressure` by **Julián Álvarez** at `00:18:53.197` (Turnover delay: 0.642s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.564s by Argentina. Harmless transition (opp max progression x=26.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.60 | -2.24 | 00:18:50.954 | Australia | Argentina | Pressure | - | [69.6, 22.1] |  |
| -1.19 | -1.83 | 00:18:51.365 | Argentina | Argentina | Ball Recovery | - | [50.7, 58.6] |  |
| +0.00 | -0.64 | 00:18:52.555 | Australia | Argentina | Ball Recovery | - | [75.2, 16.9] | 🔄 **TURNOVER** |
| +0.00 | -0.64 | 00:18:52.555 | Australia | Argentina | Carry | - | [75.2, 16.9] |  |
| +0.64 | +0.00 | 00:18:53.197 | Argentina | Argentina | Pressure | **YES** | [42.2, 56.9] | ⭐ **CP INITIATION** |
| +1.21 | +0.56 | 00:18:53.761 | Australia | Argentina | Pass | - | [77.9, 23.4] |  |
| +1.78 | +1.14 | 00:18:54.340 | Australia | Argentina | Ball Receipt* | - | [79.5, 30.0] |  |
| +1.78 | +1.14 | 00:18:54.340 | Australia | Argentina | Carry | - | [79.5, 30.0] |  |
| +2.13 | +1.49 | 00:18:54.689 | Argentina | Argentina | Pressure | **YES** | [37.5, 48.9] |  |
| +2.54 | +1.90 | 00:18:55.096 | Australia | Argentina | Dribble | - | [82.0, 32.0] |  |
| +2.54 | +1.90 | 00:18:55.096 | Argentina | Argentina | Duel | **YES** | [38.1, 48.1] |  |
| +2.54 | +1.90 | 00:18:55.096 | Argentina | Argentina | Carry | - | [38.1, 48.1] |  |
| +4.93 | +4.29 | 00:18:57.485 | Argentina | Argentina | Pass | - | [42.5, 33.0] |  |
| +5.68 | +5.03 | 00:18:58.231 | Australia | Argentina | Pressure | - | [60.9, 51.2] |  |
| +5.69 | +5.05 | 00:18:58.250 | Argentina | Argentina | Ball Receipt* | - | [59.3, 29.1] |  |
| +5.69 | +5.05 | 00:18:58.250 | Argentina | Argentina | Carry | - | [59.3, 29.1] |  |
| +6.39 | +5.75 | 00:18:58.942 | Australia | Argentina | Pressure | - | [63.4, 49.8] |  |
| +10.77 | +10.13 | 00:19:03.323 | Australia | Argentina | Pressure | - | [57.8, 32.6] |  |
| +14.21 | +13.57 | 00:19:06.762 | Argentina | Argentina | Dribble | - | [90.8, 44.3] |  |
| +14.21 | +13.57 | 00:19:06.762 | Australia | Argentina | Duel | - | [29.3, 35.8] |  |
| +15.88 | +15.24 | 00:19:08.434 | Argentina | Argentina | Pass | - | [92.0, 29.1] |  |
| +16.67 | +16.02 | 00:19:09.221 | Argentina | Argentina | Ball Receipt* | - | [99.7, 30.0] |  |
| +16.67 | +16.02 | 00:19:09.221 | Argentina | Argentina | Carry | - | [99.7, 30.0] |  |
| +17.04 | +16.40 | 00:19:09.594 | Australia | Argentina | Pressure | - | [14.2, 49.0] |  |
| +17.59 | +16.94 | 00:19:10.141 | Australia | Argentina | Dribbled Past | - | [15.0, 50.2] |  |
| +17.59 | +16.94 | 00:19:10.141 | Argentina | Argentina | Dribble | - | [105.1, 29.9] |  |
| +17.59 | +16.94 | 00:19:10.141 | Argentina | Argentina | Carry | - | [105.1, 29.9] |  |
| +18.18 | +17.54 | 00:19:10.735 | Australia | Argentina | Pressure | - | [15.0, 49.8] |  |
| +18.99 | +18.35 | 00:19:11.549 | Argentina | Argentina | Dribble | - | [105.4, 29.9] |  |
| +18.99 | +18.35 | 00:19:11.549 | Australia | Argentina | Duel | - | [14.7, 50.2] |  |

---

### Episode 58: `3940878_p37_2d18e125`
- **Match**: `3940878` | **Competition**: UEFA Euro (2024)
- **Context**: Period 1, Pressing Team: **Switzerland** vs. Possession Team: **Italy**
- **Initiation Action**: `Pressure` by **Remo Freuler** at `00:22:54.193` (Turnover delay: 3.834s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=3.834s). Harmless transition (opp max progression x=56.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.70 | -4.53 | 00:22:49.660 | Switzerland | Switzerland | Pass | - | [96.6, 34.0] |  |
| +0.00 | -3.83 | 00:22:50.359 | Switzerland | Switzerland | Ball Receipt* | - | [106.3, 46.8] |  |
| +0.00 | -3.83 | 00:22:50.359 | Italy | Italy | Ball Recovery | - | [16.6, 37.9] | 🔄 **TURNOVER** |
| +0.00 | -3.83 | 00:22:50.359 | Italy | Italy | Carry | - | [16.6, 37.9] |  |
| +1.23 | -2.60 | 00:22:51.589 | Italy | Italy | Pass | - | [18.4, 39.2] |  |
| +2.71 | -1.12 | 00:22:53.068 | Italy | Italy | Ball Receipt* | - | [36.3, 47.9] |  |
| +2.71 | -1.12 | 00:22:53.068 | Italy | Italy | Carry | - | [36.3, 47.9] |  |
| +3.83 | +0.00 | 00:22:54.193 | Switzerland | Italy | Pressure | **YES** | [84.8, 29.4] | ⭐ **CP INITIATION** |
| +6.04 | +2.21 | 00:22:56.403 | Italy | Italy | Pass | - | [46.8, 50.7] |  |
| +6.49 | +2.66 | 00:22:56.851 | Italy | Italy | Ball Receipt* | - | [52.9, 57.4] |  |
| +6.49 | +2.66 | 00:22:56.851 | Italy | Italy | Carry | - | [52.9, 57.4] |  |
| +7.17 | +3.34 | 00:22:57.531 | Switzerland | Italy | Pressure | - | [64.6, 22.2] |  |
| +7.68 | +3.85 | 00:22:58.041 | Italy | Italy | Pass | - | [51.6, 56.8] |  |
| +9.46 | +5.62 | 00:22:59.816 | Italy | Italy | Ball Receipt* | - | [56.5, 32.1] |  |
| +9.46 | +5.62 | 00:22:59.816 | Switzerland | Switzerland | Ball Recovery | - | [69.2, 42.7] |  |
| +9.46 | +5.62 | 00:22:59.816 | Switzerland | Switzerland | Carry | - | [69.2, 42.7] |  |
| +11.65 | +7.81 | 00:23:02.005 | Switzerland | Switzerland | Pass | - | [73.3, 28.6] |  |
| +13.27 | +9.44 | 00:23:03.630 | Switzerland | Switzerland | Ball Receipt* | - | [60.5, 19.4] |  |
| +13.27 | +9.44 | 00:23:03.630 | Switzerland | Switzerland | Carry | - | [60.5, 19.4] |  |
| +14.35 | +10.51 | 00:23:04.707 | Switzerland | Switzerland | Pass | - | [61.1, 19.4] |  |
| +15.33 | +11.49 | 00:23:05.685 | Switzerland | Switzerland | Ball Receipt* | - | [68.5, 15.6] |  |
| +15.33 | +11.49 | 00:23:05.685 | Switzerland | Switzerland | Carry | - | [68.5, 15.6] |  |
| +17.87 | +14.03 | 00:23:08.225 | Switzerland | Switzerland | Pass | - | [75.1, 12.5] |  |
| +19.00 | +15.16 | 00:23:09.358 | Switzerland | Switzerland | Ball Receipt* | - | [78.2, 3.8] |  |
| +19.00 | +15.16 | 00:23:09.358 | Switzerland | Switzerland | Carry | - | [78.2, 3.8] |  |
| +20.00 | +16.17 | 00:23:10.361 | Switzerland | Switzerland | Pass | - | [75.1, 6.6] |  |
| +21.53 | +17.70 | 00:23:11.891 | Switzerland | Switzerland | Ball Receipt* | - | [59.3, 17.4] |  |
| +21.53 | +17.70 | 00:23:11.891 | Switzerland | Switzerland | Carry | - | [59.3, 17.4] |  |
| +22.12 | +18.29 | 00:23:12.483 | Switzerland | Switzerland | Pass | - | [58.2, 18.1] |  |
| +23.51 | +19.67 | 00:23:13.866 | Switzerland | Switzerland | Ball Receipt* | - | [55.9, 34.5] |  |
| +23.51 | +19.67 | 00:23:13.866 | Switzerland | Switzerland | Carry | - | [55.9, 34.5] |  |

---

### Episode 59: `3902240_p88_62481c22`
- **Match**: `3902240` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Spain Women's** vs. Possession Team: **Spain Women's**
- **Initiation Action**: `Pass` by **Irene Paredes Hernandez** at `00:39:53.881` (Turnover delay: 4.448s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.241s by Spain Women's. Harmless transition (opp max progression x=35.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.57 | -7.02 | 00:39:46.863 | Netherlands Women's | Netherlands Women's | Pass | - | [39.4, 44.9] |  |
| +0.00 | -4.45 | 00:39:49.433 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [51.5, 10.1] | 🔄 **TURNOVER** |
| +0.00 | -4.45 | 00:39:49.433 | Netherlands Women's | Netherlands Women's | Carry | - | [51.5, 10.1] |  |
| +2.46 | -1.99 | 00:39:51.889 | Netherlands Women's | Netherlands Women's | Pass | - | [51.7, 10.1] |  |
| +4.45 | +0.00 | 00:39:53.881 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [86.8, 34.0] |  |
| +4.45 | +0.00 | 00:39:53.881 | Spain Women's | Spain Women's | Pass | **YES** | [35.5, 50.8] | ⭐ **CP INITIATION** |
| +5.69 | +1.24 | 00:39:55.122 | Netherlands Women's | Spain Women's | Pressure | **YES** | [67.7, 27.0] |  |
| +5.86 | +1.41 | 00:39:55.294 | Spain Women's | Spain Women's | Ball Receipt* | - | [51.6, 54.0] |  |
| +5.86 | +1.41 | 00:39:55.294 | Spain Women's | Spain Women's | Pass | - | [52.5, 56.6] |  |
| +8.09 | +3.64 | 00:39:57.524 | Spain Women's | Spain Women's | Ball Receipt* | - | [62.4, 37.0] |  |
| +8.09 | +3.64 | 00:39:57.524 | Spain Women's | Spain Women's | Pass | - | [62.4, 37.0] |  |
| +10.33 | +5.88 | 00:39:59.761 | Spain Women's | Spain Women's | Ball Receipt* | - | [74.5, 65.2] |  |
| +19.31 | +14.87 | 00:40:08.747 | Netherlands Women's | Netherlands Women's | Pass | - | [52.5, 0.1] |  |
| +19.93 | +15.49 | 00:40:09.368 | Spain Women's | Netherlands Women's | Pressure | - | [56.8, 63.6] |  |
| +20.18 | +15.73 | 00:40:09.609 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [61.5, 16.0] |  |
| +20.18 | +15.73 | 00:40:09.609 | Netherlands Women's | Netherlands Women's | Carry | - | [61.5, 16.0] |  |
| +20.39 | +15.95 | 00:40:09.828 | Spain Women's | Netherlands Women's | Pressure | - | [58.6, 64.5] |  |
| +21.06 | +16.61 | 00:40:10.493 | Netherlands Women's | Netherlands Women's | Pass | - | [60.3, 15.6] |  |
| +22.24 | +17.79 | 00:40:11.675 | Netherlands Women's | Netherlands Women's | Ball Receipt* | - | [42.6, 16.0] |  |
| +22.24 | +17.79 | 00:40:11.675 | Netherlands Women's | Netherlands Women's | Carry | - | [42.6, 16.0] |  |
| +23.36 | +18.91 | 00:40:12.795 | Netherlands Women's | Netherlands Women's | Pass | - | [39.4, 16.7] |  |

---

### Episode 60: `3835322_p161_589f104e`
- **Match**: `3835322` | **Competition**: UEFA Women's Euro (2022)
- **Context**: Period 2, Pressing Team: **Denmark Women's** vs. Possession Team: **Germany Women's**
- **Initiation Action**: `Pressure` by **Sofie Junge Pedersen** at `00:28:34.128` (Turnover delay: 3.209s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.209s). Dangerous transition triggered by: Final third entry at dt=10.026s (initial x=19.3, max x=100.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.94 | -6.15 | 00:28:27.979 | Denmark Women's | Denmark Women's | Pass | - | [54.8, 68.8] |  |
| +0.00 | -3.21 | 00:28:30.919 | Germany Women's | Denmark Women's | Clearance | - | [16.0, 33.8] | 🔄 **TURNOVER** |
| +1.82 | -1.38 | 00:28:32.744 | Germany Women's | Germany Women's | Pass | - | [19.3, 26.1] |  |
| +3.17 | -0.03 | 00:28:34.093 | Germany Women's | Germany Women's | Ball Receipt* | - | [33.0, 23.2] |  |
| +3.17 | -0.03 | 00:28:34.093 | Germany Women's | Germany Women's | Carry | - | [33.0, 23.2] |  |
| +3.21 | +0.00 | 00:28:34.128 | Denmark Women's | Germany Women's | Pressure | **YES** | [86.1, 57.1] | ⭐ **CP INITIATION** |
| +4.45 | +1.25 | 00:28:35.373 | Germany Women's | Germany Women's | Pass | - | [35.4, 20.8] |  |
| +5.16 | +1.95 | 00:28:36.080 | Denmark Women's | Germany Women's | Pressure | **YES** | [78.9, 59.8] |  |
| +5.20 | +1.99 | 00:28:36.121 | Germany Women's | Germany Women's | Ball Receipt* | - | [43.2, 17.9] |  |
| +5.20 | +1.99 | 00:28:36.121 | Germany Women's | Germany Women's | Pass | - | [38.1, 23.9] |  |
| +6.69 | +3.48 | 00:28:37.605 | Germany Women's | Germany Women's | Ball Receipt* | - | [36.4, 29.2] |  |
| +6.69 | +3.48 | 00:28:37.605 | Germany Women's | Germany Women's | Pass | - | [35.9, 38.2] |  |
| +9.33 | +6.12 | 00:28:40.251 | Germany Women's | Germany Women's | Duel | - | [71.6, 25.9] |  |
| +9.33 | +6.12 | 00:28:40.251 | Denmark Women's | Germany Women's | Clearance | - | [48.5, 54.2] |  |
| +10.88 | +7.68 | 00:28:41.804 | Germany Women's | Germany Women's | Pass | - | [71.6, 30.7] |  |
| +13.23 | +10.03 | 00:28:44.154 | Germany Women's | Germany Women's | Ball Receipt* | - | [100.4, 22.7] |  |

---

### Episode 61: `3938644_p43_c60d20ea`
- **Match**: `3938644` | **Competition**: UEFA Euro (2024)
- **Context**: Period 1, Pressing Team: **Portugal** vs. Possession Team: **Georgia**
- **Initiation Action**: `Pressure` by **João Maria Lobo Alves Palhinha Gonçalves** at `00:28:50.852` (Turnover delay: 2.642s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.642s). Harmless transition (opp max progression x=57.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.64 | -4.29 | 00:28:46.567 | Portugal | Portugal | Pass | - | [70.7, 29.8] |  |
| +0.00 | -2.64 | 00:28:48.210 | Portugal | Portugal | Ball Receipt* | - | [98.8, 15.7] |  |
| +0.00 | -2.64 | 00:28:48.210 | Georgia | Georgia | Pass | **YES** | [23.0, 61.4] | 🔄 **TURNOVER** |
| +1.21 | -1.43 | 00:28:49.421 | Georgia | Georgia | Ball Receipt* | - | [30.3, 63.3] |  |
| +1.21 | -1.43 | 00:28:49.421 | Georgia | Georgia | Carry | - | [30.3, 63.3] |  |
| +2.64 | +0.00 | 00:28:50.852 | Portugal | Georgia | Pressure | **YES** | [87.6, 19.1] | ⭐ **CP INITIATION** |
| +3.25 | +0.61 | 00:28:51.461 | Georgia | Georgia | Pass | - | [29.1, 61.4] |  |
| +3.90 | +1.26 | 00:28:52.113 | Georgia | Georgia | Ball Receipt* | - | [27.4, 53.9] |  |
| +3.90 | +1.26 | 00:28:52.113 | Georgia | Georgia | Carry | - | [27.4, 53.9] |  |
| +3.92 | +1.28 | 00:28:52.129 | Georgia | Georgia | Pass | - | [27.4, 54.0] |  |
| +4.86 | +2.22 | 00:28:53.070 | Georgia | Georgia | Ball Receipt* | - | [14.2, 59.1] |  |
| +4.86 | +2.22 | 00:28:53.070 | Georgia | Georgia | Carry | - | [14.2, 59.1] |  |
| +5.45 | +2.81 | 00:28:53.662 | Portugal | Georgia | Pressure | - | [104.6, 17.4] |  |
| +6.14 | +3.50 | 00:28:54.352 | Georgia | Georgia | Pass | - | [11.0, 55.7] |  |
| +7.01 | +4.37 | 00:28:55.217 | Portugal | Georgia | Pressure | - | [110.5, 40.7] |  |
| +7.32 | +4.68 | 00:28:55.530 | Georgia | Georgia | Ball Receipt* | - | [2.7, 43.1] |  |
| +7.32 | +4.68 | 00:28:55.530 | Georgia | Georgia | Carry | - | [2.7, 43.1] |  |
| +7.52 | +4.88 | 00:28:55.727 | Georgia | Georgia | Pass | - | [3.7, 44.0] |  |
| +10.36 | +7.71 | 00:28:58.566 | Portugal | Georgia | Pass | - | [63.1, 15.7] |  |
| +11.83 | +9.19 | 00:29:00.043 | Portugal | Georgia | Ball Receipt* | - | [76.1, 24.8] |  |
| +11.83 | +9.19 | 00:29:00.043 | Georgia | Georgia | Pass | - | [48.2, 62.7] |  |
| +12.83 | +10.19 | 00:29:01.039 | Portugal | Georgia | Pressure | - | [68.4, 13.4] |  |
| +13.10 | +10.45 | 00:29:01.307 | Georgia | Georgia | Ball Receipt* | - | [57.0, 66.4] |  |
| +13.10 | +10.45 | 00:29:01.307 | Georgia | Georgia | Carry | - | [57.0, 66.4] |  |
| +13.28 | +10.64 | 00:29:01.488 | Georgia | Georgia | Dispossessed | - | [55.8, 66.7] |  |
| +13.28 | +10.64 | 00:29:01.488 | Portugal | Portugal | Duel | **YES** | [64.3, 13.4] |  |
| +13.28 | +10.64 | 00:29:01.488 | Portugal | Portugal | Carry | - | [64.3, 13.4] |  |
| +15.10 | +12.46 | 00:29:03.311 | Portugal | Portugal | Pass | - | [51.8, 15.1] |  |
| +17.35 | +14.71 | 00:29:05.558 | Portugal | Portugal | Ball Receipt* | - | [25.1, 32.6] |  |
| +17.35 | +14.71 | 00:29:05.558 | Portugal | Portugal | Carry | - | [25.1, 32.6] |  |
| +18.57 | +15.93 | 00:29:06.779 | Portugal | Portugal | Pass | - | [25.6, 35.0] |  |
| +20.37 | +17.73 | 00:29:08.583 | Portugal | Portugal | Ball Receipt* | - | [42.1, 57.0] |  |
| +20.37 | +17.73 | 00:29:08.583 | Portugal | Portugal | Carry | - | [42.1, 57.0] |  |
| +21.40 | +18.76 | 00:29:09.609 | Portugal | Portugal | Pass | - | [43.8, 57.7] |  |

---

### Episode 62: `3835322_p99_217d424a`
- **Match**: `3835322` | **Competition**: UEFA Women's Euro (2022)
- **Context**: Period 1, Pressing Team: **Denmark Women's** vs. Possession Team: **Germany Women's**
- **Initiation Action**: `Pressure` by **Sofie Junge Pedersen** at `00:44:20.938` (Turnover delay: 2.377s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.377s). Dangerous transition triggered by: Final third entry at dt=0.54s (initial x=68.9, max x=89.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.69 | -5.06 | 00:44:15.875 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [29.5, 68.2] |  |
| -2.69 | -5.06 | 00:44:15.875 | Denmark Women's | Denmark Women's | Carry | - | [29.5, 68.2] |  |
| -2.64 | -5.02 | 00:44:15.923 | Denmark Women's | Denmark Women's | Pass | - | [29.9, 67.1] |  |
| -1.75 | -4.13 | 00:44:16.808 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [27.2, 77.4] |  |
| -1.75 | -4.13 | 00:44:16.808 | Denmark Women's | Denmark Women's | Carry | - | [27.2, 77.4] |  |
| -1.66 | -4.04 | 00:44:16.900 | Denmark Women's | Denmark Women's | Pass | - | [27.2, 77.2] |  |
| +0.00 | -2.38 | 00:44:18.561 | Germany Women's | Germany Women's | Pass | - | [68.9, 15.4] | 🔄 **TURNOVER** |
| +1.88 | -0.49 | 00:44:20.445 | Germany Women's | Germany Women's | Ball Receipt* | - | [83.2, 33.1] |  |
| +1.88 | -0.49 | 00:44:20.445 | Germany Women's | Germany Women's | Carry | - | [83.2, 33.1] |  |
| +1.92 | -0.46 | 00:44:20.481 | Germany Women's | Germany Women's | Pass | - | [85.0, 34.7] |  |
| +2.38 | +0.00 | 00:44:20.938 | Denmark Women's | Germany Women's | Pressure | **YES** | [30.8, 57.9] | ⭐ **CP INITIATION** |
| +2.92 | +0.54 | 00:44:21.478 | Germany Women's | Germany Women's | Ball Receipt* | - | [89.3, 22.2] |  |
| +2.92 | +0.54 | 00:44:21.478 | Germany Women's | Germany Women's | Carry | - | [89.3, 22.2] |  |
| +3.05 | +0.67 | 00:44:21.607 | Germany Women's | Germany Women's | Dispossessed | - | [87.1, 24.7] |  |
| +3.05 | +0.67 | 00:44:21.607 | Denmark Women's | Germany Women's | Duel | **YES** | [33.0, 55.4] |  |
| +4.29 | +1.91 | 00:44:22.847 | Germany Women's | Germany Women's | Pass | - | [87.0, 17.2] |  |
| +5.22 | +2.84 | 00:44:23.777 | Germany Women's | Germany Women's | Ball Receipt* | - | [80.6, 33.8] |  |
| +5.22 | +2.84 | 00:44:23.777 | Germany Women's | Germany Women's | Carry | - | [80.6, 33.8] |  |
| +6.60 | +4.22 | 00:44:25.161 | Denmark Women's | Germany Women's | Pressure | - | [37.3, 47.9] |  |
| +7.67 | +5.29 | 00:44:26.231 | Germany Women's | Germany Women's | Dispossessed | - | [86.9, 47.7] |  |
| +7.67 | +5.29 | 00:44:26.231 | Denmark Women's | Germany Women's | Duel | - | [33.2, 32.4] |  |
| +7.67 | +5.29 | 00:44:26.231 | Denmark Women's | Germany Women's | Carry | - | [33.2, 32.4] |  |
| +14.36 | +11.98 | 00:44:32.921 | Denmark Women's | Germany Women's | Pass | - | [61.0, 22.8] |  |
| +15.68 | +13.31 | 00:44:34.244 | Denmark Women's | Germany Women's | Pressure | - | [81.6, 11.1] |  |
| +15.92 | +13.55 | 00:44:34.484 | Denmark Women's | Germany Women's | Ball Receipt* | - | [78.1, 14.3] |  |
| +15.92 | +13.55 | 00:44:34.484 | Germany Women's | Germany Women's | Interception | - | [36.0, 65.4] |  |
| +15.92 | +13.55 | 00:44:34.484 | Germany Women's | Germany Women's | Carry | - | [36.0, 65.4] |  |
| +17.40 | +15.02 | 00:44:35.962 | Germany Women's | Germany Women's | Pass | - | [32.4, 73.4] |  |
| +18.43 | +16.06 | 00:44:36.996 | Germany Women's | Germany Women's | Ball Receipt* | - | [44.1, 74.8] |  |
| +18.43 | +16.06 | 00:44:36.996 | Germany Women's | Germany Women's | Carry | - | [44.1, 74.8] |  |
| +18.52 | +16.14 | 00:44:37.082 | Denmark Women's | Germany Women's | Pressure | - | [74.0, 5.3] |  |
| +18.97 | +16.60 | 00:44:37.534 | Germany Women's | Germany Women's | Dribble | - | [46.1, 75.2] |  |
| +18.97 | +16.60 | 00:44:37.534 | Denmark Women's | Germany Women's | Duel | - | [74.0, 4.9] |  |

---

### Episode 63: `3877090_p52_ebe02233`
- **Match**: `3877090` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Inter Miami** vs. Possession Team: **LAFC**
- **Initiation Action**: `Pressure` by **Diego Alexander Gómez Amarilla** at `00:27:15.727` (Turnover delay: 3.796s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=3.796s). Harmless transition (opp max progression x=113.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.46 | -6.26 | 00:27:09.467 | LAFC | Inter Miami | Ball Receipt* | - | [84.3, 47.2] |  |
| -2.46 | -6.26 | 00:27:09.467 | Inter Miami | Inter Miami | Pass | - | [25.0, 32.1] |  |
| -2.46 | -6.26 | 00:27:09.467 | LAFC | Inter Miami | Duel | - | [95.1, 48.0] |  |
| +0.00 | -3.80 | 00:27:11.931 | Inter Miami | Inter Miami | Ball Receipt* | - | [33.3, 30.9] |  |
| +0.00 | -3.80 | 00:27:11.931 | LAFC | LAFC | Ball Recovery | - | [84.1, 53.7] | 🔄 **TURNOVER** |
| +0.00 | -3.80 | 00:27:11.931 | LAFC | LAFC | Carry | - | [84.1, 53.7] |  |
| +0.44 | -3.35 | 00:27:12.375 | LAFC | LAFC | Pass | - | [82.7, 60.5] |  |
| +1.90 | -1.90 | 00:27:13.828 | LAFC | LAFC | Ball Receipt* | - | [95.2, 63.1] |  |
| +1.90 | -1.90 | 00:27:13.828 | LAFC | LAFC | Carry | - | [95.2, 63.1] |  |
| +3.80 | +0.00 | 00:27:15.727 | Inter Miami | LAFC | Pressure | **YES** | [32.2, 16.2] | ⭐ **CP INITIATION** |
| +4.16 | +0.37 | 00:27:16.095 | LAFC | LAFC | Pass | - | [89.4, 65.5] |  |
| +5.93 | +2.13 | 00:27:17.860 | LAFC | LAFC | Ball Receipt* | - | [87.9, 73.7] |  |
| +5.93 | +2.13 | 00:27:17.860 | LAFC | LAFC | Carry | - | [87.9, 73.7] |  |
| +7.98 | +4.19 | 00:27:19.913 | LAFC | LAFC | Pass | - | [98.0, 68.9] |  |
| +9.37 | +5.57 | 00:27:21.299 | LAFC | LAFC | Ball Receipt* | - | [109.5, 35.9] |  |
| +9.37 | +5.57 | 00:27:21.299 | LAFC | LAFC | Carry | - | [109.5, 35.9] |  |
| +9.38 | +5.58 | 00:27:21.309 | LAFC | LAFC | Miscontrol | - | [109.5, 35.9] |  |
| +12.38 | +8.58 | 00:27:24.309 | LAFC | LAFC | Ball Recovery | - | [113.2, 15.1] |  |
| +12.38 | +8.58 | 00:27:24.309 | LAFC | LAFC | Carry | - | [113.2, 15.1] |  |
| +12.84 | +9.05 | 00:27:24.775 | LAFC | LAFC | Pass | - | [112.4, 7.2] |  |
| +14.34 | +10.54 | 00:27:26.267 | LAFC | LAFC | Ball Receipt* | - | [98.9, 4.0] |  |
| +14.34 | +10.54 | 00:27:26.267 | LAFC | LAFC | Carry | - | [98.9, 4.0] |  |
| +16.03 | +12.23 | 00:27:27.962 | LAFC | LAFC | Pass | - | [99.4, 4.5] |  |
| +16.89 | +13.10 | 00:27:28.824 | LAFC | LAFC | Ball Receipt* | - | [93.9, 10.5] |  |
| +16.89 | +13.10 | 00:27:28.824 | LAFC | LAFC | Carry | - | [93.9, 10.5] |  |
| +18.57 | +14.78 | 00:27:30.505 | Inter Miami | LAFC | Pressure | - | [24.9, 62.2] |  |
| +19.08 | +15.28 | 00:27:31.009 | LAFC | LAFC | Pass | - | [94.0, 23.0] |  |
| +20.02 | +16.22 | 00:27:31.950 | LAFC | LAFC | Ball Receipt* | - | [105.2, 36.7] |  |
| +20.02 | +16.22 | 00:27:31.950 | LAFC | LAFC | Carry | - | [105.2, 36.7] |  |
| +21.00 | +17.21 | 00:27:32.935 | LAFC | LAFC | Pass | - | [105.2, 36.7] |  |
| +21.51 | +17.71 | 00:27:33.440 | LAFC | LAFC | Ball Receipt* | - | [106.9, 35.2] |  |
| +21.51 | +17.71 | 00:27:33.440 | LAFC | LAFC | Miscontrol | - | [106.9, 35.2] |  |
| +22.92 | +19.12 | 00:27:34.851 | Inter Miami | LAFC | Pass | - | [9.8, 46.0] |  |

---

### Episode 64: `3869486_p31_6271d2d1`
- **Match**: `3869486` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 1, Pressing Team: **Portugal** vs. Possession Team: **Morocco**
- **Initiation Action**: `Pressure` by **Bernardo Mota Veiga de Carvalho e Silva** at `00:19:10.616` (Turnover delay: 0.222s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=0.222s). Harmless transition (opp max progression x=17.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.86 | -2.08 | 00:19:08.538 | Portugal | Portugal | Ball Receipt* | - | [111.5, 63.5] |  |
| -1.86 | -2.08 | 00:19:08.538 | Portugal | Portugal | Duel | - | [109.1, 65.0] |  |
| -1.86 | -2.08 | 00:19:08.538 | Morocco | Portugal | Pass | - | [11.0, 15.1] |  |
| -0.65 | -0.87 | 00:19:09.742 | Morocco | Portugal | Ball Receipt* | - | [18.0, 8.5] |  |
| -0.65 | -0.87 | 00:19:09.742 | Portugal | Portugal | Ball Recovery | - | [102.1, 72.6] |  |
| +0.00 | -0.22 | 00:19:10.394 | Morocco | Morocco | Ball Recovery | - | [17.6, 8.4] | 🔄 **TURNOVER** |
| +0.00 | -0.22 | 00:19:10.394 | Morocco | Morocco | Carry | - | [17.6, 8.4] |  |
| +0.22 | +0.00 | 00:19:10.616 | Portugal | Morocco | Pressure | **YES** | [106.3, 74.8] | ⭐ **CP INITIATION** |
| +1.59 | +1.37 | 00:19:11.986 | Morocco | Morocco | Pass | - | [9.3, 4.0] |  |
| +2.00 | +1.78 | 00:19:12.397 | Morocco | Morocco | Ball Receipt* | - | [7.8, 12.9] |  |
| +2.00 | +1.78 | 00:19:12.397 | Morocco | Morocco | Carry | - | [7.8, 12.9] |  |
| +5.05 | +4.82 | 00:19:15.439 | Morocco | Morocco | Pass | - | [3.1, 9.1] |  |
| +5.57 | +5.35 | 00:19:15.966 | Morocco | Morocco | Ball Receipt* | - | [6.3, 1.4] |  |
| +5.57 | +5.35 | 00:19:15.966 | Morocco | Morocco | Carry | - | [6.3, 1.4] |  |
| +6.55 | +6.32 | 00:19:16.939 | Portugal | Morocco | Dribbled Past | - | [113.8, 78.5] |  |
| +6.55 | +6.32 | 00:19:16.939 | Morocco | Morocco | Dribble | - | [6.3, 1.6] |  |
| +6.55 | +6.32 | 00:19:16.939 | Morocco | Morocco | Carry | - | [6.3, 1.6] |  |
| +7.40 | +7.18 | 00:19:17.795 | Portugal | Morocco | Pressure | - | [109.0, 75.5] |  |
| +8.30 | +8.08 | 00:19:18.695 | Portugal | Morocco | Foul Committed | - | [104.1, 76.3] |  |
| +8.30 | +8.08 | 00:19:18.695 | Morocco | Morocco | Foul Won | - | [16.0, 3.8] |  |

---

### Episode 65: `3802699_p86_93134b75`
- **Match**: `3802699` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 2, Pressing Team: **Lille** vs. Possession Team: **Paris Saint-Germain**
- **Initiation Action**: `Pressure` by **Miguel Ângelo da Silva Rocha** at `00:00:13.936` (Turnover delay: 1.536s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.536s). Harmless transition (opp max progression x=69.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.49 | -4.02 | 00:00:09.914 | Lille | Lille | Pass | - | [45.6, 75.1] |  |
| -1.47 | -3.01 | 00:00:10.925 | Lille | Lille | Ball Receipt* | - | [62.1, 68.6] |  |
| -1.47 | -3.01 | 00:00:10.925 | Lille | Lille | Carry | - | [62.1, 68.6] |  |
| -0.58 | -2.12 | 00:00:11.817 | Paris Saint-Germain | Lille | Pressure | - | [56.1, 11.5] |  |
| +0.00 | -1.54 | 00:00:12.400 | Lille | Lille | Dribble | - | [62.1, 69.0] |  |
| +0.00 | -1.54 | 00:00:12.400 | Paris Saint-Germain | Paris Saint-Germain | Duel | **YES** | [58.0, 11.1] | 🔄 **TURNOVER** |
| +0.59 | -0.95 | 00:00:12.986 | Paris Saint-Germain | Paris Saint-Germain | Ball Recovery | - | [58.1, 14.9] |  |
| +1.54 | +0.00 | 00:00:13.936 | Lille | Paris Saint-Germain | Pressure | **YES** | [58.6, 62.1] | ⭐ **CP INITIATION** |
| +1.95 | +0.42 | 00:00:14.352 | Paris Saint-Germain | Paris Saint-Germain | Ball Recovery | - | [61.1, 14.9] |  |
| +1.95 | +0.42 | 00:00:14.352 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [61.1, 14.9] |  |
| +3.74 | +2.20 | 00:00:16.140 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [56.6, 22.2] |  |
| +4.47 | +2.93 | 00:00:16.871 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [64.0, 22.2] |  |
| +4.47 | +2.93 | 00:00:16.871 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [64.0, 22.2] |  |
| +5.19 | +3.66 | 00:00:17.592 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [64.9, 22.5] |  |
| +6.29 | +4.75 | 00:00:18.688 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [68.6, 5.5] |  |
| +6.29 | +4.75 | 00:00:18.688 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [68.6, 5.5] |  |
| +7.22 | +5.68 | 00:00:19.618 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [69.0, 5.6] |  |
| +8.09 | +6.56 | 00:00:20.494 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [52.0, 9.4] |  |
| +8.09 | +6.56 | 00:00:20.494 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [52.0, 9.4] |  |
| +9.72 | +8.18 | 00:00:22.118 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [53.5, 12.8] |  |
| +11.38 | +9.84 | 00:00:23.776 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [40.5, 42.0] |  |
| +11.38 | +9.84 | 00:00:23.776 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [40.5, 42.0] |  |
| +13.01 | +11.47 | 00:00:25.407 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [45.1, 48.4] |  |
| +14.02 | +12.48 | 00:00:26.419 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [55.1, 66.8] |  |
| +14.02 | +12.48 | 00:00:26.419 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [55.1, 66.8] |  |
| +15.54 | +14.01 | 00:00:27.945 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [54.7, 67.0] |  |
| +16.26 | +14.73 | 00:00:28.663 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [59.4, 56.7] |  |
| +16.26 | +14.73 | 00:00:28.663 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [59.4, 56.7] |  |
| +16.27 | +14.73 | 00:00:28.667 | Lille | Paris Saint-Germain | Pressure | - | [56.1, 22.0] |  |
| +17.06 | +15.52 | 00:00:29.458 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [57.0, 56.8] |  |
| +18.18 | +16.64 | 00:00:30.576 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [44.7, 43.4] |  |
| +18.18 | +16.64 | 00:00:30.576 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [44.7, 43.4] |  |
| +19.18 | +17.64 | 00:00:31.576 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [44.6, 42.8] |  |
| +20.73 | +19.20 | 00:00:33.135 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [56.1, 18.4] |  |
| +20.73 | +19.20 | 00:00:33.135 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [56.1, 18.4] |  |

---

### Episode 66: `3893834_p127_6e22c6aa`
- **Match**: `3893834` | **Competition**: Women's World Cup (2023)
- **Context**: Period 2, Pressing Team: **Morocco Women's** vs. Possession Team: **Colombia Women's**
- **Initiation Action**: `Foul Committed` by **Hanane Aït El Haj** at `00:10:42.962` (Turnover delay: 2.249s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.249s). Harmless transition (opp max progression x=26.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.79 | -5.04 | 00:10:37.918 | Morocco Women's | Morocco Women's | Pass | - | [80.7, 76.3] |  |
| -2.64 | -4.88 | 00:10:38.077 | Morocco Women's | Morocco Women's | Ball Receipt* | - | [87.5, 75.0] |  |
| -2.64 | -4.88 | 00:10:38.077 | Colombia Women's | Morocco Women's | Interception | - | [35.3, 3.4] |  |
| -2.30 | -4.55 | 00:10:38.410 | Morocco Women's | Morocco Women's | Ball Recovery | - | [85.2, 77.4] |  |
| -2.30 | -4.55 | 00:10:38.410 | Morocco Women's | Morocco Women's | Carry | - | [85.2, 77.4] |  |
| -1.68 | -3.93 | 00:10:39.031 | Colombia Women's | Morocco Women's | Pressure | - | [33.8, 2.7] |  |
| -1.34 | -3.59 | 00:10:39.371 | Morocco Women's | Morocco Women's | Pass | - | [86.3, 77.2] |  |
| -0.34 | -2.59 | 00:10:40.376 | Morocco Women's | Morocco Women's | Pressure | - | [94.4, 77.8] |  |
| +0.00 | -2.25 | 00:10:40.713 | Morocco Women's | Morocco Women's | Ball Receipt* | - | [94.4, 77.8] |  |
| +0.00 | -2.25 | 00:10:40.713 | Colombia Women's | Colombia Women's | Interception | **YES** | [26.8, 2.9] | 🔄 **TURNOVER** |
| +0.00 | -2.25 | 00:10:40.713 | Colombia Women's | Colombia Women's | Carry | - | [26.8, 2.9] |  |
| +2.25 | +0.00 | 00:10:42.962 | Morocco Women's | Colombia Women's | Foul Committed | **YES** | [94.4, 75.4] | ⭐ **CP INITIATION** |
| +2.25 | +0.00 | 00:10:42.962 | Colombia Women's | Colombia Women's | Foul Won | - | [25.7, 4.7] |  |
| +13.53 | +11.28 | 00:10:54.239 | Colombia Women's | Colombia Women's | Pass | - | [22.4, 7.6] |  |
| +15.12 | +12.87 | 00:10:55.832 | Colombia Women's | Colombia Women's | Ball Receipt* | - | [20.8, 23.1] |  |
| +15.12 | +12.87 | 00:10:55.832 | Colombia Women's | Colombia Women's | Carry | - | [20.8, 23.1] |  |
| +16.92 | +14.67 | 00:10:57.628 | Colombia Women's | Colombia Women's | Pass | - | [26.0, 29.2] |  |
| +18.78 | +16.53 | 00:10:59.488 | Colombia Women's | Colombia Women's | Ball Receipt* | - | [27.1, 54.8] |  |
| +18.78 | +16.53 | 00:10:59.488 | Colombia Women's | Colombia Women's | Carry | - | [27.1, 54.8] |  |
| +20.16 | +17.91 | 00:11:00.875 | Colombia Women's | Colombia Women's | Pass | - | [29.9, 58.9] |  |
| +21.96 | +19.71 | 00:11:02.675 | Colombia Women's | Colombia Women's | Ball Receipt* | - | [37.1, 78.2] |  |
| +21.96 | +19.71 | 00:11:02.675 | Colombia Women's | Colombia Women's | Carry | - | [37.1, 78.2] |  |

---

### Episode 67: `3773586_p146_fe107d6e`
- **Match**: `3773586` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Granada** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Foul Committed` by **Adrián Marín Gómez** at `00:44:51.948` (Turnover delay: 0.461s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=0.461s). Harmless transition (opp max progression x=12.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.91 | -2.37 | 00:44:49.582 | Granada | Granada | Ball Receipt* | - | [100.7, 5.4] |  |
| -1.91 | -2.37 | 00:44:49.582 | Granada | Granada | Carry | - | [100.7, 5.4] |  |
| -0.38 | -0.84 | 00:44:51.107 | Granada | Granada | Miscontrol | - | [103.8, 7.0] |  |
| -0.10 | -0.57 | 00:44:51.383 | Granada | Granada | Pressure | - | [105.4, 8.0] |  |
| +0.00 | -0.46 | 00:44:51.487 | Barcelona | Barcelona | Ball Recovery | - | [12.8, 71.0] | 🔄 **TURNOVER** |
| +0.00 | -0.46 | 00:44:51.487 | Barcelona | Barcelona | Carry | - | [12.8, 71.0] |  |
| +0.46 | +0.00 | 00:44:51.948 | Granada | Barcelona | Foul Committed | **YES** | [107.6, 10.1] | ⭐ **CP INITIATION** |
| +0.46 | +0.00 | 00:44:51.948 | Barcelona | Barcelona | Foul Won | - | [12.5, 70.0] |  |
| +6.87 | +6.41 | 00:44:58.361 | Barcelona | Barcelona | Pass | - | [6.1, 69.7] |  |
| +9.35 | +8.89 | 00:45:00.837 | Barcelona | Barcelona | Ball Receipt* | - | [11.3, 35.2] |  |
| +9.35 | +8.89 | 00:45:00.837 | Barcelona | Barcelona | Carry | - | [11.3, 35.2] |  |
| +18.56 | +18.10 | 00:45:10.045 | Barcelona | Barcelona | Pass | - | [67.8, 14.7] |  |
| +19.88 | +19.42 | 00:45:11.364 | Barcelona | Barcelona | Ball Receipt* | - | [86.6, 3.6] |  |
| +19.88 | +19.42 | 00:45:11.364 | Barcelona | Barcelona | Carry | - | [86.6, 3.6] |  |

---

### Episode 68: `3893820_p30_0d834e73`
- **Match**: `3893820` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Norway Women's** vs. Possession Team: **Philippines Women's**
- **Initiation Action**: `Pressure` by **Sophie Roman Haug** at `00:13:57.072` (Turnover delay: 1.436s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.436s). Harmless transition (opp max progression x=68.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.44 | 00:13:55.636 | Norway Women's | Norway Women's | Ball Receipt* | - | [96.1, 55.6] |  |
| +0.00 | -1.44 | 00:13:55.636 | Philippines Women's | Philippines Women's | Ball Recovery | - | [17.6, 10.2] | 🔄 **TURNOVER** |
| +0.00 | -1.44 | 00:13:55.636 | Philippines Women's | Philippines Women's | Carry | - | [17.6, 10.2] |  |
| +1.44 | +0.00 | 00:13:57.072 | Norway Women's | Philippines Women's | Pressure | **YES** | [97.6, 68.9] | ⭐ **CP INITIATION** |
| +1.85 | +0.41 | 00:13:57.481 | Philippines Women's | Philippines Women's | Pass | - | [22.5, 7.9] |  |
| +3.91 | +2.47 | 00:13:59.545 | Philippines Women's | Philippines Women's | Ball Receipt* | - | [63.6, 3.6] |  |
| +3.91 | +2.47 | 00:13:59.545 | Philippines Women's | Philippines Women's | Pass | - | [63.6, 3.6] |  |
| +4.15 | +2.72 | 00:13:59.787 | Philippines Women's | Philippines Women's | Ball Receipt* | - | [45.7, 6.1] |  |
| +4.15 | +2.72 | 00:13:59.787 | Norway Women's | Philippines Women's | Block | **YES** | [59.8, 76.3] |  |
| +6.32 | +4.89 | 00:14:01.959 | Philippines Women's | Philippines Women's | Pressure | - | [68.5, 19.9] |  |
| +6.63 | +5.20 | 00:14:02.267 | Norway Women's | Philippines Women's | Pass | - | [50.4, 62.5] |  |
| +9.46 | +8.02 | 00:14:05.091 | Norway Women's | Philippines Women's | Ball Receipt* | - | [74.6, 76.0] |  |
| +17.66 | +16.22 | 00:14:13.292 | Philippines Women's | Philippines Women's | Pass | - | [52.6, 0.1] |  |
| +19.16 | +17.73 | 00:14:14.797 | Philippines Women's | Philippines Women's | Ball Receipt* | - | [73.8, 2.8] |  |
| +19.16 | +17.73 | 00:14:14.797 | Philippines Women's | Philippines Women's | Pass | - | [73.3, 2.8] |  |
| +20.80 | +19.37 | 00:14:16.440 | Philippines Women's | Philippines Women's | Ball Receipt* | - | [81.2, 5.4] |  |
| +20.80 | +19.37 | 00:14:16.440 | Norway Women's | Philippines Women's | Clearance | - | [32.5, 75.3] |  |

---

### Episode 69: `3893826_p57_13bd852a`
- **Match**: `3893826` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Portugal Women's** vs. Possession Team: **United States Women's**
- **Initiation Action**: `Block` by **Catarina Amado** at `00:28:18.850` (Turnover delay: 3.4s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=3.4s). Harmless transition (opp max progression x=43.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.94 | -5.34 | 00:28:13.506 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [66.3, 44.3] |  |
| -1.94 | -5.34 | 00:28:13.506 | Portugal Women's | Portugal Women's | Carry | - | [66.3, 44.3] |  |
| -1.78 | -5.18 | 00:28:13.666 | United States Women's | Portugal Women's | Pressure | - | [53.8, 35.8] |  |
| +0.00 | -3.40 | 00:28:15.450 | Portugal Women's | Portugal Women's | Dispossessed | - | [76.2, 35.4] |  |
| +0.00 | -3.40 | 00:28:15.450 | United States Women's | United States Women's | Duel | **YES** | [43.9, 44.7] | 🔄 **TURNOVER** |
| +3.34 | -0.06 | 00:28:18.785 | United States Women's | United States Women's | Pass | - | [24.3, 75.2] |  |
| +3.40 | +0.00 | 00:28:18.850 | United States Women's | United States Women's | Ball Receipt* | - | [48.0, 66.1] |  |
| +3.40 | +0.00 | 00:28:18.850 | Portugal Women's | United States Women's | Block | **YES** | [93.1, 4.1] | ⭐ **CP INITIATION** |
| +5.21 | +1.81 | 00:28:20.664 | Portugal Women's | United States Women's | Pressure | - | [116.4, 3.9] |  |
| +6.86 | +3.46 | 00:28:22.310 | United States Women's | United States Women's | Shield | - | [3.7, 76.2] |  |
| +17.68 | +14.28 | 00:28:33.128 | United States Women's | United States Women's | Pass | - | [7.0, 44.1] |  |
| +20.16 | +16.76 | 00:28:35.613 | United States Women's | United States Women's | Ball Receipt* | - | [11.3, 24.7] |  |
| +20.16 | +16.76 | 00:28:35.613 | United States Women's | United States Women's | Carry | - | [11.3, 24.7] |  |
| +22.92 | +19.52 | 00:28:38.372 | United States Women's | United States Women's | Pass | - | [21.0, 25.5] |  |

---

### Episode 70: `3895134_p143_0cd004a4`
- **Match**: `3895134` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 2, Pressing Team: **Hoffenheim** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Pressure` by **Maximilian Beier** at `00:40:17.411` (Turnover delay: 3.526s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.526s). Dangerous transition triggered by: Final third entry at dt=12.522s (initial x=13.1, max x=85.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.56 | -6.09 | 00:40:11.325 | Bayer Leverkusen | Hoffenheim | Pressure | - | [7.8, 8.1] |  |
| -2.08 | -5.61 | 00:40:11.803 | Hoffenheim | Hoffenheim | Ball Recovery | - | [112.3, 72.6] |  |
| -2.08 | -5.61 | 00:40:11.803 | Hoffenheim | Hoffenheim | Carry | - | [112.3, 72.6] |  |
| -2.04 | -5.57 | 00:40:11.846 | Bayer Leverkusen | Hoffenheim | Dribbled Past | - | [7.8, 7.5] |  |
| -2.04 | -5.57 | 00:40:11.846 | Hoffenheim | Hoffenheim | Dribble | - | [112.3, 72.6] |  |
| -2.04 | -5.57 | 00:40:11.846 | Hoffenheim | Hoffenheim | Carry | - | [112.3, 72.6] |  |
| -0.46 | -3.98 | 00:40:13.427 | Hoffenheim | Hoffenheim | Pass | - | [118.7, 65.5] |  |
| +0.00 | -3.53 | 00:40:13.885 | Hoffenheim | Hoffenheim | Ball Receipt* | - | [111.1, 48.2] |  |
| +0.00 | -3.53 | 00:40:13.885 | Bayer Leverkusen | Hoffenheim | Block | - | [3.4, 23.9] | 🔄 **TURNOVER** |
| +1.68 | -1.85 | 00:40:15.566 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [13.1, 24.5] |  |
| +2.66 | -0.87 | 00:40:16.543 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [3.1, 24.7] |  |
| +2.66 | -0.87 | 00:40:16.543 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [3.1, 24.7] |  |
| +3.53 | +0.00 | 00:40:17.411 | Hoffenheim | Bayer Leverkusen | Pressure | **YES** | [114.6, 55.4] | ⭐ **CP INITIATION** |
| +3.90 | +0.37 | 00:40:17.783 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [4.0, 24.1] |  |
| +6.52 | +2.99 | 00:40:20.405 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [31.0, 59.4] |  |
| +6.52 | +2.99 | 00:40:20.405 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [31.0, 59.4] |  |
| +15.79 | +12.26 | 00:40:29.671 | Hoffenheim | Bayer Leverkusen | Pressure | - | [34.5, 16.0] |  |
| +16.05 | +12.52 | 00:40:29.933 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [85.5, 66.9] |  |
| +18.07 | +14.55 | 00:40:31.956 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [69.8, 56.7] |  |
| +18.07 | +14.55 | 00:40:31.956 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [69.8, 56.7] |  |
| +19.95 | +16.42 | 00:40:33.834 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [70.1, 57.7] |  |
| +21.47 | +17.95 | 00:40:35.360 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [62.4, 72.7] |  |
| +21.47 | +17.95 | 00:40:35.360 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [62.4, 72.7] |  |
| +22.68 | +19.15 | 00:40:36.564 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [57.6, 72.7] |  |

---

### Episode 71: `3802805_p62_2f1423b0`
- **Match**: `3802805` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 1, Pressing Team: **Paris Saint-Germain** vs. Possession Team: **OGC Nice**
- **Initiation Action**: `Pressure` by **Danilo Luís Hélio Pereira** at `00:37:00.847` (Turnover delay: 2.504s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.504s). Dangerous transition triggered by: Shot at dt=0.753s; Final third entry at dt=0.753s (initial x=64.4, max x=88.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.52 | -5.03 | 00:36:55.822 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [49.0, 69.0] |  |
| +0.00 | -2.50 | 00:36:58.343 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [49.3, 48.1] |  |
| +0.00 | -2.50 | 00:36:58.343 | OGC Nice | OGC Nice | Pass | - | [64.4, 41.7] | 🔄 **TURNOVER** |
| +1.62 | -0.89 | 00:36:59.960 | OGC Nice | OGC Nice | Ball Receipt* | - | [77.0, 51.3] |  |
| +1.62 | -0.89 | 00:36:59.960 | OGC Nice | OGC Nice | Carry | - | [77.0, 51.3] |  |
| +2.50 | +0.00 | 00:37:00.847 | Paris Saint-Germain | OGC Nice | Pressure | **YES** | [34.3, 27.3] | ⭐ **CP INITIATION** |
| +3.26 | +0.75 | 00:37:01.600 | OGC Nice | OGC Nice | Shot | - | [88.5, 45.2] |  |
| +4.44 | +1.94 | 00:37:02.784 | Paris Saint-Germain | OGC Nice | Goal Keeper | - | [2.6, 38.5] |  |

---

### Episode 72: `3895220_p6_8e1331a2`
- **Match**: `3895220` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Darmstadt 98** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Pressure` by **Bartol Franjić** at `00:01:10.049` (Turnover delay: 1.086s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.086s). Harmless transition (opp max progression x=56.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.09 | 00:01:08.963 | Darmstadt 98 | Darmstadt 98 | Duel | - | [72.6, 46.5] |  |
| +0.00 | -1.09 | 00:01:08.963 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [47.5, 33.6] | 🔄 **TURNOVER** |
| +1.09 | +0.00 | 00:01:10.049 | Darmstadt 98 | Bayer Leverkusen | Pressure | **YES** | [57.2, 47.3] | ⭐ **CP INITIATION** |
| +1.43 | +0.34 | 00:01:10.392 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [55.7, 34.7] |  |
| +1.43 | +0.34 | 00:01:10.392 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [56.9, 34.1] |  |
| +2.51 | +1.43 | 00:01:11.475 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [55.1, 41.5] |  |
| +2.51 | +1.43 | 00:01:11.475 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [55.1, 41.5] |  |
| +2.68 | +1.60 | 00:01:11.645 | Darmstadt 98 | Bayer Leverkusen | Pressure | **YES** | [63.6, 42.7] |  |
| +3.33 | +2.24 | 00:01:12.291 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [55.7, 41.9] |  |
| +4.93 | +3.84 | 00:01:13.893 | Darmstadt 98 | Bayer Leverkusen | Pressure | **YES** | [75.6, 32.3] |  |
| +5.28 | +4.19 | 00:01:14.244 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [38.2, 50.8] |  |
| +5.28 | +4.19 | 00:01:14.244 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [38.2, 50.8] |  |
| +6.32 | +5.24 | 00:01:15.286 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [34.1, 51.0] |  |
| +8.33 | +7.24 | 00:01:17.288 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [14.3, 45.7] |  |
| +8.33 | +7.24 | 00:01:17.288 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [14.3, 45.7] |  |
| +9.69 | +8.60 | 00:01:18.653 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [16.8, 42.7] |  |
| +11.41 | +10.32 | 00:01:20.374 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [25.3, 19.3] |  |
| +11.41 | +10.32 | 00:01:20.374 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [25.3, 19.3] |  |
| +14.74 | +13.66 | 00:01:23.704 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [30.1, 18.7] |  |
| +15.49 | +14.40 | 00:01:24.450 | Darmstadt 98 | Bayer Leverkusen | Pressure | - | [69.9, 61.0] |  |
| +15.99 | +14.91 | 00:01:24.955 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [44.9, 19.1] |  |
| +15.99 | +14.91 | 00:01:24.955 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [46.0, 19.1] |  |
| +17.15 | +16.06 | 00:01:26.114 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [32.9, 15.1] |  |
| +17.15 | +16.06 | 00:01:26.114 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [32.9, 15.1] |  |
| +18.80 | +17.72 | 00:01:27.765 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [33.5, 14.6] |  |
| +20.52 | +19.43 | 00:01:29.480 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [32.9, 30.7] |  |
| +20.52 | +19.43 | 00:01:29.480 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [32.9, 30.7] |  |

---

### Episode 73: `3998857_p62_17f0d18a`
- **Match**: `3998857` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Poland Women's** vs. Possession Team: **Denmark Women's**
- **Initiation Action**: `Pressure` by **Ewa Pajor** at `00:30:58.745` (Turnover delay: 2.573s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.573s). Harmless transition (opp max progression x=40.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.19 | -4.76 | 00:30:53.980 | Poland Women's | Poland Women's | Ball Receipt* | - | [79.1, 45.5] |  |
| -2.19 | -4.76 | 00:30:53.980 | Poland Women's | Poland Women's | Miscontrol | - | [79.9, 45.5] |  |
| +0.00 | -2.57 | 00:30:56.172 | Denmark Women's | Denmark Women's | Pass | - | [21.3, 38.9] | 🔄 **TURNOVER** |
| +1.91 | -0.66 | 00:30:58.081 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [14.3, 29.4] |  |
| +1.91 | -0.66 | 00:30:58.081 | Denmark Women's | Denmark Women's | Carry | - | [14.3, 29.4] |  |
| +1.95 | -0.62 | 00:30:58.121 | Denmark Women's | Denmark Women's | Pass | - | [14.3, 29.4] |  |
| +2.57 | +0.00 | 00:30:58.745 | Poland Women's | Denmark Women's | Pressure | **YES** | [100.1, 43.8] | ⭐ **CP INITIATION** |
| +2.89 | +0.32 | 00:30:59.062 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [20.0, 36.3] |  |
| +2.89 | +0.32 | 00:30:59.062 | Denmark Women's | Denmark Women's | Pass | - | [20.2, 35.4] |  |
| +5.33 | +2.75 | 00:31:01.499 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [40.4, 9.6] |  |
| +5.33 | +2.75 | 00:31:01.499 | Poland Women's | Denmark Women's | Interception | - | [82.3, 66.8] |  |
| +6.93 | +4.35 | 00:31:03.098 | Poland Women's | Denmark Women's | Pressure | - | [91.6, 68.3] |  |
| +7.04 | +4.47 | 00:31:03.214 | Denmark Women's | Denmark Women's | Pass | - | [25.9, 11.8] |  |
| +8.43 | +5.85 | 00:31:04.598 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [31.5, 9.8] |  |
| +8.43 | +5.85 | 00:31:04.598 | Denmark Women's | Denmark Women's | Duel | - | [31.0, 13.1] |  |
| +8.43 | +5.85 | 00:31:04.598 | Poland Women's | Denmark Women's | Pass | - | [89.1, 67.0] |  |
| +9.15 | +6.58 | 00:31:05.327 | Poland Women's | Denmark Women's | Ball Receipt* | - | [94.0, 71.6] |  |
| +9.15 | +6.58 | 00:31:05.327 | Poland Women's | Denmark Women's | Duel | - | [93.4, 69.2] |  |
| +9.15 | +6.58 | 00:31:05.327 | Denmark Women's | Denmark Women's | Pass | - | [26.7, 10.9] |  |
| +11.48 | +8.91 | 00:31:07.651 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [23.7, 20.5] |  |
| +11.48 | +8.91 | 00:31:07.651 | Denmark Women's | Denmark Women's | Carry | - | [23.7, 20.5] |  |
| +11.90 | +9.33 | 00:31:08.074 | Poland Women's | Denmark Women's | Pressure | - | [96.4, 59.6] |  |
| +12.76 | +10.19 | 00:31:08.930 | Denmark Women's | Denmark Women's | Pass | - | [23.4, 20.9] |  |
| +13.46 | +10.89 | 00:31:09.635 | Denmark Women's | Denmark Women's | Ball Receipt* | - | [24.6, 31.1] |  |
| +13.46 | +10.89 | 00:31:09.635 | Denmark Women's | Denmark Women's | Carry | - | [24.6, 31.1] |  |
| +13.50 | +10.93 | 00:31:09.675 | Denmark Women's | Denmark Women's | Miscontrol | - | [24.6, 31.1] |  |
| +14.92 | +12.35 | 00:31:11.097 | Poland Women's | Poland Women's | Ball Recovery | - | [99.0, 44.2] |  |
| +14.92 | +12.35 | 00:31:11.097 | Poland Women's | Poland Women's | Carry | - | [99.0, 44.2] |  |
| +15.34 | +12.77 | 00:31:11.513 | Denmark Women's | Poland Women's | Pressure | **YES** | [18.4, 33.5] |  |
| +15.42 | +12.85 | 00:31:11.596 | Denmark Women's | Poland Women's | Pressure | **YES** | [19.6, 35.9] |  |
| +16.00 | +13.43 | 00:31:12.173 | Poland Women's | Poland Women's | Dribble | - | [101.7, 45.1] |  |
| +16.00 | +13.43 | 00:31:12.173 | Denmark Women's | Poland Women's | Duel | **YES** | [18.4, 35.0] |  |
| +16.91 | +14.34 | 00:31:13.082 | Poland Women's | Poland Women's | Ball Recovery | - | [96.7, 43.4] |  |
| +16.95 | +14.38 | 00:31:13.122 | Poland Women's | Poland Women's | Shot | - | [97.1, 43.2] |  |
| +17.84 | +15.27 | 00:31:14.016 | Denmark Women's | Poland Women's | Goal Keeper | - | [0.6, 40.2] |  |
| +19.95 | +17.38 | 00:31:16.120 | Denmark Women's | Denmark Women's | Ball Recovery | - | [2.2, 43.1] |  |

---

### Episode 74: `3773372_p162_1742c785`
- **Match**: `3773372` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Atlético Madrid** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Foul Committed` by **Marcos Llorente Moreno** at `00:14:16.590` (Turnover delay: 2.151s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.151s). Harmless transition (opp max progression x=61.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.46 | -4.61 | 00:14:11.983 | Atlético Madrid | Atlético Madrid | Ball Receipt* | - | [53.2, 71.8] |  |
| -2.46 | -4.61 | 00:14:11.983 | Atlético Madrid | Atlético Madrid | Carry | - | [53.2, 71.8] |  |
| -1.37 | -3.52 | 00:14:13.066 | Atlético Madrid | Atlético Madrid | Pass | - | [53.2, 73.4] |  |
| +0.00 | -2.15 | 00:14:14.439 | Atlético Madrid | Atlético Madrid | Ball Receipt* | - | [82.8, 55.0] |  |
| +0.00 | -2.15 | 00:14:14.439 | Barcelona | Barcelona | Interception | **YES** | [40.3, 15.6] | 🔄 **TURNOVER** |
| +0.00 | -2.15 | 00:14:14.439 | Barcelona | Barcelona | Carry | - | [40.3, 15.6] |  |
| +2.15 | +0.00 | 00:14:16.590 | Atlético Madrid | Barcelona | Foul Committed | **YES** | [82.8, 55.0] | ⭐ **CP INITIATION** |
| +2.15 | +0.00 | 00:14:16.590 | Barcelona | Barcelona | Foul Won | - | [37.3, 25.1] |  |
| +2.15 | +0.00 | 00:14:16.590 | Barcelona | Barcelona | Carry | - | [37.3, 25.1] |  |
| +2.16 | +0.01 | 00:14:16.598 | Atlético Madrid | Barcelona | Duel | **YES** | [82.3, 64.9] |  |
| +2.16 | +0.01 | 00:14:16.598 | Barcelona | Barcelona | Pass | - | [37.8, 15.2] |  |
| +3.16 | +1.01 | 00:14:17.601 | Barcelona | Barcelona | Ball Receipt* | - | [43.8, 8.7] |  |
| +3.16 | +1.01 | 00:14:17.601 | Barcelona | Barcelona | Carry | - | [43.8, 8.7] |  |
| +3.27 | +1.12 | 00:14:17.707 | Atlético Madrid | Barcelona | Pressure | **YES** | [75.2, 70.4] |  |
| +3.54 | +1.39 | 00:14:17.982 | Barcelona | Barcelona | Pass | - | [43.6, 8.1] |  |
| +4.42 | +2.27 | 00:14:18.856 | Atlético Madrid | Barcelona | Pressure | **YES** | [64.5, 70.7] |  |
| +4.86 | +2.71 | 00:14:19.302 | Barcelona | Barcelona | Ball Receipt* | - | [58.2, 9.4] |  |
| +4.86 | +2.71 | 00:14:19.302 | Barcelona | Barcelona | Carry | - | [58.2, 9.4] |  |
| +5.13 | +2.98 | 00:14:19.568 | Barcelona | Barcelona | Pass | - | [56.7, 11.1] |  |
| +5.86 | +3.70 | 00:14:20.294 | Atlético Madrid | Barcelona | Pressure | - | [59.0, 57.7] |  |
| +6.00 | +3.85 | 00:14:20.438 | Barcelona | Barcelona | Ball Receipt* | - | [61.1, 22.4] |  |
| +6.00 | +3.85 | 00:14:20.438 | Barcelona | Barcelona | Carry | - | [61.1, 22.4] |  |
| +6.35 | +4.20 | 00:14:20.788 | Atlético Madrid | Barcelona | Foul Committed | - | [58.7, 58.7] |  |
| +6.35 | +4.20 | 00:14:20.788 | Barcelona | Barcelona | Foul Won | - | [61.4, 21.4] |  |

---

### Episode 75: `3844386_p175_bc9d48e6`
- **Match**: `3844386` | **Competition**: UEFA Women's Euro (2022)
- **Context**: Period 2, Pressing Team: **Sweden Women's** vs. Possession Team: **Belgium Women's**
- **Initiation Action**: `Pressure` by **Kosovare Asllani** at `00:42:56.069` (Turnover delay: 1.396s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.396s). Dangerous transition triggered by: Final third entry at dt=5.725s (initial x=58.6, max x=104.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.66 | -3.06 | 00:42:53.009 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [65.9, 34.8] |  |
| -1.66 | -3.06 | 00:42:53.009 | Sweden Women's | Sweden Women's | Carry | - | [65.9, 34.8] |  |
| -1.33 | -2.72 | 00:42:53.345 | Belgium Women's | Sweden Women's | Dribbled Past | **YES** | [54.2, 45.3] |  |
| -1.33 | -2.72 | 00:42:53.345 | Sweden Women's | Sweden Women's | Dribble | - | [65.9, 34.8] |  |
| -1.33 | -2.72 | 00:42:53.345 | Sweden Women's | Sweden Women's | Carry | - | [65.9, 34.8] |  |
| -0.95 | -2.35 | 00:42:53.718 | Belgium Women's | Sweden Women's | Pressure | **YES** | [56.5, 51.3] |  |
| +0.00 | -1.40 | 00:42:54.673 | Sweden Women's | Sweden Women's | Dispossessed | - | [61.5, 23.8] |  |
| +0.00 | -1.40 | 00:42:54.673 | Belgium Women's | Belgium Women's | Duel | **YES** | [58.6, 56.3] | 🔄 **TURNOVER** |
| +0.00 | -1.40 | 00:42:54.673 | Belgium Women's | Belgium Women's | Carry | - | [58.6, 56.3] |  |
| +1.40 | +0.00 | 00:42:56.069 | Sweden Women's | Belgium Women's | Pressure | **YES** | [58.6, 23.6] | ⭐ **CP INITIATION** |
| +1.83 | +0.43 | 00:42:56.503 | Belgium Women's | Belgium Women's | Pass | - | [63.2, 54.1] |  |
| +3.05 | +1.66 | 00:42:57.727 | Belgium Women's | Belgium Women's | Ball Receipt* | - | [69.3, 59.8] |  |
| +3.05 | +1.66 | 00:42:57.727 | Belgium Women's | Belgium Women's | Carry | - | [69.3, 59.8] |  |
| +4.83 | +3.43 | 00:42:59.499 | Belgium Women's | Belgium Women's | Pass | - | [78.5, 64.8] |  |
| +7.12 | +5.72 | 00:43:01.794 | Belgium Women's | Belgium Women's | Ball Receipt* | - | [104.0, 64.1] |  |
| +7.12 | +5.72 | 00:43:01.794 | Belgium Women's | Belgium Women's | Carry | - | [104.0, 64.1] |  |
| +7.21 | +5.81 | 00:43:01.880 | Belgium Women's | Belgium Women's | Pass | - | [104.4, 64.1] |  |
| +8.56 | +7.17 | 00:43:03.237 | Belgium Women's | Belgium Women's | Ball Receipt* | - | [102.5, 51.0] |  |
| +8.56 | +7.17 | 00:43:03.237 | Sweden Women's | Belgium Women's | Interception | - | [16.5, 26.4] |  |

---

### Episode 76: `3788763_p141_a9a1ac21`
- **Match**: `3788763` | **Competition**: UEFA Euro (2020)
- **Context**: Period 2, Pressing Team: **France** vs. Possession Team: **Hungary**
- **Initiation Action**: `Pressure` by **N'Golo Kanté** at `00:32:53.811` (Turnover delay: 2.212s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.212s). Harmless transition (opp max progression x=31.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.77 | -3.98 | 00:32:49.827 | Hungary | France | Clearance | - | [15.2, 52.8] |  |
| -0.27 | -2.48 | 00:32:51.327 | France | France | Pass | - | [89.4, 44.0] |  |
| +0.00 | -2.21 | 00:32:51.599 | France | France | Ball Receipt* | - | [96.0, 40.8] |  |
| +0.00 | -2.21 | 00:32:51.599 | Hungary | France | Block | - | [27.6, 36.3] | 🔄 **TURNOVER** |
| +1.12 | -1.10 | 00:32:52.716 | Hungary | Hungary | Ball Recovery | - | [29.0, 38.9] |  |
| +1.12 | -1.10 | 00:32:52.716 | Hungary | Hungary | Carry | - | [29.0, 38.9] |  |
| +2.21 | +0.00 | 00:32:53.811 | France | Hungary | Pressure | **YES** | [85.1, 40.8] | ⭐ **CP INITIATION** |
| +3.44 | +1.23 | 00:32:55.036 | France | Hungary | Foul Committed | **YES** | [88.8, 40.7] |  |
| +3.44 | +1.23 | 00:32:55.036 | Hungary | Hungary | Foul Won | - | [31.3, 39.4] |  |

---

### Episode 77: `3869254_p161_1b743aec`
- **Match**: `3869254` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **Switzerland** vs. Possession Team: **Portugal**
- **Initiation Action**: `Pressure` by **Ardon Jashari** at `00:48:10.299` (Turnover delay: 2.655s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.655s). Dangerous transition triggered by: Final third entry at dt=1.325s (initial x=75.6, max x=112.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.03 | -4.69 | 00:48:05.609 | Switzerland | Switzerland | Pass | - | [48.4, 0.1] |  |
| -0.96 | -3.62 | 00:48:06.682 | Switzerland | Switzerland | Ball Receipt* | - | [42.6, 8.0] |  |
| -0.96 | -3.62 | 00:48:06.682 | Switzerland | Switzerland | Carry | - | [42.6, 8.0] |  |
| -0.80 | -3.45 | 00:48:06.844 | Portugal | Switzerland | Pressure | - | [75.6, 72.7] |  |
| +0.00 | -2.66 | 00:48:07.644 | Switzerland | Switzerland | Dribble | - | [44.5, 9.8] |  |
| +0.00 | -2.66 | 00:48:07.644 | Portugal | Portugal | Duel | **YES** | [75.6, 70.3] | 🔄 **TURNOVER** |
| +1.41 | -1.25 | 00:48:09.049 | Portugal | Portugal | Ball Recovery | - | [85.8, 68.4] |  |
| +1.41 | -1.25 | 00:48:09.049 | Portugal | Portugal | Carry | - | [85.8, 68.4] |  |
| +2.50 | -0.16 | 00:48:10.141 | Portugal | Portugal | Pass | - | [88.9, 66.4] |  |
| +2.66 | +0.00 | 00:48:10.299 | Switzerland | Portugal | Pressure | **YES** | [30.0, 15.4] | ⭐ **CP INITIATION** |
| +3.98 | +1.32 | 00:48:11.624 | Portugal | Portugal | Ball Receipt* | - | [106.5, 70.7] |  |
| +3.98 | +1.32 | 00:48:11.624 | Portugal | Portugal | Carry | - | [106.5, 70.7] |  |
| +4.80 | +2.15 | 00:48:12.448 | Portugal | Portugal | Pass | - | [108.0, 67.2] |  |
| +5.13 | +2.48 | 00:48:12.777 | Portugal | Portugal | Ball Receipt* | - | [112.5, 53.1] |  |
| +5.13 | +2.48 | 00:48:12.777 | Switzerland | Portugal | Interception | - | [8.7, 19.5] |  |

---

### Episode 78: `4020846_p45_58005b35`
- **Match**: `4020846` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **England Women's** vs. Possession Team: **England Women's**
- **Initiation Action**: `Block` by **Leah Williamson** at `00:21:20.708` (Turnover delay: 4.094s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.853s by England Women's. Harmless transition (opp max progression x=7.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.73 | -4.82 | 00:21:15.888 | Spain Women's | England Women's | Clearance | - | [46.3, 34.8] |  |
| -0.15 | -4.25 | 00:21:16.459 | England Women's | England Women's | Pressure | - | [66.0, 51.6] |  |
| +0.00 | -4.09 | 00:21:16.614 | Spain Women's | England Women's | Ball Recovery | - | [57.0, 28.0] | 🔄 **TURNOVER** |
| +0.00 | -4.09 | 00:21:16.614 | Spain Women's | England Women's | Carry | - | [57.0, 28.0] |  |
| +4.04 | -0.05 | 00:21:20.657 | Spain Women's | England Women's | Pass | - | [74.0, 21.5] |  |
| +4.09 | +0.00 | 00:21:20.708 | England Women's | England Women's | Block | **YES** | [43.5, 59.0] | ⭐ **CP INITIATION** |
| +4.95 | +0.85 | 00:21:21.561 | England Women's | England Women's | Ball Recovery | - | [47.1, 64.8] |  |
| +4.95 | +0.85 | 00:21:21.561 | England Women's | England Women's | Carry | - | [47.1, 64.8] |  |
| +6.11 | +2.02 | 00:21:22.726 | Spain Women's | England Women's | Pressure | - | [71.9, 14.7] |  |
| +7.32 | +3.23 | 00:21:23.937 | England Women's | England Women's | Pass | - | [50.2, 70.3] |  |
| +7.43 | +3.34 | 00:21:24.048 | Spain Women's | England Women's | Block | - | [71.9, 9.4] |  |
| +10.08 | +5.98 | 00:21:26.691 | England Women's | England Women's | Pass | - | [38.5, 79.1] |  |
| +14.87 | +10.78 | 00:21:31.488 | England Women's | England Women's | Pressure | - | [95.3, 71.7] |  |
| +15.68 | +11.59 | 00:21:32.298 | Spain Women's | Spain Women's | Pass | - | [20.9, 11.7] |  |
| +17.20 | +13.11 | 00:21:33.817 | England Women's | Spain Women's | Pressure | **YES** | [111.9, 55.5] |  |
| +17.55 | +13.45 | 00:21:34.162 | Spain Women's | Spain Women's | Ball Receipt* | - | [1.9, 27.5] |  |
| +17.55 | +13.45 | 00:21:34.162 | Spain Women's | Spain Women's | Pass | - | [3.9, 25.4] |  |
| +20.00 | +15.91 | 00:21:36.618 | Spain Women's | Spain Women's | Ball Receipt* | - | [23.2, 3.9] |  |
| +20.00 | +15.91 | 00:21:36.618 | Spain Women's | Spain Women's | Carry | - | [23.2, 3.9] |  |
| +20.70 | +16.61 | 00:21:37.316 | Spain Women's | Spain Women's | Pass | - | [25.0, 2.9] |  |
| +21.51 | +17.42 | 00:21:38.124 | England Women's | Spain Women's | Pressure | - | [75.4, 78.5] |  |
| +21.63 | +17.54 | 00:21:38.247 | Spain Women's | Spain Women's | Ball Receipt* | - | [42.4, 1.6] |  |
| +21.63 | +17.54 | 00:21:38.247 | Spain Women's | Spain Women's | Carry | - | [42.4, 1.6] |  |
| +23.22 | +19.12 | 00:21:39.833 | Spain Women's | Spain Women's | Pass | - | [38.5, 1.6] |  |

---

### Episode 79: `3869354_p129_b147177d`
- **Match**: `3869354` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **England** vs. Possession Team: **France**
- **Initiation Action**: `Pressure` by **Jude Bellingham** at `00:19:34.892` (Turnover delay: 0.278s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=0.278s). Dangerous transition triggered by: Final third entry at dt=13.997s (initial x=26.2, max x=91.8).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.81 | -2.09 | 00:19:32.804 | England | England | Miscontrol | - | [92.4, 66.0] |  |
| +0.00 | -0.28 | 00:19:34.614 | France | France | Ball Recovery | - | [26.2, 18.1] | 🔄 **TURNOVER** |
| +0.00 | -0.28 | 00:19:34.614 | France | France | Carry | - | [26.2, 18.1] |  |
| +0.28 | +0.00 | 00:19:34.892 | England | France | Pressure | **YES** | [92.2, 60.9] | ⭐ **CP INITIATION** |
| +3.72 | +3.44 | 00:19:38.333 | England | France | Foul Committed | **YES** | [81.1, 63.5] |  |
| +3.72 | +3.44 | 00:19:38.333 | France | France | Foul Won | - | [39.0, 16.6] |  |
| +6.02 | +5.74 | 00:19:40.631 | France | France | Pass | - | [38.8, 20.5] |  |
| +6.85 | +6.57 | 00:19:41.463 | France | France | Ball Receipt* | - | [46.7, 44.9] |  |
| +6.85 | +6.57 | 00:19:41.463 | France | France | Carry | - | [46.7, 44.9] |  |
| +8.58 | +8.30 | 00:19:43.190 | England | France | Pressure | - | [64.4, 38.9] |  |
| +9.99 | +9.71 | 00:19:44.602 | France | France | Pass | - | [63.6, 38.0] |  |
| +11.63 | +11.35 | 00:19:46.242 | France | France | Ball Receipt* | - | [68.9, 18.3] |  |
| +11.63 | +11.35 | 00:19:46.242 | France | France | Carry | - | [68.9, 18.3] |  |
| +12.56 | +12.28 | 00:19:47.175 | England | France | Pressure | - | [45.8, 68.6] |  |
| +13.31 | +13.03 | 00:19:47.919 | France | France | Pass | - | [76.0, 10.6] |  |
| +14.27 | +14.00 | 00:19:48.889 | France | France | Ball Receipt* | - | [91.8, 4.4] |  |
| +14.27 | +14.00 | 00:19:48.889 | France | France | Carry | - | [91.8, 4.4] |  |
| +18.01 | +17.73 | 00:19:52.623 | France | France | Pass | - | [92.3, 4.9] |  |
| +18.90 | +18.62 | 00:19:53.516 | France | France | Ball Receipt* | - | [85.0, 6.8] |  |
| +18.90 | +18.62 | 00:19:53.516 | France | France | Carry | - | [85.0, 6.8] |  |
| +20.17 | +19.89 | 00:19:54.782 | France | France | Pass | - | [85.8, 8.9] |  |

---

### Episode 80: `3835321_p70_c26a6aa8`
- **Match**: `3835321` | **Competition**: UEFA Women's Euro (2022)
- **Context**: Period 1, Pressing Team: **WNT Finland** vs. Possession Team: **Spain Women's**
- **Initiation Action**: `Pressure` by **Emma Wilhelmina Koivisto** at `00:38:01.438` (Turnover delay: 2.279s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=2.279s). Harmless transition (opp max progression x=75.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.72 | -5.00 | 00:37:56.441 | WNT Finland | WNT Finland | Pass | - | [6.0, 36.0] |  |
| +0.00 | -2.28 | 00:37:59.159 | WNT Finland | WNT Finland | Ball Receipt* | - | [50.8, 25.7] |  |
| +0.00 | -2.28 | 00:37:59.159 | WNT Finland | WNT Finland | Duel | - | [52.0, 26.1] |  |
| +0.00 | -2.28 | 00:37:59.159 | Spain Women's | Spain Women's | Pass | - | [68.1, 54.0] | 🔄 **TURNOVER** |
| +0.64 | -1.64 | 00:37:59.795 | Spain Women's | Spain Women's | Ball Receipt* | - | [63.3, 58.6] |  |
| +0.64 | -1.64 | 00:37:59.795 | Spain Women's | Spain Women's | Carry | - | [63.3, 58.6] |  |
| +0.72 | -1.56 | 00:37:59.875 | Spain Women's | Spain Women's | Pass | - | [63.0, 58.6] |  |
| +2.28 | +0.00 | 00:38:01.438 | WNT Finland | Spain Women's | Pressure | **YES** | [43.2, 17.4] | ⭐ **CP INITIATION** |
| +2.50 | +0.22 | 00:38:01.655 | Spain Women's | Spain Women's | Ball Receipt* | - | [72.8, 59.5] |  |
| +2.50 | +0.22 | 00:38:01.655 | Spain Women's | Spain Women's | Carry | - | [72.8, 59.5] |  |
| +3.00 | +0.72 | 00:38:02.155 | WNT Finland | Spain Women's | Pressure | **YES** | [44.6, 18.0] |  |
| +3.55 | +1.27 | 00:38:02.709 | Spain Women's | Spain Women's | Dribble | - | [75.5, 62.1] |  |
| +3.55 | +1.27 | 00:38:02.709 | WNT Finland | Spain Women's | Duel | **YES** | [44.6, 18.0] |  |
| +3.55 | +1.27 | 00:38:02.709 | WNT Finland | Spain Women's | Carry | - | [44.6, 18.0] |  |
| +5.33 | +3.05 | 00:38:04.485 | WNT Finland | Spain Women's | Pass | - | [50.1, 16.2] |  |
| +7.63 | +5.35 | 00:38:06.786 | WNT Finland | Spain Women's | Ball Receipt* | - | [61.3, 13.2] |  |
| +7.63 | +5.35 | 00:38:06.786 | Spain Women's | Spain Women's | Pass | - | [40.3, 61.4] |  |
| +10.85 | +8.57 | 00:38:10.005 | Spain Women's | Spain Women's | Ball Receipt* | - | [14.3, 44.2] |  |
| +10.85 | +8.57 | 00:38:10.005 | Spain Women's | Spain Women's | Carry | - | [14.3, 44.2] |  |
| +11.78 | +9.50 | 00:38:10.934 | Spain Women's | Spain Women's | Pass | - | [15.3, 43.2] |  |
| +13.55 | +11.27 | 00:38:12.704 | Spain Women's | Spain Women's | Ball Receipt* | - | [32.7, 30.3] |  |
| +13.55 | +11.27 | 00:38:12.704 | Spain Women's | Spain Women's | Carry | - | [32.7, 30.3] |  |
| +17.07 | +14.79 | 00:38:16.229 | Spain Women's | Spain Women's | Pass | - | [46.7, 20.5] |  |
| +19.40 | +17.12 | 00:38:18.559 | Spain Women's | Spain Women's | Ball Receipt* | - | [73.1, 3.9] |  |
| +19.40 | +17.12 | 00:38:18.559 | Spain Women's | Spain Women's | Carry | - | [73.1, 3.9] |  |
| +20.62 | +18.34 | 00:38:19.782 | Spain Women's | Spain Women's | Pass | - | [81.1, 4.3] |  |
| +21.91 | +19.63 | 00:38:21.070 | Spain Women's | Spain Women's | Ball Receipt* | - | [77.7, 10.4] |  |
| +21.91 | +19.63 | 00:38:21.070 | Spain Women's | Spain Women's | Carry | - | [77.7, 10.4] |  |

---

### Episode 81: `3901833_p129_7770c5fc`
- **Match**: `3901833` | **Competition**: Women's World Cup (2023)
- **Context**: Period 2, Pressing Team: **France Women's** vs. Possession Team: **Morocco Women's**
- **Initiation Action**: `Pressure` by **Eve Perisset** at `00:15:27.160` (Turnover delay: 1.968s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.968s). Harmless transition (opp max progression x=56.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.76 | -4.73 | 00:15:22.431 | France Women's | France Women's | Ball Receipt* | - | [81.5, 75.7] |  |
| -2.76 | -4.73 | 00:15:22.431 | France Women's | France Women's | Carry | - | [81.5, 75.7] |  |
| -0.51 | -2.48 | 00:15:24.678 | Morocco Women's | France Women's | Pressure | - | [38.1, 12.8] |  |
| +0.00 | -1.97 | 00:15:25.192 | France Women's | France Women's | Dribble | - | [81.1, 69.7] |  |
| +0.00 | -1.97 | 00:15:25.192 | Morocco Women's | Morocco Women's | Duel | **YES** | [39.0, 10.4] | 🔄 **TURNOVER** |
| +0.00 | -1.97 | 00:15:25.192 | Morocco Women's | Morocco Women's | Carry | - | [39.0, 10.4] |  |
| +1.97 | +0.00 | 00:15:27.160 | France Women's | Morocco Women's | Pressure | **YES** | [76.4, 71.0] | ⭐ **CP INITIATION** |
| +2.87 | +0.90 | 00:15:28.064 | France Women's | Morocco Women's | Pressure | **YES** | [80.0, 72.3] |  |
| +5.85 | +3.88 | 00:15:31.045 | Morocco Women's | Morocco Women's | Pass | - | [31.5, 9.8] |  |
| +7.77 | +5.80 | 00:15:32.964 | France Women's | Morocco Women's | Pressure | - | [105.9, 38.7] |  |
| +8.41 | +6.44 | 00:15:33.600 | Morocco Women's | Morocco Women's | Ball Receipt* | - | [8.8, 40.4] |  |
| +8.41 | +6.44 | 00:15:33.600 | Morocco Women's | Morocco Women's | Pass | - | [8.0, 40.4] |  |
| +11.03 | +9.06 | 00:15:36.218 | Morocco Women's | Morocco Women's | Ball Receipt* | - | [43.9, 9.8] |  |
| +11.03 | +9.06 | 00:15:36.218 | France Women's | Morocco Women's | Pass | - | [74.3, 71.0] |  |
| +12.21 | +10.24 | 00:15:37.403 | France Women's | Morocco Women's | Ball Receipt* | - | [93.5, 48.3] |  |
| +12.21 | +10.24 | 00:15:37.403 | Morocco Women's | Morocco Women's | Ball Recovery | - | [37.1, 23.9] |  |
| +12.21 | +10.24 | 00:15:37.403 | Morocco Women's | Morocco Women's | Carry | - | [37.1, 23.9] |  |
| +12.89 | +10.92 | 00:15:38.081 | Morocco Women's | Morocco Women's | Pass | - | [34.9, 19.0] |  |
| +15.58 | +13.61 | 00:15:40.767 | Morocco Women's | Morocco Women's | Ball Receipt* | - | [56.1, 13.0] |  |
| +15.58 | +13.61 | 00:15:40.767 | France Women's | Morocco Women's | Pass | - | [63.1, 63.9] |  |
| +21.37 | +19.40 | 00:15:46.561 | France Women's | Morocco Women's | Ball Receipt* | - | [98.2, 63.9] |  |
| +21.37 | +19.40 | 00:15:46.561 | Morocco Women's | Morocco Women's | Ball Recovery | - | [9.0, 0.8] |  |
| +21.37 | +19.40 | 00:15:46.561 | Morocco Women's | Morocco Women's | Carry | - | [9.0, 0.8] |  |

---

### Episode 82: `3877115_p108_a867f4d7`
- **Match**: `3877115` | **Competition**: Major League Soccer (2023)
- **Context**: Period 2, Pressing Team: **Inter Miami** vs. Possession Team: **Toronto FC**
- **Initiation Action**: `Pressure` by **Facundo Farías** at `00:11:47.466` (Turnover delay: 1.436s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.436s). Dangerous transition triggered by: Final third entry at dt=0.514s (initial x=73.2, max x=97.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.40 | -3.84 | 00:11:43.628 | Inter Miami | Inter Miami | Pass | - | [8.8, 56.0] |  |
| +0.00 | -1.44 | 00:11:46.030 | Inter Miami | Inter Miami | Ball Receipt* | - | [50.5, 65.6] |  |
| +0.00 | -1.44 | 00:11:46.030 | Toronto FC | Toronto FC | Pass | - | [73.2, 15.1] | 🔄 **TURNOVER** |
| +1.44 | +0.00 | 00:11:47.466 | Inter Miami | Toronto FC | Pressure | **YES** | [44.5, 62.4] | ⭐ **CP INITIATION** |
| +1.45 | +0.01 | 00:11:47.475 | Toronto FC | Toronto FC | Ball Receipt* | - | [75.8, 17.5] |  |
| +1.45 | +0.01 | 00:11:47.475 | Toronto FC | Toronto FC | Carry | - | [75.8, 17.5] |  |
| +1.49 | +0.05 | 00:11:47.515 | Toronto FC | Toronto FC | Pass | - | [77.0, 17.2] |  |
| +1.95 | +0.51 | 00:11:47.980 | Toronto FC | Toronto FC | Ball Receipt* | - | [80.6, 22.8] |  |
| +1.95 | +0.51 | 00:11:47.980 | Toronto FC | Toronto FC | Carry | - | [80.6, 22.8] |  |
| +2.15 | +0.71 | 00:11:48.180 | Toronto FC | Toronto FC | Pass | - | [81.1, 22.7] |  |
| +2.71 | +1.27 | 00:11:48.735 | Toronto FC | Toronto FC | Ball Receipt* | - | [75.1, 21.1] |  |
| +2.71 | +1.27 | 00:11:48.735 | Toronto FC | Toronto FC | Carry | - | [75.1, 21.1] |  |
| +3.90 | +2.47 | 00:11:49.931 | Toronto FC | Toronto FC | Pass | - | [79.7, 22.5] |  |
| +6.76 | +5.32 | 00:11:52.787 | Toronto FC | Toronto FC | Ball Receipt* | - | [97.3, 30.6] |  |
| +6.76 | +5.32 | 00:11:52.787 | Inter Miami | Inter Miami | Ball Recovery | - | [3.6, 44.3] |  |
| +6.76 | +5.32 | 00:11:52.787 | Inter Miami | Inter Miami | Carry | - | [3.6, 44.3] |  |
| +12.57 | +11.13 | 00:11:58.598 | Inter Miami | Inter Miami | Pass | - | [8.7, 40.2] |  |
| +14.27 | +12.84 | 00:12:00.304 | Inter Miami | Inter Miami | Ball Receipt* | - | [25.3, 40.6] |  |
| +14.27 | +12.84 | 00:12:00.304 | Inter Miami | Inter Miami | Carry | - | [25.3, 40.6] |  |
| +16.63 | +15.20 | 00:12:02.662 | Inter Miami | Inter Miami | Pass | - | [34.5, 41.2] |  |
| +18.09 | +16.65 | 00:12:04.117 | Inter Miami | Inter Miami | Ball Receipt* | - | [50.3, 24.6] |  |
| +18.09 | +16.65 | 00:12:04.117 | Inter Miami | Inter Miami | Carry | - | [50.3, 24.6] |  |
| +20.41 | +18.97 | 00:12:06.439 | Inter Miami | Inter Miami | Pass | - | [66.5, 20.1] |  |

---

### Episode 83: `3893810_p73_8dc1719e`
- **Match**: `3893810` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **Portugal Women's** vs. Possession Team: **Portugal Women's**
- **Initiation Action**: `Duel` by **Ana Borges** at `00:35:22.364` (Turnover delay: 0.0s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Portugal Women's. Harmless transition (opp max progression x=34.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.57 | -1.57 | 00:35:20.798 | Vietnam Women's | Vietnam Women's | Ball Receipt* | - | [74.2, 4.6] |  |
| -1.57 | -1.57 | 00:35:20.798 | Vietnam Women's | Vietnam Women's | Carry | - | [74.2, 4.6] |  |
| -0.63 | -0.63 | 00:35:21.733 | Portugal Women's | Vietnam Women's | Pressure | - | [38.8, 75.5] |  |
| +0.00 | +0.00 | 00:35:22.364 | Vietnam Women's | Vietnam Women's | Dribble | - | [85.4, 5.0] | 🔄 **TURNOVER** |
| +0.00 | +0.00 | 00:35:22.364 | Portugal Women's | Portugal Women's | Duel | **YES** | [34.7, 75.1] | ⭐ **CP INITIATION** |
| +0.00 | +0.00 | 00:35:22.364 | Portugal Women's | Portugal Women's | Carry | - | [34.7, 75.1] |  |
| +1.20 | +1.20 | 00:35:23.567 | Portugal Women's | Portugal Women's | Pass | - | [34.7, 75.1] |  |
| +1.99 | +1.99 | 00:35:24.353 | Vietnam Women's | Portugal Women's | Pressure | **YES** | [91.4, 23.1] |  |
| +2.45 | +2.45 | 00:35:24.812 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [28.7, 57.0] |  |
| +2.45 | +2.45 | 00:35:24.812 | Portugal Women's | Portugal Women's | Carry | - | [28.7, 57.0] |  |
| +2.50 | +2.50 | 00:35:24.868 | Portugal Women's | Portugal Women's | Pass | - | [28.7, 57.0] |  |
| +3.57 | +3.57 | 00:35:25.934 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [37.9, 65.6] |  |
| +3.57 | +3.57 | 00:35:25.934 | Portugal Women's | Portugal Women's | Pass | - | [37.9, 65.6] |  |
| +4.43 | +4.43 | 00:35:26.790 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [26.8, 76.1] |  |
| +4.43 | +4.43 | 00:35:26.790 | Portugal Women's | Portugal Women's | Pass | - | [28.7, 75.8] |  |
| +5.45 | +5.45 | 00:35:27.809 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [35.2, 56.6] |  |
| +5.45 | +5.45 | 00:35:27.809 | Portugal Women's | Portugal Women's | Carry | - | [35.2, 56.6] |  |
| +5.73 | +5.73 | 00:35:28.096 | Vietnam Women's | Portugal Women's | Pressure | - | [84.9, 23.5] |  |
| +6.08 | +6.08 | 00:35:28.440 | Portugal Women's | Portugal Women's | Pass | - | [33.4, 56.9] |  |
| +6.44 | +6.44 | 00:35:28.804 | Vietnam Women's | Portugal Women's | Pressure | - | [80.4, 18.1] |  |
| +6.97 | +6.97 | 00:35:29.335 | Portugal Women's | Portugal Women's | Ball Receipt* | - | [39.7, 62.0] |  |
| +6.97 | +6.97 | 00:35:29.335 | Portugal Women's | Portugal Women's | Carry | - | [39.7, 62.0] |  |
| +7.01 | +7.01 | 00:35:29.375 | Vietnam Women's | Portugal Women's | Foul Committed | - | [79.9, 17.4] |  |
| +7.01 | +7.01 | 00:35:29.375 | Portugal Women's | Portugal Women's | Foul Won | - | [40.2, 62.7] |  |

---

### Episode 84: `3938637_p75_35359fee`
- **Match**: `3938637` | **Competition**: UEFA Euro (2024)
- **Context**: Period 2, Pressing Team: **Netherlands** vs. Possession Team: **Poland**
- **Initiation Action**: `Pressure` by **Memphis Depay** at `00:04:15.224` (Turnover delay: 1.671s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=3.236s by Netherlands. Harmless transition (opp max progression x=50.7).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.83 | -4.50 | 00:04:10.721 | Poland | Netherlands | Pressure | - | [29.2, 22.9] |  |
| -2.33 | -4.00 | 00:04:11.227 | Netherlands | Netherlands | Ball Receipt* | - | [90.5, 56.1] |  |
| -2.33 | -4.00 | 00:04:11.227 | Netherlands | Netherlands | Carry | - | [90.5, 56.1] |  |
| -1.06 | -2.73 | 00:04:12.498 | Netherlands | Netherlands | Miscontrol | - | [91.3, 49.7] |  |
| +0.00 | -1.67 | 00:04:13.553 | Poland | Poland | Ball Recovery | - | [27.3, 30.1] | 🔄 **TURNOVER** |
| +0.00 | -1.67 | 00:04:13.553 | Poland | Poland | Carry | - | [27.3, 30.1] |  |
| +1.05 | -0.62 | 00:04:14.600 | Poland | Poland | Miscontrol | - | [27.7, 33.3] |  |
| +1.07 | -0.60 | 00:04:14.623 | Poland | Poland | Block | **YES** | [28.6, 33.4] |  |
| +1.67 | +0.00 | 00:04:15.224 | Netherlands | Poland | Pressure | **YES** | [91.8, 49.1] | ⭐ **CP INITIATION** |
| +2.19 | +0.52 | 00:04:15.746 | Poland | Poland | Pass | - | [25.3, 29.1] |  |
| +4.40 | +2.73 | 00:04:17.953 | Netherlands | Poland | Pressure | **YES** | [65.7, 68.2] |  |
| +4.61 | +2.94 | 00:04:18.166 | Poland | Poland | Ball Receipt* | - | [50.7, 11.2] |  |
| +4.61 | +2.94 | 00:04:18.166 | Poland | Poland | Carry | - | [50.7, 11.2] |  |
| +4.91 | +3.24 | 00:04:18.460 | Poland | Poland | Dribble | - | [50.1, 12.5] |  |
| +4.91 | +3.24 | 00:04:18.460 | Netherlands | Netherlands | Duel | **YES** | [70.0, 67.6] |  |
| +4.91 | +3.24 | 00:04:18.460 | Netherlands | Netherlands | Carry | - | [70.0, 67.6] |  |
| +5.45 | +3.78 | 00:04:19.002 | Poland | Netherlands | Pressure | **YES** | [49.5, 11.2] |  |
| +7.17 | +5.50 | 00:04:20.726 | Netherlands | Netherlands | Pass | - | [64.8, 71.1] |  |
| +7.34 | +5.67 | 00:04:20.897 | Netherlands | Netherlands | Ball Receipt* | - | [73.6, 69.6] |  |
| +7.34 | +5.67 | 00:04:20.897 | Poland | Netherlands | Block | **YES** | [52.5, 9.2] |  |

---

### Episode 85: `3895052_p51_39424611`
- **Match**: `3895052` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Bayer Leverkusen** vs. Possession Team: **Bayer Leverkusen**
- **Initiation Action**: `Interception` by **Victor Okoh Boniface** at `00:28:55.323` (Turnover delay: 1.54s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Bayer Leverkusen. Harmless transition (opp max progression x=50.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.85 | -3.39 | 00:28:51.935 | RB Leipzig | RB Leipzig | Pass | - | [89.6, 5.7] |  |
| -1.52 | -3.06 | 00:28:52.265 | RB Leipzig | RB Leipzig | Ball Receipt* | - | [84.0, 5.1] |  |
| -1.52 | -3.06 | 00:28:52.265 | RB Leipzig | RB Leipzig | Carry | - | [84.0, 5.1] |  |
| -1.33 | -2.87 | 00:28:52.457 | Bayer Leverkusen | RB Leipzig | Pressure | - | [36.3, 73.8] |  |
| -0.91 | -2.46 | 00:28:52.868 | Bayer Leverkusen | RB Leipzig | Pressure | - | [35.1, 75.6] |  |
| -0.72 | -2.26 | 00:28:53.063 | RB Leipzig | RB Leipzig | Dispossessed | - | [83.7, 4.9] |  |
| -0.72 | -2.26 | 00:28:53.063 | Bayer Leverkusen | RB Leipzig | Duel | - | [36.4, 75.2] |  |
| +0.00 | -1.54 | 00:28:53.783 | RB Leipzig | RB Leipzig | Ball Recovery | - | [74.1, 5.7] | 🔄 **TURNOVER** |
| +0.00 | -1.54 | 00:28:53.783 | RB Leipzig | RB Leipzig | Carry | - | [74.1, 5.7] |  |
| +0.83 | -0.72 | 00:28:54.608 | RB Leipzig | RB Leipzig | Pass | - | [71.5, 6.5] |  |
| +1.54 | +0.00 | 00:28:55.323 | RB Leipzig | RB Leipzig | Ball Receipt* | - | [69.7, 15.7] |  |
| +1.54 | +0.00 | 00:28:55.323 | Bayer Leverkusen | Bayer Leverkusen | Interception | **YES** | [50.4, 63.2] | ⭐ **CP INITIATION** |
| +1.54 | +0.00 | 00:28:55.323 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [50.4, 63.2] |  |
| +2.79 | +1.25 | 00:28:56.569 | Bayer Leverkusen | Bayer Leverkusen | Dribble | - | [49.8, 62.0] |  |
| +2.79 | +1.25 | 00:28:56.569 | RB Leipzig | Bayer Leverkusen | Duel | **YES** | [70.3, 18.1] |  |
| +3.76 | +2.22 | 00:28:57.542 | Bayer Leverkusen | Bayer Leverkusen | Ball Recovery | - | [47.8, 63.0] |  |
| +3.76 | +2.22 | 00:28:57.542 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [47.8, 63.0] |  |
| +3.84 | +2.30 | 00:28:57.624 | RB Leipzig | Bayer Leverkusen | Pressure | **YES** | [69.7, 17.7] |  |
| +4.08 | +2.53 | 00:28:57.858 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [49.2, 65.2] |  |
| +5.12 | +3.58 | 00:28:58.902 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [49.0, 71.8] |  |
| +5.12 | +3.58 | 00:28:58.902 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [49.0, 71.8] |  |
| +6.42 | +4.88 | 00:29:00.198 | RB Leipzig | Bayer Leverkusen | Pressure | **YES** | [61.7, 8.5] |  |
| +7.19 | +5.65 | 00:29:00.972 | RB Leipzig | Bayer Leverkusen | Foul Committed | - | [56.6, 8.5] |  |
| +7.19 | +5.65 | 00:29:00.972 | Bayer Leverkusen | Bayer Leverkusen | Foul Won | - | [63.5, 71.6] |  |

---

### Episode 86: `3877194_p4_035cd5d0`
- **Match**: `3877194` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Inter Miami** vs. Possession Team: **Charlotte**
- **Initiation Action**: `Pressure` by **Benjamin Cremaschi** at `00:00:19.969` (Turnover delay: 1.906s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.906s). Harmless transition (opp max progression x=96.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.80 | -3.71 | 00:00:16.258 | Charlotte | Inter Miami | Pressure | **YES** | [72.0, 70.0] |  |
| -1.78 | -3.69 | 00:00:16.280 | Inter Miami | Inter Miami | Ball Receipt* | - | [47.5, 10.1] |  |
| -1.78 | -3.69 | 00:00:16.280 | Inter Miami | Inter Miami | Pass | - | [46.7, 9.8] |  |
| -0.82 | -2.72 | 00:00:17.246 | Inter Miami | Inter Miami | Ball Receipt* | - | [47.5, 3.5] |  |
| -0.82 | -2.72 | 00:00:17.246 | Inter Miami | Inter Miami | Pass | - | [46.7, 3.3] |  |
| +0.00 | -1.91 | 00:00:18.063 | Inter Miami | Inter Miami | Ball Receipt* | - | [20.7, 20.0] |  |
| +0.00 | -1.91 | 00:00:18.063 | Charlotte | Charlotte | Ball Recovery | - | [84.2, 68.6] | 🔄 **TURNOVER** |
| +0.00 | -1.91 | 00:00:18.063 | Charlotte | Charlotte | Carry | - | [84.2, 68.6] |  |
| +1.91 | +0.00 | 00:00:19.969 | Inter Miami | Charlotte | Pressure | **YES** | [30.8, 21.7] | ⭐ **CP INITIATION** |
| +3.03 | +1.12 | 00:00:21.091 | Charlotte | Charlotte | Pass | - | [83.4, 48.5] |  |
| +4.41 | +2.50 | 00:00:22.472 | Charlotte | Charlotte | Ball Receipt* | - | [83.4, 32.9] |  |
| +4.41 | +2.50 | 00:00:22.472 | Charlotte | Charlotte | Carry | - | [83.4, 32.9] |  |
| +6.95 | +5.05 | 00:00:25.017 | Charlotte | Charlotte | Pass | - | [85.6, 21.4] |  |
| +8.34 | +6.43 | 00:00:26.401 | Charlotte | Charlotte | Ball Receipt* | - | [96.3, 6.0] |  |
| +8.34 | +6.43 | 00:00:26.401 | Charlotte | Charlotte | Carry | - | [96.3, 6.0] |  |
| +8.82 | +6.91 | 00:00:26.884 | Charlotte | Charlotte | Pass | - | [95.8, 5.3] |  |
| +9.95 | +8.04 | 00:00:28.009 | Charlotte | Charlotte | Ball Receipt* | - | [85.1, 9.8] |  |
| +9.95 | +8.04 | 00:00:28.009 | Charlotte | Charlotte | Carry | - | [85.1, 9.8] |  |
| +11.36 | +9.45 | 00:00:29.423 | Charlotte | Charlotte | Pass | - | [85.0, 10.9] |  |
| +17.44 | +15.53 | 00:00:35.503 | Charlotte | Charlotte | Ball Receipt* | - | [106.0, 50.2] |  |

---

### Episode 87: `3877115_p56_fe835ae9`
- **Match**: `3877115` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Toronto FC** vs. Possession Team: **Toronto FC**
- **Initiation Action**: `Interception` by **Jonathan Osorio** at `00:33:10.995` (Turnover delay: 4.396s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.0s by Toronto FC. Harmless transition (opp max progression x=38.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.00 | -6.40 | 00:33:04.597 | Inter Miami | Inter Miami | Ball Receipt* | - | [67.9, 27.0] |  |
| -2.00 | -6.40 | 00:33:04.597 | Inter Miami | Inter Miami | Carry | - | [67.9, 27.0] |  |
| +0.00 | -4.40 | 00:33:06.599 | Inter Miami | Inter Miami | Pass | - | [68.7, 25.9] | 🔄 **TURNOVER** |
| +0.83 | -3.56 | 00:33:07.431 | Inter Miami | Inter Miami | Ball Receipt* | - | [74.7, 33.2] |  |
| +0.83 | -3.56 | 00:33:07.431 | Inter Miami | Inter Miami | Pass | - | [74.7, 33.2] |  |
| +1.70 | -2.69 | 00:33:08.300 | Inter Miami | Inter Miami | Ball Receipt* | - | [69.5, 24.3] |  |
| +1.70 | -2.69 | 00:33:08.300 | Inter Miami | Inter Miami | Carry | - | [69.5, 24.3] |  |
| +3.48 | -0.92 | 00:33:10.077 | Inter Miami | Inter Miami | Pass | - | [69.5, 24.3] |  |
| +4.40 | +0.00 | 00:33:10.995 | Inter Miami | Inter Miami | Ball Receipt* | - | [83.9, 27.6] |  |
| +4.40 | +0.00 | 00:33:10.995 | Toronto FC | Toronto FC | Interception | **YES** | [38.5, 55.8] | ⭐ **CP INITIATION** |
| +4.40 | +0.00 | 00:33:10.995 | Toronto FC | Toronto FC | Carry | - | [38.5, 55.8] |  |
| +10.48 | +6.08 | 00:33:17.075 | Toronto FC | Toronto FC | Pass | - | [79.3, 63.1] |  |
| +11.70 | +7.30 | 00:33:18.295 | Toronto FC | Toronto FC | Ball Receipt* | - | [82.0, 74.8] |  |
| +11.70 | +7.30 | 00:33:18.295 | Toronto FC | Toronto FC | Carry | - | [82.0, 74.8] |  |
| +11.74 | +7.34 | 00:33:18.335 | Toronto FC | Toronto FC | Pass | - | [83.1, 73.7] |  |
| +13.92 | +9.53 | 00:33:20.521 | Toronto FC | Toronto FC | Ball Receipt* | - | [104.7, 56.9] |  |
| +13.92 | +9.53 | 00:33:20.521 | Toronto FC | Toronto FC | Carry | - | [104.7, 56.9] |  |
| +14.12 | +9.73 | 00:33:20.723 | Toronto FC | Toronto FC | Pass | - | [104.7, 56.9] |  |
| +18.55 | +14.16 | 00:33:25.150 | Toronto FC | Toronto FC | Ball Receipt* | - | [104.5, 44.8] |  |

---

### Episode 88: `3895302_p125_16447969`
- **Match**: `3895302` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 2, Pressing Team: **Werder Bremen** vs. Possession Team: **Werder Bremen**
- **Initiation Action**: `Duel` by **Mitchell Weiser** at `00:34:24.216` (Turnover delay: 5.088s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.857s by Werder Bremen. Harmless transition (opp max progression x=47.0).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.07 | -7.16 | 00:34:17.056 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [55.2, 7.6] |  |
| -2.07 | -7.16 | 00:34:17.056 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [55.2, 7.6] |  |
| +0.00 | -5.09 | 00:34:19.128 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [56.8, 9.0] | 🔄 **TURNOVER** |
| +1.08 | -4.01 | 00:34:20.208 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [65.1, 3.4] |  |
| +1.08 | -4.01 | 00:34:20.208 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [65.1, 3.4] |  |
| +2.07 | -3.02 | 00:34:21.193 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [57.8, 10.2] |  |
| +2.07 | -3.02 | 00:34:21.193 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [57.8, 10.2] |  |
| +2.67 | -2.42 | 00:34:21.795 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [57.4, 7.6] |  |
| +3.46 | -1.63 | 00:34:22.585 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [68.5, 10.2] |  |
| +3.46 | -1.63 | 00:34:22.585 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [68.5, 10.2] |  |
| +5.09 | +0.00 | 00:34:24.216 | Bayer Leverkusen | Bayer Leverkusen | Dribble | - | [73.1, 9.2] |  |
| +5.09 | +0.00 | 00:34:24.216 | Werder Bremen | Werder Bremen | Duel | **YES** | [47.0, 70.9] | ⭐ **CP INITIATION** |
| +5.94 | +0.86 | 00:34:25.073 | Bayer Leverkusen | Werder Bremen | Pressure | **YES** | [70.7, 12.9] |  |
| +6.04 | +0.96 | 00:34:25.173 | Werder Bremen | Werder Bremen | Ball Recovery | - | [50.2, 65.5] |  |
| +6.04 | +0.96 | 00:34:25.173 | Werder Bremen | Werder Bremen | Carry | - | [50.2, 65.5] |  |
| +7.59 | +2.50 | 00:34:26.717 | Werder Bremen | Werder Bremen | Pass | - | [50.8, 57.0] |  |
| +8.85 | +3.76 | 00:34:27.975 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [51.6, 38.2] |  |
| +8.85 | +3.76 | 00:34:27.975 | Werder Bremen | Werder Bremen | Carry | - | [51.6, 38.2] |  |
| +9.70 | +4.61 | 00:34:28.829 | Werder Bremen | Werder Bremen | Pass | - | [51.6, 40.0] |  |
| +10.78 | +5.69 | 00:34:29.907 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [50.1, 49.5] |  |
| +10.78 | +5.69 | 00:34:29.907 | Werder Bremen | Werder Bremen | Carry | - | [50.1, 49.5] |  |
| +11.43 | +6.35 | 00:34:30.562 | Bayer Leverkusen | Werder Bremen | Pressure | - | [70.0, 34.9] |  |
| +11.64 | +6.55 | 00:34:30.769 | Werder Bremen | Werder Bremen | Pass | - | [52.0, 42.9] |  |
| +13.41 | +8.32 | 00:34:32.540 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [47.0, 19.4] |  |
| +13.41 | +8.32 | 00:34:32.540 | Werder Bremen | Werder Bremen | Carry | - | [47.0, 19.4] |  |
| +16.35 | +11.27 | 00:34:35.481 | Werder Bremen | Werder Bremen | Pass | - | [56.8, 23.6] |  |
| +17.75 | +12.66 | 00:34:36.880 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [48.3, 43.1] |  |
| +17.75 | +12.66 | 00:34:36.880 | Werder Bremen | Werder Bremen | Carry | - | [48.3, 43.1] |  |
| +18.92 | +13.83 | 00:34:38.048 | Werder Bremen | Werder Bremen | Pass | - | [48.7, 44.3] |  |
| +20.13 | +15.04 | 00:34:39.260 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [61.7, 61.5] |  |
| +20.13 | +15.04 | 00:34:39.260 | Werder Bremen | Werder Bremen | Carry | - | [61.7, 61.5] |  |
| +21.53 | +16.44 | 00:34:40.655 | Bayer Leverkusen | Werder Bremen | Pressure | - | [55.6, 17.1] |  |
| +23.10 | +18.01 | 00:34:42.225 | Werder Bremen | Werder Bremen | Pass | - | [69.2, 66.5] |  |
| +23.67 | +18.59 | 00:34:42.802 | Werder Bremen | Werder Bremen | Ball Receipt* | - | [72.8, 59.8] |  |
| +23.67 | +18.59 | 00:34:42.802 | Werder Bremen | Werder Bremen | Carry | - | [72.8, 59.8] |  |

---

### Episode 89: `3877170_p10_37e82900`
- **Match**: `3877170` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Inter Miami** vs. Possession Team: **Inter Miami**
- **Initiation Action**: `Pressure` by **Serhiy Kryvtsov** at `00:04:50.032` (Turnover delay: 2.192s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.341s by Inter Miami. Harmless transition (opp max progression x=115.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.54 | -4.73 | 00:04:45.299 | Inter Miami | Inter Miami | Pass | - | [82.2, 5.2] |  |
| +0.00 | -2.19 | 00:04:47.840 | Inter Miami | Inter Miami | Ball Receipt* | - | [74.7, 14.0] |  |
| +0.00 | -2.19 | 00:04:47.840 | Cincinnati | Inter Miami | Ball Recovery | - | [50.8, 54.6] | 🔄 **TURNOVER** |
| +0.00 | -2.19 | 00:04:47.840 | Cincinnati | Inter Miami | Carry | - | [50.8, 54.6] |  |
| +2.19 | +0.00 | 00:04:50.032 | Inter Miami | Inter Miami | Pressure | **YES** | [51.5, 35.3] | ⭐ **CP INITIATION** |
| +2.53 | +0.34 | 00:04:50.373 | Cincinnati | Inter Miami | Dribble | - | [69.6, 44.2] |  |
| +2.53 | +0.34 | 00:04:50.373 | Inter Miami | Inter Miami | Duel | **YES** | [50.5, 35.9] |  |
| +6.27 | +4.07 | 00:04:54.106 | Inter Miami | Inter Miami | Ball Recovery | - | [15.4, 32.9] |  |
| +6.27 | +4.07 | 00:04:54.106 | Inter Miami | Inter Miami | Carry | - | [15.4, 32.9] |  |
| +7.31 | +5.12 | 00:04:55.154 | Inter Miami | Inter Miami | Pass | - | [18.3, 34.3] |  |
| +8.64 | +6.45 | 00:04:56.484 | Inter Miami | Inter Miami | Ball Receipt* | - | [27.8, 39.5] |  |
| +9.14 | +6.94 | 00:04:56.977 | Inter Miami | Inter Miami | Pass | - | [33.7, 42.8] |  |
| +10.76 | +8.57 | 00:04:58.602 | Inter Miami | Inter Miami | Ball Receipt* | - | [46.2, 58.6] |  |
| +15.65 | +13.46 | 00:05:03.488 | Inter Miami | Inter Miami | Pass | - | [55.3, 59.2] |  |
| +17.48 | +15.29 | 00:05:05.323 | Inter Miami | Inter Miami | Ball Receipt* | - | [47.9, 61.8] |  |
| +17.48 | +15.29 | 00:05:05.323 | Inter Miami | Inter Miami | Carry | - | [47.9, 61.8] |  |
| +18.10 | +15.91 | 00:05:05.938 | Inter Miami | Inter Miami | Pass | - | [46.0, 58.8] |  |
| +19.38 | +17.19 | 00:05:07.220 | Inter Miami | Inter Miami | Ball Receipt* | - | [38.6, 42.3] |  |
| +21.62 | +19.42 | 00:05:09.456 | Inter Miami | Inter Miami | Pass | - | [38.6, 39.8] |  |

---

### Episode 90: `3930176_p61_41cce0ac`
- **Match**: `3930176` | **Competition**: UEFA Euro (2024)
- **Context**: Period 1, Pressing Team: **Switzerland** vs. Possession Team: **Germany**
- **Initiation Action**: `Pressure` by **Granit Xhaka** at `00:39:02.576` (Turnover delay: 1.22s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.22s). Dangerous transition triggered by: Final third entry at dt=4.566s (initial x=51.4, max x=114.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -1.85 | -3.07 | 00:38:59.509 | Switzerland | Switzerland | Ball Receipt* | - | [73.4, 68.6] |  |
| -1.85 | -3.07 | 00:38:59.509 | Switzerland | Switzerland | Pass | - | [73.7, 69.1] |  |
| -1.65 | -2.87 | 00:38:59.708 | Germany | Switzerland | Block | - | [45.0, 12.6] |  |
| -0.48 | -1.70 | 00:39:00.873 | Switzerland | Switzerland | Pressure | - | [66.8, 70.5] |  |
| +0.00 | -1.22 | 00:39:01.356 | Germany | Germany | Pass | - | [51.4, 7.1] | 🔄 **TURNOVER** |
| +1.22 | +0.00 | 00:39:02.576 | Switzerland | Germany | Pressure | **YES** | [57.8, 63.1] | ⭐ **CP INITIATION** |
| +1.37 | +0.15 | 00:39:02.722 | Germany | Germany | Ball Receipt* | - | [59.4, 15.7] |  |
| +1.37 | +0.15 | 00:39:02.722 | Germany | Germany | Carry | - | [59.4, 15.7] |  |
| +1.42 | +0.20 | 00:39:02.776 | Germany | Germany | Pass | - | [59.0, 15.6] |  |
| +3.28 | +2.06 | 00:39:04.637 | Germany | Germany | Ball Receipt* | - | [69.7, 7.1] |  |
| +3.28 | +2.06 | 00:39:04.637 | Germany | Germany | Carry | - | [69.7, 7.1] |  |
| +3.48 | +2.26 | 00:39:04.832 | Germany | Germany | Pass | - | [71.5, 7.6] |  |
| +5.79 | +4.57 | 00:39:07.142 | Germany | Germany | Pressure | - | [99.2, 15.7] |  |
| +6.48 | +5.26 | 00:39:07.832 | Germany | Germany | Ball Receipt* | - | [98.3, 17.0] |  |
| +6.48 | +5.26 | 00:39:07.832 | Switzerland | Germany | Pass | - | [15.7, 63.1] |  |
| +7.64 | +6.42 | 00:39:08.995 | Germany | Germany | Pressure | **YES** | [114.2, 28.1] |  |
| +8.35 | +7.13 | 00:39:09.707 | Switzerland | Germany | Ball Receipt* | - | [3.6, 44.7] |  |
| +8.35 | +7.13 | 00:39:09.707 | Switzerland | Germany | Carry | - | [3.6, 44.7] |  |
| +10.36 | +9.14 | 00:39:11.718 | Switzerland | Germany | Pass | - | [6.7, 35.5] |  |
| +12.95 | +11.73 | 00:39:14.302 | Germany | Germany | Ball Recovery | - | [63.1, 41.3] |  |
| +12.95 | +11.73 | 00:39:14.302 | Germany | Germany | Carry | - | [63.1, 41.3] |  |
| +14.42 | +13.20 | 00:39:15.776 | Germany | Germany | Pass | - | [71.4, 46.8] |  |
| +15.41 | +14.19 | 00:39:16.763 | Germany | Germany | Ball Receipt* | - | [72.8, 54.9] |  |
| +15.41 | +14.19 | 00:39:16.763 | Germany | Germany | Carry | - | [72.8, 54.9] |  |
| +19.08 | +17.86 | 00:39:20.432 | Germany | Germany | Pass | - | [85.8, 54.8] |  |
| +21.17 | +19.95 | 00:39:22.524 | Germany | Germany | Ball Receipt* | - | [97.2, 76.3] |  |
| +21.17 | +19.95 | 00:39:22.524 | Germany | Germany | Carry | - | [97.2, 76.3] |  |

---

### Episode 91: `3901735_p90_fe32d880`
- **Match**: `3901735` | **Competition**: Women's World Cup (2023)
- **Context**: Period 1, Pressing Team: **England Women's** vs. Possession Team: **Nigeria Women's**
- **Initiation Action**: `Pressure` by **Keira Walsh** at `00:42:06.304` (Turnover delay: 1.738s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.738s). Dangerous transition triggered by: Final third entry at dt=0.163s (initial x=73.4, max x=101.4).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.96 | -4.70 | 00:42:01.602 | England Women's | England Women's | Pressure | - | [55.0, 46.6] |  |
| -2.76 | -4.50 | 00:42:01.807 | England Women's | England Women's | Ball Receipt* | - | [53.5, 45.5] |  |
| -2.76 | -4.50 | 00:42:01.807 | Nigeria Women's | England Women's | Pass | - | [65.3, 34.6] |  |
| -1.28 | -3.02 | 00:42:03.288 | Nigeria Women's | England Women's | Ball Receipt* | - | [91.4, 39.7] |  |
| -1.28 | -3.02 | 00:42:03.288 | England Women's | England Women's | Clearance | - | [30.9, 37.2] |  |
| +0.00 | -1.74 | 00:42:04.566 | Nigeria Women's | Nigeria Women's | Pass | - | [73.4, 46.6] | 🔄 **TURNOVER** |
| +1.74 | +0.00 | 00:42:06.304 | England Women's | Nigeria Women's | Pressure | **YES** | [39.6, 29.0] | ⭐ **CP INITIATION** |
| +1.90 | +0.16 | 00:42:06.467 | Nigeria Women's | Nigeria Women's | Ball Receipt* | - | [80.3, 51.3] |  |
| +1.90 | +0.16 | 00:42:06.467 | Nigeria Women's | Nigeria Women's | Carry | - | [80.3, 51.3] |  |
| +4.63 | +2.89 | 00:42:09.195 | Nigeria Women's | Nigeria Women's | Pass | - | [80.7, 57.7] |  |
| +5.79 | +4.05 | 00:42:10.356 | Nigeria Women's | Nigeria Women's | Ball Receipt* | - | [91.8, 74.6] |  |
| +5.79 | +4.05 | 00:42:10.356 | Nigeria Women's | Nigeria Women's | Carry | - | [91.8, 74.6] |  |
| +9.28 | +7.54 | 00:42:13.842 | Nigeria Women's | Nigeria Women's | Pass | - | [93.3, 71.8] |  |
| +10.36 | +8.62 | 00:42:14.923 | Nigeria Women's | Nigeria Women's | Ball Receipt* | - | [101.4, 49.8] |  |
| +10.36 | +8.62 | 00:42:14.923 | Nigeria Women's | Nigeria Women's | Carry | - | [101.4, 49.8] |  |
| +10.40 | +8.66 | 00:42:14.963 | Nigeria Women's | Nigeria Women's | Miscontrol | - | [101.0, 50.2] |  |
| +11.59 | +9.85 | 00:42:16.156 | England Women's | Nigeria Women's | Clearance | - | [12.5, 41.6] |  |
| +14.69 | +12.95 | 00:42:19.251 | Nigeria Women's | Nigeria Women's | Pass | - | [92.2, 47.2] |  |
| +16.25 | +14.51 | 00:42:20.817 | Nigeria Women's | Nigeria Women's | Ball Receipt* | - | [90.9, 22.4] |  |
| +16.25 | +14.51 | 00:42:20.817 | Nigeria Women's | Nigeria Women's | Carry | - | [90.9, 22.4] |  |
| +17.66 | +15.92 | 00:42:22.223 | Nigeria Women's | Nigeria Women's | Pass | - | [92.2, 25.4] |  |
| +18.64 | +16.90 | 00:42:23.205 | Nigeria Women's | Nigeria Women's | Ball Receipt* | - | [98.9, 20.3] |  |
| +18.64 | +16.90 | 00:42:23.205 | Nigeria Women's | Nigeria Women's | Carry | - | [98.9, 20.3] |  |
| +19.21 | +17.47 | 00:42:23.772 | England Women's | Nigeria Women's | Pressure | - | [18.9, 65.8] |  |
| +21.52 | +19.78 | 00:42:26.089 | Nigeria Women's | Nigeria Women's | Pass | - | [101.6, 8.3] |  |

---

### Episode 92: `3869151_p150_6dc73411`
- **Match**: `3869151` | **Competition**: FIFA World Cup (2022)
- **Context**: Period 2, Pressing Team: **Australia** vs. Possession Team: **Argentina**
- **Initiation Action**: `Duel` by **Harry Souttar** at `00:47:36.951` (Turnover delay: 3.534s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=3.534s). Dangerous transition triggered by: Shot at dt=13.676s.

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.42 | -5.95 | 00:47:30.997 | Australia | Australia | Pass | - | [23.7, 13.0] |  |
| -1.61 | -5.15 | 00:47:31.804 | Australia | Australia | Ball Receipt* | - | [24.0, 7.2] |  |
| -1.61 | -5.15 | 00:47:31.804 | Australia | Australia | Carry | - | [24.0, 7.2] |  |
| -1.32 | -4.86 | 00:47:32.095 | Australia | Australia | Pass | - | [24.9, 6.1] |  |
| -0.28 | -3.82 | 00:47:33.132 | Argentina | Australia | Pressure | **YES** | [81.7, 66.8] |  |
| -0.13 | -3.66 | 00:47:33.289 | Australia | Australia | Ball Receipt* | - | [38.0, 13.3] |  |
| -0.13 | -3.66 | 00:47:33.289 | Australia | Australia | Carry | - | [38.0, 13.3] |  |
| +0.00 | -3.53 | 00:47:33.417 | Australia | Australia | Dispossessed | - | [38.4, 13.3] |  |
| +0.00 | -3.53 | 00:47:33.417 | Argentina | Argentina | Duel | **YES** | [81.7, 66.8] | 🔄 **TURNOVER** |
| +1.78 | -1.75 | 00:47:35.198 | Australia | Argentina | Pass | - | [38.6, 20.2] |  |
| +3.53 | +0.00 | 00:47:36.951 | Australia | Argentina | Ball Receipt* | - | [63.1, 18.3] |  |
| +3.53 | +0.00 | 00:47:36.951 | Australia | Argentina | Duel | **YES** | [62.2, 18.3] | ⭐ **CP INITIATION** |
| +3.53 | +0.00 | 00:47:36.951 | Argentina | Argentina | Pass | - | [57.9, 61.8] |  |
| +4.74 | +1.21 | 00:47:38.162 | Argentina | Argentina | Ball Receipt* | - | [68.9, 76.5] |  |
| +4.74 | +1.21 | 00:47:38.162 | Argentina | Argentina | Carry | - | [68.9, 76.5] |  |
| +7.83 | +4.30 | 00:47:41.250 | Argentina | Argentina | Pass | - | [74.1, 76.5] |  |
| +8.68 | +5.14 | 00:47:42.093 | Argentina | Argentina | Ball Receipt* | - | [77.1, 66.8] |  |
| +8.68 | +5.14 | 00:47:42.093 | Argentina | Argentina | Carry | - | [77.1, 66.8] |  |
| +9.33 | +5.79 | 00:47:42.742 | Australia | Argentina | Pressure | - | [41.7, 14.9] |  |
| +11.22 | +7.69 | 00:47:44.638 | Australia | Argentina | Dribbled Past | - | [29.2, 16.1] |  |
| +11.22 | +7.69 | 00:47:44.638 | Argentina | Argentina | Dribble | - | [90.9, 64.0] |  |
| +11.22 | +7.69 | 00:47:44.638 | Argentina | Argentina | Carry | - | [90.9, 64.0] |  |
| +17.21 | +13.68 | 00:47:50.627 | Argentina | Argentina | Shot | - | [104.6, 52.2] |  |
| +17.93 | +14.39 | 00:47:51.344 | Australia | Argentina | Goal Keeper | - | [3.0, 37.8] |  |

---

### Episode 93: `3794686_p34_f2b8ecdb`
- **Match**: `3794686` | **Competition**: UEFA Euro (2020)
- **Context**: Period 1, Pressing Team: **Croatia** vs. Possession Team: **Spain**
- **Initiation Action**: `Pressure` by **Nikola Vlašić** at `00:18:22.199` (Turnover delay: 2.428s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=2.428s). Dangerous transition triggered by: Shot at dt=14.022s; Final third entry at dt=9.634s (initial x=72.2, max x=115.1).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.31 | -4.73 | 00:18:17.465 | Croatia | Croatia | Pass | - | [38.3, 80.0] |  |
| -1.21 | -3.64 | 00:18:18.558 | Spain | Croatia | Pressure | - | [65.6, 3.0] |  |
| -1.04 | -3.47 | 00:18:18.730 | Croatia | Croatia | Ball Receipt* | - | [54.5, 77.1] |  |
| -1.04 | -3.47 | 00:18:18.730 | Croatia | Croatia | Miscontrol | - | [54.5, 77.1] |  |
| +0.00 | -2.43 | 00:18:19.771 | Spain | Spain | Pass | - | [72.2, 1.9] | 🔄 **TURNOVER** |
| +0.58 | -1.85 | 00:18:20.354 | Spain | Spain | Ball Receipt* | - | [68.6, 6.9] |  |
| +0.58 | -1.85 | 00:18:20.354 | Spain | Spain | Carry | - | [68.6, 6.9] |  |
| +2.43 | +0.00 | 00:18:22.199 | Croatia | Spain | Pressure | **YES** | [59.0, 71.3] | ⭐ **CP INITIATION** |
| +2.63 | +0.20 | 00:18:22.404 | Spain | Spain | Pass | - | [64.7, 8.5] |  |
| +4.42 | +1.99 | 00:18:24.191 | Spain | Spain | Ball Receipt* | - | [50.9, 25.8] |  |
| +4.42 | +1.99 | 00:18:24.191 | Spain | Spain | Carry | - | [50.9, 25.8] |  |
| +5.78 | +3.35 | 00:18:25.551 | Spain | Spain | Pass | - | [51.8, 37.7] |  |
| +6.95 | +4.52 | 00:18:26.717 | Spain | Spain | Ball Receipt* | - | [56.5, 26.4] |  |
| +6.95 | +4.52 | 00:18:26.717 | Spain | Spain | Pass | - | [56.5, 26.4] |  |
| +7.78 | +5.35 | 00:18:27.550 | Spain | Spain | Ball Receipt* | - | [65.9, 34.5] |  |
| +7.78 | +5.35 | 00:18:27.550 | Spain | Spain | Pass | - | [65.9, 34.5] |  |
| +8.71 | +6.28 | 00:18:28.479 | Spain | Spain | Ball Receipt* | - | [56.5, 27.8] |  |
| +8.71 | +6.28 | 00:18:28.479 | Spain | Spain | Pass | - | [57.8, 28.3] |  |
| +9.79 | +7.36 | 00:18:29.559 | Spain | Spain | Ball Receipt* | - | [76.4, 30.5] |  |
| +9.79 | +7.36 | 00:18:29.559 | Spain | Spain | Carry | - | [76.4, 30.5] |  |
| +12.06 | +9.63 | 00:18:31.833 | Spain | Spain | Pass | - | [84.5, 42.4] |  |
| +13.81 | +11.38 | 00:18:33.576 | Spain | Spain | Ball Receipt* | - | [105.1, 64.4] |  |
| +13.81 | +11.38 | 00:18:33.576 | Spain | Spain | Carry | - | [105.1, 64.4] |  |
| +15.31 | +12.88 | 00:18:35.076 | Spain | Spain | Pass | - | [111.7, 63.8] |  |
| +16.45 | +14.02 | 00:18:36.221 | Spain | Spain | Ball Receipt* | - | [113.9, 33.8] |  |
| +16.45 | +14.02 | 00:18:36.221 | Spain | Spain | Shot | - | [115.1, 34.4] |  |
| +16.58 | +14.15 | 00:18:36.351 | Croatia | Spain | Block | - | [3.9, 44.4] |  |
| +16.70 | +14.27 | 00:18:36.471 | Croatia | Spain | Goal Keeper | - | [1.6, 39.2] |  |
| +17.33 | +14.90 | 00:18:37.100 | Croatia | Spain | Ball Recovery | - | [3.1, 42.9] |  |

---

### Episode 94: `3877170_p123_6b247e0a`
- **Match**: `3877170` | **Competition**: Major League Soccer (2023)
- **Context**: Period 2, Pressing Team: **Inter Miami** vs. Possession Team: **Cincinnati**
- **Initiation Action**: `Pressure` by **Kamal Miller** at `00:20:51.927` (Turnover delay: 1.648s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.648s). Dangerous transition triggered by: Final third entry at dt=0.085s (initial x=61.1, max x=109.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.37 | -4.02 | 00:20:47.905 | Inter Miami | Inter Miami | Pass | - | [41.1, 14.6] |  |
| -1.49 | -3.14 | 00:20:48.788 | Inter Miami | Inter Miami | Ball Receipt* | - | [54.8, 10.1] |  |
| -1.49 | -3.14 | 00:20:48.788 | Inter Miami | Inter Miami | Carry | - | [54.8, 10.1] |  |
| -1.36 | -3.01 | 00:20:48.920 | Inter Miami | Inter Miami | Miscontrol | - | [54.8, 10.1] |  |
| +0.00 | -1.65 | 00:20:50.279 | Cincinnati | Cincinnati | Pass | - | [61.1, 73.4] | 🔄 **TURNOVER** |
| +1.12 | -0.52 | 00:20:51.404 | Cincinnati | Cincinnati | Ball Receipt* | - | [77.9, 71.7] |  |
| +1.12 | -0.52 | 00:20:51.404 | Cincinnati | Cincinnati | Carry | - | [77.9, 71.7] |  |
| +1.65 | +0.00 | 00:20:51.927 | Inter Miami | Cincinnati | Pressure | **YES** | [36.9, 11.5] | ⭐ **CP INITIATION** |
| +1.73 | +0.09 | 00:20:52.012 | Cincinnati | Cincinnati | Pass | - | [82.9, 74.0] |  |
| +2.62 | +0.97 | 00:20:52.896 | Cincinnati | Cincinnati | Ball Receipt* | - | [83.5, 60.5] |  |
| +2.62 | +0.97 | 00:20:52.896 | Cincinnati | Cincinnati | Carry | - | [83.5, 60.5] |  |
| +3.38 | +1.74 | 00:20:53.664 | Cincinnati | Cincinnati | Pass | - | [85.2, 60.8] |  |
| +4.89 | +3.24 | 00:20:55.170 | Cincinnati | Cincinnati | Ball Receipt* | - | [100.9, 61.3] |  |
| +4.89 | +3.24 | 00:20:55.170 | Cincinnati | Cincinnati | Carry | - | [100.9, 61.3] |  |
| +5.17 | +3.52 | 00:20:55.450 | Cincinnati | Cincinnati | Pass | - | [100.0, 61.3] |  |
| +6.45 | +4.80 | 00:20:56.731 | Cincinnati | Cincinnati | Ball Receipt* | - | [109.6, 36.1] |  |

---

### Episode 95: `3877060_p37_60a7ae6e`
- **Match**: `3877060` | **Competition**: Major League Soccer (2023)
- **Context**: Period 1, Pressing Team: **Inter Miami** vs. Possession Team: **Inter Miami**
- **Initiation Action**: `Pressure` by **Diego Alexander Gómez Amarilla** at `00:21:25.270` (Turnover delay: 1.491s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=0.989s by Inter Miami. Harmless transition (opp max progression x=5.2).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.81 | -4.30 | 00:21:20.974 | New York Red Bulls | Inter Miami | Pressure | - | [90.4, 5.9] |  |
| -2.71 | -4.20 | 00:21:21.066 | Inter Miami | Inter Miami | Pass | - | [33.1, 75.2] |  |
| +0.00 | -1.49 | 00:21:23.779 | Inter Miami | Inter Miami | Ball Receipt* | - | [46.0, 43.0] |  |
| +0.00 | -1.49 | 00:21:23.779 | New York Red Bulls | Inter Miami | Pass | - | [75.6, 34.7] | 🔄 **TURNOVER** |
| +1.09 | -0.40 | 00:21:24.870 | New York Red Bulls | Inter Miami | Ball Receipt* | - | [78.3, 10.7] |  |
| +1.09 | -0.40 | 00:21:24.870 | New York Red Bulls | Inter Miami | Carry | - | [78.3, 10.7] |  |
| +1.49 | +0.00 | 00:21:25.270 | Inter Miami | Inter Miami | Pressure | **YES** | [40.9, 65.7] | ⭐ **CP INITIATION** |
| +2.48 | +0.99 | 00:21:26.259 | New York Red Bulls | Inter Miami | Dispossessed | - | [76.3, 18.1] |  |
| +2.48 | +0.99 | 00:21:26.259 | Inter Miami | Inter Miami | Duel | **YES** | [43.8, 62.0] |  |
| +2.48 | +0.99 | 00:21:26.259 | Inter Miami | Inter Miami | Carry | - | [43.8, 62.0] |  |
| +3.27 | +1.78 | 00:21:27.049 | Inter Miami | Inter Miami | Pass | - | [44.2, 55.7] |  |
| +4.73 | +3.24 | 00:21:28.505 | Inter Miami | Inter Miami | Ball Receipt* | - | [48.3, 50.9] |  |
| +4.73 | +3.24 | 00:21:28.505 | New York Red Bulls | Inter Miami | Pass | - | [65.8, 30.1] |  |
| +8.28 | +6.79 | 00:21:32.063 | New York Red Bulls | Inter Miami | Ball Receipt* | - | [93.8, 52.5] |  |
| +8.28 | +6.79 | 00:21:32.063 | Inter Miami | Inter Miami | Ball Recovery | - | [13.0, 32.3] |  |
| +8.28 | +6.79 | 00:21:32.063 | Inter Miami | Inter Miami | Carry | - | [13.0, 32.3] |  |
| +8.92 | +7.43 | 00:21:32.699 | Inter Miami | Inter Miami | Pass | - | [14.9, 28.8] |  |
| +11.06 | +9.57 | 00:21:34.840 | Inter Miami | Inter Miami | Ball Receipt* | - | [49.5, 2.7] |  |
| +11.06 | +9.57 | 00:21:34.840 | Inter Miami | Inter Miami | Carry | - | [49.5, 2.7] |  |
| +12.73 | +11.24 | 00:21:36.510 | Inter Miami | Inter Miami | Pass | - | [52.2, 2.9] |  |
| +13.83 | +12.34 | 00:21:37.605 | Inter Miami | Inter Miami | Ball Receipt* | - | [45.7, 12.4] |  |
| +13.83 | +12.34 | 00:21:37.605 | Inter Miami | Inter Miami | Carry | - | [45.7, 12.4] |  |
| +15.07 | +13.58 | 00:21:38.851 | New York Red Bulls | Inter Miami | Pressure | - | [66.4, 64.6] |  |
| +15.74 | +14.25 | 00:21:39.518 | Inter Miami | Inter Miami | Dribble | - | [50.7, 16.3] |  |
| +15.74 | +14.25 | 00:21:39.518 | New York Red Bulls | Inter Miami | Duel | - | [69.4, 63.8] |  |
| +17.43 | +15.94 | 00:21:41.207 | Inter Miami | Inter Miami | 50/50 | - | [41.2, 12.9] |  |
| +17.43 | +15.94 | 00:21:41.207 | New York Red Bulls | Inter Miami | 50/50 | - | [78.9, 67.2] |  |

---

### Episode 96: `3998856_p58_d7cc3c68`
- **Match**: `3998856` | **Competition**: UEFA Women's Euro (2025)
- **Context**: Period 1, Pressing Team: **Sweden Women's** vs. Possession Team: **Germany Women's**
- **Initiation Action**: `Pressure` by **Hanna Ulrika Bennison** at `00:28:09.554` (Turnover delay: 1.265s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=1.265s). Harmless transition (opp max progression x=35.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.56 | -3.83 | 00:28:05.728 | Sweden Women's | Sweden Women's | Pass | - | [110.0, 74.2] |  |
| +0.00 | -1.27 | 00:28:08.289 | Sweden Women's | Sweden Women's | Duel | - | [99.3, 52.3] |  |
| +0.00 | -1.27 | 00:28:08.289 | Germany Women's | Germany Women's | Pass | - | [20.8, 27.8] | 🔄 **TURNOVER** |
| +1.27 | +0.00 | 00:28:09.554 | Sweden Women's | Germany Women's | Pressure | **YES** | [90.9, 64.3] | ⭐ **CP INITIATION** |
| +1.77 | +0.50 | 00:28:10.055 | Germany Women's | Germany Women's | Ball Receipt* | - | [29.2, 17.8] |  |
| +1.77 | +0.50 | 00:28:10.055 | Germany Women's | Germany Women's | Carry | - | [29.2, 17.8] |  |
| +2.84 | +1.57 | 00:28:11.124 | Sweden Women's | Germany Women's | Pressure | **YES** | [92.7, 65.8] |  |
| +3.17 | +1.90 | 00:28:11.457 | Germany Women's | Germany Women's | Pass | - | [26.9, 12.4] |  |
| +5.06 | +3.79 | 00:28:13.344 | Sweden Women's | Germany Women's | Ball Recovery | - | [88.1, 74.2] |  |
| +5.57 | +4.31 | 00:28:13.861 | Germany Women's | Germany Women's | Ball Recovery | - | [32.0, 4.3] |  |
| +5.57 | +4.31 | 00:28:13.861 | Germany Women's | Germany Women's | Carry | - | [32.0, 4.3] |  |
| +6.15 | +4.88 | 00:28:14.436 | Sweden Women's | Germany Women's | Pressure | - | [84.3, 75.1] |  |
| +6.58 | +5.32 | 00:28:14.872 | Germany Women's | Germany Women's | Pass | - | [35.3, 2.2] |  |
| +7.08 | +5.81 | 00:28:15.369 | Sweden Women's | Sweden Women's | Ball Recovery | - | [89.4, 71.0] |  |
| +7.08 | +5.81 | 00:28:15.369 | Sweden Women's | Sweden Women's | Carry | - | [89.4, 71.0] |  |
| +7.91 | +6.65 | 00:28:16.204 | Germany Women's | Sweden Women's | Pressure | **YES** | [30.7, 9.1] |  |
| +8.50 | +7.24 | 00:28:16.790 | Sweden Women's | Sweden Women's | Pass | - | [92.2, 71.3] |  |
| +11.07 | +9.81 | 00:28:19.360 | Germany Women's | Sweden Women's | Pressure | **YES** | [8.0, 23.5] |  |
| +11.25 | +9.98 | 00:28:19.538 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [113.9, 61.2] |  |
| +11.25 | +9.98 | 00:28:19.538 | Sweden Women's | Sweden Women's | Pass | - | [113.8, 57.1] |  |
| +12.73 | +11.46 | 00:28:21.018 | Germany Women's | Sweden Women's | Clearance | - | [8.9, 41.4] |  |
| +14.61 | +13.35 | 00:28:22.902 | Germany Women's | Sweden Women's | Clearance | - | [6.6, 26.2] |  |
| +16.73 | +15.47 | 00:28:25.024 | Sweden Women's | Sweden Women's | Ball Recovery | - | [85.8, 53.9] |  |
| +16.73 | +15.47 | 00:28:25.024 | Sweden Women's | Sweden Women's | Carry | - | [85.8, 53.9] |  |
| +17.62 | +16.36 | 00:28:25.912 | Germany Women's | Sweden Women's | Pressure | - | [27.5, 30.6] |  |
| +17.72 | +16.46 | 00:28:26.012 | Sweden Women's | Sweden Women's | Pass | - | [91.6, 51.5] |  |
| +18.44 | +17.18 | 00:28:26.730 | Germany Women's | Sweden Women's | Pressure | - | [21.4, 33.8] |  |
| +18.45 | +17.19 | 00:28:26.743 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [98.1, 47.7] |  |
| +18.45 | +17.19 | 00:28:26.743 | Sweden Women's | Sweden Women's | Carry | - | [98.1, 47.7] |  |
| +18.47 | +17.21 | 00:28:26.764 | Sweden Women's | Sweden Women's | Pass | - | [97.7, 48.5] |  |
| +19.15 | +17.89 | 00:28:27.440 | Sweden Women's | Sweden Women's | Ball Receipt* | - | [99.7, 52.8] |  |
| +19.15 | +17.89 | 00:28:27.440 | Sweden Women's | Sweden Women's | Carry | - | [99.7, 52.8] |  |
| +19.26 | +17.99 | 00:28:27.544 | Sweden Women's | Sweden Women's | Miscontrol | - | [100.4, 52.9] |  |
| +19.86 | +18.59 | 00:28:28.146 | Sweden Women's | Sweden Women's | Pressure | - | [102.8, 53.2] |  |
| +19.97 | +18.71 | 00:28:28.262 | Germany Women's | Sweden Women's | Pass | - | [15.8, 27.2] |  |
| +20.47 | +19.21 | 00:28:28.760 | Germany Women's | Sweden Women's | Ball Receipt* | - | [21.0, 29.0] |  |
| +20.47 | +19.21 | 00:28:28.760 | Germany Women's | Sweden Women's | Carry | - | [21.0, 29.0] |  |
| +20.87 | +19.61 | 00:28:29.161 | Germany Women's | Sweden Women's | Miscontrol | - | [21.0, 29.4] |  |
| +20.97 | +19.71 | 00:28:29.261 | Germany Women's | Sweden Women's | Pressure | - | [21.0, 29.4] |  |
| +21.24 | +19.97 | 00:28:29.528 | Sweden Women's | Sweden Women's | Pass | - | [98.5, 52.1] |  |

---

### Episode 97: `3895220_p58_361f8f3a`
- **Match**: `3895220` | **Competition**: 1. Bundesliga (2023/2024)
- **Context**: Period 1, Pressing Team: **Bayer Leverkusen** vs. Possession Team: **Darmstadt 98**
- **Initiation Action**: `Pressure` by **Florian Wirtz** at `00:29:08.115` (Turnover delay: 0.51s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=0.51s). Dangerous transition triggered by: Final third entry at dt=5.541s (initial x=61.2, max x=83.9).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.88 | -3.39 | 00:29:04.727 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [52.8, 37.0] |  |
| -2.34 | -2.85 | 00:29:05.264 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [49.5, 41.9] |  |
| -2.34 | -2.85 | 00:29:05.264 | Bayer Leverkusen | Bayer Leverkusen | Pass | - | [49.8, 41.9] |  |
| -0.88 | -1.39 | 00:29:06.723 | Darmstadt 98 | Bayer Leverkusen | Pressure | - | [56.3, 54.5] |  |
| -0.41 | -0.92 | 00:29:07.190 | Bayer Leverkusen | Bayer Leverkusen | Ball Receipt* | - | [59.9, 24.9] |  |
| -0.41 | -0.92 | 00:29:07.190 | Bayer Leverkusen | Bayer Leverkusen | Carry | - | [59.9, 24.9] |  |
| +0.00 | -0.51 | 00:29:07.605 | Bayer Leverkusen | Bayer Leverkusen | Dispossessed | - | [58.9, 24.4] |  |
| +0.00 | -0.51 | 00:29:07.605 | Darmstadt 98 | Darmstadt 98 | Duel | **YES** | [61.2, 55.7] | 🔄 **TURNOVER** |
| +0.00 | -0.51 | 00:29:07.605 | Darmstadt 98 | Darmstadt 98 | Carry | - | [61.2, 55.7] |  |
| +0.51 | +0.00 | 00:29:08.115 | Bayer Leverkusen | Darmstadt 98 | Pressure | **YES** | [57.6, 20.5] | ⭐ **CP INITIATION** |
| +6.05 | +5.54 | 00:29:13.656 | Darmstadt 98 | Darmstadt 98 | Pass | - | [83.9, 76.8] |  |
| +7.31 | +6.80 | 00:29:14.915 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [69.7, 70.9] |  |
| +7.31 | +6.80 | 00:29:14.915 | Darmstadt 98 | Darmstadt 98 | Carry | - | [69.7, 70.9] |  |
| +8.42 | +7.91 | 00:29:16.024 | Darmstadt 98 | Darmstadt 98 | Pass | - | [65.3, 68.5] |  |
| +10.36 | +9.85 | 00:29:17.966 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [46.0, 56.3] |  |
| +10.36 | +9.85 | 00:29:17.966 | Darmstadt 98 | Darmstadt 98 | Carry | - | [46.0, 56.3] |  |
| +12.15 | +11.64 | 00:29:19.759 | Darmstadt 98 | Darmstadt 98 | Pass | - | [46.0, 55.5] |  |
| +13.41 | +12.90 | 00:29:21.016 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [40.3, 33.2] |  |
| +13.41 | +12.90 | 00:29:21.016 | Darmstadt 98 | Darmstadt 98 | Carry | - | [40.3, 33.2] |  |
| +14.64 | +14.13 | 00:29:22.249 | Darmstadt 98 | Darmstadt 98 | Pass | - | [41.9, 31.5] |  |
| +16.22 | +15.71 | 00:29:23.829 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [43.7, 14.1] |  |
| +16.22 | +15.71 | 00:29:23.829 | Darmstadt 98 | Darmstadt 98 | Carry | - | [43.7, 14.1] |  |
| +16.90 | +16.39 | 00:29:24.501 | Darmstadt 98 | Darmstadt 98 | Pass | - | [45.0, 13.5] |  |
| +18.23 | +17.72 | 00:29:25.840 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [65.6, 6.1] |  |
| +18.23 | +17.72 | 00:29:25.840 | Darmstadt 98 | Darmstadt 98 | Pass | - | [63.9, 6.1] |  |
| +19.60 | +19.09 | 00:29:27.206 | Darmstadt 98 | Darmstadt 98 | Ball Receipt* | - | [63.5, 17.4] |  |
| +19.60 | +19.09 | 00:29:27.206 | Darmstadt 98 | Darmstadt 98 | Carry | - | [63.5, 17.4] |  |
| +19.62 | +19.11 | 00:29:27.220 | Bayer Leverkusen | Darmstadt 98 | Pressure | - | [61.0, 64.6] |  |

---

### Episode 98: `3773369_p100_81c81345`
- **Match**: `3773369` | **Competition**: La Liga (2020/2021)
- **Context**: Period 2, Pressing Team: **Barcelona** vs. Possession Team: **Barcelona**
- **Initiation Action**: `Pressure` by **Sergio Busquets i Burgos** at `00:07:09.697` (Turnover delay: 3.536s)
- **Algorithm Classification**: `successful_regain` (Regain 5s: 1, Dangerous Escape 15s: 0)
- **Rationale**: Regained possession at dt=1.202s by Barcelona. Harmless transition (opp max progression x=23.6).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -0.13 | -3.66 | 00:07:06.033 | Barcelona | Barcelona | Pass | - | [62.3, 29.6] |  |
| +0.00 | -3.54 | 00:07:06.161 | Barcelona | Barcelona | Ball Receipt* | - | [56.8, 62.2] |  |
| +0.00 | -3.54 | 00:07:06.161 | Huesca | Barcelona | Block | - | [57.4, 43.7] | 🔄 **TURNOVER** |
| +2.11 | -1.43 | 00:07:08.268 | Huesca | Barcelona | Ball Recovery | - | [42.9, 26.2] |  |
| +2.11 | -1.43 | 00:07:08.268 | Huesca | Barcelona | Carry | - | [42.9, 26.2] |  |
| +3.54 | +0.00 | 00:07:09.697 | Barcelona | Barcelona | Pressure | **YES** | [62.7, 51.3] | ⭐ **CP INITIATION** |
| +4.74 | +1.20 | 00:07:10.899 | Huesca | Barcelona | Dribble | - | [56.3, 31.1] |  |
| +4.74 | +1.20 | 00:07:10.899 | Barcelona | Barcelona | Duel | **YES** | [63.8, 49.0] |  |
| +4.74 | +1.20 | 00:07:10.899 | Barcelona | Barcelona | Carry | - | [63.8, 49.0] |  |
| +6.73 | +3.19 | 00:07:12.889 | Barcelona | Barcelona | Pass | - | [71.2, 42.6] |  |
| +7.57 | +4.03 | 00:07:13.728 | Barcelona | Barcelona | Ball Receipt* | - | [80.7, 34.6] |  |
| +7.57 | +4.03 | 00:07:13.728 | Barcelona | Barcelona | Carry | - | [80.7, 34.6] |  |
| +7.86 | +4.32 | 00:07:14.020 | Barcelona | Barcelona | Pass | - | [81.3, 34.8] |  |
| +8.72 | +5.18 | 00:07:14.878 | Barcelona | Barcelona | Ball Receipt* | - | [73.9, 27.4] |  |
| +8.72 | +5.18 | 00:07:14.878 | Barcelona | Barcelona | Carry | - | [73.9, 27.4] |  |
| +12.15 | +8.62 | 00:07:18.314 | Huesca | Barcelona | Pressure | - | [28.7, 52.9] |  |
| +12.28 | +8.74 | 00:07:18.440 | Barcelona | Barcelona | Pass | - | [89.7, 23.1] |  |
| +13.12 | +9.59 | 00:07:19.283 | Barcelona | Barcelona | Ball Receipt* | - | [107.4, 22.9] |  |
| +13.12 | +9.59 | 00:07:19.283 | Barcelona | Barcelona | Carry | - | [107.4, 22.9] |  |
| +15.94 | +12.41 | 00:07:22.103 | Huesca | Barcelona | Pressure | - | [4.4, 54.4] |  |
| +16.73 | +13.20 | 00:07:22.894 | Barcelona | Barcelona | Pass | - | [117.1, 22.0] |  |
| +17.11 | +13.57 | 00:07:23.271 | Barcelona | Barcelona | Ball Receipt* | - | [109.1, 30.3] |  |
| +17.11 | +13.57 | 00:07:23.271 | Huesca | Barcelona | Block | - | [5.7, 55.4] |  |

---

### Episode 99: `3893787_p109_e5f4d6e0`
- **Match**: `3893787` | **Competition**: Women's World Cup (2023)
- **Context**: Period 2, Pressing Team: **Norway Women's** vs. Possession Team: **New Zealand Women's**
- **Initiation Action**: `Pressure` by **Guro Reiten** at `00:06:03.658` (Turnover delay: 1.003s)
- **Algorithm Classification**: `dangerous_escape` (Regain 5s: 0, Dangerous Escape 15s: 1)
- **Rationale**: No regain within 5.0s (delay=1.003s). Dangerous transition triggered by: Shot at dt=5.008s; Final third entry at dt=3.943s (initial x=60.2, max x=113.3).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| +0.00 | -1.00 | 00:06:02.655 | Norway Women's | Norway Women's | Ball Receipt* | - | [59.9, 32.5] |  |
| +0.00 | -1.00 | 00:06:02.655 | New Zealand Women's | New Zealand Women's | Ball Recovery | - | [60.2, 49.5] | 🔄 **TURNOVER** |
| +0.00 | -1.00 | 00:06:02.655 | New Zealand Women's | New Zealand Women's | Carry | - | [60.2, 49.5] |  |
| +1.00 | +0.00 | 00:06:03.658 | Norway Women's | New Zealand Women's | Pressure | **YES** | [55.4, 27.0] | ⭐ **CP INITIATION** |
| +1.33 | +0.32 | 00:06:03.981 | New Zealand Women's | New Zealand Women's | Pass | - | [64.7, 53.1] |  |
| +4.95 | +3.94 | 00:06:07.601 | New Zealand Women's | New Zealand Women's | Ball Receipt* | - | [105.5, 59.1] |  |
| +4.96 | +3.96 | 00:06:07.618 | Norway Women's | New Zealand Women's | Pressure | **YES** | [14.0, 22.3] |  |
| +6.01 | +5.01 | 00:06:08.666 | New Zealand Women's | New Zealand Women's | Shot | - | [105.5, 59.1] |  |
| +6.11 | +5.11 | 00:06:08.764 | Norway Women's | New Zealand Women's | Block | - | [13.8, 22.0] |  |
| +6.36 | +5.35 | 00:06:09.013 | Norway Women's | New Zealand Women's | Goal Keeper | - | [3.1, 35.2] |  |
| +8.00 | +7.00 | 00:06:10.653 | New Zealand Women's | New Zealand Women's | Pressure | - | [113.3, 59.9] |  |
| +8.75 | +7.75 | 00:06:11.403 | Norway Women's | New Zealand Women's | Clearance | - | [6.8, 20.2] |  |

---

### Episode 100: `3802818_p28_75590d02`
- **Match**: `3802818` | **Competition**: Ligue 1 (2021/2022)
- **Context**: Period 1, Pressing Team: **Paris Saint-Germain** vs. Possession Team: **Lorient**
- **Initiation Action**: `Pressure` by **Danilo Luís Hélio Pereira** at `00:16:25.636` (Turnover delay: 3.247s)
- **Algorithm Classification**: `harmless_escape` (Regain 5s: 0, Dangerous Escape 15s: 0)
- **Rationale**: No regain within 5.0s (delay=3.247s). Harmless transition (opp max progression x=47.5).

**Chronological Event Sequence:**

| Rel To TO (s) | Rel To Init (s) | Timestamp | Team | Poss Team | Event Type | CP? | Location [x, y] | Notes |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| -2.79 | -6.04 | 00:16:19.596 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [96.9, 70.4] |  |
| -1.11 | -4.36 | 00:16:21.275 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [110.2, 73.7] |  |
| -1.11 | -4.36 | 00:16:21.275 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [110.2, 73.7] |  |
| -0.95 | -4.20 | 00:16:21.435 | Paris Saint-Germain | Paris Saint-Germain | Pass | - | [110.2, 73.7] |  |
| -0.07 | -3.32 | 00:16:22.318 | Paris Saint-Germain | Paris Saint-Germain | Ball Receipt* | - | [105.5, 51.8] |  |
| -0.07 | -3.32 | 00:16:22.318 | Paris Saint-Germain | Paris Saint-Germain | Carry | - | [105.5, 51.8] |  |
| -0.03 | -3.28 | 00:16:22.357 | Paris Saint-Germain | Paris Saint-Germain | Miscontrol | - | [105.5, 51.8] |  |
| +0.00 | -3.25 | 00:16:22.389 | Lorient | Paris Saint-Germain | Pressure | - | [15.9, 28.1] | 🔄 **TURNOVER** |
| +1.40 | -1.85 | 00:16:23.786 | Lorient | Lorient | Ball Recovery | - | [15.0, 25.9] |  |
| +1.40 | -1.85 | 00:16:23.786 | Lorient | Lorient | Carry | - | [15.0, 25.9] |  |
| +3.25 | +0.00 | 00:16:25.636 | Paris Saint-Germain | Lorient | Pressure | **YES** | [96.0, 59.1] | ⭐ **CP INITIATION** |
| +3.89 | +0.64 | 00:16:26.279 | Lorient | Lorient | Pass | - | [23.2, 23.5] |  |
| +4.50 | +1.25 | 00:16:26.886 | Lorient | Lorient | Ball Receipt* | - | [23.2, 15.9] |  |
| +4.50 | +1.25 | 00:16:26.886 | Lorient | Lorient | Carry | - | [23.2, 15.9] |  |
| +9.56 | +6.32 | 00:16:31.954 | Lorient | Lorient | Pass | - | [47.5, 9.0] |  |
| +10.30 | +7.05 | 00:16:32.687 | Lorient | Lorient | Ball Receipt* | - | [44.5, 16.3] |  |
| +10.30 | +7.05 | 00:16:32.687 | Lorient | Lorient | Carry | - | [44.5, 16.3] |  |
| +10.38 | +7.13 | 00:16:32.768 | Paris Saint-Germain | Lorient | Pressure | - | [73.9, 62.9] |  |
| +11.29 | +8.05 | 00:16:33.684 | Paris Saint-Germain | Lorient | Foul Committed | - | [74.9, 64.3] |  |
| +11.29 | +8.05 | 00:16:33.684 | Lorient | Lorient | Foul Won | - | [45.2, 15.8] |  |
| +22.78 | +19.54 | 00:16:45.174 | Lorient | Lorient | Pass | - | [53.9, 11.2] |  |

---
