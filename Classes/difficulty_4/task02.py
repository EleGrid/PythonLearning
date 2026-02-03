import unittest

"""
Задача: Умный холодильник (Logic & Filtering)

Класс `SmartFridge` хранит продукты в словаре `items` вида `{"Milk": days_valid, "Egg": days_valid}`, 
где `days_valid` - сколько дней осталось до истечения срока годности.
Добавьте метод `add_item(name, days)`.
Добавьте метод `get_expiring_soon(days_threshold)`, который возвращает СПИСОК продуктов, 
которые испортятся через `days_threshold` дней или раньше.

Пример:
    >>> f = SmartFridge()
    >>> f.add_item("Milk", 2)
    >>> f.add_item("Cheese", 10)
    >>> f.get_expiring_soon(3)
    ['Milk']
"""

class SmartFridge:
    def __init__(self):
        self.items = {}

    # Your code here
    pass


class TestSmartFridge(unittest.TestCase):
    def test_expiring(self):
        f = SmartFridge()
        f.add_item("A", 1)
        f.add_item("B", 5)
        self.assertEqual(f.get_expiring_soon(2), ["A"])

    def test_multiple_expiring(self):
        f = SmartFridge()
        f.add_item("A", 1)
        f.add_item("B", 2)
        f.add_item("C", 10)
        # Order implies list comparison, sorting might be needed if order matters, 
        # but usually order of insertion or dict iteration. Test checks content.
        result = f.get_expiring_soon(2)
        self.assertIn("A", result)
        self.assertIn("B", result)
        self.assertEqual(len(result), 2)

    def test_none_expiring(self):
        f = SmartFridge()
        f.add_item("A", 10)
        self.assertEqual(f.get_expiring_soon(5), [])

if __name__ == "__main__":
    unittest.main()
