from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: The Perron non-backtracking eigenvalue after node addition
          :date: 2022-03-29

        :author:
          :name: Leo Torres
          :affiliation: Max Planck Institute for Mathematics in the Sciences
          :email: leo@leotrs.com
        ::

        :abstract:
          :keywords: {spectral graph theory, non-backtracking, interlacing}
          :msc: {05C50, 05C82, 15A18, 15B99}

          first
          second
          third

          fourth
          fifth

        ::

        :section:
          :title: Introduction
          :label: sec-introduction
          :types: {t1, t2}

        Lorem ipsum.

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="mylbl" class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>The Perron non-backtracking eigenvalue after node addition</h1>

        <div class="author" data-nodeid="1">

        <p>Leo Torres</p>

        <p>Max Planck Institute for Mathematics in the Sciences</p>

        <p><a href="mailto:leo@leotrs.com">leo@leotrs.com</a></p>

        </div>

        <div class="abstract" data-nodeid="2">

        <h3>Abstract</h3>

        <p class="paragraph" data-nodeid="3">first second third</p>

        <p class="paragraph" data-nodeid="5">fourth fifth</p>

        <p class="keywords">Keywords: spectral graph theory, non-backtracking, interlacing</p>

        <p class="msc">MSC: 05C50, 05C82, 15A18, 15B99</p>

        </div>

        <section id="sec-introduction" class="section level-2 t1 t2" data-nodeid="7">

        <h2>1. Introduction</h2>

        <p class="paragraph" data-nodeid="8">Lorem ipsum.</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
