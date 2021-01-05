# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SMaLL best practice'
copyright = u'\
2021, Multi-Scale ModeLing Laboratory (SMaLL) \
POLITECNICO DI TORINO (Department of Energy "Galileo Ferraris" (DENERG)), ITA . All rights reserved'
author = 'SMaLL Team'


# The full version, including alpha/beta/rc tags
release = 'latest'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
    'sphinx.ext.ifconfig', 'sphinx.ext.intersphinx', 'sphinx.ext.viewcode',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive', 'myst_nb', 'sphinx.ext.extlinks',
    'sphinx.ext.mathjax', 'sphinx_copybutton', 'sphinx_panels'
]

ipython_mplbackend = ""

copybutton_selector = 'div:not(.no-copy)>div.highlight pre'
copybutton_prompt_text = '>>> |\\\\$ |In \\\\[\\\\d+\\\\]: |\\\\s+\\.\\.\\.: '
copybutton_prompt_is_regexp = True

todo_include_todos = True

extlinks = {
    'doi': ('https://doi.org/%s', 'doi:'),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes"]
html_logo = "logo.svg"
# Enable labeling for figures
numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True