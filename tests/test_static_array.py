import pytest

from app.main import StaticArray
from typing import Any


def test_length() -> Any:
    a = StaticArray(4)
    with pytest.raises(IndexError):
        _ = a[4]


def test_set_item() -> None:
    a = StaticArray(2)
    expected_value = 'value'
    a[1] = expected_value
    assert a[1] == expected_value
