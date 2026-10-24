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


_XREF = r"""\documentclass{article}
\newtheorem{theorem}{Theorem}
\begin{document}
\section{Intro}\label{sec:intro}
See Section~\ref{sec:intro}.
\begin{equation}\label{eq:e}
E = mc^2
\end{equation}
By \eqref{eq:e}.
\begin{theorem}\label{thm:main}
A statement.
\end{theorem}
See Theorem~\ref{thm:main}.
\end{document}
"""


_MACROS = r"""\documentclass{article}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\abs}[1]{\lvert #1 \rvert}
\DeclareMathOperator{\argmin}{arg\,min}
\begin{document}
\section{Body}
Text $x \in \RR$ and $\abs{y}$ and $\argmin f$.
\end{document}
"""


def test_import_project_emits_preamble_macros(tmp_path):
    import rsm

    (tmp_path / "main.tex").write_text(_MACROS, encoding="utf-8")
    out = app.import_project(str(tmp_path))
    # the preamble's macro definitions carry into RSM's hidden preamble block,
    # so Temml can expand any macro pandoc left raw in the math.
    assert ":mathblock: {:preamble:}" in out
    assert "\\newcommand{\\RR}{\\mathbb{R}}" in out
    assert "\\newcommand{\\abs}[1]{\\lvert #1 \\rvert}" in out
    # \DeclareMathOperator is translated to a Temml-safe \newcommand.
    assert "\\newcommand{\\argmin}{\\operatorname{arg\\,min}}" in out
    # placed so the document still renders, with the math-preamble class.
    html = rsm.render(out, handrails=False, source_offsets=False)
    assert "math-preamble" in html


def test_import_project_crossrefs(tmp_path):
    import rsm

    (tmp_path / "main.tex").write_text(_XREF, encoding="utf-8")
    out = app.import_project(str(tmp_path))
    # Every section, equation, and theorem gets a plain generated label.
    assert ":label: sec-1" in out
    assert ":label: eqn-1" in out
    assert ":label: thm-1" in out
    # \ref, \eqref, and \ref to the theorem resolve to those generated labels.
    assert ":ref:sec-1::" in out
    assert ":ref:eqn-1::" in out
    assert ":ref:thm-1::" in out
    # The result renders with resolvable labels.
    html = rsm.render(out, handrails=False, source_offsets=False)
    assert 'id="sec-1"' in html
    assert 'id="eqn-1"' in html
    assert 'id="thm-1"' in html
