"""
Задача: Общее количество продуктов

Мама составила список покупок по категориям. Напиши функцию, которая
принимает словарь покупок с вложенными категориями и считает общее
количество всех продуктов.

Пример:
    >>> shopping = {
    ...     "dairy": {"milk": 2, "cheese": 1},
    ...     "bakery": {"bread": 1}
    ... }
    >>> count_total_items(shopping)
    4
"""


def count_total_items(shopping):
      total = 0
      for category in shopping.values():
          for product_value in category.values():
              total = total + product_value
      return  total


# === Тесты ===
import unittest


class TestCountTotalItems(unittest.TestCase):
    def test_two_categories(self):
        shopping = {"dairy": {"milk": 2, "cheese": 1}, "bakery": {"bread": 1}}
        self.assertEqual(count_total_items(shopping), 4)

    def test_single_category(self):
        shopping = {"fruits": {"apples": 5, "bananas": 3}}
        self.assertEqual(count_total_items(shopping), 8)

    def test_empty(self):
        shopping = {}
        self.assertEqual(count_total_items(shopping), 0)

    def test_many_categories(self):
        shopping = {"a": {"x": 1}, "b": {"y": 2}, "c": {"z": 3}}
        self.assertEqual(count_total_items(shopping), 6)


if __name__ == "__main__":
    unittest.main()
