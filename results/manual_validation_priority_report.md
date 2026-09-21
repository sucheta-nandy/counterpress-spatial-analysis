# Priority Manual Validation Sample (40 Episodes)

This document contains full chronological event traces for the **40 priority review episodes**.

> [!IMPORTANT]
> **Human Review Instructions**:
> All human review fields in `results/tables/manual_validation_priority.csv` are strictly **unpopulated**.
> Do not consider these labels formally human-validated until review has been conducted.
> Assess:
> 1. `human_counterpress_valid`: Is the initiation action a genuine counterpressing attempt?
> 2. `human_turnover_valid`: Did the identified turnover represent the actual change of possession?
> 3. `human_regain_5s`: Was established possession regained within 5.0s?
> 4. `human_dangerous_escape_15s`: Did the opponent create a dangerous transition within 15.0s?
> 5. `human_outcome_3class`: Correct tactical outcome class.

---

### Review Case 1: `3837827_p81_932e1ec0` [ordinary_successful_regain]
- **Match**: 3837827 (Ligue 1)
- **Teams**: Pressing: Rennes | Possessing: Rennes
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:01:26.560) | **Initiation**: Duel (00:01:26.560)
- **Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2094] 00:01:25.096 | Paris Saint-Germ | Pass            -> Warren Zaire (Complete) @ [61.5, 50.4]
[2095] 00:01:25.828 | Paris Saint-Germ | Ball Receipt*   @ [62.7, 41.2]
[2096] 00:01:25.828 | Paris Saint-Germ | Carry           @ [62.7, 41.2]
[2097] 00:01:25.840 | Rennes           | Pressure        @ [60.8, 37.1]
[2098] 00:01:26.560 | Paris Saint-Germ | Dispossessed    @ [62.0, 42.1]
[2099] 00:01:26.560 | Rennes           | Duel            @ [58.1, 38.0] [CP=True]
[2100] 00:01:26.560 | Rennes           | Carry           @ [58.1, 38.0]
[2101] 00:01:27.081 | Paris Saint-Germ | Pressure        @ [60.4, 44.8] [CP=True]
[2102] 00:01:27.377 | Paris Saint-Germ | Dribbled Past   @ [61.5, 44.3] [CP=True]
[2103] 00:01:27.377 | Rennes           | Dribble         @ [58.6, 35.8]
[2104] 00:01:27.377 | Rennes           | Carry           @ [58.6, 35.8]
[2105] 00:01:29.627 | Paris Saint-Germ | Pressure        @ [53.6, 45.3] [CP=True]
[2106] 00:01:31.056 | Rennes           | Dribble         @ [75.0, 33.9]
[2107] 00:01:31.056 | Paris Saint-Germ | Duel            @ [45.1, 46.2] [CP=True]
```

### Review Case 2: `3857258_p145_a3bf4cb0` [ordinary_successful_regain]
- **Match**: 3857258 (FIFA World Cup)
- **Teams**: Pressing: Brazil | Possessing: Brazil
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:37:18.826) | **Initiation**: Pass (00:37:25.209)
- **Delay**: 6.383s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[3101] 00:37:22.300 | Serbia           | Ball Receipt*   @ [34.3, 1.2]
[3102] 00:37:22.300 | Serbia           | Carry           @ [34.3, 1.2]
[3103] 00:37:23.263 | Serbia           | Pass            -> Dušan Tadić (Incomplete) @ [32.5, 2.4]
[3104] 00:37:24.905 | Serbia           | Pressure        @ [45.6, 3.7]
[3105] 00:37:25.209 | Serbia           | Ball Receipt*   @ [45.6, 2.7]
[3106] 00:37:25.209 | Brazil           | Pass            -> Danilo Luiz  (Complete) @ [71.4, 77.7] [CP=True]
[3107] 00:37:25.960 | Brazil           | Ball Receipt*   @ [82.2, 75.9]
[3108] 00:37:25.960 | Brazil           | Carry           @ [82.2, 75.9]
[3109] 00:37:26.120 | Brazil           | Pass            -> Carlos Henri (Complete) @ [78.3, 75.3]
[3110] 00:37:27.106 | Brazil           | Ball Receipt*   @ [68.9, 66.9]
[3111] 00:37:27.106 | Brazil           | Carry           @ [68.9, 66.9]
[3112] 00:37:29.159 | Brazil           | Pass            -> Frederico Ro (Complete) @ [67.6, 61.2]
[3113] 00:37:30.516 | Brazil           | Ball Receipt*   @ [87.3, 57.7]
[3114] 00:37:30.516 | Brazil           | Carry           @ [87.3, 57.7]
```

### Review Case 3: `3857288_p133_70730b88` [ordinary_successful_regain]
- **Match**: 3857288 (FIFA World Cup)
- **Teams**: Pressing: Tunisia | Possessing: Tunisia
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Dispossessed (00:20:02.596) | **Initiation**: Duel (00:20:02.596)
- **Delay**: 0.0s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2329] 00:20:01.469 | Australia        | Ball Receipt*   @ [79.0, 39.7]
[2330] 00:20:01.469 | Australia        | Carry           @ [79.0, 39.7]
[2331] 00:20:01.770 | Tunisia          | Pressure        @ [38.6, 40.8]
[2332] 00:20:02.271 | Tunisia          | Pressure        @ [44.3, 38.9]
[2333] 00:20:02.596 | Australia        | Dispossessed    @ [76.4, 41.0]
[2334] 00:20:02.596 | Tunisia          | Duel            @ [43.7, 39.1] [CP=True]
[2335] 00:20:02.596 | Tunisia          | Carry           @ [43.7, 39.1]
[2336] 00:20:04.131 | Tunisia          | Pass            -> Naïm Sliti (Complete) @ [42.6, 46.3]
[2337] 00:20:05.976 | Tunisia          | Ball Receipt*   @ [55.2, 72.0]
[2338] 00:20:05.976 | Tunisia          | Carry           @ [55.2, 72.0]
[2339] 00:20:10.882 | Tunisia          | Pass            -> Aïssa Bilal  (Complete) @ [71.5, 51.1]
[2340] 00:20:11.858 | Tunisia          | Ball Receipt*   @ [75.1, 31.8]
[2341] 00:20:11.858 | Tunisia          | Carry           @ [75.1, 31.8]
[2342] 00:20:12.564 | Australia        | Pressure        @ [44.3, 50.2]
```

### Review Case 4: `3906390_p113_ba77b5bd` [ordinary_successful_regain]
- **Match**: 3906390 (Women's World Cup)
- **Teams**: Pressing: Spain Women's | Possessing: Spain Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:05:50.867) | **Initiation**: Pressure (00:05:52.775)
- **Delay**: 1.908s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2155] 00:05:49.987 | Spain Women's    | Pass            -> Jennifer Her (Incomplete) @ [85.7, 17.7]
[2156] 00:05:50.867 | Spain Women's    | Ball Receipt*   @ [85.7, 11.9]
[2157] 00:05:50.867 | England Women's  | Interception    @ [34.4, 66.0] [CP=True]
[2158] 00:05:52.300 | England Women's  | Ball Recovery   @ [39.4, 65.6]
[2159] 00:05:52.300 | England Women's  | Carry           @ [39.4, 65.6]
[2160] 00:05:52.775 | Spain Women's    | Pressure        @ [78.3, 9.6] [CP=True]
[2161] 00:05:53.289 | England Women's  | Pass            -> Lauren Hemp (Complete) @ [43.2, 66.6]
[2162] 00:05:54.464 | Spain Women's    | Pressure        @ [42.1, 22.3] [CP=True]
[2163] 00:05:54.505 | England Women's  | Ball Receipt*   @ [75.3, 59.4]
[2164] 00:05:54.505 | England Women's  | Carry           @ [75.3, 59.4]
[2165] 00:05:54.657 | England Women's  | Pass            -> Ella Toone (Incomplete) @ [74.1, 58.8]
[2166] 00:05:56.743 | England Women's  | Ball Receipt*   @ [69.5, 48.3]
[2167] 00:05:56.743 | Spain Women's    | Pass            -> Irene Parede (Complete) @ [45.3, 38.9]
[2168] 00:05:57.972 | Spain Women's    | Ball Receipt*   @ [34.7, 33.5]
```

