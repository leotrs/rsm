# global pytest configuration and fixtures
import rsm
import pytest
from textwrap import dedent
import sys
from icecream import ic

ic.disable()

sys.setrecursionlimit(100)

EMPTY_WANT = """\
<body>

<div class="manuscriptwrapper">

<div class="manuscript">

<section class="level-1">

</section>

</div>

</div>

</body>
"""


def compare_have_want(have, want, handrails=False):
    want = dedent(want).lstrip()
    have = dedent(have).lstrip()
    have = rsm.render(have, handrails=handrails).lstrip()

    try:
        assert have == want
    except AssertionError as with_space:
        try:
            assert "".join(have.split()) == "".join(want.split())
        except AssertionError:
            raise AssertionError("Difference in content") from with_space
        raise AssertionError("Difference in whitespace only") from with_space


def compare_have_want_handrails(have, want):
    return compare_have_want(have, want, True)
