from paver.easy import *
import paver.doctools
from paver.setuputils import setup

setup(
        name="Python Cheat Sheets",
        packages=['pcs'],
        version="0.01",
        url="http://github.com/rcludwick/pcs",
        author="Rob Ludwick",
        author_email="rcludw_gmail"
        )

docroot = path("./pavement.rst").abspath().dirname() / "doc"

options(
        docroot = docroot,
        tmpdir = docroot / "tmp",
        srcdir = docroot / "src",
        builddir = docroot / "tmp" / "pdf", 
        srcbuilddir = docroot / "tmp" / "src",
        )

options(
        rst_ext = ".rst",
        )

options(
        rst2pdf_stylesheets = ("twocolumn","letter","eightpoint","freetype-sans","friendly",),
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
    options.tmpdir.mkdir()

@task
@needs('clean_tmp')
def copy_src_to_srcbuild(options):
    srcfiles = path.glob(options.srcdir / path( "*" + options.rst_ext))
    srcfiles.copy(options.srcbuilddir)

    

    
