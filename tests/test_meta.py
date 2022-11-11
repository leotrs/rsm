import pytest
from conftest import compare_have_want
import rsm


def test_list_with_only_one_element():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        :paragraph: :types: mytype :: This paragraph has only one type

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph mytype">This paragraph has only one type</p>

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

        :paragraph: :types: mytype, :label: lbl :: This paragraph has only one type,
        that appears before another key.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p id="lbl" class="paragraph mytype">This paragraph has only one type,
        that appears before another key.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_list_no_braces():
    with pytest.raises(rsm.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            :paragraph: :types: t1, t2 :: This paragraph has only one type

            ::
            """,
            want="XXX",
        )


def test_inline_no_meta_start_with_tag():
    compare_have_want(
        have="""\
        :manuscript:

        :paragraph: :label: lbl:: Foo bar.

        This span starts with a tag that is not a meta key, :span: :ref:lbl::, instead
        it starts with a ref::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p id="lbl" class="paragraph">Foo bar.</p>

        <p class="paragraph">This span starts with a tag that is not a meta key, <span class="span"><a class="reference" href="#lbl">Paragraph None</a>, instead
        it starts with a ref</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
