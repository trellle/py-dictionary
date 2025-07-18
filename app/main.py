from decimal import Decimal
from typing import Any


max_cap = 8
cap = round(max_cap * 2 / 3)

class Dictionary:
    def __init(self) -> None:
        self.__hash_table = [Node() for _ in range(0, max_cap)]

    def extend_hash_table_capacity(self) -> None:
        for _ in range(0, len(self.__hash_table)):
            self.__hash_table.append(Node())

    def __setitem__(self, key: Any, value: Any) -> None:
        self.is_mutable(key)
        self.extend_size()
        index = self.get_index(key)
        while self.__hash_table[index] != Node():
            index = (index + 1) % len(self.__hash_table)
        self.__hash_table[index].hash = hash(key)
        self.__hash_table[index].key = key
        self.__hash_table[index].value = value

    def __getitem__(self, key) -> Any:
        self.is_mutable(key)
        index = self.get_index(key)
        if self.__hash_table[index] == Node():
            raise KeyError
        if self.__hash_table[index].hash == hash(key) and self.__hash_table[index].key == key:
            return self.__hash_table[index].value

    def __len__(self) -> int:
        return len(self.__hash_table) - self.__hash_table.count(Node())

    def is_mutable(self, key) -> None:
        if isinstance(key, (dict, list, set)):
            raise KeyError

    def get_index(self, key: Any) -> int:
        return hash(key) % len(self.__hash_table)

    def extend_size(self) -> None:
        if self.__hash_table.count(Node()) <= max_cap - cap:
            self.extend_hash_table_capacity()

class Node:
    def __init__(self) -> None:
        self.key = None
        self.hash = None
        self.value = None
