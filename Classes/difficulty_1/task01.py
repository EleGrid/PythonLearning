import unittest

"""
Задача: Создание класса Ребенок

В большой семье у каждого ребенка есть имя и возраст. 
Вам нужно создать класс `Child`, который при инициализации принимает имя (`name`) и возраст (`age`).
Также у класса должен быть метод `get_info`, который возвращает строку формата: "Name: [Имя], Age: [Возраст]".

Например, для Глеба (11 лет) метод должен вернуть "Name: Gleb, Age: 11".

Пример:
    >>> child = Child("Gleb", 11)
    >>> child.get_info()
    'Name: Gleb, Age: 11'
"""

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"



class TestChild(unittest.TestCase):
    def test_gleb(self):
        gleb = Child("Gleb", 11)
        self.assertEqual(gleb.name, "Gleb")
        self.assertEqual(gleb.age, 11)
        self.assertEqual(gleb.get_info(), "Name: Gleb, Age: 11")

    def test_alisa(self):
        alisa = Child("Alisa", 6)
        self.assertEqual(alisa.name, "Alisa")
        self.assertEqual(alisa.age, 6)
        self.assertEqual(alisa.get_info(), "Name: Alisa, Age: 6")

    def test_maya(self):
        maya = Child("Maya", 4)
        self.assertEqual(maya.name, "Maya")
        self.assertEqual(maya.age, 4)
        self.assertEqual(maya.get_info(), "Name: Maya, Age: 4")

if __name__ == "__main__":
    unittest.main()
