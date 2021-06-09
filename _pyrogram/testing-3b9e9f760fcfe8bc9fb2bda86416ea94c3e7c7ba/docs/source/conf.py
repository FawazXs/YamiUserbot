# TG-UserBot - A modular Telegram UserBot script for Python.
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import sphinx_rtd_theme  # noqa: F401
from time import strftime

sys.path.insert(0, os.path.abspath('../..'))

from userbot import __version__  # noqa: E402

project = 'TG-UserBot'
copyright = '2019 - 2020, Kandarp'
author = 'Kandarp'

version = __version__
release = 'stable'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme"
]

exclude_patterns = [
    '*generate_session.py',
    '*__init__.py',
    '*__main__.py'
]

master_doc = 'index'
autosummary_generate = True
napoleon_use_rtype = False
pygments_style = "monokai"
pagename = "TG-UserBot Documentation"
html_title = "TG-UserBot Documentation"
html_short_title = "TG-UserBot"
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_theme = "sphinx_rtd_theme"
html_logo = "_images/logo.svg"
html_favicon = "_images/favicon.ico"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
templates_path = ['_templates']
html_static_path = ['_static']
show_authors = True


intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
    'show-inheritance': True,
    'exclude-members': '__init__, __main__',
    'ignore-module-all': True
}

html_theme_options = {
    'canonical_url': 'tg-userbot.readthedocs.io',
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_external_links': False,
    'style_nav_header_background': '#EF3449'
}

html_context = {
    # Our last updated format.
    'l_updated': strftime('%b %d, %Y'),
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,
    'github_user': 'TG-UserBot',
    'github_repo': 'TG-UserBot',
    'github_version': 'master',
    'conf_py_path': '/docs/source/'
}
