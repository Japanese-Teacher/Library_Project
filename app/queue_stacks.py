from app.stack import Stack


class QueueStacks:

    def __init__(self, _size_l: int, _size_r: int):
        self._size_l = _size_l
        self._size_r = _size_r
        self._list_l = Stack(self._size_l)
        self._list_r = Stack(self._size_r)
    def push(self, value):
        self._list_l.push(value)
    def pop(self):
        if self._list_r.is_empty():
            while not self._list_l.is_empty():
                self._list_r.push(self._list_l.pop())
        return self._list_r.pop()
