# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from urllib.request import urlretrieve
import os
import sys
from pathlib import Path

module_path = os.path.join(os.path.dirname(__file__), "../..")
sys.path.insert(0, os.path.abspath(module_path))
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../../"))

# HERE = Path(__file__).parent
# sys.path[:0] = [str(HERE.parent)]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = [".rst"]
latex_additional_files = ['./notebooks/ref.bib']

master_doc = "index"


# -- Retrieve notebooks ------------------------------------------------


# notebooks_url = "https://github.com/Zhu-1998/scNEDT_notebook/raw/master/"
# notebooks = [
#     "***.ipynb",
#     "***.ipynb",
#     "***.ipynb",
#     "***.ipynb",
# ]
# for nb in notebooks:
#     try:
#         urlretrieve(notebooks_url + nb, nb)
#     except:
#         pass


# Add notebooks prolog to Google Colab and nbviewer
nbsphinx_prolog = r"""
{% set docname = 'github/Zhu-1998/scNEDT_notebook/blob/master/' + env.doc2path(env.docname, base=None) %}
.. raw:: html
    <div class="note">
      <a href="https://colab.research.google.com/{{ docname|e }}" target="_parent">
      <img src="https://user-images.githubusercontent.com/7456281/93841442-99c3e180-fc61-11ea-9c87-07760b5dfc9a.png" width="119" alt="Open In Colab"/></a>
      <a href="https://nbviewer.jupyter.org/{{ docname|e }}" target="_parent">
      <img src="https://user-images.githubusercontent.com/7456281/93841447-9c263b80-fc61-11ea-99b2-4eafe9958ee4.png" width="119" alt="Open In nbviewer"/></a>
    </div>
"""
rst_prolog = ""

# -- Project information -----------------------------------------------------

project = "scNEDT"
copyright = "2024, Ligang Zhu"
author = "Ligang Zhu"

# The full version, including alpha/beta/rc tags
release = "0.0.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# specify sphinx version
needs_sphinx = "4"
bibtex_bibfiles = ['./notebooks/ref.bib']
bibtex_reference_style = "author_year"

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    # Link to other project's documentation (see mapping below)
    "sphinx.ext.intersphinx",
    # Add a link to the Python source code for classes, functions etc.
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosectionlabel",
    # Automatically document param types (less noise in class signature)
    "sphinx_autodoc_typehints",
    "sphinxcontrib.bibtex",
    # 'sphinx_gallery.gen_gallery',
    'sphinx_gallery.load_style',
]

sphinx_gallery_conf = {
    'filename_pattern': '/tutorial_',
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}

# Mappings for sphinx.ext.intersphinx. Projects have to have Sphinx-generated doc! (.inv file)
intersphinx_mapping = {
    "anndata": ("https://anndata.readthedocs.io/en/stable/", None),
    "cycler": ("https://matplotlib.org/cycler/", None),
    "h5py": ("http://docs.h5py.org/en/stable/", None),
    "ipython": ("https://ipython.readthedocs.io/en/stable/", None),
    "louvain": ("https://louvain-igraph.readthedocs.io/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "networkx": (
        "https://networkx.github.io/documentation/networkx-1.10/",
        None,
    ),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "seaborn": ("https://seaborn.pydata.org/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Generate the API documentation when building
autosummary_generate = True
autodoc_member_order = "bysource"
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
# Remove 'view source code' from top of page (for html, not python)
html_show_sourcelink = True
# If no class summary, inherit base class summary
autodoc_inherit_docstrings = True

autodoc_default_flags = [
    # Make sure that any autodoc declarations show the right members
    "members",
    "inherited-members",
    "private-members",
    "show-inheritance",
]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = dict(
    navigation_depth=4,
    logo_only=True,
)
html_context = dict(
    display_github=True,  # Integrate GitHub
    github_user="Zhu-1998",  # organization
    github_repo="scNEDT",  # Repo name
    github_version="master",  # Version
    conf_py_path="/docs/source/",
)
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".


# def setup(app):
    # app.add_css_file("css/custom.css")


sphinx_enable_epub_build = False
sphinx_enable_pdf_build = False
