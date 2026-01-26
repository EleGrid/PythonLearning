"""
Задача: Преобразование плоского в вложенный

Майя хочет создать структурированные данные из плоского словаря.
Напиши функцию, которая преобразует плоский словарь с точечными ключами
во вложенный.

Пример:
    >>> flat = {"user.name": "Gleb", "user.age": 11}
    >>> unflatten_dict(flat)
    {'user': {'name': 'Gleb', 'age': 11}}
"""


def unflatten_dict(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestUnflattenDict(unittest.TestCase):
    def test_standard(self):
        flat = {"user.name": "Gleb", "user.age": 11}
        result = unflatten_dict(flat)
        self.assertEqual(result["user"]["name"], "Gleb")
        self.assertEqual(result["user"]["age"], 11)

    def test_deep(self):
        flat = {"a.b.c": 100}
        result = unflatten_dict(flat)
        self.assertEqual(result["a"]["b"]["c"], 100)

    def test_no_dots(self):
        flat = {"simple": 1}
        result = unflatten_dict(flat)
        self.assertEqual(result, {"simple": 1})

    def test_empty(self):
        self.assertEqual(unflatten_dict({}), {})


if __name__ == "__main__":
    unittest.main()
