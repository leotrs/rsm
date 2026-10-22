import pytest
from fastapi.testclient import TestClient

from rsmify import arxiv, main, pipeline
from rsmify.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def _reset_inflight():
    # The in-flight counter is module-level; isolate tests.
    main._inflight = 0
    yield


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_malformed_id_returns_400():
    r = client.get("/r/not-an-id")
    assert r.status_code == 400
    assert "text/html" in r.headers["content-type"]  # a readable page, not JSON
    assert "arXiv" in r.text


def test_non_arxiv_host_returns_400():
    assert client.get("/r/evil.com/abs/2401.12345").status_code == 400


def test_versionless_redirects(monkeypatch):
    monkeypatch.setattr(arxiv, "resolve_latest_version", lambda base: 4)
    r = client.get("/r/2401.12345", follow_redirects=False)
    assert r.status_code == 302  # 302, not 301: "latest" changes over time
    assert r.headers["location"] == "/r/2401.12345v4"


def test_versioned_renders_with_cache_headers(monkeypatch):
    monkeypatch.setattr(arxiv, "fetch_and_flatten", lambda aid: "/tmp/ignored.tex")
    monkeypatch.setattr(pipeline, "convert", lambda path: "<!DOCTYPE html><html></html>")
    r = client.get("/r/2401.12345v2")
    assert r.status_code == 200
    assert "immutable" in r.headers["cache-control"]
    assert r.headers["etag"] == '"2401.12345v2"'
    assert "text/html" in r.headers["content-type"]


def test_conditional_request_returns_304(monkeypatch):
    def _boom(*a, **k):
        raise AssertionError("fetch must not run on the 304 path")

    monkeypatch.setattr(arxiv, "fetch_and_flatten", _boom)
    r = client.get("/r/2401.12345v2", headers={"If-None-Match": '"2401.12345v2"'})
    assert r.status_code == 304


def test_conversion_failure_shows_page(monkeypatch):
    monkeypatch.setattr(arxiv, "fetch_and_flatten", lambda aid: "/tmp/ignored.tex")

    def _fail(path):
        raise RuntimeError("pandoc blew up")

    monkeypatch.setattr(pipeline, "convert", _fail)
    r = client.get("/r/2401.12345v9")
    assert r.status_code == 502
    assert "text/html" in r.headers["content-type"]
    assert "could not convert" in r.text.lower()


def test_fetch_error_shows_page(monkeypatch):
    def _no_source(aid):
        raise arxiv.FetchError("rsmify found no LaTeX source.", status=422)

    monkeypatch.setattr(arxiv, "fetch_and_flatten", _no_source)
    r = client.get("/r/2401.12345v1")
    assert r.status_code == 422
    assert "text/html" in r.headers["content-type"]
    assert "No LaTeX source" in r.text  # the heading for a 422


@pytest.mark.network
def test_end_to_end_real_paper():
    r = client.get("/r/math/0211159")  # resolves to v1, fetches, renders
    assert r.status_code == 200
    assert "braiid.css" in r.text
    assert r.text.lstrip()[:20].lower().startswith("<!doctype")
