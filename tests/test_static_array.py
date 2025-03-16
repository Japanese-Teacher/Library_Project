import pytest

from app.main import StaticArray


def test_length():
    a = StaticArray(4)
    with pytest.raises(IndexError):
        _ = a[4]
