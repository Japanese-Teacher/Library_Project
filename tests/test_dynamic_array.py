from app.dynamic_array import DynamicArray


def test_is_empty() -> None:
    a = DynamicArray(4)
    a.append("value")
    assert a.is_empty() is False


def test_append() -> None:
    a = DynamicArray(1)
    a.append("value")
    assert a[1] == "value"


def test_set_item() -> None:
    a = DynamicArray(2)
    a[0] = 2
    assert a[0] == 2

def test_get_size() -> None:
    a = DynamicArray(2)
    assert a.get_size() == 2