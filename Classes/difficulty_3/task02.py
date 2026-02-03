import unittest

"""
Задача: Хобби детей (List unique items)

У каждого ребенка из класса `Child` есть список хобби (`hobbies`, по умолчанию пустой список).
Добавьте метод `add_hobby(hobby_name)`.
Хобби должно добавляться в список только если его там еще нет.
Если добавили, возвращает True. Если хобби уже было — False.

Пример:
    >>> gleb = Child("Gleb", 11)
    >>> gleb.add_hobby("Football")
    True
    >>> gleb.hobbies
    ['Football']
    >>> gleb.add_hobby("Football")
    False
"""

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []

    # Your code here
    pass


class TestChildHobbies(unittest.TestCase):
    def test_add_hobby(self):
        c = Child("Alisa", 6)
        result = c.add_hobby("Dancing")
        self.assertTrue(result)
        self.assertEqual(c.hobbies, ["Dancing"])

    def test_duplicate_hobby(self):
        c = Child("Maya", 4)
        c.add_hobby("Drawing")
        result = c.add_hobby("Drawing")
        self.assertFalse(result)
        self.assertEqual(len(c.hobbies), 1)

    def test_multiple_hobbies(self):
        c = Child("Gleb", 11)
        c.add_hobby("Math")
        c.add_hobby("Coding")
        self.assertEqual(c.hobbies, ["Math", "Coding"])

if __name__ == "__main__":
    unittest.main()
