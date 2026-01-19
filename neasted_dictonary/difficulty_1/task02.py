"""
Задача: Возраст ребёнка

Майя спрашивает, сколько ей лет. Напиши функцию, которая принимает
словарь с данными ребёнка и возвращает его возраст.

Пример:
    >>> child = {"name": "Maya", "age": 4}
    >>> get_child_age(child)
    4
"""


def get_child_age(child):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetChildAge(unittest.TestCase):
    def test_maya(self):
        self.assertEqual(get_child_age({"name": "Maya", "age": 4}), 4)

    def test_alisa(self):
        self.assertEqual(get_child_age({"name": "Alisa", "age": 6}), 6)

    def test_gleb(self):
        self.assertEqual(get_child_age({"name": "Gleb", "age": 11}), 11)

    def test_zero_age(self):
        self.assertEqual(get_child_age({"name": "Baby", "age": 0}), 0)


if __name__ == "__main__":
    unittest.main()
