"""
Задача: Агрегация данных по критерию

Мама анализирует расходы семьи за месяц. Напиши функцию, которая принимает
многоуровневый словарь расходов по дням и категориям, возвращает словарь
с суммами расходов по каждой категории.

Пример:
    >>> expenses = {
    ...     "2024-01-01": {"food": 500, "transport": 200},
    ...     "2024-01-02": {"food": 300, "entertainment": 1000},
    ...     "2024-01-03": {"food": 400, "transport": 150}
    ... }
    >>> aggregate_by_category(expenses)
    {'food': 1200, 'transport': 350, 'entertainment': 1000}
"""


def aggregate_by_category(expenses):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestAggregateByCategory(unittest.TestCase):
    def test_three_days(self):
        expenses = {
            "2024-01-01": {"food": 500, "transport": 200},
            "2024-01-02": {"food": 300, "entertainment": 1000},
            "2024-01-03": {"food": 400, "transport": 150}
        }
        result = aggregate_by_category(expenses)
        self.assertEqual(result["food"], 1200)
        self.assertEqual(result["transport"], 350)
        self.assertEqual(result["entertainment"], 1000)

    def test_single_day(self):
        expenses = {"day1": {"groceries": 100, "gas": 50}}
        result = aggregate_by_category(expenses)
        self.assertEqual(result, {"groceries": 100, "gas": 50})

    def test_same_category_all_days(self):
        expenses = {"d1": {"food": 100}, "d2": {"food": 200}, "d3": {"food": 300}}
        result = aggregate_by_category(expenses)
        self.assertEqual(result, {"food": 600})

    def test_empty(self):
        result = aggregate_by_category({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
