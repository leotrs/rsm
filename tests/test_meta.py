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
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph mytype">This paragraph has only one type</p>
        </section>
        </div>
        </body>
        """
    )


def test_list_no_braces():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            :paragraph: :types: t1, t2 :: This paragraph has only one type

            ::
            """,
            want="XXX"
        )
