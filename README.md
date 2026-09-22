# When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Tests: 95 Passed](https://img.shields.io/badge/Tests-95%20Passed-brightgreen.svg)](tests/)

Supporting code, reproducible data pipeline, and statistical modeling suite for our research paper targeting the:
- **MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition**

---

## 1. Research Overview & Questions

In modern elite soccer, counterpressing—the immediate defensive pressure applied by a team upon losing possession—is one of the most widely adopted tactical paradigms. However, counterpressing presents a high-risk, high-reward tactical dilemma: committing players toward the ball can trap opponents deep in their defensive third or, if bypassed, expose severe defensive voids that lead to high-xG transitions.

While analysts frequently quantify pressing volumes (e.g., PPDA, challenge counts), teams lack objective spatial criteria to evaluate when a counterpress should be triggered versus when defenders should drop and delay. Using event-level **StatsBomb 360 freeze-frame spatial geometry**, this research investigates two central questions:

1. **Short-Horizon Controlled Regain**: Which spatial conditions at counterpress initiation predict regaining possession within 5 seconds?
2. **Transition Exposure Risk**: Which spatial conditions predict the opponent escaping pressure to generate a dangerous transition (final-third entry or shot within 15 seconds)?
3. **Cross-Competition Generalizability**: Do these relationships transfer consistently across diverse domestic leagues, international tournaments, and women's competitions?

---

## 2. Dataset Description

The analysis is conducted across **21,616 distinct open-play counterpress episodes** spanning **414 matches** from seven elite professional competitions:
- **UEFA Euro 2024** (4,764 episodes, 51 matches)
- **FIFA World Cup 2022** (2,955 episodes, 64 matches)
- **UEFA Women's Euro 2022** (3,533 episodes, 31 matches)
- **FIFA Women's World Cup 2023** (3,917 episodes, 64 matches)
- **French Ligue 1** (2,924 episodes, 77 matches)
- **Spanish La Liga** (1,861 episodes, 79 matches)
- **German 1. Bundesliga** (1,662 episodes, 48 matches)

### Episode Definition & Aggregation
To prevent pseudo-replication, individual counterpress-tagged actions (40,054 raw events) occurring within 5 seconds of an open-play turnover are collapsed into single distinct episodes anchored at the earliest initiation timestamp. All spatial predictors are measured strictly at the **moment of counterpress initiation**.

---

## 3. Outcome Definitions

We evaluate counterpress outcomes using a deterministic dual-outcome framework and a mutually exclusive three-state taxonomy:

1. **Controlled Regain within 5 Seconds (`regain_5s_controlled`)**  
   *Prevalence: 34.65% (7,491 / 21,616)*  
   Requires both verified possession transition and controlled execution (carry $\ge 3$m, completed pass, shot, or controlled recovery) within 5.000 seconds. Defensive deflections (blocks, pressures) alone do not qualify.
2. **Dangerous Transition within 15 Seconds (`dangerous_escape_15s`)**  
   *Prevalence: 22.41% (4,844 / 21,616)*  
   Occurs if the escaping opponent registers a shot or penetrates the counterpressing team's defending final third ($x \le 40$ in defending coordinates) within 15.000 seconds of initiation.
3. **Three-State Taxonomy**:
   - **Successful Regain**: 32.27% (6,976 episodes)
   - **Harmless Escape**: 45.32% (9,796 episodes)
   - **Dangerous Escape**: 22.41% (4,844 episodes)

---

## 4. Key Empirical Findings

All reported metrics are verified by automated assertion tests and derived from our canonical primary inferential GLM (`PRIMARY_INFERENTIAL_MODEL` clustered by `match_id`):

