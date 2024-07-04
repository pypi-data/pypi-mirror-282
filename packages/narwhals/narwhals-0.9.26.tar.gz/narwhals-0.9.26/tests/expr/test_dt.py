from __future__ import annotations

import contextlib
from datetime import datetime
from datetime import timedelta
from typing import Any

import hypothesis.strategies as st
import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pytest
from hypothesis import given

import narwhals as nw
from narwhals.utils import parse_version
from tests.utils import compare_dicts
from tests.utils import is_windows

data = {
    "a": [
        datetime(2021, 3, 1, 12, 34, 56, 49000),
        datetime(2020, 1, 2, 2, 4, 14, 715000),
    ],
}
data_timedelta = {
    "a": [
        None,
        timedelta(minutes=1, seconds=1, milliseconds=1, microseconds=1),
    ],
    "b": [
        timedelta(milliseconds=2),
        timedelta(milliseconds=1, microseconds=300),
    ],
    "c": np.array([None, 20], dtype="timedelta64[ns]"),
}


@pytest.mark.parametrize(
    ("attribute", "expected"),
    [
        ("year", [2021, 2020]),
        ("month", [3, 1]),
        ("day", [1, 2]),
        ("hour", [12, 2]),
        ("minute", [34, 4]),
        ("second", [56, 14]),
        ("millisecond", [49, 715]),
        ("microsecond", [49000, 715000]),
        ("nanosecond", [49000000, 715000000]),
        ("ordinal_day", [60, 2]),
    ],
)
def test_datetime_attributes(
    attribute: str,
    expected: list[int],
    constructor: Any,
) -> None:
    if "pyarrow" in str(constructor) and attribute in {
        "millisecond",
        "microsecond",
        "nanosecond",
    }:
        ctx: Any = pytest.raises(NotImplementedError, match="pyarrow")
    else:
        ctx = contextlib.nullcontext()
    df = nw.from_native(constructor(data), eager_only=True)
    with ctx:
        result = nw.to_native(df.select(getattr(nw.col("a").dt, attribute)()))
        compare_dicts(result, {"a": expected})
    with ctx:
        result = nw.to_native(df.select(getattr(df["a"].dt, attribute)()))
        compare_dicts(result, {"a": expected})


@pytest.mark.parametrize(
    ("attribute", "expected_a", "expected_b"),
    [
        ("total_minutes", [0, 1], [0, 0]),
        ("total_seconds", [0, 61], [0, 0]),
        ("total_milliseconds", [0, 61001], [2, 1]),
    ],
)
def test_duration_attributes(
    attribute: str,
    expected_a: list[int],
    expected_b: list[int],
    constructor: Any,
    request: Any,
) -> None:
    if (
        parse_version(pd.__version__) == parse_version("2.0.3")
        and "pyarrow" in str(constructor)
        and attribute in ("total_minutes", "total_seconds", "total_milliseconds")
    ):  # pragma: no cover
        request.applymarker(pytest.mark.xfail)
    df = nw.from_native(constructor(data_timedelta), eager_only=True)
    result_a = nw.to_native(df.select(getattr(nw.col("a").dt, attribute)().fill_null(0)))
    compare_dicts(result_a, {"a": expected_a})
    result_a = nw.to_native(df.select(getattr(df["a"].dt, attribute)().fill_null(0)))
    compare_dicts(result_a, {"a": expected_a})
    result_b = nw.to_native(df.select(getattr(nw.col("b").dt, attribute)().fill_null(0)))
    compare_dicts(result_b, {"b": expected_b})
    result_b = nw.to_native(df.select(getattr(df["b"].dt, attribute)().fill_null(0)))
    compare_dicts(result_b, {"b": expected_b})


