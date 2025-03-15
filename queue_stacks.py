from stack import Stack


class QueueStacks:

    def __init__(self):
        self._list_l = Stack()
        self._list_r = Stack()
    def push(self, value):
        self._list_l.push(value)
    def pop(self):
        if self._list_r.is_empty():
            while not self._list_l.is_empty():
                self._list_r.push(self._list_l.pop())
        self._list_r.pop()