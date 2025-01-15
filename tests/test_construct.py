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
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <h1>A simple proof</h1>

        <div class="paragraph" data-nodeid="1">

        <p><span class="construct let assumption" data-nodeid="2"><span class="keyword" data-nodeid="3">LET </span><span class="math" data-nodeid="5">\(G\)</span> be a simple graph</span>.  We will prove a fundamental fact about its structure. <span class="construct define assumption" data-nodeid="9"><span class="keyword" data-nodeid="10">DEFINE </span><span class="math" data-nodeid="12">\(L(G) := |E(G)|\)</span>, where <span class="math" data-nodeid="15">\(E(G)\)</span> is the set of edges of <span class="math" data-nodeid="18">\(G\)</span></span> and <span class="construct write assumption" data-nodeid="21"><span class="keyword" data-nodeid="22">WRITE </span><span class="math" data-nodeid="24">\(\deg(u)\)</span> for the degree of a node <span class="math" data-nodeid="27">\(u \in V(G)\)</span></span>.</p>

        </div>

        <div id="thm-main" class="theorem important main" data-nodeid="30">

        <div class="paragraph hr-label">

        <p><span class="span"><strong>Theorem 1.</strong></span></p>

        </div>

        <div class="claimblock" data-nodeid="31">
        <span class="keyword" data-nodeid="32">⊢ </span>
        <div id="eqn-thm" class="mathblock" data-nodeid="34">
        $$
        \sum_{u \in V(G)} \deg(u) = 2L(G).
        $$
        </div>

        </div>

        </div>

        <div class="proof" data-nodeid="36">

        <p class="paragraph hr-label"><span class="span"><strong>Proof. </strong></span></p>

        <div class="step" data-nodeid="37">

        <div class="statement" data-nodeid="38">

        <p class="paragraph" data-nodeid="39"><span class="construct define assumption" data-nodeid="40"><span class="keyword" data-nodeid="41">DEFINE </span><span class="math" data-nodeid="43">\(n = |V(G)|\)</span>.</span></p>

        </div>

        </div>

        <div class="step" data-nodeid="46">

        <div class="statement" data-nodeid="47">

        <div class="paragraph" data-nodeid="48">

        <p><span class="construct case assumption" data-nodeid="49"><span class="keyword" data-nodeid="50">CASE </span><span class="math" data-nodeid="52">\(n = 1\)</span>.</span></p>

        </div>

        </div>

        <div class="subproof" data-nodeid="55">

        <div class="step" data-nodeid="56">

        <div class="statement" data-nodeid="57">

        <div class="paragraph" data-nodeid="58">

        <p><span class="construct claim" data-nodeid="59"><span class="keyword" data-nodeid="60">⊢ </span><span class="math" data-nodeid="62">\(L(G) = 0\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="65">

        <div class="paragraph" data-nodeid="66">

        <p><span class="math" data-nodeid="67">\(G\)</span> has no self-loops by assumption.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="70">

        <div class="statement" data-nodeid="71">

        <div class="paragraph" data-nodeid="72">

        <p><span class="construct let assumption" data-nodeid="73"><span class="keyword" data-nodeid="74">LET </span><span class="math" data-nodeid="76">\(u \in V(G)\)</span></span>, <span class="construct then" data-nodeid="79"><span class="keyword" data-nodeid="80">THEN </span><span class="math" data-nodeid="82">\(\deg(u) = 0\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="85">

        <div class="paragraph" data-nodeid="86">

        <p>Since <span class="math" data-nodeid="88">\(G\)</span> has only one node, and it has no self-loops.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="91">

        <div class="statement" data-nodeid="92">

        <div class="paragraph" data-nodeid="93">

        <p><span class="construct qed" data-nodeid="94"><span class="keyword" data-nodeid="95">QED </span></span></p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="97">

        <div class="statement" data-nodeid="98">

        <div class="paragraph" data-nodeid="99">

        <p><span class="construct let assumption" data-nodeid="100"><span class="keyword" data-nodeid="101">LET </span><span class="math" data-nodeid="103">\(v \notin V(G)\)</span></span>. <span class="construct write assumption" data-nodeid="106"><span class="keyword" data-nodeid="107">WRITE </span><span class="math" data-nodeid="109">\(H\)</span> for the graph resulting from adding <span class="math" data-nodeid="112">\(v\)</span> to <span class="math" data-nodeid="115">\(G\)</span></span>. SUFFICES <span class="construct assume assumption" data-nodeid="118"><span class="keyword" data-nodeid="119">ASSUME </span><span class="span" data-nodeid="121"><span id="asm" class="span" data-nodeid="122">the theorem is true for <span class="math" data-nodeid="124">\(G\)</span></span></span></span>, <span class="construct prove assumption" data-nodeid="127"><span class="keyword" data-nodeid="128">PROVE </span>the theorem is true for <span class="math" data-nodeid="131">\(H\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="134">

        <div class="paragraph" data-nodeid="135">

        <p>By induction.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="137">

        <div class="statement" data-nodeid="138">

        <div class="paragraph" data-nodeid="139">

        <p><span class="construct define assumption" data-nodeid="140"><span class="keyword" data-nodeid="141">DEFINE </span><span class="math" data-nodeid="143">\(\deg_G(u), \deg_H(u)\)</span> as the degree of node <span class="math" data-nodeid="146">\(u\)</span> in <span class="math" data-nodeid="149">\(G\)</span> and <span class="math" data-nodeid="152">\(H\)</span> respectively.</span> Note <span class="math" data-nodeid="156">\(\deg_G(v) = 0\)</span>.</p>

        </div>

        </div>

        </div>

        <div id="stp-edges" class="step" data-nodeid="159">

        <div class="statement" data-nodeid="160">

        <div class="paragraph" data-nodeid="161">

        <p><span class="construct claim" data-nodeid="162"><span class="keyword" data-nodeid="163">⊢ </span><span class="math" data-nodeid="165">\(L(H) = L(G) + \deg_H(v)\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="168">

        <div class="paragraph" data-nodeid="169">

        <p>Because the only added edges are those incident to <span class="math" data-nodeid="171">\(v\)</span>.</p>

        </div>

        </div>

        </div>

        <div id="stp-sum" class="step" data-nodeid="174">

        <div class="statement" data-nodeid="175">

        <div class="paragraph" data-nodeid="176">

        <p><span class="construct claim" data-nodeid="177"><span class="keyword" data-nodeid="178">⊢ </span><span class="math" data-nodeid="180">\(\sum_{u \in V(H)} \deg_H(u) = 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u)\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="183">

        <div class="step" data-nodeid="184">

        <div class="statement" data-nodeid="185">

        <div class="paragraph" data-nodeid="186">

        <p><span class="construct write assumption" data-nodeid="187"><span class="keyword" data-nodeid="188">WRITE </span><span class="math" data-nodeid="190">\(W \subset V(G)\)</span> for the set of neighbors of <span class="math" data-nodeid="193">\(v\)</span>.</span></p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="196">

        <div class="statement" data-nodeid="197">

        <div class="claimblock" data-nodeid="198">
        <span class="keyword" data-nodeid="199">⊢ </span>
        <div class="mathblock" data-nodeid="201">
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

        <div class="paragraph" data-nodeid="203">

        <p>where in the right-most term in third equation we have used the fact that for every node <span class="math" data-nodeid="205">\(u\)</span> in <span class="math" data-nodeid="208">\(V(G) \setminus W \setminus v\)</span> we have <span class="math" data-nodeid="211">\(\deg_H(u) = \deg_G(u)\)</span>.</p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step last" data-nodeid="214">

        <div class="statement" data-nodeid="215">

        <div class="paragraph" data-nodeid="216">

        <p><span class="construct qed" data-nodeid="217"><span class="keyword" data-nodeid="218">QED </span></span></p>

        </div>

        </div>

        <div class="subproof" data-nodeid="220">

        <div class="claimblock" data-nodeid="221">
        <span class="keyword" data-nodeid="222">⊢ </span>
        <div class="mathblock" data-nodeid="224">
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

        <div class="paragraph" data-nodeid="226">

        <p>where the first equation is true by <a class="reference" href="#asm">induction hypothesis</a>, and the last equation is due to <a class="reference" href="#stp-edges">Step 5</a> and <a class="reference" href="#stp-sum">Step 6</a>.</p>

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
