# ReStructured Manuscripts (RSM)

[![tests](https://github.com/leotrs/rsm/actions/workflows/test.yml/badge.svg)](https://github.com/leotrs/rsm/actions/workflows/test.yml)
[![docs](https://readthedocs.org/projects/rsm-markup/badge/?version=latest)](https://rsm-markup.readthedocs.io/en/latest/?badge=latest)

The web-first authoring software for scientific manuscripts.

RSM is a suite of tools that aims to change the way scientific manuscripts are published
and shared using modern web technology. Currently, most scientific publications are made
with LaTeX and published in PDF format. While the capabilities of LaTeX and related
software are undeniable, there are many pitfalls. RSM aims to cover this gap by allowing
authors to create web-first manuscripts that enjoy the benefits of the modern web.

One of the main aims of the RSM suite is to provide scientists with tools to author
scientific manuscripts in a format that is web-ready in a transparent, native way that
is both easy to use and easy to learn.  In particular, RSM is a suite of tools that
allow the user to write a plain text file (in a special `.rsm` format) and convert the
file into a web page (i.e. a set of .html, .css, and .js files).  These files can then
be opened natively by any web browser on any device.

+ Learn more in the [official website](https://www.write-rsm.org).
+ Try it out in the [online editor](https://lets.write-rsm.org).
+ Get started with the [docs](https://docs.write-rsm.org).


<!-- ## Design philosophy -->

<!-- The RSM project follows a set of principles. Features are designed with these principles -->
<!-- in mind. If you think a feature could be improved, or a new feature could be -->
<!-- implemented, following these principles, please get in touch. -->

<!-- 1. RSM documents should be easily readable in any device, regardless of screen size, -->
<!--    operating system, or internet connection. -->

<!-- 2. RSM documents should ship with the source code that generated them. -->


<!-- ## Under the hood -->

<!-- -> Only show what the writer intended to show, unless the writer asks for more via -->
<!-- "details on demand" interactions. For example don't show menus, buttons, other things -->
<!-- unless the reader is hovering or selecting somehow -->



<!-- # -- Remember ----------------------------------------------------------- -->

<!-- Only show what the writer intended to show, unlews the writer asks for more via "details -->
<!-- on demand" interactions. For example don't show menus, buttons, other things unless the -->
<!-- reader is hovering or selecting somehow -->

<!-- + mathematical writing should be accessible, as opposed to obfuscated by notation, -->
<!--   convention, or implicit assumption -->
<!-- + the core will NOT be extended for aesthetic purposes. All aesthetics will be handled -->
<!--   via CSS. We want to avoid a situation like LaTeX where migrating from one journal -->
<!--   template to another is a PITA -->
<!-- + learn Lean, but remember RSM is about publishing, writing, and reading, not about -->
<!--   proof checking/assisting -->
<!-- + Lean is about checking correctness, RSM is about making a proof easy to read for a human -->
<!-- + Lean is about writing/checking math, RSM is about publishing/sharing math -->
<!-- + the proof markup language (PMUL) should be writeable by hand, if at all possible -->
<!-- + quote Mason Porter: 'a proof should _always_ have accompanying prose' -->
<!-- + quote Lamport: 'get to a level where every step is obviously true, and then go one -->
<!--   level further' -->
<!-- + write a short paper for a math education or math software meeting -->
<!-- + the document should only show what the writer intended, all other bells and whistles -->
<!--   should only happen "on demand", when the reader requests them -->
<!-- + the core extensions should take care of the model, the theme should take care of the -->
<!--   view. In particular, all css and js belongs to the theme -->
<!-- + the UI should be seamless and out of your way. The user should be able to hide -->
<!--   navigations/menus/buttons and maximize screen real state to show CONTENT. -->
<!-- + from Conor: how to date/timestamp versions of a web-paper? -->
