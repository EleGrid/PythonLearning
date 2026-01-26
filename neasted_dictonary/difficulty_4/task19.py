"""
Задача: Клонирование с модификацией

Глеб создаёт копию данных с изменённым значением. Напиши функцию, которая
клонирует словарь, изменяя значение по указанному пути.

Пример:
    >>> data = {"user": {"name": "Gleb", "scores": {"math": 4}}}
    >>> clone_with_change(data, ["user", "scores", "math"], 5)
    {'user': {'name': 'Gleb', 'scores': {'math': 5}}}
"""


def clone_with_change(data: dict, path: list, new_value) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCloneWithChange(unittest.TestCase):
    def test_change_nested(self):
        data = {"user": {"name": "Gleb", "scores": {"math": 4}}}
        result = clone_with_change(data, ["user", "scores", "math"], 5)
        self.assertEqual(result["user"]["scores"]["math"], 5)
        self.assertEqual(data["user"]["scores"]["math"], 4)  # Original unchanged

    def test_change_top_level(self):
        data = {"name": "Alisa"}
        result = clone_with_change(data, ["name"], "Maya")
        self.assertEqual(result["name"], "Maya")

    def test_preserves_other(self):
        data = {"a": {"x": 1, "y": 2}}
        result = clone_with_change(data, ["a", "x"], 100)
        self.assertEqual(result["a"]["y"], 2)

    def test_empty_path(self):
        data = {"a": 1}
        result = clone_with_change(data, [], "new")
        self.assertEqual(result, "new")


if __name__ == "__main__":
    unittest.main()
