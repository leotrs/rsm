import pytest
from conftest import compare_have_want_handrails


@pytest.mark.skip
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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

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


@pytest.mark.skip
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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <section class="section level-2">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

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


@pytest.mark.skip
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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="abstract">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

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


@pytest.mark.skip
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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="theorem">

        <div class="handrail handrail--offset stars-0 clocks-0">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="theorem-contents handrail__collapsible">

        <p class="paragraph theorem__title do-not-hide"><span class="span"><strong>Theorem 1.</strong></span></p>

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


@pytest.mark.skip
def test_proof():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :proof:

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="proof">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="proof__header">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1)</div>
        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


@pytest.mark.skip
def test_proof_with_sketch():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :proof:

          :sketch: Foo.::

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="proof">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="proof__header">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof__tabs">

        <button class="sketch active">sketch</button>

        <button class="full">full</button>

        </div>

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="sketch">

        <p class="paragraph">Foo.</p>

        </div>

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1)</div>
        <div class="step last hide">

        <div class="statement">

        <p class="paragraph">Bar.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


@pytest.mark.skip
def test_sub_step():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :proof:

          :step: Top level step.

            :step: Sub-step.

              :p: Sub-proof.::

            ::
          ::

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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="proof">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="proof__header">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1)</div>
        <div class="step last">

        <div class="statement">

        <p class="paragraph">Top level step.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents handrail handrail--hug handrail__collapsible">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1.1)</div>
        <div class="step">

        <div class="statement">

        <p class="paragraph">Sub-step.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents handrail handrail--hug handrail__collapsible">

        <p class="paragraph">Sub-proof.</p>

        </div>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


@pytest.mark.skip
def test_two_steps():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :proof:

          :step: First step.::

          :step: Secon step.::

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

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="proof">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="proof__header">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1)</div>
        <div class="step">

        <div class="statement">

        <p class="paragraph">First step.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(2)</div>
        <div class="step last">

        <div class="statement">

        <p class="paragraph">Secon step.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
