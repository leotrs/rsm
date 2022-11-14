# global pytest configuration and fixtures
import rsm
from rsm.manuscript import PlainTextManuscript
from textwrap import dedent
from icecream import ic
import sys

sys.setrecursionlimit(100)

EMPTY_WANT = """\
<body>

<div class="manuscriptwrapper">

<div id="manuscript" class="manuscript">

<section class="level-1">

<h1></h1>

</section>

</div>

</div>

</body>
"""


def compare_have_want(have, want, handrails=False):
    want = dedent(want).lstrip()
    have = PlainTextManuscript(dedent(have).lstrip())
    have = rsm.render(have, handrails=handrails).lstrip()

    # compare without whitespace
    # assert ''.join(have.split()) == ''.join(want.split())

    # compare with whitespace
    assert have == want


def compare_have_want_handrails(have, want):
    return compare_have_want(have, want, True)


ic.disable()
