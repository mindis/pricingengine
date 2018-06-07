#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pricing Engine documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  5 14:16:40 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
##Allow MarkDown.
##Prerequisite. pip install recommonmark 
import recommonmark
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('../lib'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# consider: 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.ifconfig', 'sphinx.ext.coverage',
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['docs/templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
#source_suffix = '.rst'
##Allow MarkDown.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Pricing Engine'
copyright = '2017, Matt Goldman, Brian Quistorff'
author = 'Matt Goldman, Brian Quistorff'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# Ensure: Keep in sync with lib/setup.py
# The short X.Y version.
#version = '2.1'
from pricingengine import __version__
version = __version__
# The full version, including alpha/beta/rc tags. (For now, keep the same)
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

html_copy_source=False
#html_show_sourcelink=False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['docs/build', 'Thumbs.db', '.DS_Store', 'skeletons', 'prototypes']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

def skip(app, what, name, obj, skip, options):
    #force showing __init__()'s
    if name == "__init__":
        return False
    
    skip_fns = ['DynamicDML.outcome_colname', 
                'DynamicDML.get_treatment_leads', 
                'DynamicDML.get_outcome_lead', 
                'DynamicDML.get_treatment_fore_diffs', 
                'DynamicDML.get_outcome_fore_diffs', 
                'DynamicDML.outcome_lag_colname', 
                'DynamicDML.treatment_lagdiff_colname', 
                'DynamicDML.treatment_lead_colname', 
                'DynamicDML.outcome_lead_colname', 
                'DynamicDML.treatment_model_type', 
                'DynamicDML.base_pred_treat_frame', 
                'DynamicDML.base_pred_outcome_frame', 
                'DoubleMLLikeModel.treatment_scale', 
                'DoubleML.feature_scale', 
                #'DoubleML.get_technical_treatment',
                'EstimationDataset.from_df',
                'Regression.regressor_scale',
                'Regression.fit_encoders',
                'ConstVar.get_effect_weights',
                'OwnPastAggVar.get_effect_weights',
                'OwnVar.get_effect_weights',
                'PToPVar.get_effect_weights',
                'PeerAggVar.get_effect_weights',
               ]
    if what=="class" and '__qualname__' in dir(obj) and obj.__qualname__ in skip_fns:
        return True
    
    # Can't figure out how to get the properties class to skip more targettedly
    skip_prs = ['features_fit',
                'aux_dataframe', 
                'treatment_generator', 
                'feature_generator', 
               ]
    if what=="class" and name in skip_prs:
        return True
    
    skip_mds = ['SchemaValidationError', 'SchemaValidationException', 'EstimationDataSetValidator', 'ValidPanels', 'SeqDoubleML']
    if what=="module" and name in skip_mds:
        return True
    #helpful debugging line
    #print what, name, obj, dir(obj)
    
    return skip
#autodoc_default_flags = ['inherited-members']
def setup(app):
    app.connect("autodoc-skip-member", skip)

    #Allow MarkDown
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: "build/apidoc/" + url,
			'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
			'enable_auto_doc_ref': True,
			'enable_math': True,
			'enable_inline_math': True
            }, True)
    app.add_transform(AutoStructify)

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['docs/static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

##Allow MarkDown.
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser', }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PricingEnginedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PricingEngine.tex', 'Pricing Engine Documentation',
     'Matt Goldman, Brian Quistorff', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pricingengine', 'Pricing Engine Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PricingEngine', 'Pricing Engine Documentation',
     author, 'PricingEngine', 'One line description of project.',
     'Miscellaneous'),
]
