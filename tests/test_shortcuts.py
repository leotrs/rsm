from conftest import compare_have_want, EMPTY_WANT


def test_one_strong():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has a **shortcut** for strong span.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

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

        This paragraph has two **shortcuts** for strong **spans**.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

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

        This paragraph has a *shortcut* for emphasis span.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

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

        <div id="manuscript" class="manuscript">

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

        <div id="manuscript" class="manuscript">

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This paragraph is followed by display math
        </p>

        <div class="mathblock">
        $$
        2 + 2 = 4.
        $$
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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

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

        This paragraph contains a |- claim with a turnstile. And also another one ⊢ but it takes
        multiple lines.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This paragraph contains a <span class="claim"><span class="keyword">⊢ </span>claim with a turnstile</span>. And also another one <span class="claim"><span class="keyword">⊢ </span>but it takes
        multiple lines</span>.</p>

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

        :step: :label: st1 :: All $X$ are $Z$ and all $Z$ are $Y$.::

        :step: QED.

           :p: Due to :prev:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1. </strong></span></p>

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

        <p class="paragraph"><span class="keyword">QED </span>.</p>

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

        :step: :label: st1 :: All $X$ are $Z$ and all $Z$ are $Y$.::

        :step: :label: st2 :: Something inconsequential here.::

        :step: QED.

           :p: Due to :prev2:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1. </strong></span></p>

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

        <p class="paragraph"><span class="keyword">QED </span>.</p>

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

        :step: :label: st1 :: All $X$ are $Z$.::

        :step: :label: st2 :: All $Z$ are $Y$.::

        :step: QED.

           :p: Due to :prev: and :prev2:.::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1. </strong></span></p>

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

        <p class="paragraph"><span class="keyword">QED </span>.</p>

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

        This is inline code `comp = [abs(x) for x in range(10)]`.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">This is inline code <span class="code">comp = [abs(x) for x in range(10)]</span>.</p>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="codeblock">
        comp = [abs(x) for x in range(10)]


        </div>

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

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div class="codeblock">
        comp = [abs(x) for x in range(10)]


        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_comment_one_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        % comment

        ::
        """,
        want=EMPTY_WANT,
    )


def test_comment_multi_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        % this is a
        % multi line comment

        ::
        """,
        want=EMPTY_WANT,
    )


def test_comment_multi_line_comment():
    compare_have_want(
        have="""\
        :manuscript:

        Foo.% this is a comment at the end of a line

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph">Foo.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_asterisk_inside_math():
    raise NotImplementedError


def test_asterisk_inside_code():
    raise NotImplementedError


def test_asterisk_inside_mathblock():
    raise NotImplementedError


def test_asterisk_inside_codeblock():
    raise NotImplementedError
