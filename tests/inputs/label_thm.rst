#############
Label theorem
#############

One of the main features of RSM is that anything can be labeled and referenced.  For
example,

.. theorem::
   :label: some-thm

   :label:`some-stm` All `X` are `Y`. And now something else. And some other words and
   math `\forall X, P(X)`.

   And this is the second paragraph, but still in the theorem.

   .. math::

      \forall X, P(X),

   and finally we come to the end.

The first paragraph of the theorem has been labeled and can now be referred to
:ref:`like this <some-stm>`.  The entire theorem itself can be referred to :ref:`like
this <some-thm>`.
