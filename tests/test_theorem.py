import pytest
from conftest import compare_have_want
import rsm


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        Theorem contents.

        ::

        :lemma:

        And a lemma.

        ::

        :theorem:

        Another theorem.

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

        <p class="paragraph"><span class="span"><strong>Theorem 1. </strong></span>Theorem contents.</p>

        </div>

        </div>

        <div class="lemma">

        <div class="lemma-contents">

        <p class="paragraph"><span class="span"><strong>Lemma 1. </strong></span>And a lemma.</p>

        </div>

        </div>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph"><span class="span"><strong>Theorem 2. </strong></span>Another theorem.</p>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
