"""
Задача: Безопасное получение значения

Алиса ищет свой любимый цвет в анкете, но он может быть не заполнен.
Напиши функцию, которая принимает словарь, список ключей для навигации
и значение по умолчанию. Возвращает значение по пути или значение по умолчанию.

Пример:
    >>> data = {"child": {"name": "Alisa", "preferences": {"color": "pink"}}}
    >>> safe_get(data, ["child", "preferences", "color"], "unknown")
    'pink'
    >>> safe_get(data, ["child", "preferences", "food"], "unknown")
    'unknown'
"""


def safe_get(data, keys, default):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSafeGet(unittest.TestCase):
    def test_found(self):
        data = {"child": {"name": "Alisa", "preferences": {"color": "pink"}}}
        self.assertEqual(safe_get(data, ["child", "preferences", "color"], "unknown"), "pink")

    def test_not_found(self):
        data = {"child": {"name": "Alisa"}}
        self.assertEqual(safe_get(data, ["child", "preferences", "food"], "unknown"), "unknown")

    def test_single_key(self):
        data = {"name": "Gleb"}
        self.assertEqual(safe_get(data, ["name"], "none"), "Gleb")

    def test_empty_path(self):
        data = {"name": "Maya"}
        self.assertEqual(safe_get(data, [], data), data)

    def test_middle_key_missing(self):
        data = {"a": {"b": 1}}
        self.assertEqual(safe_get(data, ["a", "c", "d"], "default"), "default")


if __name__ == "__main__":
    unittest.main()
