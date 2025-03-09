from typing import Any


class StaticArray:

    def __init__(self, size: int):
        self._list = [None for _ in range(size)]
        self._size = size

    def __getitem__(self, item: int) -> Any:
        return self._list[item]

    def __setitem__(self, key: int, value: Any) -> None:
        self._list[key] = value
