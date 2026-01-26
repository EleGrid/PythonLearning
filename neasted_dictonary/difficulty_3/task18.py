"""
Задача: Удаление пустых категорий

Мама чистит список покупок от пустых категорий. Напиши функцию, которая
принимает словарь и удаляет все вложенные словари, которые пусты.

Пример:
    >>> shopping = {"fruits": {"apple": 2}, "dairy": {}, "bakery": {"bread": 1}}
    >>> remove_empty(shopping)
    {'fruits': {'apple': 2}, 'bakery': {'bread': 1}}
"""


def remove_empty(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestRemoveEmpty(unittest.TestCase):
    def test_remove_one_empty(self):
        shopping = {"fruits": {"apple": 2}, "dairy": {}}
        result = remove_empty(shopping)
        self.assertNotIn("dairy", result)
        self.assertIn("fruits", result)

    def test_all_empty(self):
        shopping = {"a": {}, "b": {}, "c": {}}
        self.assertEqual(remove_empty(shopping), {})

    def test_none_empty(self):
        shopping = {"a": {"x": 1}, "b": {"y": 2}}
        result = remove_empty(shopping)
        self.assertEqual(len(result), 2)

    def test_empty_input(self):
        self.assertEqual(remove_empty({}), {})


if __name__ == "__main__":
    unittest.main()
