"""
Задача: Замена всех значений

Алиса хочет сбросить все числовые значения в бюджете на ноль.
Напиши функцию, которая рекурсивно заменяет все значения определённого типа.

Пример:
    >>> data = {"food": {"milk": 80, "cheese": 250}}
    >>> replace_all_values(data, int, 0)
    {'food': {'milk': 0, 'cheese': 0}}
"""


def replace_all_values(data: dict, value_type: type, new_value) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestReplaceAllValues(unittest.TestCase):
    def test_replace_ints(self):
        data = {"food": {"milk": 80, "cheese": 250}}
        result = replace_all_values(data, int, 0)
        self.assertEqual(result["food"]["milk"], 0)
        self.assertEqual(result["food"]["cheese"], 0)

    def test_replace_strings(self):
        data = {"user": {"name": "Gleb", "city": "Moscow"}}
        result = replace_all_values(data, str, "empty")
        self.assertEqual(result["user"]["name"], "empty")

    def test_no_match(self):
        data = {"a": {"b": 1}}
        result = replace_all_values(data, str, "x")
        self.assertEqual(result["a"]["b"], 1)

    def test_empty(self):
        self.assertEqual(replace_all_values({}, int, 0), {})


if __name__ == "__main__":
    unittest.main()
