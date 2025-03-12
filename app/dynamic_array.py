from typing import Any

from main import StaticArray


class DynamicArray:

    def __init__(self, size: int):
        self._size = size
        self._real_size = int(self._size * 1.5)
        self._list = StaticArray(self._real_size)

    def __getitem__(self, item: int) -> Any:
        return self._list[item]

    def __setitem__(self, key: int, value: Any) -> None:
        self._list[key] = value

    def is_empty(self) -> bool:
        if not self._size > 0:
            return True
        return False

    def append(self, value: Any) -> Any:
        if self._size < self._real_size:
            self._list[self._size] = value
            self._size += 1
        else:
            self._list[self._size] = value
            self._real_size = self._real_size * 1.5
            self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Pop from empty array")
        value = self._list[self._size - 1]
        self._list[self._size - 1] = None
        self._size -= 1
        return value