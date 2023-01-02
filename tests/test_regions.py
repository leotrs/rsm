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

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>
        <span class="error">[CST error at (3, 0) - (3, 71)]</span>
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

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph will terminate before the section starts</p>

        <section class="section level-2">

        <h2>1. </h2>

        <p class="paragraph">And this is inside the section.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
