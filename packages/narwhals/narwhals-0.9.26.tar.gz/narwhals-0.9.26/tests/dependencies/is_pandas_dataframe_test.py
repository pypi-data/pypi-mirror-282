import pandas as pd
import polars as pl

from narwhals.dependencies import is_pandas_dataframe


def test_is_pandas_dataframe() -> None:
    assert is_pandas_dataframe(pd.DataFrame())
    assert not is_pandas_dataframe(pl.DataFrame())