1. **Incremental Value of 360 Geometry**: StatsBomb 360 freeze-frame spatial geometry provides statistically reliable incremental predictive value over match context and pitch location alone for 5-second regains ($\Delta \text{ROC-AUC} = \mathbf{+0.0230}$, $\Delta \text{PR-AUC} = \mathbf{+0.0377}$; paired match-clustered bootstrap 95% CI $[\mathbf{+0.0181, +0.0278}]$).
2. **Immediate Teammate Proximity**: Holding modeled covariates fixed, shorter nearest-teammate distance is strongly associated with higher regain odds ($\text{OR} = \mathbf{0.800}$ [95% CI: $0.729, 0.878$], $p < 0.0001$ per 1 SD = 8.2 StatsBomb coordinate units). Being 1 SD closer corresponds to **+25.0% higher regain odds**.
3. **Broader Numerical Support**: Robust positive associations emerge at 10 units ($\text{OR} = \mathbf{1.071}$ [95% CI: $1.014, 1.130$]) and 15 units ($\text{OR} = \mathbf{1.144}$ [95% CI: $1.085, 1.207$]), while immediate 5-unit advantage is not independently significant in the fully adjusted model.
4. **Pitch Position & Transition Danger**: Longitudinal pitch position dominates transition risk ($\text{OR} = \mathbf{0.379}$ [95% CI: $0.359, 0.399$]). Turnovers in the defensive third yield **31.57% danger** versus **11.28%** in the attacking third (nearly 3x higher).
5. **The Centrality Trade-Off**: Unadjusted regain rates are flat across pitch width (34.30% wide vs. 34.85% central), but after adjustment central pressing has modestly higher regain odds ($\text{OR} = \mathbf{1.111}$). However, central counterpresses carry substantially higher transition danger (**25.15% central vs. 16.86% wide**, $\text{OR} = \mathbf{1.219}$ [95% CI: $1.174, 1.266$]).
6. **Linear Sufficiency vs. Non-Linear Benefit**: Flexible non-linear models (GAM, HGB) do not improve regain discrimination over spatial logistic regression (Delta ROC-AUC CIs overlap zero). In contrast, gradient boosting significantly improves transition danger ranking ($\Delta \text{PR-AUC} = \mathbf{+0.0394}$ [95% CI: $+0.0299, +0.0490$]) due to threshold depth non-linearities.
7. **Competition Holdout Transfer**: In leave-one-competition-out cross-validation across all seven competitions, out-of-sample regain ROC-AUC ranges from 0.7873 to 0.8466 and danger ROC-AUC ranges from 0.7532 to 0.7919.

---

## 5. Repository Structure

```text
counterpress-spatial-analysis/
├── LICENSE                             # MIT Open-Source License
├── README.md                           # Project overview, documentation, and reproduction
├── pyproject.toml                      # Package specifications and dependencies
├── .gitignore                          # Exclusions for virtual environments and caches
├── data/
│   ├── raw/match_manifest.csv          # Catalog of 414 matches with StatsBomb 360 availability
│   ├── interim/.gitkeep                # Directory for cleaned event tables
│   └── processed/.gitkeep              # Directory for engineered spatial feature parquets
├── src/
│   └── counterpress/                   # Core modular Python library
│       ├── config.py                   # Coordinates, pitch bounds, and directory constants
│       ├── data.py                     # StatsBomb downloader, caching, and manifest parsers
│       ├── turnovers.py                # Deterministic turnover & open-play detection
│       ├── outcomes.py                 # 5s regain and 15s transition danger labeling
│       ├── spatial.py                  # Geometric calculations, Voronoi, and density metrics
│       ├── features.py                 # Tabular feature matrix pipeline
│       ├── modeling.py                 # Grouped CV, calibration, and clustered GLM inference
│       └── visualization.py            # Freeze-frame pitch plots & diagnostic overlays
├── scripts/
│   ├── extract_episodes.py             # Episode extraction and multi-action collapsing
│   ├── extract_spatial_features.py     # 360 freeze-frame geometric feature engineering
│   ├── run_iteration4_modeling.py      # Match-clustered cross-validation and GLM fitting
│   ├── generate_iteration4_figures.py  # Publication figure generation
│   ├── generate_descriptive_tables.py  # Descriptive cross-tabulations
│   └── build_canonical_claims.py       # Programmatic claims table generator
├── results/
│   ├── figures/                        # Publication figures (ROC curves, PDPs, forest plots)
│   └── tables/                         # Canonical CSV result matrices, GLM coefficients, audit tables
├── docs/
│   ├── ssac27_abstract_version_a.md    # SSAC27 Abstract Draft (Methodological Focus, 437 words)
│   ├── ssac27_abstract_version_b.md    # SSAC27 Abstract Draft (Practitioner Focus, 439 words)
│   ├── cmsac_poster_abstract_contingency.md # CMSAC Contingency Poster Draft (247 words)
│   ├── manuscript_outline.md           # 12-section full manuscript architecture
│   ├── related_work_todo.md            # Literature verification checklist
│   ├── poster_storyboard.md            # 6-block visual poster layout
│   └── ssac_repository_checklist.md    # Open-source public readiness audit
└── tests/
    ├── test_abstract_claims.py         # Automated word count and numerical claim checks
    ├── test_claim_consistency.py       # Assertions A-I for conference claims
    ├── test_cohort_invariants.py       # Primary cohort (21,616 episodes, 414 matches) checks
    ├── test_data.py                    # Schema and pitch boundary invariant tests
    ├── test_features.py                # Spatial feature extraction tests
    ├── test_iteration3_invariants.py   # Spatial feature summary consistency
    ├── test_modeling.py                # CV fold isolation and inference tests
    ├── test_outcomes.py                # Outcome sequence and latency logic tests
    ├── test_spatial.py                 # Geometric polygon clipping and Euclidean distance tests
    └── test_turnovers.py               # Turnover detection and latency filtering tests
```

