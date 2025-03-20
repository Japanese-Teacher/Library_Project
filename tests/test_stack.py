from app.stack import Stack


def test_get_size():
    a = Stack()
    assert a.get_size() == 0
    a.push('value')
    assert a.get_size() == 1

def test_push():
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.top() == expected_value

def test_top():
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.top() == expected_value

def test_pop():
    a = Stack()
    expected_value = 'value'
    a.push(expected_value)
    assert a.pop() == expected_value
    assert a.get_size() == 0