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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <section class="section level-2">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="abstract">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

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


def test_theorem():
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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="theorem">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span></div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1. </strong></span></p>

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