### Review Case 5: `3893790_p172_aea04013` [ordinary_successful_regain]
- **Match**: 3893790 (Women's World Cup)
- **Teams**: Pressing: Nigeria Women's | Possessing: Nigeria Women's
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:47:04.421) | **Initiation**: Duel (00:47:12.107)
- **Delay**: 7.686s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2742] 00:47:04.421 | Canada Women's   | Carry           @ [48.1, 26.3]
[2743] 00:47:05.541 | Canada Women's   | Pass            -> Cloé Zoé Eyj (Complete) @ [50.5, 27.3]
[2744] 00:47:07.980 | Canada Women's   | Ball Receipt*   @ [80.8, 54.9]
[2745] 00:47:07.980 | Canada Women's   | Carry           @ [80.8, 54.9]
[2746] 00:47:12.107 | Canada Women's   | Dribble         @ [104.6, 51.0]
[2747] 00:47:12.107 | Nigeria Women's  | Duel            @ [15.5, 29.1] [CP=True]
[2748] 00:47:13.254 | Canada Women's   | Ball Recovery   @ [103.9, 54.3]
[2749] 00:47:14.342 | Nigeria Women's  | Ball Recovery   @ [18.8, 24.2]
[2750] 00:47:14.342 | Nigeria Women's  | Carry           @ [18.8, 24.2]
[2751] 00:47:16.251 | Nigeria Women's  | Pass            -> Jennifer Ony (Complete) @ [26.1, 22.2]
[2752] 00:47:17.606 | Nigeria Women's  | Ball Receipt*   @ [34.2, 5.8]
[2753] 00:47:17.606 | Nigeria Women's  | Carry           @ [34.2, 5.8]
[2754] 00:47:20.384 | Nigeria Women's  | Pass            -> Uchenna Kanu (Complete) @ [45.9, 5.0]
[2755] 00:47:21.252 | Nigeria Women's  | Ball Receipt*   @ [65.8, 6.3]
```

### Review Case 6: `3998847_p26_e3799406` [ordinary_successful_regain]
- **Match**: 3998847 (UEFA Women's Euro)
- **Teams**: Pressing: Spain Women's | Possessing: Spain Women's
- **Turnover Context**: immediate_restart_phase (Origin: From Corner)
- **Turnover**: 50/50 (00:09:04.827) | **Initiation**: Pressure (00:09:06.288)
- **Delay**: 1.461s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[331] 00:09:00.315 | Spain Women's    | Pass            (Incomplete) @ [120.0, 0.1]
[332] 00:09:02.002 | Belgium Women's  | Clearance       @ [6.0, 39.5]
[333] 00:09:04.827 | Spain Women's    | 50/50           @ [97.0, 59.4]
[334] 00:09:04.827 | Belgium Women's  | 50/50           @ [23.1, 20.7]
[335] 00:09:04.827 | Belgium Women's  | Carry           @ [23.1, 20.7]
[336] 00:09:06.288 | Spain Women's    | Pressure        @ [97.0, 59.4] [CP=True]
[337] 00:09:08.455 | Belgium Women's  | Pass            -> Jarne Teulin (Complete) @ [21.0, 21.3]
[338] 00:09:09.445 | Belgium Women's  | Ball Receipt*   @ [27.8, 8.9]
[339] 00:09:09.445 | Belgium Women's  | Carry           @ [27.8, 8.9]
[340] 00:09:09.580 | Spain Women's    | Pressure        @ [92.3, 72.1] [CP=True]
[341] 00:09:10.018 | Belgium Women's  | Pass            (Incomplete) @ [27.8, 8.4]
[342] 00:09:11.288 | Spain Women's    | Pass            -> María France (Complete) @ [83.8, 62.9] [CP=True]
[343] 00:09:13.016 | Spain Women's    | Ball Receipt*   @ [87.6, 72.4]
[344] 00:09:13.016 | Spain Women's    | Carry           @ [87.6, 72.4]
```

### Review Case 7: `3837938_p7_bb63490a` [ordinary_successful_regain]
- **Match**: 3837938 (Ligue 1)
- **Teams**: Pressing: Paris Saint-Germain | Possessing: OGC Nice
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:03:34.248) | **Initiation**: Pressure (00:03:36.952)
- **Delay**: 2.704s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[219] 00:03:31.388 | Paris Saint-Germ | Pass            -> Kylian Mbapp (Incomplete) @ [43.6, 58.1]
[220] 00:03:34.248 | Paris Saint-Germ | Ball Receipt*   @ [96.0, 37.9]
[221] 00:03:34.248 | OGC Nice         | Pass            -> Dante Bonfim (Complete) @ [27.2, 34.8] [CP=True]
[222] 00:03:35.465 | OGC Nice         | Ball Receipt*   @ [31.3, 26.6]
[223] 00:03:35.644 | OGC Nice         | Pass            -> Khéphren Thu (Complete) @ [31.3, 25.7]
[224] 00:03:36.952 | Paris Saint-Germ | Pressure        @ [74.1, 55.9] [CP=True]
[225] 00:03:37.010 | OGC Nice         | Ball Receipt*   @ [42.5, 24.2]
[226] 00:03:37.010 | OGC Nice         | Carry           @ [42.5, 24.2]
[227] 00:03:39.129 | OGC Nice         | Pass            -> Nicolas Pépé (Incomplete) @ [39.7, 34.1]
[228] 00:03:41.779 | OGC Nice         | Ball Receipt*   @ [74.4, 60.4]
[229] 00:03:41.779 | Paris Saint-Germ | Ball Recovery   @ [49.0, 18.9]
[230] 00:03:41.779 | Paris Saint-Germ | Carry           @ [49.0, 18.9]
[231] 00:03:42.958 | OGC Nice         | Pressure        @ [72.4, 48.2] [CP=True]
[232] 00:03:43.443 | Paris Saint-Germ | Pass            -> Sergio Ramos (Complete) @ [47.2, 30.8]
```

### Review Case 8: `3802665_p95_879d7810` [ordinary_successful_regain]
- **Match**: 3802665 (Ligue 1)
- **Teams**: Pressing: Montpellier | Possessing: Montpellier
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Receipt* (00:45:12.088) | **Initiation**: Duel (00:45:12.487)
- **Delay**: 0.399s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2062] 00:45:11.609 | Paris Saint-Germ | Pass            -> Sergio Ramos (Complete) @ [29.5, 2.0]
[2063] 00:45:11.831 | Montpellier      | Pressure        @ [82.2, 76.4]
[2064] 00:45:12.088 | Paris Saint-Germ | Ball Receipt*   @ [35.8, 3.7]
[2065] 00:45:12.088 | Paris Saint-Germ | Carry           @ [35.8, 3.7]
[2066] 00:45:12.487 | Paris Saint-Germ | Dispossessed    @ [34.9, 5.5]
[2067] 00:45:12.487 | Montpellier      | Duel            @ [85.2, 74.6] [CP=True]
[2068] 00:45:13.835 | Montpellier      | Pass            -> Joris Chotar (Complete) @ [79.3, 74.4]
[2069] 00:45:14.531 | Montpellier      | Ball Receipt*   @ [87.0, 75.6]
[2070] 00:45:14.531 | Montpellier      | Carry           @ [87.0, 75.6]
[2071] 00:45:14.703 | Montpellier      | Pass            -> Sacha Delaye (Complete) @ [87.0, 75.6]
[2072] 00:45:15.203 | Montpellier      | Ball Receipt*   @ [86.4, 69.6]
[2073] 00:45:15.203 | Montpellier      | Carry           @ [86.4, 69.6]
[2074] 00:45:15.624 | Montpellier      | Pass            -> Stephy Alvar (Incomplete) @ [86.4, 69.6]
[2075] 00:45:17.763 | Montpellier      | Ball Receipt*   @ [90.8, 74.6]
```

### Review Case 9: `3788766_p107_15ad5bb1` [ordinary_successful_regain]
- **Match**: 3788766 (UEFA Euro)
- **Teams**: Pressing: Italy | Possessing: Italy
- **Turnover Context**: open_play (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:08:10.036) | **Initiation**: Pressure (00:08:10.996)
- **Delay**: 0.96s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[1974] 00:08:07.981 | Italy            | Ball Receipt*   @ [62.2, 27.2]
[1975] 00:08:07.981 | Italy            | Carry           @ [62.2, 27.2]
[1976] 00:08:08.018 | Italy            | Miscontrol      @ [61.8, 26.8]
[1977] 00:08:10.036 | Wales            | Ball Recovery   @ [63.0, 76.1]
[1978] 00:08:10.036 | Wales            | Carry           @ [63.0, 76.1]
[1979] 00:08:10.996 | Italy            | Pressure        @ [56.1, 8.0] [CP=True]
[1980] 00:08:11.246 | Wales            | Pass            -> Aaron Ramsey (Complete) @ [63.7, 76.1]
[1981] 00:08:16.091 | Wales            | Ball Receipt*   @ [116.6, 52.1]
[1982] 00:08:16.091 | Wales            | Carry           @ [116.6, 52.1]
[1983] 00:08:17.929 | Wales            | Pass            -> Daniel James (Incomplete) @ [116.3, 51.4]
[1984] 00:08:18.326 | Wales            | Ball Receipt*   @ [109.3, 41.2]
[1985] 00:08:18.326 | Italy            | Ball Recovery   @ [7.7, 32.7]
[1986] 00:08:18.326 | Italy            | Carry           @ [7.7, 32.7]
[1987] 00:08:20.050 | Wales            | Pressure        @ [115.7, 63.9]
```

### Review Case 10: `3893795_p122_8d11ca97` [ordinary_successful_regain]
- **Match**: 3893795 (Women's World Cup)
- **Teams**: Pressing: Denmark Women's | Possessing: Denmark Women's
- **Turnover Context**: immediate_restart_phase (Origin: From Throw In)
- **Turnover**: Ball Recovery (00:11:32.017) | **Initiation**: Pressure (00:11:38.881)
- **Delay**: 6.864s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[2415] 00:11:29.830 | Denmark Women's  | Pass            -> Karen Holmga (Incomplete) @ [105.7, 80.0]
[2416] 00:11:32.017 | Denmark Women's  | Ball Receipt*   @ [109.7, 54.8]
[2417] 00:11:32.017 | China PR Women's | Ball Recovery   @ [9.0, 32.1]
[2418] 00:11:34.249 | China PR Women's | Ball Recovery   @ [19.5, 41.2]
[2419] 00:11:34.249 | China PR Women's | Carry           @ [19.5, 41.2]
[2420] 00:11:38.881 | Denmark Women's  | Pressure        @ [75.8, 14.5] [CP=True]
[2421] 00:11:40.343 | China PR Women's | Pass            -> Jiahui Lou (Incomplete) @ [55.9, 72.7]
[2422] 00:11:42.745 | China PR Women's | Ball Receipt*   @ [78.1, 68.5]
[2423] 00:11:42.745 | Denmark Women's  | Ball Recovery   @ [45.1, 8.8]
[2424] 00:11:42.745 | Denmark Women's  | Carry           @ [45.1, 8.8]
[2425] 00:11:42.905 | China PR Women's | Dribbled Past   @ [75.2, 70.2]
[2426] 00:11:42.905 | Denmark Women's  | Dribble         @ [44.9, 9.9]
[2427] 00:11:42.905 | Denmark Women's  | Carry           @ [44.9, 9.9]
[2428] 00:11:44.487 | Denmark Women's  | Pass            -> Katrine Veje (Complete) @ [37.8, 16.8]
```

