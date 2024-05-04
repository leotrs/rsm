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

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-toggle"><span><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <polyline points="9 6 15 12 9 18"></polyline>
                </svg></span></div>

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-dots-vertical" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <circle cx="12" cy="12" r="1"></circle>
                <circle cx="12" cy="19" r="1"></circle>
                <circle cx="12" cy="5" r="1"></circle>
                </svg></span>
        <div class="options hide">

        <span class="option option__link"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-link" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M10 14a3.5 3.5 0 0 0 5 0l4 -4a3.5 3.5 0 0 0 -5 -5l-.5 .5"></path>
                <path d="M14 10a3.5 3.5 0 0 0 -5 0l-4 4a3.5 3.5 0 0 0 5 5l.5 -.5"></path>
                </svg></span>

        <span class="option option__tree"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-binary-tree" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M6 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M16 4a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M16 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M11 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M21 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M5.058 18.306l2.88 -4.606"></path>
                <path d="M10.061 10.303l2.877 -4.604"></path>
                <path d="M10.065 13.705l2.876 4.6"></path>
                <path d="M15.063 5.7l2.881 4.61"></path>
                </svg></span>

        <span class="option option__source"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-source-code" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M14.5 4h2.5a3 3 0 0 1 3 3v10a3 3 0 0 1 -3 3h-10a3 3 0 0 1 -3 -3v-5"></path>
                <path d="M6 5l-2 2l2 2"></path>
                <path d="M10 9l2 -2l-2 -2"></path>
                </svg></span>

        </div>
        </div>

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

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-toggle"><span><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <polyline points="9 6 15 12 9 18"></polyline>
                </svg></span></div>

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-dots-vertical" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <circle cx="12" cy="12" r="1"></circle>
                <circle cx="12" cy="19" r="1"></circle>
                <circle cx="12" cy="5" r="1"></circle>
                </svg></span>
        <div class="options hide">

        <span class="option option__link"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-link" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M10 14a3.5 3.5 0 0 0 5 0l4 -4a3.5 3.5 0 0 0 -5 -5l-.5 .5"></path>
                <path d="M14 10a3.5 3.5 0 0 0 -5 0l-4 4a3.5 3.5 0 0 0 5 5l.5 -.5"></path>
                </svg></span>

        <span class="option option__tree"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-binary-tree" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M6 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M16 4a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M16 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M11 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M21 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
                <path d="M5.058 18.306l2.88 -4.606"></path>
                <path d="M10.061 10.303l2.877 -4.604"></path>
                <path d="M10.065 13.705l2.876 4.6"></path>
                <path d="M15.063 5.7l2.881 4.61"></path>
                </svg></span>

        <span class="option option__source"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-source-code" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M14.5 4h2.5a3 3 0 0 1 3 3v10a3 3 0 0 1 -3 3h-10a3 3 0 0 1 -3 -3v-5"></path>
                <path d="M6 5l-2 2l2 2"></path>
                <path d="M10 9l2 -2l-2 -2"></path>
                </svg></span>

        </div>
        </div>

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
