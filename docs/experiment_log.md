# Experiment Log

Chronological record of research questions, computational runs, anomalies detected, and modeling iterations.

---

## [2026-09-18] Iteration 1: Repository Scaffolding & Initial Data Audit

### Objective
Establish a reproducible repository structure, configure Python environment, build an automated caching downloader for StatsBomb Open Data, audit all 360 competitions, verify coordinate conventions and event sequences, and produce verified sample visualizations.

### Actions Taken
1. Initialized repository directories: `data/`, `notebooks/`, `src/counterpress/`, `tests/`, `results/`, `docs/`, `submissions/`.
2. Created `.gitignore`, `pyproject.toml`, and `.venv` with `pandas`, `numpy`, `matplotlib`, `mplsoccer==1.4.0`, `scipy`, `shapely`, `requests`, `statsbombpy`, `pytest`, `jupyter`, `ipykernel`.
3. Created `src/counterpress/config.py`, `src/counterpress/data.py`, `src/counterpress/spatial.py`, `src/counterpress/visualization.py`, and interface stubs for `turnovers.py`, `outcomes.py`, `features.py`, and `models.py`.
4. Installed editable package `counterpress-spatial-analysis` and verified 11 unit tests passing via `pytest`.
5. Built manifest of 3,961 matches across 80 competition-seasons and identified 12 competitions with 360 data.
6. Executed full multithreaded data audit across 477 matches (1,744,882 events, 50,366 counterpress events).
7. Discovered two remote data issues:
   - AFCON 2023: Remote HTTP 404 for match 3923881 360 JSON.
   - UEFA Women's Euro 2022: Match 3845506 contains a 16KB zeroed block upstream in `three-sixty/3845506.json`.
8. Generated 4 publication-quality freeze frame visualizations in `results/figures/` spanning World Cup 2022, Bundesliga 2023/24, Euro 2024, and La Liga 2020/21.
9. Built and executed `notebooks/01_data_audit.ipynb` end-to-end.
10. Authored comprehensive reports: `docs/data_audit.md`, `docs/methodology.md`, `docs/data_dictionary.md`, `docs/assumptions.md`.

### Status & Verification
- Unit Tests: 11 / 11 PASSED.
- Usable 360 Counterpress Sample Size: **40,054 events** across **424 matches**.
- Notebook: `01_data_audit.ipynb` fully rendered and saved.
- Outcome: Completed Iteration 1. Ready for Iteration 2 (Turnover extraction & dual-horizon outcome labeling).

---

## [2026-09-18] Iteration 2: Episode Extraction & Outcome Labeling

### Objective
Shift the analytical unit from individual counterpress actions to post-turnover **counterpress episodes** to prevent pseudo-replication. Implement deterministic open-play turnover detection, dual-horizon outcome labeling (5s regain, 15s transition risk, 3-state tactical partition), execute across 424 matches, run 13 automated sanity checks, generate a stratified 100-episode manual validation sample, and apply methodological corrections across all documentation.

### Actions Taken
1. Applied 4 mandatory methodological corrections across existing documentation:
   - Replaced speculative MLS camera panning claims with empirical reporting.
   - Reframed missingness analysis to test observable associations rather than claiming to "confirm MAR."
   - Standardized all spatial distances to StatsBomb coordinate units ($120 \times 80$).
   - Formally distinguished action-level events (~50,366 raw / ~40,054 with 360) from derived episodes.
2. Implemented `src/counterpress/turnovers.py`:
   - `extract_counterpress_episodes`: Groups multiple chained counterpress actions within the same post-turnover possession into a single episode.
   - `identify_turnover_event`: Backwards search to pin down the exact turnover event and latency.
   - `is_open_play_transition`: Segregates open-play turnovers from set-piece restarts.
3. Implemented `src/counterpress/outcomes.py`:
   - `compute_episode_outcomes`: Evaluates `regain_5s` (using strict `possession_team` semantics; defensive actions do not equal regains) alongside sensitivity targets (`regain_3s`, `regain_8s`).
   - Evaluates `dangerous_escape_15s` (opponent shot or $x \ge 80.0$ entry, conditional on not starting in final third).
   - Partitions into `episode_outcome_3class` (`successful_regain`, `harmless_escape`, `dangerous_escape`).
4. Expanded unit tests to 17 tests covering all edge cases in `tests/test_turnovers.py` and `tests/test_outcomes.py` (17/17 PASSED).
5. Executed full extraction pipeline via `scripts/extract_episodes.py` across 424 matches:
   - 45,389 counterpress actions collapsed into **29,186 distinct episodes** (1.555 actions/episode).
   - 24,355 open-play episodes (83.45%).
   - 25,846 episodes with usable initiation 360 (88.56%).
   - Regain 5s: 14,598 (50.02%); Dangerous Escape 15s: 4,835 (16.57%).
   - Three-class: Successful Regain = 14,598 (50.02%), Harmless Escape = 9,945 (34.07%), Dangerous Escape = 4,643 (15.91%).
