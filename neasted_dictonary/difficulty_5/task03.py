"""
Задача: Поиск пути к значению

Мама ищет, в какой категории находится определённый товар. Напиши функцию,
которая принимает многоуровневый словарь и искомое значение, возвращает
путь к этому значению в виде списка ключей или None, если значение не найдено.

Пример:
    >>> catalog = {
    ...     "electronics": {"phones": {"iphone": 999}, "tablets": {"ipad": 799}},
    ...     "clothes": {"shoes": {"sneakers": 150}}
    ... }
    >>> find_path(catalog, 999)
    ['electronics', 'phones', 'iphone']
    >>> find_path(catalog, 500)
    None
"""


def find_path(data, target, path=None):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestFindPath(unittest.TestCase):
    def test_find_deep(self):
        catalog = {
            "electronics": {"phones": {"iphone": 999}},
            "clothes": {"shoes": {"sneakers": 150}}
        }
        result = find_path(catalog, 999)
        self.assertEqual(result, ["electronics", "phones", "iphone"])

    def test_not_found(self):
        catalog = {"a": {"b": 1}}
        result = find_path(catalog, 999)
        self.assertIsNone(result)

    def test_first_level(self):
        data = {"key": 42}
        result = find_path(data, 42)
        self.assertEqual(result, ["key"])

    def test_string_value(self):
        data = {"person": {"name": "Gleb"}}
        result = find_path(data, "Gleb")
        self.assertEqual(result, ["person", "name"])


if __name__ == "__main__":
    unittest.main()
