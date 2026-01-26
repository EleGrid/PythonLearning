"""
Задача: Проверка наличия ключа

Майя проверяет, есть ли её любимая игрушка в списке. Напиши функцию, которая
проверяет, существует ли указанный ключ во вложенном словаре.

Пример:
    >>> toys = {"maya": {"bunny": 1, "bear": 2}}
    >>> has_item(toys, "maya", "bunny")
    True
    >>> has_item(toys, "maya", "doll")
    False
"""


def has_item(data: dict, outer_key: str, inner_key: str) -> bool:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestHasItem(unittest.TestCase):
    def test_exists(self):
        toys = {"maya": {"bunny": 1, "bear": 2}}
        self.assertTrue(has_item(toys, "maya", "bunny"))

    def test_missing_inner(self):
        toys = {"maya": {"bunny": 1}}
        self.assertFalse(has_item(toys, "maya", "doll"))

    def test_missing_outer(self):
        toys = {"maya": {"bunny": 1}}
        self.assertFalse(has_item(toys, "gleb", "car"))

    def test_empty(self):
        self.assertFalse(has_item({}, "any", "key"))


if __name__ == "__main__":
    unittest.main()
