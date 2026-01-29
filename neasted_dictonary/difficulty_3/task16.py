"""
Задача: Группировка по возрасту

Мама составляет список друзей детей по возрастным группам. Напиши функцию,
которая принимает словарь детей с их данными и возвращает словарь,
сгруппированный по возрасту.

Пример:
    >>> kids = {"Gleb": {"age": 11}, "Alisa": {"age": 6}, "Petya": {"age": 11}}
    >>> group_by_age(kids)
    {11: ['Gleb', 'Petya'], 6: ['Alisa']}
"""


def group_by_age(data: dict) -> dict:
    age_dict = {}
    for name_key in data:
        group_age = data[name_key]['age']
        if group_age not in age_dict:
            age_dict[group_age] = []
        our_list = age_dict[group_age]
        our_list.append(name_key)
    return age_dict



# === Тесты ===
import unittest


class TestGroupByAge(unittest.TestCase):
    def test_standard(self):
        kids = {"Gleb": {"age": 11}, "Alisa": {"age": 6}, "Petya": {"age": 11}}
        result = group_by_age(kids)
        self.assertEqual(sorted(result[11]), ["Gleb", "Petya"])
        self.assertEqual(result[6], ["Alisa"])

    def test_single_age(self):
        kids = {"Maya": {"age": 4}, "Lena": {"age": 4}}
        result = group_by_age(kids)
        self.assertEqual(len(result[4]), 2)

    def test_empty(self):
        self.assertEqual(group_by_age({}), {})

    def test_one_child(self):
        kids = {"Gleb": {"age": 11}}
        result = group_by_age(kids)
        self.assertEqual(result, {11: ["Gleb"]})


if __name__ == "__main__":
    unittest.main()
