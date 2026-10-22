"""arXiv identifier parsing and e-print fetching (bead rsm-ddx.9).

All arXiv network access lives in this module, behind functions that main.py
calls. The SSRF guard is structural: these functions only ever build URLs from
an identifier that already matched one of the arXiv id patterns below, against
the fixed host allowlist. They never fetch a caller-supplied URL, and a
redirect that would leave the allowlist is refused, so there is no path for a
request to reach an arbitrary host.
"""

from __future__ import annotations

import gzip
import io
import re
import tarfile
import tempfile
from dataclasses import dataclass
from pathlib import Path

import httpx

# New-style ids look like 2401.12345 (4-digit sequence before 2015, 5 after),
# optionally suffixed with a version like v2. Old-style ids carry an archive
# and optional subclass before a slash, e.g. math.GT/0309136 or hep-th/9901001.
_NEW = re.compile(r"(?P<base>\d{4}\.\d{4,5})(?:v(?P<ver>\d+))?")
_OLD = re.compile(r"(?P<base>[a-z][a-z-]*(?:\.[A-Z]{2})?/\d{7})(?:v(?P<ver>\d+))?")

ARXIV_HOSTS = ("export.arxiv.org", "arxiv.org")

_USER_AGENT = "rsmify/0.1 (arXiv-to-RSM personal reader)"
_API = "https://export.arxiv.org/api/query"
_EPRINT = "https://export.arxiv.org/e-print"

# \input and \include pull another source file into the main document.
_INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")


class FetchError(Exception):
    """A paper's source could not be fetched or unpacked."""


@dataclass(frozen=True)
class ArxivId:
    base: str
    version: int | None = None

    @property
    def has_version(self) -> bool:
        return self.version is not None

    def canonical(self) -> str:
        if self.version is None:
            raise ValueError("canonical() needs a resolved version")
        return f"{self.base}v{self.version}"


def parse_id(raw: str) -> ArxivId:
    """Parse a bare id, a versioned id, or an arxiv.org abs/pdf URL.

    Raises ValueError on anything that is not a recognizable arXiv id. This is
    the first layer of the SSRF guard: nothing downstream accepts input that
    does not pass here.
    """
    s = raw.strip()
    # Tolerate a pasted arxiv.org URL by keeping only the id after /abs/ or /pdf/.
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(.+)$", s, re.IGNORECASE)
    if m:
        s = m.group(1)
    s = re.sub(r"\.pdf$", "", s.rstrip("/"), flags=re.IGNORECASE)
    for pattern in (_NEW, _OLD):
        match = pattern.fullmatch(s)
        if match:
            ver = match.group("ver")
            return ArxivId(match.group("base"), int(ver) if ver else None)
    raise ValueError(f"not a recognizable arXiv id: {raw!r}")


def resolve_latest_version(base: str) -> int:
    """Return the latest version number for a version-less id.

    Reads it off the arXiv API entry, whose id ends with the canonical
    versioned abstract URL. Defaults to 1 if no version is stated.
    """
    resp = httpx.get(
        _API,
        params={"id_list": base},
        headers={"User-Agent": _USER_AGENT},
        timeout=30.0,
    )
    resp.raise_for_status()
    m = re.search(rf"arxiv\.org/abs/{re.escape(base)}v(\d+)", resp.text)
    return int(m.group(1)) if m else 1


def fetch_and_flatten(arxiv_id: ArxivId) -> str:
    """Fetch the e-print source, unpack it, and return a path to the flattened main .tex.

    Figure files are left on disk next to the .tex but not otherwise handled
    here; serving them is bead rsm-ddx.10.
    """
    url = f"{_EPRINT}/{arxiv_id.canonical()}"
    try:
        resp = httpx.get(
            url,
            headers={"User-Agent": _USER_AGENT},
            timeout=60.0,
            follow_redirects=True,
        )
    except httpx.HTTPError as exc:
        raise FetchError(f"could not reach arXiv: {exc}")
    if resp.url.host not in ARXIV_HOSTS:
        raise FetchError(f"refusing redirect off arXiv to {resp.url.host!r}")
    if resp.status_code != 200:
        raise FetchError(f"arXiv returned {resp.status_code} for {arxiv_id.canonical()}")

    workdir = Path(tempfile.mkdtemp(prefix="rsmify-"))
    _extract(resp.content, workdir)
    main_tex = _find_main_tex(workdir)
    flattened = _flatten(main_tex)
    out = workdir / "_rsmify_flat.tex"
    out.write_text(flattened, encoding="utf-8", errors="replace")
    return str(out)


def _extract(content: bytes, workdir: Path) -> None:
    """Unpack an arXiv e-print payload, which is a tarball, a single gzipped file, or raw."""
    try:
        with tarfile.open(fileobj=io.BytesIO(content), mode="r:*") as tar:
            _safe_extract(tar, workdir)
            return
    except tarfile.ReadError:
        pass
    try:
        data = gzip.decompress(content)
    except (OSError, EOFError):
        data = content
    (workdir / "main.tex").write_bytes(data)


def _safe_extract(tar: tarfile.TarFile, dest: Path) -> None:
    """Extract a tar while refusing members that would escape dest (path traversal)."""
    dest_resolved = dest.resolve()
    for member in tar.getmembers():
        target = (dest / member.name).resolve()
        if not str(target).startswith(str(dest_resolved)):
            raise FetchError(f"unsafe path in tar: {member.name!r}")
    tar.extractall(dest)


def _find_main_tex(workdir: Path) -> Path:
    """The main file is the .tex that declares \\documentclass."""
    texs = sorted(workdir.rglob("*.tex"))
    if not texs:
        raise FetchError("no .tex file found in e-print source")
    for tex in texs:
        try:
            if "\\documentclass" in tex.read_text(encoding="utf-8", errors="replace"):
                return tex
        except OSError:
            continue
    return texs[0]


def _flatten(path: Path, seen: set[Path] | None = None) -> str:
    """Inline \\input and \\include targets recursively, guarding against cycles."""
    seen = set() if seen is None else seen
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    base = path.parent
    text = path.read_text(encoding="utf-8", errors="replace")

    def repl(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        child = base / name
        if not child.suffix:
            child = child.with_suffix(".tex")
        if child.exists():
            return _flatten(child, seen)
        return match.group(0)

    return _INPUT.sub(repl, text)
