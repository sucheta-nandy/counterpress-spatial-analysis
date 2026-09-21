"""Data acquisition, caching, and manifest generation for StatsBomb Open Data and 360.

Provides deterministic, cached access to:
- Competitions metadata
- Match lists
- Event-level logs
- 360 freeze-frame tracking data
"""

import json
import logging
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd

from counterpress.config import RAW_DIR, STATSBOMB_GITHUB_RAW_BASE, STATSBOMB_RAW_DIR

logger = logging.getLogger(__name__)


class StatsBombDownloader:
    """Handles downloading and local file-system caching of StatsBomb Open Data."""

    def __init__(self, cache_dir: Path = STATSBOMB_RAW_DIR, base_url: str = STATSBOMB_GITHUB_RAW_BASE):
        self.cache_dir = Path(cache_dir)
        self.base_url = base_url.rstrip("/")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_json(self, relative_path: str, force_refresh: bool = False) -> Optional[Any]:
        """Fetch JSON data from local cache or remote GitHub raw repository."""
        local_path = self.cache_dir / relative_path
        if local_path.exists() and not force_refresh:
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Error reading cached file {local_path}: {e}. Re-fetching.")

        remote_url = f"{self.base_url}/{relative_path}"
        try:
            req = urllib.request.Request(
                remote_url,
                headers={"User-Agent": "CounterpressResearch/1.0 (Academic Research; StatsBombOpenData)"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            local_path.parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, "w", encoding="utf-8") as f:
                json.dump(data, f)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            logger.error(f"HTTP Error {e.code} fetching {remote_url}: {e.reason}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching {remote_url}: {e}")
            raise

    def get_competitions(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Fetch list of all competition-seasons."""
        data = self._get_json("competitions.json", force_refresh=force_refresh)
        return data if data is not None else []

    def get_matches(self, competition_id: int, season_id: int, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Fetch list of matches for a competition and season."""
        data = self._get_json(f"matches/{competition_id}/{season_id}.json", force_refresh=force_refresh)
        return data if data is not None else []

    def get_events(self, match_id: int, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Fetch event-level data for a specific match."""
        data = self._get_json(f"events/{match_id}.json", force_refresh=force_refresh)
        return data if data is not None else []

    def get_three_sixty(self, match_id: int, force_refresh: bool = False) -> Optional[List[Dict[str, Any]]]:
        """Fetch 360 freeze frames for a specific match.

        Returns None if no 360 data exists for this match.
        """
        return self._get_json(f"three-sixty/{match_id}.json", force_refresh=force_refresh)


# Global default downloader instance
_default_downloader = StatsBombDownloader()


def load_competitions(force_refresh: bool = False) -> pd.DataFrame:
    """Load all competition seasons into a pandas DataFrame."""
    raw = _default_downloader.get_competitions(force_refresh=force_refresh)
    return pd.DataFrame(raw)


def load_matches(competition_id: int, season_id: int, force_refresh: bool = False) -> pd.DataFrame:
    """Load matches for a specific competition-season into a pandas DataFrame."""
    raw = _default_downloader.get_matches(competition_id, season_id, force_refresh=force_refresh)
    return pd.DataFrame(raw)


def load_events(match_id: int, force_refresh: bool = False) -> List[Dict[str, Any]]:
    """Load raw event log for a match."""
    return _default_downloader.get_events(match_id, force_refresh=force_refresh)


def load_three_sixty(match_id: int, force_refresh: bool = False) -> Optional[List[Dict[str, Any]]]:
    """Load raw 360 freeze frames for a match."""
    return _default_downloader.get_three_sixty(match_id, force_refresh=force_refresh)


def build_match_manifest(
    output_path: Optional[Path] = None, force_refresh: bool = False
) -> pd.DataFrame:
    """Build a comprehensive manifest of all matches with 360 availability across all competitions.

    Saves to data/raw/match_manifest.csv if output_path is provided or default.
    """
    comps = load_competitions(force_refresh=force_refresh)
    manifest_rows = []

    for _, comp in comps.iterrows():
        cid = comp["competition_id"]
        sid = comp["season_id"]
        cname = comp["competition_name"]
        sname = comp["season_name"]
        c_has_360 = pd.notna(comp.get("match_available_360")) and comp.get("match_available_360") is not None

        try:
            matches = _default_downloader.get_matches(cid, sid, force_refresh=force_refresh)
        except Exception as e:
            logger.warning(f"Could not load matches for {cname} ({sname}): {e}")
            continue

        for m in matches:
            m_status_360 = m.get("match_status_360")
            has_360 = m_status_360 == "available"
            manifest_rows.append({
                "match_id": m["match_id"],
                "match_date": m.get("match_date"),
                "competition_id": cid,
                "competition_name": cname,
                "season_id": sid,
                "season_name": sname,
                "competition_gender": comp.get("competition_gender"),
                "home_team_id": m.get("home_team", {}).get("home_team_id"),
                "home_team_name": m.get("home_team", {}).get("home_team_name"),
                "away_team_id": m.get("away_team", {}).get("away_team_id"),
                "away_team_name": m.get("away_team", {}).get("away_team_name"),
                "home_score": m.get("home_score"),
                "away_score": m.get("away_score"),
                "match_status": m.get("match_status"),
                "match_status_360": m_status_360,
                "has_360": has_360,
                "comp_flag_360": c_has_360,
            })

    df = pd.DataFrame(manifest_rows)
    if output_path is None:
        output_path = RAW_DIR / "match_manifest.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Saved manifest of {len(df)} matches to {output_path}")
    return df


def audit_single_match(match_id: int) -> Dict[str, Any]:
    """Audit a single match: count events, counterpress events, and 360-matched counterpress events."""
    events = load_events(match_id)
    frames = load_three_sixty(match_id)

    frame_uuids = set(f["event_uuid"] for f in frames) if frames else set()

    n_events = len(events)
    n_cp = 0
    n_cp_with_360 = 0
    n_cp_with_players = 0

    for e in events:
        if e.get("counterpress") is True:
            n_cp += 1
            eid = e.get("id")
            if eid in frame_uuids:
                n_cp_with_360 += 1

    # Check freeze-frame player counts
    if frames:
        for f in frames:
            if f.get("event_uuid") in {e.get("id") for e in events if e.get("counterpress") is True}:
                if len(f.get("freeze_frame", [])) > 0:
                    n_cp_with_players += 1

    return {
        "match_id": match_id,
        "n_events": n_events,
        "n_cp": n_cp,
        "n_cp_with_360": n_cp_with_360,
        "n_cp_with_players": n_cp_with_players,
        "has_360_file": frames is not None,
    }
