# Counterpress Initiation Delays > 5.0 Seconds: Comprehensive Audit & Validation Report

## 1. Executive Summary & Delay Distribution

In Iteration 2, automated extraction revealed that **2,376 out of 29,186 episodes (8.14%)** exhibited an initiation delay exceeding the standard 5.0-second counterpress window. This conflicts with StatsBomb's conceptual definition of counterpressing and was flagged for rigorous investigation.

### Overall Distribution of Delays > 5.0s:
- **Total Episodes > 5.0s**: **2,376** (8.141% of total)
- **Minimum Delay**: 5.001 seconds
- **25th Percentile**: 5.806 seconds
- **Median Delay**: 6.614 seconds
- **75th Percentile**: 7.332 seconds
- **95th Percentile**: 7.865 seconds
- **Maximum Delay**: 8.000 seconds

### Delay Bins:
| Delay Interval | Episode Count | Percentage of >5s Cases | Cumulative Percentage |
| :--- | :--- | :--- | :--- |
| **5.0 – 6.0 sec** | 748 | 31.48% | 31.48% |
| **6.0 – 8.0 sec** | 1,628 | 68.52% | 100.00% |
| **8.0 – 10.0 sec** | 0 | 0.00% | 100.00% |
| **> 10.0 sec** | 0 | 0.00% | 100.00% |

> [!IMPORTANT]
> **Key Finding**: **31.5% of all >5s delays fall between 5.001s and 6.000s**. While marginal delays may reflect observational differences or pass flight time, the exact cause cannot be confirmed from event logs alone. All cases exceeding 5.0s are excluded from the primary cohort.

---

## 2. Categorization by Operational Audit Categories

Every delay > 5.0s was classified into five operational audit categories (assigned algorithmically based on event patterns, not proven underlying causes):

| Cause Code | Cause Description | Episode Count | Pct of >5s Cases |
| :--- | :--- | :--- | :--- |
| **Cause A** | Turnover detector linked to wrong turnover (e.g. earlier pass in multi-pass sequence) | 142 | 5.98% |
| **Cause B** | StatsBomb possession indexing delayed the apparent turnover | 18 | 0.76% |
| **Cause C** | Multiple contested events (duels, aerial headers, 50/50s) before clear turnover | 325 | 13.68% |
| **Cause D** | Ambiguous timestamp or simultaneous event sequence | 1,180 | 49.66% |
| **Cause E** | Episode genuinely cannot be linked to a turnover within 5 seconds | 711 | 29.92% |

### Breakdown by Competition:
| Competition | Count > 5s | Pct of >5s |
| :--- | :--- | :--- |
| UEFA Euro | 512 | 21.55% |
| Ligue 1 | 504 | 21.21% |
| FIFA World Cup | 350 | 14.73% |
| UEFA Women's Euro | 307 | 12.92% |
| La Liga | 250 | 10.52% |
| Women's World Cup | 237 | 9.97% |
| 1. Bundesliga | 179 | 7.53% |
| Major League Soccer | 37 | 1.56% |

### Breakdown by Initiation Event Type:
| Initiation Event Type | Count > 5s | Pct of >5s |
| :--- | :--- | :--- |
| Pressure | 816 | 34.34% |
| Interception | 731 | 30.77% |
| Pass | 544 | 22.90% |
| Duel | 209 | 8.80% |
| Block | 59 | 2.48% |
| 50/50 | 7 | 0.29% |
| Dribbled Past | 6 | 0.25% |
| Foul Committed | 4 | 0.17% |

---

## 3. Methodological Resolution & Quality Flags

To preserve strict methodological integrity without artificially forcing events into the 5-second window:
1. **`turnover_link_quality`**:
   - `high`: Direct, unambiguous turnover event found producing $0.0 \le 	ext{delay\_seconds} \le 5.0$.
   - `ambiguous`: Contested transitions or boundary edge cases ($5.0 < 	ext{delay} \le 6.0$).
   - `invalid`: No valid turnover linkage within 5.0s, or unlinked fallback ($> 5.0$s).
2. **`latency_valid`**:
   - Set to `True` **only** when `turnover_link_quality == "high"` and $0.0 \le 	ext{delay\_seconds} \le 5.0$.
   - Evaluates to `False` for all {over5_count:,} cases with delay $> 5.0$s.

---

## 4. Chronological Event Traces ({len(traces_for_report)} Representative Cases)

Below are complete chronological event traces demonstrating each cause category and delay interval:

### Case 1: Episode `3895340_p94_a0027fc7` (1. Bundesliga)
- **Initiation Delay**: 5.237 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bochum
- **Turnover Event**: Block -> **Initiation Event**: Pressure

```text
[2082] 00:12:22.624 | Bayer Leverkusen | Carry           @ [93.5, 38.4]
[2083] 00:12:23.747 | Bayer Leverkusen | Shot            (Blocked) @ [94.5, 40.5]
[2084] 00:12:23.977 | Bochum           | Block           @ [21.0, 40.0]
[2085] 00:12:24.017 | Bochum           | Goal Keeper     @ [2.1, 40.1]
[2086] 00:12:25.752 | Bochum           | Pass            -> Patrick Oste (Complete) @ [43.0, 31.1]
[2087] 00:12:26.848 | Bochum           | Ball Receipt*   @ [35.0, 32.1]
[2088] 00:12:26.848 | Bochum           | Carry           @ [35.0, 32.1]
[2089] 00:12:27.835 | Bochum           | Pass            -> Kevin Stöger (Complete) @ [37.2, 34.3]
[2090] 00:12:28.667 | Bochum           | Ball Receipt*   @ [33.0, 38.1]
[2091] 00:12:28.667 | Bochum           | Carry           @ [33.0, 38.1]
[2092] 00:12:29.214 | Bayer Leverkusen | Pressure        @ [83.4, 38.6] [CP=True]
[2093] 00:12:29.966 | Bayer Leverkusen | Foul Committed  @ [83.1, 40.6] [CP=True]
[2094] 00:12:29.966 | Bochum           | Foul Won        @ [37.0, 39.5]
```

### Case 2: Episode `3895348_p36_d0369eda` (1. Bundesliga)
- **Initiation Delay**: 5.061 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[1351] 00:25:36.964 | Augsburg         | Carry           @ [63.1, 63.6]
[1352] 00:25:39.236 | Bayer Leverkusen | Pressure        @ [47.4, 16.9]
[1353] 00:25:39.372 | Augsburg         | Pass            -> Mads Pederse (Complete) @ [69.6, 67.2]
[1354] 00:25:39.936 | Augsburg         | Ball Receipt*   @ [78.2, 77.9]
[1355] 00:25:39.936 | Augsburg         | Carry           @ [78.2, 77.9]
[1356] 00:25:40.126 | Augsburg         | Pass            -> Arne Maier (Complete) @ [77.6, 76.8]
[1357] 00:25:41.845 | Augsburg         | Ball Receipt*   @ [92.7, 77.3]
[1358] 00:25:41.845 | Augsburg         | Carry           @ [92.7, 77.3]
[1359] 00:25:43.536 | Augsburg         | Pass            -> Mads Pederse (Incomplete) @ [86.8, 76.3]
[1360] 00:25:44.433 | Augsburg         | Ball Receipt*   @ [85.7, 65.9]
[1361] 00:25:44.433 | Bayer Leverkusen | Interception    @ [33.9, 11.8] [CP=True]
[1362] 00:25:44.433 | Bayer Leverkusen | Carry           @ [33.9, 11.8]
[1363] 00:25:45.198 | Augsburg         | Pressure        @ [83.1, 72.4] [CP=True]
```

### Case 3: Episode `3895286_p103_024184b0` (1. Bundesliga)
- **Initiation Delay**: 5.109 seconds (Cause A: Turnover detector linked to earlier action in chain or pass flight boundary)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Hoffenheim
- **Turnover Event**: Block -> **Initiation Event**: Pressure

```text
[2609] 00:12:37.997 | Bayer Leverkusen | Carry           @ [91.1, 21.2]
[2610] 00:12:39.300 | Bayer Leverkusen | Shot            (Saved) @ [94.0, 26.1]
[2611] 00:12:39.321 | Hoffenheim       | Block           @ [25.1, 53.4]
[2612] 00:12:40.739 | Hoffenheim       | Goal Keeper     @ [2.1, 42.1]
[2613] 00:12:44.430 | Bayer Leverkusen | Pressure        @ [111.7, 42.2] [CP=True]
[2614] 00:12:46.300 | Hoffenheim       | Pass            -> Florian Gril (Complete) @ [8.4, 45.0]
[2615] 00:12:47.625 | Hoffenheim       | Ball Receipt*   @ [17.7, 38.1]
```

### Case 4: Episode `3895320_p117_d5e07119` (1. Bundesliga)
- **Initiation Delay**: 5.022 seconds (Cause A: Turnover detector linked to earlier action in chain or pass flight boundary)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Goal Keeper -> **Initiation Event**: Pressure

```text
[2700] 00:20:44.375 | Bayer Leverkusen | Carry           @ [112.2, 22.8]
[2701] 00:20:44.635 | Bayer Leverkusen | Pass            (Incomplete) @ [112.7, 23.3]
[2702] 00:20:45.128 | VfB Stuttgart    | Goal Keeper     @ [3.3, 38.9]
[2703] 00:20:49.480 | VfB Stuttgart    | Ball Recovery   @ [11.0, 10.8]
[2704] 00:20:49.480 | VfB Stuttgart    | Carry           @ [11.0, 10.8]
[2705] 00:20:50.150 | Bayer Leverkusen | Pressure        @ [105.6, 66.3] [CP=True]
[2706] 00:20:50.528 | VfB Stuttgart    | Pass            -> Serhou Guira (Incomplete) @ [14.7, 9.7]
[2707] 00:20:55.332 | VfB Stuttgart    | Ball Receipt*   @ [47.0, 15.5]
```

### Case 5: Episode `3895266_p40_001e5546` (1. Bundesliga)
- **Initiation Delay**: 5.788 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Wolfsburg | **Possession Team**: Wolfsburg
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[1073] 00:19:37.087 | Bayer Leverkusen | Ball Receipt*   @ [54.2, 13.7]
[1074] 00:19:37.087 | Bayer Leverkusen | Carry           @ [54.2, 13.7]
[1075] 00:19:40.792 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [50.4, 26.0]
[1076] 00:19:41.780 | Bayer Leverkusen | Ball Receipt*   @ [65.0, 30.4]
[1077] 00:19:41.780 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [65.0, 30.4]
[1078] 00:19:43.859 | Bayer Leverkusen | Ball Receipt*   @ [56.2, 51.9]
[1079] 00:19:43.859 | Bayer Leverkusen | Carry           @ [56.2, 51.9]
[1080] 00:19:45.629 | Bayer Leverkusen | Pass            -> Nathan Tella (Incomplete) @ [66.4, 50.3]
[1081] 00:19:46.580 | Bayer Leverkusen | Ball Receipt*   @ [80.0, 54.2]
[1082] 00:19:46.580 | Wolfsburg        | Interception    @ [36.3, 24.4] [CP=True]
[1083] 00:19:46.580 | Wolfsburg        | Carry           @ [36.3, 24.4]
[1084] 00:19:48.614 | Wolfsburg        | Pass            -> Maximilian A (Complete) @ [37.9, 27.0]
```

