from conftest import compare_have_want


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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div id="eqn-plus" class="mathblock smallequation">
        $$
        2 + 2 = 4
        $$
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
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

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

        This paragraph contains inline math :math: {:label: bar, :types: {smallequation}} 2 + 2
        = 4::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">When <span class="math">\(a \ne 0\)</span>, there are two solutions to <span class="math">\(ax^2 + bx + c = 0\)</span> and they are</p>

        <div class="mathblock">
        $$
        x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
        $$
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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">This is some inline <span class="math">\(2+2=4\)</span> math.  And then some display math.</p>

        <div id="eqn-foo" class="mathblock">
        $$
        2+2=4
        $$
        </div>

        <p class="paragraph">And now we refer to <a class="reference" href="#eqn-foo">Equation 1</a>.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
