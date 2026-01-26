"""
Задача: Получение значения по пути

Майя получает данные по динамическому пути. Напиши функцию, которая
безопасно извлекает значение из многоуровневого словаря по списку ключей.

Пример:
    >>> data = {"a": {"b": {"c": "treasure"}}}
    >>> get_by_path(data, ["a", "b", "c"])
    'treasure'
    >>> get_by_path(data, ["a", "x"])
    None
"""


def get_by_path(data: dict, path: list):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetByPath(unittest.TestCase):
    def test_found(self):
        data = {"a": {"b": {"c": "treasure"}}}
        self.assertEqual(get_by_path(data, ["a", "b", "c"]), "treasure")

    def test_not_found(self):
        data = {"a": {"b": 1}}
        self.assertIsNone(get_by_path(data, ["a", "x"]))

    def test_empty_path(self):
        data = {"a": 1}
        self.assertEqual(get_by_path(data, []), data)

    def test_single_key(self):
        data = {"x": 42}
        self.assertEqual(get_by_path(data, ["x"]), 42)


if __name__ == "__main__":
    unittest.main()