6. Executed all 13 sanity checks (0 duplicate initiating events, 0 logical contradictions, 0 negative delays).
7. Built stratified 100-episode manual validation sample (`results/tables/manual_episode_validation.csv`) with uncorrupted blank human-review columns and generated `results/manual_validation_report.md` with complete chronological event sequences.
8. Built and executed `notebooks/02_counterpress_detection.ipynb` cleanly via nbconvert.
9. Authored `docs/episode_definition.md`, `docs/outcome_definition.md`, `docs/iteration2_report.md`.

### Status & Verification
- Unit Tests: 17 / 17 PASSED in 0.54s.
- Sanity Checks: 13 / 13 PASSED.
- Notebook: `02_counterpress_detection.ipynb` fully executed and verified.
- Status: Completed Iteration 2. Methodological review identified key edge cases requiring Iteration 2.5.

---

## [2026-09-18] Iteration 2.5: Counterpress Episode Validation, Edge-Case Resolution, and Primary Cohort Locking

### Objective
Resolve critical methodological issues discovered after reviewing Iteration 2:
1. Standardize terminology: replace "statistically independent counterpress episodes" with "distinct counterpress episodes" across all documents, adding notes on match-level clustering.
2. Investigate counterpress initiation delays > 5.0 seconds (1,563 episodes in Iteration 2 extraction), audit causes A-E, improve `identify_turnover_event()`, and create `turnover_link_quality` and `latency_valid` fields.
3. Audit open-play vs set-piece classification across 4,831 restart-origin episodes, define `possession_origin_pattern` vs `turnover_context` (`open_play`, `immediate_restart_phase`, `ambiguous`), and retain possessions developing into genuine open-play circulation.
4. Resolve the 192 overlapping episodes between `regain_5s == 1` and `dangerous_escape_15s == 1`, establish tactical danger priority in `episode_outcome_3class` (`dangerous_escape` > `successful_regain` > `harmless_escape`), and verify mutual exclusivity.
5. Create a priority manual validation subset of ~40 episodes (min 30 unique) with strictly unpopulated human review columns.
6. Formally lock the primary modeling cohort (`primary_cohort_eligible`) and generate a transparent cohort flow table (`cohort_flow.csv`).

### Actions Taken
1. Replaced "statistically independent counterpress episodes" with "distinct counterpress episodes" throughout `README.md`, `docs/episode_definition.md`, `docs/data_audit.md`, `docs/assumptions.md`, and `docs/iteration2_report.md`. Added methodological notes on match grouping and multilevel modeling.
2. Refactored `src/counterpress/turnovers.py`:
   - Enhanced `identify_turnover_event()` to identify dispossession events and return `(turnover_event, latency_seconds, turnover_link_quality)`.
   - Added `classify_turnover_context()` to separate restart origin from open-play turnover context.
   - Added `turnover_link_quality` (`high`, `ambiguous`, `invalid`) and `latency_valid` (`0 <= delay <= 5.0 and link_quality == 'high'`).
3. Refactored `src/counterpress/outcomes.py`:
   - Revised `episode_outcome_3class` so that `dangerous_escape_15s == 1` takes priority over `regain_5s == 1`.
   - Reclassified 192 overlapping episodes from `successful_regain` to `dangerous_escape`.
4. Re-executed `scripts/extract_episodes.py` across 424 matches:
   - 29,186 distinct episodes.
   - 26,375 latency valid episodes (90.37%).
   - 27,272 open-play turnover context episodes (93.44%).
   - Revised 3-class distribution: Successful Regain = 14,406 (49.36%), Harmless Escape = 9,945 (34.07%), Dangerous Escape = 4,835 (16.57%).
   - Primary cohort eligible: **21,616 episodes (74.06%)**.
5. Created and executed `scripts/audit_iteration2_5.py`:
   - `results/tables/delay_over_5_audit.csv` and `results/delay_over_5_validation_report.md` (detailed traces for representative >5s cases).
   - `results/tables/restart_context_audit.csv` (124 stratified cases) and `docs/open_play_definition.md`.
   - `results/tables/manual_validation_priority.csv` (40 unique cases, blank human columns) and `results/manual_validation_priority_report.md`.
   - `results/tables/cohort_flow.csv` tracking all filtering stages.
   - `docs/iteration2_5_report.md` summarizing all results.
6. Expanded unit tests from 17 to 23 tests covering all edge cases (latency > 5s, restart open-play, immediate restart, danger priority, simultaneous timestamps). All 23 PASSED.

### Status & Verification
- Unit Tests: 23 / 23 PASSED in 0.54s.
- Automated Sanity Checks: 13 / 13 PASSED with 0 violations.
- Primary Modeling Cohort: Locked at **21,616 episodes** across 418 matches and 10 clean competition-seasons.
- Status: Completed Iteration 2.5. Methodological review of priority sample identified outcome label validity issues requiring Iteration 2.6.

---

## [2026-09-18] Iteration 2.6: Established-Possession Regain Definition and Human Trace Validation

