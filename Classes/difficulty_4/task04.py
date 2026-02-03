import unittest

"""
Задача: Конфликт расписания (Time Logic)

Класс `TimeManager` хранит занятия ребенка: `(start_hour, end_hour)`.
Например: `(14, 16)` - с 14:00 до 16:00.
Метод `add_activity(start, end)` должен добавлять занятие только если оно 
НЕ ПЕРЕСЕКАЕТСЯ с уже существующими.
Если пересекается - возвращать False и не добавлять. Иначе - True и добавлять.
Считаем, что (14, 15) и (15, 16) НЕ пересекаются (стыкуются).

Пример:
    >>> tm = TimeManager()
    >>> tm.add_activity(10, 12)
    True
    >>> tm.add_activity(11, 13) # Пересечение с 10-12
    False
"""

class TimeManager:
    def __init__(self):
        self.activities = []

    # Your code here
    pass


class TestTimeManager(unittest.TestCase):
    def test_no_overlap(self):
        tm = TimeManager()
        self.assertTrue(tm.add_activity(10, 12))
        self.assertTrue(tm.add_activity(12, 14))

    def test_overlap_inside(self):
        tm = TimeManager()
        tm.add_activity(10, 15)
        self.assertFalse(tm.add_activity(11, 12))

    def test_overlap_partial(self):
        tm = TimeManager()
        tm.add_activity(10, 12)
        self.assertFalse(tm.add_activity(11, 13))
        self.assertFalse(tm.add_activity(9, 11))

if __name__ == "__main__":
    unittest.main()
