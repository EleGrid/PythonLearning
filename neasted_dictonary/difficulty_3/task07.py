"""
Задача: Список всех ключей

Глеб помогает маме разобраться с вложенными данными. Напиши функцию, которая
принимает словарь с одним уровнем вложенности и возвращает список всех
ключей внутренних словарей.

Пример:
    >>> data = {"fruits": {"apple": 5, "banana": 3}, "vegetables": {"carrot": 2}}
    >>> get_inner_keys(data)
    ['apple', 'banana', 'carrot']
"""


def get_inner_keys(data: dict) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetInnerKeys(unittest.TestCase):
    def test_standard(self):
        data = {"fruits": {"apple": 5, "banana": 3}, "vegetables": {"carrot": 2}}
        result = get_inner_keys(data)
        self.assertEqual(sorted(result), ["apple", "banana", "carrot"])

    def test_single_category(self):
        data = {"toys": {"car": 1, "doll": 2, "ball": 3}}
        result = get_inner_keys(data)
        self.assertEqual(sorted(result), ["ball", "car", "doll"])

    def test_empty(self):
        self.assertEqual(get_inner_keys({}), [])

    def test_empty_inner(self):
        data = {"empty": {}}
        self.assertEqual(get_inner_keys(data), [])


if __name__ == "__main__":
    unittest.main()
