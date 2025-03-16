import pytest

from app.queue_stacks import QueueStacks


def test_stacks_are_empty():
    a = QueueStacks(0,0)
    with pytest.raises(IndexError):
        a.pop()


def test_stacks_pop():
    a = QueueStacks(0,0)
    a.push(5)
    assert a.pop() == 5