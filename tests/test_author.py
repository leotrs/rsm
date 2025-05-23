from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :rsm:
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

        <div id="mylbl" class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>My Title</h1>

        <div class="author" data-nodeid="1">

        <div class="paragraph">

        <p>Leo Torres</p>

        <p>Max Planck Institute for Mathematics in the Sciences</p>

        <p><a href="mailto:leo@leotrs.com">leo@leotrs.com</a></p>
        </div>
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
        :rsm:
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

        <div id="mylbl" class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>The Perron non-backtracking eigenvalue after node addition</h1>

        <div class="author" data-nodeid="1">

        </div>

        <div class="paragraph" data-nodeid="2">

        <p>Lorem ipsum.</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
