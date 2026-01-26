"""
Задача: Транспонирование структуры

Майя хочет реорганизовать данные по-другому. Напиши функцию, которая
транспонирует структуру: меняет местами уровни вложенности.

Пример:
    >>> data = {"jan": {"food": 100, "transport": 50}, "feb": {"food": 120, "transport": 60}}
    >>> transpose_dict(data)
    {'food': {'jan': 100, 'feb': 120}, 'transport': {'jan': 50, 'feb': 60}}
"""


def transpose_dict(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestTransposeDict(unittest.TestCase):
    def test_standard(self):
        data = {"jan": {"food": 100, "transport": 50}, "feb": {"food": 120, "transport": 60}}
        result = transpose_dict(data)
        self.assertEqual(result["food"]["jan"], 100)
        self.assertEqual(result["food"]["feb"], 120)
        self.assertEqual(result["transport"]["jan"], 50)

    def test_single_outer(self):
        data = {"a": {"x": 1, "y": 2}}
        result = transpose_dict(data)
        self.assertEqual(result["x"]["a"], 1)
        self.assertEqual(result["y"]["a"], 2)

    def test_single_inner(self):
        data = {"a": {"x": 1}, "b": {"x": 2}}
        result = transpose_dict(data)
        self.assertEqual(result["x"], {"a": 1, "b": 2})

    def test_empty(self):
        self.assertEqual(transpose_dict({}), {})


if __name__ == "__main__":
    unittest.main()
