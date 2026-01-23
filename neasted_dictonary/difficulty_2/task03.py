"""
Задача: Количество комнат

Мама составляет план уборки квартиры. Напиши функцию, которая принимает
словарь квартиры с вложенным словарём комнат и возвращает количество комнат.

Пример:
    >>> apartment = {"address": "Main St", "rooms": {"bedroom": 3, "bathroom": 2, "kitchen": 1}}
    >>> count_rooms(apartment)
    3
"""


def count_rooms(apartment):
    return len(apartment['rooms'])


# === Тесты ===
import unittest


class TestCountRooms(unittest.TestCase):
    def test_three_types(self):
        apartment = {"address": "Main St", "rooms": {"bedroom": 3, "bathroom": 2, "kitchen": 1}}
        self.assertEqual(count_rooms(apartment), 3)

    def test_single_room(self):
        apartment = {"rooms": {"studio": 1}}
        self.assertEqual(count_rooms(apartment), 1)

    def test_many_rooms(self):
        apartment = {"rooms": {"bedroom": 2, "bathroom": 1, "kitchen": 1, "living": 1, "balcony": 2}}
        self.assertEqual(count_rooms(apartment), 5)

    def test_empty_rooms(self):
        apartment = {"rooms": {}}
        self.assertEqual(count_rooms(apartment), 0)


if __name__ == "__main__":
    unittest.main()
