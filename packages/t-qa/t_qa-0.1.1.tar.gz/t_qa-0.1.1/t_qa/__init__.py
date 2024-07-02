"""Top-level package for T QA."""

__author__ = """Thoughtful"""
__email__ = "support@thoughtful.ai"
__version__ = "__version__ = '0.1.1'"

from .qa import configure, test_case_passed, test_case_failed

__all__ = [
    "configure",
    "test_case_passed",
    "test_case_failed",
]
