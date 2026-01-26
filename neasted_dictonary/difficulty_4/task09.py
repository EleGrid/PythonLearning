"""
Задача: Путь к значению

Майя хочет найти путь к определённому значению в многоуровневом словаре.
Напиши функцию, которая возвращает список ключей, ведущих к значению.

Пример:
    >>> data = {"a": {"b": {"c": "target"}}}
    >>> path_to_value(data, "target")
    ['a', 'b', 'c']
"""


def path_to_value(data: dict, value) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestPathToValue(unittest.TestCase):
    def test_deep_path(self):
        data = {"a": {"b": {"c": "target"}}}
        self.assertEqual(path_to_value(data, "target"), ["a", "b", "c"])

    def test_top_level(self):
        data = {"x": "target", "y": 2}
        self.assertEqual(path_to_value(data, "target"), ["x"])

    def test_not_found(self):
        data = {"a": {"b": 1}}
        self.assertEqual(path_to_value(data, "missing"), [])

    def test_number_value(self):
        data = {"level": {"deep": 42}}
        self.assertEqual(path_to_value(data, 42), ["level", "deep"])


if __name__ == "__main__":
    unittest.main()
