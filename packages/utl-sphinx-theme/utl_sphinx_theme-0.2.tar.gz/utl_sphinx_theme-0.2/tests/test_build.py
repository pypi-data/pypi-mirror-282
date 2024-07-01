"""Sphinx build test."""

from __future__ import annotations


import io
import pathlib
import tempfile

import sphinx

import sphinx.addnodes
import sphinx.application


_PROJ_DIR = pathlib.Path(__file__).parent / '..'
_TEST_DOCS = _PROJ_DIR / 'docs'

_TEXT = """
<div class="pageheader">
  <a href="https://utlco.com">
    <img src="_static/logo.svg" alt="logo" />
  </a>
  <h1>{title}</h1>
</div>
"""
_TITLE = 'Test Title'


def test_build() -> None:
    """Test building documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:

        destdir = pathlib.Path(tmpdir, '_build')
        doctreedir = pathlib.Path(tmpdir, 'doctree')

        status = io.StringIO()
        warning = io.StringIO()

        kwargs = {
            'status': status,
            'warning': warning,
            'confoverrides': {
                'html_theme': 'utl_sphinx_theme',
                'html_theme_options': {
                    'title': _TITLE,
                },
            },
        }

        app = sphinx.application.Sphinx(
            _TEST_DOCS,
            _TEST_DOCS,
            destdir,
            doctreedir,
            'html',
            **kwargs,
        )
        app.builder.build_all()

        assert app.env.get_doctree('index').findall(sphinx.addnodes.toctree)

        index_path = pathlib.Path(app.outdir, 'index.html')
        with index_path.open() as f:
            content = f.read()

        assert _TEXT.format(title=_TITLE) in content
