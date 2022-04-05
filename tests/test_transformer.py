import pytest
from conftest import compare_have_want
import rsm


def test_duplicate_label():
    with pytest.raises(rsm.core.transformer.RSMTransformerError):
        compare_have_want(
            have="""\
            :manuscript:

            There are :span: :label: mylbl :: two :: spans with the :span: :label: mylbl
            :: same :: label in this paragraph.

            ::
            """,
            want='XXX'
        )


def test_numbered_sections():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: First

        Content of first.

        ::

        :section:
          :title: Second

        Content of second.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <section class="section level-2">
        <h2>1. First</h2>
        <p class="paragraph">Content of first.</p>
        </section><section class="section level-2">
        <h2>2. Second</h2>
        <p class="paragraph">Content of second.</p>
        </section>
        </section>
        </div>
        </body>
        """
    )
