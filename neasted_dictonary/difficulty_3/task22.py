"""
Задача: Сортировка по значению

Глеб хочет отсортировать продукты по цене. Напиши функцию, которая принимает
словарь с ценами и возвращает список товаров, отсортированных по цене.

Пример:
    >>> prices = {"dairy": {"milk": 80, "cheese": 250, "yogurt": 45}}
    >>> sort_by_price(prices, "dairy")
    ['yogurt', 'milk', 'cheese']
"""


def sort_by_price(data: dict, category: str) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSortByPrice(unittest.TestCase):
    def test_standard(self):
        prices = {"dairy": {"milk": 80, "cheese": 250, "yogurt": 45}}
        result = sort_by_price(prices, "dairy")
        self.assertEqual(result, ["yogurt", "milk", "cheese"])

    def test_single_item(self):
        prices = {"fruits": {"apple": 100}}
        result = sort_by_price(prices, "fruits")
        self.assertEqual(result, ["apple"])

    def test_missing_category(self):
        prices = {"dairy": {"milk": 80}}
        result = sort_by_price(prices, "fruits")
        self.assertEqual(result, [])

    def test_same_prices(self):
        prices = {"a": {"x": 50, "y": 50}}
        result = sort_by_price(prices, "a")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
