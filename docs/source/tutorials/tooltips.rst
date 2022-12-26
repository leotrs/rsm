.. _tooltips:

References and tooltips
=======================

Use the ``:label:`` tag to assign a unique label to any part of the manuscript, and use
the ``:ref:`` tag to refer to it.

.. rsm::

   :manuscript:

   :remark:
     :label: some-lbl

   This remark can be referenced by using
   its label.

   ::

   Refer to :ref:some-lbl:: above.

   ::

Hovering over the link text will display a tooltip showing the referenced region.

By default, the ``:ref:`` tag is displayed using the type of region referenced and its
number, if it has one; this generates the text "Remark 1" in the preceding example.  You
can override this behavior when using the ``:reftext:`` tag.

.. rsm::

   :manuscript:

   :remark:
     :label: some-lbl
     :reftext: Awesome Remark

   This remark can be referenced by using
   its label.

   ::

   Refer to :ref:some-lbl:: above.

   ::

The ``:reftext:`` tag is used at the same place where the ``:label:`` tag is defined,
and it changes the default text displayed whenever the annotated region is referenced.
You can also override the behavior of a single call to ``:ref:`` by using the following
notation.

.. rsm::

   :manuscript:

   :remark:
     :label: some-lbl

   This remark can be referenced by using
   its label.

   ::

   Refer to :ref:some-lbl:: above, or call
   it :ref:some-lbl, Awesome Remark::.

   ::

.. admonition:: Summary

   Use ``:label:`` to define a unique label to a region of the manuscript.  Use
   ``:ref:`` to reference a region via its label.  Override the displayed text globally
   by using ``:reftext:`` at the location where the label is defined, or by using a
   comma at the location where ``:ref:`` is used.  Regardless of the displayed text, a
   reference always displays a tooltip.

      
