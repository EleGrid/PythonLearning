"""
Задача: Слияние с приоритетом

Глеб объединяет настройки по умолчанию с пользовательскими настройками.
Напиши функцию, которая глубоко объединяет словари, где второй словарь
имеет приоритет.

Пример:
    >>> defaults = {"ui": {"theme": "light", "font": "Arial"}, "sound": True}
    >>> user = {"ui": {"theme": "dark"}}
    >>> merge_with_priority(defaults, user)
    {'ui': {'theme': 'dark', 'font': 'Arial'}, 'sound': True}
"""


def merge_with_priority(base: dict, override: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestMergeWithPriority(unittest.TestCase):
    def test_override_nested(self):
        defaults = {"ui": {"theme": "light", "font": "Arial"}, "sound": True}
        user = {"ui": {"theme": "dark"}}
        result = merge_with_priority(defaults, user)
        self.assertEqual(result["ui"]["theme"], "dark")
        self.assertEqual(result["ui"]["font"], "Arial")
        self.assertEqual(result["sound"], True)

    def test_no_override(self):
        defaults = {"a": {"b": 1}}
        result = merge_with_priority(defaults, {})
        self.assertEqual(result, {"a": {"b": 1}})

    def test_add_new(self):
        defaults = {"a": 1}
        user = {"b": 2}
        result = merge_with_priority(defaults, user)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_deep_override(self):
        defaults = {"a": {"b": {"c": 1}}}
        user = {"a": {"b": {"c": 2}}}
        result = merge_with_priority(defaults, user)
        self.assertEqual(result["a"]["b"]["c"], 2)


if __name__ == "__main__":
    unittest.main()
