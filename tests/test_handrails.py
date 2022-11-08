import pytest
from conftest import compare_have_want_handrails


def test_manuscript():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        Hello.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h1></h1>

        </div>

        <p class="paragraph">Hello.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_section():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        # Title

        Hello.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h1></h1>

        </div>

        <section class="section level-2">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h2>1. Title</h2>

        </div>

        <p class="paragraph">Hello.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_abstract():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :abstract:

           This is the abstract.

        ::

        Hello.

        ::
        """,
        want="""\

        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h1></h1>

        </div>

        <div class="abstract">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h3>Abstract</h3>

        </div>

        <p class="paragraph">This is the abstract.</p>

        </div>

        <p class="paragraph">Hello.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_section():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :theorem:

           All $X$ are $Y$.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <h1></h1>

        </div>

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">
        bar
        </div>

        <div class="theorem">

        </div>

        <p class="paragraph"><span class="span"><strong>Theorem 1. </strong></span>All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )