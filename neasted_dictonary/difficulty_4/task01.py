"""
Задача: Обновление вложенного значения

Глеб получил новую оценку по математике. Напиши функцию, которая принимает
словарь ученика, путь в виде списка ключей и новое значение. Функция должна
обновить значение по указанному пути и вернуть изменённый словарь.

Пример:
    >>> student = {"name": "Gleb", "grades": {"math": 4, "english": 5}}
    >>> update_nested(student, ["grades", "math"], 5)
    {'name': 'Gleb', 'grades': {'math': 5, 'english': 5}}
"""


def update_nested(data, keys, value):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestUpdateNested(unittest.TestCase):
    def test_update_grade(self):
        student = {"name": "Gleb", "grades": {"math": 4, "english": 5}}
        result = update_nested(student, ["grades", "math"], 5)
        self.assertEqual(result["grades"]["math"], 5)

    def test_single_key(self):
        data = {"name": "Alisa"}
        result = update_nested(data, ["name"], "Maya")
        self.assertEqual(result["name"], "Maya")

    def test_deep_path(self):
        data = {"a": {"b": {"c": 1}}}
        result = update_nested(data, ["a", "b", "c"], 99)
        self.assertEqual(result["a"]["b"]["c"], 99)

    def test_preserves_other_values(self):
        student = {"name": "Gleb", "grades": {"math": 4, "english": 5}}
        result = update_nested(student, ["grades", "math"], 5)
        self.assertEqual(result["grades"]["english"], 5)
        self.assertEqual(result["name"], "Gleb")


if __name__ == "__main__":
    unittest.main()
