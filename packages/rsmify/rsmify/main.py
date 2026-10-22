"""rsmify FastAPI service (bead rsm-ddx.8).

The URL schema mirrors arxiv.org/abs/ so an arxiv.org URL converts to an rsmify
URL by swapping the host. A version-less request redirects to the resolved
versioned URL, which is served with immutable caching.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from . import arxiv, pipeline

app = FastAPI(
    title="rsmify",
    description="arXiv-to-RSM personal reader",
)

# A paper at a fixed version never changes, so the browser may keep it forever.
_IMMUTABLE = "public, max-age=31536000, immutable"


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/abs/{raw:path}", response_class=HTMLResponse)
def abs_page(raw: str, request: Request) -> HTMLResponse:
    try:
        arxiv_id = arxiv.parse_id(raw)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    if not arxiv_id.has_version:
        try:
            version = arxiv.resolve_latest_version(arxiv_id.base)
        except Exception as exc:
            raise HTTPException(status_code=502, detail=f"version lookup failed: {exc}")
        return RedirectResponse(
            url=f"/abs/{arxiv_id.base}v{version}", status_code=301
        )

    etag = f'"{arxiv_id.canonical()}"'
    if request.headers.get("if-none-match") == etag:
        return HTMLResponse(status_code=304, content="")

    try:
        tex_path = arxiv.fetch_and_flatten(arxiv_id)
    except arxiv.FetchError as exc:
        raise HTTPException(status_code=502, detail=f"arXiv fetch failed: {exc}")
    try:
        html = pipeline.convert(tex_path)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"conversion failed: {exc}")

    return HTMLResponse(
        content=html,
        headers={"Cache-Control": _IMMUTABLE, "ETag": etag},
    )
