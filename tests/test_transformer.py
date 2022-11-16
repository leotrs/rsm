import pytest
from conftest import compare_have_want
import rsm


def test_duplicate_label():
    with pytest.raises(rsm.transformer.RSMTransformerError):
        compare_have_want(
            have="""\
            :manuscript:

            There are :span: {:label: mylbl} two :: spans with the :span: {:label: mylbl}
            same :: label in this paragraph.

            ::
            """,
            want='XXX',
        )
