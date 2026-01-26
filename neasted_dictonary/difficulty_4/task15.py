"""
Задача: Сравнение структур

Глеб проверяет, имеют ли два словаря одинаковую структуру (ключи).
Напиши функцию, которая сравнивает структуры двух многоуровневых словарей.

Пример:
    >>> dict1 = {"a": {"b": 1, "c": 2}}
    >>> dict2 = {"a": {"b": 10, "c": 20}}
    >>> same_structure(dict1, dict2)
    True
"""


def same_structure(dict1: dict, dict2: dict) -> bool:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSameStructure(unittest.TestCase):
    def test_same(self):
        dict1 = {"a": {"b": 1, "c": 2}}
        dict2 = {"a": {"b": 10, "c": 20}}
        self.assertTrue(same_structure(dict1, dict2))

    def test_different_keys(self):
        dict1 = {"a": {"b": 1}}
        dict2 = {"a": {"c": 1}}
        self.assertFalse(same_structure(dict1, dict2))

    def test_different_depth(self):
        dict1 = {"a": {"b": {"c": 1}}}
        dict2 = {"a": {"b": 1}}
        self.assertFalse(same_structure(dict1, dict2))

    def test_both_empty(self):
        self.assertTrue(same_structure({}, {}))


if __name__ == "__main__":
    unittest.main()
