import pytest
import rsm
from conftest import compare_have_want


def test_reftext():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: First
          :label: sec-lbl

        Content of first.

        ::

        This is a paragraph that refers to :ref:sec-lbl::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section id="sec-lbl" class="section level-2">

        <h2>1. First</h2>

        <p class="paragraph">Content of first.</p>

        </section>

        <p class="paragraph">This is a paragraph that refers to <a class="reference" href="#sec-lbl">Section 1</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_overwrite_reftext():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: First
          :label: sec-lbl

        Content of first.

        ::

        This is a paragraph that refers to :ref:sec-lbl,The Section::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section id="sec-lbl" class="section level-2">

        <h2>1. First</h2>

        <p class="paragraph">Content of first.</p>

        </section>

        <p class="paragraph">This is a paragraph that refers to <a class="reference" href="#sec-lbl">The Section</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_ref_to_unknown_label(caplog):
    compare_have_want(
        have="""\
        :manuscript:

        :ref:foo::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="error">[unknown label "foo"]</span></p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert "Reference to nonexistent label" in caplog.text
