import pytest
import rsm
from conftest import compare_have_want


def test_real_life_example():
    compare_have_want(
        have=r"""        :manuscript:

        :algorithm:
        \begin{algorithm}
        \caption{Quicksort}
        \begin{algorithmic}
            \PROCEDURE{Quicksort}{$A, p, r$}
                \IF{$p < r$}
                    \STATE $q = $ \CALL{Partition}{$A, p, r$}
                    \STATE \CALL{Quicksort}{$A, p, q - 1$}
                    \STATE \CALL{Quicksort}{$A, q + 1, r$}
                \ENDIF
            \ENDPROCEDURE
            \PROCEDURE{Partition}{$A, p, r$}
                \STATE $x = A[r]$
                \STATE $i = p - 1$
                \FOR{$j = p$ \TO $r - 1$}
                    \IF{$A[j] < x$}
                        \STATE $i = i + 1$
                        \STATE exchange
                        $A[i]$ with $A[j]$
                    \ENDIF
                    \STATE exchange $A[i]$ with $A[r]$
                \ENDFOR
            \ENDPROCEDURE
        \end{algorithmic}
        \end{algorithm}
        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <pre class="algorithm pseudocode">
        \begin{algorithm}
        \caption{Quicksort}
        \begin{algorithmic}
            \PROCEDURE{Quicksort}{$A, p, r$}
                \IF{$p < r$}
                    \STATE $q = $ \CALL{Partition}{$A, p, r$}
                    \STATE \CALL{Quicksort}{$A, p, q - 1$}
                    \STATE \CALL{Quicksort}{$A, q + 1, r$}
                \ENDIF
            \ENDPROCEDURE
            \PROCEDURE{Partition}{$A, p, r$}
                \STATE $x = A[r]$
                \STATE $i = p - 1$
                \FOR{$j = p$ \TO $r - 1$}
                    \IF{$A[j] < x$}
                        \STATE $i = i + 1$
                        \STATE exchange
                        $A[i]$ with $A[j]$
                    \ENDIF
                    \STATE exchange $A[i]$ with $A[r]$
                \ENDFOR
            \ENDPROCEDURE
        \end{algorithmic}
        \end{algorithm}
        </pre>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_label():
    compare_have_want(
        have=r"""        :manuscript:

        :algorithm:
        :label: alg

        \begin{algorithm}
        \caption{Quicksort}
        \begin{algorithmic}
        k=v
        \end{algorithmic}
        \end{algorithm}
        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <pre id="alg" class="algorithm pseudocode">
        \begin{algorithm}
        \caption{Quicksort}
        \begin{algorithmic}
        k=v
        \end{algorithmic}
        \end{algorithm}
        </pre>

        </section>

        </div>

        </div>

        </body>
        """,
    )
