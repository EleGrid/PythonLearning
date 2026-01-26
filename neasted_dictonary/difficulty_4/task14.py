"""
Задача: Фильтрация по условию

Мама отбирает только дорогие покупки из вложенного списка. Напиши функцию,
которая рекурсивно фильтрует все числовые значения по условию.

Пример:
    >>> data = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
    >>> filter_recursive(data, lambda x: x > 100)
    {'food': {'cheese': 250}, 'toys': {'car': 500}}
"""


def filter_recursive(data: dict, condition) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFilterRecursive(unittest.TestCase):
    def test_filter_by_value(self):
        data = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
        result = filter_recursive(data, lambda x: x > 100)
        self.assertNotIn("milk", result.get("food", {}))
        self.assertIn("cheese", result["food"])

    def test_filter_all(self):
        data = {"a": {"x": 10, "y": 20}}
        result = filter_recursive(data, lambda x: x > 100)
        self.assertEqual(result, {})

    def test_filter_none(self):
        data = {"a": {"x": 100, "y": 200}}
        result = filter_recursive(data, lambda x: x > 50)
        self.assertEqual(len(result["a"]), 2)

    def test_empty(self):
        self.assertEqual(filter_recursive({}, lambda x: x > 0), {})


if __name__ == "__main__":
    unittest.main()
