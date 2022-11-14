import pytest
import subprocess
from conftest import compare_have_want


@pytest.mark.slow
def test_render():
    have = """:manuscript:

    Lorem ipsum.

    ::
    """
    result = subprocess.run(['rsm-render', have], stdout=subprocess.PIPE, check=True)

    compare_have_want(
        have=have,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">Lorem ipsum.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_invalid_rsm():
    have = "test_file.rsm"
    with pytest.raises(subprocess.CalledProcessError):
        result = subprocess.run(
            ['rsm-render', have], stdout=subprocess.PIPE, check=True
        )
