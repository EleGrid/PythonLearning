"""
Задача: Сумма по категории

Мама считает расходы по конкретной категории. Напиши функцию, которая
принимает словарь расходов и название категории, возвращает сумму.

Пример:
    >>> expenses = {"food": {"bread": 50, "milk": 80}, "transport": {"bus": 30}}
    >>> sum_category(expenses, "food")
    130
"""


def sum_category(data: dict, category: str) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSumCategory(unittest.TestCase):
    def test_standard(self):
        expenses = {"food": {"bread": 50, "milk": 80}, "transport": {"bus": 30}}
        self.assertEqual(sum_category(expenses, "food"), 130)

    def test_missing_category(self):
        expenses = {"food": {"bread": 50}}
        self.assertEqual(sum_category(expenses, "toys"), 0)

    def test_empty_category(self):
        expenses = {"food": {}}
        self.assertEqual(sum_category(expenses, "food"), 0)

    def test_single_item(self):
        expenses = {"transport": {"taxi": 500}}
        self.assertEqual(sum_category(expenses, "transport"), 500)


if __name__ == "__main__":
    unittest.main()
