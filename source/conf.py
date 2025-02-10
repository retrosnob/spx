# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'spx'
copyright = '2025, JR'
author = 'JR'
release = '0.9'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# Set the correct base URL for GitHub Pages
html_baseurl = "https://retrosnob.github.io/spx/"

# Use a relative URL prefix for static assets
html_css_files = [
    '_static/basic.css',  # Adjust if you have custom CSS
    'custom.css'  # Add custom CSS if applicable
]