"""
Задача: Оценка по предмету

Глеб хочет узнать свою оценку по математике. Напиши функцию, которая
принимает словарь ученика с вложенным словарём оценок и название предмета,
возвращает оценку.

Пример:
    >>> student = {"name": "Gleb", "grades": {"math": 5, "english": 4}}
    >>> get_grade(student, "math")
    5
"""


def get_grade(student, subject):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetGrade(unittest.TestCase):
    def test_math(self):
        student = {"name": "Gleb", "grades": {"math": 5, "english": 4}}
        self.assertEqual(get_grade(student, "math"), 5)

    def test_english(self):
        student = {"name": "Gleb", "grades": {"math": 5, "english": 4}}
        self.assertEqual(get_grade(student, "english"), 4)

    def test_single_subject(self):
        student = {"name": "Alisa", "grades": {"reading": 5}}
        self.assertEqual(get_grade(student, "reading"), 5)

    def test_many_subjects(self):
        student = {"name": "Gleb", "grades": {"math": 5, "english": 4, "pe": 5, "arts": 4}}
        self.assertEqual(get_grade(student, "pe"), 5)


if __name__ == "__main__":
    unittest.main()
