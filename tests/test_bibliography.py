import pytest
from conftest import compare_have_want


def test_single():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This has a citation at the end. :cite:knuth::

        :bibliography: ::

        ::


        :bibtex:

        @book{knuth,
          title={Art of computer programming, volume 2, Seminumerical algorithms},
          author={Knuth, Donald E},
          year={2014},
          publisher={Addison-Wesley Professional}
        }

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This has a citation at the end. [<a id="cite-0" class="reference" href="#knuth">1</a>]</p>

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography">

        <li id="knuth" class="bibitem">
        Knuth, Donald E. "Art of computer programming, volume 2, Seminumerical algorithms". Addison-Wesley Professional. 2014.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_with_shortcuts():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This has a *citation* at the end. :cite:knuth::

        :bibliography: ::

        ::


        :bibtex:

        @book{knuth,
          title={Art of computer programming, volume 2: Seminumerical algorithms},
          author={Knuth, Donald E},
          year={2014},
          publisher={Addison-Wesley Professional}
        }

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This has a <span class="span"><strong>citation</strong></span> at the end. [<a id="cite-0" class="reference" href="#knuth">1</a>]</p>

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography">

        <li id="knuth" class="bibitem">
        Knuth, Donald E. "Art of computer programming, volume 2: Seminumerical algorithms". Addison-Wesley Professional. 2014.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_many():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This has a citation at the end. :cite:torres2020,knuth::

        :bibliography: ::

        ::


        :bibtex:

        @article{torres2020,
          title={Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization},
          author={Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina},
          journal={SIAM Journal on Mathematics of Data Science},
          volume={3},
          number={2},
          year={2021},
        }

        @book{knuth,
          title={Art of computer programming, volume 2: Seminumerical algorithms},
          author={Knuth, Donald E},
          year={2014},
          publisher={Addison-Wesley Professional}
        }

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This has a citation at the end. [<a id="cite-0" class="reference" href="#torres2020">1</a>, <a id="cite-0" class="reference" href="#knuth">2</a>]</p>

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography">

        <li id="torres2020" class="bibitem">
        Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina. "Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization". SIAM Journal on Mathematics of Data Science. 2021.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        <li id="knuth" class="bibitem">
        Knuth, Donald E. "Art of computer programming, volume 2: Seminumerical algorithms". Addison-Wesley Professional. 2014.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_order():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This has a citation at the end. :cite:knuth,torres2020::

        :bibliography: ::

        ::


        :bibtex:

        @article{torres2020,
          title={Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization},
          author={Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina},
          journal={SIAM Journal on Mathematics of Data Science},
          volume={3},
          number={2},
          year={2021},
        }

        @book{knuth,
          title={Art of computer programming, volume 2: Seminumerical algorithms},
          author={Knuth, Donald E},
          year={2014},
          publisher={Addison-Wesley Professional}
        }

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This has a citation at the end. [<a id="cite-0" class="reference" href="#knuth">2</a>, <a id="cite-0" class="reference" href="#torres2020">1</a>]</p>

        <section class="level-2">

        <h2>References</h2>

        <ol class="bibliography">

        <li id="torres2020" class="bibitem">
        Torres, Leo and Chan, Kevin S and Tong, Hanghang and Eliassi-Rad, Tina. "Nonbacktracking eigenvalues under node removal: X-centrality and targeted immunization". SIAM Journal on Mathematics of Data Science. 2021.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        <li id="knuth" class="bibitem">
        Knuth, Donald E. "Art of computer programming, volume 2: Seminumerical algorithms". Addison-Wesley Professional. 2014.<br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
