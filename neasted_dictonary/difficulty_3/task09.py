"""
Задача: Подсчёт элементов

Мама хочет узнать, сколько всего продуктов в списке покупок. Напиши функцию,
которая принимает словарь с категориями и продуктами и возвращает общее
количество продуктов.

Пример:
    >>> shopping = {"fruits": {"apple": 3, "banana": 2}, "dairy": {"milk": 1}}
    >>> count_items(shopping)
    3
"""


def count_items(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCountItems(unittest.TestCase):
    def test_standard(self):
        shopping = {"fruits": {"apple": 3, "banana": 2}, "dairy": {"milk": 1}}
        self.assertEqual(count_items(shopping), 3)

    def test_single_category(self):
        shopping = {"toys": {"car": 1, "doll": 2}}
        self.assertEqual(count_items(shopping), 2)

    def test_empty(self):
        self.assertEqual(count_items({}), 0)

    def test_empty_categories(self):
        shopping = {"fruits": {}, "dairy": {}}
        self.assertEqual(count_items(shopping), 0)


if __name__ == "__main__":
    unittest.main()
