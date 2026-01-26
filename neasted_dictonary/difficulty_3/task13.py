"""
Задача: Извлечение значений

Алиса собирает все цены из прайс-листа. Напиши функцию, которая принимает
словарь с вложенными категориями и возвращает список всех значений.

Пример:
    >>> prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
    >>> get_all_values(prices)
    [80, 250, 45]
"""


def get_all_values(data: dict) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetAllValues(unittest.TestCase):
    def test_standard(self):
        prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
        result = get_all_values(prices)
        self.assertEqual(sorted(result), [45, 80, 250])

    def test_single_value(self):
        prices = {"a": {"b": 100}}
        self.assertEqual(get_all_values(prices), [100])

    def test_empty(self):
        self.assertEqual(get_all_values({}), [])

    def test_empty_inner(self):
        prices = {"a": {}, "b": {}}
        self.assertEqual(get_all_values(prices), [])


if __name__ == "__main__":
    unittest.main()
