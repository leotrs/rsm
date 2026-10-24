"""Regression corpus of real bibliography samples (bead rsm-ddx.5.7).

The .bbl fixtures were generated with bibtex from tests/fixtures/bibliography/
refs.bib across four styles (plain, ieeetr, amsalpha, plainnat), so extraction,
AnyStyle structuring, and RSM emission stay checked against real input. Each
fixture is isolated in its own directory per test, because a .bib in the same
directory would shadow a .bbl by the source precedence.
"""

import re
import shutil
from pathlib import Path

import pytest

from rsm.bibemit import references_block
from rsm.bibextract import extract_references

FIX = Path(__file__).parent / "fixtures" / "bibliography"
KEYS = {
    "shannon1948",
    "knuth1997",
    "vaswani2017",
    "bengio2013",
    "turing1938",
    "preprint2020",
}
BBL_STYLES = ["plain", "ieeetr", "amsalpha", "plainnat"]
HAS_ANYSTYLE = shutil.which("anystyle") is not None


@pytest.mark.parametrize("style", BBL_STYLES)
def test_bbl_extraction(tmp_path, style):
    shutil.copy(FIX / f"{style}.bbl", tmp_path / "paper.bbl")
    refs = extract_references("", tmp_path, KEYS)
    assert {r.key for r in refs} == KEYS
    assert all(r.source == "bbl" for r in refs)
    for r in refs:
        assert "\\newblock" not in r.raw
        assert "~" not in r.raw
        assert "{" not in r.raw and "}" not in r.raw


def test_bib_extraction_passthrough(tmp_path):
    shutil.copy(FIX / "refs.bib", tmp_path / "refs.bib")
    refs = extract_references(r"\bibliography{refs}", tmp_path, KEYS)
    assert {r.key for r in refs} == KEYS
    assert all(r.source == "bib" for r in refs)
    assert any("Shannon" in r.raw for r in refs)


@pytest.mark.skipif(not HAS_ANYSTYLE, reason="anystyle not installed")
@pytest.mark.parametrize("style", BBL_STYLES)
def test_bbl_emission_wellformed(tmp_path, style):
    shutil.copy(FIX / f"{style}.bbl", tmp_path / "paper.bbl")
    block = references_block("", tmp_path)
    assert block.startswith(":references:")
    assert block.rstrip().endswith("::")
    emitted = {key for _, key in re.findall(r"^@(\w+)\{([^,]+),", block, re.M)}
    assert emitted == KEYS
    assert "\\newblock" not in block
    assert "~" not in block


def test_bib_emission_passthrough(tmp_path):
    shutil.copy(FIX / "refs.bib", tmp_path / "refs.bib")
    block = references_block(r"\bibliography{refs}", tmp_path)
    assert block.startswith(":references:")
    assert block.rstrip().endswith("::")
    assert "@article{shannon1948" in block
    assert "Mathematical Theory of Communication" in block
