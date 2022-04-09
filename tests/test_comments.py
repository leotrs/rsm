import pytest
from conftest import compare_have_want
import rsm


def test_comment_single_line():
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
        <h3>Theorem</h3>
        <div class="comment">
        This is a single line comment.
        </div><p class="paragraph">Theorem contents.</p>
        </div>
        </section>
        </div>
        </body>
        """
    )
