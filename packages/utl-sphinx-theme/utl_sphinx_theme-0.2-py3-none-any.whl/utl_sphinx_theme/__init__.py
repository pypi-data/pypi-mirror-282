
# See: https://www.sphinx-doc.org/en/master/development/theming.html

from os import path

def setup(app):
    app.add_html_theme('utl_sphinx_theme', path.abspath(path.dirname(__file__)))
