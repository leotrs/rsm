######
Labels
######

This tests the functionality of custom labels.


***************
Labeled theorem
***************

The following theorem has a label, and its statement does as well.

.. theorem::
   :label: thm-lbl

   :label:`stm-lbl` All `X` are `Y`.

The statement of the theorem has been labeled and can now be referred to :ref:`like this
<stm-lbl>`.  The theorem itself can now be referred to :ref:`like this
<thm-lbl>`.

