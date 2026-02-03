"""
Задача: Самая большая категория

Майя ищет категорию с наибольшим количеством товаров. Напиши функцию,
которая принимает словарь и возвращает название самой большой категории.

Пример:
    >>> shopping = {"fruits": {"apple": 1, "banana": 2}, "dairy": {"milk": 1}}
    >>> largest_category(shopping)
    'fruits'
"""


def largest_category(data: dict) -> str:
    max_category = None
    max_count = 0
    for category, products in data.items():
        current_count = len(products)
        if current_count > max_count:
            max_count = current_count
            max_category = category
    return max_category



# === Тесты ===
import unittest


class TestLargestCategory(unittest.TestCase):
    def test_standard(self):
        shopping = {"fruits": {"apple": 1, "banana": 2}, "dairy": {"milk": 1}}
        self.assertEqual(largest_category(shopping), "fruits")

    def test_equal_sizes(self):
        shopping = {"a": {"x": 1}, "b": {"y": 1}}
        result = largest_category(shopping)
        self.assertIn(result, ["a", "b"])

    def test_single_category(self):
        shopping = {"toys": {"car": 1, "doll": 2, "ball": 3}}
        self.assertEqual(largest_category(shopping), "toys")

    def test_empty(self):
        self.assertIsNone(largest_category({}))


if __name__ == "__main__":
    unittest.main()
