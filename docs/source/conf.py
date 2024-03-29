# Configuration path for the Sphinx documentation builder.
#
# This path only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from sphinx.ext.autosummary import Autosummary
from sphinx.ext.autosummary import get_documenter
from docutils.parsers.rst import directives
from sphinx.util.inspect import safe_getattr
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path, '..', '..'))
sys.path.insert(0, os.path.join(path, '..', '..', 'glabel'))


# -- Project information -----------------------------------------------------

project = 'GLabel'
copyright = '2020, Zillig Tobias'
author = 'Zillig Tobias'

# The full version, including alpha/beta/rc tags
release = "0.3.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'autodocsumm',
]
todo_include_todos = True
autosummary_generate = True
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

intersphinx_mapping = {
    'pyqtgraph': ('http://www.pyqtgraph.org/documentation/', None)
}

extlinks = {
    'pyqt': ('https://doc.qt.io/qt-5/%s.html', ''),
    'tf': ('https://tensorflow.org/api_docs/python/%s', '')
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# html_theme_options = {
#     'nosidebar': True,
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a path named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']