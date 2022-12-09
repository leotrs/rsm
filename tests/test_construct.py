from conftest import compare_have_want


def test_real_life_example():
    compare_have_want(
        have=r"""        :manuscript:
        :title: A simple proof

        :let: $G$ be a simple graph::.  We will prove a fundamental fact about its structure.
        :define: $L(G) := |E(G)|$, where $E(G)$ is the set of edges of $G$:: and :write:
        $\deg(u)$ for the degree of a node $u \in V(G)$::.

        :theorem:
        :label: thm-main
        :goal: eqn-thm
        :types: {important, main}

          $$
          :label: eqn-thm
          :isclaim:
            \sum_{u \in V(G)} \deg(u) = 2L(G).
          $$

        ::

        :proof:

          :step: :define: $n = |V(G)|$.:: ::

          :step: :case: $n = 1$.::

            :step: :claim: $L(G) = 0$ ::.

              :p: $G$ has no self-loops by assumption.::

            ::

            :step: :let: $u \in V(G)$::, :then: $\deg(u) = 0$::.

              :p: Since $G$ has only one node, and it has no self-loops.::

            ::

            :step: :qed:
            ::

          ::

          :step: :let: $v \notin V(G)$::.  :write: $H$ for the graph resulting from adding $v$
            to $G$::. SUFFICES :assume: :span: :span:{:label: asm} the theorem is true for $G$
            ::::::, :prove: the theorem is true for $H$::.

            :p: By induction. ::

          ::

          :step: :define: $\deg_G(u), \deg_H(u)$ as the degree of node $u$ in
            $G$ and $H$ respectively.:: Note $\deg_G(v) = 0$. ::

          :step:
          :label: stp-edges
            :claim: $L(H) = L(G) + \deg_H(v)$::.

            :p: Because the only added edges are those incident to $v$.::

          ::

          :step:
          :label: stp-sum
            :claim: $\sum_{u \in V(H)} \deg_H(u) = 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u)$::.

            :step: :write: $W \subset V(G)$ for the set of neighbors of $v$.::::

            :step:

              $$
              :isclaim:
                \begin{align}
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in V(H)\setminus\{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} \deg_H(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} (\deg_G(u) + 1) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in W} \deg_G(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u),
                \end{align}
              $$

              where in the right-most term in third equation we have used the fact that for
              every node $u$ in $V(G) \setminus W \setminus v$ we have $\deg_H(u) = \deg_G(u)$.

            ::

          ::

          :step: :qed:

            :p:

              $$
              :isclaim:
                \begin{align}
                2 L(G) &= \sum_{u \in V(G)} \deg_G(u) \\
                2 L(G) + 2 \deg_H(v) &=  2 \deg_H(v) + \sum_{u \in V(G)} \deg_G(u) \\
                2 L(H) &=  \sum_{u \in V(H)} \deg_H(u),
                \end{align}
              $$

              where the first equation is true by :ref:asm,induction hypothesis::, and the last
              equation is due to :prev2: and :prev:.

            ::

          ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1>A simple proof</h1>

        <p class="paragraph"><span class="construct let assumption"><span class="keyword">LET </span><span class="math">\(G\)</span> be a simple graph</span>.  We will prove a fundamental fact about its structure. <span class="construct define assumption"><span class="keyword">DEFINE </span><span class="math">\(L(G) := |E(G)|\)</span>, where <span class="math">\(E(G)\)</span> is the set of edges of <span class="math">\(G\)</span></span> and <span class="construct write assumption"><span class="keyword">WRITE </span><span class="math">\(\deg(u)\)</span> for the degree of a node <span class="math">\(u \in V(G)\)</span></span>.</p>

        <div id="thm-main" class="theorem important main">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.</strong></span></p>

        <div class="claimblock">
        <span class="keyword">⊢ </span>
        <div id="eqn-thm" class="mathblock">
        $$
        \sum_{u \in V(G)} \deg(u) = 2L(G).
        $$
        <div class="mathblock__number">(1)</div>

        </div>

        </div>

        </div>

        </div>

        <div class="proof">

        <p class="paragraph proof__title"><span class="span"><strong>Proof. </strong></span></p>

        <div class="proof-contents">

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct define assumption"><span class="keyword">DEFINE </span><span class="math">\(n = |V(G)|\)</span>.</span></p>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct case assumption"><span class="keyword">CASE </span><span class="math">\(n = 1\)</span>.</span></p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(L(G) = 0\)</span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph"><span class="math">\(G\)</span> has no self-loops by assumption.</p>

        </div>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct let assumption"><span class="keyword">LET </span><span class="math">\(u \in V(G)\)</span></span>, <span class="construct then"><span class="keyword">THEN </span><span class="math">\(\deg(u) = 0\)</span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">Since <span class="math">\(G\)</span> has only one node, and it has no self-loops.</p>

        </div>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct qed"><span class="keyword">QED </span></span></p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct let assumption"><span class="keyword">LET </span><span class="math">\(v \notin V(G)\)</span></span>. <span class="construct write assumption"><span class="keyword">WRITE </span><span class="math">\(H\)</span> for the graph resulting from adding <span class="math">\(v\)</span> to <span class="math">\(G\)</span></span>. SUFFICES <span class="construct assume assumption"><span class="keyword">ASSUME </span><span class="span"><span id="asm" class="span">the theorem is true for <span class="math">\(G\)</span></span></span></span>, <span class="construct prove assumption"><span class="keyword">PROVE </span>the theorem is true for <span class="math">\(H\)</span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">By induction.</p>

        </div>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct define assumption"><span class="keyword">DEFINE </span><span class="math">\(\deg_G(u), \deg_H(u)\)</span> as the degree of node <span class="math">\(u\)</span> in <span class="math">\(G\)</span> and <span class="math">\(H\)</span> respectively.</span> Note <span class="math">\(\deg_G(v) = 0\)</span>.</p>

        </div>

        </div>

        <div id="stp-edges" class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(L(H) = L(G) + \deg_H(v)\)</span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <p class="paragraph">Because the only added edges are those incident to <span class="math">\(v\)</span>.</p>

        </div>

        </div>

        </div>

        <div id="stp-sum" class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct claim"><span class="keyword">⊢ </span><span class="math">\(\sum_{u \in V(H)} \deg_H(u) = 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u)\)</span></span>.</p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <div class="step">

        <div class="statement">

        <p class="paragraph"><span class="construct write assumption"><span class="keyword">WRITE </span><span class="math">\(W \subset V(G)\)</span> for the set of neighbors of <span class="math">\(v\)</span>.</span></p>

        </div>

        </div>

        <div class="step">

        <div class="statement">

        <div class="claimblock">
        <span class="keyword">⊢ </span>
        <div class="mathblock">
        $$
        \begin{align}
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in V(H)\setminus\{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} \deg_H(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} (\deg_G(u) + 1) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in W} \deg_G(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u),
                \end{align}
        $$
        <div class="mathblock__number">(2)</div>

        </div>

        </div>

        <p class="paragraph">where in the right-most term in third equation we have used the fact that for every node <span class="math">\(u\)</span> in <span class="math">\(V(G) \setminus W \setminus v\)</span> we have <span class="math">\(\deg_H(u) = \deg_G(u)\)</span>.</p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step last">

        <div class="statement">

        <p class="paragraph"><span class="construct qed"><span class="keyword">QED </span></span></p>

        </div>

        <div class="subproof">

        <div class="subproof-contents">

        <div class="claimblock">
        <span class="keyword">⊢ </span>
        <div class="mathblock">
        $$
        \begin{align}
                2 L(G) &= \sum_{u \in V(G)} \deg_G(u) \\
                2 L(G) + 2 \deg_H(v) &=  2 \deg_H(v) + \sum_{u \in V(G)} \deg_G(u) \\
                2 L(H) &=  \sum_{u \in V(H)} \deg_H(u),
                \end{align}
        $$
        <div class="mathblock__number">(3)</div>

        </div>

        </div>

        <p class="paragraph">where the first equation is true by <a class="reference" href="#asm">induction hypothesis</a>, and the last equation is due to <a class="reference" href="#stp-edges">Step 5</a> and <a class="reference" href="#stp-sum">Step 6</a>.</p>

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