### Case 6: Episode `3895266_p51_2e3e7fe5` (1. Bundesliga)
- **Initiation Delay**: 5.396 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Wolfsburg | **Possession Team**: Wolfsburg
- **Turnover Event**: Clearance -> **Initiation Event**: Pressure

```text
[1329] 00:26:47.571 | Wolfsburg        | Pass            -> Jonas Older  (Incomplete) @ [120.0, 0.1]
[1330] 00:26:49.201 | Wolfsburg        | Ball Receipt*   @ [111.0, 44.1]
[1331] 00:26:49.201 | Bayer Leverkusen | Clearance       @ [7.5, 39.5]
[1332] 00:26:51.854 | Bayer Leverkusen | Ball Recovery   @ [28.1, 40.3]
[1333] 00:26:52.699 | Bayer Leverkusen | Ball Recovery   @ [21.6, 48.4]
[1334] 00:26:52.699 | Bayer Leverkusen | Carry           @ [21.6, 48.4]
[1335] 00:26:54.597 | Wolfsburg        | Pressure        @ [85.0, 29.6] [CP=True]
[1336] 00:26:55.096 | Wolfsburg        | Dribbled Past   @ [85.0, 33.1] [CP=True]
[1337] 00:26:55.096 | Bayer Leverkusen | Dribble         @ [35.1, 47.0]
```

### Case 7: Episode `3895333_p49_8064a1db` (1. Bundesliga)
- **Initiation Delay**: 5.132 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Eintracht Frankfurt | **Possession Team**: Eintracht Frankfurt
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[1211] 00:29:18.003 | Bayer Leverkusen | Ball Receipt*   @ [23.1, 45.0]
[1212] 00:29:18.003 | Bayer Leverkusen | Carry           @ [23.1, 45.0]
[1213] 00:29:24.158 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [47.6, 51.4]
[1214] 00:29:25.832 | Bayer Leverkusen | Ball Receipt*   @ [63.5, 68.9]
[1215] 00:29:25.832 | Bayer Leverkusen | Carry           @ [63.5, 68.9]
[1216] 00:29:26.600 | Bayer Leverkusen | Pass            -> Nathan Tella (Incomplete) @ [72.0, 68.6]
[1217] 00:29:28.878 | Bayer Leverkusen | Pressure        @ [101.0, 74.2]
[1218] 00:29:29.290 | Bayer Leverkusen | Ball Receipt*   @ [98.8, 74.2]
[1219] 00:29:29.290 | Eintracht Frankf | Interception    @ [14.3, 8.5] [CP=True]
[1220] 00:29:29.290 | Eintracht Frankf | Carry           @ [14.3, 8.5]
[1221] 00:29:33.995 | Bayer Leverkusen | Pressure        @ [115.9, 74.0] [CP=True]
```

### Case 8: Episode `3895333_p103_6ee1cd6c` (1. Bundesliga)
- **Initiation Delay**: 5.148 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Eintracht Frankfurt | **Possession Team**: Eintracht Frankfurt
- **Turnover Event**: Duel -> **Initiation Event**: Pressure

```text
[2407] 00:18:59.096 | Bayer Leverkusen | Pressure        @ [11.0, 56.8]
[2408] 00:19:02.157 | Eintracht Frankf | Dispossessed    @ [115.1, 23.5]
[2409] 00:19:02.157 | Bayer Leverkusen | Duel            @ [5.0, 56.6]
[2410] 00:19:02.157 | Bayer Leverkusen | Carry           @ [5.0, 56.6]
[2411] 00:19:05.006 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [2.6, 58.3]
[2412] 00:19:06.652 | Bayer Leverkusen | Ball Receipt*   @ [15.2, 76.4]
[2413] 00:19:06.652 | Bayer Leverkusen | Carry           @ [15.2, 76.4]
[2414] 00:19:07.305 | Eintracht Frankf | Pressure        @ [110.4, 8.0] [CP=True]
[2415] 00:19:07.534 | Eintracht Frankf | Pressure        @ [103.0, 4.8] [CP=True]
[2416] 00:19:07.880 | Bayer Leverkusen | Pass            -> Edmond Fayça (Incomplete) @ [13.2, 76.9]
```

### Case 9: Episode `3895121_p10_ae390965` (1. Bundesliga)
- **Initiation Delay**: 5.446 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Ball Recovery -> **Initiation Event**: Pressure

```text
[184] 00:04:27.359 | Bayer Leverkusen | Ball Receipt*   @ [87.5, 61.7]
[185] 00:04:27.359 | Bayer Leverkusen | Miscontrol      @ [87.5, 63.4]
[186] 00:04:29.220 | Freiburg         | Ball Recovery   @ [19.4, 23.3]
[187] 00:04:29.220 | Freiburg         | Carry           @ [19.4, 23.3]
[188] 00:04:31.768 | Freiburg         | Pass            -> Vincenzo Gri (Complete) @ [21.4, 18.3]
[189] 00:04:33.286 | Freiburg         | Ball Receipt*   @ [41.5, 0.6]
[190] 00:04:33.286 | Freiburg         | Carry           @ [41.5, 0.6]
[191] 00:04:34.666 | Bayer Leverkusen | Pressure        @ [78.6, 79.5] [CP=True]
[192] 00:04:36.852 | Freiburg         | Miscontrol      @ [35.1, 0.8]
[193] 00:04:41.849 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [85.4, 80.0]
```

### Case 10: Episode `3895121_p83_c46bc7f6` (1. Bundesliga)
- **Initiation Delay**: 5.196 seconds (Cause B: StatsBomb possession indexing retained pressing team despite brief contestation)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Pressure

```text
[2122] 00:04:06.304 | Bayer Leverkusen | Ball Receipt*   @ [87.8, 19.5]
[2123] 00:04:06.304 | Freiburg         | Ball Recovery   @ [3.5, 56.5]
[2124] 00:04:12.657 | Freiburg         | Pass            -> Nicolas Höfl (Complete) @ [9.0, 30.2]
[2125] 00:04:14.923 | Freiburg         | Ball Receipt*   @ [26.3, 58.1]
[2126] 00:04:17.853 | Bayer Leverkusen | Pressure        @ [87.8, 17.9] [CP=True]
[2127] 00:04:17.885 | Freiburg         | Pass            -> Kiliann Sild (Incomplete) @ [32.3, 62.2]
[2128] 00:04:18.862 | Freiburg         | Ball Receipt*   @ [37.7, 77.3]
```

### Case 11: Episode `3895121_p128_a24bae03` (1. Bundesliga)
- **Initiation Delay**: 5.740 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Freiburg
- **Turnover Event**: 50/50 -> **Initiation Event**: Duel

```text
[3473] 00:36:41.439 | Bayer Leverkusen | Block           @ [93.9, 36.8]
[3474] 00:36:41.963 | Bayer Leverkusen | 50/50           @ [97.7, 39.1]
[3475] 00:36:41.963 | Freiburg         | 50/50           @ [22.4, 41.0]
[3476] 00:36:43.818 | Freiburg         | Ball Recovery   @ [9.7, 36.5]
[3477] 00:36:43.818 | Freiburg         | Carry           @ [9.7, 36.5]
[3478] 00:36:44.826 | Freiburg         | Pass            -> Ritsu Doan (Complete) @ [8.9, 46.6]
[3479] 00:36:47.644 | Freiburg         | Ball Receipt*   @ [33.9, 77.0]
[3480] 00:36:47.703 | Bayer Leverkusen | Duel            @ [86.2, 3.1] [CP=True]
[3481] 00:36:47.703 | Freiburg         | Pass            -> Lucas Höler (Complete) @ [33.9, 77.0]
[3482] 00:36:48.005 | Freiburg         | Ball Receipt*   @ [36.2, 66.5]
```

### Case 12: Episode `3895302_p143_f908d853` (1. Bundesliga)
- **Initiation Delay**: 5.983 seconds (Cause A: Turnover detector linked to earlier action in chain or pass flight boundary)
- **Counterpressing Team**: Werder Bremen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Block -> **Initiation Event**: Pressure

```text
[4210] 00:44:14.465 | Werder Bremen    | Pass            -> Marvin Ducks (Incomplete) @ [97.1, 57.2]
[4211] 00:44:14.664 | Werder Bremen    | Ball Receipt*   @ [98.7, 41.0]
[4212] 00:44:14.664 | Bayer Leverkusen | Block           @ [22.6, 25.1]
[4213] 00:44:16.038 | Bayer Leverkusen | Ball Recovery   @ [30.9, 21.7]
[4214] 00:44:16.038 | Bayer Leverkusen | Carry           @ [30.9, 21.7]
[4215] 00:44:20.647 | Werder Bremen    | Pressure        @ [57.5, 53.2] [CP=True]
[4216] 00:44:21.113 | Bayer Leverkusen | Pass            -> Florian Wirt (Complete) @ [66.1, 27.3]
[4217] 00:44:22.580 | Bayer Leverkusen | Ball Receipt*   @ [89.4, 55.4]
```

### Case 13: Episode `3895180_p19_cbd960db` (1. Bundesliga)
- **Initiation Delay**: 5.103 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Eintracht Frankfurt | **Possession Team**: Eintracht Frankfurt
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[266] 00:05:15.088 | Bayer Leverkusen | Carry           @ [55.6, 14.0]
[267] 00:05:15.614 | Eintracht Frankf | Pressure        @ [62.8, 63.7]
[268] 00:05:16.214 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [53.1, 15.3]
[269] 00:05:17.431 | Bayer Leverkusen | Ball Receipt*   @ [41.1, 23.1]
[270] 00:05:17.431 | Bayer Leverkusen | Carry           @ [41.1, 23.1]
[271] 00:05:20.721 | Bayer Leverkusen | Pass            -> Jonas Hofman (Incomplete) @ [34.3, 33.7]
[272] 00:05:21.317 | Bayer Leverkusen | Ball Receipt*   @ [55.0, 53.1]
[273] 00:05:21.317 | Eintracht Frankf | Interception    @ [70.6, 30.2] [CP=True]
[274] 00:05:21.317 | Eintracht Frankf | Carry           @ [70.6, 30.2]
[275] 00:05:23.464 | Bayer Leverkusen | Pressure        @ [41.1, 49.3] [CP=True]
```

