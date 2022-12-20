# Ran when building wheel files for rsm-markup

import subprocess
import sys
from typing import Any

# All shell commands below run from this directory by default; see the cwd parameter
DEFAULT_CMD_DIR = "tree-sitter-rsm"


def run(
    cmd: str,
    check: bool = True,
    shell: bool = True,
    cwd: str = DEFAULT_CMD_DIR,
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
    run("npm install")  # Install tree-sitter and its dependencies

    # 'tree-sitter test' creates the .so file; we don't care if the tests actually pass,
    if sys.platform == "win32":
        run("sh node_modules/.bin/tree-sitter generate")
        run("sh node_modules/.bin/tree-sitter test", check=False)
    else:
        run("node ./node_modules/.bin/tree-sitter generate")
        run("node ./node_modules/.bin/tree-sitter test", check=False)

    fn = "rsm.dll" if sys.platform == "win32" else "rsm.so"
    # watch out: tree-sitter might change this dir inadvertently...
    run(f"cp ~/.tree-sitter/bin/{fn} rsm/", cwd=".")
    run("ls rsm/", cwd=".", print_output=True)


if __name__ == "__main__":
    build(None)
