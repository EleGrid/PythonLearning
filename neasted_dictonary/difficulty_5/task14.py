"""
Задача: Сжатие путей

Глеб хочет оптимизировать хранение данных. Напиши функцию, которая
сжимает пустые промежуточные уровни в многоуровневом словаре.

Пример:
    >>> data = {"a": {"b": {"c": 1}}}
    >>> compress_paths(data)
    {'a.b.c': 1}
"""


def compress_paths(data: dict, prefix: str = "") -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCompressPaths(unittest.TestCase):
    def test_single_path(self):
        data = {"a": {"b": {"c": 1}}}
        result = compress_paths(data)
        self.assertEqual(result, {"a.b.c": 1})

    def test_multiple_leaves(self):
        data = {"a": {"x": 1, "y": 2}}
        result = compress_paths(data)
        self.assertEqual(result["a.x"], 1)
        self.assertEqual(result["a.y"], 2)

    def test_mixed_depth(self):
        data = {"a": 1, "b": {"c": 2}}
        result = compress_paths(data)
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b.c"], 2)

    def test_empty(self):
        self.assertEqual(compress_paths({}), {})


if __name__ == "__main__":
    unittest.main()
