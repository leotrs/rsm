import pytest
from conftest import compare_have_want

import rsm


def test_inline_cannot_contain_block():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This is a paragraph :span: with an inline :section: with a block. :: ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>
        <span class="error" data-nodeid="1">[CST error at (3, 0) - (3, 42)]</span>
        <section class="section level-2" data-nodeid="2">

        <h2>1. </h2>

        <div class="paragraph" data-nodeid="3">

        <p>with a block.</p>

        </div>

        </section>
        <span class="error" data-nodeid="5">[CST error at (5, 0) - (5, 2)]</span>
        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_paragraph_ends_at_block():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph will terminate before the section starts :section: And this
        is inside the section. ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>

        <div class="paragraph" data-nodeid="1">

        <p>This paragraph will terminate before the section starts</p>

        </div>

        <section class="section level-2" data-nodeid="3">

        <h2>1. </h2>

        <div class="paragraph" data-nodeid="4">

        <p>And this is inside the section.</p>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