### Review Case 11: `3837662_p13_fa9edc11` [ordinary_unsuccessful_regain]
- **Match**: 3837662 (Ligue 1)
- **Teams**: Pressing: Lille | Possessing: Paris Saint-Germain
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:05:06.508) | **Initiation**: Pressure (00:05:07.379)
- **Delay**: 0.871s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[256] 00:05:04.876 | Paris Saint-Germ | Carry           @ [19.2, 50.9]
[257] 00:05:05.720 | Lille            | Pressure        @ [93.2, 27.5] [CP=True]
[258] 00:05:06.508 | Paris Saint-Germ | Pass            -> Vitor Machad (Complete) @ [27.5, 53.0]
[259] 00:05:06.908 | Paris Saint-Germ | Ball Receipt*   @ [42.2, 51.3]
[260] 00:05:06.908 | Paris Saint-Germ | Carry           @ [42.2, 51.3]
[261] 00:05:07.379 | Lille            | Pressure        @ [77.5, 29.2] [CP=True]
[262] 00:05:08.224 | Paris Saint-Germ | Pass            -> Marcos Aoás  (Complete) @ [37.8, 51.3]
[263] 00:05:08.956 | Paris Saint-Germ | Ball Receipt*   @ [30.7, 56.4]
[264] 00:05:08.956 | Paris Saint-Germ | Carry           @ [30.7, 56.4]
[265] 00:05:11.574 | Paris Saint-Germ | Pass            -> Sergio Ramos (Complete) @ [30.7, 56.4]
[266] 00:05:12.820 | Paris Saint-Germ | Ball Receipt*   @ [23.8, 69.7]
[267] 00:05:12.820 | Paris Saint-Germ | Carry           @ [23.8, 69.7]
[268] 00:05:13.577 | Paris Saint-Germ | Pass            -> Vitor Machad (Complete) @ [23.8, 69.7]
[269] 00:05:14.433 | Paris Saint-Germ | Ball Receipt*   @ [36.7, 63.2]
```

### Review Case 12: `3998840_p8_887bac36` [ordinary_unsuccessful_regain]
- **Match**: 3998840 (UEFA Women's Euro)
- **Teams**: Pressing: Poland Women's | Possessing: Germany Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:03:25.853) | **Initiation**: Pressure (00:03:28.464)
- **Delay**: 2.611s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[140] 00:03:25.853 | Germany Women's  | Pass            -> Klara Bühl (Complete) @ [41.1, 8.0]
[141] 00:03:27.211 | Germany Women's  | Ball Receipt*   @ [50.2, 11.7]
[142] 00:03:27.211 | Germany Women's  | Pass            -> Sjoeke Nüske (Complete) @ [50.4, 12.1]
[143] 00:03:27.914 | Germany Women's  | Ball Receipt*   @ [43.3, 23.5]
[144] 00:03:27.914 | Germany Women's  | Carry           @ [43.3, 23.5]
[145] 00:03:28.464 | Poland Women's   | Pressure        @ [76.1, 58.5] [CP=True]
[146] 00:03:30.617 | Germany Women's  | Pass            -> Klara Bühl (Out) @ [42.6, 30.1]
[147] 00:03:34.619 | Germany Women's  | Ball Receipt*   @ [76.8, 14.8]
[148] 00:03:56.195 | Poland Women's   | Pass            (Incomplete) @ [37.3, 80.0]
[149] 00:03:58.180 | Germany Women's  | Clearance       @ [62.7, 2.9]
[150] 00:03:58.707 | Poland Women's   | Pressure        @ [58.1, 77.2]
[151] 00:03:59.007 | Germany Women's  | Pass            (Incomplete) @ [61.9, 1.9]
[152] 00:04:01.211 | Poland Women's   | Pass            (Incomplete) @ [41.8, 76.1]
[153] 00:04:02.757 | Germany Women's  | Pass            -> Lea Schüller (Complete) @ [57.4, 3.1]
```

