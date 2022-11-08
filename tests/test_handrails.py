import pytest
from conftest import compare_have_want_handrails as compare


def test_manuscript():
    compare(
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
