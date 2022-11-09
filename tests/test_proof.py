from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        All $X$ are $Y$.

        ::

        :proof:

        :step: Axiom. ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents handrail__collapsible">

        <p class="paragraph theorem__title do-not-hide"><span class="span"><strong>Theorem 1. </strong></span></p>

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="proof">

        <div class="proof-contents handrail__collapsible">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        <div class="step last">

        <p class="paragraph">Axiom. </p>

        </div>

        </div>

        <div class="tombstone"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
