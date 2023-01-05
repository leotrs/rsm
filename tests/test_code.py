from conftest import compare_have_want


def test_code():
    compare_have_want(
        have="""\
        :manuscript:

        :code: comp = [abs(x) for x in range(10)] ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span class="code"><code>comp = [abs(x) for x in range(10)]</code></span>
        </p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_code_with_shorthand():
    compare_have_want(
        have="""\
        :manuscript:

        `comp = [abs(x) for x in range(10)]`

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span class="code"><code>comp = [abs(x) for x in range(10)]</code></span>
        </p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_code_with_lang():
    compare_have_want(
        have="""\
        :manuscript:

        :code: {:lang: python}
          comp = [abs(x) for x in range(10)]
        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span class="code"><code class="highlight python"><span class="n">comp</span> <span class="o">=</span> <span class="p">[</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
        </code></span>
        </p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_code_with_shorthand_and_lang():
    compare_have_want(
        have="""\
        :manuscript:

        `{:lang: python} comp = [abs(x) for x in range(10)]`

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span class="code"><code class="highlight python"><span class="n">comp</span> <span class="o">=</span> <span class="p">[</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
        </code></span>
        </p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_codeblock():
    compare_have_want(
        have="""\
        :manuscript:

        :codeblock:

          comp = [abs(x) for x in range(10)]

        ::

        ::
        """,
        want="""\
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


def test_codeblock_with_lang():
    compare_have_want(
        have="""\
        :manuscript:

        :codeblock:
          :lang: python

          comp = [abs(x) for x in range(10)]

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="codeblock">

        <pre>
        <code class="highlight python"><span class="n">comp</span> <span class="o">=</span> <span class="p">[</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
        </code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_codeblock_with_shorthand():
    compare_have_want(
        have="""\
        :manuscript:

        ```
        comp = [abs(x) for x in range(10)]
        ```

        ::
        """,
        want="""\
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


def test_codeblock_with_shorthand_and_lang():
    compare_have_want(
        have="""\
        :manuscript:

        ```
        :lang: python

        comp = [abs(x) for x in range(10)]

        ```

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div class="codeblock">

        <pre>
        <code class="highlight python"><span class="n">comp</span> <span class="o">=</span> <span class="p">[</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
        </code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_meta():
    compare_have_want(
        have="""\
        :manuscript:

        `{:label: 1}k=v`

        :code:{:label: 2}k=v::

        :codeblock:
          :label: 3
          k = v
        ::

        ```
          :label: 4
          k = v
        ```

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span id="1" class="code"><code>k=v</code></span>
        </p>

        <p class="paragraph">
        <span id="2" class="code"><code>k=v</code></span>
        </p>

        <div id="3" class="codeblock">

        <pre>
        <code>k = v</code>
        </pre>

        </div>

        <div id="4" class="codeblock">

        <pre>
        <code>k = v</code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_meta_and_lang():
    compare_have_want(
        have="""\
        :manuscript:

        `{:label: 1, :lang: js}k=v`

        :code:{:label: 2, :lang: js}k=v::

        :codeblock:
          :label: 3
          :lang: js
          k = v
        ::

        ```
          :label: 4
          :lang: js
          k = v
        ```

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">
        <span id="1" class="code"><code class="highlight js"><span class="nx">k</span><span class="o">=</span><span class="nx">v</span>
        </code></span>
        </p>

        <p class="paragraph">
        <span id="2" class="code"><code class="highlight js"><span class="nx">k</span><span class="o">=</span><span class="nx">v</span>
        </code></span>
        </p>

        <div id="3" class="codeblock">

        <pre>
        <code class="highlight js"><span class="nx">k</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">v</span>
        </code>
        </pre>

        </div>

        <div id="4" class="codeblock">

        <pre>
        <code class="highlight js"><span class="nx">k</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">v</span>
        </code>
        </pre>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
