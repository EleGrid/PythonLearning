"""
Задача: Средняя оценка ученика

Глеб хочет узнать свою среднюю оценку. Напиши функцию, которая принимает
словарь с оценками по предметам и возвращает среднюю оценку.

Пример:
    >>> grades = {"Gleb": {"math": 5, "english": 4, "science": 5}}
    >>> average_grade(grades, "Gleb")
    4.67
"""


def average_grade(data: dict, student: str) -> float:
    if student not in data:
        return 0.0
    number_len = 0
    number_sum = 0
    for subject in data[student]:
        number_sum = number_sum + data[student][subject]
        number_len = number_len + 1
    total = number_sum/number_len
    return total





# === Тесты ===
import unittest


class TestAverageGrade(unittest.TestCase):
    def test_standard(self):
        grades = {"Gleb": {"math": 5, "english": 4, "science": 5}}
        self.assertAlmostEqual(average_grade(grades, "Gleb"), 4.67, places=2)

    def test_single_subject(self):
        grades = {"Alisa": {"art": 5}}
        self.assertEqual(average_grade(grades, "Alisa"), 5.0)

    def test_all_same(self):
        grades = {"Maya": {"a": 4, "b": 4, "c": 4}}
        self.assertEqual(average_grade(grades, "Maya"), 4.0)

    def test_missing_student(self):
        grades = {"Gleb": {"math": 5}}
        self.assertEqual(average_grade(grades, "Unknown"), 0)


if __name__ == "__main__":
    unittest.main()
