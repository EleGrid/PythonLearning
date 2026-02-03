import unittest

"""
Задача: Домашний питомец

Дети очень хотят домашнее животное. Создайте класс `Pet` (Питомец).
Конструктор должен принимать вид животного (`species`) и его имя (`name`).
Оба значения должны сохраняться в соответствующие атрибуты.

Пример:
    >>> my_pet = Pet("Cat", "Murzik")
    >>> my_pet.species
    'Cat'
    >>> my_pet.name
    'Murzik'
"""

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name



class TestPet(unittest.TestCase):
    def test_dog(self):
        dog = Pet("Dog", "Rex")
        self.assertEqual(dog.species, "Dog")
        self.assertEqual(dog.name, "Rex")

    def test_cat(self):
        cat = Pet("Cat", "Barsik")
        self.assertEqual(cat.species, "Cat")
        self.assertEqual(cat.name, "Barsik")

    def test_hamster(self):
        hamster = Pet("Hamster", "Khoma")
        self.assertEqual(hamster.species, "Hamster")
        self.assertEqual(hamster.name, "Khoma")

if __name__ == "__main__":
    unittest.main()
