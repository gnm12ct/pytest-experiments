"""
Configure assertion rewrites

Pytest needs to be told which modules need assertions rewritting. This
enables detailed traceback information to be returned, such as showing
the differences in expected and actual results. Any modules with
assertions used in the plugin need to be specified here.

https://docs.pytest.org/en/latest/writing_plugins.html#assertion-rewriting
"""

import pytest

pytest.register_assert_rewrite("pytest_files.items")