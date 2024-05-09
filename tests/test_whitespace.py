from conftest import compare_have_want


def test_one_word():
    compare_have_want(
        have="""
        :manuscript:

        This should be a single wo:span:{:strong:}rd::.

        This should be a single :span:{:strong:}wo::rd.

        This should be a single w:span:{:strong:}or::d.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This should be a single wo<span class="span" data-nodeid="3"><strong>rd</strong></span>.</p>

        <p class="paragraph" data-nodeid="6">This should be a single <span class="span" data-nodeid="8"><strong>wo</strong></span>rd.</p>

        <p class="paragraph" data-nodeid="11">This should be a single w<span class="span" data-nodeid="13"><strong>or</strong></span>d.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_one_word_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        This should be a single wo*rd*.

        This should be a single *wo*rd.

        This should be a single w*or*d.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This should be a single wo<span class="span" data-nodeid="3"><strong>rd</strong></span>.</p>

        <p class="paragraph" data-nodeid="6">This should be a single <span class="span" data-nodeid="8"><strong>wo</strong></span>rd.</p>

        <p class="paragraph" data-nodeid="11">This should be a single w<span class="span" data-nodeid="13"><strong>or</strong></span>d.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_period_after():
    compare_have_want(
        have="""
        :manuscript:

        Period after math :math:2+2=4::.

        Period after code:code:k=v::.

        Period after claim :claim:foo::.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Period after math <span class="math" data-nodeid="3">\(2+2=4\)</span>.</p>

        <p class="paragraph" data-nodeid="6">Period after code
        <span class="code" data-nodeid="8"><code>k=v</code></span>
        .</p>

        <p class="paragraph" data-nodeid="11">Period after claim <span class="construct claim" data-nodeid="13"><span class="keyword" data-nodeid="14">⊢ </span>foo</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_period_after_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        Period after math $2+2=4$.

        Period after code`k=v`.

        Period after claim :|-:foo::.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Period after math <span class="math" data-nodeid="3">\(2+2=4\)</span>.</p>

        <p class="paragraph" data-nodeid="6">Period after code
        <span class="code" data-nodeid="8"><code>k=v</code></span>
        .</p>

        <p class="paragraph" data-nodeid="11">Period after claim <span class="construct claim" data-nodeid="13"><span class="keyword" data-nodeid="14">⊢ </span>foo</span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_separate_words():
    compare_have_want(
        have="""
        :manuscript:

        :span:{:strong:}Separate:: words.

        Separate :span:{:strong:}words::.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1"><span class="span" data-nodeid="2"><strong>Separate</strong></span> words.</p>

        <p class="paragraph" data-nodeid="5">Separate <span class="span" data-nodeid="7"><strong>words</strong></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_separate_words_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        *Separate* words.

        Separate *words*.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1"><span class="span" data-nodeid="2"><strong>Separate</strong></span> words.</p>

        <p class="paragraph" data-nodeid="5">Separate <span class="span" data-nodeid="7"><strong>words</strong></span>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_multiline_content_middle_of_line():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph
        with :span: {:strong:} a
        span :: that takes multiple lines

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="span" data-nodeid="3"><strong>a span</strong></span> that takes multiple lines</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_multiline_content_beginning_of_line():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph with
        :span: {:strong:} a
        span :: that takes multiple lines

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="span" data-nodeid="3"><strong>a span</strong></span> that takes multiple lines</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_multiline_content_beginning_of_line_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph with
        * a
        span * that takes multiple lines

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="span" data-nodeid="3"><strong>a span</strong></span> that takes multiple lines</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_span_multiline_content_middle_of_line_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph
        with * a
        span * that takes multiple lines

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="span" data-nodeid="3"><strong>a span</strong></span> that takes multiple lines</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_start_of_line():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph with
        :math:2+2=4:: at the start of a line.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="math" data-nodeid="3">\(2+2=4\)</span> at the start of a line.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_start_of_line_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        This is a paragraph with
        $2+2=4$ at the start of a line.

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">This is a paragraph with <span class="math" data-nodeid="3">\(2+2=4\)</span> at the start of a line.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_table_tr():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td: /foo/ :: :td: *bar* :: ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <table class="table" data-nodeid="1">

        <tbody class="tablebody" data-nodeid="2">

        <tr class="tablerow" data-nodeid="3">

        <td class="tabledatum" data-nodeid="4"><span class="span" data-nodeid="5"><em>foo</em></span></td>

        <td class="tabledatum" data-nodeid="7"><span class="span" data-nodeid="8"><strong>bar</strong></span></td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_table_trshort():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: /foo/ : *bar* ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <table class="table" data-nodeid="1">

        <tbody class="tablebody" data-nodeid="2">

        <tr class="tablerow" data-nodeid="3">

        <td class="tabledatum" data-nodeid="4"><span class="span" data-nodeid="5"><em>foo</em></span></td>

        <td class="tabledatum" data-nodeid="7"><span class="span" data-nodeid="8"><strong>bar</strong></span></td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_ignore_space_within_inline():
    compare_have_want(
        have="""
        :manuscript:

        Ignore space :span: {:strong:} within :: inline.

        Ignore space :span: {:strong:}   within   :: inline.

        Ignore space :claim: within :: inline.

        Ignore space :claim:   within   :: inline.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Ignore space <span class="span" data-nodeid="3"><strong>within</strong></span> inline.</p>

        <p class="paragraph" data-nodeid="6">Ignore space <span class="span" data-nodeid="8"><strong>within</strong></span> inline.</p>

        <p class="paragraph" data-nodeid="11">Ignore space <span class="construct claim" data-nodeid="13"><span class="keyword" data-nodeid="14">⊢ </span>within</span> inline.</p>

        <p class="paragraph" data-nodeid="18">Ignore space <span class="construct claim" data-nodeid="20"><span class="keyword" data-nodeid="21">⊢ </span>within</span> inline.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_ignore_space_within_inline_with_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        Ignore space * within * inline.

        Ignore space *   within   * inline.

        Ignore space :|-: within ::. inline.

        Ignore space :|-:   within   ::. inline.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Ignore space <span class="span" data-nodeid="3"><strong>within</strong></span> inline.</p>

        <p class="paragraph" data-nodeid="6">Ignore space <span class="span" data-nodeid="8"><strong>within</strong></span> inline.</p>

        <p class="paragraph" data-nodeid="11">Ignore space <span class="construct claim" data-nodeid="13"><span class="keyword" data-nodeid="14">⊢ </span>within</span>. inline.</p>

        <p class="paragraph" data-nodeid="18">Ignore space <span class="construct claim" data-nodeid="20"><span class="keyword" data-nodeid="21">⊢ </span>within</span>. inline.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_consecutive_lines_should_be_joined_by_spaces():
    compare_have_want(
        have="""
        :manuscript:

        Consecutive lines should be
        joined by spaces.

        Consecutive lines should :span:{:strong:}be
        joined:: by spaces.

        Consecutive lines should *be
        joined* by spaces.

        Consecutive lines should be
        :span:{:strong:}joined:: by spaces.

        Consecutive lines should be
        *joined* by spaces.

        Consecutive lines should *be*
        joined by spaces.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <p class="paragraph" data-nodeid="1">Consecutive lines should be joined by spaces.</p>

        <p class="paragraph" data-nodeid="3">Consecutive lines should <span class="span" data-nodeid="5"><strong>be joined</strong></span> by spaces.</p>

        <p class="paragraph" data-nodeid="8">Consecutive lines should <span class="span" data-nodeid="10"><strong>be joined</strong></span> by spaces.</p>

        <p class="paragraph" data-nodeid="13">Consecutive lines should be <span class="span" data-nodeid="15"><strong>joined</strong></span> by spaces.</p>

        <p class="paragraph" data-nodeid="18">Consecutive lines should be <span class="span" data-nodeid="20"><strong>joined</strong></span> by spaces.</p>

        <p class="paragraph" data-nodeid="23">Consecutive lines should <span class="span" data-nodeid="25"><strong>be</strong></span> joined by spaces.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
