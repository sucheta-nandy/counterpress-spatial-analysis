"""Generate the 01_data_audit.ipynb notebook."""

import nbformat as nbf
from pathlib import Path

nb = nbf.v4.new_notebook()

cells = []

# Title and Overview
cells.append(nbf.v4.new_markdown_cell("""# 01 - StatsBomb Open Data & 360 Freeze Frame Audit

**Project**: *"When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer"*  
**Target Conferences**: MIT Sloan Sports Analytics Conference (SSAC) & Carnegie Mellon Sports Analytics Conference (CMSAC)  
**Author**: Research Team  
**Data Provider**: StatsBomb Open Data  

---

## Notebook Objectives
1. **Catalog Available Competitions**: Identify all competition-seasons with StatsBomb 360 freeze frames.
2. **Audit Dataset Size & Coverage**: Quantify matches, event records, counterpress events, and 360-matched counterpress actions.
3. **Verify Data Integrity**:
   - Event ordering and timeline consistency.
   - Timestamps and latency relative to turnovers.
   - Team perspective normalization and coordinate bounds ($120 \\times 80$ yd).
   - Freeze frame alignment (actor location vs. event location).
4. **Investigate Selection Bias & Missingness**:
   - Quantify missing 360 coverage across competitions and pitch zones.
   - Identify corrupted or missing upstream files (e.g. AFCON 2023 404, UEFA Women's Euro 2022 null byte block).
5. **Inspect Sample Visualizations**: Display verified counterpress freeze frames across varied tactical contexts.
"""))

# Imports & Setup
cells.append(nbf.v4.new_code_cell("""import json
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image, display

from counterpress.config import RAW_DIR, TABLES_DIR, FIGURES_DIR, PITCH_LENGTH, PITCH_WIDTH
from counterpress.data import load_competitions, load_events, load_three_sixty, StatsBombDownloader

%matplotlib inline
"""))

# Section 1: Competition & 360 Availability Audit
cells.append(nbf.v4.new_markdown_cell("""## 1. 360 Competition Catalog & Audit Table

Below is the exhaustive audit across all 12 competition-seasons flagged with 360 data in the official StatsBomb Open Data repository.
"""))

cells.append(nbf.v4.new_code_cell("""audit_csv = TABLES_DIR / "competition_360_audit.csv"
df_audit = pd.read_csv(audit_csv)
display(df_audit)
"""))

# Section 2: Summary Metrics
cells.append(nbf.v4.new_markdown_cell("""## 2. Key Sample Size & Usability Statistics"""))

cells.append(nbf.v4.new_code_cell("""total_row = df_audit[df_audit["competition"] == "TOTAL"].iloc[0]
valid_comps = df_audit[(df_audit["competition"] != "TOTAL") & (df_audit["n_counterpress_usable_360"] > 0)]

print(f"Total Matches Audited: {int(total_row['match_count']):,}")
print(f"Total Matches with 360 Available: {int(total_row['match_count_360']):,}")
print(f"Total Event Records: {int(total_row['n_event_records']):,}")
print(f"Total Counterpress Events: {int(total_row['n_counterpress_events']):,}")
print(f"Total Counterpress Events with Usable 360 Frames: {int(total_row['n_counterpress_usable_360']):,}")
print(f"Overall 360 Matching Rate: {total_row['pct_counterpress_usable_360']:.2f}%")
print(f"Competitions with Usable 360: {len(valid_comps)} of 12")
"""))

# Section 3: Verification Checks
cells.append(nbf.v4.new_markdown_cell("""## 3. Freeze-Frame Verification & Alignment Checks

We inspect 4 distinct counterpress events across different tournaments and leagues to verify coordinate alignment between the event record and the 360 freeze frame.
"""))

cells.append(nbf.v4.new_code_cell("""report_json = FIGURES_DIR / "verification_examples_report.json"
with open(report_json, "r") as f:
    verification_data = json.load(f)

df_verif = pd.DataFrame(verification_data)
cols = [
    "match_desc", "timestamp", "event_type", "pressing_team", 
    "possession_team", "actor_player", "coord_difference_dx_dy", "total_visible_players"
]
display(df_verif[cols])
"""))

# Section 4: Sample Visualizations
cells.append(nbf.v4.new_markdown_cell("""## 4. Representative Counterpress Visualizations

Each visualization renders the $120 \\times 80$ StatsBomb pitch, the camera's 360 visible area polygon, the counterpressing team (blue), opponent possession team (red), the pressing actor (gold star), and 5/10/15 yard density rings.
"""))

cells.append(nbf.v4.new_code_cell("""fig_paths = [
    FIGURES_DIR / "counterpress_example_1_worldcup.png",
    FIGURES_DIR / "counterpress_example_2_bundesliga.png",
    FIGURES_DIR / "counterpress_example_3_euro2024.png",
    FIGURES_DIR / "counterpress_example_4_laliga.png",
]

for p in fig_paths:
    if p.exists():
        display(Image(filename=str(p), width=800))
"""))

# Section 5: Summary and Conclusions
cells.append(nbf.v4.new_markdown_cell("""## 5. Audit Findings & Next Steps

### Data Integrity Findings:
1. **Coordinate System Invariant**: Coordinates are normalized to $120 \\times 80$ yards. The freeze-frame player locations and actor coordinates match event coordinates with floating-point precision ($\Delta \\le 10^{-6}$).
2. **Team Perspective**: In a counterpress event by Team A, Team A attacks toward $x = 120$ (own goal at $x = 0$). Teammates (`teammate: true`) are counterpressers; opponents (`teammate: false`) are in possession.
3. **Data Anomalies Identified**:
   - **AFCON 2023**: 360 file for final match (3923881) returns HTTP 404 (file missing upstream).
   - **UEFA Women's Euro 2022**: Match 3845506 (England vs Sweden) contains a 16KB zeroed/null-byte block in the upstream JSON.
   - **MLS 2023**: Unusually low 360 coverage on counterpressing (47.7% vs >85% in European leagues/tournaments).

### Next Iteration:
Proceed to **Notebook 02**: Turnover Detection & Counterpress Chain Extraction (`turnovers.py` & `outcomes.py`).
"""))

nb.cells = cells

notebook_path = Path("notebooks/01_data_audit.ipynb")
with open(notebook_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Generated {notebook_path} successfully with {len(cells)} cells.")
