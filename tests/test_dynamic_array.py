from app.dynamic_array import DynamicArray


def test_is_empty():
    a = DynamicArray(4)
    a.append("value")
    assert a.is_empty() == False


def test_append():
    a = DynamicArray(1)
    a.append("value")
    assert a[1] == "value"


def set_item():
    a = DynamicArray(2)
    a[0] = "value"
    a[0] = 2
    assert a[0] == 2
