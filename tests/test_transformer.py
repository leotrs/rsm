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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>Title</h1>

        <p class="paragraph" data-nodeid="1">There are <span id="mylbl" class="span" data-nodeid="3">two</span> spans with the <span class="span" data-nodeid="6">same</span> label in this paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert "Duplicate label mylbl" in caplog.text


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

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography" data-nodeid="1">

        <li id="torres2020" class="bibitem" data-nodeid="2">
        Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina. "Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization". SIAM Journal on Mathematics of Data Science. 2021.
        </li>

        <li class="bibitem" data-nodeid="3">
        Bar. "Foo". Bug.
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert "Duplicate label torres2020" in caplog.text


def test_theorem_within_section():
    compare_have_want(
        have="""\
        :manuscript:

        # Section

        :theorem:

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <div class="theorem" data-nodeid="2">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_theorems_same_section():
    compare_have_want(
        have="""\
        :manuscript:

        # Section

        :theorem:

        ::

        :theorem:

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <div class="theorem" data-nodeid="2">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        <div class="theorem" data-nodeid="3">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.2.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_theorems_different_sections():
    compare_have_want(
        have="""\
        :manuscript:

        # Section 1

        :theorem:

        ::

        ::

        # Section 2

        :theorem:

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section 1</h2>

        <div class="theorem" data-nodeid="2">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        <section class="section level-2" data-nodeid="3">

        <h2>2. Section 2</h2>

        <div class="theorem" data-nodeid="4">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 2.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_theorems_same_section_nonum():
    compare_have_want(
        have="""\
        :manuscript:

        # Section

        :theorem:
        :nonum:

        ::

        :theorem:

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <div class="theorem" data-nodeid="2">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem.</strong></span></p>

        </div>

        </div>

        <div class="theorem" data-nodeid="3">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_theorem_inside_section_with_nonum():
    compare_have_want(
        have="""\
        :manuscript:

        # Section
        :nonum:

        :theorem:

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>Section</h2>

        <div class="theorem" data-nodeid="2">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_theorem_inside_subsection():
    compare_have_want(
        have="""\
        :manuscript:

        # Section

        ## Subsection

        :theorem:

        ::

        ::

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <section class="subsection level-3" data-nodeid="2">

        <h3>1.1. Subsection</h3>

        <div class="theorem" data-nodeid="3">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
