"""
Задача: Рекурсивное клонирование с преобразованием ключей

Алиса хочет преобразовать все ключи в нижний регистр. Напиши функцию,
которая рекурсивно клонирует словарь, применяя функцию преобразования
ко всем ключам.

Пример:
    >>> data = {"User": {"Name": "Gleb", "AGE": 11}}
    >>> transform_keys(data, str.lower)
    {'user': {'name': 'Gleb', 'age': 11}}
"""


def transform_keys(data: dict, transform_func) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestTransformKeys(unittest.TestCase):
    def test_lowercase(self):
        data = {"User": {"Name": "Gleb", "AGE": 11}}
        result = transform_keys(data, str.lower)
        self.assertIn("user", result)
        self.assertIn("name", result["user"])
        self.assertEqual(result["user"]["age"], 11)

    def test_uppercase(self):
        data = {"user": {"name": "Gleb"}}
        result = transform_keys(data, str.upper)
        self.assertIn("USER", result)
        self.assertIn("NAME", result["USER"])

    def test_preserves_values(self):
        data = {"a": {"b": "value"}}
        result = transform_keys(data, str.upper)
        self.assertEqual(result["A"]["B"], "value")

    def test_empty(self):
        self.assertEqual(transform_keys({}, str.lower), {})


if __name__ == "__main__":
    unittest.main()
