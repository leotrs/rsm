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

          We have
          $$
          :label: eqn-thm
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

            :step: We have
              $$
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

            :p: We have
              $$
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

        <p><span class="span label">Theorem 1.</span></p>

        </div>

        <div class="paragraph" data-nodeid="31">

        <p>We have </p>
        <div id="eqn-thm" class="mathblock" data-nodeid="33">
        $$
        \sum_{u \in V(G)} \deg(u) = 2L(G).
        $$
        </div>

        </div>

        </div>

        <div class="proof" data-nodeid="35">

        <div class="paragraph hr-label">

        <p><span class="span label">Proof.</span></p>

        </div>

        <div class="step" data-nodeid="36">

        <div class="statement" data-nodeid="37">

        <div class="paragraph" data-nodeid="38">

        <p><span class="construct define assumption" data-nodeid="39"><span class="keyword" data-nodeid="40">DEFINE </span><span class="math" data-nodeid="42">\(n = |V(G)|\)</span>.</span></p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="45">

        <div class="statement" data-nodeid="46">

        <div class="paragraph" data-nodeid="47">

        <p><span class="construct case assumption" data-nodeid="48"><span class="keyword" data-nodeid="49">CASE </span><span class="math" data-nodeid="51">\(n = 1\)</span>.</span></p>

        </div>

        </div>

        <div class="subproof" data-nodeid="54">

        <div class="step" data-nodeid="55">

        <div class="statement" data-nodeid="56">

        <div class="paragraph" data-nodeid="57">

        <p><span class="construct claim" data-nodeid="58"><span class="keyword" data-nodeid="59">⊢ </span><span class="math" data-nodeid="61">\(L(G) = 0\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="64">

        <div class="paragraph" data-nodeid="65">

        <p><span class="math" data-nodeid="66">\(G\)</span> has no self-loops by assumption.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="69">

        <div class="statement" data-nodeid="70">

        <div class="paragraph" data-nodeid="71">

        <p><span class="construct let assumption" data-nodeid="72"><span class="keyword" data-nodeid="73">LET </span><span class="math" data-nodeid="75">\(u \in V(G)\)</span></span>, <span class="construct then" data-nodeid="78"><span class="keyword" data-nodeid="79">THEN </span><span class="math" data-nodeid="81">\(\deg(u) = 0\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="84">

        <div class="paragraph" data-nodeid="85">

        <p>Since <span class="math" data-nodeid="87">\(G\)</span> has only one node, and it has no self-loops.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="90">

        <div class="statement" data-nodeid="91">

        <div class="paragraph" data-nodeid="92">

        <p><span class="construct qed" data-nodeid="93"><span class="keyword" data-nodeid="94">QED </span></span></p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="96">

        <div class="statement" data-nodeid="97">

        <div class="paragraph" data-nodeid="98">

        <p><span class="construct let assumption" data-nodeid="99"><span class="keyword" data-nodeid="100">LET </span><span class="math" data-nodeid="102">\(v \notin V(G)\)</span></span>. <span class="construct write assumption" data-nodeid="105"><span class="keyword" data-nodeid="106">WRITE </span><span class="math" data-nodeid="108">\(H\)</span> for the graph resulting from adding <span class="math" data-nodeid="111">\(v\)</span> to <span class="math" data-nodeid="114">\(G\)</span></span>. SUFFICES <span class="construct assume assumption" data-nodeid="117"><span class="keyword" data-nodeid="118">ASSUME </span><span class="span" data-nodeid="120"><span id="asm" class="span" data-nodeid="121">the theorem is true for <span class="math" data-nodeid="123">\(G\)</span></span></span></span>, <span class="construct prove assumption" data-nodeid="126"><span class="keyword" data-nodeid="127">PROVE </span>the theorem is true for <span class="math" data-nodeid="130">\(H\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="133">

        <div class="paragraph" data-nodeid="134">

        <p>By induction.</p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="136">

        <div class="statement" data-nodeid="137">

        <div class="paragraph" data-nodeid="138">

        <p><span class="construct define assumption" data-nodeid="139"><span class="keyword" data-nodeid="140">DEFINE </span><span class="math" data-nodeid="142">\(\deg_G(u), \deg_H(u)\)</span> as the degree of node <span class="math" data-nodeid="145">\(u\)</span> in <span class="math" data-nodeid="148">\(G\)</span> and <span class="math" data-nodeid="151">\(H\)</span> respectively.</span> Note <span class="math" data-nodeid="155">\(\deg_G(v) = 0\)</span>.</p>

        </div>

        </div>

        </div>

        <div id="stp-edges" class="step" data-nodeid="158">

        <div class="statement" data-nodeid="159">

        <div class="paragraph" data-nodeid="160">

        <p><span class="construct claim" data-nodeid="161"><span class="keyword" data-nodeid="162">⊢ </span><span class="math" data-nodeid="164">\(L(H) = L(G) + \deg_H(v)\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="167">

        <div class="paragraph" data-nodeid="168">

        <p>Because the only added edges are those incident to <span class="math" data-nodeid="170">\(v\)</span>.</p>

        </div>

        </div>

        </div>

        <div id="stp-sum" class="step" data-nodeid="173">

        <div class="statement" data-nodeid="174">

        <div class="paragraph" data-nodeid="175">

        <p><span class="construct claim" data-nodeid="176"><span class="keyword" data-nodeid="177">⊢ </span><span class="math" data-nodeid="179">\(\sum_{u \in V(H)} \deg_H(u) = 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u)\)</span></span>.</p>

        </div>

        </div>

        <div class="subproof" data-nodeid="182">

        <div class="step" data-nodeid="183">

        <div class="statement" data-nodeid="184">

        <div class="paragraph" data-nodeid="185">

        <p><span class="construct write assumption" data-nodeid="186"><span class="keyword" data-nodeid="187">WRITE </span><span class="math" data-nodeid="189">\(W \subset V(G)\)</span> for the set of neighbors of <span class="math" data-nodeid="192">\(v\)</span>.</span></p>

        </div>

        </div>

        </div>

        <div class="step" data-nodeid="195">

        <div class="statement" data-nodeid="196">

        <div class="paragraph" data-nodeid="197">

        <p>We have </p>
        <div class="mathblock" data-nodeid="199">
        $$
        \begin{align}
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in V(H)\setminus\{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} \deg_H(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_H(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= \phantom{2} \deg_H(v) + \sum_{u \in W} (\deg_G(u) + 1) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in W} \deg_G(u) + \sum_{u \in V(H) \setminus W \setminus \{v\}} \deg_G(u) \\
                \sum_{u \in V(H)} \deg_H(u) &= 2\deg_H(v) + \sum_{u \in V(G)} \deg_G(u),
                \end{align}
        $$
        </div>

        </div>

        <div class="paragraph" data-nodeid="201">

        <p>where in the right-most term in third equation we have used the fact that for every node <span class="math" data-nodeid="203">\(u\)</span> in <span class="math" data-nodeid="206">\(V(G) \setminus W \setminus v\)</span> we have <span class="math" data-nodeid="209">\(\deg_H(u) = \deg_G(u)\)</span>.</p>

        </div>

        </div>

        </div>

        </div>

        </div>

        <div class="step last" data-nodeid="212">

        <div class="statement" data-nodeid="213">

        <div class="paragraph" data-nodeid="214">

        <p><span class="construct qed" data-nodeid="215"><span class="keyword" data-nodeid="216">QED </span></span></p>

        </div>

        </div>

        <div class="subproof" data-nodeid="218">

        <div class="paragraph" data-nodeid="219">

        <p>We have </p>
        <div class="mathblock" data-nodeid="221">
        $$
        \begin{align}
                2 L(G) &= \sum_{u \in V(G)} \deg_G(u) \\
                2 L(G) + 2 \deg_H(v) &=  2 \deg_H(v) + \sum_{u \in V(G)} \deg_G(u) \\
                2 L(H) &=  \sum_{u \in V(H)} \deg_H(u),
                \end{align}
        $$
        </div>

        </div>

        <div class="paragraph" data-nodeid="223">

        <p>where the first equation is true by <a class="reference" href="#asm">induction hypothesis</a>, and the last equation is due to <a class="reference" href="#stp-edges">Step ⟨5⟩</a> and <a class="reference" href="#stp-sum">Step ⟨6⟩</a>.</p>

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