### Review Case 13: `3998838_p98_25bcc2e1` [ordinary_unsuccessful_regain]
- **Match**: 3998838 (UEFA Women's Euro)
- **Teams**: Pressing: Belgium Women's | Possessing: Italy Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Block (00:02:42.241) | **Initiation**: Pressure (00:02:48.406)
- **Delay**: 6.165s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[1559] 00:02:42.176 | Belgium Women's  | Pass            (Incomplete) @ [119.4, 72.7]
[1560] 00:02:42.241 | Italy Women's    | Block           @ [1.3, 9.1]
[1561] 00:02:43.947 | Italy Women's    | Pass            -> Lisa Boattin (Complete) @ [11.0, 31.5]
[1562] 00:02:45.190 | Italy Women's    | Ball Receipt*   @ [9.0, 19.9]
[1563] 00:02:45.190 | Italy Women's    | Carry           @ [9.0, 19.9]
[1564] 00:02:48.406 | Belgium Women's  | Pressure        @ [103.2, 71.2] [CP=True]
[1565] 00:02:49.182 | Italy Women's    | Pass            -> Emma Severin (Complete) @ [19.8, 8.0]
[1566] 00:02:50.379 | Italy Women's    | Ball Receipt*   @ [29.0, 16.0]
[1567] 00:02:50.379 | Italy Women's    | Carry           @ [29.0, 16.0]
[1568] 00:02:56.197 | Italy Women's    | Pass            -> Sofia Cantor (Complete) @ [58.5, 22.1]
[1569] 00:02:57.544 | Italy Women's    | Ball Receipt*   @ [75.5, 4.0]
[1570] 00:02:57.544 | Italy Women's    | Carry           @ [75.5, 4.0]
[1571] 00:02:59.559 | Belgium Women's  | Pressure        @ [40.7, 76.1]
[1572] 00:03:00.576 | Italy Women's    | Pass            -> Manuela Giug (Complete) @ [75.3, 4.2]
```

### Review Case 14: `3788754_p120_f8d30c17` [ordinary_unsuccessful_regain]
- **Match**: 3788754 (UEFA Euro)
- **Teams**: Pressing: Switzerland | Possessing: Italy
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:18:58.351) | **Initiation**: Pressure (00:18:59.411)
- **Delay**: 1.06s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[2749] 00:18:55.714 | Italy            | Pressure        @ [30.6, 50.2]
[2750] 00:18:56.391 | Switzerland      | Pass            -> Mario Gavran (Incomplete) @ [91.0, 26.5]
[2751] 00:18:58.351 | Switzerland      | Ball Receipt*   @ [111.6, 32.8]
[2752] 00:18:58.351 | Italy            | Ball Recovery   @ [1.4, 46.8]
[2753] 00:18:58.351 | Italy            | Carry           @ [1.4, 46.8]
[2754] 00:18:59.411 | Switzerland      | Pressure        @ [111.6, 29.9] [CP=True]
[2755] 00:19:11.505 | Italy            | Pass            -> Jorge Luiz F (Complete) @ [8.5, 49.0]
[2756] 00:19:13.220 | Italy            | Ball Receipt*   @ [24.0, 33.1]
[2757] 00:19:15.096 | Italy            | Pass            -> Gianluigi Do (Complete) @ [14.9, 30.9]
[2758] 00:19:18.526 | Italy            | Ball Receipt*   @ [3.0, 37.3]
[2759] 00:19:19.088 | Switzerland      | Pressure        @ [110.9, 45.3]
[2760] 00:19:19.724 | Italy            | Pass            -> Jorge Luiz F (Complete) @ [7.1, 41.5]
[2761] 00:19:22.277 | Italy            | Ball Receipt*   @ [31.7, 23.5]
[2762] 00:19:22.277 | Italy            | Carry           @ [31.7, 23.5]
```

### Review Case 15: `3837896_p87_6d38cf89` [ordinary_unsuccessful_regain]
- **Match**: 3837896 (Ligue 1)
- **Teams**: Pressing: Paris Saint-Germain | Possessing: Nantes
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Block (00:05:18.423) | **Initiation**: Pressure (00:05:19.948)
- **Delay**: 1.525s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[2578] 00:05:18.423 | Paris Saint-Germ | Ball Receipt*   @ [97.8, 38.5]
[2579] 00:05:18.423 | Nantes           | Block           @ [29.0, 30.6]
[2580] 00:05:19.207 | Nantes           | Ball Recovery   @ [25.6, 45.0]
[2581] 00:05:19.207 | Nantes           | Carry           @ [25.6, 45.0]
[2582] 00:05:19.761 | Nantes           | Pass            -> Ignatius Kpe (Complete) @ [27.0, 46.7]
[2583] 00:05:19.948 | Paris Saint-Germ | Pressure        @ [88.0, 27.3] [CP=True]
[2584] 00:05:23.384 | Nantes           | Ball Receipt*   @ [38.7, 71.0]
[2585] 00:05:23.384 | Nantes           | Carry           @ [38.7, 71.0]
[2586] 00:05:24.216 | Paris Saint-Germ | Pressure        @ [72.8, 9.1]
[2587] 00:05:24.368 | Nantes           | Pass            -> Florent Moll (Complete) @ [47.7, 75.3]
[2588] 00:05:25.108 | Paris Saint-Germ | Pressure        @ [66.9, 14.2]
[2589] 00:05:25.636 | Nantes           | Ball Receipt*   @ [51.8, 63.5]
[2590] 00:05:25.636 | Nantes           | Carry           @ [51.8, 63.5]
[2591] 00:05:26.831 | Nantes           | Pass            -> Fabien Cento (Complete) @ [50.6, 63.5]
```

### Review Case 16: `3893801_p46_531f18b3` [ordinary_unsuccessful_regain]
- **Match**: 3893801 (Women's World Cup)
- **Teams**: Pressing: Brazil Women's | Possessing: Panama Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:24:15.178) | **Initiation**: Pressure (00:24:15.778)
- **Delay**: 0.6s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[880] 00:24:14.000 | Brazil Women's   | Carry           @ [104.9, 73.1]
[881] 00:24:14.375 | Panama Women's   | Pressure        @ [15.0, 8.1]
[882] 00:24:15.178 | Brazil Women's   | Dribble         @ [104.7, 71.6]
[883] 00:24:15.178 | Panama Women's   | Duel            @ [15.4, 8.5] [CP=True]
[884] 00:24:15.178 | Panama Women's   | Carry           @ [15.4, 8.5]
[885] 00:24:15.778 | Brazil Women's   | Pressure        @ [104.9, 71.6] [CP=True]
[886] 00:24:18.872 | Panama Women's   | Pass            -> Schiandra Ya (Complete) @ [10.7, 7.2]
[887] 00:24:20.134 | Panama Women's   | Ball Receipt*   @ [15.7, 15.8]
[888] 00:24:20.134 | Panama Women's   | Pass            -> Marta Alexan (Complete) @ [15.7, 13.6]
[889] 00:24:21.470 | Panama Women's   | Ball Receipt*   @ [24.6, 5.5]
[890] 00:24:21.470 | Panama Women's   | Carry           @ [24.6, 5.5]
[891] 00:24:21.785 | Panama Women's   | Pass            -> Karla Paola  (Incomplete) @ [25.1, 6.8]
[892] 00:24:22.731 | Panama Women's   | Ball Receipt*   @ [35.3, 15.1]
[893] 00:24:22.731 | Brazil Women's   | Pass            -> Antonia Ronn (Complete) @ [85.8, 64.1]
```

### Review Case 17: `3788741_p35_447ab819` [ordinary_unsuccessful_regain]
- **Match**: 3788741 (UEFA Euro)
- **Teams**: Pressing: Italy | Possessing: Turkey
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:14:33.536) | **Initiation**: Foul Committed (00:14:33.831)
- **Delay**: 0.295s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[671] 00:14:32.895 | Italy            | Carry           @ [97.1, 10.1]
[672] 00:14:33.059 | Turkey           | Pressure        @ [27.5, 68.9]
[673] 00:14:33.536 | Italy            | Dispossessed    @ [95.7, 14.6]
[674] 00:14:33.536 | Turkey           | Duel            @ [24.4, 65.5] [CP=True]
[675] 00:14:33.536 | Turkey           | Carry           @ [24.4, 65.5]
[676] 00:14:33.831 | Italy            | Foul Committed  @ [95.7, 13.9] [CP=True]
[677] 00:14:33.831 | Turkey           | Foul Won        @ [24.4, 66.2]
[678] 00:15:14.458 | Turkey           | Pass            -> Kenan Karama (Incomplete) @ [26.6, 61.7]
[679] 00:15:18.448 | Turkey           | Ball Receipt*   @ [90.1, 75.1]
[680] 00:15:18.448 | Turkey           | Duel            @ [91.8, 74.9]
[681] 00:15:18.448 | Italy            | Clearance       @ [28.3, 5.2]
[682] 00:15:19.553 | Italy            | Pressure        @ [34.1, 20.4]
[683] 00:15:19.747 | Turkey           | Pass            -> Ozan Tufan (Complete) @ [84.6, 56.6]
[684] 00:15:20.626 | Turkey           | Ball Receipt*   @ [81.2, 65.5]
```

### Review Case 18: `3857276_p12_fcc6b2e3` [ordinary_unsuccessful_regain]
- **Match**: 3857276 (FIFA World Cup)
- **Teams**: Pressing: Morocco | Possessing: Canada
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:05:49.229) | **Initiation**: Pressure (00:05:49.485)
- **Delay**: 0.256s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[240] 00:05:47.247 | Morocco          | Ball Receipt*   @ [42.3, 8.4]
[241] 00:05:47.247 | Canada           | Duel            @ [76.8, 71.2]
[242] 00:05:47.247 | Morocco          | Pass            (Incomplete) @ [43.3, 8.9]
[243] 00:05:49.229 | Canada           | Ball Recovery   @ [55.5, 68.8]
[244] 00:05:49.229 | Canada           | Carry           @ [55.5, 68.8]
[245] 00:05:49.485 | Morocco          | Pressure        @ [63.1, 11.3] [CP=True]
[246] 00:05:49.885 | Canada           | Pass            -> Steven de So (Complete) @ [56.0, 68.8]
[247] 00:05:51.283 | Canada           | Ball Receipt*   @ [42.3, 59.4]
[248] 00:05:51.283 | Canada           | Pass            -> Mark Anthony (Complete) @ [42.8, 59.4]
[249] 00:05:52.212 | Canada           | Ball Receipt*   @ [54.9, 50.2]
[250] 00:05:52.212 | Canada           | Carry           @ [54.9, 50.2]
[251] 00:05:52.293 | Canada           | Miscontrol      @ [54.9, 50.2]
[252] 00:05:53.377 | Morocco          | Ball Recovery   @ [53.2, 31.2]
[253] 00:05:53.377 | Morocco          | Carry           @ [53.2, 31.2]
```

### Review Case 19: `3837954_p102_c3d7ac6b` [ordinary_unsuccessful_regain]
- **Match**: 3837954 (Ligue 1)
- **Teams**: Pressing: Paris Saint-Germain | Possessing: Angers
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:20:08.392) | **Initiation**: Pressure (00:20:09.388)
- **Delay**: 0.996s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[3255] 00:20:07.661 | Paris Saint-Germ | Carry           @ [102.1, 44.1]
[3256] 00:20:08.029 | Paris Saint-Germ | Pass            -> Lionel André (Incomplete) @ [102.1, 44.1]
[3257] 00:20:08.392 | Paris Saint-Germ | Ball Receipt*   @ [107.1, 46.1]
[3258] 00:20:08.392 | Angers           | Interception    @ [15.1, 34.3] [CP=True]
[3259] 00:20:08.392 | Angers           | Carry           @ [15.1, 34.3]
[3260] 00:20:09.388 | Paris Saint-Germ | Pressure        @ [104.1, 42.4] [CP=True]
[3261] 00:20:10.023 | Angers           | Pass            -> Abdoulaye Ba (Complete) @ [15.1, 38.1]
[3262] 00:20:12.027 | Angers           | Ball Receipt*   @ [21.0, 61.9]
[3263] 00:20:12.027 | Angers           | Carry           @ [21.0, 61.9]
[3264] 00:20:13.559 | Angers           | Pass            -> Himad Abdell (Complete) @ [24.4, 68.1]
[3265] 00:20:14.542 | Angers           | Ball Receipt*   @ [38.3, 61.9]
[3266] 00:20:14.542 | Angers           | Carry           @ [38.3, 61.9]
[3267] 00:20:16.565 | Angers           | Pass            -> Batista Mend (Complete) @ [51.0, 71.7]
[3268] 00:20:17.997 | Angers           | Ball Receipt*   @ [43.2, 61.0]
```

### Review Case 20: `3895167_p51_d51517b5` [ordinary_unsuccessful_regain]
- **Match**: 3895167 (1. Bundesliga)
- **Teams**: Pressing: Bayer Leverkusen | Possessing: VfB Stuttgart
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:27:43.575) | **Initiation**: Pressure (00:27:47.559)
- **Delay**: 3.984s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `0` | 3-Class: `harmless_escape`

```text
[1215] 00:27:44.944 | VfB Stuttgart    | Ball Receipt*   @ [67.9, 38.8]
[1216] 00:27:44.944 | VfB Stuttgart    | Carry           @ [67.9, 38.8]
[1217] 00:27:45.681 | VfB Stuttgart    | Pass            -> Dan-Axel Zag (Complete) @ [64.1, 36.2]
[1218] 00:27:46.805 | VfB Stuttgart    | Ball Receipt*   @ [55.6, 26.8]
[1219] 00:27:46.805 | VfB Stuttgart    | Carry           @ [55.6, 26.8]
[1220] 00:27:47.559 | Bayer Leverkusen | Pressure        @ [63.0, 55.0] [CP=True]
[1221] 00:27:47.767 | VfB Stuttgart    | Pass            -> Alexander Nü (Complete) @ [55.4, 27.0]
[1222] 00:27:50.072 | VfB Stuttgart    | Ball Receipt*   @ [19.3, 37.7]
[1223] 00:27:50.072 | VfB Stuttgart    | Carry           @ [19.3, 37.7]
[1224] 00:27:54.355 | VfB Stuttgart    | Pass            -> Dan-Axel Zag (Complete) @ [20.3, 38.2]
[1225] 00:27:55.620 | VfB Stuttgart    | Ball Receipt*   @ [24.2, 23.9]
[1226] 00:27:55.620 | VfB Stuttgart    | Carry           @ [24.2, 23.9]
[1227] 00:27:58.147 | VfB Stuttgart    | Pass            -> Alexander Nü (Complete) @ [23.5, 23.2]
[1228] 00:28:00.335 | VfB Stuttgart    | Ball Receipt*   @ [12.1, 37.7]
```

### Review Case 21: `3788755_p18_b58f036d` [dangerous_shot]
- **Match**: 3788755 (UEFA Euro)
- **Teams**: Pressing: Wales | Possessing: Turkey
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:08:20.865) | **Initiation**: Pressure (00:08:22.961)
- **Delay**: 2.096s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[357] 00:08:19.401 | Wales            | Pass            -> Gareth Frank (Incomplete) @ [48.5, 0.1]
[358] 00:08:20.865 | Wales            | Ball Receipt*   @ [65.1, 7.9]
[359] 00:08:20.865 | Turkey           | Pass            -> Okay Yokuşlu (Complete) @ [54.7, 71.0]
[360] 00:08:22.279 | Turkey           | Ball Receipt*   @ [57.9, 64.5]
[361] 00:08:22.279 | Turkey           | Carry           @ [57.9, 64.5]
[362] 00:08:22.961 | Wales            | Pressure        @ [56.6, 13.6] [CP=True]
[363] 00:08:23.038 | Turkey           | Pass            -> Hakan Çalhan (Complete) @ [62.0, 64.2]
[364] 00:08:23.425 | Wales            | Pressure        @ [50.9, 21.9] [CP=True]
[365] 00:08:23.613 | Turkey           | Ball Receipt*   @ [67.4, 58.9]
[366] 00:08:23.613 | Turkey           | Carry           @ [67.4, 58.9]
[367] 00:08:24.018 | Wales            | Foul Committed  @ [52.4, 13.2] [CP=True]
[368] 00:08:24.018 | Turkey           | Foul Won        @ [67.7, 66.9]
[369] 00:08:27.525 | Turkey           | Pass            -> Cengiz Ünder (Complete) @ [67.4, 75.5]
[370] 00:08:30.519 | Turkey           | Ball Receipt*   @ [98.5, 72.8]
```

