"""
Задача: Подсчёт категорий

Майя считает, сколько категорий непустые. Напиши функцию, которая принимает
словарь и возвращает количество непустых вложенных словарей.

Пример:
    >>> data = {"fruits": {"apple": 1}, "dairy": {}, "bakery": {"bread": 2}}
    >>> count_non_empty(data)
    2
"""


def count_non_empty(data: dict) -> int:
    count = 0
    for category in data:
        if len(data[category]) > 0:
            count = count + 1
    return count



# === Тесты ===
import unittest


class TestCountNonEmpty(unittest.TestCase):
    def test_standard(self):
        data = {"fruits": {"apple": 1}, "dairy": {}, "bakery": {"bread": 2}}
        self.assertEqual(count_non_empty(data), 2)

    def test_all_empty(self):
        data = {"a": {}, "b": {}, "c": {}}
        self.assertEqual(count_non_empty(data), 0)

    def test_all_non_empty(self):
        data = {"a": {"x": 1}, "b": {"y": 2}}
        self.assertEqual(count_non_empty(data), 2)

    def test_empty_input(self):
        self.assertEqual(count_non_empty({}), 0)


if __name__ == "__main__":
    unittest.main()
