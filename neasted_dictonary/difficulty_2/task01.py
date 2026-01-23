"""
Задача: Город ребёнка

У каждого ребёнка есть анкета с адресом. Напиши функцию, которая
принимает словарь ребёнка с вложенным словарём адреса и возвращает город.

Пример:
    >>> child = {"name": "Gleb", "address": {"city": "Moscow", "street": "Lenina"}}
    >>> get_city(child)
    'Moscow'
"""


def get_city(child: dict) -> str:
    return child['address']['city']



# === Тесты ===
import unittest


class TestGetCity(unittest.TestCase):
    def test_moscow(self):
        child = {"name": "Gleb", "address": {"city": "Moscow", "street": "Lenina"}}
        self.assertEqual(get_city(child), "Moscow")

    def test_spb(self):
        child = {"name": "Alisa", "address": {"city": "Saint Petersburg", "street": "Nevsky"}}
        self.assertEqual(get_city(child), "Saint Petersburg")

    def test_with_more_fields(self):
        child = {"name": "Maya", "age": 4, "address": {"city": "Kazan", "street": "Main", "building": 10}}
        self.assertEqual(get_city(child), "Kazan")

    def test_simple_address(self):
        child = {"name": "Gleb", "address": {"city": "Sochi"}}
        self.assertEqual(get_city(child), "Sochi")


if __name__ == "__main__":
    unittest.main()
