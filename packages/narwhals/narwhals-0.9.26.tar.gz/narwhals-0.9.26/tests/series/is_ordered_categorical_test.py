from typing import Any

import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

import narwhals as nw


def test_is_ordered_categorical() -> None:
    s = pl.Series(["a", "b"], dtype=pl.Categorical)
    assert nw.is_ordered_categorical(nw.from_native(s, series_only=True))
    s = pl.Series(["a", "b"], dtype=pl.Categorical(ordering="lexical"))
    assert not nw.is_ordered_categorical(nw.from_native(s, series_only=True))
    s = pl.Series(["a", "b"], dtype=pl.Enum(["a", "b"]))
    assert nw.is_ordered_categorical(nw.from_native(s, series_only=True))
    s = pd.Series(["a", "b"], dtype=pd.CategoricalDtype(ordered=True))
    assert nw.is_ordered_categorical(nw.from_native(s, series_only=True))
    s = pd.Series(["a", "b"], dtype=pd.CategoricalDtype(ordered=False))
    assert not nw.is_ordered_categorical(nw.from_native(s, series_only=True))
    s = pa.chunked_array(
        [pa.array(["a", "b"], type=pa.dictionary(pa.int32(), pa.string()))]
    )
    assert not nw.is_ordered_categorical(nw.from_native(s, series_only=True))


def test_is_definitely_not_ordered_categorical(
    constructor_series_with_pyarrow: Any,
) -> None:
    assert not nw.is_ordered_categorical(
        nw.from_native(constructor_series_with_pyarrow([1, 2, 3]), series_only=True)
    )


@pytest.mark.xfail(reason="https://github.com/apache/arrow/issues/41017")
def test_is_ordered_categorical_pyarrow() -> None:
    s = pa.chunked_array(
        [pa.array(["a", "b"], type=pa.dictionary(pa.int32(), pa.string(), ordered=True))]
    )
    assert nw.is_ordered_categorical(nw.from_native(s, series_only=True))
