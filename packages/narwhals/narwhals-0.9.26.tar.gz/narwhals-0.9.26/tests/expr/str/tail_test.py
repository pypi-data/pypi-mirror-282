from typing import Any

import narwhals as nw
from tests.utils import compare_dicts

data = {
    "a": ["foo", "bars"],
}


def test_str_tail(constructor: Any) -> None:
    df = nw.from_native(constructor(data), eager_only=True)
    expected = {
        "a": ["foo", "ars"],
    }

    result_frame = df.select(nw.col("a").str.tail(3))
    compare_dicts(result_frame, expected)

    result_series = df["a"].str.tail(3)
    assert result_series.to_numpy().tolist() == expected["a"]
