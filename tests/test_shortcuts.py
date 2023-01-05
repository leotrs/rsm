import pytest
from conftest import EMPTY_WANT, compare_have_want


def test_one_strong():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has a *shortcut* for strong span.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph has a <span class="span"><strong>shortcut</strong></span> for strong span.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_strong():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has two *shortcuts* for strong *spans*.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph has two <span class="span"><strong>shortcuts</strong></span> for strong <span class="span"><strong>spans</strong></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_one_emphas():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has a /shortcut/ for emphasis span.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph has a <span class="span"><em>shortcut</em></span> for emphasis span.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_one_math():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has some $2+2=4$ awesome math.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph has some <span class="math">\(2+2=4\)</span> awesome math.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_math():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has some $2+2=4$ awesome math and also some math that $2 + 2 + 2
        + 2 + 2 = 10$ is broken down.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <h1>My Title</h1>

        <p class="paragraph">This paragraph has some <span class="math">\(2+2=4\)</span> awesome math and also some math that <span class="math">\(2 + 2 + 2
        + 2 + 2 = 10\)</span> is broken down.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_mathblock():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph is followed by display math

        $$2 + 2 = 4.$$

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph is followed by display math</p>

        <div class="mathblock">
        $$
        2 + 2 = 4.
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_section_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        # My Section
          :label: my-sec

        This section contains a shortcut

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <section id="my-sec" class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">This section contains a shortcut</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_subsubsection_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        # My Section

        Foo.

        ## My Subsection

        Bar.

        ### My Subsubsection

        Baz.

        ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <section class="section level-2">

        <h2>1. My Section</h2>

        <p class="paragraph">Foo.</p>

        <section class="subsection level-3">

        <h3>1.1. My Subsection</h3>

        <p class="paragraph">Bar.</p>

        <section class="subsubsection level-4">

        <h4>1.1.1. My Subsubsection</h4>

        <p class="paragraph">Baz.</p>

        </section>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_claim_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains a :|-: claim with a turnstile::. And also another one :⊢: but it takes
        multiple lines::.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph contains a <span class="construct claim"><span class="keyword">⊢ </span>claim with a turnstile</span>. And also another one <span class="construct claim"><span class="keyword">⊢ </span>but it takes multiple lines</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_prev_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        All $X$ are $Y$.

        ::

        :proof:

        :step:
          :label: st1
          All $X$ are $Z$ and all $Z$ are $Y$.
        ::

        :step: :qed:.

           :p: Due to :prev:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div id="st1" class="step">

        <div class="statement">

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Z\)</span> and all <span class="math">\(Z\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph"><span class="construct qed"><span class="keyword">QED </span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">Due to <a class="reference" href="#st1">Step 1</a>.</p>

        </div>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_prev2_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        All $X$ are $Y$.

        ::

        :proof:

        :step:
          :label: st1
          All $X$ are $Z$ and all $Z$ are $Y$.
        ::

        :step:
          :label: st2
          Something inconsequential here.
        ::

        :step: :qed:.

           :p: Due to :prev2:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div id="st1" class="step">

        <div class="statement">

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Z\)</span> and all <span class="math">\(Z\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div id="st2" class="step">

        <div class="statement">

        <p class="paragraph">Something inconsequential here.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph"><span class="construct qed"><span class="keyword">QED </span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">Due to <a class="reference" href="#st1">Step 1</a>.</p>

        </div>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_prev_and_prev2_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        :theorem:

        All $X$ are $Y$.

        ::

        :proof:

        :step:
          :label: st1
          All $X$ are $Z$.
        ::

        :step:
          :label: st2
          All $Z$ are $Y$.
        ::

        :step: :qed:.

           :p: Due to :prev: and :prev2:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div id="st1" class="step">

        <div class="statement">

        <p class="paragraph">All <span class="math">\(X\)</span> are <span class="math">\(Z\)</span>.</p>

        </div>

        </div>

        <div id="st2" class="step">

        <div class="statement">

        <p class="paragraph">All <span class="math">\(Z\)</span> are <span class="math">\(Y\)</span>.</p>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph"><span class="construct qed"><span class="keyword">QED </span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">Due to <a class="reference" href="#st2">Step 2</a> and <a class="reference" href="#st1">Step 1</a>.</p>

        </div>

        </div>

        </div>

        </div>

        <div class="halmos"></div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_code_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        This is inline code`comp = [abs(x) for x in range(10)]`.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is inline code
        <span class="code"><code>comp = [abs(x) for x in range(10)]</code></span>
        .</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_codeblock_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        ```
        comp = [abs(x) for x in range(10)]
        ```

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="codeblock">

        <pre>
        <code>comp = [abs(x) for x in range(10)]</code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_hashtag_not_at_the_start_of_line():
    compare_have_want(
        have=r"""        :manuscript:

        # This is a section title

        And \# this is not!

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <section class="section level-2">

        <h2>1. This is a section title</h2>

        <p class="paragraph">And # this is not!</p>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_escaped_colon_behind_halmos():
    compare_have_want(
        have=r"""        :manuscript:

        Shortcut right beside an escaped colon :span: {:emphas:} foo\:::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">Shortcut right beside an escaped colon <span class="span"><em>foo:</em></span></p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_escaped_colon_behind_halmos_after_shortcut():
    compare_have_want(
        have=r"""        :manuscript:

        Shortcut right beside an escaped colon *foo\:*

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">Shortcut right beside an escaped colon <span class="span"><strong>foo:</strong></span></p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_after_turnstile():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph has math inside a claim :⊢: $2+2=4$::.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This paragraph has math inside a claim <span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(2+2=4\)</span></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_turnstile_and_math_within_list():
    compare_have_want(
        have="""\
        :manuscript:

        We now make a bunch of claims

        :enumerate:

        :item: {:label: one} :⊢: $2+2=4$::.

        :item: {:label: two} :⊢: $3+3=6$::.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">We now make a bunch of claims</p>

        <ol class="enumerate">

        <li id="one" class="item">
        <span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(2+2=4\)</span></span>.
        </li>

        <li id="two" class="item">
        <span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(3+3=6\)</span></span>.
        </li>

        </ol>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_asterisk_inside_math():
    compare_have_want(
        have="""\
        :manuscript:

        $2*2 = 4*1$

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph"><span class="math">\(2*2 = 4*1\)</span></p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_asterisk_inside_code():
    compare_have_want(
        have="""\
        :manuscript:

        `[x**2 for x in range(10)]`

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span class="code"><code>[x**2 for x in range(10)]</code></span>
        </p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_asterisk_inside_mathblock():
    compare_have_want(
        have="""\
        :manuscript:

        $$
        2*2 = 4*1
        $$

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="mathblock">
        $$
        2*2 = 4*1
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_asterisk_inside_codeblock():
    compare_have_want(
        have="""\
        :manuscript:

        ```
        2*2 = 4*1
        ```

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="codeblock">

        <pre>
        <code>2*2 = 4*1</code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
