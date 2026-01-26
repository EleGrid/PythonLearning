"""
Задача: Поиск по шаблону

Майя ищет значения по шаблону пути с wildcards. Напиши функцию, которая
находит все значения, соответствующие шаблону пути, где '*' означает
любой ключ.

Пример:
    >>> data = {"users": {"admin": {"role": "admin"}, "guest": {"role": "guest"}}}
    >>> find_by_pattern(data, ["users", "*", "role"])
    ['admin', 'guest']
"""


def find_by_pattern(data: dict, pattern: list) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindByPattern(unittest.TestCase):
    def test_wildcard_middle(self):
        data = {"users": {"admin": {"role": "admin"}, "guest": {"role": "guest"}}}
        result = find_by_pattern(data, ["users", "*", "role"])
        self.assertEqual(sorted(result), ["admin", "guest"])

    def test_no_wildcard(self):
        data = {"a": {"b": {"c": "value"}}}
        result = find_by_pattern(data, ["a", "b", "c"])
        self.assertEqual(result, ["value"])

    def test_wildcard_start(self):
        data = {"x": {"val": 1}, "y": {"val": 2}}
        result = find_by_pattern(data, ["*", "val"])
        self.assertEqual(sorted(result), [1, 2])

    def test_no_match(self):
        data = {"a": {"b": 1}}
        result = find_by_pattern(data, ["x", "y"])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
