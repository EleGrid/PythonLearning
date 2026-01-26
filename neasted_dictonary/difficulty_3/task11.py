"""
Задача: Объединение словарей

Мама составляет общий список покупок из списков разных магазинов. Напиши
функцию, которая принимает два словаря с одинаковой структурой категорий
и объединяет их значения.

Пример:
    >>> shop1 = {"fruits": {"apple": 2}, "dairy": {"milk": 1}}
    >>> shop2 = {"fruits": {"apple": 3}, "dairy": {"cheese": 1}}
    >>> merge_shopping(shop1, shop2)
    {'fruits': {'apple': 5}, 'dairy': {'milk': 1, 'cheese': 1}}
"""


def merge_shopping(dict1: dict, dict2: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestMergeShopping(unittest.TestCase):
    def test_merge_same_keys(self):
        shop1 = {"fruits": {"apple": 2}}
        shop2 = {"fruits": {"apple": 3}}
        result = merge_shopping(shop1, shop2)
        self.assertEqual(result["fruits"]["apple"], 5)

    def test_merge_different_keys(self):
        shop1 = {"dairy": {"milk": 1}}
        shop2 = {"dairy": {"cheese": 1}}
        result = merge_shopping(shop1, shop2)
        self.assertEqual(result["dairy"], {"milk": 1, "cheese": 1})

    def test_empty_first(self):
        shop2 = {"fruits": {"apple": 3}}
        result = merge_shopping({}, shop2)
        self.assertEqual(result, {"fruits": {"apple": 3}})

    def test_empty_second(self):
        shop1 = {"fruits": {"apple": 2}}
        result = merge_shopping(shop1, {})
        self.assertEqual(result, {"fruits": {"apple": 2}})


if __name__ == "__main__":
    unittest.main()
