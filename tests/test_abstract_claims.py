"""tests/test_abstract_claims.py

Automated Claim Validation and Word Count Tests for Conference Abstracts:
- SSAC27 Abstract Version A (Methodological Focus)
- SSAC27 Abstract Version B (Practitioner Focus)
- CMSAC Poster Abstract Contingency Draft

Ensures that every quantitative statement programmatically matches
results/tables/canonical_conference_claims.csv and strictly obeys
venue word limits and terminology rules.
"""

from pathlib import Path
import re
import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = PROJECT_ROOT / "docs"
TABLES_DIR = PROJECT_ROOT / "results" / "tables"


@pytest.fixture(scope="module")
def claims_df():
    return pd.read_csv(TABLES_DIR / "canonical_conference_claims.csv")


@pytest.fixture(scope="module")
def abstract_a_text():
    content = (DOCS_DIR / "ssac27_abstract_version_a.md").read_text(encoding="utf-8")
    match = re.search(r"(### TITLE[\s\S]+)", content)
    return match.group(1) if match else content


@pytest.fixture(scope="module")
def abstract_b_text():
    content = (DOCS_DIR / "ssac27_abstract_version_b.md").read_text(encoding="utf-8")
    match = re.search(r"(### TITLE[\s\S]+)", content)
    return match.group(1) if match else content


@pytest.fixture(scope="module")
def cmsac_text():
    content = (DOCS_DIR / "cmsac_poster_abstract_contingency.md").read_text(encoding="utf-8")
    match = re.search(r"(### TITLE[\s\S]+)", content)
    return match.group(1) if match else content


def count_words(text: str) -> int:
    """Standard word count splitting on whitespace."""
    clean_text = re.sub(r"[#*_`]", " ", text)
    tokens = [t for t in clean_text.split() if t]
    return len(tokens)


# ----------------------------------------------------------------------
# 1. Word Count Limits
# ----------------------------------------------------------------------
def test_ssac27_abstract_a_word_count(abstract_a_text):
    wc = count_words(abstract_a_text)
    assert wc < 500, f"SSAC27 Version A exceeds 500 words limit: {wc}"
    assert 400 <= wc <= 460, f"SSAC27 Version A outside target 400-460 range: {wc}"


def test_ssac27_abstract_b_word_count(abstract_b_text):
    wc = count_words(abstract_b_text)
    assert wc < 500, f"SSAC27 Version B exceeds 500 words limit: {wc}"
    assert 400 <= wc <= 460, f"SSAC27 Version B outside target 400-460 range: {wc}"


def test_cmsac_abstract_word_count(cmsac_text):
    wc = count_words(cmsac_text)
    assert wc <= 320, f"CMSAC draft exceeds 320 words: {wc}"
    assert wc >= 220, f"CMSAC draft below 220 words: {wc}"


# ----------------------------------------------------------------------
# 2. Canonical Quantitative Values Consistency
# ----------------------------------------------------------------------
def test_abstracts_dataset_scale(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "21,616" in text, f"{name} missing canonical episode count 21,616"
        assert "414" in text, f"{name} missing canonical match count 414"
        assert "seven" in text.lower(), f"{name} missing competition count 7"


def test_abstracts_outcome_prevalences(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "34.65%" in text, f"{name} missing regain prevalence 34.65%"
        assert "22.41%" in text, f"{name} missing danger prevalence 22.41%"


def test_abstracts_incremental_predictive_value(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "+0.0230" in text, f"{name} missing delta ROC-AUC +0.0230"
        assert "+0.0377" in text, f"{name} missing delta PR-AUC +0.0377"
        assert "0.7926" in text, f"{name} missing Context ROC-AUC 0.7926"
        assert "0.8156" in text, f"{name} missing Full Spatial ROC-AUC 0.8156"
        assert "+0.0181, +0.0278" in text, f"{name} missing paired bootstrap CI +0.0181, +0.0278"


def test_abstracts_nearest_teammate_odds_ratio(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "0.800" in text, f"{name} missing nearest teammate OR 0.800"
        assert "0.729, 0.878" in text, f"{name} missing nearest teammate 95% CI 0.729, 0.878"
        assert "8.2" in text, f"{name} missing nearest teammate SD 8.2 units"


def test_abstracts_numerical_advantage_odds_ratios(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "1.071" in text, f"{name} missing numerical advantage 10u OR 1.071"
        assert "1.144" in text, f"{name} missing numerical advantage 15u OR 1.144"


def test_abstracts_danger_pitch_third_and_centrality(abstract_a_text, abstract_b_text, cmsac_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        assert "31.57%" in text, f"{name} missing defensive third danger 31.57%"
        assert "11.28%" in text, f"{name} missing attacking third danger 11.28%"
        assert "0.379" in text, f"{name} missing initiation_x OR 0.379"
        assert "0.359, 0.399" in text, f"{name} missing initiation_x CI 0.359, 0.399"
        assert "25.15%" in text, f"{name} missing central danger 25.15%"
        assert "16.86%" in text, f"{name} missing wide danger 16.86%"
        assert "1.219" in text, f"{name} missing touchline danger OR 1.219"
        assert "1.174, 1.266" in text, f"{name} missing touchline danger CI 1.174, 1.266"


def test_abstracts_nonlinearity_metrics(abstract_a_text, abstract_b_text):
    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B")]:
        assert "+0.0394" in text, f"{name} missing HGB danger delta PR-AUC +0.0394"
        assert "+0.0299, +0.0490" in text, f"{name} missing HGB danger PR-AUC CI +0.0299, +0.0490"


# ----------------------------------------------------------------------
# 3. Terminology & Phrasing Guardrails
# ----------------------------------------------------------------------
def test_abstracts_terminology_guardrails(abstract_a_text, abstract_b_text, cmsac_text):
    prohibited_patterns = [
        r"continuous tracking",
        r"tracking-derived",
        r"first study",
        r"first to",
        r"causes regain",
        r"guarantees",
        r"100% verified",
        r"ground-truth validated",
        r"35\.9%",
        r"\+0\.0251",
        r"\+0\.0204",
        r"1\.074",
        r"1\.055",
        r"0\.512"
    ]

    for text, name in [(abstract_a_text, "Version A"), (abstract_b_text, "Version B"), (cmsac_text, "CMSAC")]:
        for pattern in prohibited_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            assert len(matches) == 0, f"{name} contains prohibited phrasing '{pattern}': {matches}"
