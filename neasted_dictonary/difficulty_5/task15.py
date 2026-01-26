"""
Задача: Вычисление процентного распределения

Алиса анализирует бюджет и хочет увидеть процентное распределение.
Напиши функцию, которая преобразует значения в проценты от общей суммы
на каждом уровне.

Пример:
    >>> budget = {"food": {"milk": 100, "bread": 100}, "transport": {"bus": 200}}
    >>> calculate_percentages(budget)
    {'food': {'milk': 25.0, 'bread': 25.0}, 'transport': {'bus': 50.0}}
"""


def calculate_percentages(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCalculatePercentages(unittest.TestCase):
    def test_standard(self):
        budget = {"food": {"milk": 100, "bread": 100}, "transport": {"bus": 200}}
        result = calculate_percentages(budget)
        self.assertAlmostEqual(result["food"]["milk"], 25.0)
        self.assertAlmostEqual(result["transport"]["bus"], 50.0)

    def test_single_category(self):
        budget = {"food": {"milk": 100}}
        result = calculate_percentages(budget)
        self.assertEqual(result["food"]["milk"], 100.0)

    def test_equal_values(self):
        budget = {"a": {"x": 50}, "b": {"y": 50}}
        result = calculate_percentages(budget)
        self.assertEqual(result["a"]["x"], 50.0)
        self.assertEqual(result["b"]["y"], 50.0)

    def test_empty(self):
        self.assertEqual(calculate_percentages({}), {})


if __name__ == "__main__":
    unittest.main()
