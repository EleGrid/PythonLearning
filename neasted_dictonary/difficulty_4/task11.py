"""
Задача: Удаление по пути

Глеб удаляет ненужную запись из многоуровневого словаря. Напиши функцию,
которая удаляет значение по указанному пути (списку ключей).

Пример:
    >>> data = {"a": {"b": {"c": 1, "d": 2}}}
    >>> delete_by_path(data, ["a", "b", "c"])
    {'a': {'b': {'d': 2}}}
"""


def delete_by_path(data: dict, path: list) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestDeleteByPath(unittest.TestCase):
    def test_delete_nested(self):
        data = {"a": {"b": {"c": 1, "d": 2}}}
        result = delete_by_path(data, ["a", "b", "c"])
        self.assertNotIn("c", result["a"]["b"])
        self.assertIn("d", result["a"]["b"])

    def test_delete_top_level(self):
        data = {"x": 1, "y": 2}
        result = delete_by_path(data, ["x"])
        self.assertEqual(result, {"y": 2})

    def test_path_not_exists(self):
        data = {"a": {"b": 1}}
        result = delete_by_path(data, ["a", "c"])
        self.assertEqual(result, {"a": {"b": 1}})

    def test_empty_path(self):
        data = {"a": 1}
        result = delete_by_path(data, [])
        self.assertEqual(result, {"a": 1})


if __name__ == "__main__":
    unittest.main()
