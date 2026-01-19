"""
Задача: Первое хобби

Алиса хочет узнать своё первое хобби из списка. Напиши функцию, которая
принимает словарь ребёнка со списком хобби и возвращает первое хобби.

Пример:
    >>> child = {"name": "Alisa", "hobbies": ["drawing", "dancing", "singing"]}
    >>> get_first_hobby(child)
    'drawing'
"""


def get_first_hobby(child):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetFirstHobby(unittest.TestCase):
    def test_alisa(self):
        child = {"name": "Alisa", "hobbies": ["drawing", "dancing", "singing"]}
        self.assertEqual(get_first_hobby(child), "drawing")

    def test_single_hobby(self):
        child = {"name": "Maya", "hobbies": ["playing"]}
        self.assertEqual(get_first_hobby(child), "playing")

    def test_gleb(self):
        child = {"name": "Gleb", "hobbies": ["chess", "swimming", "coding"]}
        self.assertEqual(get_first_hobby(child), "chess")

    def test_many_hobbies(self):
        child = {"name": "Alisa", "hobbies": ["reading", "writing", "painting", "music"]}
        self.assertEqual(get_first_hobby(child), "reading")


if __name__ == "__main__":
    unittest.main()
