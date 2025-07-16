"""
My GitHub Class - A tutorial project for GitHub Actions with Python.
"""

__version__ = "0.1.0"
__author__ = "GitHub Actions Tutorial"
__email__ = "tutorial@example.com"

from .calculator import Calculator
from .utils import (
    chunks,
    filter_list,
    format_currency,
    get_file_size,
    read_json_file,
    validate_email,
    write_json_file,
)

__all__ = [
    "Calculator",
    "chunks",
    "filter_list",
    "format_currency",
    "get_file_size",
    "read_json_file",
    "validate_email",
    "write_json_file",
]