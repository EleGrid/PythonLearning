"""
Задача: Сериализация с обработкой циклов

Глеб создаёт сложные структуры данных. Напиши функцию, которая преобразует
многоуровневый словарь в список пар (путь, значение), обрабатывая только
листовые значения.

Пример:
    >>> data = {"a": {"b": 1, "c": {"d": 2}}}
    >>> serialize_leaves(data)
    [('a.b', 1), ('a.c.d', 2)]
"""


def serialize_leaves(data: dict, prefix: str = "") -> list:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestSerializeLeaves(unittest.TestCase):
    def test_standard(self):
        data = {"a": {"b": 1, "c": {"d": 2}}}
        result = serialize_leaves(data)
        self.assertIn(("a.b", 1), result)
        self.assertIn(("a.c.d", 2), result)

    def test_flat(self):
        data = {"x": 1, "y": 2}
        result = serialize_leaves(data)
        self.assertIn(("x", 1), result)
        self.assertIn(("y", 2), result)

    def test_deep(self):
        data = {"a": {"b": {"c": {"d": 100}}}}
        result = serialize_leaves(data)
        self.assertEqual(result, [("a.b.c.d", 100)])

    def test_empty(self):
        self.assertEqual(serialize_leaves({}), [])


if __name__ == "__main__":
    unittest.main()
