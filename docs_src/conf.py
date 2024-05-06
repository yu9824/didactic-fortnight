# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

from template import __author__, __version__

dirpath_current = os.path.abspath(os.path.dirname(__file__))

project = "template"
copyright = "2024, yu9824"
author = __author__
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # docstringからドキュメントを作成してくれる。
    "sphinx.ext.napoleon",  # google式・numpy式docstringを整形してくれる。
    "sphinx.ext.githubpages",  # github-pages用のファイルを生成してくれる。
    "recommonmark",  # markdownで書けるようにする。
    "sphinx_markdown_tables",  # markdownの表を書けるようにする。
    "sphinx_multiversion",  # 複数バージョンの共存
]

templates_path = [os.path.join(dirpath_current, "_templates")]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = [os.path.join(dirpath_current, "_static")]

# for markdown documentations
source_suffix = [".rst", ".md"]
source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser",
}

# for multi-version
smv_tag_whitelist = r"^v\d+\.\d+.\d+$"  # Include tags like "v2.1.1"
smv_branch_whitelist = r"^main$"  # Include 'main' branch only
