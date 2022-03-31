"""
util.py
-------

Utilities.

"""


def short_repr(text: str, classname, limit: int = 20) -> str:
    if len(text) > limit:
        name = classname if classname else ''
        before = text[:10].replace('\n', '\\n')
        after = text[-10:].replace('\n', '\\n')
        if classname:
            return f'{classname}({before} [...] {after})'
        else:
            return f'"{before} [...] {after}"'
    else:
        return repr(text.replace('\n', '\\n'))


class ShortenedString(str):
    """A string that appears shortened."""
    def __repr__(self):
        return short_repr(self, classname=None)
