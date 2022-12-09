from conftest import compare_have_want, compare_have_want_handrails


def test_simple_no_handrails():
    compare_have_want(
        have="""\
        :manuscript:

        :proof:

          :sketch: Foo.::

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="sketch">

        <p class="paragraph">Foo.</p>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph">Bar.</p>

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


def test_simple_with_handrails():
    compare_have_want_handrails(
        have="""\
        :manuscript:

        :proof:

          :sketch: Foo.::

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="proof">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        <span class="option option__assumptions">assumptions</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="proof__header">

        <p class="paragraph proof__title do-not-hide"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof__tabs">

        <button class="sketch active">sketch</button>

        <button class="full">full</button>

        </div>

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="sketch">

        <p class="paragraph">Foo.</p>

        </div>

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        <span class="option option__assumptions">assumptions</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>
        <div class="step__number">(1)</div>
        <div class="step last hide">

        <div class="statement">

        <p class="paragraph">Bar.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
