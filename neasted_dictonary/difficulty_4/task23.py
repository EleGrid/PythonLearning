"""
Задача: Валидация структуры

Алиса проверяет, соответствует ли словарь заданной схеме. Напиши функцию,
которая проверяет, содержит ли словарь все обязательные ключи из схемы.

Пример:
    >>> schema = {"user": {"name": True, "age": True}}
    >>> data = {"user": {"name": "Gleb", "age": 11, "extra": "ok"}}
    >>> validate_schema(data, schema)
    True
"""


def validate_schema(data: dict, schema: dict) -> bool:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestValidateSchema(unittest.TestCase):
    def test_valid(self):
        schema = {"user": {"name": True, "age": True}}
        data = {"user": {"name": "Gleb", "age": 11, "extra": "ok"}}
        self.assertTrue(validate_schema(data, schema))

    def test_missing_key(self):
        schema = {"user": {"name": True, "age": True}}
        data = {"user": {"name": "Gleb"}}
        self.assertFalse(validate_schema(data, schema))

    def test_missing_category(self):
        schema = {"user": {"name": True}}
        data = {"profile": {"name": "Gleb"}}
        self.assertFalse(validate_schema(data, schema))

    def test_empty_schema(self):
        self.assertTrue(validate_schema({"a": 1}, {}))


if __name__ == "__main__":
    unittest.main()
