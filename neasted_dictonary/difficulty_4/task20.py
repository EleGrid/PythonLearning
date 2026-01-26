"""
Задача: Агрегация по категориям

Алиса считает суммы по каждой категории верхнего уровня. Напиши функцию,
которая возвращает словарь с суммами всех числовых значений по категориям.

Пример:
    >>> budget = {"food": {"milk": 80, "bread": 50}, "transport": {"bus": 30, "metro": 40}}
    >>> aggregate_categories(budget)
    {'food': 130, 'transport': 70}
"""


def aggregate_categories(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestAggregateCategories(unittest.TestCase):
    def test_standard(self):
        budget = {"food": {"milk": 80, "bread": 50}, "transport": {"bus": 30, "metro": 40}}
        result = aggregate_categories(budget)
        self.assertEqual(result["food"], 130)
        self.assertEqual(result["transport"], 70)

    def test_nested_deep(self):
        budget = {"a": {"b": {"c": 100}}}
        result = aggregate_categories(budget)
        self.assertEqual(result["a"], 100)

    def test_single_category(self):
        budget = {"toys": {"car": 500}}
        result = aggregate_categories(budget)
        self.assertEqual(result["toys"], 500)

    def test_empty(self):
        self.assertEqual(aggregate_categories({}), {})


if __name__ == "__main__":
    unittest.main()