### Case 14: Episode `3895134_p111_e9d2bf4a` (1. Bundesliga)
- **Initiation Delay**: 5.768 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Interception -> **Initiation Event**: Interception

```text
[2758] 00:19:52.076 | Bayer Leverkusen | Pass            -> Jeremie Frim (Incomplete) @ [98.9, 12.6]
[2759] 00:19:53.249 | Bayer Leverkusen | Ball Receipt*   @ [106.9, 16.3]
[2760] 00:19:53.249 | Hoffenheim       | Interception    @ [14.1, 61.4]
[2761] 00:19:53.249 | Hoffenheim       | Carry           @ [14.1, 61.4]
[2762] 00:19:55.442 | Hoffenheim       | Pass            -> Grischa Pröm (Complete) @ [17.3, 53.2]
[2763] 00:19:57.098 | Hoffenheim       | Ball Receipt*   @ [29.0, 39.6]
[2764] 00:19:57.098 | Hoffenheim       | Carry           @ [29.0, 39.6]
[2765] 00:19:58.016 | Hoffenheim       | Pass            -> Maximilian B (Incomplete) @ [36.0, 34.1]
[2766] 00:19:59.017 | Hoffenheim       | Ball Receipt*   @ [49.8, 15.6]
[2767] 00:19:59.017 | Bayer Leverkusen | Interception    @ [69.8, 63.2] [CP=True]
[2768] 00:19:59.017 | Bayer Leverkusen | Carry           @ [69.8, 63.2]
[2769] 00:20:05.305 | Bayer Leverkusen | Pass            -> Jonas Hofman (Incomplete) @ [101.4, 56.0]
```

### Case 15: Episode `3895220_p3_b82515b0` (1. Bundesliga)
- **Initiation Delay**: 5.075 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Darmstadt 98
- **Turnover Event**: Ball Recovery -> **Initiation Event**: Pressure

```text
[14] 00:00:09.871 | Darmstadt 98     | Foul Won        @ [55.8, 42.4]
[15] 00:00:11.099 | Bayer Leverkusen | Pressure        @ [58.9, 43.6]
[16] 00:00:11.581 | Darmstadt 98     | Ball Recovery   @ [64.2, 41.8]
[17] 00:00:12.258 | Darmstadt 98     | Ball Recovery   @ [63.8, 36.9]
[18] 00:00:12.258 | Darmstadt 98     | Carry           @ [63.8, 36.9]
[19] 00:00:14.066 | Darmstadt 98     | Pass            -> Gerrit Holtm (Complete) @ [77.5, 31.0]
[20] 00:00:15.547 | Darmstadt 98     | Ball Receipt*   @ [93.3, 29.8]
[21] 00:00:15.547 | Darmstadt 98     | Carry           @ [93.3, 29.8]
[22] 00:00:16.656 | Bayer Leverkusen | Pressure        @ [13.4, 56.3] [CP=True]
[23] 00:00:17.188 | Darmstadt 98     | Shot            (Off T) @ [107.6, 18.8]
[24] 00:00:17.987 | Bayer Leverkusen | Goal Keeper     @ [2.5, 44.1]
```

### Case 16: Episode `3895292_p53_6bd4ee66` (1. Bundesliga)
- **Initiation Delay**: 5.699 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Union Berlin
- **Turnover Event**: Clearance -> **Initiation Event**: Pressure

```text
[1186] 00:29:38.600 | Bayer Leverkusen | Pass            -> Florian Wirt (Incomplete) @ [53.3, 26.0]
[1187] 00:29:39.929 | Bayer Leverkusen | Ball Receipt*   @ [84.2, 39.1]
[1188] 00:29:39.929 | Union Berlin     | Clearance       @ [31.6, 37.5]
[1189] 00:29:42.349 | Union Berlin     | Ball Recovery   @ [23.8, 58.9]
[1190] 00:29:42.349 | Union Berlin     | Carry           @ [23.8, 58.9]
[1191] 00:29:44.418 | Union Berlin     | Pass            -> Lucas Tousar (Complete) @ [22.6, 69.0]
[1192] 00:29:45.628 | Bayer Leverkusen | Pressure        @ [73.8, 15.6] [CP=True]
[1193] 00:29:45.637 | Union Berlin     | Ball Receipt*   @ [43.6, 65.1]
[1194] 00:29:45.637 | Union Berlin     | Carry           @ [43.6, 65.1]
```

### Case 17: Episode `3895292_p163_534f802d` (1. Bundesliga)
- **Initiation Delay**: 5.542 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[3800] 00:49:49.580 | Union Berlin     | Ball Receipt*   @ [65.7, 56.8]
[3801] 00:49:49.580 | Union Berlin     | Carry           @ [65.7, 56.8]
[3802] 00:49:52.098 | Union Berlin     | Pass            -> Benedict Hol (Complete) @ [68.7, 49.7]
[3803] 00:49:53.415 | Union Berlin     | Ball Receipt*   @ [85.2, 65.6]
[3804] 00:49:53.415 | Union Berlin     | Carry           @ [85.2, 65.6]
[3805] 00:49:55.808 | Union Berlin     | Pass            -> Danilho Doek (Incomplete) @ [89.7, 66.8]
[3806] 00:49:57.640 | Union Berlin     | Ball Receipt*   @ [108.7, 28.8]
[3807] 00:49:57.640 | Bayer Leverkusen | Interception    @ [11.4, 45.7] [CP=True]
[3808] 00:49:57.640 | Bayer Leverkusen | Carry           @ [11.4, 45.7]
[3809] 00:50:05.111 | Bayer Leverkusen | Pass            -> Jeremie Frim (Complete) @ [8.1, 77.4]
```

### Case 18: Episode `3895107_p71_0fbc2e16` (1. Bundesliga)
- **Initiation Delay**: 5.494 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: FC Köln
- **Turnover Event**: Pressure -> **Initiation Event**: 50/50

```text
[1950] 00:45:09.539 | FC Köln          | Block           @ [90.5, 78.2]
[1951] 00:45:12.159 | Bayer Leverkusen | Ball Recovery   @ [51.9, 1.4]
[1952] 00:45:12.414 | FC Köln          | Pressure        @ [68.2, 78.7]
[1953] 00:45:14.077 | FC Köln          | Pass            -> Timo Hübers (Complete) @ [64.8, 72.2]
[1954] 00:45:15.783 | FC Köln          | Ball Receipt*   @ [53.7, 71.9]
[1955] 00:45:15.783 | FC Köln          | Carry           @ [53.7, 71.9]
[1956] 00:45:15.815 | FC Köln          | Pass            -> Faride Alido (Complete) @ [53.0, 69.6]
[1957] 00:45:17.018 | FC Köln          | Ball Receipt*   @ [67.3, 71.4]
[1958] 00:45:17.018 | FC Köln          | Carry           @ [67.3, 71.4]
[1959] 00:45:17.105 | FC Köln          | Miscontrol      @ [69.7, 72.1]
[1960] 00:45:17.908 | Bayer Leverkusen | 50/50           @ [53.2, 8.8] [CP=True]
[1961] 00:45:17.908 | FC Köln          | 50/50           @ [66.9, 71.3]
[1962] 00:45:19.016 | Bayer Leverkusen | Pressure        @ [53.2, 8.7] [CP=True]
```

### Case 19: Episode `3895107_p76_50f9c656` (1. Bundesliga)
- **Initiation Delay**: 5.606 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: FC Köln | **Possession Team**: FC Köln
- **Turnover Event**: Pass -> **Initiation Event**: Duel

```text
[2036] 00:47:18.887 | Bayer Leverkusen | Ball Receipt*   @ [107.0, 28.9]
[2037] 00:47:18.887 | FC Köln          | Clearance       @ [10.7, 46.0]
[2038] 00:47:20.178 | Bayer Leverkusen | Pass            -> Alejandro Gr (Complete) @ [99.7, 41.8]
[2039] 00:47:21.275 | Bayer Leverkusen | Ball Receipt*   @ [95.6, 31.5]
[2040] 00:47:21.275 | Bayer Leverkusen | Carry           @ [95.6, 31.5]
[2041] 00:47:22.732 | Bayer Leverkusen | Pass            -> Victor Okoh  (Complete) @ [94.9, 31.1]
[2042] 00:47:23.422 | Bayer Leverkusen | Ball Receipt*   @ [102.1, 19.3]
[2043] 00:47:23.422 | Bayer Leverkusen | Carry           @ [102.1, 19.3]
[2044] 00:47:25.784 | Bayer Leverkusen | Dribble         @ [108.9, 21.1]
[2045] 00:47:25.784 | FC Köln          | Duel            @ [11.2, 59.0] [CP=True]
[2046] 00:47:25.784 | FC Köln          | Carry           @ [11.2, 59.0]
[2047] 00:47:27.904 | FC Köln          | Pass            -> Davie Selke (Complete) @ [3.1, 55.8]
```

### Case 20: Episode `3895107_p91_2659c4c2` (1. Bundesliga)
- **Initiation Delay**: 5.964 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: FC Köln | **Possession Team**: FC Köln
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[2239] 00:03:49.825 | Bayer Leverkusen | Carry           @ [21.4, 53.9]
[2240] 00:03:51.478 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [25.9, 50.9]
[2241] 00:03:53.525 | Bayer Leverkusen | Ball Receipt*   @ [28.7, 28.4]
[2242] 00:03:53.525 | Bayer Leverkusen | Carry           @ [28.7, 28.4]
[2243] 00:03:55.177 | Bayer Leverkusen | Pass            -> Victor Okoh  (Complete) @ [34.5, 26.0]
[2244] 00:03:56.843 | Bayer Leverkusen | Ball Receipt*   @ [57.6, 6.2]
[2245] 00:03:56.843 | Bayer Leverkusen | Pass            -> Alejandro Gr (Complete) @ [57.6, 6.2]
[2246] 00:03:57.239 | Bayer Leverkusen | Ball Receipt*   @ [57.6, 13.2]
[2247] 00:03:57.239 | Bayer Leverkusen | Carry           @ [57.6, 13.2]
[2248] 00:03:58.276 | Bayer Leverkusen | Pass            -> Florian Wirt (Incomplete) @ [61.9, 15.6]
[2249] 00:03:59.489 | Bayer Leverkusen | Ball Receipt*   @ [83.5, 24.8]
[2250] 00:03:59.489 | FC Köln          | Interception    @ [37.9, 56.2] [CP=True]
[2251] 00:03:59.489 | FC Köln          | Carry           @ [37.9, 56.2]
[2252] 00:04:01.192 | FC Köln          | Pass            -> Davie Selke (Complete) @ [40.5, 54.7]
```

