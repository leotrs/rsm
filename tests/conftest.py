import rsm
from rsm.core.manuscript import PlainTextManuscript
from textwrap import dedent
from icecream import ic

ic.disable()


import sys

sys.setrecursionlimit(100)


def compare_have_want(have, want, handrails=False):
    want = dedent(want).strip()
    have = PlainTextManuscript(dedent(have).strip())
    have = rsm.render(have, handrails=handrails).strip()

    # compare without whitespace
    assert ''.join(have.split()) == ''.join(want.split())

    # compare with whitespace
    assert have == want


def compare_have_want_handrails(have, want):
    return compare_have_want(have, want, True)