### Review Case 22: `3893805_p151_f4fb206d` [dangerous_shot]
- **Match**: 3893805 (Women's World Cup)
- **Teams**: Pressing: Costa Rica Women's | Possessing: Japan Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:31:35.148) | **Initiation**: Pressure (00:31:37.646)
- **Delay**: 2.498s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2993] 00:31:33.930 | Costa Rica Women | Pass            -> María Paula  (Incomplete) @ [33.4, 66.4]
[2994] 00:31:35.148 | Costa Rica Women | Ball Receipt*   @ [44.0, 74.0]
[2995] 00:31:35.148 | Japan Women's    | Interception    @ [77.3, 9.1] [CP=True]
[2996] 00:31:35.148 | Japan Women's    | Carry           @ [77.3, 9.1]
[2997] 00:31:36.742 | Japan Women's    | Pass            -> Riko Ueki (Complete) @ [85.8, 13.0]
[2998] 00:31:37.646 | Costa Rica Women | Pressure        @ [32.6, 54.4] [CP=True]
[2999] 00:31:37.731 | Japan Women's    | Ball Receipt*   @ [88.9, 28.6]
[3000] 00:31:37.731 | Japan Women's    | Carry           @ [88.9, 28.6]
[3001] 00:31:39.124 | Japan Women's    | Pass            -> Hinata Miyaz (Complete) @ [93.8, 33.0]
[3002] 00:31:40.049 | Japan Women's    | Ball Receipt*   @ [101.0, 41.1]
[3003] 00:31:40.049 | Japan Women's    | Carry           @ [101.0, 41.1]
[3004] 00:31:41.534 | Japan Women's    | Shot            (Saved) @ [101.3, 43.2]
[3005] 00:31:42.632 | Costa Rica Women | Goal Keeper     @ [2.1, 39.5]
[3006] 00:32:06.060 | Costa Rica Women | Pass            -> Sheika Dalei (Incomplete) @ [14.6, 39.3]
```

### Review Case 23: `3802793_p128_5060fc9f` [dangerous_shot]
- **Match**: 3802793 (Ligue 1)
- **Teams**: Pressing: OGC Nice | Possessing: Paris Saint-Germain
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:18:44.071) | **Initiation**: Pressure (00:18:47.101)
- **Delay**: 3.03s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2827] 00:18:42.894 | Paris Saint-Germ | Pressure        @ [65.1, 49.1]
[2828] 00:18:43.435 | OGC Nice         | Pass            -> Dante Bonfim (Incomplete) @ [57.4, 28.6]
[2829] 00:18:44.071 | OGC Nice         | Ball Receipt*   @ [41.5, 25.0]
[2830] 00:18:44.071 | Paris Saint-Germ | Interception    @ [68.5, 51.9] [CP=True]
[2831] 00:18:44.071 | Paris Saint-Germ | Carry           @ [68.5, 51.9]
[2832] 00:18:47.101 | OGC Nice         | Pressure        @ [27.6, 30.5] [CP=True]
[2833] 00:18:48.080 | Paris Saint-Germ | Pass            -> Ángel Fabián (Incomplete) @ [93.7, 50.4]
[2834] 00:18:48.300 | Paris Saint-Germ | Ball Receipt*   @ [101.2, 56.2]
[2835] 00:18:48.300 | OGC Nice         | Interception    @ [22.9, 28.8] [CP=True]
[2836] 00:18:50.314 | Paris Saint-Germ | Pass            -> Lionel André (Complete) @ [89.0, 55.8]
[2837] 00:18:51.273 | Paris Saint-Germ | Ball Receipt*   @ [94.0, 37.8]
[2838] 00:18:51.273 | Paris Saint-Germ | Carry           @ [94.0, 37.8]
[2839] 00:18:51.911 | OGC Nice         | Pressure        @ [19.5, 44.7]
[2840] 00:18:52.638 | Paris Saint-Germ | Pass            -> Kylian Mbapp (Complete) @ [93.1, 35.4]
```

### Review Case 24: `3773597_p26_7e73f311` [dangerous_shot]
- **Match**: 3773597 (La Liga)
- **Teams**: Pressing: Real Sociedad | Possessing: Barcelona
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:16:33.884) | **Initiation**: Pressure (00:16:34.284)
- **Delay**: 0.4s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[780] 00:16:31.127 | Real Sociedad    | Carry           @ [44.2, 13.4]
[781] 00:16:31.127 | Barcelona        | Block           @ [100.2, 53.5]
[782] 00:16:32.883 | Barcelona        | Pressure        @ [77.9, 67.2]
[783] 00:16:33.322 | Real Sociedad    | Miscontrol      @ [39.4, 12.7]
[784] 00:16:33.884 | Barcelona        | Pass            -> Sergio Busqu (Complete) @ [79.6, 67.4]
[785] 00:16:34.284 | Real Sociedad    | Pressure        @ [32.9, 17.7] [CP=True]
[786] 00:16:34.620 | Barcelona        | Ball Receipt*   @ [85.3, 64.3]
[787] 00:16:34.620 | Barcelona        | Carry           @ [85.3, 64.3]
[788] 00:16:36.101 | Barcelona        | Pass            -> Lionel André (Complete) @ [88.2, 67.4]
[789] 00:16:36.690 | Barcelona        | Ball Receipt*   @ [94.4, 55.0]
[790] 00:16:36.690 | Barcelona        | Carry           @ [94.4, 55.0]
[791] 00:16:37.052 | Real Sociedad    | Pressure        @ [29.1, 24.4] [CP=True]
[792] 00:16:38.662 | Barcelona        | Shot            (Blocked) @ [99.5, 45.1]
[793] 00:16:38.943 | Real Sociedad    | Block           @ [18.4, 35.5]
```

### Review Case 25: `3837859_p152_f43e1242` [dangerous_shot]
- **Match**: 3837859 (Ligue 1)
- **Teams**: Pressing: Toulouse | Possessing: Paris Saint-Germain
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:46:19.850) | **Initiation**: Pressure (00:46:21.412)
- **Delay**: 1.562s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[3796] 00:46:17.702 | Paris Saint-Germ | Pressure        @ [103.6, 58.6]
[3797] 00:46:17.852 | Toulouse         | Pass            (Incomplete) @ [16.2, 22.8]
[3798] 00:46:19.850 | Paris Saint-Germ | Pass            -> Lionel André (Complete) @ [85.1, 59.2]
[3799] 00:46:21.213 | Paris Saint-Germ | Ball Receipt*   @ [99.7, 65.3]
[3800] 00:46:21.213 | Paris Saint-Germ | Carry           @ [99.7, 65.3]
[3801] 00:46:21.412 | Toulouse         | Pressure        @ [22.2, 14.2] [CP=True]
[3802] 00:46:25.659 | Toulouse         | Pressure        @ [21.5, 39.3]
[3803] 00:46:26.102 | Paris Saint-Germ | Pass            -> Ismaël Gharb (Complete) @ [96.4, 38.8]
[3804] 00:46:27.332 | Paris Saint-Germ | Ball Receipt*   @ [103.9, 21.8]
[3805] 00:46:27.332 | Paris Saint-Germ | Carry           @ [103.9, 21.8]
[3806] 00:46:30.046 | Paris Saint-Germ | Shot            (Blocked) @ [102.9, 34.2]
[3807] 00:46:30.108 | Paris Saint-Germ | Block           @ [104.4, 34.8]
[3808] 00:46:30.339 | Toulouse         | Goal Keeper     @ [3.0, 41.6]
[3809] 00:46:40.482 | Toulouse         | Pass            -> Anthony Roua (Complete) @ [7.0, 44.1]
```

