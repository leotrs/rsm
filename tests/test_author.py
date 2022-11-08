from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: My Title
          :date: 2022-03-29

        :author:
          :name: Leo Torres
          :affiliation: Max Planck Institute for Mathematics in the Sciences
          :email: leo@leotrs.com
        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="mylbl" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <div class="author">

        <p>Leo Torres
        Max Planck Institute for Mathematics in the Sciences
        leo@leotrs.com</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_empty_author():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: The Perron non-backtracking eigenvalue after node addition
          :date: 2022-03-29

        :author: ::

        Lorem ipsum.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="mylbl" class="manuscript">

        <section class="level-1">

        <h1>The Perron non-backtracking eigenvalue after node addition</h1>

        <div class="author">

        </div>

        <p class="paragraph">Lorem ipsum.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
