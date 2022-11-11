import pytest
import rsm
from conftest import compare_have_want


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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This paragraph has a hyperlink <a class="reference" href="https://www.apache.com">https://www.apache.com</a>.</p>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This is a link to <a class="reference" href="https://www.apache.com"> Apache</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_no_target():
    with pytest.raises(rsm.core.translator.RSMTranslatorError):
        compare_have_want(
            have="""\
        :manuscript:

        This is a malformed url :url:::.

        ::
        """,
            want='XXX',
        )

    with pytest.raises(rsm.core.translator.RSMTranslatorError):
        compare_have_want(
            have="""\
        :manuscript:

        This is a malformed url with a space :url: ::.

        ::
        """,
            want='XXX',
        )