### Case 21: Episode `3895250_p45_7d909078` (1. Bundesliga)
- **Initiation Delay**: 5.302 seconds (Cause A: Turnover detector linked to earlier action in chain or pass flight boundary)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Clearance -> **Initiation Event**: Dribbled Past

```text
[1043] 00:24:36.478 | FSV Mainz 05     | Clearance       @ [7.8, 35.3]
[1044] 00:25:18.053 | Bayer Leverkusen | Pass            (Incomplete) @ [120.0, 80.0]
[1045] 00:25:19.939 | FSV Mainz 05     | Clearance       @ [5.0, 41.4]
[1046] 00:25:21.693 | FSV Mainz 05     | Ball Recovery   @ [19.8, 50.1]
[1047] 00:25:21.693 | FSV Mainz 05     | Carry           @ [19.8, 50.1]
[1048] 00:25:25.241 | Bayer Leverkusen | Dribbled Past   @ [91.3, 4.6] [CP=True]
[1049] 00:25:25.241 | FSV Mainz 05     | Dribble         @ [28.8, 75.5]
[1050] 00:25:25.241 | FSV Mainz 05     | Carry           @ [28.8, 75.5]
```

### Case 22: Episode `3895250_p57_c9857c32` (1. Bundesliga)
- **Initiation Delay**: 5.402 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[1365] 00:31:40.634 | FSV Mainz 05     | Ball Receipt*   @ [42.2, 43.5]
[1366] 00:31:40.634 | FSV Mainz 05     | Carry           @ [42.2, 43.5]
[1367] 00:31:43.568 | FSV Mainz 05     | Pass            -> Anthony Caci (Complete) @ [47.5, 36.1]
[1368] 00:31:45.327 | FSV Mainz 05     | Ball Receipt*   @ [56.6, 4.9]
[1369] 00:31:45.327 | FSV Mainz 05     | Carry           @ [56.6, 4.9]
[1370] 00:31:48.188 | FSV Mainz 05     | Pass            -> Leandro Barr (Incomplete) @ [69.0, 7.6]
[1371] 00:31:48.970 | FSV Mainz 05     | Ball Receipt*   @ [87.1, 16.5]
[1372] 00:31:48.970 | Bayer Leverkusen | Interception    @ [35.8, 65.3] [CP=True]
[1373] 00:31:48.970 | Bayer Leverkusen | Carry           @ [35.8, 65.3]
[1374] 00:31:50.211 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [33.8, 61.3]
```

### Case 23: Episode `3895309_p89_eda85659` (1. Bundesliga)
- **Initiation Delay**: 5.905 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Borussia Dortmund | **Possession Team**: Borussia Dortmund
- **Turnover Event**: Pass -> **Initiation Event**: Block

```text
[2587] 00:12:56.425 | Bayer Leverkusen | Ball Recovery   @ [52.1, 57.4]
[2588] 00:12:56.425 | Bayer Leverkusen | Carry           @ [52.1, 57.4]
[2589] 00:13:00.979 | Bayer Leverkusen | Pass            -> Jeremie Frim (Complete) @ [65.9, 42.5]
[2590] 00:13:03.872 | Bayer Leverkusen | Ball Receipt*   @ [85.2, 67.3]
[2591] 00:13:03.872 | Bayer Leverkusen | Carry           @ [85.2, 67.3]
[2592] 00:13:06.412 | Bayer Leverkusen | Pass            -> Josip Staniš (Incomplete) @ [107.7, 65.6]
[2593] 00:13:06.884 | Bayer Leverkusen | Ball Receipt*   @ [109.6, 46.3]
[2594] 00:13:06.884 | Borussia Dortmun | Block           @ [8.2, 27.3] [CP=True]
[2595] 00:13:08.840 | Borussia Dortmun | Ball Recovery   @ [2.2, 31.5]
[2596] 00:13:21.332 | Borussia Dortmun | Pass            -> Nico Schlott (Complete) @ [7.6, 39.8]
```

### Case 24: Episode `3895074_p37_630bb15d` (1. Bundesliga)
- **Initiation Delay**: 5.024 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Duel

```text
[705] 00:16:01.891 | Bayern Munich    | Carry           @ [83.5, 59.7]
[706] 00:16:02.493 | Bayer Leverkusen | Pressure        @ [40.0, 23.4]
[707] 00:16:02.616 | Bayern Munich    | Pass            -> Alphonso Dav (Complete) @ [83.3, 58.6]
[708] 00:16:03.867 | Bayern Munich    | Ball Receipt*   @ [85.7, 31.1]
[709] 00:16:03.867 | Bayern Munich    | Carry           @ [85.7, 31.1]
[710] 00:16:04.744 | Bayern Munich    | Pass            -> Serge Gnabry (Complete) @ [86.1, 28.7]
[711] 00:16:05.772 | Bayern Munich    | Ball Receipt*   @ [98.8, 16.3]
[712] 00:16:05.772 | Bayern Munich    | Carry           @ [98.8, 16.3]
[713] 00:16:07.640 | Bayern Munich    | Dribble         @ [105.1, 22.4]
[714] 00:16:07.640 | Bayer Leverkusen | Duel            @ [15.0, 57.7] [CP=True]
[715] 00:16:11.954 | Bayer Leverkusen | Ball Recovery   @ [2.5, 74.1]
[716] 00:16:11.954 | Bayer Leverkusen | Carry           @ [2.5, 74.1]
```

### Case 25: Episode `3895074_p64_5a212df7` (1. Bundesliga)
- **Initiation Delay**: 5.187 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Pass

```text
[1403] 00:30:56.449 | Bayern Munich    | Ball Receipt*   @ [13.9, 20.1]
[1404] 00:30:56.449 | Bayern Munich    | Carry           @ [13.9, 20.1]
[1405] 00:31:00.093 | Bayern Munich    | Pass            -> Min Jae Kim (Complete) @ [23.1, 13.1]
[1406] 00:31:01.151 | Bayern Munich    | Ball Receipt*   @ [22.8, 24.8]
[1407] 00:31:01.151 | Bayern Munich    | Carry           @ [22.8, 24.8]
[1408] 00:31:01.702 | Bayern Munich    | Pass            -> Joshua Kimmi (Complete) @ [22.8, 24.8]
[1409] 00:31:02.853 | Bayern Munich    | Ball Receipt*   @ [28.8, 32.3]
[1410] 00:31:02.853 | Bayern Munich    | Carry           @ [28.8, 32.3]
[1411] 00:31:03.891 | Bayern Munich    | Pass            -> Serge Gnabry (Incomplete) @ [33.7, 32.0]
[1412] 00:31:05.280 | Bayern Munich    | Ball Receipt*   @ [49.1, 39.1]
[1413] 00:31:05.280 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [67.8, 38.0] [CP=True]
[1414] 00:31:06.832 | Bayer Leverkusen | Ball Receipt*   @ [78.4, 30.5]
[1415] 00:31:06.832 | Bayer Leverkusen | Carry           @ [78.4, 30.5]
```

### Case 26: Episode `3895340_p3_eefaa391` (1. Bundesliga)
- **Initiation Delay**: 6.172 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Pass

```text
[4] 00:00:00.000 | Bayer Leverkusen | Half Start     
[5] 00:00:00.719 | Bochum           | Pass            -> Manuel Riema (Complete) @ [61.0, 40.1]
[6] 00:00:02.879 | Bochum           | Ball Receipt*   @ [32.4, 43.6]
[7] 00:00:02.879 | Bochum           | Carry           @ [32.4, 43.6]
[8] 00:00:02.936 | Bochum           | Pass            -> Felix Passla (Complete) @ [32.4, 41.8]
[9] 00:00:05.306 | Bochum           | Ball Receipt*   @ [52.3, 66.9]
[10] 00:00:05.306 | Bochum           | Carry           @ [52.3, 66.9]
[11] 00:00:06.825 | Bochum           | Pass            (Incomplete) @ [62.2, 70.1]
[12] 00:00:09.051 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [20.2, 39.6] [CP=True]
[13] 00:00:10.414 | Bayer Leverkusen | Ball Receipt*   @ [32.0, 26.7]
[14] 00:00:10.450 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [32.0, 26.7]
```

### Case 27: Episode `3895340_p45_839908f8` (1. Bundesliga)
- **Initiation Delay**: 6.960 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bochum | **Possession Team**: Bochum
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[788] 00:25:40.090 | Bayer Leverkusen | Ball Receipt*   @ [90.2, 3.7]
[789] 00:25:40.090 | Bayer Leverkusen | Carry           @ [90.2, 3.7]
[790] 00:25:41.568 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [90.2, 3.7]
[791] 00:25:42.578 | Bayer Leverkusen | Ball Receipt*   @ [76.2, 29.2]
[792] 00:25:42.578 | Bayer Leverkusen | Carry           @ [76.2, 29.2]
[793] 00:25:44.363 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [79.0, 26.7]
[794] 00:25:45.405 | Bayer Leverkusen | Ball Receipt*   @ [86.7, 46.2]
[795] 00:25:45.405 | Bayer Leverkusen | Carry           @ [86.7, 46.2]
[796] 00:25:47.461 | Bayer Leverkusen | Pass            -> Nathan Tella (Incomplete) @ [89.5, 49.1]
[797] 00:25:48.528 | Bayer Leverkusen | Ball Receipt*   @ [102.1, 66.9]
[798] 00:25:48.528 | Bochum           | Interception    @ [17.7, 14.3] [CP=True]
[799] 00:25:48.528 | Bochum           | Carry           @ [17.7, 14.3]
[800] 00:25:49.136 | Bayer Leverkusen | Foul Committed  @ [99.6, 64.8] [CP=True]
```

