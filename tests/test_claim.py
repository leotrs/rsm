from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: Section

        This pargraph contains a claim :claim: {:label: clm-lbl} all $X$ are $Y$ ::.

        ::

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section</h2>

        <p class="paragraph">This pargraph contains a claim <span id="clm-lbl" class="claim"><span class="keyword">⊢ </span>all <span class="math">\(X\)</span> are <span class="math">\(Y\)</span> </span>.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_with_math():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph has math inside a claim ⊢ $2+2=4$.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This paragraph has math inside a claim <span class="claim"><span class="keyword">⊢ </span><span class="math">\(2+2=4\)</span></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_lonely_claim():
    compare_have_want(
        have="""\
        :manuscript:

        ⊢ $2+2=4$.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="claim"><span class="keyword">⊢ </span><span class="math">\(2+2=4\)</span></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_claim_within_list():
    compare_have_want(
        have="""\
        :manuscript:

        We now make a bunch of claims
        :enumerate:

        :item: {:label: one} ⊢ $2+2=4$.

        :item: {:label: two} ⊢ $3+3=6$.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">We now make a bunch of claims
        </p>

        <ol class="enumerate">

        <li id="one" class="item">
        <span class="claim"><span class="keyword">⊢ </span><span class="math">\(2+2=4\)</span></span>.
        </li>

        <li id="two" class="item">
        <span class="claim"><span class="keyword">⊢ </span><span class="math">\(3+3=6\)</span></span>.
        </li>

        </ol>

        </section>

        </div>

        </div>

        </body>
        """,
    )
