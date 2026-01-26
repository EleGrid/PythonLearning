"""
Задача: Рекурсивное суммирование

Алиса считает общую стоимость всех покупок во вложенном бюджете.
Напиши функцию, которая рекурсивно суммирует все числовые значения.

Пример:
    >>> budget = {"food": {"dairy": {"milk": 80}, "bread": 50}, "transport": 100}
    >>> sum_recursive(budget)
    230
"""


def sum_recursive(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSumRecursive(unittest.TestCase):
    def test_nested(self):
        budget = {"food": {"dairy": {"milk": 80}, "bread": 50}, "transport": 100}
        self.assertEqual(sum_recursive(budget), 230)

    def test_flat(self):
        data = {"a": 10, "b": 20, "c": 30}
        self.assertEqual(sum_recursive(data), 60)

    def test_deep(self):
        data = {"a": {"b": {"c": {"d": 100}}}}
        self.assertEqual(sum_recursive(data), 100)

    def test_empty(self):
        self.assertEqual(sum_recursive({}), 0)


if __name__ == "__main__":
    unittest.main()
