"""
Задача: Максимальное значение

Алиса считает, какой продукт самый дорогой. Напиши функцию, которая принимает
словарь с ценами продуктов по категориям и возвращает максимальную цену.

Пример:
    >>> prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
    >>> find_max_value(prices)
    250
"""


def find_max_value(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindMaxValue(unittest.TestCase):
    def test_standard(self):
        prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
        self.assertEqual(find_max_value(prices), 250)

    def test_single_item(self):
        prices = {"food": {"apple": 100}}
        self.assertEqual(find_max_value(prices), 100)

    def test_same_values(self):
        prices = {"a": {"x": 50}, "b": {"y": 50}}
        self.assertEqual(find_max_value(prices), 50)

    def test_negative_values(self):
        prices = {"a": {"x": -10, "y": -5}}
        self.assertEqual(find_max_value(prices), -5)


if __name__ == "__main__":
    unittest.main()
