"""
Задача: Список ключей

Мама составила словарь покупок. Напиши функцию, которая принимает
словарь и возвращает список всех ключей.

Пример:
    >>> shopping = {"milk": 2, "bread": 1}
    >>> get_all_keys(shopping)
    ['milk', 'bread']
"""


def get_all_keys(data):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetAllKeys(unittest.TestCase):
    def test_shopping(self):
        result = get_all_keys({"milk": 2, "bread": 1})
        self.assertEqual(sorted(result), ["bread", "milk"])

    def test_single_key(self):
        result = get_all_keys({"eggs": 12})
        self.assertEqual(result, ["eggs"])

    def test_empty_dict(self):
        result = get_all_keys({})
        self.assertEqual(result, [])

    def test_many_keys(self):
        data = {"a": 1, "b": 2, "c": 3}
        result = get_all_keys(data)
        self.assertEqual(sorted(result), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
