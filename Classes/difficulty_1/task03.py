import unittest

"""
Задача: Добавление приветствия

У нас уже есть заготовка класса `Child` с именем и возрастом.
Добавьте в этот класс метод `say_hello`, который возвращает строку "Hello, my name is [Name]!".

Пример:
    >>> child = Child("Gleb", 11)
    >>> child.say_hello()
    'Hello, my name is Gleb!'
"""

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Your code here
    pass


class TestChildHello(unittest.TestCase):
    def test_gleb_hello(self):
        gleb = Child("Gleb", 11)
        self.assertEqual(gleb.say_hello(), "Hello, my name is Gleb!")

    def test_alisa_hello(self):
        alisa = Child("Alisa", 6)
        self.assertEqual(alisa.say_hello(), "Hello, my name is Alisa!")

    def test_maya_hello(self):
        maya = Child("Maya", 4)
        self.assertEqual(maya.say_hello(), "Hello, my name is Maya!")

if __name__ == "__main__":
    unittest.main()
