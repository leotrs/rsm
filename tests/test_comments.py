import pytest
from conftest import compare_have_want
import rsm


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:
          :title: Main Theorem

        :comment: This is a single line comment.

        Theorem contents.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <div class="theorem">
        <div class="comment">
        This is a single line comment.
        </div><p class="paragraph"><span class="span"><strong>Theorem 1. </strong></span>Theorem contents.</p>
        </div>
        </section>
        </div>
        </body>
        """
    )
