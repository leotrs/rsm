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
        foo
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
