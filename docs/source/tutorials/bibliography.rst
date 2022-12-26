.. _bibliography:

Bibliography
============

RSM supports bibliography using BibTex notation.  Use the ``:bibliography:`` tag to note
where in the manuscript the list of references will appear.

.. rsm::

   :manuscript:

   Some content here.

   :bibliography: ::

   ::

Use the ``:bibtex:`` tag to supply the necessary references in BibTex notation.

.. code-block:: text

   :bibtex:

   @book{knuth,
         title={Art of computer programming, volume 2, Seminumerical algorithms},
         author={Knuth, Donald E},
         year={2014},
         publisher={Addison-Wesley Professional}
        }

   ::

.. important::

   The ``:bibtex:`` tag is located outside, and immediately after the closing Halmos of
   the ``:manuscript:`` tag.

Within the manuscript contents, use ``:cite:`` to refer to a bibliography item.  Here is
a complete example of the bibliography system.


.. rsm::

   :manuscript:

   Here comes a citation :cite:knuth::.

   :bibliography: ::

   ::

   :bibtex:

   @book{knuth,
         title={Art of Computer Programming},
         author={Knuth, Donald E},
         year={2014},
         publisher={Addison-Wesley}
        }

   ::
