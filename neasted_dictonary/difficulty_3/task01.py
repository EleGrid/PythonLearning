"""
Задача: Полный адрес

Мама заполняет документы и нужен полный адрес. Напиши функцию, которая
принимает словарь с вложенным адресом и возвращает строку "город, улица".

Пример:
    >>> data = {"name": "Gleb", "address": {"city": "Moscow", "street": "Lenina"}}
    >>> get_full_address(data)
    'Moscow, Lenina'
"""


def get_full_address(data:dict) -> str:
   return data['address']['city'] + ", " + data['address']['street']


# === Тесты ===
import unittest


class TestGetFullAddress(unittest.TestCase):
    def test_standard(self):
        data = {"name": "Gleb", "address": {"city": "Moscow", "street": "Lenina"}}
        self.assertEqual(get_full_address(data), "Moscow, Lenina")

    def test_spb(self):
        data = {"address": {"city": "Saint Petersburg", "street": "Nevsky Prospect"}}
        self.assertEqual(get_full_address(data), "Saint Petersburg, Nevsky Prospect")

    def test_short_names(self):
        data = {"address": {"city": "Ufa", "street": "Main"}}
        self.assertEqual(get_full_address(data), "Ufa, Main")

    def test_with_extra_fields(self):
        data = {"name": "Maya", "address": {"city": "Kazan", "street": "Central", "building": 5}}
        self.assertEqual(get_full_address(data), "Kazan, Central")


if __name__ == "__main__":
    unittest.main()
