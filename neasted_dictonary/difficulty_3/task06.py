"""
Задача: Суммарные расходы

Мама ведёт учёт расходов по категориям. Напиши функцию, которая принимает
словарь с вложенными тратами и возвращает общую сумму всех расходов.

Пример:
    >>> expenses = {"food": {"bread": 50, "milk": 80}, "transport": {"bus": 30}}
    >>> total_expenses(expenses)
    160
"""


def total_expenses(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestTotalExpenses(unittest.TestCase):
    def test_standard(self):
        expenses = {"food": {"bread": 50, "milk": 80}, "transport": {"bus": 30}}
        self.assertEqual(total_expenses(expenses), 160)

    def test_single_category(self):
        expenses = {"toys": {"lego": 500, "doll": 300}}
        self.assertEqual(total_expenses(expenses), 800)

    def test_empty(self):
        self.assertEqual(total_expenses({}), 0)

    def test_nested_empty(self):
        expenses = {"food": {}, "clothes": {}}
        self.assertEqual(total_expenses(expenses), 0)


if __name__ == "__main__":
    unittest.main()
