"""
Задача: Агрегация с группировкой

Алиса анализирует расходы по разным критериям. Напиши функцию, которая
группирует и суммирует значения из списка словарей по нескольким полям.

Пример:
    >>> expenses = [
    ...     {"category": "food", "month": "jan", "amount": 100},
    ...     {"category": "food", "month": "jan", "amount": 50},
    ...     {"category": "transport", "month": "jan", "amount": 30}
    ... ]
    >>> aggregate_sum(expenses, "category")
    {'food': 150, 'transport': 30}
"""


def aggregate_sum(items: list, group_by: str) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestAggregateSum(unittest.TestCase):
    def test_by_category(self):
        expenses = [
            {"category": "food", "month": "jan", "amount": 100},
            {"category": "food", "month": "jan", "amount": 50},
            {"category": "transport", "month": "jan", "amount": 30}
        ]
        result = aggregate_sum(expenses, "category")
        self.assertEqual(result["food"], 150)
        self.assertEqual(result["transport"], 30)

    def test_by_month(self):
        expenses = [
            {"category": "food", "month": "jan", "amount": 100},
            {"category": "food", "month": "feb", "amount": 200}
        ]
        result = aggregate_sum(expenses, "month")
        self.assertEqual(result["jan"], 100)
        self.assertEqual(result["feb"], 200)

    def test_single_item(self):
        expenses = [{"type": "a", "amount": 50}]
        result = aggregate_sum(expenses, "type")
        self.assertEqual(result["a"], 50)

    def test_empty(self):
        self.assertEqual(aggregate_sum([], "any"), {})


if __name__ == "__main__":
    unittest.main()
