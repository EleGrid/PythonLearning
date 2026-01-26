"""
Задача: Нормализация значений

Глеб хочет нормализовать все значения в диапазон 0-1. Напиши функцию,
которая рекурсивно нормализует все числовые значения относительно
минимального и максимального.

Пример:
    >>> data = {"a": {"x": 0, "y": 100}, "b": {"z": 50}}
    >>> normalize_values(data)
    {'a': {'x': 0.0, 'y': 1.0}, 'b': {'z': 0.5}}
"""


def normalize_values(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestNormalizeValues(unittest.TestCase):
    def test_standard(self):
        data = {"a": {"x": 0, "y": 100}, "b": {"z": 50}}
        result = normalize_values(data)
        self.assertEqual(result["a"]["x"], 0.0)
        self.assertEqual(result["a"]["y"], 1.0)
        self.assertEqual(result["b"]["z"], 0.5)

    def test_all_same(self):
        data = {"a": {"x": 50, "y": 50}}
        result = normalize_values(data)
        self.assertEqual(result["a"]["x"], 0.0)
        self.assertEqual(result["a"]["y"], 0.0)

    def test_negative(self):
        data = {"a": {"x": -100, "y": 100}}
        result = normalize_values(data)
        self.assertEqual(result["a"]["x"], 0.0)
        self.assertEqual(result["a"]["y"], 1.0)

    def test_empty(self):
        self.assertEqual(normalize_values({}), {})


if __name__ == "__main__":
    unittest.main()
