"""
Задача: Слияние вложенных словарей

Мама объединяет бюджеты за несколько месяцев. Напиши функцию, которая
глубоко объединяет два многоуровневых словаря.

Пример:
    >>> dict1 = {"food": {"dairy": 100}}
    >>> dict2 = {"food": {"bakery": 50}, "transport": 80}
    >>> deep_merge(dict1, dict2)
    {'food': {'dairy': 100, 'bakery': 50}, 'transport': 80}
"""


def deep_merge(dict1: dict, dict2: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestDeepMerge(unittest.TestCase):
    def test_merge_nested(self):
        dict1 = {"food": {"dairy": 100}}
        dict2 = {"food": {"bakery": 50}, "transport": 80}
        result = deep_merge(dict1, dict2)
        self.assertEqual(result["food"]["dairy"], 100)
        self.assertEqual(result["food"]["bakery"], 50)
        self.assertEqual(result["transport"], 80)

    def test_no_overlap(self):
        dict1 = {"a": {"x": 1}}
        dict2 = {"b": {"y": 2}}
        result = deep_merge(dict1, dict2)
        self.assertEqual(result, {"a": {"x": 1}, "b": {"y": 2}})

    def test_empty_first(self):
        result = deep_merge({}, {"a": 1})
        self.assertEqual(result, {"a": 1})

    def test_overwrite_value(self):
        dict1 = {"a": {"x": 1}}
        dict2 = {"a": {"x": 2}}
        result = deep_merge(dict1, dict2)
        self.assertEqual(result["a"]["x"], 2)


if __name__ == "__main__":
    unittest.main()
