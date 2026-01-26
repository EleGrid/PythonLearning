"""
Задача: Разница словарей

Мама сравнивает бюджеты двух месяцев. Напиши функцию, которая находит
все ключи, которые есть в первом словаре, но нет во втором (рекурсивно).

Пример:
    >>> dict1 = {"food": {"milk": 80, "cheese": 250}}
    >>> dict2 = {"food": {"milk": 80}}
    >>> find_difference(dict1, dict2)
    ['food.cheese']
"""


def find_difference(dict1: dict, dict2: dict, prefix: str = "") -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindDifference(unittest.TestCase):
    def test_missing_key(self):
        dict1 = {"food": {"milk": 80, "cheese": 250}}
        dict2 = {"food": {"milk": 80}}
        result = find_difference(dict1, dict2)
        self.assertIn("food.cheese", result)

    def test_missing_category(self):
        dict1 = {"food": {"milk": 80}, "toys": {"car": 100}}
        dict2 = {"food": {"milk": 80}}
        result = find_difference(dict1, dict2)
        self.assertIn("toys", result)

    def test_no_difference(self):
        dict1 = {"a": {"b": 1}}
        dict2 = {"a": {"b": 2}}
        result = find_difference(dict1, dict2)
        self.assertEqual(result, [])

    def test_empty_second(self):
        dict1 = {"a": 1}
        result = find_difference(dict1, {})
        self.assertIn("a", result)


if __name__ == "__main__":
    unittest.main()
