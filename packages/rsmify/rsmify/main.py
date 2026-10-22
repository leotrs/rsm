"""rsmify host service (beads rsm-ddx.8, .9, .12).

Serves arXiv papers rendered through RSM at /r/<arxiv-id>. A version-less id
302-redirects to the resolved versioned URL, served with an immutable ETag so
the browser (and a CDN, when one fronts aris.pub) caches it. There is no
server-side cache store by design (bead rsm-ddx.8).

The endpoint is public and does real work per request, so it is bounded: at
most _MAX_CONCURRENT conversions run at once (others get 503), and each has a
wall-clock budget (then 504). Every failure renders a readable page, never a
bare status code or a JSON error.
"""

from __future__ import annotations

import asyncio
import html

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from . import arxiv, pipeline

app = FastAPI(title="rsmify", description="arXiv-to-RSM reader")

# A paper at a fixed version never changes, so the browser (and a CDN) may keep
# it forever.
_IMMUTABLE = "public, max-age=31536000, immutable"

_MAX_CONCURRENT = 2
_CONVERT_TIMEOUT_S = 90

_inflight = 0
_inflight_lock = asyncio.Lock()

_ERROR_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>rsmify</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ margin:0; min-height:100vh; box-sizing:border-box; display:flex;
    align-items:center; justify-content:center; padding:2rem;
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    background:#fafafa; color:#1a1a1a; }}
  @media (prefers-color-scheme:dark) {{ body {{ background:#121212; color:#e8e8e8; }} }}
  main {{ max-width:34rem; }}
  .tag {{ font-size:.8rem; letter-spacing:.08em; text-transform:uppercase; opacity:.5; }}
  h1 {{ font-size:1.5rem; margin:.3rem 0 .75rem; line-height:1.25; }}
  p {{ margin:.5rem 0; }}
  .hint {{ opacity:.7; font-size:.95rem; }}
  code {{ background:rgba(128,128,128,.18); padding:.1em .4em; border-radius:4px;
    font-size:.9em; }}
</style>
</head>
<body>
  <main>
    <div class="tag">rsmify</div>
    <h1>{heading}</h1>
    <p>{message}</p>
    {hint}
  </main>
</body>
</html>
"""

# Headings for the FetchError statuses that arxiv.py raises.
_FETCH_HEADINGS = {
    404: "Not on arXiv",
    413: "This paper is too large",
    422: "No LaTeX source",
}


def _error_page(status: int, heading: str, message: str, hint: str = "") -> HTMLResponse:
    hint_html = f'<p class="hint">{html.escape(hint)}</p>' if hint else ""
    page = _ERROR_TEMPLATE.format(
        heading=html.escape(heading), message=message, hint=hint_html
    )
    return HTMLResponse(content=page, status_code=status)


def _convert(arxiv_id: arxiv.ArxivId) -> str:
    tex_path = arxiv.fetch_and_flatten(arxiv_id)
    return pipeline.convert(tex_path)


async def _guarded_convert(arxiv_id: arxiv.ArxivId) -> str:
    global _inflight
    try:
        return await asyncio.to_thread(_convert, arxiv_id)
    finally:
        async with _inflight_lock:
            _inflight -= 1


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/r/{raw:path}", response_class=HTMLResponse)
async def read_paper(raw: str, request: Request) -> HTMLResponse:
    global _inflight
    try:
        arxiv_id = arxiv.parse_id(raw)
    except ValueError:
        return _error_page(
            400,
            "That is not an arXiv paper",
            # raw is user input, so escape it before reflecting it into the page.
            f"rsmify did not recognize <code>{html.escape(raw)}</code> as an arXiv id.",
            "Try a link like arxiv.org/abs/2401.12345, or just the id 2401.12345.",
        )

    if not arxiv_id.has_version:
        try:
            version = await asyncio.to_thread(
                arxiv.resolve_latest_version, arxiv_id.base
            )
        except Exception:
            return _error_page(
                502,
                "Could not reach arXiv",
                "rsmify could not look up the latest version of this paper.",
                "Try again in a moment.",
            )
        # 302, not 301: the latest version changes when arXiv posts a new one.
        return RedirectResponse(url=f"/r/{arxiv_id.base}v{version}", status_code=302)

    etag = f'"{arxiv_id.canonical()}"'
    if request.headers.get("if-none-match") == etag:
        return HTMLResponse(status_code=304, content="")

    async with _inflight_lock:
        if _inflight >= _MAX_CONCURRENT:
            return _error_page(
                503,
                "rsmify is busy",
                "Too many papers are being converted right now.",
                "Reload in a few seconds.",
            )
        _inflight += 1

    # Shield so a client timeout does not try to cancel the conversion thread
    # (it cannot be cancelled): it finishes and frees its slot in the background.
    task = asyncio.create_task(_guarded_convert(arxiv_id))
    try:
        rendered = await asyncio.wait_for(asyncio.shield(task), _CONVERT_TIMEOUT_S)
    except asyncio.TimeoutError:
        return _error_page(
            504,
            "Still converting",
            "This paper is taking a while to convert.",
            "Try again shortly. Very large papers may not finish.",
        )
    except arxiv.FetchError as exc:
        return _error_page(
            exc.status,
            _FETCH_HEADINGS.get(exc.status, "Could not fetch this paper"),
            html.escape(str(exc)),
        )
    except Exception:
        return _error_page(
            502,
            "Could not render this paper",
            "rsmify fetched the source but could not convert it to RSM.",
            "The importer is still rough, and some papers do not make it through yet.",
        )

    return HTMLResponse(
        content=rendered, headers={"Cache-Control": _IMMUTABLE, "ETag": etag}
    )
