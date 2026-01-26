"""
Задача: Инвертирование ключей

Мама хочет найти, в какой комнате находится каждая вещь. Напиши функцию,
которая принимает словарь {комната: {вещь: количество}} и возвращает
словарь {вещь: комната}.

Пример:
    >>> rooms = {"kitchen": {"pan": 2, "pot": 3}, "bedroom": {"lamp": 1}}
    >>> invert_location(rooms)
    {'pan': 'kitchen', 'pot': 'kitchen', 'lamp': 'bedroom'}
"""


def invert_location(data: dict) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestInvertLocation(unittest.TestCase):
    def test_standard(self):
        rooms = {"kitchen": {"pan": 2, "pot": 3}, "bedroom": {"lamp": 1}}
        result = invert_location(rooms)
        self.assertEqual(result["pan"], "kitchen")
        self.assertEqual(result["lamp"], "bedroom")

    def test_single_room(self):
        rooms = {"living": {"tv": 1, "sofa": 1}}
        result = invert_location(rooms)
        self.assertEqual(result, {"tv": "living", "sofa": "living"})

    def test_empty(self):
        self.assertEqual(invert_location({}), {})

    def test_empty_room(self):
        rooms = {"empty": {}}
        self.assertEqual(invert_location(rooms), {})


if __name__ == "__main__":
    unittest.main()
