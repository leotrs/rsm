import rsm
from textwrap import dedent


def compare_have_want(have, want):
    want = dedent(want).strip()
    have = rsm.core.manuscript.PlainTextManuscript(dedent(have))
    have = rsm.Application().run(have, write=False)
    have = have.body.strip()

    # compare without whitespace
    assert ''.join(have.split()) == ''.join(want.split())

    # compare with whitespace
    assert have == want
