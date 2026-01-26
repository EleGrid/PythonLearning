"""
Задача: Поиск ключа по значению

Алиса ищет, в какой категории находится товар с определённой ценой.
Напиши функцию, которая принимает словарь и значение, возвращает ключ
внутреннего словаря, где найдено это значение.

Пример:
    >>> prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
    >>> find_by_value(prices, 250)
    'cheese'
"""


def find_by_value(data: dict, value: int) -> str:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindByValue(unittest.TestCase):
    def test_found(self):
        prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
        self.assertEqual(find_by_value(prices, 250), "cheese")

    def test_not_found(self):
        prices = {"a": {"x": 10}}
        self.assertIsNone(find_by_value(prices, 999))

    def test_first_match(self):
        prices = {"a": {"x": 100}, "b": {"y": 100}}
        result = find_by_value(prices, 100)
        self.assertIn(result, ["x", "y"])

    def test_empty(self):
        self.assertIsNone(find_by_value({}, 10))


if __name__ == "__main__":
    unittest.main()
