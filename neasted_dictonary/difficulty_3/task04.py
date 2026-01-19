"""
Задача: Все хобби детей

Мама хочет знать все хобби своих детей. Напиши функцию, которая принимает
словарь семьи с детьми и возвращает список всех уникальных хобби.

Пример:
    >>> family = {
    ...     "Gleb": {"age": 11, "hobbies": ["chess", "swimming"]},
    ...     "Alisa": {"age": 6, "hobbies": ["dancing", "chess"]}
    ... }
    >>> get_all_hobbies(family)
    ['chess', 'dancing', 'swimming']
"""


def get_all_hobbies(family):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestGetAllHobbies(unittest.TestCase):
    def test_two_children(self):
        family = {
            "Gleb": {"age": 11, "hobbies": ["chess", "swimming"]},
            "Alisa": {"age": 6, "hobbies": ["dancing", "chess"]}
        }
        result = get_all_hobbies(family)
        self.assertEqual(sorted(result), ["chess", "dancing", "swimming"])

    def test_single_child(self):
        family = {"Maya": {"age": 4, "hobbies": ["playing", "drawing"]}}
        result = get_all_hobbies(family)
        self.assertEqual(sorted(result), ["drawing", "playing"])

    def test_no_duplicates(self):
        family = {
            "A": {"hobbies": ["x"]},
            "B": {"hobbies": ["y"]},
            "C": {"hobbies": ["z"]}
        }
        result = get_all_hobbies(family)
        self.assertEqual(sorted(result), ["x", "y", "z"])

    def test_all_same_hobby(self):
        family = {
            "Gleb": {"hobbies": ["music"]},
            "Alisa": {"hobbies": ["music"]}
        }
        result = get_all_hobbies(family)
        self.assertEqual(result, ["music"])


if __name__ == "__main__":
    unittest.main()
