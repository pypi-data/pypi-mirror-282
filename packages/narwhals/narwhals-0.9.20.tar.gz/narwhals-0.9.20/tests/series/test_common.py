from __future__ import annotations

import re
from typing import Any
from typing import Literal

import numpy as np
import pandas as pd
import polars as pl
import pytest
from numpy.testing import assert_array_equal
from pandas.testing import assert_series_equal

import narwhals as nw
from narwhals.utils import parse_version

df_pandas = pd.DataFrame({"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]})
if parse_version(pd.__version__) >= parse_version("1.5.0"):
    df_pandas_pyarrow = pd.DataFrame(
        {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]}
    ).astype(
        {
            "a": "Int64[pyarrow]",
            "b": "Int64[pyarrow]",
            "z": "Float64[pyarrow]",
        }
    )
    df_pandas_nullable = pd.DataFrame(
        {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]}
    ).astype(
        {
            "a": "Int64",
            "b": "Int64",
            "z": "Float64",
        }
    )
else:  # pragma: no cover
    # pyarrow/nullable dtypes not supported so far back
    df_pandas_pyarrow = df_pandas
    df_pandas_nullable = df_pandas
df_polars = pl.DataFrame({"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]})
df_lazy = pl.LazyFrame({"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]})


@pytest.mark.parametrize(
    "df_raw", [df_pandas, df_polars, df_pandas_nullable, df_pandas_pyarrow]
)
def test_len(df_raw: Any) -> None:
    result = len(nw.from_native(df_raw["a"], series_only=True))
    assert result == 3
    result = nw.from_native(df_raw["a"], series_only=True).len()
    assert result == 3
    result = len(nw.from_native(df_raw)["a"])
    assert result == 3


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.filterwarnings("ignore:np.find_common_type is deprecated:DeprecationWarning")
def test_is_in(df_raw: Any) -> None:
    result = nw.from_native(df_raw["a"], series_only=True).is_in([1, 2])
    assert result[0]
    assert not result[1]
    assert result[2]


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.filterwarnings("ignore:np.find_common_type is deprecated:DeprecationWarning")
def test_is_in_other(df_raw: Any) -> None:
    with pytest.raises(
        NotImplementedError,
        match=(
            "Narwhals `is_in` doesn't accept expressions as an argument, as opposed to Polars. You should provide an iterable instead."
        ),
    ):
        nw.from_native(df_raw).with_columns(contains=nw.col("c").is_in("sets"))


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.filterwarnings("ignore:np.find_common_type is deprecated:DeprecationWarning")
def test_filter(df_raw: Any) -> None:
    result = nw.from_native(df_raw["a"], series_only=True).filter(df_raw["a"] > 1)
    expected = np.array([3, 2])
    assert (result.to_numpy() == expected).all()
    result = nw.from_native(df_raw, eager_only=True).select(
        nw.col("a").filter(nw.col("a") > 1)
    )["a"]
    expected = np.array([3, 2])
    assert (result.to_numpy() == expected).all()


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_gt(df_raw: Any) -> None:
    s = nw.from_native(df_raw["a"], series_only=True)
    result = s > s  # noqa: PLR0124
    assert not result[0]
    assert not result[1]
    assert not result[2]
    result = s > 1
    assert not result[0]
    assert result[1]
    assert result[2]


@pytest.mark.parametrize(
    "df_raw", [df_pandas, df_lazy, df_pandas_nullable, df_pandas_pyarrow]
)
def test_dtype(df_raw: Any) -> None:
    result = nw.from_native(df_raw).lazy().collect()["a"].dtype
    assert result == nw.Int64
    assert result.is_numeric()


@pytest.mark.parametrize(
    "df_raw", [df_pandas, df_lazy, df_pandas_nullable, df_pandas_pyarrow]
)
def test_reductions(df_raw: Any) -> None:
    s = nw.from_native(df_raw).lazy().collect()["a"]
    assert s.mean() == 2.0
    assert s.std() == 1.0
    assert s.min() == 1
    assert s.max() == 3
    assert s.sum() == 6
    assert nw.to_native(s.is_between(1, 2))[0]
    assert not nw.to_native(s.is_between(1, 2))[1]
    assert nw.to_native(s.is_between(1, 2))[2]
    assert s.n_unique() == 3
    unique = s.unique().sort()
    assert unique[0] == 1
    assert unique[1] == 2
    assert unique[2] == 3
    assert s.alias("foo").name == "foo"


@pytest.mark.parametrize(
    "df_raw", [df_pandas, df_lazy, df_pandas_nullable, df_pandas_pyarrow]
)
def test_boolean_reductions(df_raw: Any) -> None:
    df = nw.from_native(df_raw).lazy().select(nw.col("a") > 1)
    assert not df.collect()["a"].all()
    assert df.collect()["a"].any()


@pytest.mark.parametrize("df_raw", [df_pandas, df_lazy])
def test_convert(df_raw: Any) -> None:
    result = nw.from_native(df_raw).lazy().collect()["a"].to_numpy()
    assert_array_equal(result, np.array([1, 3, 2]))
    result = nw.from_native(df_raw).lazy().collect()["a"].to_pandas()
    assert_series_equal(result, pd.Series([1, 3, 2], name="a"))


def test_cast() -> None:
    df_raw = pl.DataFrame(
        {
            "a": [1],
            "b": [1],
            "c": [1],
            "d": [1],
            "e": [1],
            "f": [1],
            "g": [1],
            "h": [1],
            "i": [1],
            "j": [1],
            "k": ["1"],
            "l": [1],
            "m": [True],
            "n": [True],
            "o": ["a"],
            "p": [1],
        },
        schema={
            "a": pl.Int64,
            "b": pl.Int32,
            "c": pl.Int16,
            "d": pl.Int8,
            "e": pl.UInt64,
            "f": pl.UInt32,
            "g": pl.UInt16,
            "h": pl.UInt8,
            "i": pl.Float64,
            "j": pl.Float32,
            "k": pl.String,
            "l": pl.Datetime,
            "m": pl.Boolean,
            "n": pl.Boolean,
            "o": pl.Categorical,
            "p": pl.Int64,
        },
    )
    df = nw.from_native(df_raw, eager_only=True).select(
        nw.col("a").cast(nw.Int32),
        nw.col("b").cast(nw.Int16),
        nw.col("c").cast(nw.Int8),
        nw.col("d").cast(nw.Int64),
        nw.col("e").cast(nw.UInt32),
        nw.col("f").cast(nw.UInt16),
        nw.col("g").cast(nw.UInt8),
        nw.col("h").cast(nw.UInt64),
        nw.col("i").cast(nw.Float32),
        nw.col("j").cast(nw.Float64),
        nw.col("k").cast(nw.String),
        nw.col("l").cast(nw.Datetime),
        nw.col("m").cast(nw.Int8),
        nw.col("n").cast(nw.Int8),
        nw.col("o").cast(nw.String),
        nw.col("p").cast(nw.Duration),
    )
    result = df.schema
    expected = {
        "a": nw.Int32,
        "b": nw.Int16,
        "c": nw.Int8,
        "d": nw.Int64,
        "e": nw.UInt32,
        "f": nw.UInt16,
        "g": nw.UInt8,
        "h": nw.UInt64,
        "i": nw.Float32,
        "j": nw.Float64,
        "k": nw.String,
        "l": nw.Datetime,
        "m": nw.Int8,
        "n": nw.Int8,
        "o": nw.String,
        "p": nw.Duration,
    }
    assert result == expected
    result_pd = nw.from_native(df.to_pandas(), eager_only=True).schema
    assert result_pd == expected
    result = df.select(
        df["a"].cast(nw.Int32),
        df["b"].cast(nw.Int16),
        df["c"].cast(nw.Int8),
        df["d"].cast(nw.Int64),
        df["e"].cast(nw.UInt32),
        df["f"].cast(nw.UInt16),
        df["g"].cast(nw.UInt8),
        df["h"].cast(nw.UInt64),
        df["i"].cast(nw.Float32),
        df["j"].cast(nw.Float64),
        df["k"].cast(nw.String),
        df["l"].cast(nw.Datetime),
        df["m"].cast(nw.Int8),
        df["n"].cast(nw.Boolean),
        df["o"].cast(nw.Categorical),
        df["p"].cast(nw.Duration),
    ).schema
    expected = {
        "a": nw.Int32,
        "b": nw.Int16,
        "c": nw.Int8,
        "d": nw.Int64,
        "e": nw.UInt32,
        "f": nw.UInt16,
        "g": nw.UInt8,
        "h": nw.UInt64,
        "i": nw.Float32,
        "j": nw.Float64,
        "k": nw.String,
        "l": nw.Datetime,
        "m": nw.Int8,
        "n": nw.Boolean,
        "o": nw.Categorical,
        "p": nw.Duration,
    }
    df = nw.from_native(df.to_pandas())  # type: ignore[assignment]
    result_pd = df.select(
        df["a"].cast(nw.Int32),
        df["b"].cast(nw.Int16),
        df["c"].cast(nw.Int8),
        df["d"].cast(nw.Int64),
        df["e"].cast(nw.UInt32),
        df["f"].cast(nw.UInt16),
        df["g"].cast(nw.UInt8),
        df["h"].cast(nw.UInt64),
        df["i"].cast(nw.Float32),
        df["j"].cast(nw.Float64),
        df["k"].cast(nw.String),
        df["l"].cast(nw.Datetime),
        df["m"].cast(nw.Int8),
        df["n"].cast(nw.Boolean),
        df["o"].cast(nw.Categorical),
        df["p"].cast(nw.Duration),
    ).schema
    assert result == expected
    df = nw.from_native(df.to_pandas().convert_dtypes())  # type: ignore[assignment]
    result_pd = df.select(
        df["a"].cast(nw.Int32),
        df["b"].cast(nw.Int16),
        df["c"].cast(nw.Int8),
        df["d"].cast(nw.Int64),
        df["e"].cast(nw.UInt32),
        df["f"].cast(nw.UInt16),
        df["g"].cast(nw.UInt8),
        df["h"].cast(nw.UInt64),
        df["i"].cast(nw.Float32),
        df["j"].cast(nw.Float64),
        df["k"].cast(nw.String),
        df["l"].cast(nw.Datetime),
        df["m"].cast(nw.Int8),
        df["n"].cast(nw.Boolean),
        df["o"].cast(nw.Categorical),
        df["p"].cast(nw.Duration),
    ).schema
    assert result == expected
    if parse_version(pd.__version__) < parse_version("2.0.0"):  # pragma: no cover
        return
    df = nw.from_native(df.to_pandas().convert_dtypes(dtype_backend="pyarrow"))  # type: ignore[assignment]
    result_pd = df.select(
        df["a"].cast(nw.Int32),
        df["b"].cast(nw.Int16),
        df["c"].cast(nw.Int8),
        df["d"].cast(nw.Int64),
        df["e"].cast(nw.UInt32),
        df["f"].cast(nw.UInt16),
        df["g"].cast(nw.UInt8),
        df["h"].cast(nw.UInt64),
        df["i"].cast(nw.Float32),
        df["j"].cast(nw.Float64),
        df["k"].cast(nw.String),
        df["l"].cast(nw.Datetime),
        df["m"].cast(nw.Int8),
        df["n"].cast(nw.Boolean),
        df["o"].cast(nw.Categorical),
        df["p"].cast(nw.Duration),
    ).schema
    assert result == expected


def test_to_numpy() -> None:
    s = pd.Series([1, 2, None], dtype="Int64")
    nw_series = nw.from_native(s, series_only=True)
    assert nw_series.to_numpy().dtype == "float64"
    assert nw_series.__array__().dtype == "float64"
    assert nw_series.shape == (3,)


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_is_duplicated(df_raw: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    result = series.is_duplicated()
    expected = np.array([True, True, False])
    assert (result.to_numpy() == expected).all()


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize(("threshold", "expected"), [(0, False), (10, True)])
def test_is_empty(df_raw: Any, threshold: Any, expected: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    result = series.filter(series > threshold).is_empty()
    assert result == expected


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_is_unique(df_raw: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    result = series.is_unique()
    expected = np.array([False, False, True])
    assert (result.to_numpy() == expected).all()


@pytest.mark.parametrize("s_raw", [pd.Series([1, 2, None]), pl.Series([1, 2, None])])
def test_null_count(s_raw: Any) -> None:
    series = nw.from_native(s_raw, series_only=True)
    result = series.null_count()
    assert result == 1


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_is_first_distinct(df_raw: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    result = series.is_first_distinct()
    expected = np.array([True, False, True])
    assert (result.to_numpy() == expected).all()


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_is_last_distinct(df_raw: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    result = series.is_last_distinct()
    expected = np.array([False, True, True])
    assert (result.to_numpy() == expected).all()


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_value_counts(df_raw: Any) -> None:
    series = nw.from_native(df_raw["b"], series_only=True)
    sorted_result = series.value_counts(sort=True)
    assert sorted_result.columns == ["b", "count"]

    expected = np.array([[4, 2], [6, 1]])
    assert (sorted_result.to_numpy() == expected).all()

    unsorted_result = series.value_counts(sort=False)
    assert unsorted_result.columns == ["b", "count"]

    a = unsorted_result.to_numpy()

    assert (a[a[:, 0].argsort()] == expected).all()


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize(
    ("col", "descending", "expected"),
    [("a", False, False), ("z", False, True), ("z", True, False)],
)
def test_is_sorted(df_raw: Any, col: str, descending: bool, expected: bool) -> None:  # noqa: FBT001
    series = nw.from_native(df_raw[col], series_only=True)
    result = series.is_sorted(descending=descending)
    assert result == expected


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
def test_is_sorted_invalid(df_raw: Any) -> None:
    series = nw.from_native(df_raw["z"], series_only=True)

    with pytest.raises(TypeError):
        series.is_sorted(descending="invalid_type")  # type: ignore[arg-type]


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize(
    ("interpolation", "expected"),
    [
        ("lower", 7.0),
        ("higher", 8.0),
        ("midpoint", 7.5),
        ("linear", 7.6),
        ("nearest", 8.0),
    ],
)
@pytest.mark.filterwarnings("ignore:the `interpolation=` argument to percentile")
def test_quantile(
    df_raw: Any,
    interpolation: Literal["nearest", "higher", "lower", "midpoint", "linear"],
    expected: float,
) -> None:
    q = 0.3

    series = nw.from_native(df_raw["z"], allow_series=True)
    result = series.quantile(quantile=q, interpolation=interpolation)  # type: ignore[union-attr]
    assert result == expected


@pytest.mark.parametrize(
    ("df_raw", "mask", "expected"),
    [
        (df_pandas, pd.Series([True, False, True]), pd.Series([1, 4, 2])),
        (df_polars, pl.Series([True, False, True]), pl.Series([1, 4, 2])),
    ],
)
def test_zip_with(df_raw: Any, mask: Any, expected: Any) -> None:
    series1 = nw.from_native(df_raw["a"], series_only=True)
    series2 = nw.from_native(df_raw["b"], series_only=True)
    mask = nw.from_native(mask, series_only=True)
    result = series1.zip_with(mask, series2)
    expected = nw.from_native(expected, series_only=True)
    assert result == expected


def test_cast_string() -> None:
    s_pd = pd.Series([1, 2]).convert_dtypes()
    s = nw.from_native(s_pd, series_only=True)
    s = s.cast(nw.String)
    result = nw.to_native(s)
    assert result.dtype in ("string", object)


df_pandas = pd.DataFrame({"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]})


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize(("index", "expected"), [(0, 1), (1, 3)])
def test_item(df_raw: Any, index: int, expected: int) -> None:
    s = nw.from_native(df_raw["a"], series_only=True)
    result = s.item(index)
    assert result == expected
    assert nw.from_native(df_raw["a"].head(1), series_only=True).item() == 1

    with pytest.raises(
        ValueError,
        match=re.escape("can only call '.item()' if the Series is of length 1,"),
    ):
        s.item(None)


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize("n", [1, 2, 3, 10])
def test_head(df_raw: Any, n: int) -> None:
    s_raw = df_raw["z"]
    s = nw.from_native(s_raw, allow_series=True)

    assert s.head(n) == nw.from_native(s_raw.head(n), series_only=True)


@pytest.mark.parametrize("df_raw", [df_pandas, df_polars])
@pytest.mark.parametrize("n", [1, 2, 3, 10])
def test_tail(df_raw: Any, n: int) -> None:
    s_raw = df_raw["z"]
    s = nw.from_native(s_raw, allow_series=True)

    assert s.tail(n) == nw.from_native(s_raw.tail(n), series_only=True)
