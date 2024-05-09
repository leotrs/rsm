import pytest
from conftest import compare_have_want

import rsm


def test_list_with_only_one_element():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        :paragraph: {:types: mytype} This paragraph has only one type

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph mytype" data-nodeid="1">This paragraph has only one type</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_list_with_one_element_before_key():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        :paragraph: {:types: mytype, :label: lbl} This paragraph has only one type,
        that appears before another key.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>

        <p id="lbl" class="paragraph mytype" data-nodeid="1">This paragraph has only one type, that appears before another key.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_list_no_braces():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        :paragraph: {:types: t1, t2} This paragraph has only one type

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>
        <span class="error" data-nodeid="1">[CST error at (3, 0) - (3, 28)]</span>
        <p class="paragraph" data-nodeid="2">This paragraph has only one type</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_no_meta_start_with_tag():
    compare_have_want(
        have="""\
        :manuscript:

        :paragraph: {:label: lbl} Foo bar.

        This span starts with a tag that is not a meta key, :span: :ref:lbl,some paragraph::, instead
        it starts with a ref::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p id="lbl" class="paragraph" data-nodeid="1">Foo bar.</p>

        <p class="paragraph" data-nodeid="3">This span starts with a tag that is not a meta key, <span class="span" data-nodeid="5"><a class="reference" href="#lbl">some paragraph</a>, instead it starts with a ref</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_list_within_inline():
    compare_have_want(
        have="""\
        :manuscript:

        Foo :span: {:types: {t1, t2}} bar :: baz.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Foo <span class="span t1 t2" data-nodeid="3">bar</span> baz.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_start_with_brace():
    compare_have_want(
        have=r"""        :manuscript:

        This span starts with a brace :span: \{ ::.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This span starts with a brace <span class="span" data-nodeid="3">{</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_meta_with_no_space():
    compare_have_want(
        have="""\
        :manuscript:

        Foo :span: {:strong:} bar ::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Foo <span class="span" data-nodeid="3"><strong>bar</strong></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_meta_with_space_in_between_braces():
    compare_have_want(
        have="""\
        :manuscript:

        Foo :span: { :strong: } bar ::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Foo <span class="span" data-nodeid="3"><strong>bar</strong></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
