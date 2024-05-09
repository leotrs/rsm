from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        All $X$ are $Y$.

        ::

        :proof:

        :step: Axiom.::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="theorem" data-nodeid="1">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph" data-nodeid="2">All <span class="math" data-nodeid="4">\(X\)</span> are <span class="math" data-nodeid="7">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="proof" data-nodeid="10">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step last" data-nodeid="11">

        <div class="statement" data-nodeid="12">

        <p class="paragraph" data-nodeid="13">Axiom.</p>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_empty_proof():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        Theorem contents.

        ::

        :proof:

        ::


        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="theorem" data-nodeid="1">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph" data-nodeid="2">Theorem contents.</p>

        </div>

        </div>

        <div class="proof" data-nodeid="4">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_sub_step():
    compare_have_want(
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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="proof" data-nodeid="1">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step last" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Top level step.</p>

        </div>

        <div class="subproof" data-nodeid="6">

        <div class="subproof-contents">

        <div class="step" data-nodeid="7">

        <div class="statement" data-nodeid="8">

        <p class="paragraph" data-nodeid="9">Sub-step.</p>

        </div>

        <div class="subproof" data-nodeid="11">

        <div class="subproof-contents">

        <p class="paragraph" data-nodeid="12">Sub-proof.</p>

        </div>

        </div>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_steps():
    compare_have_want(
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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="proof" data-nodeid="1">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">First step.</p>

        </div>

        </div>

        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Secon step.</p>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
