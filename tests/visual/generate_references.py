"""generate_references.py

Generate reference files for BackstopJS to do its thing.

"""

from pathlib import Path

import rsm

DATA_DIR = Path(__file__).parent / "rsm_data"


def main():
    for file in DATA_DIR.iterdir():
        if file.is_file() and file.suffix == ".rsm":
            rsm.make(path=file, lint=False, outname=f"m{file.stem}.html")


if __name__ == "__main__":
    main()
