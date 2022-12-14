"""Read the contents of a file containing RSM markup."""

from pathlib import Path

import logging

logger = logging.getLogger("RSM").getChild("read ")


class Reader:
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
