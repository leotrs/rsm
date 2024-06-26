from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: Section

          This paragraph contains a claim :claim: {:label: clm-lbl}all $X$ are $Y$ ::.

        ::

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <p class="paragraph" data-nodeid="2">This paragraph contains a claim <span id="clm-lbl" class="construct claim" data-nodeid="4"><span class="keyword" data-nodeid="5">⊢ </span>all <span class="math" data-nodeid="8">\(X\)</span> are <span class="math" data-nodeid="11">\(Y\)</span></span>.</p>

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

        This paragraph has math inside a claim :claim: :math:2+2=4:: ::.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This paragraph has math inside a claim <span class="construct claim" data-nodeid="3"><span class="keyword" data-nodeid="4">⊢ </span><span class="math" data-nodeid="6">\(2+2=4\)</span></span>.</p>

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

        We now make a bunch of claims.

        :enumerate:

        :item: {:label: one} :claim: :math:2+2=4:: ::.

        :item: {:label: two} :claim: :math:3+3=6:: ::.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">We now make a bunch of claims.</p>

        <ol class="enumerate" data-nodeid="3">

        <li id="one" class="item" data-nodeid="4">
        <span class="construct claim" data-nodeid="5"><span class="keyword" data-nodeid="6">⊢ </span><span class="math" data-nodeid="8">\(2+2=4\)</span></span>.
        </li>

        <li id="two" class="item" data-nodeid="11">
        <span class="construct claim" data-nodeid="12"><span class="keyword" data-nodeid="13">⊢ </span><span class="math" data-nodeid="15">\(3+3=6\)</span></span>.
        </li>

        </ol>

        </section>

        </div>

        </div>

        </body>
        """,
    )
