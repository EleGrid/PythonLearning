"""
Задача: Фильтрация по поддереву

Алиса хочет извлечь часть данных по условию на поддерево. Напиши функцию,
которая возвращает только те ветки словаря, где сумма всех значений
превышает порог.

Пример:
    >>> data = {"food": {"milk": 80, "cheese": 250}, "transport": {"bus": 30}}
    >>> filter_by_subtree_sum(data, 100)
    {'food': {'milk': 80, 'cheese': 250}}
"""


def filter_by_subtree_sum(data: dict, threshold: int) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFilterBySubtreeSum(unittest.TestCase):
    def test_filter_by_sum(self):
        data = {"food": {"milk": 80, "cheese": 250}, "transport": {"bus": 30}}
        result = filter_by_subtree_sum(data, 100)
        self.assertIn("food", result)
        self.assertNotIn("transport", result)

    def test_all_pass(self):
        data = {"a": {"x": 100}, "b": {"y": 200}}
        result = filter_by_subtree_sum(data, 50)
        self.assertEqual(len(result), 2)

    def test_none_pass(self):
        data = {"a": {"x": 10}, "b": {"y": 20}}
        result = filter_by_subtree_sum(data, 100)
        self.assertEqual(result, {})

    def test_empty(self):
        self.assertEqual(filter_by_subtree_sum({}, 0), {})


if __name__ == "__main__":
    unittest.main()
