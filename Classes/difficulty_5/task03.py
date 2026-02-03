import unittest

"""
Задача: Ленивая уборка (Optimization)

Класс `Pantry` хранит продукты: `{"Milk": expiration_date}`.
Вместо того чтобы каждый раз проверять все продукты, реализуйте метод `clean_expired(current_date)`,
но с оптимизацией: метод `get_product(name, current_date)` должен сам проверять, 
не испортился ли продукт, прежде чем его вернуть.
Если испортился - удалить из хранилища и вернуть None.
Если свежий - вернуть название.

Пример:
    >>> p = Pantry()
    >>> p.add_product("Milk", 10) # expires on day 10
    >>> p.get_product("Milk", 5)  # current day 5 -> OK
    'Milk'
    >>> p.get_product("Milk", 11) # current day 11 -> Expired -> None
    None
    >>> p.products
    {}
"""

class Pantry:
    def __init__(self):
        self.products = {} # Name: Expiration Day

    def add_product(self, name, expiration):
        self.products[name] = expiration

    def get_product(self, name, current_date):
        # Implement lazy expiration check
        pass


class TestPantry(unittest.TestCase):
    def test_get_fresh(self):
        p = Pantry()
        p.add_product("A", 10)
        self.assertEqual(p.get_product("A", 5), "A")
        self.assertIn("A", p.products)

    def test_get_expired_lazy_removal(self):
        p = Pantry()
        p.add_product("B", 10)
        self.assertIsNone(p.get_product("B", 12))
        self.assertNotIn("B", p.products) # Should be removed

if __name__ == "__main__":
    unittest.main()
