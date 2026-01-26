"""
Задача: Глубокое сравнение словарей

Мама сравнивает два бюджета и хочет найти все различия. Напиши функцию,
которая рекурсивно сравнивает два многоуровневых словаря и возвращает
словарь с различающимися значениями.

Пример:
    >>> dict1 = {"food": {"milk": 80, "bread": 50}}
    >>> dict2 = {"food": {"milk": 90, "bread": 50}}
    >>> deep_diff(dict1, dict2)
    {'food.milk': {'old': 80, 'new': 90}}
"""


def deep_diff(dict1: dict, dict2: dict, prefix: str = "") -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestDeepDiff(unittest.TestCase):
    def test_value_changed(self):
        dict1 = {"food": {"milk": 80, "bread": 50}}
        dict2 = {"food": {"milk": 90, "bread": 50}}
        result = deep_diff(dict1, dict2)
        self.assertEqual(result["food.milk"]["old"], 80)
        self.assertEqual(result["food.milk"]["new"], 90)

    def test_no_diff(self):
        dict1 = {"a": {"b": 1}}
        dict2 = {"a": {"b": 1}}
        self.assertEqual(deep_diff(dict1, dict2), {})

    def test_added_key(self):
        dict1 = {"a": {"b": 1}}
        dict2 = {"a": {"b": 1, "c": 2}}
        result = deep_diff(dict1, dict2)
        self.assertIn("a.c", result)

    def test_removed_key(self):
        dict1 = {"a": {"b": 1, "c": 2}}
        dict2 = {"a": {"b": 1}}
        result = deep_diff(dict1, dict2)
        self.assertIn("a.c", result)


if __name__ == "__main__":
    unittest.main()
