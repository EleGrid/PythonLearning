"""
Задача: Вычисление статистики по вложенному словарю

Мама анализирует расходы и хочет получить статистику. Напиши функцию,
которая рекурсивно вычисляет сумму, минимум, максимум и среднее всех
числовых значений.

Пример:
    >>> budget = {"food": {"milk": 80, "bread": 50}, "transport": 100}
    >>> calculate_stats(budget)
    {'sum': 230, 'min': 50, 'max': 100, 'avg': 76.67}
"""


def calculate_stats(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCalculateStats(unittest.TestCase):
    def test_standard(self):
        budget = {"food": {"milk": 80, "bread": 50}, "transport": 100}
        result = calculate_stats(budget)
        self.assertEqual(result["sum"], 230)
        self.assertEqual(result["min"], 50)
        self.assertEqual(result["max"], 100)
        self.assertAlmostEqual(result["avg"], 76.67, places=2)

    def test_single_value(self):
        data = {"a": {"b": 100}}
        result = calculate_stats(data)
        self.assertEqual(result["sum"], 100)
        self.assertEqual(result["min"], 100)
        self.assertEqual(result["max"], 100)
        self.assertEqual(result["avg"], 100)

    def test_deep(self):
        data = {"a": {"b": {"c": 10, "d": 20}}}
        result = calculate_stats(data)
        self.assertEqual(result["sum"], 30)

    def test_empty(self):
        result = calculate_stats({})
        self.assertEqual(result["sum"], 0)


if __name__ == "__main__":
    unittest.main()
