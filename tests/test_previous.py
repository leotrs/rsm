import pytest
import rsm
from conftest import compare_have_want


def test_works_with_no_reftext_and_label():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :step:
            :label: lbl
          Foo.
          ::

          :step: Bar :previous:1::.::

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

        <div id="lbl" class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Foo.</p>

        </div>

        </div>

        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Bar <a class="reference" href="#lbl">Step 1</a>.</p>

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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="proof" data-nodeid="1">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Foo.</p>

        </div>

        </div>

        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Bar <a class="reference" href="#">Step 1</a>.</p>

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

          :step:
            :label: lbl
          Foo.::

          :step: Bar :previous:1,bar::.::

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

        <div id="lbl" class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Foo.</p>

        </div>

        </div>

        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Bar <a class="reference" href="#lbl">bar</a>.</p>

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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="proof" data-nodeid="1">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Foo.</p>

        </div>

        </div>

        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Bar <a class="reference" href="#">bar</a>.</p>

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
