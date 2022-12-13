.. _faq:

Frequently asked questions
==========================


.. _whats-wrong-with-latex-pdf:

What's wrong with LaTeX + PDF?
******************************

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
