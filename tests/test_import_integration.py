"""End-to-end tests for the assembled import path (app.import_project).

These exercise resolve -> pandoc -> drop pandoc's bibliography -> append the
real one, the one function the `rsm import` CLI and rsmify both call. They need
pandoc; the structured output needs AnyStyle, so they assert the parts that
hold either way (the key is present, pandoc's collapsed copy is gone).
"""

import shutil

import pytest

from rsm import app

HAS_PANDOC = shutil.which("pandoc") is not None

pytestmark = pytest.mark.skipif(not HAS_PANDOC, reason="pandoc not installed")

_INLINE = r"""\documentclass{article}
\begin{document}
We build on prior work \cite{knuth}.
\begin{thebibliography}{9}
\bibitem{knuth} Donald E. Knuth. The Art of Computer Programming. Addison-Wesley, 1968.
\end{thebibliography}
\end{document}
"""


def test_import_project_inline_bibliography(tmp_path):
    (tmp_path / "main.tex").write_text(_INLINE, encoding="utf-8")
    out = app.import_project(str(tmp_path))
    body, sep, refs = out.partition(":references:")
    assert sep, "no :references: block emitted"
    assert ":cite:knuth::" in body
    assert "knuth" in refs
    # pandoc's collapsed copy is suppressed: the reference text appears only in
    # our block, never in the body.
    assert "Art of Computer Programming" in refs
    assert "Art of Computer Programming" not in body


def test_import_project_bib_passthrough(tmp_path):
    (tmp_path / "main.tex").write_text(
        r"\documentclass{article}" "\n\\begin{document}\n\\cite{k}\n"
        r"\bibliography{refs}" "\n\\end{document}\n",
        encoding="utf-8",
    )
    (tmp_path / "refs.bib").write_text(
        "@book{k, title={A Passthrough Book}, author={Writer, A}, year={2000}}",
        encoding="utf-8",
    )
    out = app.import_project(str(tmp_path))
    _body, sep, refs = out.partition(":references:")
    assert sep
    assert "@book{k" in refs
    assert "A Passthrough Book" in refs


def test_import_project_single_tex_file(tmp_path):
    f = tmp_path / "paper.tex"
    f.write_text(_INLINE, encoding="utf-8")
    out = app.import_project(str(f))
    assert ":cite:knuth::" in out
    assert ":references:" in out
