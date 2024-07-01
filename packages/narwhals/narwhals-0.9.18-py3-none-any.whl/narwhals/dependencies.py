# pandas / Polars / etc. : if a user passes a dataframe from one of these
# libraries, it means they must already have imported the given module.
# So, we can just check sys.modules.

import sys
from typing import Any


def get_polars() -> Any:
    """Get Polars module (if already imported - else return None)."""
    return sys.modules.get("polars", None)


def get_pandas() -> Any:
    """Get pandas module (if already imported - else return None)."""
    return sys.modules.get("pandas", None)


def get_modin() -> Any:  # pragma: no cover
    """Get modin.pandas module (if already imported - else return None)."""
    if (modin := sys.modules.get("modin", None)) is not None:
        return modin.pandas
    return None


def get_cudf() -> Any:
    """Get cudf module (if already imported - else return None)."""
    return sys.modules.get("cudf", None)


def get_pyarrow() -> Any:  # pragma: no cover
    """Get pyarrow module (if already imported - else return None)."""
    return sys.modules.get("pyarrow", None)


def get_pyarrow_compute() -> Any:  # pragma: no cover
    """Get pyarrow.compute module (if pyarrow has already been imported - else return None)."""
    if "pyarrow" in sys.modules:
        import pyarrow.compute as pc

        return pc
    return None


def get_numpy() -> Any:
    """Get numpy module (if already imported - else return None)."""
    return sys.modules.get("numpy", None)
