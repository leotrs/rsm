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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">% This is not a comment.</p>

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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Foo.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_percent_within_math_is_not_a_comment():
    compare_have_want(
        have=r"""        :manuscript:

        $10\%$ this is not a comment

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1"><span class="math" data-nodeid="2">\(10\%\)</span> this is not a comment</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_broken_paragraph():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph
        % with a comment
        in the middle

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph in the middle</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
