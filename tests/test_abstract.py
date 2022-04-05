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
          :MSC: {05C50, 05C82, 15A18, 15B99}

          Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum.

          Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum.

        ::

        :section:
          :title: Introduction
          :label: sec:introduction
          :types: {t1, t2}

        Lorem ipsum.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="mylbl" class="manuscript">
        <section class="level-1">
        <h1>The Perron non-backtracking eigenvalue after node addition</h1>
        <div class="author">
        <p>
        Leo Torres
        Max Planck Institute for Mathematics in the Sciences
        leo@leotrs.com
        </p>

        </div><div class="abstract">
        <h3>Abstract</h3>
        <p class="paragraph">Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum.</p><p class="paragraph">Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem
          ipsum. Lorem ipsum.</p><p class="keywords">
        Keywords: spectral graph theory, non-backtracking, interlacing
        </p>
        <p class="MSC">
        MSC: 05C50, 05C82, 15A18, 15B99
        </p>

        </div><section id="sec:introduction" class="section level-2 t1 t2">
        <h2>1. Introduction</h2>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </section>
        </div>
        </body>
        """
    )
