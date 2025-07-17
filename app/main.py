from decimal import Decimal
from typing import Any


max_cap = 8
cap = round(max_cap * 2 / 3)

class Dictionary:
    def __init(self) -> None:
        self.__hash_table = [{} for _ in range(0, max_cap)]

    def extend_hash_table_capacity(self) -> None:
        for _ in range(0, len(self.__hash_table)):
            self.__hash_table.append({})

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, (dict, list, set)):
            raise KeyError
        if self.__hash_table.count({}) <= max_cap - cap:
            self.extend_hash_table_capacity()
        index = hash(key) % len(self.__hash_table)
        while self.__hash_table[index] != {}:
            index = (index + 1) % len(self.__hash_table)
        self.__hash_table[index]["hash"] = hash(key)
        self.__hash_table[index]["key"] = key
        self.__hash_table[index]["value"] = value

    def __getitem__(self, key) -> Any:
        if isinstance(key, (dict, list, set)):
            raise KeyError
        for element in self.__hash_table:
            if element["hash"] == hash(key) and element["key"] == key:
                return element["value"]