### Case 28: Episode `3895340_p123_1c2fbd0c` (1. Bundesliga)
- **Initiation Delay**: 6.835 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bochum | **Possession Team**: Bochum
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[2720] 00:29:07.739 | Bayer Leverkusen | Carry           @ [1.2, 56.4]
[2721] 00:29:09.406 | Bayer Leverkusen | Pass            -> Josip Staniš (Complete) @ [4.0, 57.6]
[2722] 00:29:14.545 | Bayer Leverkusen | Ball Receipt*   @ [23.3, 59.2]
[2723] 00:29:14.545 | Bayer Leverkusen | Carry           @ [23.3, 59.2]
[2724] 00:29:14.597 | Bayer Leverkusen | Pass            -> Jonathan Tah (Complete) @ [24.9, 58.6]
[2725] 00:29:15.873 | Bayer Leverkusen | Ball Receipt*   @ [23.5, 49.8]
[2726] 00:29:15.873 | Bayer Leverkusen | Carry           @ [23.5, 49.8]
[2727] 00:29:17.073 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [25.3, 47.4]
[2728] 00:29:18.192 | Bayer Leverkusen | Ball Receipt*   @ [36.9, 38.9]
[2729] 00:29:18.192 | Bayer Leverkusen | Carry           @ [36.9, 38.9]
[2730] 00:29:20.466 | Bayer Leverkusen | Pass            -> Borja Iglesi (Incomplete) @ [43.2, 33.1]
[2731] 00:29:21.380 | Bayer Leverkusen | Ball Receipt*   @ [65.4, 50.0]
[2732] 00:29:21.380 | Bochum           | Interception    @ [62.7, 33.8] [CP=True]
[2733] 00:29:21.380 | Bochum           | Carry           @ [62.7, 33.8]
[2734] 00:29:22.317 | Bochum           | Pass            -> Matúš Bero (Complete) @ [62.7, 36.7]
```

### Case 29: Episode `3895340_p153_94ebca87` (1. Bundesliga)
- **Initiation Delay**: 7.876 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bochum | **Possession Team**: Bochum
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[3256] 00:46:33.591 | Bayer Leverkusen | Carry           @ [10.9, 41.2]
[3257] 00:46:34.852 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [14.5, 41.1]
[3258] 00:46:36.219 | Bayer Leverkusen | Ball Receipt*   @ [36.1, 15.3]
[3259] 00:46:36.219 | Bayer Leverkusen | Carry           @ [36.1, 15.3]
[3260] 00:46:40.920 | Bayer Leverkusen | Pass            -> Alejandro Gr (Complete) @ [61.6, 14.9]
[3261] 00:46:42.084 | Bayer Leverkusen | Ball Receipt*   @ [74.7, 7.2]
[3262] 00:46:42.084 | Bayer Leverkusen | Carry           @ [74.7, 7.2]
[3263] 00:46:42.972 | Bayer Leverkusen | Pass            -> Gustavo Adol (Incomplete) @ [74.7, 7.2]
[3264] 00:46:44.095 | Bayer Leverkusen | Ball Receipt*   @ [82.1, 27.7]
[3265] 00:46:44.095 | Bochum           | Interception    @ [40.0, 62.0] [CP=True]
[3266] 00:46:44.095 | Bochum           | Carry           @ [40.0, 62.0]
[3267] 00:46:44.542 | Bayer Leverkusen | Pressure        @ [81.2, 16.7] [CP=True]
```

### Case 30: Episode `3895348_p22_f0274d17` (1. Bundesliga)
- **Initiation Delay**: 6.693 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Duel -> **Initiation Event**: Interception

```text
[723] 00:14:09.546 | Augsburg         | Pressure        @ [43.8, 77.5]
[724] 00:14:10.640 | Bayer Leverkusen | Dispossessed    @ [77.3, 3.8]
[725] 00:14:10.640 | Augsburg         | Duel            @ [42.8, 76.3]
[726] 00:14:10.640 | Augsburg         | Carry           @ [42.8, 76.3]
[727] 00:14:12.314 | Augsburg         | Pass            -> Arne Maier (Complete) @ [44.5, 76.1]
[728] 00:14:13.351 | Augsburg         | Ball Receipt*   @ [51.2, 77.5]
[729] 00:14:13.351 | Augsburg         | Carry           @ [51.2, 77.5]
[730] 00:14:14.030 | Augsburg         | Pass            -> Ermedin Demi (Incomplete) @ [53.0, 76.8]
[731] 00:14:17.238 | Augsburg         | Pressure        @ [92.1, 76.8]
[732] 00:14:17.333 | Augsburg         | Ball Receipt*   @ [89.6, 76.6]
[733] 00:14:17.333 | Bayer Leverkusen | Interception    @ [27.0, 1.3] [CP=True]
[734] 00:14:17.333 | Bayer Leverkusen | Carry           @ [27.0, 1.3]
[735] 00:14:17.959 | Augsburg         | Dribbled Past   @ [90.7, 78.4]
```

### Case 31: Episode `3895348_p33_b1bc0c1e` (1. Bundesliga)
- **Initiation Delay**: 7.097 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Pass

```text
[1181] 00:22:39.205 | Augsburg         | Carry           @ [9.7, 43.6]
[1182] 00:22:42.693 | Augsburg         | Pass            -> Tim Breithau (Complete) @ [11.9, 47.0]
[1183] 00:22:43.757 | Augsburg         | Ball Receipt*   @ [30.3, 42.4]
[1184] 00:22:43.757 | Augsburg         | Carry           @ [30.3, 42.4]
[1185] 00:22:44.343 | Augsburg         | Pass            -> Arne Maier (Complete) @ [30.0, 44.0]
[1186] 00:22:45.707 | Augsburg         | Ball Receipt*   @ [55.5, 62.2]
[1187] 00:22:45.707 | Augsburg         | Carry           @ [55.5, 62.2]
[1188] 00:22:46.954 | Augsburg         | Pass            -> Phillip Tiet (Complete) @ [62.7, 63.2]
[1189] 00:22:48.141 | Augsburg         | Ball Receipt*   @ [69.7, 54.0]
[1190] 00:22:48.141 | Augsburg         | Carry           @ [69.7, 54.0]
[1191] 00:22:49.084 | Augsburg         | Pass            -> Arne Maier (Incomplete) @ [70.1, 55.3]
[1192] 00:22:50.854 | Augsburg         | Ball Receipt*   @ [86.2, 69.6]
[1193] 00:22:50.854 | Bayer Leverkusen | Pass            -> Alejandro Gr (Complete) @ [35.8, 14.0] [CP=True]
[1194] 00:22:52.263 | Bayer Leverkusen | Ball Receipt*   @ [40.8, 15.6]
[1195] 00:22:52.263 | Bayer Leverkusen | Carry           @ [40.8, 15.6]
```

### Case 32: Episode `3895348_p45_864d04ef` (1. Bundesliga)
- **Initiation Delay**: 6.378 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Augsburg | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Block -> **Initiation Event**: Pressure

```text
[1625] 00:31:13.979 | Augsburg         | Ball Receipt*   @ [111.1, 33.1]
[1626] 00:31:14.025 | Augsburg         | Shot            (Blocked) @ [111.1, 33.1]
[1627] 00:31:14.198 | Bayer Leverkusen | Block           @ [8.0, 46.3]
[1628] 00:31:14.619 | Bayer Leverkusen | Goal Keeper     @ [5.4, 45.0]
[1629] 00:31:17.812 | Bayer Leverkusen | Ball Recovery   @ [10.3, 75.4]
[1630] 00:31:17.812 | Bayer Leverkusen | Carry           @ [10.3, 75.4]
[1631] 00:31:19.511 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [10.3, 75.0]
[1632] 00:31:20.576 | Augsburg         | Pressure        @ [100.5, 13.9] [CP=True]
[1633] 00:31:20.727 | Bayer Leverkusen | Ball Receipt*   @ [19.4, 67.8]
[1634] 00:31:20.727 | Bayer Leverkusen | Carry           @ [19.4, 67.8]
```

### Case 33: Episode `3895348_p47_80fe14ff` (1. Bundesliga)
- **Initiation Delay**: 6.195 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Augsburg | **Possession Team**: Augsburg
- **Turnover Event**: Pass -> **Initiation Event**: Pass

```text
[1716] 00:32:57.877 | Bayer Leverkusen | Carry           @ [71.9, 32.9]
[1717] 00:32:57.981 | Augsburg         | Pressure        @ [49.1, 50.5]
[1718] 00:33:00.222 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [70.6, 37.5]
[1719] 00:33:02.243 | Bayer Leverkusen | Ball Receipt*   @ [69.1, 51.0]
[1720] 00:33:02.243 | Bayer Leverkusen | Carry           @ [69.1, 51.0]
[1721] 00:33:03.146 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [69.3, 52.6]
[1722] 00:33:04.346 | Bayer Leverkusen | Ball Receipt*   @ [84.8, 60.5]
[1723] 00:33:04.346 | Bayer Leverkusen | Carry           @ [84.8, 60.5]
[1724] 00:33:05.343 | Bayer Leverkusen | Pass            (Incomplete) @ [85.0, 58.5]
[1725] 00:33:06.417 | Augsburg         | Pass            -> Iago Amaral  (Complete) @ [28.1, 39.1] [CP=True]
[1726] 00:33:09.401 | Augsburg         | Ball Receipt*   @ [7.9, 27.0]
[1727] 00:33:09.401 | Augsburg         | Carry           @ [7.9, 27.0]
```

