"""
Задача: Безопасный доступ

Майя просит найти любимую игрушку в списке. Напиши функцию, которая безопасно
получает значение из вложенного словаря. Если ключ не найден, вернуть None.

Пример:
    >>> toys = {"maya": {"favorite": "bunny"}, "alisa": {"favorite": "doll"}}
    >>> safe_get(toys, "maya", "favorite")
    'bunny'
    >>> safe_get(toys, "gleb", "favorite")
    None
"""


def safe_get(data: dict, key1: str, key2: str):
    if key1 in data:
        if key2 in data[key1]:
            return  data[key1][key2]
    else:
        return None



# === Тесты ===
import unittest


class TestSafeGet(unittest.TestCase):
    def test_existing_keys(self):
        toys = {"maya": {"favorite": "bunny"}, "alisa": {"favorite": "doll"}}
        self.assertEqual(safe_get(toys, "maya", "favorite"), "bunny")

    def test_missing_outer_key(self):
        toys = {"maya": {"favorite": "bunny"}}
        self.assertIsNone(safe_get(toys, "gleb", "favorite"))

    def test_missing_inner_key(self):
        toys = {"maya": {"color": "pink"}}
        self.assertIsNone(safe_get(toys, "maya", "favorite"))

    def test_empty_dict(self):
        self.assertIsNone(safe_get({}, "any", "key"))


if __name__ == "__main__":
    unittest.main()
