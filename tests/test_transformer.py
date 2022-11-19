import pytest
from conftest import compare_have_want
import rsm


def test_duplicate_label_warning(caplog):
    compare_have_want(
        have="""\
        :manuscript:
          :title: Title

        There are :span: {:label: mylbl} two :: spans with the :span: {:label: mylbl}
        same :: label in this paragraph.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>Title</h1>

        <p class="paragraph">There are <span id="mylbl" class="span">two </span> spans with the <span class="span">same </span> label in this paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert 'Duplicate label mylbl' in caplog.text


def test_duplicate_bibtex_item_warning(caplog):
    compare_have_want(
        have="""\
        :manuscript:

        :bibliography: ::

        ::


        :bibtex:

        @article{torres2020,
          title={Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization},
          author={Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina},
          journal={SIAM Journal on Mathematics of Data Science},
          year={2021},
        }

        @book{torres2020,
          title={Foo},
          author={Bar},
          journal={Baz},
          year={Bug},
        }

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography">

        <li id="torres2020" class="bibitem">
        Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina. "Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization". SIAM Journal on Mathematics of Data Science. 2021.
        </li>

        <li class="bibitem">
        Bar. "Foo". . Bug.
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert 'Duplicate label torres2020' in caplog.text
