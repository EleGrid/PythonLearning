"""
Задача: Топ-N значений

Майя хочет найти топ самых дорогих покупок. Напиши функцию, которая
возвращает N самых больших значений из многоуровневого словаря с их путями.

Пример:
    >>> data = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
    >>> top_n_values(data, 2)
    [('toys.car', 500), ('food.cheese', 250)]
"""


def top_n_values(data: dict, n: int) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestTopNValues(unittest.TestCase):
    def test_top_2(self):
        data = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
        result = top_n_values(data, 2)
        self.assertEqual(result[0], ("toys.car", 500))
        self.assertEqual(result[1], ("food.cheese", 250))

    def test_top_1(self):
        data = {"a": {"x": 100, "y": 50}}
        result = top_n_values(data, 1)
        self.assertEqual(result, [("a.x", 100)])

    def test_n_greater_than_count(self):
        data = {"a": {"x": 1}}
        result = top_n_values(data, 10)
        self.assertEqual(len(result), 1)

    def test_empty(self):
        self.assertEqual(top_n_values({}, 5), [])


if __name__ == "__main__":
    unittest.main()
