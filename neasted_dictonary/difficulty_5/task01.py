"""
Задача: Глубокое копирование с трансформацией

Мама хочет создать копию бюджета, увеличив все расходы на определённый процент.
Напиши функцию, которая принимает многоуровневый словарь с числовыми значениями
и множитель, возвращает новый словарь с изменёнными значениями.

Структура словаря сохраняется, все числовые значения умножаются на множитель.

Пример:
    >>> budget = {
    ...     "food": {"groceries": 1000, "restaurants": 500},
    ...     "transport": {"gas": 800, "parking": 200}
    ... }
    >>> transform_values(budget, 1.1)
    {'food': {'groceries': 1100.0, 'restaurants': 550.0}, 'transport': {'gas': 880.0, 'parking': 220.0}}
"""


def transform_values(data, multiplier):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestTransformValues(unittest.TestCase):
    def test_increase_by_10_percent(self):
        budget = {"food": {"groceries": 1000, "restaurants": 500}}
        result = transform_values(budget, 1.1)
        self.assertAlmostEqual(result["food"]["groceries"], 1100.0)
        self.assertAlmostEqual(result["food"]["restaurants"], 550.0)

    def test_decrease_by_half(self):
        data = {"a": {"b": 100}}
        result = transform_values(data, 0.5)
        self.assertEqual(result["a"]["b"], 50.0)

    def test_three_levels(self):
        data = {"a": {"b": {"c": 10}}}
        result = transform_values(data, 2)
        self.assertEqual(result["a"]["b"]["c"], 20.0)

    def test_preserves_structure(self):
        data = {"x": {"y": 5, "z": 10}, "w": {"v": 15}}
        result = transform_values(data, 2)
        self.assertEqual(set(result.keys()), {"x", "w"})
        self.assertEqual(set(result["x"].keys()), {"y", "z"})


if __name__ == "__main__":
    unittest.main()
