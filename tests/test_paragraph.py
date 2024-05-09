import pytest
from conftest import compare_have_want
import rsm


def test_succeeding_blankline():
    compare_have_want(
        have="""\
        :manuscript:

        Foo.
        ::
        """,
        want="""\
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


def test_succeeding_blankline_with_tag():
    compare_have_want(
        have="""\
        :manuscript:

        :paragraph: {:types: foo}This is a paragraph.
        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph foo" data-nodeid="1">This is a paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_start_with_tag():
    compare_have_want(
        have="""\
        :manuscript:

        :span: {:strong:} this tag :: starts the paragraph.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1"><span class="span" data-nodeid="2"><strong>this tag</strong></span> starts the paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_start_with_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        :|-: A claim::.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1"><span class="construct claim" data-nodeid="2"><span class="keyword" data-nodeid="3">⊢ </span>A claim</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: The Perron non-backtracking eigenvalue after node addition
          :date: 2022-03-29

        :section:
          :title: Introduction
          :label: sec-introduction
          :types: {t1, t2}

        Lorem ipsum.

        :paragraph: {:label: par1} This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.

        :paragraph:
           {:label: par2}
        This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.

        :paragraph: {:label: par3, :types: {a, b, c}} This is a paragraph with meta data. It
        has several lines of text. It has several lines of text. It has several lines of
        text. It has several lines of text. It has several lines of text.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="mylbl" class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>The Perron non-backtracking eigenvalue after node addition</h1>

        <section id="sec-introduction" class="section level-2 t1 t2" data-nodeid="1">

        <h2>1. Introduction</h2>

        <p class="paragraph" data-nodeid="2">Lorem ipsum.</p>

        <p id="par1" class="paragraph" data-nodeid="4">This is a paragraph with meta data. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text.</p>

        <p id="par2" class="paragraph" data-nodeid="6">This is a paragraph with meta data. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text.</p>

        <p id="par3" class="paragraph a b c" data-nodeid="8">This is a paragraph with meta data. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text. It has several lines of text.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