@pytest.mark.parametrize(
    ("attribute", "expected_b", "expected_c"),
    [
        ("total_microseconds", [2000, 1300], [0, 0]),
        ("total_nanoseconds", [2000000, 1300000], [0, 20]),
    ],
)
def test_duration_micro_nano(
    attribute: str,
    expected_b: list[int],
    expected_c: list[int],
    constructor: Any,
    request: Any,
) -> None:
    if (
        parse_version(pd.__version__) == parse_version("2.0.3")
        and "pyarrow" in str(constructor)
        and attribute
        in (
            "total_minutes",
            "total_seconds",
            "total_milliseconds",
            "total_microseconds",
            "total_nanoseconds",
        )
    ):  # pragma: no cover
        request.applymarker(pytest.mark.xfail)
    df = nw.from_native(constructor(data_timedelta), eager_only=True)
    result_b = nw.to_native(df.select(getattr(nw.col("b").dt, attribute)().fill_null(0)))
    compare_dicts(result_b, {"b": expected_b})
    result_b = nw.to_native(df.select(getattr(df["b"].dt, attribute)().fill_null(0)))
    compare_dicts(result_b, {"b": expected_b})
    result_c = nw.to_native(df.select(getattr(nw.col("c").dt, attribute)().fill_null(0)))
    compare_dicts(result_c, {"c": expected_c})
    result_c = nw.to_native(df.select(getattr(df["c"].dt, attribute)().fill_null(0)))
    compare_dicts(result_c, {"c": expected_c})


@given(dates=st.datetimes(min_value=datetime(1960, 1, 1), max_value=datetime(1980, 1, 1)))  # type: ignore[misc]
@pytest.mark.skipif(
    parse_version(pd.__version__) < parse_version("2.0.0"),
    reason="pyarrow dtype not available",
)
def test_ordinal_day(dates: datetime) -> None:
    result_pd = nw.from_native(pd.Series([dates]), series_only=True).dt.ordinal_day()[0]
    result_pdms = nw.from_native(
        pd.Series([dates]).dt.as_unit("ms"), series_only=True
    ).dt.ordinal_day()[0]
    result_pda = nw.from_native(
        pd.Series([dates]).convert_dtypes(dtype_backend="pyarrow"), series_only=True
    ).dt.ordinal_day()[0]
    result_pdn = nw.from_native(
        pd.Series([dates]).convert_dtypes(dtype_backend="numpy_nullable"),
        series_only=True,
    ).dt.ordinal_day()[0]
    result_pl = nw.from_native(pl.Series([dates]), series_only=True).dt.ordinal_day()[0]
    assert result_pd == result_pl
    assert result_pda == result_pl
    assert result_pdn == result_pl
    assert result_pdms == result_pl


@given(
    timedeltas=st.timedeltas(
        min_value=-timedelta(days=5, minutes=70, seconds=10),
        max_value=timedelta(days=3, minutes=90, seconds=60),
    )
)  # type: ignore[misc]
@pytest.mark.skipif(
    parse_version(pd.__version__) < parse_version("2.2.0"),
    reason="pyarrow dtype not available",
)
def test_total_minutes(timedeltas: timedelta) -> None:
    result_pd = nw.from_native(
        pd.Series([timedeltas]), series_only=True
    ).dt.total_minutes()[0]
    result_pdns = nw.from_native(
        pd.Series([timedeltas]).dt.as_unit("ns"), series_only=True
    ).dt.total_minutes()[0]
    result_pda = nw.from_native(
        pd.Series([timedeltas]).convert_dtypes(dtype_backend="pyarrow"), series_only=True
    ).dt.total_minutes()[0]
    result_pdn = nw.from_native(
        pd.Series([timedeltas]).convert_dtypes(dtype_backend="numpy_nullable"),
        series_only=True,
    ).dt.total_minutes()[0]
    result_pl = nw.from_native(
        pl.Series([timedeltas]), series_only=True
    ).dt.total_minutes()[0]
    assert result_pd == result_pl
    assert result_pda == result_pl
    assert result_pdn == result_pl
    assert result_pdns == result_pl


