import unittest

"""
Задача: Школьный дневник

У Глеба есть дневник. В классе `SchoolDiary` есть метод `grade_homework`, 
который принимает оценку (`score`).
Допишите метод так, чтобы он возвращал "Good job!" если оценка 4 или 5,
и "Try better!" если оценка 3 и ниже.

Пример:
    >>> diary = SchoolDiary()
    >>> diary.grade_homework(5)
    'Good job!'
    >>> diary.grade_homework(2)
    'Try better!'
"""

class SchoolDiary:
    def grade_homework(self, score) -> str:
        if score in [4,5]:
            return "Good job!"
        else:
            return "Try better!"


class TestSchoolDiary(unittest.TestCase):
    def test_excellent(self):
        d = SchoolDiary()
        self.assertEqual(d.grade_homework(5), "Good job!")

    def test_good(self):
        d = SchoolDiary()
        self.assertEqual(d.grade_homework(4), "Good job!")

    def test_satisfactory(self):
        d = SchoolDiary()
        self.assertEqual(d.grade_homework(3), "Try better!")

    def test_bad(self):
        d = SchoolDiary()
        self.assertEqual(d.grade_homework(2), "Try better!")

if __name__ == "__main__":
    unittest.main()
