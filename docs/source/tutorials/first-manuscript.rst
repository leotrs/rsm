.. _first-manuscript:

Your first manuscript
=====================

Create a new file called :code:`manuscript.rsm` and add the following contents

.. code-block::

   :manuscript:

   Web-first scientific publishing.

   ::

In the command line, :code:`cd` to the directory where the :code:`manuscript.rsm` file
is stored and execute

.. code-block:: bash

   $ rsm-make manuscript.rsm

This will create a new file called :code:`index.html` in the same directory.  Open this
file with your web browser to see the web manuscript created by RSM.

When running the last command, you probably saw the following warning (or something similar):

.. code-block:: bash

   RSM.tlate WRN | Manuscript with no title

Here, RSM is telling us that our manuscript is missing a title.  We can rectify that by
editing :code:`manuscript.rsm` as follows

.. code-block::

   :manuscript:
     :title: ReStructured Manuscripts

   Web-first scientific publishing.

   ::

Run again the same command,

.. code-block:: bash

   $ rsm-make manuscript.rsm

And the warning should have disappeared.  You can refresh your browser to see now the
title of your manuscript displayed.


.. note::

   The word "tlate" in the warning

   .. code-block:: bash
   
      RSM.tlate WRN | Manuscript with no title

   stands for "translate".  This means that the warning was issued during the
   translation step of RSM manuscript processing pipeline. :ref:`Learn more <pipeline>`.