### Review Case 26: `3930176_p61_41cce0ac` [final_third_penetration]
- **Match**: 3930176 (UEFA Euro)
- **Teams**: Pressing: Switzerland | Possessing: Germany
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:39:01.356) | **Initiation**: Pressure (00:39:02.576)
- **Delay**: 1.22s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[1616] 00:38:59.509 | Switzerland      | Ball Receipt*   @ [73.4, 68.6]
[1617] 00:38:59.509 | Switzerland      | Pass            (Incomplete) @ [73.7, 69.1]
[1618] 00:38:59.708 | Germany          | Block           @ [45.0, 12.6]
[1619] 00:39:00.873 | Switzerland      | Pressure        @ [66.8, 70.5]
[1620] 00:39:01.356 | Germany          | Pass            -> Kai Havertz (Complete) @ [51.4, 7.1]
[1621] 00:39:02.576 | Switzerland      | Pressure        @ [57.8, 63.1] [CP=True]
[1622] 00:39:02.722 | Germany          | Ball Receipt*   @ [59.4, 15.7]
[1623] 00:39:02.722 | Germany          | Carry           @ [59.4, 15.7]
[1624] 00:39:02.776 | Germany          | Pass            -> Maximilian M (Complete) @ [59.0, 15.6]
[1625] 00:39:04.637 | Germany          | Ball Receipt*   @ [69.7, 7.1]
[1626] 00:39:04.637 | Germany          | Carry           @ [69.7, 7.1]
[1627] 00:39:04.832 | Germany          | Pass            -> Florian Wirt (Incomplete) @ [71.5, 7.6]
[1628] 00:39:07.142 | Germany          | Pressure        @ [99.2, 15.7]
[1629] 00:39:07.832 | Germany          | Ball Receipt*   @ [98.3, 17.0]
```

### Review Case 27: `3788771_p151_5d4cb613` [final_third_penetration]
- **Match**: 3788771 (UEFA Euro)
- **Teams**: Pressing: Scotland | Possessing: Croatia
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:34:02.319) | **Initiation**: Pressure (00:34:07.023)
- **Delay**: 4.704s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[3095] 00:34:00.713 | Croatia          | Clearance       @ [7.2, 40.3]
[3096] 00:34:02.076 | Scotland         | Pressure        @ [91.2, 29.4]
[3097] 00:34:02.319 | Croatia          | Pass            -> Andrej Krama (Complete) @ [29.9, 57.7]
[3098] 00:34:03.515 | Croatia          | Ball Receipt*   @ [39.6, 50.9]
[3099] 00:34:03.515 | Croatia          | Carry           @ [39.6, 50.9]
[3100] 00:34:07.023 | Scotland         | Pressure        @ [61.6, 51.4] [CP=True]
[3101] 00:34:09.955 | Croatia          | Pass            -> Ivan Perišić (Complete) @ [73.3, 18.9]
[3102] 00:34:10.818 | Croatia          | Ball Receipt*   @ [68.7, 14.9]
[3103] 00:34:10.818 | Croatia          | Carry           @ [68.7, 14.9]
[3104] 00:34:13.617 | Scotland         | Pressure        @ [41.0, 60.7]
[3105] 00:34:16.329 | Croatia          | Pass            -> Andrej Krama (Incomplete) @ [93.1, 25.4]
[3106] 00:34:16.918 | Croatia          | Ball Receipt*   @ [92.1, 36.9]
[3107] 00:34:16.918 | Scotland         | Interception    @ [27.0, 49.7]
[3108] 00:34:18.669 | Croatia          | Pressure        @ [106.1, 34.2]
```

### Review Case 28: `3901832_p94_db3966bf` [final_third_penetration]
- **Match**: 3901832 (Women's World Cup)
- **Teams**: Pressing: Colombia Women's | Possessing: Jamaica Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:00:18.266) | **Initiation**: Block (00:00:22.658)
- **Delay**: 4.392s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[1447] 00:00:18.266 | Jamaica Women's  | Pass            -> Allyson Swab (Complete) @ [32.7, 64.1]
[1448] 00:00:19.590 | Jamaica Women's  | Ball Receipt*   @ [27.1, 64.4]
[1449] 00:00:19.590 | Jamaica Women's  | Pass            -> Khadija Moni (Complete) @ [25.4, 64.4]
[1450] 00:00:22.658 | Jamaica Women's  | Ball Receipt*   @ [70.7, 61.3]
[1451] 00:00:22.658 | Jamaica Women's  | Carry           @ [70.7, 61.3]
[1452] 00:00:22.658 | Colombia Women's | Block           @ [48.6, 18.0] [CP=True]
[1453] 00:00:25.396 | Colombia Women's | Pressure        @ [46.7, 29.1]
[1454] 00:00:25.887 | Jamaica Women's  | Pass            -> Jody Brown (Complete) @ [72.8, 51.5]
[1455] 00:00:27.962 | Jamaica Women's  | Ball Receipt*   @ [70.7, 31.5]
[1456] 00:00:27.962 | Jamaica Women's  | Carry           @ [70.7, 31.5]
[1457] 00:00:29.059 | Jamaica Women's  | Pass            -> Drew Spence (Complete) @ [73.8, 31.8]
[1458] 00:00:30.111 | Jamaica Women's  | Ball Receipt*   @ [80.4, 49.6]
[1459] 00:00:30.111 | Jamaica Women's  | Carry           @ [80.4, 49.6]
[1460] 00:00:32.251 | Jamaica Women's  | Pass            -> Trudi Sudan  (Complete) @ [87.6, 53.3]
```

### Review Case 29: `3938639_p152_b585e681` [final_third_penetration]
- **Match**: 3938639 (UEFA Euro)
- **Teams**: Pressing: Turkey | Possessing: Georgia
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:48:39.961) | **Initiation**: Pressure (00:48:41.688)
- **Delay**: 1.727s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[3762] 00:48:40.695 | Georgia          | Ball Receipt*   @ [49.4, 29.2]
[3763] 00:48:40.695 | Georgia          | Carry           @ [49.4, 29.2]
[3764] 00:48:40.708 | Georgia          | Pass            -> Giorgi Kocho (Complete) @ [49.6, 29.2]
[3765] 00:48:41.505 | Georgia          | Ball Receipt*   @ [44.4, 32.1]
[3766] 00:48:41.505 | Georgia          | Carry           @ [44.4, 32.1]
[3767] 00:48:41.688 | Turkey           | Pressure        @ [77.6, 46.8] [CP=True]
[3768] 00:48:42.303 | Turkey           | Foul Committed  @ [71.4, 50.4] [CP=True]
[3769] 00:48:42.303 | Georgia          | Foul Won        @ [48.7, 29.7]
[3770] 00:48:49.455 | Georgia          | Pass            -> Otar Kakabad (Complete) @ [51.8, 31.8]
[3771] 00:48:52.047 | Georgia          | Ball Receipt*   @ [63.6, 73.0]
[3772] 00:48:52.047 | Georgia          | Carry           @ [63.6, 73.0]
[3773] 00:48:53.837 | Georgia          | Pass            -> Budu Zivziva (Complete) @ [82.0, 72.5]
[3774] 00:48:54.951 | Turkey           | Pressure        @ [13.5, 31.0]
[3775] 00:48:55.279 | Georgia          | Ball Receipt*   @ [105.7, 51.2]
```

### Review Case 30: `3877090_p118_ddf5c3ae` [final_third_penetration]
- **Match**: 3877090 (Major League Soccer)
- **Teams**: Pressing: LAFC | Possessing: Inter Miami
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Duel (00:12:54.258) | **Initiation**: Pressure (00:12:58.119)
- **Delay**: 3.861s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2239] 00:12:52.270 | Inter Miami      | Pressure        @ [44.5, 20.5] [CP=True]
[2240] 00:12:54.258 | LAFC             | Dribble         @ [86.5, 55.0]
[2241] 00:12:54.258 | Inter Miami      | Duel            @ [33.6, 25.1] [CP=True]
[2242] 00:12:56.045 | Inter Miami      | Ball Recovery   @ [38.0, 29.4]
[2243] 00:12:56.045 | Inter Miami      | Carry           @ [38.0, 29.4]
[2244] 00:12:58.119 | LAFC             | Pressure        @ [75.2, 47.2] [CP=True]
[2245] 00:12:59.028 | Inter Miami      | Pass            -> Facundo Farí (Complete) @ [42.2, 26.7]
[2246] 00:13:01.562 | Inter Miami      | Ball Receipt*   @ [46.3, 3.1]
[2247] 00:13:01.562 | Inter Miami      | Carry           @ [46.3, 3.1]
[2248] 00:13:03.442 | Inter Miami      | Pass            -> Jordi Alba R (Complete) @ [50.0, 1.7]
[2249] 00:13:05.588 | Inter Miami      | Ball Receipt*   @ [87.9, 16.5]
[2250] 00:13:05.588 | Inter Miami      | Carry           @ [87.9, 16.5]
[2251] 00:13:09.484 | Inter Miami      | Pass            -> Benjamin Cre (Complete) @ [99.7, 8.5]
[2252] 00:13:10.502 | LAFC             | Pressure        @ [21.0, 56.3]
```

### Review Case 31: `3930162_p126_6e7317f9` [initiation_delay_over_5s]
- **Match**: 3930162 (UEFA Euro)
- **Teams**: Pressing: Slovenia | Possessing: Slovenia
- **Turnover Context**: open_play (Origin: From Goal Kick)
- **Turnover**: Ball Recovery (00:38:34.190) | **Initiation**: Pressure (00:38:41.935)
- **Delay**: 7.745s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[3135] 00:38:34.190 | Denmark          | Ball Recovery   @ [44.5, 7.1]
[3136] 00:38:34.190 | Denmark          | Carry           @ [44.5, 7.1]
[3137] 00:38:37.491 | Denmark          | Pass            -> Kasper Schme (Complete) @ [35.0, 6.4]
[3138] 00:38:39.722 | Denmark          | Ball Receipt*   @ [7.8, 34.0]
[3139] 00:38:39.722 | Denmark          | Carry           @ [7.8, 34.0]
[3140] 00:38:41.935 | Slovenia         | Pressure        @ [100.6, 44.0] [CP=True]
[3141] 00:38:42.715 | Denmark          | Pass            -> Yussuf Yurar (Incomplete) @ [8.5, 39.1]
[3142] 00:38:45.762 | Denmark          | Ball Receipt*   @ [69.2, 38.7]
[3143] 00:38:45.762 | Slovenia         | Pass            -> Jon Gorenc S (Complete) @ [57.0, 45.8]
[3144] 00:38:46.464 | Slovenia         | Ball Receipt*   @ [60.2, 39.2]
[3145] 00:38:46.464 | Slovenia         | Carry           @ [60.2, 39.2]
[3146] 00:38:47.195 | Slovenia         | Pass            -> Andraž Špora (Incomplete) @ [60.2, 39.9]
[3147] 00:38:48.478 | Slovenia         | Ball Receipt*   @ [83.2, 39.9]
[3148] 00:38:48.478 | Denmark          | Pass            -> Christian Da (Complete) @ [40.5, 37.5] [CP=True]
```

