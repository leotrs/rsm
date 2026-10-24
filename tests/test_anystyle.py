import logging
import shutil

import pytest

from rsm import anystyle
from rsm.anystyle import structure
from rsm.bibextract import Reference

HAS_ANYSTYLE = shutil.which("anystyle") is not None


def _ref(key: str, text: str) -> Reference:
    return Reference(key, "bbl", text)


@pytest.mark.skipif(not HAS_ANYSTYLE, reason="anystyle not installed")
def test_structure_real_anystyle():
    refs = [
        _ref(
            "knuth",
            "Donald E. Knuth. The Art of Computer Programming. Addison-Wesley, 1968.",
        ),
        _ref(
            "torres",
            "Leo Torres, Kevin Chan. Nonbacktracking eigenvalues under node removal. "
            "SIAM Journal on Mathematics of Data Science, 2021.",
        ),
    ]
    out = structure(refs)
    assert [s.key for s in out] == ["knuth", "torres"]
    assert all(not s.is_verbatim for s in out)
    assert any("Art of Computer Programming" in t for t in out[0].fields["title"])
    assert out[0].fields.get("author")


def test_structure_mocked_fields(monkeypatch):
    monkeypatch.setattr(anystyle, "available", lambda: True)
    monkeypatch.setattr(
        anystyle,
        "_parse",
        lambda texts: [
            {
                "title": ["A Title"],
                "author": [{"family": "X"}],
                "date": ["2020"],
                "type": "article-journal",
            }
        ],
    )
    out = structure([_ref("a", "whatever")])
    assert not out[0].is_verbatim
    assert out[0].fields["type"] == "article-journal"


def test_below_floor_degrades_and_warns(monkeypatch, caplog):
    monkeypatch.setattr(anystyle, "available", lambda: True)
    monkeypatch.setattr(anystyle, "_parse", lambda texts: [{"title": ["Only a title"]}])
    caplog.set_level(logging.WARNING, logger="RSM")
    out = structure([_ref("lonely", "Only a title with no author or year")])
    assert out[0].is_verbatim
    assert any("lonely" in r.getMessage() for r in caplog.records)


def test_no_anystyle_degrades_all_with_one_warning(monkeypatch, caplog):
    monkeypatch.setattr(anystyle, "available", lambda: False)
    caplog.set_level(logging.WARNING, logger="RSM")
    out = structure([_ref("a", "x"), _ref("b", "y")])
    assert all(s.is_verbatim for s in out)
    summary = [r for r in caplog.records if "verbatim" in r.getMessage()]
    assert len(summary) == 1  # one summary line, not one per key


def test_parse_failure_degrades(monkeypatch):
    monkeypatch.setattr(anystyle, "available", lambda: True)
    monkeypatch.setattr(anystyle, "_parse", lambda texts: None)
    out = structure([_ref("a", "x")])
    assert out[0].is_verbatim


def test_empty():
    assert structure([]) == []
