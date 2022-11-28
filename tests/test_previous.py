import pytest
import rsm
from conftest import compare_have_want


def test_works_with_no_reftext_and_label():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :step: {:label: lbl} Foo.::

          :step: Bar :previous:1::.::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div id="lbl" class="step">

        <div class="statement">

        <p class="paragraph">Foo.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar <a class="reference" href="#lbl">Step 1</a>.</p>

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


def test_works_with_no_reftext_and_no_label():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :step: Foo.::

          :step: Bar :previous:1::.::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step">

        <div class="statement">

        <p class="paragraph">Foo.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar <a class="reference" href="#">Step 1</a>.</p>

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


def test_works_with_reftext_and_label():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :step: {:label: lbl} Foo.::

          :step: Bar :previous:1,bar::.::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div id="lbl" class="step">

        <div class="statement">

        <p class="paragraph">Foo.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar <a class="reference" href="#lbl">bar</a>.</p>

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


def test_works_with_reftext_and_no_label():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :step: Foo.::

          :step: Bar :previous:1,bar::.::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step">

        <div class="statement">

        <p class="paragraph">Foo.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar <a class="reference" href="#">bar</a>.</p>

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


def test_previous_outside_step():
    with pytest.raises(rsm.transformer.RSMTransformerError):
        compare_have_want(
            have="""\
            :manuscript:

            Foo :previous:1,bar::.

            ::
            """,
            want="X",
        )
