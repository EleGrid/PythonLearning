"""
Задача: Подсчёт всех ключей

Алиса считает все уникальные ключи в многоуровневом словаре. Напиши функцию,
которая рекурсивно собирает все ключи на всех уровнях.

Пример:
    >>> data = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
    >>> count_all_keys(data)
    5
"""


def count_all_keys(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCountAllKeys(unittest.TestCase):
    def test_nested(self):
        data = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
        self.assertEqual(count_all_keys(data), 5)

    def test_flat(self):
        data = {"x": 1, "y": 2, "z": 3}
        self.assertEqual(count_all_keys(data), 3)

    def test_deep(self):
        data = {"a": {"b": {"c": {"d": 1}}}}
        self.assertEqual(count_all_keys(data), 4)

    def test_empty(self):
        self.assertEqual(count_all_keys({}), 0)


if __name__ == "__main__":
    unittest.main()
