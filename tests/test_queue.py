import pytest

from app.queue_stacks import QueueStacks


def test_stacks_are_empty():
    a = QueueStacks()
    with pytest.raises(IndexError):
        a.pop()


def test_stacks_pop():
    a = QueueStacks()
    a.push(5)
    assert a.pop() == 5

