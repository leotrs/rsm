import pytest
from conftest import compare_have_want

import rsm


def test_no_reftext():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph has a hyperlink :url:https://www.apache.com::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph has a hyperlink <a href="https://www.apache.com">https://www.apache.com</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_custom_reftext():
    compare_have_want(
        have="""\
        :manuscript:

        This is a link to :url:https://www.apache.com, Apache::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a link to <a href="https://www.apache.com"> Apache</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_no_target():
    compare_have_want(
        have="""\
        :manuscript:

        This is a malformed url :url:::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a malformed url [CST error at (2, 24) - (2, 31)] .</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )

    compare_have_want(
        have="""\
        :manuscript:

        This is a malformed url with a space :url: ::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a malformed url with a space [CST error at (2, 37) - (2, 45)] .</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
