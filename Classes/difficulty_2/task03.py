import unittest

"""
Задача: Просроченные продукты

Есть класс `Product` с названием и сроком годности в днях (`days_valid`).
Добавьте метод `is_expired(days_passed)`, который принимает количество прошедших дней.
Если `days_passed` больше `days_valid`, метод возвращает True (испорчен).
Иначе False (свежий).

Пример:
    >>> milk = Product("Milk", 3)
    >>> milk.is_expired(2)
    False
    >>> milk.is_expired(5)
    True
"""

class Product:
    def __init__(self, name, days_valid):
        self.name = name
        self.days_valid = days_valid

    # Your code here
    pass


class TestProductExpiration(unittest.TestCase):
    def test_fresh(self):
        p = Product("Yogurt", 7)
        self.assertFalse(p.is_expired(5))

    def test_expired(self):
        p = Product("Milk", 3)
        self.assertTrue(p.is_expired(4))

    def test_last_day(self):
        p = Product("Bread", 3)
        self.assertFalse(p.is_expired(3)) # On the last day it is still valid usually

if __name__ == "__main__":
    unittest.main()
