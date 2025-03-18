import pytest

from app.main import StaticArray


def test_length():
    a = StaticArray(4)
    with pytest.raises(IndexError):
        _ = a[4]


def test_size():
    a = StaticArray(3)
    with pytest.raises(IndexError):
        last_index = a[3]


def set_item():
    a = StaticArray(2)
    a[1] = "value"
    assert a[1] == "value"
