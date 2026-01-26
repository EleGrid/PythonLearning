"""
Задача: Все пути в словаре

Глеб хочет получить все возможные пути к значениям. Напиши функцию,
которая возвращает список всех путей (в виде списков ключей) к конечным значениям.

Пример:
    >>> data = {"a": {"b": 1, "c": 2}}
    >>> get_all_paths(data)
    [['a', 'b'], ['a', 'c']]
"""


def get_all_paths(data: dict, prefix: list = None) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetAllPaths(unittest.TestCase):
    def test_two_paths(self):
        data = {"a": {"b": 1, "c": 2}}
        result = get_all_paths(data)
        self.assertEqual(len(result), 2)
        self.assertIn(["a", "b"], result)
        self.assertIn(["a", "c"], result)

    def test_deep_path(self):
        data = {"a": {"b": {"c": 1}}}
        result = get_all_paths(data)
        self.assertEqual(result, [["a", "b", "c"]])

    def test_multiple_categories(self):
        data = {"a": {"x": 1}, "b": {"y": 2}}
        result = get_all_paths(data)
        self.assertEqual(len(result), 2)

    def test_empty(self):
        self.assertEqual(get_all_paths({}), [])


if __name__ == "__main__":
    unittest.main()
