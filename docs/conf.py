# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from pathlib import Path

packages_path = (Path(os.path.dirname(__file__)) / ".." / "packages").resolve()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "stdlibx"
copyright = "2026, Lucino772"
author = "Lucino772"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.apidoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

autodoc_typehints = "description"
autodoc_member_order = "groupwise"

# sphinx.ext.viewcode
viewcode_line_numbers = True

# sphinx.ext.apidoc
apidoc_separate_modules = True
apidoc_include_private = False
apidoc_no_headings = False
apidoc_module_first = True
apidoc_automodule_options = {"members", "show-inheritance", "undoc-members"}
apidoc_modules = [
    {
        "path": str(packages_path / "stdlibx-cancel" / "src" / "stdlibx"),
        "destination": "packages/cancel/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-compose" / "src" / "stdlibx"),
        "destination": "packages/compose/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-config" / "src" / "stdlibx"),
        "destination": "packages/config/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-itertools" / "src" / "stdlibx"),
        "destination": "packages/itertools/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-matchtools" / "src" / "stdlibx"),
        "destination": "packages/matchtools/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-option" / "src" / "stdlibx"),
        "destination": "packages/option/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-result" / "src" / "stdlibx"),
        "destination": "packages/result/reference",
        "implicit_namespaces": True,
    },
    {
        "path": str(packages_path / "stdlibx-streams" / "src" / "stdlibx"),
        "destination": "packages/streams/reference",
        "implicit_namespaces": True,
    },
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
