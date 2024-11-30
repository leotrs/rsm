import pytest
from conftest import compare_have_want_handrails


def test_manuscript():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        Hello.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <p class="paragraph" data-nodeid="1">Hello.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_section():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        # Title

          Hello.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <section class="section level-2" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h2>1. Title</h2>

        </div>

        <p class="paragraph" data-nodeid="2">Hello.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_abstract():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :abstract:

          This is the abstract.

        ::

        Hello.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="abstract" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h3>Abstract</h3>

        </div>

        <p class="paragraph" data-nodeid="2">This is the abstract.</p>

        </div>

        <p class="paragraph" data-nodeid="4">Hello.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_theorem():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :theorem:

          All $X$ are $Y$.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="theorem" data-nodeid="1">

        <div class="handrail handrail--offset stars-0 clocks-0" tabindex=0>

        <div class="handrail__btn-container">

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

        <div class="theorem-contents handrail__collapsible">

        <p class="paragraph theorem__title do-not-hide"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph" data-nodeid="2">All <span class="math" data-nodeid="4">\(X\)</span> are <span class="math" data-nodeid="7">\(Y\)</span>.</p>

        </div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_proof():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

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

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="proof" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step last" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Bar.</p>

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


def test_proof_with_sketch():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :proof:

          :sketch: Foo.::

          :step: Bar.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="proof" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <div class="sketch" data-nodeid="2">

        <p class="paragraph" data-nodeid="3">Foo.</p>

        </div>

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step last hide" data-nodeid="5">

        <div class="statement" data-nodeid="6">

        <p class="paragraph" data-nodeid="7">Bar.</p>

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


def test_sub_step():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :proof:

          :step: Top level step.

            :step: Sub-step.

              :p: Sub-proof.::

            ::
          ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="proof" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step last" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">Top level step.</p>

        </div>

        <div class="subproof" data-nodeid="6">

        <div class="subproof-contents handrail handrail--hug handrail__collapsible">

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step__number">(1.1)</div>
        <div class="step" data-nodeid="7">

        <div class="statement" data-nodeid="8">

        <p class="paragraph" data-nodeid="9">Sub-step.</p>

        </div>

        <div class="subproof" data-nodeid="11">

        <div class="subproof-contents handrail handrail--hug handrail__collapsible">

        <p class="paragraph" data-nodeid="12">Sub-proof.</p>

        </div>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        </div>

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


def test_two_steps():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :proof:

          :step: First step.::

          :step: Secon step.::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        <h1>Some Title</h1>

        </div>

        <div class="proof" data-nodeid="1">

        <div class="handrail handrail--offset" tabindex=0>

        <div class="handrail__btn-container">

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

        </div>

        <div class="proof-contents handrail__collapsible">

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step" data-nodeid="2">

        <div class="statement" data-nodeid="3">

        <p class="paragraph" data-nodeid="4">First step.</p>

        </div>

        </div>

        <div class="halmos hide"></div>

        </div>

        <div class="handrail handrail--offset handrail__collapsible" tabindex=0>

        <div class="handrail__btn-container">

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
        <div class="step__number">(2)</div>
        <div class="step last" data-nodeid="6">

        <div class="statement" data-nodeid="7">

        <p class="paragraph" data-nodeid="8">Secon step.</p>

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


def test_unnumbered_mathblock_no_phantom_number():
    compare_have_want_handrails(
        have="""
        :manuscript:

        $$
        :nonum:
          3 + 3 = 6
        $$

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="mathblock" data-nodeid="1">
        $$
        3 + 3 = 6
        $$
        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_mathblock_phantom_number():
    compare_have_want_handrails(
        have="""
        :manuscript:

        $$
        3 + 3 = 6
        $$

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="mathblock" data-nodeid="1">

        <div class="mathblock__number mathblock__number--phantom">(1)</div>
        $$
        3 + 3 = 6
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
