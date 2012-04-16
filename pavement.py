from paver.easy import *
import paver.doctools
from paver.setuputils import setup

import itertools

setup(
        name="Python Cheat Sheets",
        packages=['pcs'],
        version="0.01",
        url="http://github.com/rcludwick/pcs",
        author="Rob Ludwick",
        author_email="rcludw_gmail"
        )

docroot = path("./pavement.py").abspath().dirname() / "doc"

options(
        docroot = docroot,
        tmpdir = docroot / "tmp",
        srcdir = docroot.dirname() / "src",
        builddir = docroot / "tmp" / "pdf", 
        srcbuilddir = docroot / "tmp" / "src",
        )

options(
        rst_ext = ".rst",
        pdf_ext = ".pdf"
        )

options(
        rst2pdf_stylesheets = ("sphinx", "twocolumn", "letter",
            "eightpoint",),
        )

@task
def create_docdir(options):
    if not options.docroot.exists():
        options.docroot.mkdir()

@task
@needs('create_docdir')
def clean_tmp(options):
    if options.tmpdir.exists():
        options.tmpdir.rmtree()

@task
def create_builddirs(options):
    if options.tmpdir.exists():
        call_task("clean_tmp")
    options.tmpdir.mkdir()
    options.builddir.mkdir()
    options.srcbuilddir.mkdir()

@task
@needs('create_builddirs')
def copy_src_to_srcbuild(options):
    srcfiles = options.srcdir.glob("*" + options.rst_ext)
    for f in srcfiles:
        f.copy(options.srcbuilddir)

@task
@needs('copy_src_to_srcbuild')
def rsttopdf(options):
    rstfiles = options.srcbuilddir.glob( "*" + options.rst_ext)
    stylesheets = ",".join(options.rst2pdf_stylesheets)
    for i in rstfiles:
        oname = i.stripext().basename() + options.pdf_ext
        o = options.builddir / oname
        sh("rst2pdf --first-page-even %s -o %s -s %s" % ( i , o , stylesheets) )


@task
@needs("rsttopdf")
def move_pdfs(options):
    pdfiles = options.builddir.glob("*" + options.pdf_ext)
    for f in pdfiles:
        f.move(options.docroot)

@task
def clean_doc_dir(options):
    call_task("clean_tmp")
    pdfiles = options.docroot.glob("*" + options.pdf_ext)
    for p in pdfiles:
        p.unlink()
    

@task
@needs("clean_doc_dir")
def default(options):
    call_task("rsttopdf")
    call_task("move_pdfs")
    call_task("clean_tmp")


