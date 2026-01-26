"""
Задача: Группировка по нескольким уровням

Майя группирует расходы сначала по месяцу, потом по категории. Напиши
функцию, которая принимает список словарей и группирует их по указанным полям.

Пример:
    >>> expenses = [
    ...     {"month": "jan", "category": "food", "amount": 100},
    ...     {"month": "jan", "category": "food", "amount": 50},
    ...     {"month": "jan", "category": "transport", "amount": 30}
    ... ]
    >>> group_by_fields(expenses, ["month", "category"])
    {'jan': {'food': [100, 50], 'transport': [30]}}
"""


def group_by_fields(items: list, fields: list) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGroupByFields(unittest.TestCase):
    def test_two_levels(self):
        expenses = [
            {"month": "jan", "category": "food", "amount": 100},
            {"month": "jan", "category": "food", "amount": 50},
            {"month": "jan", "category": "transport", "amount": 30}
        ]
        result = group_by_fields(expenses, ["month", "category"])
        self.assertEqual(result["jan"]["food"], [100, 50])
        self.assertEqual(result["jan"]["transport"], [30])

    def test_single_field(self):
        items = [{"type": "a", "val": 1}, {"type": "b", "val": 2}]
        result = group_by_fields(items, ["type"])
        self.assertEqual(result["a"], [1])
        self.assertEqual(result["b"], [2])

    def test_multiple_months(self):
        expenses = [
            {"month": "jan", "category": "food", "amount": 100},
            {"month": "feb", "category": "food", "amount": 200}
        ]
        result = group_by_fields(expenses, ["month", "category"])
        self.assertIn("jan", result)
        self.assertIn("feb", result)

    def test_empty(self):
        self.assertEqual(group_by_fields([], ["a"]), {})


if __name__ == "__main__":
    unittest.main()
