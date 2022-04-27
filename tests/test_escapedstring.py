from rsm.core.util import EscapedString


def test_ignore_single_char():
    esc = EscapedString(r'\:', ':')
    assert esc.find(':') == -1
    assert len(esc) == 1
