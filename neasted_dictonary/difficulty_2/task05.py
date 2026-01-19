"""
Задача: Проверка наличия адреса

Мама проверяет, заполнен ли адрес в анкете ребёнка. Напиши функцию,
которая принимает словарь ребёнка и возвращает True, если есть ключ "address".

Пример:
    >>> child = {"name": "Gleb", "address": {"city": "Moscow"}}
    >>> has_address(child)
    True
    >>> child2 = {"name": "Maya"}
    >>> has_address(child2)
    False
"""


def has_address(child):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestHasAddress(unittest.TestCase):
    def test_has_address(self):
        child = {"name": "Gleb", "address": {"city": "Moscow"}}
        self.assertTrue(has_address(child))

    def test_no_address(self):
        child = {"name": "Maya"}
        self.assertFalse(has_address(child))

    def test_empty_address(self):
        child = {"name": "Alisa", "address": {}}
        self.assertTrue(has_address(child))

    def test_only_name(self):
        child = {"name": "Gleb", "age": 11}
        self.assertFalse(has_address(child))


if __name__ == "__main__":
    unittest.main()
