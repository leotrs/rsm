"""
util.py
-------

Utilities.

"""

from typing import Any


def short_repr(text: str, classname, limit: int = 20) -> str:
    if len(text) > limit:
        before = text[:10].replace('\n', '\\n').strip()
        after = text[-10:].replace('\n', '\\n').strip()
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


class EscapedString:
    def __init__(self, src='', chars=None):
        self.escape_chars = set() if chars is None else set(chars)
        self._src = str(src)

    def __contains__(self, sub):
        return sub in self._src

    def __len__(self):
        return len(self._src)

    def __repr__(self):
        return repr(self._src)

    def __str__(self):
        return self._src

    def __getitem__(self, _slice):
        return self.__class__(self._src[_slice])

    def __add__(self, other):
        return self._src + other

    def __radd__(self, other):
        return other + self._src

    def __eq__(self, other):
        return self._src == other

    def __hash__(self):
        return hash(self._src)

    def format(self, *args, **kwargs):
        return self._src.format(*args, **kwargs)

    def strip(self, chars=None, /):
        return self.__class__(self._src.strip(chars))

    def lstrip(self, chars=None, /):
        return self.__class__(self._src.lstrip(chars))

    def rstrip(self, chars=None, /):
        return self.__class__(self._src.rstrip(chars))

    def find(self, sub, start=0, end=None, skip_escaped=True):
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.find(sub, start, end)
        index = self._src.find(sub, start, end)
        if index < 1:
            # If sub was found at index 0, it cannot have been escaped since there is
            # nothing behind it!  If the index was negative, it was not found.  Either
            # way, we are done.
            return index
        while self._src[index - 1] == '\\':
            index = self._src.find(sub, index + 1, end)
            if index < 0:
                return index
        return index

    def rfind(self, sub, start=0, end=None, skip_escaped=True):
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.rfind(sub, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def index(self, sub, start=0, end=None, skip_escaped=True):
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.index(sub, start, end)
        index = self._src.index(sub, start, end)
        if index == 0:
            # If sub was found at index 0, it cannot have been escaped since there is
            # nothing behind it!  Unlike find(), index() never returns -1 (it raises an
            # exception instead), so no need to check for that.
            return index
        while self._src[index - 1] == '\\':
            index = self._src.find(sub, index + 1, end)
        return index

    def rindex(self, sub, start=0, end=None, skip_escaped=True):
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.rindex(sub, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def replace(self, old, new, count=-1, /, skip_escaped=True):
        if not skip_escaped or old not in self.escape_chars:
            return self.__class__(self._src.replace(old, new, count))
        raise Exception("Leo should have implemented this but didn't")

    def startswith(self, prefix, start=0, end=None, skip_escaped=True):
        if end == -1:
            end = len(self._src)
        if len(prefix) == 1:
            return self._src.startswith(prefix, start, end)
        if not skip_escaped or prefix not in self.escape_chars:
            return self._src.startswith(prefix, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def endswith(self, prefix, start=0, end=None, skip_escaped=True):
        if end is None:
            end = len(self._src)
        if not skip_escaped or prefix not in self.escape_chars:
            return self._src.endswith(prefix, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def split(self, /, sep=None, maxsplit=-1, skip_escaped=True):
        if not skip_escaped or sep not in self.escape_chars:
            return self._src.split(sep, maxsplit)
        raise Exception("Leo should have implemented this but didn't")
