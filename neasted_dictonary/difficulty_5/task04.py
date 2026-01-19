"""
Задача: Валидация структуры словаря

Мама проверяет, соответствует ли заполненная анкета ребёнка требуемой структуре.
Напиши функцию, которая принимает словарь данных и словарь-схему, проверяет,
что все ключи схемы присутствуют в данных с правильными типами.

Схема указывает ожидаемые типы: "str", "int", "dict", "list".

Пример:
    >>> schema = {"name": "str", "age": "int", "address": {"city": "str"}}
    >>> data = {"name": "Gleb", "age": 11, "address": {"city": "Moscow"}}
    >>> validate_structure(data, schema)
    True
    >>> bad_data = {"name": "Gleb", "age": "eleven"}
    >>> validate_structure(bad_data, schema)
    False
"""


def validate_structure(data, schema):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestValidateStructure(unittest.TestCase):
    def test_valid(self):
        schema = {"name": "str", "age": "int", "address": {"city": "str"}}
        data = {"name": "Gleb", "age": 11, "address": {"city": "Moscow"}}
        self.assertTrue(validate_structure(data, schema))

    def test_wrong_type(self):
        schema = {"age": "int"}
        data = {"age": "eleven"}
        self.assertFalse(validate_structure(data, schema))

    def test_missing_key(self):
        schema = {"name": "str", "age": "int"}
        data = {"name": "Alisa"}
        self.assertFalse(validate_structure(data, schema))

    def test_nested_invalid(self):
        schema = {"address": {"city": "str"}}
        data = {"address": {"city": 123}}
        self.assertFalse(validate_structure(data, schema))

    def test_with_list(self):
        schema = {"hobbies": "list"}
        data = {"hobbies": ["chess", "swimming"]}
        self.assertTrue(validate_structure(data, schema))


if __name__ == "__main__":
    unittest.main()
