# RSM: (R)e-(S)tructured (M)anuscripts

RSM is a suite of tools that aims to change the format of scientific publications using
modern web technology. Currently, most scientific publications are made with LaTeX and
published in PDF format. While the capabilities of LaTeX and related software are
undeniable, there are many pitfalls. RSM aims to cover this gap.


## What's wrong with LaTeX + PDF?

There's nothing inherently wrong with writing scientific manuscripts in LaTeX and
publishing them in PDF format.  However, the LaTeX ecosystem was designed at a time
where the main medium of scientific publication was physically printed books and
magazines.  Today, this is far from the truth as more and more scientists read papers
online.  The PDF format and many of LaTeX's features are designed to output documents
that will be physically printed, and this is not necessarily the best option when
reading a digital document.  These are some of the problems that arise when reading PDFs
on a digital device:

1. A PDF file has a fixed geometry (page size, margins, etc), while digital devices
   (laptops, tablets, mobile phones) have a variety of screen sizes and shapes.  The
   same PDF file may be read easily in, for example, a laptop screen, but not in a
   tablet or mobile screen.

2. A PDF file has a fixed layout (the relative positions of text, headers, figures,
   tables, etc).  In contrast, in the last decade, digital documents and especially web
   pages are moving toward being *responsive*, that is, their layout adapts to the
   features of the devices they are being read on.

3. A PDF file has a fixed typography (font family, weight, size, color, etc).  For
   accessibility reasons, a reader may prefer different typographic choices.  For
   example, some font families are designed to be read more easily by people with
   dyslexia, while high-contrast color schemes are preferred by people with certain
   sight conditions.  PDF files cannot adapt to the preferences of the user without
   using external tools.

4. While there are ways to configure LaTeX to output files in a format different than
   PDF (e.g. EPS, DVI), most of the above critiques still hold true.
   
5. While there are ways to transform the output of LaTeX to a web-ready format
   (i.e. HTML), this is always an extra step that must be done outside of the LaTeX
   ecosystem.  As a result, not all of the LaTeX features translate transparently to the
   final output and some post-processing is sometimes necessary.


## What RSM does differently

One of the main aims of the RSM suite is to provide scientists with tools to author
scientific manuscripts in a format that is web-ready in a transparent, native way that
is both easy to use and easy to learn.  In particular, RSM is a suite of tools that
allow the user to write a plain text file (in a special `.rsm` format) and convert the
file into a web page (i.e. a set of .html, .css, and .js files).  These files can then
be opened natively by any web browser on any device.  In the rest of this README, and in
the documentation, the files output by RSM are referred to as *the document*, or *the
output document*.


## Features

RSM's output document has the following features:

1. Responsive: its geometry and layout adapt to the device it is being read on.

2. Accessible: the user is free to change the geometry, layout, typography and other
   settings of a RSM document.

3. Separation of concerns: internally, the structure and content of an RSM document are
   separate from the style and look-and-feel.  The former are stored in HTML format,
   while the latter are treated with CSS and Javascript.

4. Interactive: RSM documents support context-relevant tooltips, embedded video or
   animations, enhanced document navigation, smart search, content folding, smart
   context menus, and many other opportunities for interaction.

5. Extensible: potential to extend using the entire ecosystem of modern web technologies


## Components

The RSM framework is comprised of several components, each of which can be used in
isolation, though using them in unison yields best results.

1. **The **RSM file format, `.rsm`** is a format that allows writers to produce
   technical documents that get rendered directly into web-ready formats. RSM is a plain
   text format so you can edit a .`rsm` file with your favorite text
   editor. Fundamentally, the `.rsm` file format is essentially an extension of the .rst
   file format.

1. **The RSM project** is simply a folder that contains a `.rsm` file and its .html
   output. When sharing your RSM document, you should always share *the entire* RSM
   folder, not just one file.

2. **rsm-edit, the RSM text editor,** is a text editor specifically designed to edit
   .rsm files. Besides having basic text editing features, rsm-edit has features
   specific to producing `.rsm` files.

3. **rsm-view, the RSM reader,** is a file viewer specifically designed to show `.rsm`
   files. It is essentially a web browser, though it has some extra features.

4. **rsm-make, the RSM command line utility** is for now the main way to execute all the
   core functionality of the RSM framework.


## Basic usage

One of the objectives of the RSM project is to make it possible to produce and share
documents that can be viewed easily at any time anywhere, without restriction of device,
software, software versions, operating system, internet connection, etc. Therefore, the
only required component is a `.rsm` file. An basic `.rsm` file can be produced with any
text editor, and it can be viewed on any modern web browser, even without internet
connection.


