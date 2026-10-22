import pytest
from fastapi.testclient import TestClient

from rsmify import arxiv, pipeline
from rsmify.main import app

client = TestClient(app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_malformed_id_returns_400():
    assert client.get("/abs/not-an-id").status_code == 400


def test_non_arxiv_host_returns_400():
    # The host-swap URL schema only recognizes arXiv ids, so a foreign host fails.
    assert client.get("/abs/evil.com/abs/2401.12345").status_code == 400


def test_versionless_redirects(monkeypatch):
    monkeypatch.setattr(arxiv, "resolve_latest_version", lambda base: 4)
    r = client.get("/abs/2401.12345", follow_redirects=False)
    assert r.status_code == 301
    assert r.headers["location"] == "/abs/2401.12345v4"


def test_versioned_renders_with_cache_headers(monkeypatch):
    monkeypatch.setattr(arxiv, "fetch_and_flatten", lambda aid: "/tmp/ignored.tex")
    monkeypatch.setattr(pipeline, "convert", lambda path: "<!DOCTYPE html><html></html>")
    r = client.get("/abs/2401.12345v2")
    assert r.status_code == 200
    assert "immutable" in r.headers["cache-control"]
    assert r.headers["etag"] == '"2401.12345v2"'
    assert "text/html" in r.headers["content-type"]


def test_conditional_request_returns_304(monkeypatch):
    # A matching ETag short-circuits before any fetch runs.
    def _boom(*a, **k):
        raise AssertionError("fetch must not run on the 304 path")

    monkeypatch.setattr(arxiv, "fetch_and_flatten", _boom)
    r = client.get("/abs/2401.12345v2", headers={"If-None-Match": '"2401.12345v2"'})
    assert r.status_code == 304


def test_conversion_failure_returns_502(monkeypatch):
    monkeypatch.setattr(arxiv, "fetch_and_flatten", lambda aid: "/tmp/ignored.tex")

    def _fail(path):
        raise RuntimeError("pandoc blew up")

    monkeypatch.setattr(pipeline, "convert", _fail)
    assert client.get("/abs/2401.12345v9").status_code == 502


@pytest.mark.network
def test_end_to_end_real_paper():
    r = client.get("/abs/math/0211159")  # resolves to v1, fetches, renders
    assert r.status_code == 200
    assert "braiid.css" in r.text
    assert r.text.lstrip()[:20].lower().startswith("<!doctype")
