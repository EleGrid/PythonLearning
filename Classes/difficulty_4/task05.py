import unittest

"""
Задача: Взросление (State Change)

Класс `Child` имеет атрибуты `age` и `status` ("Home", "Kindergarten", "School", "University").
- 0-2 года: "Home"
- 3-6 лет: "Kindergarten"
- 7-17 лет: "School"
- 18+: "University"
Метод `grow_up()` увеличивает возраст на 1 и автоматически обновляет `status` и соответсвии с правилами.

Пример:
    >>> maya = Child(2)
    >>> maya.status
    'Home'
    >>> maya.grow_up()
    >>> maya.age
    3
    >>> maya.status
    'Kindergarten'
"""

class Child:
    def __init__(self, age):
        self.age = age
        self.status = self._get_status()

    def _get_status(self):
        # Helper to determine status based on age
        if self.age < 3: return "Home"
        if self.age < 7: return "Kindergarten"
        if self.age < 18: return "School"
        return "University"

    def grow_up(self):
        # Implement logic
        pass

class TestChildGrowing(unittest.TestCase):
    def test_kindergarten_transition(self):
        c = Child(2)
        self.assertEqual(c.status, "Home")
        c.grow_up()
        self.assertEqual(c.age, 3)
        self.assertEqual(c.status, "Kindergarten")

    def test_school_transition(self):
        c = Child(6)
        c.grow_up()
        self.assertEqual(c.status, "School")

    def test_university_transition(self):
        c = Child(17)
        c.grow_up()
        self.assertEqual(c.status, "University")

if __name__ == "__main__":
    unittest.main()
