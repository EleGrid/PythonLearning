"""
Задача: Рекурсивный подсчёт глубины

Мама хочет узнать глубину вложенности данных. Напиши функцию, которая
принимает многоуровневый словарь и возвращает максимальную глубину вложенности.

Пример:
    >>> data = {"a": {"b": {"c": 1}}}
    >>> get_depth(data)
    3
    >>> get_depth({"x": 1})
    1
"""


def get_depth(data: dict) -> int:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetDepth(unittest.TestCase):
    def test_three_levels(self):
        data = {"a": {"b": {"c": 1}}}
        self.assertEqual(get_depth(data), 3)

    def test_one_level(self):
        data = {"x": 1, "y": 2}
        self.assertEqual(get_depth(data), 1)

    def test_two_levels(self):
        data = {"a": {"b": 1}}
        self.assertEqual(get_depth(data), 2)

    def test_empty(self):
        self.assertEqual(get_depth({}), 0)


if __name__ == "__main__":
    unittest.main()
