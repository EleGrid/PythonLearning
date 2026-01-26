"""
Задача: Применение функции к значениям

Майя хочет применить скидку ко всем ценам. Напиши функцию, которая
рекурсивно применяет переданную функцию ко всем числовым значениям.

Пример:
    >>> prices = {"food": {"milk": 100, "cheese": 200}}
    >>> apply_discount = lambda x: x * 0.9
    >>> map_values(prices, apply_discount)
    {'food': {'milk': 90.0, 'cheese': 180.0}}
"""


def map_values(data: dict, func) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestMapValues(unittest.TestCase):
    def test_discount(self):
        prices = {"food": {"milk": 100, "cheese": 200}}
        result = map_values(prices, lambda x: x * 0.9)
        self.assertAlmostEqual(result["food"]["milk"], 90.0)
        self.assertAlmostEqual(result["food"]["cheese"], 180.0)

    def test_double(self):
        data = {"a": {"x": 5}}
        result = map_values(data, lambda x: x * 2)
        self.assertEqual(result["a"]["x"], 10)

    def test_deep(self):
        data = {"a": {"b": {"c": 10}}}
        result = map_values(data, lambda x: x + 1)
        self.assertEqual(result["a"]["b"]["c"], 11)

    def test_empty(self):
        self.assertEqual(map_values({}, lambda x: x), {})


if __name__ == "__main__":
    unittest.main()
