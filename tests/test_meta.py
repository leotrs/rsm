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


def test_manuscript_with_inline_meta():
    compare_have_want(
        have="""\
        :manuscript: :title: Title

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>Title</h1>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_block_with_inline_meta_no_content():
    compare_have_want(
        have="""\
        :manuscript:

        :section: :title: My title, :label: my-sec :: ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section id="my-sec" class="section level-2">

        <h2>1. My title</h2>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_block_with_inline_meta_with_content():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: My title

        :theorem: :label: my-thm, :stars: 3, :clocks: 2 ::

          Foo.

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. My title</h2>

        <div id="my-thm" class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1. </strong></span></p>

        <p class="paragraph">Foo.</p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_block_with_inline_meta_with_content():
    compare_have_want(
        have="""\
        :manuscript:

        This contains a :span: :strong:, :label: my-span :: labeled span ::.

        ::
        """,
        want="""\
       <body>

       <div class="manuscriptwrapper">

       <div id="manuscript" class="manuscript">

       <section class="level-1">

       <h1></h1>

       <p class="paragraph">This contains a <span id="my-span" class="span"><strong>labeled span </strong></span>.</p>

       </section>

       </div>

       </div>

       </body>
        """,
    )


def test_block_with_inline_meta_must_fit_insingle_line():
    with pytest.raises(Exception):
        compare_have_want(
            have="""\
            :manuscript:

            :section:
              :title: My title

            :theorem: :label: my-thm,
              :stars: 3, :clocks: 2 ::

              Foo.

            ::

            ::

            ::
            """,
            want="X",
        )


def test_inline_no_meta_start_with_tag():
    compare_have_want(
        have="""\
        :manuscript:

        :paragraph: :label: lbl :: Foo bar.

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
