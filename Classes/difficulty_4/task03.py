import unittest

"""
Задача: Сортировка белья (Logic)

Класс `LaundryBasket` хранит список одежды. Каждая вещь: `{"type": "Shirt", "color": "Red"}`.
Метод `add_clothes(type, color)` добавляет вещь.
Метод `sort_clothes()` должен возвращать словарь с 3 ключами: "White", "Color", "Dark".
- "White": если цвет "White".
- "Dark": если цвет "Black" или "Blue".
- "Color": все остальные цвета.
Значения словаря - списки типов одежды.

Пример:
    >>> l = LaundryBasket()
    >>> l.add_clothes("Shirt", "White")
    >>> l.add_clothes("Jeans", "Blue")
    >>> l.add_clothes("Dress", "Red")
    >>> l.sort_clothes()
    {'White': ['Shirt'], 'Dark': ['Jeans'], 'Color': ['Dress']}
"""

class LaundryBasket:
    def __init__(self):
        self.clothes = []

    # Your code here
    pass


class TestLaundry(unittest.TestCase):
    def test_sorting(self):
        l = LaundryBasket()
        l.add_clothes("T-Shirt", "White")
        l.add_clothes("Pants", "Black")
        l.add_clothes("Socks", "Red")
        
        sorted_c = l.sort_clothes()
        self.assertEqual(sorted_c["White"], ["T-Shirt"])
        self.assertEqual(sorted_c["Dark"], ["Pants"])
        self.assertEqual(sorted_c["Color"], ["Socks"])

if __name__ == "__main__":
    unittest.main()
