import pytest
import rsm
from conftest import compare_have_want


def test_numbered_sections():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: First

        Content of first.

        ::

        :section:
          :title: Second

        Content of second.

        ::

        ::
        """,
        want="""\
        <body>

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. First</h2>

        <p class="paragraph">Content of first.</p>

        </section>

        <section class="section level-2">

        <h2>2. Second</h2>

        <p class="paragraph">Content of second.</p>

        </section>

        </section>

        </div>

        </body>
        """,
    )


def test_nonum():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: First

        Content of first.

        ::

        :section:
          :title: Second
          :nonum:

        Content of second.

        ::

        :section:
          :title: Third

        Content of third.

        ::

        ::
        """,
        want="""\
        <body>

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. First</h2>

        <p class="paragraph">Content of first.</p>

        </section>

        <section class="section level-2">

        <h2>Second</h2>

        <p class="paragraph">Content of second.</p>

        </section>

        <section class="section level-2">

        <h2>2. Third</h2>

        <p class="paragraph">Content of third.</p>

        </section>

        </section>

        </div>

        </body>
        """,
    )
