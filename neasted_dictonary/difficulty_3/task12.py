"""
Задача: Фильтрация по значению

Глеб ищет все продукты дороже определённой суммы. Напиши функцию, которая
принимает словарь с ценами и минимальную цену, возвращает словарь только
с товарами дороже указанной суммы.

Пример:
    >>> prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
    >>> filter_by_price(prices, 50)
    {'dairy': {'milk': 80, 'cheese': 250}}
"""


def filter_by_price(data: dict, min_price: int) -> dict:
    min_price_dict = {}
    for category in data.keys():
        for product in data[category]:
            if data[category][product] < min_price:
                continue
            if category not in min_price_dict:
                min_price_dict[category] = {}
            min_price_dict[category][product] = data[category][product]
    return min_price_dict




# === Тесты ===
import unittest


class TestFilterByPrice(unittest.TestCase):
    def test_filter_standard(self):
        prices = {"dairy": {"milk": 80, "cheese": 250}, "bakery": {"bread": 45}}
        result = filter_by_price(prices, 50)
        self.assertIn("dairy", result)
        self.assertNotIn("bakery", result)

    def test_filter_all(self):
        prices = {"a": {"x": 10}, "b": {"y": 20}}
        result = filter_by_price(prices, 100)
        self.assertEqual(result, {})

    def test_filter_none(self):
        prices = {"a": {"x": 100}, "b": {"y": 200}}
        result = filter_by_price(prices, 50)
        self.assertEqual(len(result), 2)

    def test_empty_input(self):
        self.assertEqual(filter_by_price({}, 50), {})


if __name__ == "__main__":
    unittest.main()
