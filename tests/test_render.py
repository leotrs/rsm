import subprocess
from conftest import compare_have_want


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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">Lorem ipsum.</p>

        </section>

        </div>

        </body>
        """,
    )
