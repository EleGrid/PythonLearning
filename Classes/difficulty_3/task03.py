import unittest

"""
Задача: Проверка рецепта (Dict lookup)

Есть класс `Recipe` с ингредиентами (`ingredients` - словарь {продукт: количество}).
Метод `can_cook(fridge_items)` принимает словарь продуктов в холодильнике.
Он должен вернуть True, только если ВСЕ ингредиенты есть в холодильнике в нужном количестве (или больше).
Исправьте логику метода.

Пример:
    >>> r = Recipe({"Eggs": 2, "Milk": 1})
    >>> fridge = {"Eggs": 10, "Milk": 5}
    >>> r.can_cook(fridge)
    True
    >>> empty_fridge = {}
    >>> r.can_cook(empty_fridge)
    False
"""

class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients # Dict: {"Egg": 2, "Salt": 1}

    def can_cook(self, fridge_items):
        # Currently the logic is flawed or missing
        # Implement the check: for each item in self.ingredients, 
        # check if it exists in fridge_items and amount is >= needed
        pass


class TestRecipe(unittest.TestCase):
    def test_can_cook(self):
        r = Recipe({"Flour": 500, "Sugar": 200})
        fridge = {"Flour": 1000, "Sugar": 500, "Eggs": 3}
        self.assertTrue(r.can_cook(fridge))

    def test_missing_ingredient(self):
        r = Recipe({"Flour": 500, "Eggs": 2})
        fridge = {"Flour": 1000}
        self.assertFalse(r.can_cook(fridge))

    def test_not_enough(self):
        r = Recipe({"Milk": 2})
        fridge = {"Milk": 1}
        self.assertFalse(r.can_cook(fridge))

if __name__ == "__main__":
    unittest.main()
