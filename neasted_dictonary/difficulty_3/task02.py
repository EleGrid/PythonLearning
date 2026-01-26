"""
Задача: Средняя оценка

Глеб хочет узнать свою среднюю оценку по всем предметам. Напиши функцию,
которая принимает словарь ученика с вложенным словарём оценок и возвращает
среднее арифметическое всех оценок.

Пример:
    >>> student = {"name": "Gleb", "grades": {"math": 5, "english": 4, "pe": 5}}
    >>> get_average_grade(student)
    4.67
"""


def get_average_grade(student):
    marks = 0
    grades = student['grades']
    if len(grades) == 0:
        return 0
    for key in grades:
       marks = marks + grades[key]
    ave = marks/ len(grades)
    return ave





# === Тесты ===
import unittest


class TestGetAverageGrade(unittest.TestCase):
    def test_three_subjects(self):
        student = {"name": "Gleb", "grades": {"math": 5, "english": 4, "pe": 5}}
        self.assertAlmostEqual(get_average_grade(student), 4.67, places=2)

    def test_two_subjects(self):
        student = {"name": "Alisa", "grades": {"math": 5, "reading": 5}}
        self.assertEqual(get_average_grade(student), 5.0)

    def test_single_subject(self):
        student = {"name": "Maya", "grades": {"arts": 4}}
        self.assertEqual(get_average_grade(student), 4.0)

    def test_many_subjects(self):
        student = {"name": "Gleb", "grades": {"a": 3, "b": 4, "c": 5, "d": 4}}
        self.assertEqual(get_average_grade(student), 4.0)

    def test_zero_subjects(self):
        student = {"name": "Gleb", "grades": {}}
        self.assertEqual(get_average_grade(student), 0)


if __name__ == "__main__":
    unittest.main()
