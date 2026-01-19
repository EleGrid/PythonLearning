"""
Задача: Найти всех детей определённого возраста

Мама ищет в базе данных детского сада всех детей определённого возраста.
Напиши функцию, которая принимает словарь групп с детьми и возраст,
возвращает список имён всех детей этого возраста.

Пример:
    >>> kindergarten = {
    ...     "group_a": {"Maya": {"age": 4}, "Lena": {"age": 5}},
    ...     "group_b": {"Alisa": {"age": 6}, "Misha": {"age": 4}}
    ... }
    >>> find_children_by_age(kindergarten, 4)
    ['Maya', 'Misha']
"""


def find_children_by_age(kindergarten, age):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindChildrenByAge(unittest.TestCase):
    def test_find_age_4(self):
        kindergarten = {
            "group_a": {"Maya": {"age": 4}, "Lena": {"age": 5}},
            "group_b": {"Alisa": {"age": 6}, "Misha": {"age": 4}}
        }
        result = find_children_by_age(kindergarten, 4)
        self.assertEqual(sorted(result), ["Maya", "Misha"])

    def test_find_age_6(self):
        kindergarten = {
            "group_a": {"Alisa": {"age": 6}},
            "group_b": {"Gleb": {"age": 11}}
        }
        result = find_children_by_age(kindergarten, 6)
        self.assertEqual(result, ["Alisa"])

    def test_no_match(self):
        kindergarten = {"group": {"child": {"age": 5}}}
        result = find_children_by_age(kindergarten, 10)
        self.assertEqual(result, [])

    def test_single_group(self):
        kindergarten = {"group": {"A": {"age": 4}, "B": {"age": 4}, "C": {"age": 5}}}
        result = find_children_by_age(kindergarten, 4)
        self.assertEqual(sorted(result), ["A", "B"])


if __name__ == "__main__":
    unittest.main()
