import pytest
import rsm
from conftest import compare_have_want


def test_no_manuscript_title():
    compare_have_want(
        have="""\
        :manuscript:

        Lorem ipsum.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </div>
        </body>
        """
    )


def test_manuscript_title():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        Lorem ipsum.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </div>
        </body>
        """
    )


def test_manuscript_meta():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: My Title
          :date: 2022-03-29
        ::
        """,
        want="""\
        <body>
        <div id="mylbl" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>

        </section>
        </div>
        </body>
        """
    )


def test_no_tombstone():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:

            Lorem ipsum.
            """,
            want='XXX'
        )


def test_section_header():
    compare_have_want(
        have="""\
        :manuscript:

        Lorem ipsum.

        :section:
          :title: section title

        Lorem ipsum.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">Lorem ipsum.</p><section class="section level-2">
        <h2>1. section title</h2>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </section>
        </div>
        </body>
        """
    )
