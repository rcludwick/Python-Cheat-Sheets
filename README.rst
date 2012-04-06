===================
Python Cheat Sheets
===================

Why?
====

To create a simple way to create reference sheets to sit in a binder and provide useful information
so that I do not have to google "python <thing> example".  The python documentation is nice, but can be lacking in examples.

How?
====

Using restructured text and rst2pdf, the goal will be to create a series of pdfs that can be printed off in a binder.  Each sheet will include a QR code and a url that will point to the latest version of the documentupon a commit.  This way, updates can be easily checked or shared with friends.


Files will be built using the following command::

rst2pdf -s twocolumn,letter,eightpoint,freetype-sans,friendly threading.rst > threading.pdf
