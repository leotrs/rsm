import rsm
from textwrap import dedent


def compare_have_want(have, want):
    have = rsm.core.manuscript.PlainTextManuscript(dedent(have))
    want = dedent(want)
    web = rsm.Application().run(have, write=False)
    assert web.body == want
