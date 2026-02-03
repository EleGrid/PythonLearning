import unittest

"""
Задача: Исправление ужина

В классе `Dinner` (Ужин) допущена ошибка. При инициализации название блюда (`dish_name`) 
почему-то не сохраняется в атрибут объекта.
Исправьте метод `__init__`, чтобы название блюда корректно сохранялось в `self.dish_name`.

Пример:
    >>> dinner = Dinner("Soup")
    >>> dinner.dish_name
    'Soup'
"""

class Dinner:
    def __init__(self, dish_name):
        self.dish_name = dish_name

class TestDinner(unittest.TestCase):
    def test_soup(self):
        dinner = Dinner("Soup")
        self.assertEqual(dinner.dish_name, "Soup")

    def test_pasta(self):
        dinner = Dinner("Pasta")
        self.assertEqual(dinner.dish_name, "Pasta")

    def test_salad(self):
        dinner = Dinner("Salad")
        self.assertEqual(dinner.dish_name, "Salad")

if __name__ == "__main__":
    unittest.main()
