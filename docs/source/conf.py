# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
from pathlib import Path
from typing import List

root = Path(__file__).parents[2]

project = "Lognament"
copyright = "2022, Alex Le Tran"
author = "Alex Le Tran"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.duration", "sphinx.ext.doctest", "autoapi.extension"]
autoapi_type = "python"
autoapi_dirs = [f"{os.path.abspath(root)}/lognament"]

templates_path = ["_templates"]
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
