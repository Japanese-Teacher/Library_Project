from typing import Any

from app.dynamic_array import DynamicArray


class Stack:
    def __init__(self):
        self._list = DynamicArray(0)

    def push(self, value) -> Any:
        return self._list.append(value)

    def top(self) -> Any:
        return self._list[self._list.get_size() - 1]

    def pop(self) -> Any:
        return self._list.pop()

    def get_size(self) -> int:
        return self._list.get_size()

    def is_empty(self) -> bool:
        return self._list.is_empty()
