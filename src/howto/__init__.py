"""
howto - A Python package project.
"""

from importlib.metadata import metadata
from . import animals

try:
    pkg_metadata = metadata("howto")
    __version__ = pkg_metadata["Version"]
except ImportError:
    # fallback for development
    __version__ = "0.1.0"

