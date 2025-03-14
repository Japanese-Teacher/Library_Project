from app.dynamic_array import DynamicArray


class Stack:
    def __init__(self, size: int):
        self._size = size
        self._list = DynamicArray(self._size)

    def push(self, value):
        self._list.append(value)

    def top(self):
        return self._list[self._size - 1]

    def pop(self):
        self._list.pop()

    def is_empty(self) -> bool:
        return self._list.is_empty()