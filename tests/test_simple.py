import pytest
import rsm
from textwrap import dedent

# This file contains a single test, test_simple() that receives an argument 'have' which
# is a string containing rsm markup plaintext, and an argument 'want' that is a string
# containing html.  The test checks whether the rsm application converts 'have' into
# 'want'.  The test test_simple() is parameterized and executed on multiple pairs of
# (have, want) values.  These are specified in the long argument to
# @pytest.mark.parametrize.  dedent() and a backslash escaping the first newline are
# used for readability purposes.

@pytest.mark.parametrize(
    'have, want',
    [
        # test case
        (
            # have
            dedent("""\
            :manuscript:

            Lorem ipsum.

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="manuscript" class="manuscript">
            <section class="level-1">
            <h1></h1>
            <p class="paragraph">Lorem ipsum.</p>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :title: My Title

            Lorem ipsum.

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="manuscript" class="manuscript">
            <section class="level-1">
            <h1>My Title</h1>
            <p class="paragraph">Lorem ipsum.</p>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :label: mylbl
              :title: My Title
              :date: 2022-03-29
            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="mylbl" class="manuscript">
            <section class="level-1">
            <h1>My Title</h1>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :label: mylbl
              :title: My Title
              :date: 2022-03-29

            :author:
              :name: Leo Torres
              :affiliation: Max Planck Institute for Mathematics in the Sciences
              :email: leo@leotrs.com
            ::

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="mylbl" class="manuscript">
            <section class="level-1">
            <h1>My Title</h1>
            <div class="author">
            <p>
            Leo Torres
            Max Planck Institute for Mathematics in the Sciences
            leo@leotrs.com
            </p>
            </div>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :label: mylbl
              :title: The Perron non-backtracking eigenvalue after node addition
              :date: 2022-03-29

            :author:
              :name: Leo Torres
              :affiliation: Max Planck Institute for Mathematics in the Sciences
              :email: leo@leotrs.com
            ::

            :abstract:
              :keywords: {spectral graph theory, non-backtracking, interlacing}
              :MSC: {05C50, 05C82, 15A18, 15B99}

              Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
              ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
              ipsum. Lorem ipsum.

              Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
              ipsum. Lorem ipsum.

            ::

            :section:
              :title: Introduction
              :label: sec:introduction
              :types: {t1, t2}

            Lorem ipsum.

            ::

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="mylbl" class="manuscript">
            <section class="level-1">
            <h1>The Perron non-backtracking eigenvalue after node addition</h1>
            <div class="author">
            <p>
            Leo Torres
            Max Planck Institute for Mathematics in the Sciences
            leo@leotrs.com
            </p>
            </div>
            <div class="abstract">
            <h3>Abstract</h3>
            <p class="paragraph">Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
            ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
            ipsum. Lorem ipsum.</p>
            <p class="paragraph">Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
            ipsum. Lorem ipsum.</p>
            <p class="keywords">
            Keywords: spectral graph theory, non-backtracking, interlacing
            </p>
            <p class="MSC">
            MSC: 05C50, 05C82, 15A18, 15B99
            </p>
            </div>
            <section id="sec:introduction" class="section level-2 t1 t2">
            <p class="paragraph">Lorem ipsum.</p>
            </section>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
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
            """)
            ,
            # want
            dedent("""\
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
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :label: mylbl
              :title: The Perron non-backtracking eigenvalue after node addition
              :date: 2022-03-29

            :section:
              :title: Introduction
              :label: sec-introduction
              :types: {t1, t2}

            This is a paragraph with no tag.

            :paragraph: This is a paragraph with tag and no meta data.

            :paragraph:
            This is a paragraph with tag and no meta data.

            ::

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="mylbl" class="manuscript">
            <section class="level-1">
            <h1>The Perron non-backtracking eigenvalue after node addition</h1>
            <section id="sec-introduction" class="section level-2 t1 t2">
            <p class="paragraph">This is a paragraph with no tag.</p>
            <p class="paragraph">This is a paragraph with tag and no meta data.</p>
            <p class="paragraph">This is a paragraph with tag and no meta data.</p>
            </section>
            </section>
            </div>
            </body>
            """)
        ),

        # test case
        (
            # have
            dedent("""\
            :manuscript:
              :label: mylbl
              :title: The Perron non-backtracking eigenvalue after node addition
              :date: 2022-03-29

            :author: ::

            Lorem ipsum.

            ::
            """)
            ,
            # want
            dedent("""\
            <body>
            <div id="mylbl" class="manuscript">
            <section class="level-1">
            <h1>The Perron non-backtracking eigenvalue after node addition</h1>
            <div class="author">
            </div>
            <p class="paragraph">Lorem ipsum.</p>
            </section>
            </div>
            </body>
            """)
        ),

    ]
)
def test_simple(have, want):
    have = rsm.core.manuscript.PlainTextManuscript(have)
    web = rsm.Application().run(have, write=False)
    assert web.body == want