### Review Case 32: `3857290_p22_379d5832` [initiation_delay_over_5s]
- **Match**: 3857290 (FIFA World Cup)
- **Teams**: Pressing: Switzerland | Possessing: Switzerland
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:11:06.904) | **Initiation**: Interception (00:11:13.634)
- **Delay**: 6.73s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[507] 00:11:11.109 | Cameroon         | Ball Receipt*   @ [53.5, 38.7]
[508] 00:11:11.915 | Cameroon         | Pass            -> Martin Hongl (Complete) @ [50.6, 35.2]
[509] 00:11:13.046 | Cameroon         | Ball Receipt*   @ [41.8, 38.9]
[510] 00:11:13.046 | Cameroon         | Carry           @ [41.8, 38.9]
[511] 00:11:13.080 | Cameroon         | Pass            (Incomplete) @ [41.0, 38.9]
[512] 00:11:13.634 | Switzerland      | Interception    @ [73.7, 47.0] [CP=True]
[513] 00:11:13.634 | Switzerland      | Carry           @ [73.7, 47.0]
[514] 00:11:14.588 | Cameroon         | Pressure        @ [43.7, 34.6] [CP=True]
[515] 00:11:14.754 | Switzerland      | Pass            -> Djibril Sow (Complete) @ [75.6, 47.2]
[516] 00:11:15.326 | Switzerland      | Ball Receipt*   @ [84.5, 47.0]
[517] 00:11:15.326 | Switzerland      | Carry           @ [84.5, 47.0]
[518] 00:11:16.043 | Switzerland      | Pass            -> Granit Xhaka (Complete) @ [85.3, 45.5]
[519] 00:11:16.929 | Switzerland      | Ball Receipt*   @ [83.9, 28.7]
[520] 00:11:16.929 | Switzerland      | Carry           @ [83.9, 28.7]
```

### Review Case 33: `3773547_p123_7978608c` [initiation_delay_over_5s]
- **Match**: 3773547 (La Liga)
- **Teams**: Pressing: Osasuna | Possessing: Barcelona
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:05:10.117) | **Initiation**: Pressure (00:05:17.799)
- **Delay**: 7.682s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2447] 00:05:14.392 | Barcelona        | Ball Receipt*   @ [72.7, 23.6]
[2448] 00:05:14.392 | Barcelona        | Carry           @ [72.7, 23.6]
[2449] 00:05:15.356 | Barcelona        | Pass            -> Lionel André (Complete) @ [76.2, 28.9]
[2450] 00:05:16.314 | Barcelona        | Ball Receipt*   @ [88.6, 39.9]
[2451] 00:05:16.314 | Barcelona        | Carry           @ [88.6, 39.9]
[2452] 00:05:17.799 | Osasuna          | Pressure        @ [27.2, 40.2] [CP=True]
[2453] 00:05:18.274 | Osasuna          | Dribbled Past   @ [29.7, 40.2] [CP=True]
[2454] 00:05:18.274 | Barcelona        | Dribble         @ [90.4, 39.9]
[2455] 00:05:18.274 | Barcelona        | Carry           @ [90.4, 39.9]
[2456] 00:05:19.341 | Osasuna          | Pressure        @ [22.3, 47.4] [CP=True]
[2457] 00:05:19.720 | Barcelona        | Pass            -> Martin Brait (Complete) @ [95.7, 32.7]
[2458] 00:05:21.032 | Barcelona        | Ball Receipt*   @ [110.1, 25.0]
[2459] 00:05:21.032 | Barcelona        | Carry           @ [110.1, 25.0]
[2460] 00:05:21.112 | Barcelona        | Pass            -> Philippe Cou (Incomplete) @ [110.1, 25.0]
```

### Review Case 34: `3803000_p18_8d0b4f71` [initiation_delay_over_5s]
- **Match**: 3803000 (Ligue 1)
- **Teams**: Pressing: Clermont Foot | Possessing: Paris Saint-Germain
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:10:16.205) | **Initiation**: Pressure (00:10:22.603)
- **Delay**: 6.398s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `0` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[478] 00:10:18.493 | Paris Saint-Germ | Pass            -> Idrissa Gana (Complete) @ [34.2, 37.0]
[479] 00:10:19.337 | Paris Saint-Germ | Ball Receipt*   @ [42.6, 18.3]
[480] 00:10:20.324 | Paris Saint-Germ | Pass            -> Kylian Mbapp (Complete) @ [42.6, 18.3]
[481] 00:10:21.058 | Paris Saint-Germ | Ball Receipt*   @ [51.4, 22.3]
[482] 00:10:21.058 | Paris Saint-Germ | Carry           @ [51.4, 22.3]
[483] 00:10:22.603 | Clermont Foot    | Pressure        @ [62.7, 58.6] [CP=True]
[484] 00:10:24.319 | Paris Saint-Germ | Pass            -> Neymar da Si (Out) @ [74.0, 12.3]
[485] 00:10:26.508 | Paris Saint-Germ | Ball Receipt*   @ [81.5, 4.1]
[486] 00:10:33.935 | Clermont Foot    | Pass            -> Johan Gastie (Complete) @ [19.8, 80.0]
[487] 00:10:34.644 | Clermont Foot    | Ball Receipt*   @ [25.4, 71.4]
[488] 00:10:37.153 | Clermont Foot    | Pass            -> Jason Bertho (Complete) @ [31.0, 70.1]
[489] 00:10:38.180 | Clermont Foot    | Ball Receipt*   @ [32.1, 60.7]
[490] 00:10:38.180 | Clermont Foot    | Pass            -> Johan Gastie (Complete) @ [32.1, 60.7]
[491] 00:10:38.814 | Clermont Foot    | Ball Receipt*   @ [35.9, 66.0]
```

### Review Case 35: `3877115_p58_e75ec80b` [initiation_delay_over_5s]
- **Match**: 3877115 (Major League Soccer)
- **Teams**: Pressing: Toronto FC | Possessing: Toronto FC
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Ball Recovery (00:35:14.711) | **Initiation**: Pass (00:35:22.283)
- **Delay**: 7.572s (Quality: `invalid`, Latency Valid: `False`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `0` | 3-Class: `successful_regain`

```text
[1517] 00:35:18.745 | Inter Miami      | Pass            -> Lionel André (Complete) @ [46.2, 55.5]
[1518] 00:35:19.820 | Inter Miami      | Ball Receipt*   @ [57.4, 45.9]
[1519] 00:35:19.820 | Inter Miami      | Carry           @ [57.4, 45.9]
[1520] 00:35:21.266 | Inter Miami      | Pass            -> Josef Alexan (Incomplete) @ [57.2, 42.0]
[1521] 00:35:22.283 | Inter Miami      | Ball Receipt*   @ [73.5, 29.9]
[1522] 00:35:22.283 | Toronto FC       | Pass            -> Alonso Coell (Complete) @ [42.7, 45.4] [CP=True]
[1523] 00:35:24.706 | Toronto FC       | Ball Receipt*   @ [39.3, 27.1]
[1524] 00:35:24.706 | Toronto FC       | Carry           @ [39.3, 27.1]
[1525] 00:35:26.150 | Toronto FC       | Pass            -> Franco Ibarr (Complete) @ [36.2, 27.3]
[1526] 00:35:27.030 | Toronto FC       | Ball Receipt*   @ [43.3, 35.0]
[1527] 00:35:27.030 | Toronto FC       | Carry           @ [43.3, 35.0]
[1528] 00:35:27.070 | Toronto FC       | Pass            -> Michael Brad (Complete) @ [43.1, 34.6]
[1529] 00:35:29.396 | Toronto FC       | Ball Receipt*   @ [40.2, 19.8]
[1530] 00:35:29.396 | Toronto FC       | Carry           @ [40.2, 19.8]
```

### Review Case 36: `3998858_p130_97541a12` [regain_danger_overlap]
- **Match**: 3998858 (UEFA Women's Euro)
- **Teams**: Pressing: England Women's | Possessing: Wales W
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:24:10.700) | **Initiation**: Pressure (00:24:14.871)
- **Delay**: 4.171s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2724] 00:24:10.700 | England Women's  | Ball Receipt*   @ [47.2, 53.7]
[2725] 00:24:10.700 | Wales W          | Pass            -> Jessica Fish (Complete) @ [77.1, 23.8] [CP=True]
[2726] 00:24:11.538 | Wales W          | Ball Receipt*   @ [84.0, 32.7]
[2727] 00:24:11.538 | Wales W          | Carry           @ [84.0, 32.7]
[2728] 00:24:14.139 | Wales W          | Pass            -> Carrie Jones (Complete) @ [83.5, 34.8]
[2729] 00:24:14.871 | England Women's  | Pressure        @ [23.7, 31.8] [CP=True]
[2730] 00:24:14.908 | Wales W          | Ball Receipt*   @ [93.9, 48.1]
[2731] 00:24:14.908 | Wales W          | Carry           @ [93.9, 48.1]
[2732] 00:24:15.229 | Wales W          | Dribble         @ [95.1, 45.4]
[2733] 00:24:15.229 | England Women's  | Duel            @ [25.0, 34.7] [CP=True]
[2734] 00:24:17.592 | England Women's  | Pass            -> Bethany Mead (Complete) @ [31.2, 27.1]
[2735] 00:24:18.671 | England Women's  | Ball Receipt*   @ [27.4, 18.0]
[2736] 00:24:18.671 | England Women's  | Carry           @ [27.4, 18.0]
[2737] 00:24:19.072 | Wales W          | Pressure        @ [89.9, 62.9] [CP=True]
```

