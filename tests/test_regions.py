import pytest
from conftest import compare_have_want
import rsm


def test_inline_cannot_contain_block():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            This is a paragraph :span: with an inline :section: with a block. :: ::

            ::
            """,
            want='XXX',
        )

    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            This is a paragraph :claim: with an inline :theorem: with a block. :: ::

            ::
            """,
            want='XXX',
        )


def test_paragraph_cannot_contain_block():
    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            This is a paragraph with a :section: block. ::

            ::
            """,
            want='XXX',
        )

    with pytest.raises(rsm.core.parser.RSMParserError):
        compare_have_want(
            have="""\
            :manuscript:
              :title: My Title

            This is a paragraph :theorem: with a block. ::

            ::
            """,
            want='XXX',
        )
