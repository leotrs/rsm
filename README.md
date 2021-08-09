# reStructuredManuscript (RSM)

RSM is a framework that aims to change the format of scientific publications using
modern web technology. Currently, most scientific publications are made with LaTeX and
published in PDF format. While the capabilities of LaTeX and related software are
undeniable, there are many pitfalls. RSM aims to cover this gap.


## What's wrong with LaTeX + PDF?

1. One of the most egregious pitfalls is that LaTeX is designed to output a document in
   a single style (or class). In theory, changing to a different class should be as easy
   as changing one line (the one containing the `\documentclass` command, usually at the
   top of the file), though any scientist who has tried to convert from one journal's
   LaTeX template to another knows that in practice this process can be much more
   cumbersome and time-consuming.

1. Nobody teaches LaTeX, everybody learns python

1. Visualizing the document on different deices is usually a nuisance at best, and
   impossible at worst. The usual output of LaTeX is a single PDF file, with a
   predetermined geometry (page size, margins, etc) and typography (font family, font
   size, etc). When the same document is rendered on different devices (say, a laptop
   computer or a mobile phone) or with different rendering software (say, an internet
   browser or Adobe Acrobat), the document is not optimized for a different screen size.

1. potential to extend using the entire ecosystem of modern web technologies

1. MORE HERE


## Components

The RSM framework is comprised of several components, each of which can be used in
isolation, though using them in unison yields best results.

1. **.rsm, the **RSM file format** is a format that allows writers to produce technical
   documents that get rendered directly into web-ready formats. RSM is a plain text
   format so you can edit an .rsm file with your favorite text editor. Fundamentally,
   the .rsm file format is essentially an extension of the .rst file format.

1. **The RSM project** is simply a folder that contains an .rsm file and its .html
   output. When sharing your RSM document, you should always share *the entire* RSM
   folder, not just one file.

2. **rsm-edit, the RSM text editor,** is a text editor specifically designed to edit
   .rsm files. Besides having basic text editing features, rsm-edit has features
   specific to producing .rsm files.

3. **rsm-view, the RSM reader,** is a file viewer specifically designed to show .rsm
   files. It is essentially a web browser, though it has some extra features.

4. **rsm-make, the RSM command line utility** is for now the main way to execute all the
   core functionality of the RSM framework.


## Basic usage

One of the objectives of the RSM project is to make it possible to produce and share
documents that can be viewed easily at any time anywhere, without restriction of device,
software, software versions, operating system, internet connection, etc. Therefore, the
only required component is a .rsm file. An basic .rsm file can be produced with any text
editor, and it can be viewed on any modern web browser, even without internet
connection.


## Advanced usage

Additionally to the basic features, the RSM project also provides advanced features that
do require the adoption of some of the other components. For example, writers using the
.rsm format may find it useul to use rsm-edit. Accordingly, some of the features of
rsm-edit can only be fully enjoyed by readers via rsm-view.

Adopting the rsm-edit and rsm-view is not necessarily the most accessible
thing. However, the project is currently in proof-of-concept stage. If it proves to be a
useful tool and the community starts adopting it, then care will be placed to guarantee
that adopting the rsm-view and rsm-edit tools is as easy and accessible as
possible. Specifically, there should be cloud versions of both tools where all that's
necessary is an internet connection.


## Features

### Basic features

This is a list of features that are available via basic usage, that is, features
packaged in the .rsm file format that will be available when producing .rsm files with
any text editor and viewing them on any web browser.

+ Documents are typeset using HTML and CSS. Any modern web browser is able to render a
  .rsm document. Furthermore, the same document will be viewable on any device that
  supports web browsing in a native way. Among other things, this means that an RSM
  document automatically renders at the correct screen size, that font size is
  customizable, and that screen readers and other accessibility tools are readily
  available (as long as they are supported by the chosen web browser).
+ The RSM file format is plain text, which means that a RSM file can be produced on any
  text editor. Furthermore, the RSM format is designed to be read by humans, not by
  machines to RSM files are arguably easier to read than LaTeX files even before
  rendering. Specifically, in contrast to LaTeX, RSM does not make use of backlash
  commands `\\` with sometimes obscure names that may or may not be overwritten by
  different packages. Instead, RSM has a small core of text formatting functionality
  that can not be overwritten and is guaranteed to always mean the same thing.


### Advanced features

This is a list of features that are available via the rsm-edit and rsm-view tools.

**rsm-edit**

**rsm-view**

+ Customizable look and feel: margins, font family, etc
+ LaTeX search
+ 'my copy'


## Examples

The following is a short .rsm file:

```rst
.. default-role:: math


##########################
This is the document title
##########################

This is some content, with inline math like `G` or `2m\times2m` matrix,
and display-style equations

.. math::
   :label: eqn-nbm

   B_{k \to l,i \to j} := \delta_{jk}\left(1-\delta_{il}\right).


.. _sec-zero-one:

******************************
This is a section title
******************************

This is the section's content.

.. _sec-trees:

Sub-section title
=================

This is the sub-section content


```


## Getting started

Currently, the easiest way of using RSM is as follows:

1. Create a new folder in your file system. For this example, we will use
   `project/`. This folder contains all files pertaining to your manuscript, both the
   .rsm source files and the .html output files.

2. Create a new text file in your project folder, for example
   `project/manuscript.rsm`. This file contains your source code. It is the equivalent
   of the .tex files if you are using LaTeX.

3. Write some RSM in your `project/manuscript.rsm` file using your favorite text
   editor. Save your changes.

4. Run the `rsm-make` command line utility from your project folder: ```bash $ cd
   project/ project/$ rsm-make manuscript.rsm Building RSM...  Done.  $ ``` This will
   create, among other things, a new file `project/index.html`. This is the equivalent
   of the PDF file if you are using LaTeX.

5. To see your rendered manuscript, simply open the `project/index.html` file with any
   web browser. For example, in Firefox, you can click on the File menu, click Open, and
   navigate to your file.



## Design philosophy

The RSM project follows a set of principles. Features are designed with these principles
in mind. If you think a feature could be improved, or a new feature could be
implemented, following these principles, please get in touch.

1. RSM documents should be easily readable in any device, regardless of screen size,
   operating system, or internet connection. BECAUSE ACCESSIBILITY.

2. RSM documents should ship with the source code that generated them. BECAUSE
   TRANSPARENCY AND EXTENSIBILITY.

3. WHAT ELSE?



## Under the hood

+ .rst extensions implemented in sphinx
+ WHAT ELSE?


# Mention distill.pub and structured proofs at some point...
