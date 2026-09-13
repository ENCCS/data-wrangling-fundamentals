# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Practical Data Wrangling"
copyright = "2026 | ENCCS"
author = "Yonglei Wang"
github_user = "ENCCS"
github_repo_name = ""  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/content/"  # with leading and trailing slash


# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    # remove once sphinx_rtd_theme updated for contrast and accessibility:
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinx.ext.todo",
]


# Settings for myst_nb:
# nb_execution_mode = "cache"
jupyter_execute_notebooks = "off"
nb_execution_mode = "cache"
myst_enable_extensions = [
    "colon_fence",
]


# Settings for sphinx-copybutton
copybutton_exclude = ".linenos, .gp"



html_title = project


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_static_path = ['_static']
html_css_files = ["overrides.css"]

html_theme = "sphinx_rtd_theme"
html_logo = "./_static/ENCCS.jpg"
html_favicon = "./_static/favicon.ico"

html_theme_options = {
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# HTML context:
from os.path import basename, dirname, realpath

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": "data-wrangling-fundamentals",
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}


# add few new directives
from sphinx_lesson.directives import _BaseCRDirective

class SignatureDirective(_BaseCRDirective):
    extra_classes = ["toggle-shown", "dropdown"]

class ParametersDirective(_BaseCRDirective):
    extra_classes = ["dropdown"]

class TypealongDirective(_BaseCRDirective):
    extra_classes = ["toggle-shown", "dropdown"]


DIRECTIVES = [SignatureDirective, ParametersDirective, TypealongDirective]

def setup(app):
    for obj in DIRECTIVES:
        app.add_directive(obj.cssname(), obj)



