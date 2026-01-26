"""
Задача: Условное глубокое обновление

Алиса обновляет цены только для определённых категорий. Напиши функцию,
которая рекурсивно обновляет значения, проходящие условие, с помощью
переданной функции.

Пример:
    >>> budget = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
    >>> update_where(budget, lambda x: x > 100, lambda x: int(x * 0.9))
    {'food': {'milk': 80, 'cheese': 225}, 'toys': {'car': 450}}
"""


def update_where(data: dict, condition, transform) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestUpdateWhere(unittest.TestCase):
    def test_discount_expensive(self):
        budget = {"food": {"milk": 80, "cheese": 250}, "toys": {"car": 500}}
        result = update_where(budget, lambda x: x > 100, lambda x: int(x * 0.9))
        self.assertEqual(result["food"]["milk"], 80)
        self.assertEqual(result["food"]["cheese"], 225)
        self.assertEqual(result["toys"]["car"], 450)

    def test_no_match(self):
        data = {"a": {"x": 10, "y": 20}}
        result = update_where(data, lambda x: x > 100, lambda x: 0)
        self.assertEqual(result["a"]["x"], 10)
        self.assertEqual(result["a"]["y"], 20)

    def test_all_match(self):
        data = {"a": {"x": 100, "y": 200}}
        result = update_where(data, lambda x: x > 50, lambda x: x * 2)
        self.assertEqual(result["a"]["x"], 200)
        self.assertEqual(result["a"]["y"], 400)

    def test_empty(self):
        self.assertEqual(update_where({}, lambda x: True, lambda x: x), {})


if __name__ == "__main__":
    unittest.main()
