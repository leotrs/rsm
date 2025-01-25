from conftest import compare_have_want, compare_have_want_handrails


def test_simple_no_handrails():
    compare_have_want(
        have="""\
        :manuscript:

        :sketch: Foo.::

        :proof:

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="sketch" data-nodeid="1">

        <div class="paragraph hr-label">

        <p><span class="span"><strong>Proof sketch.</strong></span></p>

        </div>

        <div class="paragraph" data-nodeid="2">

        <p>Foo.</p>

        </div>

        </div>

        <div class="proof" data-nodeid="4">

        <div class="paragraph hr-label">

        <p><span class="span"><strong>Proof. </strong></span></p>

        </div>

        <div class="step last" data-nodeid="5">

        <div class="statement" data-nodeid="6">

        <div class="paragraph" data-nodeid="7">

        <p>Bar.</p>

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
