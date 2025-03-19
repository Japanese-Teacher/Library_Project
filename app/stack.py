from app.dynamic_array import DynamicArray


class Stack:
    def __init__(self):
        self._size = 0
        self._list = DynamicArray(self._size)

    def push(self, value):
        return self._list.append(value)

    def top(self):
        return self._list[self._size - 1]

    def pop(self):
        return self._list.pop()

    def get_size(self):
        return self._size

    def is_empty(self) -> bool:
        return self._list.is_empty()
