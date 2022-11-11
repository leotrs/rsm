import pytest
import rsm
from rsm.util import EscapedString
from conftest import compare_have_want


def test_ignore_single_char():
    esc = EscapedString(r'\:', ':')
    assert esc.find(':') == -1


def test_simple_not_escaped():
    with pytest.raises(ValueError):
        compare_have_want(
            have="""
            :manuscript:

            Warning: this is a warning.

            ::
            """,
            want="XXX",
        )


def test_simple():
    compare_have_want(
        have=r"""
        :manuscript:

        Warning\: this is a warning.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">Warning: this is a warning.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_colon_inside_bold():
    compare_have_want(
        have=r"""
        :manuscript:

        :span: :strong: :: Warning\: :: this is a warning.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="span"><strong>Warning: </strong></span> this is a warning.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_colon_inside_bold_no_space():
    compare_have_want(
        have=r"""
        :manuscript:

        :span: :strong: :: Warning\::: this is a warning.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="span"><strong>Warning: </strong></span>this is a warning.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_colon_inside_bold_with_shortcut():
    compare_have_want(
        have=r"""
        :manuscript:

        **Warning\: ** this is a warning.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="span"><strong>Warning: </strong></span> this is a warning.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
