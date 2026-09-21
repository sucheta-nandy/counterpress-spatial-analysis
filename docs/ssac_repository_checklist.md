# SSAC27 Open-Source Repository Readiness Audit & Checklist

**Target Competition**: MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition  
**Requirement**: Open-source supporting code and data repository for reproducibility.  
**Repository Placeholder**: `[PUBLIC REPOSITORY URL]`  

---

## 1. Executive Summary & Readiness Verdict

An exhaustive audit of the `counterpress-spatial-analysis` codebase confirms that the project adheres to reproducible research standards and is ready for public release upon submission. All quantitative results reported in conference abstracts and manuscripts are generated through deterministic pipelines with fixed random seeds.

| Component | Status | Verification Detail |
| :--- | :---: | :--- |
| **Code Reproducibility** | **READY** | Automated execution via `pyproject.toml` and CLI scripts; 84/84 unit tests passing. |
| **Data Licensing** | **READY** | StatsBomb Open Data attribution and terms clearly stated; raw data downloaded via public manifests. |
| **Open Source License** | **READY** | Permissive MIT License established at repository root. |
| **Environment Specification** | **READY** | Deterministic dependencies defined in `pyproject.toml` with explicit version bounds. |
| **Sanitization & Security** | **READY** | No API keys, credentials, private paths, or proprietary data committed. |
| **Documentation & Dictionary** | **READY** | Comprehensive data dictionaries, methodology notes, and frozen result tables provided. |

---

## 2. Detailed Component Audit

### 2.1 Repository File Sanitization
* **Absolute Path Audit**: All scripts and modules utilize dynamic root discovery via `Path(__file__).resolve().parents[...]` or relative workspace paths. No hardcoded absolute workstation paths exist in runtime executable logic.
* **Credentials & Secrets**: Zero API keys, authentication tokens, or private credentials exist in the codebase.
* **OS & IDE Artifacts**: `.DS_Store`, `.idea/`, `.vscode/`, and `.pytest_cache/` are explicitly ignored in `.gitignore`.
* **Temporary Files**: Scratch logs, intermediate test caches, and temporary virtual environments (`.venv/`) are excluded from version control.

### 2.2 Data Integrity & Attribution
* **Attribution Notice**: StatsBomb Open Data user agreement and attribution are prominently displayed in `README.md`.
* **No Unauthorized Redistribution**: The repository does not commit large raw JSON event dumps; instead, `data/raw/match_manifest.csv` catalogs the 414 matches and official GitHub URLs, enabling automated, reproducible fetching via `scripts/fetch_data.py`.
* **Locked Cohort Manifest**: [`results/tables/primary_cohort_episode_ids.csv`](../results/tables/primary_cohort_episode_ids.csv) ($N = 21,616$) ensures external users analyze the exact frozen cohort.

### 2.3 Environment & Determinism
* **Python Environment**: Standardized on Python $\ge 3.9$ via `pyproject.toml`.
* **Core Dependencies**:
  - `pandas >= 2.0.0`
  - `numpy >= 1.24.0`
  - `scipy >= 1.10.0`
  - `scikit-learn >= 1.3.0`
  - `statsmodels >= 0.14.0`
  - `pyarrow >= 12.0.0`
  - `shapely >= 2.0.0`
  - `matplotlib >= 3.7.0`
  - `seaborn >= 0.12.0`
  - `pytest >= 7.0.0`
* **Random Seeds**: Modeling scripts and cross-validation partitioners explicitly enforce `random_state=42` and `np.random.seed(42)` across all 5 folds and 1,000 bootstrap resamples.

---

## 3. End-to-End Reproduction Pipeline

Public users can fully reproduce the published results and figures by executing the following terminal commands:

```bash
# 1. Clone repository
git clone [PUBLIC REPOSITORY URL]
cd counterpress-spatial-analysis

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

# 3. Download raw StatsBomb Open Data (414 matches)
python scripts/fetch_data.py

# 4. Extract counterpress episodes & enforce open-play transition gates
python scripts/extract_episodes.py

# 5. Compute StatsBomb 360 freeze-frame spatial features
python scripts/compute_spatial_features.py

# 6. Execute match-clustered modeling, GLM inference, & paired bootstrap
python scripts/run_iteration4_modeling.py

# 7. Generate publication figures & descriptive tables
python scripts/generate_iteration4_figures.py
python scripts/generate_descriptive_tables.py

# 8. Rebuild canonical conference claims table programmatically
python scripts/build_canonical_claims.py

# 9. Run full verification test suite (all assertions must pass)
pytest tests/ -v
```

---

## 4. Public README Structure Template

When publishing the repository to GitHub, the root `README.md` should adhere to the following outline:

```markdown
# When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Tests: 84 Passed](https://img.shields.io/badge/Tests-84%20Passed-brightgreen.svg)](tests/)

This repository contains the official supporting code, data manifests, statistical modeling scripts, and reproducibility test harness for our research paper submitted to the **MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition**.

## Repository Contents
- `data/`: Match manifests and instructions to download raw StatsBomb 360 data.
- `src/counterpress/`: Modular Python library for turnover detection, 360 geometry, and clustered inference.
- `scripts/`: Deterministic pipeline scripts for data processing, model fitting, and figure generation.
- `results/`: Canonical result tables, GLM coefficient matrices, and publication figures.
- `docs/`: Comprehensive data dictionary, methodology documentation, and claims audit.
- `tests/`: 84 automated unit tests verifying data invariants, spatial math, and numeric consistency.

## Quickstart & Reproduction
[Commands as detailed above]

## Data Attribution
All event and 360 freeze-frame data provided by StatsBomb (https://statsbomb.com/) via the StatsBomb Open Data initiative. Used under the StatsBomb Open Data User Agreement.

## Citation & Inquiries
Please cite the SSAC27 paper:
[Citation Placeholder]
```
