"""
Задача: Имя ребёнка

У мамы есть словарь с информацией о детях. Напиши функцию, которая
принимает словарь ребёнка и возвращает его имя.

Пример:
    >>> child = {"name": "Gleb", "age": 11}
    >>> get_child_name(child)
    'Gleb'
"""


def get_child_name(child):
    return child['name']


# === Тесты ===
import unittest


class TestGetChildName(unittest.TestCase):
    def test_gleb(self):
        self.assertEqual(get_child_name({"name": "Gleb", "age": 11}), "Gleb")

    def test_alisa(self):
        self.assertEqual(get_child_name({"name": "Alisa", "age": 6}), "Alisa")

    def test_maya(self):
        self.assertEqual(get_child_name({"name": "Maya", "age": 4}), "Maya")

    def test_with_extra_fields(self):
        self.assertEqual(get_child_name({"name": "Gleb", "age": 11, "grade": 5}), "Gleb")


if __name__ == "__main__":
    unittest.main()
