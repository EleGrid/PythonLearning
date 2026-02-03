import unittest

"""
Задача: Семейный бюджет (Aggregation)

Создайте класс `FamilyBudget`.
У него есть список расходов `expenses` (список словарей `{"category": "Food", "amount": 100}`).
Метод `add_expense(category, amount)` добавляет расход.
Метод `get_total_by_category(category)` должен вернуть сумму всех расходов в заданной категории.

Пример:
    >>> b = FamilyBudget()
    >>> b.add_expense("Food", 100)
    >>> b.add_expense("Transport", 50)
    >>> b.add_expense("Food", 200)
    >>> b.get_total_by_category("Food")
    300
"""

class FamilyBudget:
    def __init__(self):
        self.expenses = []

    # Your code here
    pass


class TestFamilyBudget(unittest.TestCase):
    def test_single_category(self):
        b = FamilyBudget()
        b.add_expense("Food", 100)
        b.add_expense("Food", 50)
        self.assertEqual(b.get_total_by_category("Food"), 150)

    def test_multiple_categories(self):
        b = FamilyBudget()
        b.add_expense("A", 10)
        b.add_expense("B", 20)
        self.assertEqual(b.get_total_by_category("A"), 10)

    def test_empty_category(self):
        b = FamilyBudget()
        b.add_expense("A", 10)
        self.assertEqual(b.get_total_by_category("Z"), 0)

if __name__ == "__main__":
    unittest.main()
