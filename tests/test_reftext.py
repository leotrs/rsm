from conftest import compare_have_want
import rsm


def test_mechanism():
    cls = rsm.nodes.Section
    node = cls()
    assert node.classreftext == cls.classreftext
    assert node.reftext == cls.classreftext

    node.reftext = 'foobar'
    assert node.classreftext == cls.classreftext
    assert node.reftext == 'foobar'

    node = cls(customreftext='foobar')
    assert node.classreftext == cls.classreftext
    assert node.reftext == 'foobar'


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :mathblock:
          :label: eqn
          :reftext: Important Equation
          2+2=4
        ::

        Here we refer to the :ref:eqn::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div id="eqn" class="mathblock">
        $$
        2+2=4
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        <p class="paragraph">Here we refer to the <a class="reference" href="#eqn">Important Equation</a>.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )
