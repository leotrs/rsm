import sys
import pytest
import subprocess
from textwrap import dedent
from importlib.metadata import version


def cmd(src):
    return " ".join(["rsm-render", f"'{src}'"])


@pytest.mark.slow
def test_render():
    src = ":manuscript:\n\nFoo.\n\nBar.\n\nBaz.\n\n::\n"
    want = dedent(
        """
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">Foo.</p>

        <p class="paragraph">Bar.</p>

        <p class="paragraph">Baz.</p>

        </section>

        </div>

        </div>

        </body>
        """
    )

    result = subprocess.run(cmd(src), stdout=subprocess.PIPE, check=True, shell=True)

    # get rid of any logs appearing before the html body, and decode
    output = result.stdout[result.stdout.find(b"<body>") :].decode("utf-8")
    if sys.platform == "win32":
        output = output.replace("\r", "")
    assert output.strip() == want.strip()


@pytest.mark.slow
def test_invalid_rsm():
    have = "test_file.rsm"
    with pytest.raises(subprocess.CalledProcessError):
        result = subprocess.run(
            cmd(have), stdout=subprocess.PIPE, check=True, shell=True
        )


@pytest.mark.slow
def test_render_version():
    result = subprocess.run(
        "rsm-render --version", stdout=subprocess.PIPE, check=True, shell=True
    )
    output = result.stdout.decode("utf-8").strip()
    assert output == f"rsm-markup v{version('rsm-markup')}"
