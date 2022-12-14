"""Input: Path to .rsm file -- Output: file contents."""

from pathlib import Path

import logging

logger = logging.getLogger("RSM").getChild("read ")


class Reader:
    """Read the contents of a .rsm file."""

    def __init__(self) -> None:
        self.path: Path = Path()
        self.src: str = ""

    def read(self, path: Path | None) -> str:
        logger.info("Reading...")
        if not path:
            raise TypeError("Expected path, got None")
        self.path = Path(path)
        with open(path) as file:
            self.src = file.read()
        return self.src
