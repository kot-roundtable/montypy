"""Unit tests for __version__.py."""

import montypy


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(montypy, "__version__")
    assert montypy.__version__ != "0.0.0"
