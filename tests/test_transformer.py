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

        <p class="paragraph">There are <span id="mylbl" class="span">two</span> spans with the <span class="span">same</span> label in this paragraph.</p>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section</h2>

        <div class="theorem">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section</h2>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        <div class="theorem">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section 1</h2>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        <section class="section level-2">

        <h2>2. Section 2</h2>

        <div class="theorem">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section</h2>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem.</strong></span></p>

        </div>

        </div>

        <div class="theorem">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>Section</h2>

        <div class="theorem">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Section</h2>

        <section class="subsection level-3">

        <h3>1.1. Subsection</h3>

        <div class="theorem">

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


def test_ref_to_unknown_label(caplog):
    compare_have_want(
        have="""\
        :manuscript:

        :ref:foo::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><span class="error">[unknown label "foo"]</span></p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
    assert "Reference to nonexistent label" in caplog.text
