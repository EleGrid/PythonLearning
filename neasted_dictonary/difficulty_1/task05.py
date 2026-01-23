"""
Задача: Проверка ключа

Глеб проверяет, есть ли в списке дел определённое задание. Напиши функцию,
которая принимает словарь и ключ, возвращает True если ключ есть, иначе False.

Пример:
    >>> tasks = {"homework": True, "piano": False}
    >>> has_key(tasks, "homework")
    True
    >>> has_key(tasks, "swimming")
    False
"""


def has_key(data, key):
    if key in data:
        return True
    else:
        return False




# === Тесты ===
import unittest


class TestHasKey(unittest.TestCase):
    def test_key_exists(self):
        self.assertTrue(has_key({"homework": True}, "homework"))

    def test_key_not_exists(self):
        self.assertFalse(has_key({"homework": True}, "swimming"))

    def test_empty_dict(self):
        self.assertFalse(has_key({}, "any_key"))

    def test_key_with_none_value(self):
        self.assertTrue(has_key({"task": None}, "task"))


if __name__ == "__main__":
    unittest.main()
