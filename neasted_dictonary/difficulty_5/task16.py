"""
Задача: Кэширование с вложенными ключами

Майя создаёт систему кэширования. Напиши функцию, которая устанавливает
значение в кэш по составному ключу, создавая промежуточные уровни при
необходимости.

Пример:
    >>> cache = {}
    >>> set_nested(cache, ["user", "profile", "name"], "Gleb")
    >>> cache
    {'user': {'profile': {'name': 'Gleb'}}}
"""


def set_nested(data: dict, path: list, value) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSetNested(unittest.TestCase):
    def test_create_path(self):
        cache = {}
        set_nested(cache, ["user", "profile", "name"], "Gleb")
        self.assertEqual(cache["user"]["profile"]["name"], "Gleb")

    def test_update_existing(self):
        cache = {"user": {"profile": {"name": "old"}}}
        set_nested(cache, ["user", "profile", "name"], "new")
        self.assertEqual(cache["user"]["profile"]["name"], "new")

    def test_add_to_existing(self):
        cache = {"user": {"profile": {"name": "Gleb"}}}
        set_nested(cache, ["user", "profile", "age"], 11)
        self.assertEqual(cache["user"]["profile"]["age"], 11)

    def test_single_key(self):
        cache = {}
        set_nested(cache, ["simple"], "value")
        self.assertEqual(cache["simple"], "value")


if __name__ == "__main__":
    unittest.main()
