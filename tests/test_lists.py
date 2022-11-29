import pytest
import rsm
from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        :enumerate:
          :label: enm-foo

          :item: {:label: itm-1} Foo bar.

          :item: {:label: itm-2} Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem
            ipsum dolor sit amet.

          :item: {:label: itm-3}
          Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem
          ipsum dolor sit amet.

        ::

        :itemize:
          :label: itm-foo

          :item: {:label: itm-4} Foo bar.

          :item: {:label: itm-5} Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem
            ipsum dolor sit amet.

          :item: {:label: itm-6}
          Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem
          ipsum dolor sit amet.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <ol id="enm-foo" class="enumerate">

        <li id="itm-1" class="item">
        Foo bar.
        </li>

        <li id="itm-2" class="item">
        Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.
        </li>

        <li id="itm-3" class="item">
        Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.
        </li>

        </ol>

        <ul id="itm-foo" class="itemize">

        <li id="itm-4" class="item">
        Foo bar.
        </li>

        <li id="itm-5" class="item">
        Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.
        </li>

        <li id="itm-6" class="item">
        Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.
        </li>

        </ul>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_item_with_wrong_parent():
    with pytest.raises(rsm.nodes.RSMNodeError):
        compare_have_want(
            have="""\
            :manuscript:

            :item: Foo bar.

            ::
            """,
            want="XXX",
        )

    with pytest.raises(rsm.nodes.RSMNodeError):
        compare_have_want(
            have="""\
            :manuscript:

            # Some section

            :item: Foo bar.

            ::
            """,
            want="XXX",
        )

    with pytest.raises(rsm.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:

            # Some section

            Lorem ipsum :item: Foo bar.

            ::
            """,
            want="XXX",
        )
