from conftest import compare_have_want


def test_one_span():
    compare_have_want(
        have="""\
        :manuscript:

        This is a :span: {:strong:} boring :: paragraph.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a <span class="span"><strong>boring</strong></span> paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_spans():
    compare_have_want(
        have="""\
        :manuscript:

        This is a :span: {:strong:} boring :: paragraph, though it has two :span:
        {:emphas:} spans :: so it's less boring.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a <span class="span"><strong>boring</strong></span> paragraph, though it has two <span class="span"><em>spans</em></span> so it's less boring.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_nested():
    compare_have_want(
        have="""\
        :manuscript:

        This is a :span: {:strong:} paragraph with a :span: {:emphas:} span within a span ::
        :: so that makes it really cool.  BTW it also has a Halmos at the start of a
        line!

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a <span class="span"><strong>paragraph with a <span class="span"><em>span within a span</em></span></strong></span> so that makes it really cool.  BTW it also has a Halmos at the start of a line!</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_with_multiline_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This is a paragraph
        with :span: {:strong:,
        :label: lbl} a
        span :: and it is multi line.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a paragraph with <span id="lbl" class="span"><strong>a span</strong></span> and it is multi line.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_with_label():
    compare_have_want(
        have="""\
        :manuscript:

        This is a :span: {:label: myspn, :strong:} boring :: paragraph.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This is a <span id="myspn" class="span"><strong>boring</strong></span> paragraph.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_part_of_word():
    compare_have_want(
        have="""\
        :manuscript:

        This word is half bold :span: {:strong:} bo::ring.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This word is half bold <span class="span"><strong>bo</strong></span>ring.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_part_of_word_with_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        This word is half bold *bo*ring.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <p class="paragraph">This word is half bold <span class="span"><strong>bo</strong></span>ring.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