### Case 34: Episode `3895348_p54_5a9f32d9` (1. Bundesliga)
- **Initiation Delay**: 7.280 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Augsburg | **Possession Team**: Augsburg
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[1891] 00:36:52.378 | Bayer Leverkusen | Carry           @ [43.6, 44.3]
[1892] 00:36:52.458 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [43.6, 44.3]
[1893] 00:36:54.136 | Bayer Leverkusen | Ball Receipt*   @ [63.8, 41.2]
[1894] 00:36:54.136 | Bayer Leverkusen | Carry           @ [63.8, 41.2]
[1895] 00:36:56.967 | Bayer Leverkusen | Pass            -> Victor Okoh  (Complete) @ [85.7, 43.2]
[1896] 00:36:57.880 | Bayer Leverkusen | Ball Receipt*   @ [92.7, 25.4]
[1897] 00:36:57.880 | Bayer Leverkusen | Carry           @ [92.7, 25.4]
[1898] 00:37:01.075 | Bayer Leverkusen | Pass            -> Alejandro Gr (Incomplete) @ [99.3, 26.1]
[1899] 00:37:01.416 | Bayer Leverkusen | Ball Receipt*   @ [110.6, 22.0]
[1900] 00:37:01.416 | Augsburg         | Interception    @ [13.6, 54.7] [CP=True]
[1901] 00:37:01.416 | Augsburg         | Carry           @ [13.6, 54.7]
[1902] 00:37:01.860 | Bayer Leverkusen | Pressure        @ [104.1, 26.5] [CP=True]
```

### Case 35: Episode `3895286_p14_7eb7a15a` (1. Bundesliga)
- **Initiation Delay**: 6.141 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Hoffenheim | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Block -> **Initiation Event**: Block

```text
[256] 00:05:17.566 | Bayer Leverkusen | Pressure        @ [87.2, 16.1]
[257] 00:05:18.091 | Hoffenheim       | Pass            (Incomplete) @ [35.2, 64.5]
[258] 00:05:18.182 | Bayer Leverkusen | Block           @ [85.6, 13.9]
[259] 00:05:19.365 | Bayer Leverkusen | Ball Recovery   @ [79.4, 7.7]
[260] 00:05:19.365 | Bayer Leverkusen | Carry           @ [79.4, 7.7]
[261] 00:05:20.168 | Bayer Leverkusen | Pass            -> Florian Wirt (Complete) @ [82.1, 7.9]
[262] 00:05:20.773 | Bayer Leverkusen | Ball Receipt*   @ [88.4, 11.2]
[263] 00:05:20.773 | Bayer Leverkusen | Carry           @ [88.4, 11.2]
[264] 00:05:22.022 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [91.1, 17.4]
[265] 00:05:22.790 | Bayer Leverkusen | Ball Receipt*   @ [91.3, 26.2]
[266] 00:05:22.790 | Bayer Leverkusen | Carry           @ [91.3, 26.2]
[267] 00:05:24.109 | Bayer Leverkusen | Shot            (Blocked) @ [93.5, 38.9]
[268] 00:05:24.323 | Hoffenheim       | Block           @ [20.4, 41.3] [CP=True]
[269] 00:05:24.363 | Hoffenheim       | Goal Keeper     @ [2.2, 40.5]
[270] 00:05:26.166 | Hoffenheim       | Pressure        @ [36.7, 56.1]
```

### Case 36: Episode `3895286_p87_e7104794` (1. Bundesliga)
- **Initiation Delay**: 6.928 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Hoffenheim | **Possession Team**: Hoffenheim
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[2374] 00:04:39.999 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [59.2, 46.2]
[2375] 00:04:41.006 | Bayer Leverkusen | Ball Receipt*   @ [67.6, 51.9]
[2376] 00:04:43.195 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [69.1, 51.6]
[2377] 00:04:44.464 | Bayer Leverkusen | Ball Receipt*   @ [65.3, 43.9]
[2378] 00:04:44.464 | Bayer Leverkusen | Carry           @ [65.3, 43.9]
[2379] 00:04:45.946 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [68.4, 47.1]
[2380] 00:04:47.492 | Bayer Leverkusen | Ball Receipt*   @ [89.3, 67.7]
[2381] 00:04:47.492 | Bayer Leverkusen | Carry           @ [89.3, 67.7]
[2382] 00:04:49.438 | Bayer Leverkusen | Pass            -> Jonas Hofman (Incomplete) @ [94.9, 65.8]
[2383] 00:04:50.123 | Bayer Leverkusen | Ball Receipt*   @ [96.8, 52.5]
[2384] 00:04:50.123 | Hoffenheim       | Interception    @ [18.7, 24.3] [CP=True]
[2385] 00:04:50.123 | Hoffenheim       | Carry           @ [18.7, 24.3]
[2386] 00:04:51.585 | Hoffenheim       | Pass            -> Maximilian B (Incomplete) @ [24.3, 24.3]
```

### Case 37: Episode `3895266_p18_d14f72f5` (1. Bundesliga)
- **Initiation Delay**: 7.293 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Wolfsburg | **Possession Team**: Wolfsburg
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[437] 00:08:14.562 | Bayer Leverkusen | Ball Receipt*   @ [48.3, 8.1]
[438] 00:08:14.562 | Bayer Leverkusen | Carry           @ [48.3, 8.1]
[439] 00:08:16.122 | Bayer Leverkusen | Pass            -> Jonathan Tah (Complete) @ [47.2, 11.0]
[440] 00:08:17.111 | Bayer Leverkusen | Ball Receipt*   @ [37.5, 20.8]
[441] 00:08:17.111 | Bayer Leverkusen | Carry           @ [37.5, 20.8]
[442] 00:08:18.494 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [39.1, 20.8]
[443] 00:08:19.390 | Bayer Leverkusen | Ball Receipt*   @ [49.5, 25.2]
[444] 00:08:19.390 | Bayer Leverkusen | Carry           @ [49.5, 25.2]
[445] 00:08:20.179 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [48.8, 28.2]
[446] 00:08:21.313 | Bayer Leverkusen | Ball Receipt*   @ [52.6, 39.0]
[447] 00:08:21.313 | Bayer Leverkusen | Carry           @ [52.6, 39.0]
[448] 00:08:22.017 | Bayer Leverkusen | Pass            -> Florian Wirt (Incomplete) @ [53.7, 36.8]
[449] 00:08:23.415 | Bayer Leverkusen | Ball Receipt*   @ [72.3, 28.2]
[450] 00:08:23.415 | Wolfsburg        | Interception    @ [42.2, 49.6] [CP=True]
[451] 00:08:23.415 | Wolfsburg        | Carry           @ [42.2, 49.6]
[452] 00:08:24.717 | Wolfsburg        | Pass            -> Tiago Barrei (Complete) @ [44.4, 48.5]
```

### Case 38: Episode `3895266_p20_5dbb033e` (1. Bundesliga)
- **Initiation Delay**: 7.501 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[496] 00:09:16.804 | Wolfsburg        | Carry           @ [61.8, 45.8]
[497] 00:09:17.088 | Wolfsburg        | Pass            -> Maxence Lacr (Complete) @ [62.1, 46.9]
[498] 00:09:18.777 | Wolfsburg        | Ball Receipt*   @ [72.3, 70.0]
[499] 00:09:18.777 | Wolfsburg        | Carry           @ [72.3, 70.0]
[500] 00:09:22.110 | Wolfsburg        | Pass            -> Lovro Majer (Complete) @ [76.7, 73.8]
[501] 00:09:22.900 | Wolfsburg        | Ball Receipt*   @ [82.0, 79.3]
[502] 00:09:22.900 | Wolfsburg        | Carry           @ [82.0, 79.3]
[503] 00:09:25.895 | Wolfsburg        | Pass            -> Moritz Jenz (Incomplete) @ [69.1, 72.9]
[504] 00:09:26.278 | Wolfsburg        | Ball Receipt*   @ [51.4, 60.3]
[505] 00:09:26.278 | Bayer Leverkusen | Interception    @ [58.9, 9.9] [CP=True]
[506] 00:09:26.278 | Bayer Leverkusen | Carry           @ [58.9, 9.9]
[507] 00:09:31.133 | Wolfsburg        | Pressure        @ [27.7, 62.1] [CP=True]
```

