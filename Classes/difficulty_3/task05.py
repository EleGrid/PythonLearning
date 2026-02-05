import unittest

"""
Задача: Обновление уборки

Вернемся к классу `CleaningSchedule`. Теперь мы храним не просто список комнат,
а словарь `rooms`, где ключ - название комнаты, а значение - Boolean (убрано или нет).
По умолчанию все False.
Метод `__init__` принимает СПИСОК названий, преобразует в словарь.
Добавьте метод `clean_room(room_name)`, который меняет статус на True.
Если такой комнаты нет, ничего не делает.

Пример:
    >>> s = CleaningSchedule(["Kitchen", "Hall"])
    >>> s.rooms
    {'Kitchen': False, 'Hall': False}
    >>> s.clean_room("Kitchen")
    >>> s.rooms
    {'Kitchen': True, 'Hall': False}
"""

class CleaningSchedule:
    def __init__(self, room_names):
        self.rooms = {}
        for key_room in room_names:
            self.rooms[key_room] = False

    def clean_room(self, room_name):
        if room_name in self.rooms:
            self.rooms[room_name] = True



class TestCleaningUpdate(unittest.TestCase):
    def test_init(self):
        s = CleaningSchedule(["A", "B"])
        self.assertEqual(s.rooms, {"A": False, "B": False})

    def test_clean(self):
        s = CleaningSchedule(["A"])
        s.clean_room("A")
        self.assertTrue(s.rooms["A"])

    def test_clean_unknown(self):
        s = CleaningSchedule(["A"])
        s.clean_room("Z")
        self.assertFalse(s.rooms["A"])
        self.assertNotIn("Z", s.rooms)

if __name__ == "__main__":
    unittest.main()
