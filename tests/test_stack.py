from app.stack import Stack


def test_get_size() -> None:
    a = Stack()
    assert a.get_size() == 0
    a.push('value')
    assert a.get_size() == 1

def test_push() -> None:
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.top() == expected_value

def test_top() -> None:
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.top() == expected_value

def test_pop() -> None:
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.pop() == expected_value
    assert a.get_size() == 0