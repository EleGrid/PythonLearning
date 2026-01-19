"""
Задача: Группировка детей по возрасту

Мама организует праздник и хочет сгруппировать детей по возрасту.
Напиши функцию, которая принимает словарь детей и возвращает новый словарь,
где ключи — возраст, а значения — списки имён детей этого возраста.

Пример:
    >>> children = {
    ...     "Gleb": {"age": 11, "grade": 5},
    ...     "Alisa": {"age": 6, "grade": 1},
    ...     "Maya": {"age": 4},
    ...     "Petya": {"age": 11, "grade": 5}
    ... }
    >>> group_by_age(children)
    {11: ['Gleb', 'Petya'], 6: ['Alisa'], 4: ['Maya']}
"""


def group_by_age(children):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGroupByAge(unittest.TestCase):
    def test_example(self):
        children = {
            "Gleb": {"age": 11, "grade": 5},
            "Alisa": {"age": 6, "grade": 1},
            "Maya": {"age": 4},
            "Petya": {"age": 11, "grade": 5}
        }
        result = group_by_age(children)
        self.assertEqual(sorted(result[11]), ["Gleb", "Petya"])
        self.assertEqual(result[6], ["Alisa"])
        self.assertEqual(result[4], ["Maya"])

    def test_single_child(self):
        children = {"Alisa": {"age": 6}}
        result = group_by_age(children)
        self.assertEqual(result, {6: ["Alisa"]})

    def test_all_same_age(self):
        children = {"A": {"age": 5}, "B": {"age": 5}, "C": {"age": 5}}
        result = group_by_age(children)
        self.assertEqual(sorted(result[5]), ["A", "B", "C"])

    def test_empty(self):
        result = group_by_age({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