### Case 39: Episode `3895266_p26_ffd93003` (1. Bundesliga)
- **Initiation Delay**: 7.596 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Wolfsburg | **Possession Team**: Wolfsburg
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[675] 00:12:41.285 | Bayer Leverkusen | Ball Receipt*   @ [76.8, 42.4]
[676] 00:12:41.285 | Bayer Leverkusen | Pass            -> Florian Wirt (Complete) @ [76.8, 42.4]
[677] 00:12:41.996 | Bayer Leverkusen | Ball Receipt*   @ [82.0, 48.3]
[678] 00:12:41.996 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [83.3, 48.3]
[679] 00:12:42.436 | Bayer Leverkusen | Ball Receipt*   @ [78.4, 41.8]
[680] 00:12:42.436 | Bayer Leverkusen | Carry           @ [78.4, 41.8]
[681] 00:12:44.244 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [80.9, 41.7]
[682] 00:12:44.902 | Bayer Leverkusen | Ball Receipt*   @ [78.3, 31.1]
[683] 00:12:44.902 | Bayer Leverkusen | Carry           @ [78.3, 31.1]
[684] 00:12:45.808 | Bayer Leverkusen | Pass            -> Piero Martín (Complete) @ [79.0, 27.7]
[685] 00:12:48.119 | Bayer Leverkusen | Ball Receipt*   @ [103.6, 3.4]
[686] 00:12:48.119 | Bayer Leverkusen | Carry           @ [103.6, 3.4]
[687] 00:12:48.137 | Bayer Leverkusen | Pass            -> Alejandro Gr (Incomplete) @ [103.6, 3.4]
[688] 00:12:49.278 | Bayer Leverkusen | Pressure        @ [96.2, 11.7]
[689] 00:12:49.592 | Bayer Leverkusen | Ball Receipt*   @ [94.6, 13.1]
[690] 00:12:49.592 | Wolfsburg        | Interception    @ [23.9, 66.3] [CP=True]
[691] 00:12:49.592 | Wolfsburg        | Carry           @ [23.9, 66.3]
[692] 00:12:49.980 | Bayer Leverkusen | Dribbled Past   @ [95.5, 10.4] [CP=True]
```

### Case 40: Episode `3895266_p79_987fc8cb` (1. Bundesliga)
- **Initiation Delay**: 6.010 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Wolfsburg | **Possession Team**: Wolfsburg
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[2129] 00:00:33.051 | Bayer Leverkusen | Ball Receipt*   @ [70.3, 15.4]
[2130] 00:00:33.051 | Bayer Leverkusen | Carry           @ [70.3, 15.4]
[2131] 00:00:35.530 | Bayer Leverkusen | Pass            -> Piero Martín (Complete) @ [83.3, 13.1]
[2132] 00:00:36.382 | Bayer Leverkusen | Ball Receipt*   @ [88.7, 5.6]
[2133] 00:00:36.382 | Bayer Leverkusen | Carry           @ [88.7, 5.6]
[2134] 00:00:37.532 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [83.7, 4.5]
[2135] 00:00:38.358 | Bayer Leverkusen | Ball Receipt*   @ [77.4, 13.1]
[2136] 00:00:38.358 | Bayer Leverkusen | Carry           @ [77.4, 13.1]
[2137] 00:00:39.341 | Bayer Leverkusen | Pass            -> Florian Wirt (Complete) @ [77.4, 13.1]
[2138] 00:00:39.939 | Bayer Leverkusen | Ball Receipt*   @ [84.3, 20.7]
[2139] 00:00:39.939 | Bayer Leverkusen | Carry           @ [84.3, 20.7]
[2140] 00:00:40.150 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [84.8, 20.7]
[2141] 00:00:40.563 | Bayer Leverkusen | Ball Receipt*   @ [80.6, 23.5]
[2142] 00:00:40.563 | Bayer Leverkusen | Carry           @ [80.6, 23.5]
[2143] 00:00:40.769 | Bayer Leverkusen | Pass            -> Florian Wirt (Incomplete) @ [79.1, 23.8]
[2144] 00:00:41.540 | Bayer Leverkusen | Ball Receipt*   @ [83.2, 17.3]
[2145] 00:00:41.540 | Wolfsburg        | Interception    @ [36.8, 57.9] [CP=True]
[2146] 00:00:41.540 | Wolfsburg        | Carry           @ [36.8, 57.9]
[2147] 00:00:42.252 | Wolfsburg        | Pass            -> Maximilian A (Complete) @ [40.8, 57.9]
```

### Case 41: Episode `3895266_p120_47dd76b6` (1. Bundesliga)
- **Initiation Delay**: 7.304 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Wolfsburg
- **Turnover Event**: Goal Keeper -> **Initiation Event**: Pressure

```text
[3647] 00:32:45.710 | Bayer Leverkusen | Ball Receipt*   @ [108.4, 48.8]
[3648] 00:32:45.726 | Bayer Leverkusen | Shot            (Saved) @ [108.4, 48.8]
[3649] 00:32:46.855 | Wolfsburg        | Goal Keeper     @ [0.9, 37.5]
[3650] 00:32:51.155 | Wolfsburg        | Pass            -> Cédric Zesig (Complete) @ [12.2, 28.5]
[3651] 00:32:52.948 | Wolfsburg        | Ball Receipt*   @ [24.5, 10.5]
[3652] 00:32:52.948 | Wolfsburg        | Carry           @ [24.5, 10.5]
[3653] 00:32:54.159 | Bayer Leverkusen | Pressure        @ [91.3, 68.6] [CP=True]
[3654] 00:32:54.374 | Wolfsburg        | Pass            -> Maximilian A (Complete) @ [26.7, 10.2]
[3655] 00:32:54.929 | Wolfsburg        | Ball Receipt*   @ [23.9, 15.7]
```

### Case 42: Episode `3895333_p26_e0b3075c` (1. Bundesliga)
- **Initiation Delay**: 6.751 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Pass

```text
[496] 00:12:47.178 | Eintracht Frankf | Ball Receipt*   @ [50.9, 44.1]
[497] 00:12:47.178 | Eintracht Frankf | Carry           @ [50.9, 44.1]
[498] 00:12:48.464 | Eintracht Frankf | Pass            -> Lucas Silva  (Complete) @ [48.9, 48.1]
[499] 00:12:49.755 | Eintracht Frankf | Ball Receipt*   @ [42.6, 61.3]
[500] 00:12:49.755 | Eintracht Frankf | Carry           @ [42.6, 61.3]
[501] 00:12:50.585 | Eintracht Frankf | Pass            -> Eric Junior  (Complete) @ [42.6, 61.3]
[502] 00:12:51.779 | Eintracht Frankf | Ball Receipt*   @ [50.8, 76.5]
[503] 00:12:51.779 | Eintracht Frankf | Carry           @ [50.8, 76.5]
[504] 00:12:53.229 | Eintracht Frankf | Pass            -> Mario Götze (Complete) @ [50.8, 76.5]
[505] 00:12:53.660 | Eintracht Frankf | Ball Receipt*   @ [50.6, 71.6]
[506] 00:12:53.660 | Eintracht Frankf | Pass            -> Eric Junior  (Incomplete) @ [50.6, 71.6]
[507] 00:12:54.752 | Eintracht Frankf | Pressure        @ [62.6, 77.7]
[508] 00:12:55.215 | Eintracht Frankf | Ball Receipt*   @ [58.6, 77.7]
[509] 00:12:55.215 | Bayer Leverkusen | Pass            -> Edmond Fayça (Complete) @ [55.1, 4.9] [CP=True]
[510] 00:12:58.058 | Bayer Leverkusen | Ball Receipt*   @ [22.2, 4.5]
[511] 00:12:58.058 | Bayer Leverkusen | Carry           @ [22.2, 4.5]
```

