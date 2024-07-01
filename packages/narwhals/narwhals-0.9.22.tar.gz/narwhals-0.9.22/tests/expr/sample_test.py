from typing import Any

import pandas as pd
import polars as pl
import pytest

import narwhals as nw


@pytest.mark.parametrize("constructor", [pd.DataFrame, pl.DataFrame])
def test_expr_sample(constructor: Any) -> None:
    df = nw.from_native(constructor({"a": [1, 2, 3], "b": [4, 5, 6]})).lazy()
    result_shape = nw.to_native(df.select(nw.col("a").sample(n=2)).collect()).shape
    expected = (2, 1)
    assert result_shape == expected
    result_shape = nw.to_native(df.collect()["a"].sample(n=2)).shape
    expected = (2,)  # type: ignore[assignment]
    assert result_shape == expected
