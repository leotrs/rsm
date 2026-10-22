import pytest

from rsmify import arxiv
from rsmify.arxiv import ArxivId


@pytest.mark.parametrize(
    "raw, base, version",
    [
        ("2401.12345", "2401.12345", None),
        ("2401.12345v3", "2401.12345", 3),
        ("math.GT/0309136", "math.GT/0309136", None),
        ("hep-th/9901001v2", "hep-th/9901001", 2),
        ("math/0211159", "math/0211159", None),
        ("https://arxiv.org/abs/2401.12345v2", "2401.12345", 2),
        ("https://arxiv.org/pdf/2401.12345", "2401.12345", None),
        ("  2401.12345v1  ", "2401.12345", 1),
    ],
)
def test_parse_id_accepts(raw, base, version):
    aid = arxiv.parse_id(raw)
    assert aid.base == base
    assert aid.version == version


@pytest.mark.parametrize(
    "raw",
    [
        "not-an-id",
        "",
        "http://evil.com/abs/2401.12345",
        "evil.com/abs/2401.12345",
        "arxiv.org/abs/",
        "2401",
        "12345.6789.0",
    ],
)
def test_parse_id_rejects(raw):
    with pytest.raises(ValueError):
        arxiv.parse_id(raw)


def test_canonical_requires_version():
    with pytest.raises(ValueError):
        ArxivId("2401.12345", None).canonical()
    assert ArxivId("2401.12345", 2).canonical() == "2401.12345v2"


def test_fetch_refuses_offsite_redirect(monkeypatch):
    # SSRF guard: a redirect that lands off the arXiv host allowlist is refused.
    class _URL:
        host = "evil.com"

    class _Resp:
        url = _URL()
        status_code = 200
        content = b"x"

    monkeypatch.setattr(arxiv.httpx, "get", lambda *a, **k: _Resp())
    with pytest.raises(arxiv.FetchError):
        arxiv.fetch_and_flatten(ArxivId("2401.12345", 1))
