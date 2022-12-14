"""take a file path and return a string."""

from pathlib import Path

import logging

logger = logging.getLogger("RSM").getChild("read ")


class Reader:
    def __init__(self) -> None:
        self.path: Path = Path()
        self.src: str = ""

    def read(self, path: Path | None) -> str:
        print("READING READING READING READING READING READING ")
        logger.info("Reading...")
        if not path:
            raise TypeError("Expected path, got None")
        self.path = Path(path)
        with open(path) as file:
            self.src = file.read()
        # return PlainTextManuscript(self.src)
        return self.src