### Case 43: Episode `3895121_p94_926ba5dc` (1. Bundesliga)
- **Initiation Delay**: 7.598 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Bayer Leverkusen
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[2452] 00:11:00.442 | Freiburg         | Ball Receipt*   @ [16.6, 49.4]
[2453] 00:11:00.442 | Freiburg         | Carry           @ [16.6, 49.4]
[2454] 00:11:01.805 | Freiburg         | Pass            -> Philipp Lien (Complete) @ [15.0, 49.0]
[2455] 00:11:03.064 | Freiburg         | Ball Receipt*   @ [31.3, 41.6]
[2456] 00:11:03.064 | Freiburg         | Carry           @ [31.3, 41.6]
[2457] 00:11:04.076 | Freiburg         | Pass            -> Nicolas Höfl (Complete) @ [31.5, 43.3]
[2458] 00:11:05.239 | Freiburg         | Ball Receipt*   @ [40.7, 52.8]
[2459] 00:11:05.239 | Freiburg         | Carry           @ [40.7, 52.8]
[2460] 00:11:05.689 | Freiburg         | Pass            -> Philipp Lien (Complete) @ [40.1, 52.6]
[2461] 00:11:06.924 | Freiburg         | Ball Receipt*   @ [28.9, 37.8]
[2462] 00:11:06.924 | Freiburg         | Carry           @ [28.9, 37.8]
[2463] 00:11:07.234 | Freiburg         | Pass            -> Merlin Röhl (Incomplete) @ [28.9, 37.8]
[2464] 00:11:09.403 | Freiburg         | Ball Receipt*   @ [32.8, 11.3]
[2465] 00:11:09.403 | Bayer Leverkusen | Interception    @ [86.6, 66.9] [CP=True]
[2466] 00:11:09.403 | Bayer Leverkusen | Carry           @ [86.6, 66.9]
[2467] 00:11:09.531 | Bayer Leverkusen | Dribble         @ [88.0, 67.8]
```

### Case 44: Episode `3895302_p62_142c2982` (1. Bundesliga)
- **Initiation Delay**: 6.600 seconds (Cause E: Opponent sustained possession with 4+ actions; genuinely unlinked within 5.0s)
- **Counterpressing Team**: Bayer Leverkusen | **Possession Team**: Werder Bremen
- **Turnover Event**: Block -> **Initiation Event**: Pressure

```text
[1957] 00:41:55.039 | Bayer Leverkusen | Carry           @ [111.0, 10.4]
[1958] 00:41:56.085 | Bayer Leverkusen | Pass            (Incomplete) @ [116.2, 11.4]
[1959] 00:41:56.196 | Werder Bremen    | Block           @ [4.9, 66.3]
[1960] 00:41:58.040 | Werder Bremen    | Ball Recovery   @ [3.1, 70.8]
[1961] 00:41:58.040 | Werder Bremen    | Carry           @ [3.1, 70.8]
[1962] 00:41:59.115 | Werder Bremen    | Pass            -> Nick Woltema (Complete) @ [3.4, 73.9]
[1963] 00:42:01.538 | Werder Bremen    | Ball Receipt*   @ [37.7, 69.7]
[1964] 00:42:01.538 | Werder Bremen    | Carry           @ [37.7, 69.7]
[1965] 00:42:01.566 | Werder Bremen    | Pass            -> Leonardo Bit (Complete) @ [39.3, 70.2]
[1966] 00:42:02.796 | Bayer Leverkusen | Pressure        @ [82.2, 8.0] [CP=True]
[1967] 00:42:03.068 | Werder Bremen    | Ball Receipt*   @ [35.3, 73.4]
[1968] 00:42:03.068 | Werder Bremen    | Carry           @ [35.3, 73.4]
```

### Case 45: Episode `3895302_p84_88e5a51f` (1. Bundesliga)
- **Initiation Delay**: 7.328 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Werder Bremen | **Possession Team**: Werder Bremen
- **Turnover Event**: Pass -> **Initiation Event**: Interception

```text
[2644] 00:07:33.905 | Bayer Leverkusen | Carry           @ [4.9, 29.7]
[2645] 00:07:34.563 | Werder Bremen    | Pressure        @ [109.8, 44.0] [CP=True]
[2646] 00:07:35.386 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [5.7, 28.5]
[2647] 00:07:36.456 | Bayer Leverkusen | Ball Receipt*   @ [26.1, 32.4]
[2648] 00:07:36.456 | Bayer Leverkusen | Carry           @ [26.1, 32.4]
[2649] 00:07:36.664 | Bayer Leverkusen | Pass            -> Piero Martín (Complete) @ [26.1, 33.6]
[2650] 00:07:38.021 | Bayer Leverkusen | Ball Receipt*   @ [41.7, 7.5]
[2651] 00:07:38.021 | Bayer Leverkusen | Carry           @ [41.7, 7.5]
[2652] 00:07:40.610 | Bayer Leverkusen | Pass            -> Lukáš Hrádec (Incomplete) @ [57.1, 9.6]
[2653] 00:07:42.707 | Bayer Leverkusen | Pressure        @ [90.6, 9.4]
[2654] 00:07:42.714 | Bayer Leverkusen | Ball Receipt*   @ [87.1, 5.1]
[2655] 00:07:42.714 | Werder Bremen    | Interception    @ [31.1, 73.8] [CP=True]
[2656] 00:07:42.714 | Werder Bremen    | Carry           @ [31.1, 73.8]
[2657] 00:07:44.572 | Werder Bremen    | Pass            -> Michael Zett (Complete) @ [6.7, 66.4]
```

### Case 46: Episode `3895302_p112_dd24a9d2` (1. Bundesliga)
- **Initiation Delay**: 7.692 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Werder Bremen | **Possession Team**: Werder Bremen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Pass

```text
[3502] 00:27:38.441 | Bayer Leverkusen | Ball Receipt*   @ [69.3, 42.3]
[3503] 00:27:38.441 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [69.3, 42.3]
[3504] 00:27:39.200 | Bayer Leverkusen | Ball Receipt*   @ [60.5, 39.1]
[3505] 00:27:39.200 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [60.5, 39.1]
[3506] 00:27:39.759 | Bayer Leverkusen | Ball Receipt*   @ [66.5, 42.3]
[3507] 00:27:39.759 | Bayer Leverkusen | Carry           @ [66.5, 42.3]
[3508] 00:27:39.879 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [66.5, 42.3]
[3509] 00:27:40.652 | Bayer Leverkusen | Ball Receipt*   @ [59.2, 40.2]
[3510] 00:27:40.652 | Bayer Leverkusen | Carry           @ [59.2, 40.2]
[3511] 00:27:42.483 | Bayer Leverkusen | Pass            -> Granit Xhaka (Complete) @ [62.7, 34.0]
[3512] 00:27:43.406 | Bayer Leverkusen | Ball Receipt*   @ [68.9, 11.9]
[3513] 00:27:45.122 | Bayer Leverkusen | Pass            -> Jeremie Frim (Incomplete) @ [71.5, 13.4]
[3514] 00:27:46.892 | Bayer Leverkusen | Ball Receipt*   @ [99.3, 67.0]
[3515] 00:27:46.892 | Werder Bremen    | Pass            -> Romano Schmi (Complete) @ [21.5, 15.1] [CP=True]
[3516] 00:27:48.209 | Werder Bremen    | Ball Receipt*   @ [33.8, 20.8]
[3517] 00:27:48.209 | Werder Bremen    | Carry           @ [33.8, 20.8]
```

### Case 47: Episode `3895302_p125_16447969` (1. Bundesliga)
- **Initiation Delay**: 7.160 seconds (Cause C: Multiple contested events (duels/50-50s) delayed clear possession establishment)
- **Counterpressing Team**: Werder Bremen | **Possession Team**: Werder Bremen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Duel

```text
[3814] 00:34:14.460 | Bayer Leverkusen | Carry           @ [43.2, 26.2]
[3815] 00:34:15.935 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [45.9, 22.9]
[3816] 00:34:17.056 | Bayer Leverkusen | Ball Receipt*   @ [55.2, 7.6]
[3817] 00:34:17.056 | Bayer Leverkusen | Carry           @ [55.2, 7.6]
[3818] 00:34:19.128 | Bayer Leverkusen | Pass            -> Alejandro Gr (Complete) @ [56.8, 9.0]
[3819] 00:34:20.208 | Bayer Leverkusen | Ball Receipt*   @ [65.1, 3.4]
[3820] 00:34:20.208 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [65.1, 3.4]
[3821] 00:34:21.193 | Bayer Leverkusen | Ball Receipt*   @ [57.8, 10.2]
[3822] 00:34:21.193 | Bayer Leverkusen | Carry           @ [57.8, 10.2]
[3823] 00:34:21.795 | Bayer Leverkusen | Pass            -> Florian Wirt (Complete) @ [57.4, 7.6]
[3824] 00:34:22.585 | Bayer Leverkusen | Ball Receipt*   @ [68.5, 10.2]
[3825] 00:34:22.585 | Bayer Leverkusen | Carry           @ [68.5, 10.2]
[3826] 00:34:24.216 | Bayer Leverkusen | Dribble         @ [73.1, 9.2]
[3827] 00:34:24.216 | Werder Bremen    | Duel            @ [47.0, 70.9] [CP=True]
[3828] 00:34:25.073 | Bayer Leverkusen | Pressure        @ [70.7, 12.9] [CP=True]
[3829] 00:34:25.173 | Werder Bremen    | Ball Recovery   @ [50.2, 65.5]
```

### Case 48: Episode `3895302_p139_724b3479` (1. Bundesliga)
- **Initiation Delay**: 6.705 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Werder Bremen | **Possession Team**: Werder Bremen
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Interception

```text
[4139] 00:42:38.180 | Bayer Leverkusen | Carry           @ [33.7, 22.9]
[4140] 00:42:38.218 | Bayer Leverkusen | Pass            -> Robert Andri (Complete) @ [34.4, 23.4]
[4141] 00:42:39.997 | Bayer Leverkusen | Ball Receipt*   @ [29.6, 31.0]
[4142] 00:42:39.997 | Bayer Leverkusen | Carry           @ [29.6, 31.0]
[4143] 00:42:40.103 | Bayer Leverkusen | Pass            -> Exequiel Ale (Complete) @ [31.3, 29.7]
[4144] 00:42:40.829 | Bayer Leverkusen | Ball Receipt*   @ [39.3, 24.7]
[4145] 00:42:40.829 | Bayer Leverkusen | Carry           @ [39.3, 24.7]
[4146] 00:42:40.949 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [39.3, 24.7]
[4147] 00:42:42.973 | Bayer Leverkusen | Ball Receipt*   @ [47.7, 55.7]
[4148] 00:42:42.973 | Bayer Leverkusen | Carry           @ [47.7, 55.7]
[4149] 00:42:45.718 | Bayer Leverkusen | Pass            -> Jonas Hofman (Incomplete) @ [77.6, 58.5]
[4150] 00:42:46.702 | Bayer Leverkusen | Ball Receipt*   @ [98.2, 56.2]
[4151] 00:42:46.702 | Werder Bremen    | Interception    @ [26.1, 25.0] [CP=True]
[4152] 00:42:46.702 | Werder Bremen    | Carry           @ [26.1, 25.0]
[4153] 00:42:48.516 | Bayer Leverkusen | Pressure        @ [87.4, 54.0] [CP=True]
```

### Case 49: Episode `3895180_p3_8aeef19c` (1. Bundesliga)
- **Initiation Delay**: 6.664 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Eintracht Frankfurt | **Possession Team**: Eintracht Frankfurt
- **Turnover Event**: Ball Receipt* -> **Initiation Event**: Pass

```text
[13] 00:00:07.429 | Bayer Leverkusen | Carry           @ [61.8, 21.2]
[14] 00:00:07.500 | Bayer Leverkusen | Pass            -> Odilon Kosso (Complete) @ [61.8, 21.2]
[15] 00:00:09.677 | Bayer Leverkusen | Ball Receipt*   @ [35.0, 47.6]
[16] 00:00:09.677 | Bayer Leverkusen | Carry           @ [35.0, 47.6]
[17] 00:00:11.239 | Bayer Leverkusen | Pass            -> Jonas Hofman (Complete) @ [30.1, 49.9]
[18] 00:00:13.147 | Bayer Leverkusen | Ball Receipt*   @ [54.4, 62.6]
[19] 00:00:13.147 | Bayer Leverkusen | Carry           @ [54.4, 62.6]
[20] 00:00:14.771 | Bayer Leverkusen | Pass            -> Jeremie Frim (Incomplete) @ [62.2, 65.2]
[21] 00:00:16.341 | Bayer Leverkusen | Ball Receipt*   @ [79.9, 74.4]
[22] 00:00:16.341 | Eintracht Frankf | Pass            -> Ansgar Knauf (Complete) @ [38.9, 8.4] [CP=True]
[23] 00:00:17.179 | Eintracht Frankf | Ball Receipt*   @ [53.1, 14.3]
[24] 00:00:17.179 | Eintracht Frankf | Carry           @ [53.1, 14.3]
```

### Case 50: Episode `3895180_p32_2f903a53` (1. Bundesliga)
- **Initiation Delay**: 6.936 seconds (Cause D: Ambiguous timestamp/simultaneous event sequence)
- **Counterpressing Team**: Eintracht Frankfurt | **Possession Team**: Eintracht Frankfurt
- **Turnover Event**: Ball Recovery -> **Initiation Event**: Pass

```text
[460] 00:11:18.528 | Bayer Leverkusen | Duel            @ [113.9, 43.8]
[461] 00:11:18.528 | Eintracht Frankf | Clearance       @ [6.2, 36.3]
[462] 00:11:21.476 | Bayer Leverkusen | Ball Recovery   @ [83.5, 73.6]
[463] 00:11:21.476 | Bayer Leverkusen | Carry           @ [83.5, 73.6]
[464] 00:11:22.546 | Bayer Leverkusen | Pass            -> Jeremie Frim (Complete) @ [78.0, 72.3]
[465] 00:11:24.643 | Bayer Leverkusen | Ball Receipt*   @ [68.9, 48.0]
[466] 00:11:24.643 | Bayer Leverkusen | Carry           @ [68.9, 48.0]
[467] 00:11:26.611 | Bayer Leverkusen | Pass            -> Alejandro Gr (Incomplete) @ [68.9, 48.0]
[468] 00:11:28.412 | Bayer Leverkusen | Ball Receipt*   @ [105.7, 56.5]
[469] 00:11:28.412 | Eintracht Frankf | Pass            -> Mario Götze (Complete) @ [16.9, 25.3] [CP=True]
[470] 00:11:30.444 | Eintracht Frankf | Ball Receipt*   @ [39.3, 36.3]
[471] 00:11:30.444 | Eintracht Frankf | Carry           @ [39.3, 36.3]
```