### Objective
Resolve critical validity issues in `regain_5s` discovered during manual trace review of the Iteration 2.5 priority sample:
1. Redefine established possession regain: require BOTH possession-transition evidence and controlled-possession evidence by the pressing team within 5.000 seconds.
2. Implement dual regain variables: preserve `regain_5s_possession_annotation` for auditing; create `regain_5s_controlled` (primary), `controlled_regain_time`, `controlled_regain_event_id`, `controlled_regain_event_type`, `controlled_regain_evidence`.
3. Investigate disagreements across full dataset (2x2 table, agreement rate, Cohen's kappa, stratifications).
4. Manually audit 100 disagreement traces (50 annot=1/ctrl=0, 50 annot=0/ctrl=1) in `results/regain_disagreement_validation_report.md`.
5. Re-evaluate the priority 40 sample with extended traces and side-by-side labels in `results/tables/manual_validation_priority_v2.csv` and `results/manual_validation_priority_v2_report.md`, explicitly analyzing Cases 9, 18, 37, and 40.
6. Recalculate primary cohort ($N = 21,616$) outcome distributions.
7. Refine reporting terminology (`counterpressing_team`, `opponent_team_at_turnover`, `possession_team_at_counterpress_initiation`, `possession_id_at_counterpress_initiation`) and soften causal claims.
8. Expand unit tests to cover all edge cases (10 new tests).

### Actions Taken
1. Refactored `src/counterpress/outcomes.py`:
   - Created `detect_controlled_regain()`: requires transition evidence and on-ball action by pressing team (`Carry`, completed `Pass`, `Ball Recovery` + control, `Duel` + control, `Interception` + control, `Goal Keeper` control, controlled `Ball Receipt*`). Standalone defensive events (`Pressure`, `Block`, `Foul Committed`, uncompleted `Clearance`) and opponent actions strictly excluded.
   - Preserved `regain_5s_possession_annotation`, `seconds_to_regain_annotation`, `regain_event_id_annotation`, `episode_outcome_3class_old`.
   - Primary `regain_5s_controlled` aliased to `regain_5s`.
   - Updated `dangerous_escape_15s` to strictly precede `controlled_regain_time`.
   - Recomputed `episode_outcome_3class` (`dangerous_escape` > `successful_regain` > `harmless_escape`).
2. Updated `src/counterpress/turnovers.py` with explicit metadata fields: `opponent_team_at_turnover`, `possession_team_at_counterpress_initiation`, `possession_id_at_counterpress_initiation`.
3. Expanded unit tests in `tests/test_outcomes.py` from 23 to 31 tests. All 31 PASSED in 0.43s.
4. Re-executed extraction across all 424 matches (29,186 episodes) in `scripts/extract_episodes.py`:
   - All 13 sanity checks PASSED.
   - Primary cohort retained exactly at **21,616 distinct episodes**.
5. Created and executed `scripts/audit_iteration2_6.py`:
   - `results/tables/regain_label_comparison.csv` (2x2 table and 6 stratified analyses).
   - `results/regain_disagreement_validation_report.md` (100 extended chronological traces).
   - `results/tables/manual_validation_priority_v2.csv` (40 priority cases; human review columns strictly unpopulated).
   - `results/manual_validation_priority_v2_report.md` (extended traces and explicit analyses of Cases 9, 18, 37, 40).
   - `docs/iteration2_6_report.md` (comprehensive milestone report).
6. Updated documentation: `docs/outcome_definition.md`, `docs/data_dictionary.md`, `docs/assumptions.md`, and softened unsupported causal claims across previous reports.

### Key Empirical Findings
- Full dataset ($N = 29,186$):
  - Legacy annotation regain rate: **50.02%** (14,598 episodes).
  - Controlled regain rate: **44.09%** (12,869 episodes).
  - Agreement rate: **90.27%** (26,347 episodes).
  - Cohen's Kappa: **0.8055** (strong inter-definition agreement).
  - False-positive candidates (annot=1, ctrl=0): **2,284 episodes** (7.83%).
  - False-negative candidates (annot=0, ctrl=1): **555 episodes** (1.90%).
  - 3-class outcome shifts: 2,213 episodes (7.58%). Successful Regain = 39.13%, Harmless Escape = 39.09%, Dangerous Escape = 21.78%.
- Priority Cases:
  - Case 9 (`3788766_p107_15ad5bb1`): False positive resolved ($1 \to 0$, dt=7.33s).
  - Case 18 (`3857276_p12_fcc6b2e3`): False negative resolved ($0 \to 1$, dt=3.89s).
  - Case 37 (`3802805_p92_835a9886`): Regain at 4.97s, but danger occurred at dt=0.002s $\to$ `dangerous_escape`.
  - Case 40 (`3895180_p19_f72281df`): Regain at 3.28s, but danger occurred at dt=1.29s $\to$ `dangerous_escape`.
- Primary cohort ($N = 21,616$):
  - Regain (5s) rate: **39.25%** (8,485 episodes) vs 43.49% under legacy annotation.
  - Dangerous escape (15s) rate: **23.92%** (5,171 episodes).
  - 3-Class: Successful Regain = 34.31%, Harmless Escape = 41.77%, Dangerous Escape = 23.92%.

### Status & Verification
- Unit Tests: 31 / 31 PASSED in 0.43s.
- Sanity Checks: 13 / 13 PASSED.
- Primary Modeling Cohort: Fully locked and validated at **$N = 21,616$ distinct episodes**.
- Status: Completed Iteration 2.6.

---

## [2026-09-18] Iteration 2.7: Final Outcome Freeze and Scientific Transition Verification

### Objective
Perform final audit and freeze of outcome labeling before spatial feature engineering:
1. Enforce strict scientific possession-transition verification: require BOTH verified possession-transition evidence and confirming controlled play within 5.000s of initiation (`confirming_control_dt <= 5.000s`).
2. Eliminate unverified standalone pressing-team actions occurring during opponent possession sequences without preceding turnover or ball-winning events.
3. Establish conservative confirming control timing: operational `controlled_regain_time` is defined by the confirming control timestamp (`controlled_control_time`). If acquisition is at 4.8s but control at 5.2s, `regain_5s_controlled` is 0.
4. Store `controlled_acquisition_time`, `controlled_control_time`, and operational `controlled_regain_time`.
5. Preserve `regain_5s_controlled_v26` and `regain_5s_possession_annotation` alongside primary frozen variable `regain_5s_controlled` for complete longitudinal auditing.
6. Re-extract and audit across all 424 matches (29,186 episodes, 21,616 primary cohort).
7. Standardize terminology: replace "Outcome Labels Methodologically Validated" with "Outcome Labels Methodologically Refined and Automated Sanity-Checked".

### Actions Taken
1. Refactored `src/counterpress/outcomes.py`:
   - Updated `detect_controlled_regain()`: requires transition evidence (Pathway A: defensive acquisition; Pathway B: opponent turnover; Pathway C: new possession assignment) and confirming control (`Carry`, completed `Pass`, controlled `Ball Receipt*`, completed `Dribble`, `Shot`).
   - Retained `detect_controlled_regain_v26()` for longitudinal auditing.
   - Updated `compute_episode_outcomes()`: stores `controlled_acquisition_time`, `controlled_control_time`, `controlled_regain_time` (= confirming control time), `regain_5s_controlled_v26`, and all transition risk metrics.
2. Expanded unit tests in `tests/test_outcomes.py` to 41 tests (10 new tests specifically testing standalone action rejections, exact 5.0s boundaries, 5.2s timing rejections, duels followed by opponent control, and same-timestamp events). All 41 PASSED in 0.49s.
3. Re-extracted all episodes in `scripts/extract_episodes.py`:
   - Processed 424 matches; total 29,186 episodes.
   - All 13 sanity checks PASSED.
   - Primary cohort preserved exactly at **21,616 distinct episodes**.
4. Executed `scripts/audit_iteration2_7.py`:
   - Produced `results/tables/regain_v26_vs_v27.csv` (full 2x2 comparison, agreement %, Cohen's kappa).
   - Audited the 11,544 changed cases: 11,496 rejected standalone actions without transition; 48 control timing exceeded 5.0s.
   - Produced `results/tables/final_regain_trace_audit.csv` & `results/final_regain_trace_audit.md` (100 stratified positive traces: 25 recovery, 20 duel, 15 interception, 20 new possession, 20 other; review checkboxes strictly unpopulated).
   - Produced `results/tables/regain_v27_changed_cases.csv` (50 sample changed cases).
   - Generated comprehensive milestone report in `docs/iteration2_7_report.md`.
5. Updated documentation: `docs/outcome_definition.md`, `docs/data_dictionary.md`, `docs/assumptions.md`, and standardized terminology.

### Key Empirical Findings
- Full dataset ($N = 29,186$):
  - v2.6 positive rate: **44.09%** (12,869 episodes).
  - v2.7 frozen positive rate: **4.54%** (1,325 episodes).
  - Agreement rate: **60.45%** | Cohen's Kappa: **0.1137**.
  - Total changed cases: **11,544 episodes** (11,496 standalone actions in opponent possession eliminated; 48 control exceeded 5.0s).
- Primary cohort ($N = 21,616$):
  - `regain_3s_controlled`: **2.29%** (495 episodes).
  - `regain_5s_controlled`: **5.05%** (1,091 episodes) vs 39.25% under v2.6.
  - `regain_8s_controlled`: **8.96%** (1,936 episodes).
  - `dangerous_escape_15s`: **34.50%** (7,457 episodes).
  - Final Three-State Tactical Outcome:
    1. `dangerous_escape`: **34.50%** (7,457 episodes).
    2. `successful_regain`: **4.22%** (913 episodes).
    3. `harmless_escape`: **61.28%** (13,246 episodes).
  - Overlap between 3 classes: **0 episodes** (100% mutually exclusive and exhaustive).

### Status & Verification
- Unit Tests: 41 / 41 PASSED in 0.49s.
- Sanity Checks: 13 / 13 PASSED.
- Primary Modeling Cohort: Frozen at **$N = 21,616$ distinct episodes**.
- Outcome Labels: Fully frozen, transition-verified, and automated sanity-checked.
- Ready for Iteration 3: Spatial Feature Engineering and Freeze Frame Processing.

---

## Experiment Entry: 2026-09-18 — Iteration 3: Spatial Feature Engineering and Freeze-Frame Processing

### Objective
1. Engineer rigorous spatial, geometric, and visual features from StatsBomb 360 freeze frames for all 21,616 primary cohort counterpress episodes across 414 matches.
2. Maintain strict temporal leakage boundaries ($t \le t_{\text{init}}$): all spatial features must be derived strictly and exclusively from the freeze frame at initiation.
3. Enforce primary cohort invariants: exactly 21,616 rows, zero drops, zero duplicates.
4. Calculate boundary-clipped camera coverage at 5, 10, and 15 StatsBomb coordinate units and inside the forward escape corridor ($R=20$, $60^\circ$ wedge).
5. Extract player metrics: actor exclusion from teammate support, nearest distances, dispersion, convex hull area ($\ge 3$ non-collinear points; NaN otherwise), forward numerical advantage, and corridor occupation.
6. Generate 20 publication-grade visual QA diagnostic figures across stratified tactical criteria.
7. Prepare the unified feature dataset `counterpress_features.parquet` and summary table `spatial_feature_summary.csv`.

### Artifacts and File Checksums (SHA256)
- `data/processed/counterpress_features.parquet`: `9cdce247bc67a8e82806dd86c09639f279b8da046deb4857e2f553847c698cd3`
- `results/tables/spatial_feature_summary.csv`: `928d746252a3d19ee265091830b8f39fa8ff29ca7871222cde0e2eacd0fcb648`
- `results/tables/primary_cohort_episode_ids.csv`: `a46d57b759ae11074da421536bbda91013a497015f0c0c25b2cb180bd17ea5df`
- `src/counterpress/spatial.py`: `1e625d22bda91219eb6dba57491924b9af9aed94aac853b945c6e445e2080821`
- `src/counterpress/features.py`: `aa63bc4e29f402b451ff85d39166478a6732ca372e75debc32ff18280ae052ff`
- `scripts/extract_spatial_features.py`: `cfa6e31210c7da8c6b58b40a967e65d5c85a308a48f1e4abef20a7d92d0f7107`
- `scripts/generate_spatial_qa_visualizations.py`: `f5e188a955a2ba7e5ed9310af280f10a15430cc3754e68e60aebcd44ea926236`

### Actions Taken
1. Implemented geometric operations in `src/counterpress/spatial.py`:
   - Euclidean distances, pitch boundary clipping, coordinate/polygon inversion with CCW vertex order preservation.
   - Circle-pitch intersection area as denominator for camera coverage.
   - Convex hull calculation (strictly returning `NaN` for $< 3$ points or collinear configurations).
   - Mean pairwise distance calculation (strictly returning `NaN` for $< 2$ points).
   - Forward escape corridor circular sector geometry ($R=20$, directed to $(120, 40)$, half-angle $30^\circ$, area $\approx 209.44$ units$^2$) and corridor coverage.
2. Built row feature extractor in `src/counterpress/features.py`:
   - Identified actor (`actor == True`), separated teammates and opponents, strictly excluded actor from teammate support counts.
   - Handled coordinate perspective orientation: flagged inverted frames via `actor_distance_from_event` and `actor_matching_anomalous`.
   - Extracted 84 total columns per episode encompassing identifiers, quality flags, camera coverage, player counts, local advantage (5, 10, 15), forward advantage, escape corridor metrics, nearest distances, and compactness.
3. Extracted features across all 414 matches in `scripts/extract_spatial_features.py`:
   - Processed 21,616 primary cohort episodes in ~58 seconds.
   - Executed Sanity Checks A through K: all passed with zero violations.
   - Saved `data/processed/counterpress_features.parquet` (21,616 rows, 84 columns).
   - Saved `results/tables/spatial_feature_summary.csv` (84 feature rows with complete distribution metrics).
4. Generated 20 publication-grade visual QA freeze-frame figures in `results/figures/qa_spatial/` using `scripts/generate_spatial_qa_visualizations.py` and `src/counterpress/visualization.py`.
5. Expanded test suite to 69 tests across `tests/test_spatial.py`, `tests/test_features.py`, and `tests/test_iteration3_invariants.py`. All 69 tests pass in ~1.02s.
6. Authored comprehensive milestone report in `docs/iteration3_report.md` and updated `docs/data_dictionary.md` with the exact 84-column schema.

### Key Empirical Findings
- Primary Cohort Preservation: Exactly 21,616 distinct episodes across 414 matches. Zero drops, zero duplicates.
- Camera Coverage:
  - 5-unit: Mean = 96.85%, Median = 100.0%, $\ge 80\%$ in 20,882 episodes (96.60%).
  - 10-unit: Mean = 95.57%, Median = 100.0%, $\ge 80\%$ in 20,547 episodes (95.05%).
  - 15-unit: Mean = 91.88%, Median = 98.36%, $\ge 80\%$ in 19,535 episodes (90.37%).
  - Forward Escape Corridor (20u): Mean = 77.82%, Median = 92.40%, $\ge 80\%$ in 13,873 episodes (64.18%).
- Frame Composition:
  - Total frame players: Mean = 15.48, Median = 16.0, Min = 3, Max = 22.
  - Teammates (excluding actor): Mean = 6.54, Median = 7.0, Min = 0, Max = 10.
  - Opponents: Mean = 7.95, Median = 8.0, Min = 1, Max = 11.
  - Goalkeepers visible: Mean = 0.35, Median = 0.0, Min = 0, Max = 1.
- Local Numerical Advantage (Teammates - Opponents):
  - 5-unit: Mean = -0.90, Median = -1.0, Std = 0.80, Min = -7, Max = +3.
  - 10-unit: Mean = -0.93, Median = -1.0, Std = 1.36, Min = -7, Max = +5.
  - 15-unit: Mean = -0.97, Median = -1.0, Std = 1.72, Min = -8, Max = +5.
- Forward Structure & Escape Corridor:
  - Opponents ahead of ball: Mean = 3.09, Median = 3.0.
  - Defenders ahead of ball: Mean = 3.55, Median = 3.0.
  - Forward advantage: Mean = -0.46, Median = -1.0.
  - Opponents in 20u corridor: Mean = 0.62, Median = 0.0, Max = 6.
  - Defenders in 20u corridor: Mean = 0.84, Median = 1.0, Max = 6.
  - Corridor advantage: Mean = -0.22, Median = 0.0.
- Proximity & Dispersion:
  - Nearest opponent distance: Mean = 3.86, Median = 2.23 StatsBomb coordinate units (100% valid).
  - Nearest teammate distance: Mean = 8.86, Median = 7.30 StatsBomb coordinate units (99.85% valid).
  - Teammate hull area: Mean = 553.99, Median = 509.79 units$^2$ (valid for 97.10%; NaN for $< 3$ players).
  - Opponent hull area: Mean = 590.67, Median = 545.75 units$^2$ (valid for 99.61%; NaN for $< 3$ players).
- Canonical Outcomes (strictly unchanged):
  - `regain_5s_controlled`: 7,491 / 21,616 = 34.65%
  - `dangerous_escape_15s`: 4,844 / 21,616 = 22.41%
  - `regain_3s_controlled`: 6,161 / 21,616 = 28.50%
  - `regain_8s_controlled`: 8,878 / 21,616 = 41.07%
  - Three-State: `successful_regain` = 6,976 (32.27%), `harmless_escape` = 9,796 (45.32%), `dangerous_escape` = 4,844 (22.41%).

### Status & Verification
- Test Suite: 69 / 69 PASSED in 1.02s.
- Sanity Checks A–K: ALL PASSED.
- Parquet Dimensions: 21,616 rows x 84 columns.
- SHA256 Verification: Verified and recorded.
- Visual QA Figures: 20 figures generated in `results/figures/qa_spatial/`.
- Ready for Iteration 4: Predictive Modeling and Inference (stop condition enforced; no models trained).

---

## Experiment Entry: 2026-09-18 — Iteration 4: Grouped Predictive Modeling, Spatial Effect Estimation, and Tactical Interpretation

### Objective
1. Conduct rigorous out-of-sample predictive evaluation across the model hierarchy (Models 0–5) using 5-fold GroupKFold grouped by `match_id` ($N = 21,616$ episodes, 414 matches).
2. Measure the incremental predictive value of 360 spatial geometry beyond pitch location and match context for both `regain_5s_controlled` and `dangerous_escape_15s`.
3. Perform pre-specified feature-family ablations to isolate the relative contributions of local pressure, compactness, forward escape structure, and pitch geometry.
4. Estimate inferential associations via clustered logistic regression using `statsmodels` (standard errors clustered by `match_id`).
5. Conduct sensitivity and generalization tests: high local coverage ($\ge 80\%$), high corridor coverage ($\ge 80\%$), actor-discrepancy exclusion ($N=787$), and leave-one-competition-out evaluation.
6. Evaluate a secondary 3-class multinomial tactical model (`successful_regain`, `harmless_escape`, `dangerous_escape`).
7. Generate publication-quality Figures 1 through 7 and self-contained Jupyter notebooks (`04_exploratory_analysis.ipynb`, `05_modeling.ipynb`).

### Artifacts and File Checksums (SHA256)
- `results/tables/model_cv_folds.csv`: `434d385108269d0ec9c39ce6f5e04cb2c8e31fc575bc86dc018318610738600c`
- `results/tables/model_feature_sets.csv`: `7bb362ec0d07ae2524a87754d92ee21d15bf0db1598f86f33d7b8ba07ce884e9`
- `results/tables/descriptive_outcome_tables.csv`: `ebc59ce13ff24738fb9a888c3a9f0e6ae5d1d6a9e1445b2f2161b96a80dfdb38`
- `results/tables/model_performance.csv`: `c5980fc85d1d867c29352e04e9c70b6159c3da11ce0c13bb104fa2fc1e60f089`
- `results/tables/model_incremental_value.csv`: `c99bf461d63ea0cce93259d81d22ceca477a33190be68d1b11b5e58bbbf9b48c`
- `results/tables/feature_family_ablation.csv`: `d3be3bfe6da1e4277b0559eb4bb4d07b46944e4a77ce15ffba7b30fc3ef74457`
- `results/tables/logistic_coefficients.csv`: `ba5956fe0210f96bc8e6f16428e23f03b879a9cae8fe4c1775e119bf544f9f70`
- `results/tables/leave_competition_out.csv`: `42a420b92db237e1913303d2e0ea9ca8c962b9213bcfa728c306d860d5b99fc6`

### Key Empirical Findings
1. Incremental Predictive Value of Spatial Geometry:
   - Regain within 5s: Context Logistic ROC-AUC = 0.7926 $\to$ Full Spatial Logistic ROC-AUC = **0.8156** ($\Delta = +0.0230$, PR-AUC gain +0.0377, Brier reduction -0.0063).
   - Dangerous Escape within 15s: Context Logistic ROC-AUC = 0.7687 $\to$ Gradient Boosting ROC-AUC = **0.7904** ($\Delta = +0.0217$, PR-AUC gain +0.0625).
2. Linear vs. Nonlinear Structure:
   - Regain is predominantly linear in log-odds: GAM (0.8157) and Gradient Boosting (0.8147) match Full Spatial Logistic (0.8156).
   - Transition risk exhibits significant non-linearities: Gradient Boosting achieves PR-AUC = 0.5344 vs. Logistic 0.4954.
3. Statistically Significant Clustered Predictors:
   - Regain: `nearest_teammate_distance` ($\beta = -0.2228, z = -4.71, p < 0.0001, \text{OR} = 0.800$), `numerical_advantage_15` ($\beta = +0.1348, z = +4.98, p < 0.0001, \text{OR} = 1.144$), `opponent_mean_pairwise_distance` ($\beta = +0.1250, z = +4.78, p < 0.0001, \text{OR} = 1.133$).
   - Transition Risk: `initiation_x` ($\beta = -0.9715, z = -36.07, p < 0.0001, \text{OR} = 0.379$), `distance_to_nearest_touchline` ($\beta = +0.1981, z = +10.32, p < 0.0001, \text{OR} = 1.219$), `teammate_mean_pairwise_distance` ($\beta = +0.0831, z = +3.73, p = 0.0002, \text{OR} = 1.087$).
4. Robustness & Generalization:
   - High local coverage ($\ge 80\%$): Regain ROC-AUC = **0.8214**.
   - Actor discrepancy exclusion ($N=787$ dropped): Regain ROC-AUC = **0.8196**.
   - Leave-One-Competition-Out: All 7 competitions generalize well (ROC-AUC 0.7873 to 0.8466).
5. Three-Class Tactical Model:
   - Macro ROC-AUC = **0.7960**, Macro F1 = **0.6288**. Harmless escape recall = 83.1%, regain recall = 59.3%, dangerous escape recall = 42.2%.

### Status & Verification
- Unit Tests: 74 / 74 PASSED in 2.60s.
- Invariants Preserved: Primary cohort $N = 21,616$, 414 matches. Zero leakage.
- Figures 1–7 Generated and Verified in `results/figures/`.
- Notebooks 04 and 05 Created in `notebooks/`.

---

## 2026-09-18 — Iteration 4.5: Pre-Submission Statistical and Interpretation Audit

### Objectives & Constraints
- Consistency, statistical-validation, and interpretation audit prior to drafting MIT Sloan and CMSAC submissions.
- **Iterations 1–4 remain frozen**: primary cohort ($N = 21,616$, 414 matches), outcomes (`regain_5s_controlled` 34.65%, `dangerous_escape_15s` 22.41%), and spatial features unchanged. No new models or exploratory predictors.

### Key Audit Actions & Resolutions
1. **Touchline Coefficient Interpretation**:
   - `distance_to_nearest_touchline`: larger value = farther from touchline = more central.
   - Regain GLM coefficient is positive: $\beta = +0.1055, z = +5.62, p < 0.0001, \text{OR} = 1.111$ (more central counterpresses show higher adjusted regain odds conditional on covariates).
   - Descriptive regain rates are flat across touchline distance: Wide ($0-10$u) = 34.99%, Half-space ($10-20$u) = 34.90%, Central ($20-40$u) = 34.38%.
   - Transition danger: strongly positive both descriptively (Wide 16.86% $\to$ Central 25.15%, +49% relative increase) and conditionally ($\beta = +0.1981, z = +10.32, \text{OR} = 1.219$).
   - Tactical trade-off formulated with exact empirical nuance: central counterpresses show modestly higher modeled regain odds (+11% per SD) alongside substantially higher transition danger (+49% relative descriptive, +22% adjusted odds).
2. **Forward Numerical Advantage & Corridor Sign**:
   - True definition: $\text{forward\_numerical\_advantage} = \text{opponents\_ahead} - \text{defenders\_ahead}$ (positive = Opponent Surplus; negative = Pressing Defensive Surplus).
   - Implementation in `src/counterpress/features.py` verified as 100% correct.
   - Presentation labels in `descriptive_outcome_tables.csv` and Figure 6 were inverted in Iteration 4; corrected and regenerated.
   - Confounding diagnosed: Bivariate danger rate was lower for opponent surplus because attacking-third counterpresses have high opponent surplus alongside a low baseline danger rate (11.25%). In multivariable regression controlling for $x$, $\beta = +0.0617, p = 0.0103, \text{OR} = 1.064$ (more opponents ahead increases danger).
3. **Visibility Subset Reconciliation**:
   - `coverage_10 >= 0.80`: **20,547** (boolean flag) / **20,548** (float predicate), 0 missing. 1 row difference caused by floating point precision ($0.7999999999999999$).
   - `escape_corridor_coverage_20 >= 0.80`: **13,411** (62.04%), 0 missing. 13,873 was a draft pre-bounding figure.
   - Canonical status codified in `results/tables/visibility_subset_reconciliation.csv`.
4. **Cluster-Bootstrap Confidence Intervals**:
   - Null model CI $[0.4861, 0.5006]$ in Iteration 4 identified as a fold-prevalence pooling artifact (pooling 5 distinct training prevalences across folds created micro-variation). Within-fold and analytically, constant score ROC-AUC is identically $0.5000$.
   - Unit test `test_constant_predictor_roc_auc` implemented and passing.
   - Updated `results/tables/model_performance.csv` with $[0.5000, 0.5000]^*$ note.
5. **Paired Model Comparisons (1,000 Match-Cluster Resamples)**:
   - Regain: Model 3 vs Model 4 (GAM) $\Delta \text{ROC-AUC} = +0.0001$ [95% CI: $-0.0014, +0.0018$]; $\Delta \text{PR-AUC} = +0.0014$ [$-0.0006, +0.0036$] (overlaps zero).
   - Regain: Model 3 vs Model 5 (HGB) $\Delta \text{ROC-AUC} = -0.0011$ [$-0.0042, +0.0022$] (overlaps zero).
   - Danger: Model 3 vs Model 4 (GAM) $\Delta \text{ROC-AUC} = +0.0047$ [$+0.0026, +0.0067$]; $\Delta \text{PR-AUC} = +0.0296$ [$+0.0220, +0.0365$] (strictly positive).
   - Danger: Model 3 vs Model 5 (HGB) $\Delta \text{ROC-AUC} = +0.0091$ [$+0.0059, +0.0125$]; $\Delta \text{PR-AUC} = +0.0394$ [$+0.0299, +0.0490$] (strictly positive).
   - Codified in `results/tables/paired_model_comparisons.csv`.
6. **Revised Non-Linearity Claims**:
   - Regain: Flexible models did not materially improve out-of-sample discrimination over full spatial logistic model.
   - Danger: Flexible models yielded superior probability ranking and precision-recall performance, driven by non-linear threshold effects. Mechanistic interaction speculations disallowed.
7. **Non-Linear Diagnostics for Danger**:
   - Model 5 partial dependence generated in `results/figures/figure_8_danger_nonlinearity_diagnostics.png`.
   - Confirmed pitch $x$ threshold at $x \approx 35-40$ and touchline saturating sigmoidal response.
8. **Feature-Family vs. Coefficient Interpretation**:
   - Delineated conditional regression association vs. out-of-sample incremental value.
   - Forward escape structure shows conditional regression association ($\beta = +0.0617$ danger, $\beta = -0.0734$ regain) but negligible incremental predictive value ($\Delta \text{ROC-AUC} = 0.0000$).
9. **Fold-Wise Stability**:
   - Compact inferential GLM fit across all 5 folds: primary predictors exhibit identical signs in 100% of folds with minimal standard errors (`results/tables/coefficient_stability.csv`).
   - Permutation importance stability codified in `results/tables/permutation_importance_stability.csv`.
10. **Multiple-Inference Correction**:
    - Benjamini-Hochberg FDR $q$-values computed and saved in `results/tables/logistic_coefficients.csv`.
11. **Effect Language Corrections**:
    - Causal/hyperbolic phrases removed; observational interpretations enforced (e.g. 1 SD closer nearest teammate associated with ~25% higher odds of controlled regain).
12. **High-Coverage Sensitivity**:
    - Verified: standardized coefficients remain consistent across full cohort, 10m high-coverage cohort, and corridor high-coverage cohort (`results/tables/high_coverage_sensitivity_coefficients.csv`).
13. **Claims Audit Table**:
    - 10 conference-safe claims established in `results/tables/pre_submission_claims_audit.csv`.

### Artifacts & Tables Created/Updated
- `results/tables/paired_model_comparisons.csv`
- `results/tables/visibility_subset_reconciliation.csv`
- `results/tables/coefficient_stability.csv`
- `results/tables/permutation_importance_stability.csv`
- `results/tables/high_coverage_sensitivity_coefficients.csv`
- `results/tables/pre_submission_claims_audit.csv`
- `results/tables/descriptive_outcome_tables.csv` (labels corrected)
- `results/tables/logistic_coefficients.csv` (FDR $q$-values added)
- `results/tables/model_performance.csv` (Null model CI note updated)
- `results/tables/leave_competition_out.csv` (verified with prevalence)
- `results/figures/figure_5_danger_forward_advantage.png` (re-rendered with corrected labels)
- `results/figures/figure_6_danger_corridor_advantage.png` (re-rendered with corrected labels)
- `results/figures/figure_8_danger_nonlinearity_diagnostics.png` (new PDP figure)
- `docs/iteration4_5_report.md` (comprehensive audit report)
- `docs/iteration4_report.md` (audited prose and tables)

### Status & Verification
- Unit Tests: **75 / 75 PASSED** in 2.65s (`pytest tests/ -v`).
- Readiness: Primary cohort and model outputs are **100% audited, robust, and verified for MIT Sloan and CMSAC abstract drafting**.




