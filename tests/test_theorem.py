from conftest import compare_have_want, compare_have_want_handrails


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        Theorem contents.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="theorem" data-nodeid="1">

        <p class="paragraph hr-label"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph" data-nodeid="2">Theorem contents.</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_multiple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        Theorem contents.

        ::

        :lemma:

        And a lemma.

        ::

        :theorem:

        Another theorem.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="theorem" data-nodeid="1">

        <p class="paragraph hr-label"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph" data-nodeid="2">Theorem contents.</p>

        </div>

        <div class="lemma theorem" data-nodeid="4">

        <p class="paragraph hr-label"><span class="span"><strong>Lemma 2.</strong></span></p>

        <p class="paragraph" data-nodeid="5">And a lemma.</p>

        </div>

        <div class="theorem" data-nodeid="7">

        <p class="paragraph hr-label"><span class="span"><strong>Theorem 3.</strong></span></p>

        <p class="paragraph" data-nodeid="8">Another theorem.</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
