from conftest import compare_have_want


def test_codeblock():
    compare_have_want(
        have="""\
        :manuscript:

        :codeblock:
          :label: some-code
          :types: python

          comp = [abs(x) for x in range(10)]

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <div id="some-code" class="codeblock python">
        comp = [abs(x) for x in range(10)]
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

        <p class="paragraph"><span id="1" class="code">k=v</span></p>

        <p class="paragraph"><span id="2" class="code">k=v</span></p>

        <div id="3" class="codeblock">
        k = v
        </div>

        <div id="4" class="codeblock">
        k = v
        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
