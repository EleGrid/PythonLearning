"""
Задача: Рекурсивный поиск ключа

Глеб ищет значение по ключу в многоуровневом словаре. Напиши функцию,
которая рекурсивно ищет ключ на любом уровне вложенности.

Пример:
    >>> data = {"level1": {"level2": {"target": "found"}}}
    >>> find_key_recursive(data, "target")
    'found'
    >>> find_key_recursive(data, "missing")
    None
"""


def find_key_recursive(data: dict, key: str):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindKeyRecursive(unittest.TestCase):
    def test_found_deep(self):
        data = {"level1": {"level2": {"target": "found"}}}
        self.assertEqual(find_key_recursive(data, "target"), "found")

    def test_found_top(self):
        data = {"target": "here", "other": {"nested": 1}}
        self.assertEqual(find_key_recursive(data, "target"), "here")

    def test_not_found(self):
        data = {"a": {"b": 1}}
        self.assertIsNone(find_key_recursive(data, "missing"))

    def test_empty(self):
        self.assertIsNone(find_key_recursive({}, "any"))


if __name__ == "__main__":
    unittest.main()
