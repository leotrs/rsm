import pytest
import rsm
from conftest import compare_have_want


def test_no_reftext():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph has a hyperlink :url:www.apache.com::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This paragraph has a hyperlink <a class="reference" href="www.apache.com">www.apache.com</a>.</p>

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

        This is a link to :url:www.apache.com, Apache::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This is a link to <a class="reference" href="www.apache.com"> Apache</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_no_target():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
        :manuscript:

        This is a malformed url :url::.

        ::
        """,
            want='XXX',
        )
