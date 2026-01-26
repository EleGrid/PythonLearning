"""
Задача: Поиск дубликатов значений

Глеб проверяет данные на дубликаты. Напиши функцию, которая находит
все значения, которые встречаются более одного раза в многоуровневом словаре.

Пример:
    >>> data = {"a": {"x": 100, "y": 200}, "b": {"z": 100}}
    >>> find_duplicates(data)
    [100]
"""


def find_duplicates(data: dict) -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindDuplicates(unittest.TestCase):
    def test_has_duplicates(self):
        data = {"a": {"x": 100, "y": 200}, "b": {"z": 100}}
        result = find_duplicates(data)
        self.assertEqual(result, [100])

    def test_no_duplicates(self):
        data = {"a": {"x": 1}, "b": {"y": 2}}
        result = find_duplicates(data)
        self.assertEqual(result, [])

    def test_multiple_duplicates(self):
        data = {"a": {"x": 1, "y": 2}, "b": {"z": 1, "w": 2}}
        result = find_duplicates(data)
        self.assertEqual(sorted(result), [1, 2])

    def test_empty(self):
        self.assertEqual(find_duplicates({}), [])


if __name__ == "__main__":
    unittest.main()
