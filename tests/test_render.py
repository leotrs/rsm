import pytest
import subprocess
from textwrap import dedent


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

    result = subprocess.run(["rsm-render", src], stdout=subprocess.PIPE, check=True)
    output = result.stdout[result.stdout.find(b"<body>") :].decode("utf-8")
    assert output.strip() == want.strip()


@pytest.mark.slow
def test_invalid_rsm():
    have = "test_file.rsm"
    with pytest.raises(subprocess.CalledProcessError):
        result = subprocess.run(
            ["rsm-render", have], stdout=subprocess.PIPE, check=True
        )
