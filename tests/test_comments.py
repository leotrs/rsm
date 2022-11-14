import pytest
from conftest import compare_have_want
import rsm


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:
          :title: Main Theorem

        :note: This is a single line note.

        Theorem contents.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1. </strong></span></p>

        <div class="note">
        This is a single line note.
        </div>

        <p class="paragraph">Theorem contents.</p>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
