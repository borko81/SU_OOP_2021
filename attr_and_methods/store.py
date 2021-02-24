from typing import Dict
from collections import defaultdict
import unittest


class Store:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict = defaultdict(int)

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return Store(name, type, size // 2)

    def add_item(self, item_name: str):
        if self.capacity > len(self.items):
            self.items[item_name] += 1
            return f"{item_name} added to the store"
        return "Not enough capacity in the store"

    def remove_item(self, item_name, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# Unittest


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store('TownStore', 'Show', 5)

    def test_correct_set_up(self):
        self.assertEqual(self.store.name, 'TownStore')
        self.assertEqual(self.store.type, 'Show')
        self.assertEqual(self.store.capacity, 5)
        self.assertEqual(self.store.items, {})

    def test_new_store_from_capacity(self):
        result = Store.from_size('One', "Two", 2)
        self.assertEqual(result.type, 'Two')
        self.assertEqual(result.capacity, 1)
        self.assertEqual(result.items, {})

    def test_add_item_valid(self):
        self.assertEqual(self.store.add_item('tommato'), "tommato added to the store")
        self.assertEqual(self.store.items['tommato'], 1)

    def test_add_item_invalid(self):
        result = Store('TEST', 'SHOP', 0)
        self.assertEqual(result.add_item('potatoes'), "Not enough capacity in the store")

    def test_repr(self):
        self.assertEqual(repr(self.store), f"{self.store.name} of type {self.store.type} with capacity {self.store.capacity}")

    def test_remove_items(self):
        self.store.add_item('tommato')
        self.assertEqual(self.store.remove_item('tommato', 2), "Cannot remove 2 tommato")
        self.assertEqual(self.store.remove_item('tommato', 1), "1 tommato removed from the store")
        self.assertEqual(self.store.items['tommato'], 0)


if __name__ == "__main__":
    unittest.main()
