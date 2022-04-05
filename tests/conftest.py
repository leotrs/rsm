import rsm
from rsm.core.manuscript import PlainTextManuscript
from textwrap import dedent
from icecream import ic
ic.disable()


def compare_have_want(have, want):
    want = dedent(want).strip()
    have = PlainTextManuscript(dedent(have).strip())
    have = rsm.Application(plain=have).run(write=False)
    have = have.body.strip()

    # compare without whitespace
    assert ''.join(have.split()) == ''.join(want.split())

    # compare with whitespace
    assert have == want
