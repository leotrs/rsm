# global pytest configuration and fixtures
import rsm
import pytest
from rsm.manuscript import PlainTextManuscript
from textwrap import dedent
import sys
from icecream import ic

ic.disable()

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


# This is defined in pytest_configure, which is executed before any of the tests are ran
# this is done so that the helper function compare_have_want can read the command line
# option -T that determines which parser to use
compare_have_want = None


def compare_have_want_handrails(have, want):
    return compare_have_want(have, want, True)


def pytest_addoption(parser):
    parser.addoption("-T", "--treesitter", action="store_true", default=False)


def pytest_configure(config):
    treesitter = config.getoption("-T")

    def func(have, want, handrails=False):
        want = dedent(want).lstrip()
        have = PlainTextManuscript(dedent(have).lstrip())
        have = rsm.render(have, handrails=handrails, treesitter=treesitter).lstrip()

        try:
            assert have == want
        except AssertionError as with_space:
            try:
                assert ''.join(have.split()) == ''.join(want.split())
            except AssertionError:
                raise AssertionError('Difference in content') from with_space
            raise AssertionError('Difference in whitespace only') from with_space

    global compare_have_want
    compare_have_want = func
