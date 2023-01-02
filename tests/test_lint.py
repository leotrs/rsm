import subprocess
import sys
from importlib.metadata import version
from textwrap import dedent

import pytest

EMPTY_MANUSCRIPT = ":manuscript: ::"
EMPTY_MANUSCRIPT_LOGS = [
    {
        "name": "RSM.parse",
        "level": "WRN",
        "msg": "The CST contains errors.",
        "filename": "tsparser.py",
        "lineno": 381,
    }
]

WRONG_MANUSCRIPT = ":manuscript: * ::"
WRONG_MANUSCRIPT_LOGS = [
    {
        "name": "RSM.parse",
        "level": "WRN",
        "msg": "The CST contains errors.",
        "filename": "tsparser.py",
        "lineno": 381,
    }
]


def cmd(src):
    return " ".join(["rsm-lint", f"'{src}'"])


@pytest.mark.slow
def test_render(tmp_path):
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
    # In this source code, we use the \r\n line ending typical in Windows systems.  When
    # running this test on a UNIX machine, they will simply be ignored.  When running on
    # a Windows machine, the test will fail if they are not present.
    src = ":manuscript:\r\n\r\nFoo.\r\n\r\nBar.\r\n\r\nBaz.\r\n\r\n::\r\n"
    file = tmp_path / "test.rsm"
    file.write_text(src)
    result = subprocess.run(
        f"rsm-render {str(file.resolve())}",
        stdout=subprocess.PIPE,
        check=True,
        shell=True,
    )

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
