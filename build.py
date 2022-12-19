# Ran when building wheel files for rsm-markup

import subprocess
import sys

DEFAULT_CMD_DIR = "tree-sitter-rsm"


def run(cmd, check=True, shell=True, cwd=DEFAULT_CMD_DIR, print_output=False):
    print(f"build.py: {cmd}", flush=True)
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, check=check, shell=shell, cwd=cwd
    )
    if print_output:
        print(result.stdout.decode("utf-8"))


def build(setup_kwargs):
    run("npm install")

    # 'tree-sitter test' creates the .so file; we don't care if the tests actually pass,
    # thus we use check=False
    if sys.platform == "win32":
        run("sh node_modules/.bin/tree-sitter generate")
        run("sh node_modules/.bin/tree-sitter test", check=False)
    else:
        run("node ./node_modules/.bin/tree-sitter generate")
        run("node ./node_modules/.bin/tree-sitter test", check=False)

    fn = "rsm.dll" if sys.platform == "win32" else "rsm.so"
    run(f"cp ~/.tree-sitter/bin/{fn} rsm/", cwd=".")


if __name__ == "__main__":
    build(None)
