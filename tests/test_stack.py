from app.stack import Stack


def test_get_size():
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.get_size() == 1

def test_push():
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.top() == expected_value
