"""
Задача: Разворачивание плоского словаря

Мама получила данные в плоском формате и хочет восстановить структуру.
Напиши функцию, которая принимает плоский словарь с ключами через точку
и возвращает многоуровневый словарь.

Пример:
    >>> flat = {'food.groceries': 5000, 'food.restaurants': 2000, 'transport.gas': 3000}
    >>> unflatten_dict(flat)
    {'food': {'groceries': 5000, 'restaurants': 2000}, 'transport': {'gas': 3000}}
"""


def unflatten_dict(flat_dict):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestUnflattenDict(unittest.TestCase):
    def test_two_categories(self):
        flat = {"food.groceries": 5000, "food.restaurants": 2000, "transport.gas": 3000}
        result = unflatten_dict(flat)
        self.assertEqual(result["food"]["groceries"], 5000)
        self.assertEqual(result["food"]["restaurants"], 2000)
        self.assertEqual(result["transport"]["gas"], 3000)

    def test_three_levels(self):
        flat = {"a.b.c": 1, "a.b.d": 2}
        result = unflatten_dict(flat)
        self.assertEqual(result["a"]["b"]["c"], 1)
        self.assertEqual(result["a"]["b"]["d"], 2)

    def test_single_key(self):
        flat = {"simple": 100}
        result = unflatten_dict(flat)
        self.assertEqual(result, {"simple": 100})

    def test_empty(self):
        result = unflatten_dict({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
