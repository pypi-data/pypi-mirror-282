
================
utl_sphinx_theme
================

* Github: https://github.com/utlco/utl-sphinx-theme
* Documentation: https://utlco.github.io/utl-sphinx-theme/

Very simple
`Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_
theme derived from **sphinx13** which is used for official Sphinx documentation.

There are a few small differences, mainly in colors and header styling.

Some basic options have been added as well.

How to use
==========

Install the theme from GitHub::

    pip install https://github.com/utlco/utl-sphinx-theme/archive/refs/heads/main.zip

Add the following line to your conf.py::

    html_theme = 'utl_sphinx_theme'

To change the theme options (also in conf.py)::

    html_options = {
        'title': 'MyTitle',
        'logo': '_static/my-logo.svg',
    }

By default it will use the logo image **_static/logo.svg**.

