"""
Задача: Подсчёт значений определённого типа

Глеб считает, сколько строковых значений в многоуровневом словаре.
Напиши функцию, которая рекурсивно подсчитывает значения заданного типа.

Пример:
    >>> data = {"user": {"name": "Gleb", "age": 11}, "city": "Moscow"}
    >>> count_type(data, str)
    2
"""


def count_type(data: dict, value_type: type) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestCountType(unittest.TestCase):
    def test_count_strings(self):
        data = {"user": {"name": "Gleb", "age": 11}, "city": "Moscow"}
        self.assertEqual(count_type(data, str), 2)

    def test_count_ints(self):
        data = {"a": {"x": 1, "y": 2}, "b": 3}
        self.assertEqual(count_type(data, int), 3)

    def test_no_match(self):
        data = {"a": {"b": "text"}}
        self.assertEqual(count_type(data, int), 0)

    def test_empty(self):
        self.assertEqual(count_type({}, str), 0)


if __name__ == "__main__":
    unittest.main()
