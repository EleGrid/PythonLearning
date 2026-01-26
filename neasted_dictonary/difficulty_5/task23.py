"""
Задача: Сравнение с допуском

Глеб сравнивает два бюджета с допустимой погрешностью. Напиши функцию,
которая проверяет, отличаются ли все соответствующие значения не более
чем на заданный процент.

Пример:
    >>> budget1 = {"food": {"milk": 100}}
    >>> budget2 = {"food": {"milk": 105}}
    >>> compare_with_tolerance(budget1, budget2, 10)
    True
    >>> compare_with_tolerance(budget1, budget2, 1)
    False
"""


def compare_with_tolerance(dict1: dict, dict2: dict, tolerance_percent: float) -> bool:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCompareWithTolerance(unittest.TestCase):
    def test_within_tolerance(self):
        budget1 = {"food": {"milk": 100}}
        budget2 = {"food": {"milk": 105}}
        self.assertTrue(compare_with_tolerance(budget1, budget2, 10))

    def test_outside_tolerance(self):
        budget1 = {"food": {"milk": 100}}
        budget2 = {"food": {"milk": 120}}
        self.assertFalse(compare_with_tolerance(budget1, budget2, 10))

    def test_exact_match(self):
        budget1 = {"a": {"b": 50}}
        budget2 = {"a": {"b": 50}}
        self.assertTrue(compare_with_tolerance(budget1, budget2, 0))

    def test_different_structure(self):
        budget1 = {"a": {"b": 100}}
        budget2 = {"a": {"c": 100}}
        self.assertFalse(compare_with_tolerance(budget1, budget2, 10))


if __name__ == "__main__":
    unittest.main()
