# Ran when building wheel files for rsm-markup

import subprocess
import sys
from typing import Any

RESULT = subprocess.run(
    "which npm", shell=True, check=True, capture_output=True, text=True
)
NPM_PATH = RESULT.stdout.strip()


def run(
    cmd: str,
    check: bool = True,
    shell: bool = True,
    cwd: str = "tree-sitter-rsm",
    print_output: bool = False,
):
    """Run a shell command from `cwd`.

    Use check=False if you don't care whether it succeeds.

    """
    print(f"build.py: {cmd}", flush=True)
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, check=check, shell=shell, cwd=cwd
    )
    if print_output:
        print(result.stdout.decode("utf-8"))


def build(_: Any):  # one argument is passed by poetry but we don't need it
    """Install tree-sitter and build the shared object library."""
    run(f"{NPM_PATH} install")  # Install tree-sitter and its dependencies

    # 'tree-sitter test' creates the .so file; we don't care if the tests actually pass,
    if sys.platform == "win32":
        run("sh node_modules/.bin/tree-sitter generate")
        run("sh node_modules/.bin/tree-sitter build -o build/rsm.so")
    else:
        run("node ./node_modules/.bin/tree-sitter generate")
        run("node ./node_modules/.bin/tree-sitter build -o build/rsm.so")

    fn = "rsm.dll" if sys.platform == "win32" else "rsm.so"
    # watch out: tree-sitter might change this dir inadvertently...
    # run(f"cp ~/.tree-sitter/bin/{fn} rsm/", cwd=".")
    run(f"cp build/{fn} ../rsm/")


if __name__ == "__main__":
    build(None)
