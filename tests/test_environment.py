"""Minimal checks of the development environment; no data or model tests."""

import importlib
import sys

import pytest


def test_virtual_environment():
    assert sys.prefix != sys.base_prefix
    assert sys.version_info[:2] == (3, 12)


@pytest.mark.parametrize("module", [
    "numpy", "pandas", "scipy", "openpyxl", "penaltyblog", "sklearn",
    "matplotlib", "seaborn", "jupyterlab", "ipykernel", "pytest",
    "dixon_coles_modern",
])
def test_import(module):
    importlib.import_module(module)
