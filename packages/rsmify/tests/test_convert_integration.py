"""End-to-end test for rsmify's slimmed conversion, without the network.

Builds the kind of payload arxiv.fetch writes (a gzipped tar e-print) and runs
it through pipeline.convert, which delegates to rsm-lang. Needs pandoc; the
bibliography renders whether or not AnyStyle is present (verbatim fallback).
"""

import gzip
import io
import shutil
import tarfile

import pytest

from rsmify import pipeline

HAS_PANDOC = shutil.which("pandoc") is not None

_MAIN = (
    "\\documentclass{article}\n"
    "\\begin{document}\n"
    "We cite \\cite{k} and include a section. \\input{sec}\n"
    "\\begin{thebibliography}{9}\n"
    "\\bibitem{k} A. Writer. A Distinctive Title. Venue, 2001.\n"
    "\\end{thebibliography}\n"
    "\\end{document}\n"
)
_SEC = "Distinctive included body text."


def _gzipped_tar_eprint(path):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tar:
        for name, data in {"main.tex": _MAIN, "sec.tex": _SEC}.items():
            b = data.encode()
            info = tarfile.TarInfo(name)
            info.size = len(b)
            tar.addfile(info, io.BytesIO(b))
    path.write_bytes(gzip.compress(buf.getvalue()))


@pytest.mark.skipif(not HAS_PANDOC, reason="pandoc not installed")
def test_convert_local_eprint_to_html(tmp_path):
    payload = tmp_path / "eprint.gz"
    _gzipped_tar_eprint(payload)
    html = pipeline.convert(str(payload))
    assert html.lstrip().lower().startswith("<!doctype html>")
    # the \input was flattened into the document
    assert "Distinctive included body text." in html
    # the bibliography reached the page
    assert "A Distinctive Title" in html
