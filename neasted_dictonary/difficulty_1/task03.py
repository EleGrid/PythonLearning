"""
Задача: Любимый цвет

Алиса хочет узнать свой любимый цвет из анкеты. Напиши функцию,
которая принимает словарь с данными и ключ, возвращает значение по ключу.

Пример:
    >>> data = {"name": "Alisa", "favorite_color": "pink"}
    >>> get_value(data, "favorite_color")
    'pink'
"""


def get_value(data, key):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetValue(unittest.TestCase):
    def test_favorite_color(self):
        data = {"name": "Alisa", "favorite_color": "pink"}
        self.assertEqual(get_value(data, "favorite_color"), "pink")

    def test_name(self):
        data = {"name": "Gleb", "hobby": "chess"}
        self.assertEqual(get_value(data, "name"), "Gleb")

    def test_number_value(self):
        data = {"item": "apples", "count": 5}
        self.assertEqual(get_value(data, "count"), 5)

    def test_list_value(self):
        data = {"toys": ["doll", "car"]}
        self.assertEqual(get_value(data, "toys"), ["doll", "car"])


if __name__ == "__main__":
    unittest.main()
