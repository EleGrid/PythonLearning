import unittest

"""
Задача: График уборки

Мама составляет график уборки. Нужно создать класс `CleaningSchedule`, 
который при инициализации принимает список комнат (`rooms`), где нужно убраться.
Атрибут, в котором хранится список, должен называться `rooms_to_clean`.

Пример:
    >>> schedule = CleaningSchedule(["kitchen", "bedroom"])
    >>> schedule.rooms_to_clean
    ['kitchen', 'bedroom']
"""

class CleaningSchedule:
    def __init__(self, rooms):
        self.rooms_to_clean = rooms


class TestCleaningSchedule(unittest.TestCase):
    def test_rooms_list(self):
        rooms = ["kitchen", "living_room", "bathroom"]
        schedule = CleaningSchedule(rooms)
        self.assertEqual(schedule.rooms_to_clean, rooms)

    def test_empty_schedule(self):
        schedule = CleaningSchedule([])
        self.assertEqual(schedule.rooms_to_clean, [])

    def test_single_room(self):
        schedule = CleaningSchedule(["nursery"])
        self.assertEqual(schedule.rooms_to_clean, ["nursery"])

if __name__ == "__main__":
    unittest.main()