## Advanced usage

Additionally to the basic features, the RSM project also provides advanced features that
do require the adoption of some of the other components. For example, writers using the
`.rsm` format may find it useul to use rsm-edit. Accordingly, some of the features of
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
packaged in the `.rsm` file format that will be available when producing `.rsm` files
with any text editor and viewing them on any web browser.

+ Documents are typeset using HTML and CSS. Any modern web browser is able to render a
  `.rsm` document. Furthermore, the same document will be viewable on any device that
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

The following is a short `.rsm` file:

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
   `.rsm` source files and the .html output files.

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




-> Only show what the writer intended to show, unlews the writer asks for more via
"details on demand" interactions. For example don't show menus, buttons, other things
unless the reader is hovering or selecting somehow




# -- Feats ----------------------------------------------------------------
#
# what to do when a theorem contains more than one claim.
#
# thm: ASSUME x, y, z. PROVE |- P is true, and |- Q is true.
# 
# be able to refer to results by their 'title' (recall Jay Cummings' longform math textbook's "List of results" - an example is on Notion 'linear alg. textbook')
#
# consider supporting advanced highlighting systems: (https://twitter.com/joe_doesmath/status/1420816265439027205)
#
# consider supporting 'annotated equations' (https://twitter.com/sibinmohan/status/1480583840858996743)

# -- Tests ----------------------------------------------------------------
# Statement contianing math
# Statement longer than one line
# In sub-step: Statement contianing math
# In sub-step: Statement longer than one line
# And then again in sub-sub-step
# Statmeent made up of a single latex symbol
# Test that :step:`lbl` and :step: `some_latex` are parsed correctly

# -- Remember -----------------------------------------------------------
# the doctree is the model, the html/css is the view
# as much as possible, only use margin-bottom
# Use margins when pushing blocks away from each other
# Use padding when pushing things into their own block
# only use JS for complex selectors and adding/removing classes
# anything more complicated goes to rsm-read (exception tooltips/tree)

# -- Refactor -----------------------------------------------------------
# refactor handrail--hug (almost all handrails are hug...)
# refactor the position of handrail__btn-container
# refactor AutoNumberProofs, -Theorems, and -Sections
# use docutils.directives.class_option
# should theorem-like even have handrail buttons? (just put them in the proof...)
# Use something similar to the following to reduce boilerplate:
#
# class GenericRole(object):
#     def __init__(self, role_name, node_class):
#         self.name = role_name
#         self.node_class = node_class
#     def __call__(self, role, rawtext, text, lineno, inliner,
#                  options={}, content=[]):
#         set_classes(options)
#         return [self.node_class(rawtext, text, **options)], []



# Only show what the writer intended to show, unlews the writer asks for more via "details
# on demand" interactions. For example don't show menus, buttons, other things unless the
# reader is hovering or selecting somehow



writing: always develop intuition using concrete examples and then introduce a formal
definition. Perhaps even introduce 'wrong' or outdated definitions.


from Conor: how to date/timestamp versions of a web-paper?

Only show what the writer intended to show, unlews the writer asks for more via "details on demand" interactions. For example don't show menus, buttons, other things unless the reader is hovering or selecting somehow



+ mathematical writing should be accessible, as opposed to obfuscated by notation,
  convention, or implicit assumption
+ the core will NOT be extended for aesthetic purposes. All aesthetics will be handled
  via CSS. We want to avoid a situation like LaTeX where migrating from one journal
  template to another is a PITA
+ learn Lean, but remember RSM is about publishing, writing, and reading, not about
  proof checking/assisting
+ Lean is about checking correctness, RSM is about making a proof easy to read for a human
+ Lean is about writing/checking math, RSM is about publishing/sharing math
+ the proof markup language (PMUL) should be writeable by hand, if at all possible
+ quote Mason Porter: 'a proof should _always_ have accompanying prose'
+ quote Lamport: 'get to a level where every step is obviously true, and then go one
  level further'
+ write a short paper for a math education or math software meeting
+ the document should only show what the writer intended, all other bells and whistles
  should only happen "on demand", when the reader requests them
+ the core extensions should take care of the model, the theme should take care of the
  view. In particular, all css and js belongs to the theme
+ the UI should be seamless and out of your way. The user should be able to hide
  navigations/menus/buttons and maximize screen real state to show CONTENT.
