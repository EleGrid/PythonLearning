"""
Задача: Инвертирование многоуровневого словаря

Майя хочет найти путь к каждому значению. Напиши функцию, которая
инвертирует вложенный словарь: значения становятся ключами, а путь — значением.

Пример:
    >>> data = {"a": {"b": "target"}}
    >>> invert_nested(data)
    {'target': 'a.b'}
"""


def invert_nested(data: dict, prefix: str = "") -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestInvertNested(unittest.TestCase):
    def test_simple(self):
        data = {"a": {"b": "target"}}
        result = invert_nested(data)
        self.assertEqual(result["target"], "a.b")

    def test_multiple_values(self):
        data = {"a": {"x": "val1"}, "b": {"y": "val2"}}
        result = invert_nested(data)
        self.assertEqual(result["val1"], "a.x")
        self.assertEqual(result["val2"], "b.y")

    def test_deep(self):
        data = {"a": {"b": {"c": "deep"}}}
        result = invert_nested(data)
        self.assertEqual(result["deep"], "a.b.c")

    def test_empty(self):
        self.assertEqual(invert_nested({}), {})


if __name__ == "__main__":
    unittest.main()
