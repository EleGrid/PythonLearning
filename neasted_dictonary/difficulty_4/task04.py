"""
Задача: Сплющивание многоуровневого словаря

Для отчёта маме нужно преобразовать вложенный словарь расходов в плоский
формат. Напиши функцию, которая принимает многоуровневый словарь и
возвращает плоский словарь с ключами через точку.

Пример:
    >>> expenses = {
    ...     "food": {"groceries": 5000, "restaurants": 2000},
    ...     "transport": {"gas": 3000}
    ... }
    >>> flatten_dict(expenses)
    {'food.groceries': 5000, 'food.restaurants': 2000, 'transport.gas': 3000}
"""


def flatten_dict(data, prefix=""):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFlattenDict(unittest.TestCase):
    def test_two_levels(self):
        expenses = {"food": {"groceries": 5000, "restaurants": 2000}, "transport": {"gas": 3000}}
        result = flatten_dict(expenses)
        self.assertEqual(result["food.groceries"], 5000)
        self.assertEqual(result["food.restaurants"], 2000)
        self.assertEqual(result["transport.gas"], 3000)

    def test_single_level(self):
        data = {"a": 1, "b": 2}
        result = flatten_dict(data)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_three_levels(self):
        data = {"a": {"b": {"c": 1}}}
        result = flatten_dict(data)
        self.assertEqual(result, {"a.b.c": 1})

    def test_empty(self):
        result = flatten_dict({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
