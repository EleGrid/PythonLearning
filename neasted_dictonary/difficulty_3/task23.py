"""
Задача: Копирование структуры

Алиса создаёт шаблон расписания. Напиши функцию, которая копирует структуру
вложенного словаря, заменяя все значения на None.

Пример:
    >>> schedule = {"monday": {"math": "9:00", "english": "11:00"}}
    >>> copy_structure(schedule)
    {'monday': {'math': None, 'english': None}}
"""


def copy_structure(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCopyStructure(unittest.TestCase):
    def test_standard(self):
        schedule = {"monday": {"math": "9:00", "english": "11:00"}}
        result = copy_structure(schedule)
        self.assertEqual(result["monday"]["math"], None)
        self.assertEqual(result["monday"]["english"], None)

    def test_preserves_keys(self):
        data = {"a": {"x": 1, "y": 2}}
        result = copy_structure(data)
        self.assertEqual(set(result["a"].keys()), {"x", "y"})

    def test_empty(self):
        self.assertEqual(copy_structure({}), {})

    def test_multiple_categories(self):
        data = {"a": {"x": 1}, "b": {"y": 2}}
        result = copy_structure(data)
        self.assertIsNone(result["a"]["x"])
        self.assertIsNone(result["b"]["y"])


if __name__ == "__main__":
    unittest.main()
