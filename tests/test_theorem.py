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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">Theorem contents.</p>

        </div>

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

        :theorem:

        Theorem contents.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <div class="handrail handrail--offset">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <h1></h1>

        </div>

        <div class="theorem">

        <div class="handrail handrail--offset stars-0 clocks-0">

        <div class="handrail__btn-container">

        <div class="handrail__btn handrail__btn-menu handrail__btn--relative"><span>⋮</span>
        <div class="options hide">

        <span class="option option__link">link</span>

        <span class="option option__tree">tree</span>

        <span class="option option__source">source</span>

        </div>
        </div>

        <div class="handrail__btn handrail__btn-toggle"><span>〉</span></div>

        </div>

        <div class="theorem-contents handrail__collapsible">

        <p class="paragraph theorem__title do-not-hide"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">Theorem contents.</p>

        </div>

        </div>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">Theorem contents.</p>

        </div>

        </div>

        <div class="lemma theorem">

        <div class="theorem-contents lemma-contents">

        <p class="paragraph theorem__title lemma__title"><span class="span"><strong>Lemma 2.</strong></span></p>

        <p class="paragraph">And a lemma.</p>

        </div>

        </div>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 3.</strong></span></p>

        <p class="paragraph">Another theorem.</p>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
