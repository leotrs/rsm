import pytest
from conftest import compare_have_want

import rsm


def test_display_alone():
    compare_have_want(
        have="""\
        :manuscript:

        :mathblock:
          :label: eqn-plus
          :types: smallequation

          2 + 2 = 4
        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div id="eqn-plus" class="mathblock smallequation">
        $$
        2 + 2 = 4
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_no_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains inline math :math: 2 + 2 = 4::.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph contains inline math <span class="math">\(2 + 2 = 4\)</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_with_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains inline math :math: {:label: bar, :types: smallequation} 2 + 2
        = 4::.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph contains inline math <span id="bar" class="math smallequation">\(2 + 2
        = 4\)</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_with_shortcuts():
    compare_have_want(
        have=r"""        :manuscript:

        # My Section

        When $a \ne 0$, there are two solutions to $ax^2 + bx + c = 0$ and they are

        $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <section class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">When <span class="math">\(a \ne 0\)</span>, there are two solutions to <span class="math">\(ax^2 + bx + c = 0\)</span> and they are</p>

        <div class="mathblock">
        $$
        x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
        $$
        <div class="mathblock__number">(1.1)</div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_ref():
    compare_have_want(
        have=r"""        :manuscript:

        # My Section

        This is some inline $2+2=4$ math.  And then some display math.

        :mathblock:
          :label: eqn-foo
          2+2=4
        ::

        And now we refer to :ref:eqn-foo::.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <section class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">This is some inline <span class="math">\(2+2=4\)</span> math.  And then some display math.</p>

        <div id="eqn-foo" class="mathblock">
        $$
        2+2=4
        $$
        <div class="mathblock__number">(1.1)</div>

        </div>

        <p class="paragraph">And now we refer to <a class="reference" href="#eqn-foo">(1.1)</a>.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_mathblock_nonum():
    compare_have_want(
        have=r"""        :manuscript:

        :mathblock:
          :nonum:
          2+2=4
        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="mathblock">
        $$
        2+2=4
        $$
        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_mathblock_nonum_with_shortcut():
    compare_have_want(
        have=r"""        :manuscript:

        $$
          :nonum:
          2+2=4
        $$

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="mathblock">
        $$
        2+2=4
        $$
        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_unclosed_dollar_sign():
    compare_have_want(
        have=r"""        :manuscript:

        There are three dollar signs here $2+2 $= 0$.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">There are three dollar signs here <span class="math">\(2+2\)</span>= 0 [CST error at (2, 43) - (2, 44)] .</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_mathblock_isclaim():
    compare_have_want(
        have="""
        :manuscript:

        $$
        :isclaim:
          2+2 = 4
        $$

        :mathblock:
        :isclaim:
          2+2 = 4
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="claimblock">
        <span class="keyword">⊢ </span>
        <div class="mathblock">
        $$
        2+2 = 4
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </div>

        <div class="claimblock">
        <span class="keyword">⊢ </span>
        <div class="mathblock">
        $$
        2+2 = 4
        $$
        <div class="mathblock__number">(2)</div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
