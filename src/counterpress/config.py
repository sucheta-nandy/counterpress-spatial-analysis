"""Global configuration constants, directory paths, and coordinate systems for

the counterpress spatial analysis research project.
"""

from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
STATSBOMB_RAW_DIR = RAW_DIR / "statsbomb"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"
METRICS_DIR = RESULTS_DIR / "metrics"
DOCS_DIR = PROJECT_ROOT / "docs"

# Ensure essential output directories exist
for path in [STATSBOMB_RAW_DIR, INTERIM_DIR, PROCESSED_DIR, FIGURES_DIR, TABLES_DIR, METRICS_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# StatsBomb Coordinate System
# The coordinate system is 120 (length) x 80 (width) StatsBomb coordinate units.
# In event data, the team performing the action attacks from left to right:
# (0, 0) is top-left, (120, 80) is bottom-right.
# Acting team's defending goal is at x=0, y=40; attacking goal is at x=120, y=40.
PITCH_LENGTH = 120.0
PITCH_WIDTH = 80.0
PITCH_AREA = PITCH_LENGTH * PITCH_WIDTH  # 9600.0 StatsBomb coordinate area units
GOAL_LINE_DEFENDING = 0.0
GOAL_LINE_ATTACKING = 120.0
GOAL_CENTER = (120.0, 40.0)
OWN_GOAL_CENTER = (0.0, 40.0)
PITCH_CENTER = (60.0, 40.0)

# Forward escape corridor constants
ESCAPE_CORRIDOR_RADIUS = 20.0
ESCAPE_CORRIDOR_HALF_ANGLE_DEG = 30.0

# Touchlines: y = 0.0 and y = 80.0
TOUCHLINE_TOP = 0.0
TOUCHLINE_BOTTOM = 80.0

# Pitch zones (thirds)
DEFENSIVE_THIRD_X = 40.0
MIDDLE_THIRD_X = 80.0
FINAL_THIRD_X = 80.0

# Operational time windows (seconds)
# StatsBomb definition: pressing actions occurring within 5 seconds of an open play turnover
COUNTERPRESS_WINDOW_SECONDS = 5.0

# Outcome 1: Regain possession within 5 seconds of counterpress initiation (with 3s and 8s sensitivity)
REGAIN_WINDOW_SECONDS = 5.0
REGAIN_SENSITIVITY_WINDOWS = [3.0, 5.0, 8.0]

# Outcome 2: Opponent escapes and creates a dangerous transition within 15 seconds
TRANSITION_WINDOW_SECONDS = 15.0

# Spatial radii for local density / superiority features (in StatsBomb coordinate units)
SPATIAL_RADII = [5.0, 10.0, 15.0]

# Reproducibility seed
RANDOM_SEED = 42

# Official StatsBomb Open Data GitHub raw repository
STATSBOMB_GITHUB_RAW_BASE = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"
