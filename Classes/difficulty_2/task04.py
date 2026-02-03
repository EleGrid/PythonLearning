import unittest

"""
Задача: Настольная лампа

Создайте класс `Lamp` (Лампа).
У нее должен быть атрибут `is_on` (включена ли она), по умолчанию False.
Создайте метод `toggle()`, который переключает состояние лампы:
если была выключена — включает, если была включена — выключает.

Пример:
    >>> lamp = Lamp()
    >>> lamp.is_on
    False
    >>> lamp.toggle()
    >>> lamp.is_on
    True
    >>> lamp.toggle()
    >>> lamp.is_on
    False
"""

class Lamp:
    # Your code here
    pass


class TestLamp(unittest.TestCase):
    def test_initial_state(self):
        l = Lamp()
        self.assertFalse(l.is_on)

    def test_toggle(self):
        l = Lamp()
        l.toggle()
        self.assertTrue(l.is_on)
        l.toggle()
        self.assertFalse(l.is_on)

    def test_multiple_toggles(self):
        l = Lamp()
        for _ in range(10):
            l.toggle()
        self.assertFalse(l.is_on) # Even number of toggles returns to False

if __name__ == "__main__":
    unittest.main()
