import pytest
from conftest import compare_have_want, EMPTY_WANT
import rsm


def test_comment_one_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        % comment

        ::
        """,
        want=EMPTY_WANT,
    )


def test_comment_multi_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        % this is a
        % multi line comment

        ::
        """,
        want=EMPTY_WANT,
    )


def test_escape_comment_delimiter():
    compare_have_want(
        have=r"""        :manuscript:

        \% This is not a comment.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">% This is not a comment.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_end_of_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        Foo.% this is a comment at the end of a line

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">Foo.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_percent_within_math_is_not_a_comment():
    compare_have_want(
        have="""
        :manuscript:

        $10\%$ this is not a comment

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="math">\(10\%\)</span> this is not a comment</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