---

## 6. Installation & Setup

### Prerequisites
- Python 3.9+
- Git

### Virtual Environment Setup
```bash
# Clone the repository
git clone https://github.com/sucheta-nandy/counterpress-spatial-analysis.git
cd counterpress-spatial-analysis

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install package and dependencies in editable mode
pip install --upgrade pip
pip install -e ".[dev]"
```

---

## 7. Data Acquisition Instructions

This project exclusively utilizes **StatsBomb Open Data** and **StatsBomb 360 Open Data**. In accordance with the StatsBomb Open Data User Agreement, raw JSON data files are not redistributed in this repository.

To download the required open-data matches:
```bash
# Fetch raw StatsBomb event and 360 files for all 414 cataloged matches
python -c "
from counterpress.data import StatsBombDownloader
import pandas as pd
manifest = pd.read_csv('data/raw/match_manifest.csv')
downloader = StatsBombDownloader()
downloader.download_matches(manifest['match_id'].tolist())
"
```

---

## 8. Full Reproduction Pipeline

Execute the pipeline sequentially to reproduce all processed matrices, models, tables, and figures:

```bash
# 1. Extract counterpress episodes from raw events
python scripts/extract_episodes.py

# 2. Engineer 360 freeze-frame spatial features
python scripts/extract_spatial_features.py

# 3. Fit match-clustered probability models, inferential GLM, and paired bootstrap
python scripts/run_iteration4_modeling.py

# 4. Generate descriptive tables and publication figures
python scripts/generate_descriptive_tables.py
python scripts/generate_iteration4_figures.py

# 5. Programmatically build canonical claims table
python scripts/build_canonical_claims.py
```

---

## 9. Running Automated Verification Tests

The test suite validates spatial coordinate math, outcome sequence rules, cohort invariants, and exact numeric consistency across all conference claims:

```bash
pytest tests/ -v
```

Expected output: **95 passed in ~3.30s**.

---

## 10. Methodological Limitations

1. **Freeze Frames vs. Continuous Tracking**: StatsBomb 360 captures spatial geometry at event initiation only; player velocities, accelerations, and body orientations are unobserved.
2. **Broadcast Camera Truncation**: Players outside the broadcast field of view are unobserved. Sensitivity models confirm that primary associations remain stable when restricted to high-visibility episodes ($\ge 80\%$ coverage), but peripheral positioning is unobserved.
3. **Observational Associations**: Results represent conditional statistical associations, not causal treatment effects. Tactical selection bias may influence when teams press.
4. **Human Adjudication**: While outcome algorithms are automated and statistically audited, comprehensive video adjudication of edge-case traces remains an ongoing objective.

---

## 11. Conference Status & Attribution

- **MIT Sloan Sports Analytics Conference 2027 (SSAC27)**: Research Paper Competition submission draft prepared ([`docs/ssac27_abstract_version_a.md`](docs/ssac27_abstract_version_a.md)).


### Attribution
Data provided by [StatsBomb](https://statsbomb.com/). Used under the [StatsBomb Open Data User Agreement](https://github.com/statsbomb/open-data).
