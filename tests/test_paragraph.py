import pytest
from conftest import compare_have_want
import rsm


def test_preceding_blankline():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title
            This is a paragraph.

            ::
            """,
            want='XXX'
        )

    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title
            :paragraph: This is a paragraph.

            ::
            """,
            want='XXX'
        )


def test_succeeding_blankline():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:

            This is a paragraph.
            ::
            """,
            want='XXX'
        )

    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:

            :paragraph: This is a paragraph.
            ::
            """,
            want='XXX'
        )


def test_no_meta():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: The Perron non-backtracking eigenvalue after node addition
          :date: 2022-03-29

        :section:
          :title: Introduction

        :paragraph: This is a paragraph with tag and no meta data.

        :paragraph:
        This is a paragraph with tag and no meta data.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="mylbl" class="manuscript">
        <section class="level-1">
        <h1>The Perron non-backtracking eigenvalue after node addition</h1>
        <section class="section level-2">
        <p class="paragraph">This is a paragraph with tag and no meta data.</p>
        <p class="paragraph">This is a paragraph with tag and no meta data.</p>
        </section>
        </section>
        </div>
        </body>
        """
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

        :paragraph: :label: par1 :: This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.

        :paragraph:
           :label: par2
        This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.

        :paragraph: :label: par3, :types: {a, b, c} :: This is a paragraph with meta data. It
        has several lines of text. It has several lines of text. It has several lines of
        text. It has several lines of text. It has several lines of text.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="mylbl" class="manuscript">
        <section class="level-1">
        <h1>The Perron non-backtracking eigenvalue after node addition</h1>
        <section id="sec-introduction" class="section level-2 t1 t2">
        <p class="paragraph">Lorem ipsum.</p>
        <p id="par1" class="paragraph">This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.</p>
        <p id="par2" class="paragraph">This is a paragraph with meta data. It has several lines of text. It has several lines
        of text. It has several lines of text. It has several lines of text. It has several
        lines of text.</p>
        <p id="par3" class="paragraph a b c">This is a paragraph with meta data. It
        has several lines of text. It has several lines of text. It has several lines of
        text. It has several lines of text. It has several lines of text.</p>
        </section>
        </section>
        </div>
        </body>
        """
    )
