import unittest

"""
Задача: Список покупок (Dictionary)

Мама составляет список покупок. Создайте класс `ShoppingList`.
У него должен быть атрибут `items` (словарь, по умолчанию пустой).
Добавьте метод `add_item(name, quantity)`, который добавляет товар в список.
Если товар уже есть, нужно увеличить его количество. Если нет — добавить.

Пример:
    >>> s_list = ShoppingList()
    >>> s_list.add_item("Apples", 5)
    >>> s_list.items
    {'Apples': 5}
    >>> s_list.add_item("Apples", 2)
    >>> s_list.items
    {'Apples': 7}
"""

class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] = self.items[name] + quantity
        else:
            self.items[name] = quantity



class TestShoppingList(unittest.TestCase):
    def test_add_new_item(self):
        sl = ShoppingList()
        sl.add_item("Milk", 1)
        self.assertEqual(sl.items, {"Milk": 1})

    def test_add_existing_item(self):
        sl = ShoppingList()
        sl.add_item("Bread", 1)
        sl.add_item("Bread", 1)
        self.assertEqual(sl.items, {"Bread": 2})

    def test_multiple_items(self):
        sl = ShoppingList()
        sl.add_item("Egss", 10)
        sl.add_item("Cheese", 1)
        self.assertEqual(sl.items, {"Egss": 10, "Cheese": 1})

if __name__ == "__main__":
    unittest.main()
