"""
Задача: Преобразование в плоский словарь

Мама хочет упростить структуру данных. Напиши функцию, которая превращает
вложенный словарь в плоский, объединяя ключи через точку.

Пример:
    >>> data = {"user": {"name": "Gleb", "age": 11}}
    >>> flatten_dict(data)
    {'user.name': 'Gleb', 'user.age': 11}
"""


def flatten_dict(data: dict) -> dict:
    new_dict = {}
    for key_1 in data:
        for key_2 in data[key_1]:
            new_key = f"{key_1}.{key_2}"
            new_dict[new_key] = data[key_1][key_2]
    return new_dict

# === Тесты ===
import unittest


class TestFlattenDict(unittest.TestCase):
    def test_standard(self):
        data = {"user": {"name": "Gleb", "age": 11}}
        result = flatten_dict(data)
        self.assertEqual(result["user.name"], "Gleb")
        self.assertEqual(result["user.age"], 11)

    def test_multiple_categories(self):
        data = {"a": {"x": 1}, "b": {"y": 2}}
        result = flatten_dict(data)
        self.assertEqual(result["a.x"], 1)
        self.assertEqual(result["b.y"], 2)

    def test_empty(self):
        self.assertEqual(flatten_dict({}), {})

    def test_empty_inner(self):
        data = {"a": {}}
        self.assertEqual(flatten_dict(data), {})


if __name__ == "__main__":
    unittest.main()