@pytest.mark.parametrize(
    "fmt", ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%G-W%V-%u", "%G-W%V"]
)
@pytest.mark.skipif(is_windows(), reason="pyarrow breaking on windows")
def test_dt_to_string(constructor_with_pyarrow: Any, fmt: str) -> None:
    input_frame = nw.from_native(constructor_with_pyarrow(data), eager_only=True)
    input_series = input_frame["a"]

    expected_col = [datetime.strftime(d, fmt) for d in data["a"]]

    result = input_series.dt.to_string(fmt).to_list()
    if constructor_with_pyarrow is pa.table or "pyarrow" in str(constructor_with_pyarrow):
        # PyArrow differs from other libraries, in that %S also shows
        # the fraction of a second.
        result = [x[: x.find(".")] if "." in x else x for x in result]
    assert result == expected_col
    result = input_frame.select(nw.col("a").dt.to_string(fmt))["a"].to_list()
    if constructor_with_pyarrow is pa.table or "pyarrow" in str(constructor_with_pyarrow):
        # PyArrow differs from other libraries, in that %S also shows
        # the fraction of a second.
        result = [x[: x.find(".")] if "." in x else x for x in result]
    assert result == expected_col


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (datetime(2020, 1, 9), "2020-01-09T00:00:00.000000"),
        (datetime(2020, 1, 9, 12, 34, 56), "2020-01-09T12:34:56.000000"),
        (datetime(2020, 1, 9, 12, 34, 56, 123), "2020-01-09T12:34:56.000123"),
        (datetime(2020, 1, 9, 12, 34, 56, 123456), "2020-01-09T12:34:56.123456"),
    ],
)
@pytest.mark.skipif(is_windows(), reason="pyarrow breaking on windows")
def test_dt_to_string_iso_local_datetime(
    constructor_with_pyarrow: Any, data: datetime, expected: str
) -> None:
    def _clean_string(result: str) -> str:
        # rstrip '0' to remove trailing zeros, as different libraries handle this differently
        # if there's then a trailing `.`, remove that too.
        if "." in result:
            result = result.rstrip("0").rstrip(".")
        return result

    df = constructor_with_pyarrow({"a": [data]})
    result = (
        nw.from_native(df, eager_only=True)["a"]
        .dt.to_string("%Y-%m-%dT%H:%M:%S.%f")
        .to_list()[0]
    )
    assert _clean_string(result) == _clean_string(expected)

    result = (
        nw.from_native(df, eager_only=True)
        .select(nw.col("a").dt.to_string("%Y-%m-%dT%H:%M:%S.%f"))["a"]
        .to_list()[0]
    )
    assert _clean_string(result) == _clean_string(expected)

    result = (
        nw.from_native(df, eager_only=True)["a"]
        .dt.to_string("%Y-%m-%dT%H:%M:%S%.f")
        .to_list()[0]
    )
    assert _clean_string(result) == _clean_string(expected)

    result = (
        nw.from_native(df, eager_only=True)
        .select(nw.col("a").dt.to_string("%Y-%m-%dT%H:%M:%S%.f"))["a"]
        .to_list()[0]
    )
    assert _clean_string(result) == _clean_string(expected)


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (datetime(2020, 1, 9), "2020-01-09"),
    ],
)
@pytest.mark.skipif(is_windows(), reason="pyarrow breaking on windows")
def test_dt_to_string_iso_local_date(
    constructor_with_pyarrow: Any, data: datetime, expected: str
) -> None:
    df = constructor_with_pyarrow({"a": [data]})
    result = (
        nw.from_native(df, eager_only=True)["a"].dt.to_string("%Y-%m-%d").to_list()[0]
    )
    assert result == expected

    result = (
        nw.from_native(df, eager_only=True)
        .select(b=nw.col("a").dt.to_string("%Y-%m-%d"))["b"]
        .to_list()[0]
    )
    assert result == expected
