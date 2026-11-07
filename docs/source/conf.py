# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sophie Kernchen'
copyright = '2026, Sophie Kernchen'
author = 'Sophie Kernchen'
release = '2026.11.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_title = "Überblick Sophie"
html_permalinks_icon = '<span>&#x1FA84;</span>'
html_theme = 'sphinxawesome_theme'
html_logo = '_static/img/keso.png'
html_favicon = '_static/img/keso.png'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]