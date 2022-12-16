"""
util.py
-------

Utilities.

"""

import textwrap
from typing import Any, Optional, Union


class EscapedString:
    def __init__(self, src: str = "", chars: Optional[str] = None):
        self.escape_chars = set() if chars is None else set(chars)
        self._src = str(src)

    def __contains__(self, sub: str) -> bool:
        return sub in self._src

    def __len__(self) -> int:
        return len(self._src)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.escape_chars}, {textwrap.shorten(self._src, 60)})"

    def __str__(self) -> str:
        return self._src

    def escape(self) -> str:
        ret = self._src
        for char in self.escape_chars:
            ret = ret.replace(f"\\{char}", char)
        return ret

    def __getitem__(self, _slice: Union[int, slice]) -> "EscapedString":
        return self.__class__(self._src[_slice])

    def __add__(self, other: str) -> str:
        return self._src + other

    def __radd__(self, other: str) -> str:
        return other + self._src

    def __eq__(self, other: Any) -> bool:
        return self._src == other

    def __hash__(self) -> int:
        return hash(self._src)

    def format(self, *args: Any, **kwargs: Any) -> str:
        return self._src.format(*args, **kwargs)

    def strip(self, chars: Optional[str] = None, /) -> "EscapedString":
        return self.__class__(self._src.strip(chars))

    def lstrip(self, chars: Optional[str] = None, /) -> "EscapedString":
        return self.__class__(self._src.lstrip(chars))

    def rstrip(self, chars: Optional[str] = None, /) -> "EscapedString":
        return self.__class__(self._src.rstrip(chars))

    def find(
        self,
        sub: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> int:
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
        while self._src[index - 1] == "\\":
            index = self._src.find(sub, index + 1, end)
            if index < 0:
                return index
        return index

    def rfind(
        self,
        sub: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> int:
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.rfind(sub, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def index(
        self,
        sub: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> int:
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
        while self._src[index - 1] == "\\":
            index = self._src.find(sub, index + 1, end)
        return index

    def rindex(
        self,
        sub: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> int:
        if end is None:
            end = len(self._src)
        if not skip_escaped or sub not in self.escape_chars:
            return self._src.rindex(sub, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def replace(
        self, old: str, new: str, count: int = -1, /, skip_escaped: bool = True
    ) -> "EscapedString":
        if not skip_escaped or old not in self.escape_chars:
            return self.__class__(self._src.replace(old, new, count))
        raise Exception("Leo should have implemented this but didn't")

    def startswith(
        self,
        prefix: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> bool:
        if end == -1:
            end = len(self._src)
        if len(prefix) == 1:
            return self._src.startswith(prefix, start, end)
        if not skip_escaped or prefix not in self.escape_chars:
            return self._src.startswith(prefix, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def endswith(
        self,
        prefix: str,
        start: int = 0,
        end: Optional[int] = None,
        skip_escaped: bool = True,
    ) -> bool:
        if end is None:
            end = len(self._src)
        if not skip_escaped or prefix not in self.escape_chars:
            return self._src.endswith(prefix, start, end)
        raise Exception("Leo should have implemented this but didn't")

    def split(
        self,
        /,
        sep: Optional[str] = None,
        maxsplit: int = -1,
        skip_escaped: bool = True,
    ) -> list[str]:
        if not skip_escaped or sep not in self.escape_chars:
            return self._src.split(sep, maxsplit)
        runs = []
        prev = 0
        curr = 0
        while curr < len(self._src):
            if self._src[curr] in self.escape_chars and (
                curr > 0 and self._src[curr - 1] != "\\"
            ):
                runs.append(self._src[prev + 1 : curr - 1])
                prev = curr
            curr += 1
        runs.append(self._src[prev + 1 : curr - 1])

        return runs
