"""
Задача: Создание индекса

Алиса создаёт индекс для быстрого поиска. Напиши функцию, которая принимает
многоуровневый словарь и создаёт индекс всех значений с их путями.

Пример:
    >>> data = {"users": {"admin": "John", "guest": "Jane"}}
    >>> build_index(data)
    {'John': ['users', 'admin'], 'Jane': ['users', 'guest']}
"""


def build_index(data: dict, path: list = None) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestBuildIndex(unittest.TestCase):
    def test_standard(self):
        data = {"users": {"admin": "John", "guest": "Jane"}}
        result = build_index(data)
        self.assertEqual(result["John"], ["users", "admin"])
        self.assertEqual(result["Jane"], ["users", "guest"])

    def test_deep(self):
        data = {"a": {"b": {"c": "value"}}}
        result = build_index(data)
        self.assertEqual(result["value"], ["a", "b", "c"])

    def test_numbers(self):
        data = {"prices": {"milk": 80}}
        result = build_index(data)
        self.assertEqual(result[80], ["prices", "milk"])

    def test_empty(self):
        self.assertEqual(build_index({}), {})


if __name__ == "__main__":
    unittest.main()