### Review Case 37: `3802805_p92_835a9886` [regain_danger_overlap]
- **Match**: 3802805 (Ligue 1)
- **Teams**: Pressing: OGC Nice | Possessing: Paris Saint-Germain
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:40:26.550) | **Initiation**: Pressure (00:40:28.264)
- **Delay**: 1.714s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2157] 00:40:26.238 | OGC Nice         | Pressure        @ [48.6, 48.1] [CP=True]
[2158] 00:40:26.550 | Paris Saint-Germ | Pass            -> Lionel André (Complete) @ [71.5, 32.4]
[2159] 00:40:27.047 | Paris Saint-Germ | Ball Receipt*   @ [76.9, 36.1]
[2160] 00:40:27.047 | Paris Saint-Germ | Carry           @ [76.9, 36.1]
[2161] 00:40:27.179 | Paris Saint-Germ | Pass            -> Marco Verrat (Complete) @ [75.8, 34.4]
[2162] 00:40:28.264 | OGC Nice         | Pressure        @ [43.5, 57.5] [CP=True]
[2163] 00:40:28.266 | Paris Saint-Germ | Ball Receipt*   @ [76.6, 22.6]
[2164] 00:40:28.266 | Paris Saint-Germ | Carry           @ [76.6, 22.6]
[2165] 00:40:28.777 | Paris Saint-Germ | Pass            -> Lionel André (Complete) @ [76.6, 22.6]
[2166] 00:40:29.384 | Paris Saint-Germ | Ball Receipt*   @ [79.2, 27.5]
[2167] 00:40:29.384 | Paris Saint-Germ | Carry           @ [79.2, 27.5]
[2168] 00:40:30.058 | Paris Saint-Germ | Pass            -> Neymar da Si (Incomplete) @ [81.3, 24.7]
[2169] 00:40:30.326 | Paris Saint-Germ | Ball Receipt*   @ [93.1, 22.0]
[2170] 00:40:30.326 | OGC Nice         | Block           @ [34.3, 57.5] [CP=True]
```

### Review Case 38: `3893819_p175_a0c43844` [regain_danger_overlap]
- **Match**: 3893819 (Women's World Cup)
- **Teams**: Pressing: Korea Republic Women's | Possessing: Morocco Women's
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:26:44.087) | **Initiation**: Dribbled Past (00:26:48.805)
- **Delay**: 4.718s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[2532] 00:26:42.751 | Morocco Women's  | Pressure        @ [64.0, 30.3]
[2533] 00:26:44.010 | Korea Republic W | Pressure        @ [53.3, 43.1]
[2534] 00:26:44.087 | Morocco Women's  | Pass            -> Ibtissam Jra (Complete) @ [66.8, 37.0]
[2535] 00:26:45.565 | Morocco Women's  | Ball Receipt*   @ [74.5, 23.9]
[2536] 00:26:45.565 | Morocco Women's  | Carry           @ [74.5, 23.9]
[2537] 00:26:48.805 | Korea Republic W | Dribbled Past   @ [30.9, 50.0] [CP=True]
[2538] 00:26:48.805 | Morocco Women's  | Dribble         @ [89.2, 30.1]
[2539] 00:26:48.805 | Morocco Women's  | Carry           @ [89.2, 30.1]
[2540] 00:26:50.914 | Morocco Women's  | Pass            (Incomplete) @ [92.2, 38.9]
[2541] 00:26:51.059 | Korea Republic W | Block           @ [26.8, 39.5]
[2542] 00:26:53.490 | Korea Republic W | Ball Recovery   @ [35.6, 43.6]
[2543] 00:26:53.490 | Korea Republic W | Carry           @ [35.6, 43.6]
[2544] 00:26:53.572 | Morocco Women's  | Pressure        @ [81.1, 33.5] [CP=True]
[2545] 00:26:57.239 | Morocco Women's  | Foul Committed  @ [71.9, 21.1] [CP=True]
```

### Review Case 39: `3788754_p52_796d3382` [regain_danger_overlap]
- **Match**: 3788754 (UEFA Euro)
- **Teams**: Pressing: Switzerland | Possessing: Italy
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Pass (00:32:21.854) | **Initiation**: Pressure (00:32:25.722)
- **Delay**: 3.868s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[1401] 00:32:21.854 | Italy            | Pass            -> Ciro Immobil (Complete) @ [48.3, 14.6]
[1402] 00:32:23.346 | Italy            | Ball Receipt*   @ [71.9, 10.1]
[1403] 00:32:23.346 | Italy            | Pass            -> Lorenzo Insi (Complete) @ [71.9, 10.1]
[1404] 00:32:24.979 | Italy            | Ball Receipt*   @ [77.7, 3.3]
[1405] 00:32:24.979 | Italy            | Carry           @ [77.7, 3.3]
[1406] 00:32:25.722 | Switzerland      | Pressure        @ [36.3, 76.0] [CP=True]
[1407] 00:32:25.887 | Italy            | Dispossessed    @ [83.3, 2.6]
[1408] 00:32:25.887 | Switzerland      | Duel            @ [36.8, 77.5] [CP=True]
[1409] 00:32:27.029 | Italy            | Pressure        @ [74.3, 3.6] [CP=True]
[1410] 00:32:27.691 | Switzerland      | Pass            (Incomplete) @ [45.2, 77.0]
[1411] 00:32:27.756 | Italy            | Block           @ [73.4, 3.3] [CP=True]
[1412] 00:32:36.504 | Switzerland      | Pass            -> Fabian Lukas (Complete) @ [55.8, 80.0]
[1413] 00:32:39.442 | Switzerland      | Ball Receipt*   @ [26.8, 59.6]
[1414] 00:32:39.442 | Switzerland      | Carry           @ [26.8, 59.6]
```

### Review Case 40: `3895180_p19_f72281df` [regain_danger_overlap]
- **Match**: 3895180 (1. Bundesliga)
- **Teams**: Pressing: Bayer Leverkusen | Possessing: Eintracht Frankfurt
- **Turnover Context**: open_play (Origin: Regular Play)
- **Turnover**: Interception (00:05:21.317) | **Initiation**: Pressure (00:05:23.464)
- **Delay**: 2.147s (Quality: `high`, Latency Valid: `True`)
- **Algorithm Labels**: Regain 5s: `1` | Danger 15s: `1` | 3-Class: `dangerous_escape`

```text
[270] 00:05:17.431 | Bayer Leverkusen | Carry           @ [41.1, 23.1]
[271] 00:05:20.721 | Bayer Leverkusen | Pass            -> Jonas Hofman (Incomplete) @ [34.3, 33.7]
[272] 00:05:21.317 | Bayer Leverkusen | Ball Receipt*   @ [55.0, 53.1]
[273] 00:05:21.317 | Eintracht Frankf | Interception    @ [70.6, 30.2] [CP=True]
[274] 00:05:21.317 | Eintracht Frankf | Carry           @ [70.6, 30.2]
[275] 00:05:23.464 | Bayer Leverkusen | Pressure        @ [41.1, 49.3] [CP=True]
[276] 00:05:24.144 | Eintracht Frankf | Pass            -> Fares Chaïbi (Complete) @ [79.4, 28.3]
[277] 00:05:24.754 | Eintracht Frankf | Ball Receipt*   @ [87.5, 30.8]
[278] 00:05:24.754 | Eintracht Frankf | Carry           @ [87.5, 30.8]
[279] 00:05:24.802 | Eintracht Frankf | Pass            -> Ansgar Knauf (Complete) @ [87.0, 31.2]
[280] 00:05:25.272 | Eintracht Frankf | Ball Receipt*   @ [79.4, 31.4]
[281] 00:05:25.272 | Eintracht Frankf | Carry           @ [79.4, 31.4]
[282] 00:05:25.696 | Eintracht Frankf | Miscontrol      @ [79.4, 31.2]
[283] 00:05:26.334 | Eintracht Frankf | Pressure        @ [82.0, 29.1]
```
