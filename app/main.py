from __future__ import annotations
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

    def __getitem__(self, key: Any) -> Any:
        self.is_mutable(key)
        index = self.get_index(key)
        self.is_node_empty(index)
        if (self.__hash_table[index].hash == hash(key)
                and self.__hash_table[index].key == key):
            return self.__hash_table[index].value

    def __len__(self) -> int:
        return len(self.__hash_table) - self.__hash_table.count(Node())

    def is_mutable(self, key: Any) -> None:
        if isinstance(key, (dict, list, set)):
            raise KeyError

    def get_index(self, key: Any) -> int:
        return hash(key) % len(self.__hash_table)

    def extend_size(self) -> None:
        if self.__hash_table.count(Node()) <= max_cap - cap:
            self.extend_hash_table_capacity()

    def is_node_empty(self, index: int) -> None:
        if self.__hash_table[index] == Node():
            raise KeyError

    def clear(self) -> None:
        for elem in self.__hash_table:
            self.clear_node(elem)

    def clear_node(self, node: Node) -> None:
        node.hash = None
        node.key = None
        node.value = None

    def __delitem__(self, key: Any) -> None:
        self.is_mutable(key)
        index = self.get_index(key)
        self.is_node_empty(index)
        if (self.__hash_table[index].hash == hash(key)
                and self.__hash_table[index].key == key):
            self.clear_node(self.__hash_table[index])

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            value = self.__getitem__(key)
        except KeyError:
            return default
        else:
            return value

    def pop(self, key: Any, default: Any = None) -> Any:
        try:
            self.is_mutable(key)
            index = self.get_index(key)
        except KeyError:
            return default
        else:
            if (self.__hash_table[index].hash == hash(key)
                    and self.__hash_table[index].key == key):
                my_key = self.__hash_table[index].key
            self.clear_node(index)
            return my_key

    def update(self, insert_dict: Dictionary) -> None:
        for elem in insert_dict:
            self.__setitem__(elem.key, elem.value)

    def __iter__(self) -> iter:
        return DictIterator(self)


class Node:
    def __init__(self) -> None:
        self.key = None
        self.hash = None
        self.value = None


class DictIterator:
    def __init__(self) -> None:
        pass
