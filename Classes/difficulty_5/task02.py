import unittest

"""
Задача: Сравнение членов семьи (Magic Methods)

Создайте класс `FamilyMember` с именем и возрастом.
Реализуйте магические методы:
1. `__str__` - для красивого вывода "Name (Age)".
2. `__eq__` (==) - люди равны, если равны и имя и возраст.
3. `__lt__` (<) - сравнение по возрасту.

Пример:
    >>> dad = FamilyMember("Dad", 40)
    >>> mom = FamilyMember("Mom", 38)
    >>> print(dad)
    'Dad (40)'
    >>> dad > mom
    True
    >>> dad == FamilyMember("Dad", 40)
    True
"""

class FamilyMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Your code here
    pass


class TestFamilyMember(unittest.TestCase):
    def test_string_repr(self):
        m = FamilyMember("Gleb", 11)
        self.assertEqual(str(m), "Gleb (11)")

    def test_equality(self):
        m1 = FamilyMember("Alisa", 6)
        m2 = FamilyMember("Alisa", 6)
        m3 = FamilyMember("Maya", 4)
        self.assertEqual(m1, m2)
        self.assertNotEqual(m1, m3)

    def test_comparison(self):
        gleb = FamilyMember("Gleb", 11)
        alisa = FamilyMember("Alisa", 6)
        self.assertTrue(alisa < gleb)
        self.assertFalse(gleb < alisa)

if __name__ == "__main__":
    unittest.main()
