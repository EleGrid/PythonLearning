"""
Задача: Pivot-таблица

Майя создаёт сводную таблицу расходов. Напиши функцию, которая преобразует
список записей в pivot-таблицу с суммированием.

Пример:
    >>> records = [
    ...     {"month": "jan", "category": "food", "amount": 100},
    ...     {"month": "jan", "category": "transport", "amount": 50},
    ...     {"month": "feb", "category": "food", "amount": 120}
    ... ]
    >>> pivot_table(records, "month", "category", "amount")
    {'jan': {'food': 100, 'transport': 50}, 'feb': {'food': 120}}
"""


def pivot_table(records: list, row_field: str, col_field: str, value_field: str) -> dict:
    # Your code here
    pass


# === Тесты ===
import unittest


class TestPivotTable(unittest.TestCase):
    def test_standard(self):
        records = [
            {"month": "jan", "category": "food", "amount": 100},
            {"month": "jan", "category": "transport", "amount": 50},
            {"month": "feb", "category": "food", "amount": 120}
        ]
        result = pivot_table(records, "month", "category", "amount")
        self.assertEqual(result["jan"]["food"], 100)
        self.assertEqual(result["jan"]["transport"], 50)
        self.assertEqual(result["feb"]["food"], 120)

    def test_aggregation(self):
        records = [
            {"m": "jan", "c": "food", "v": 50},
            {"m": "jan", "c": "food", "v": 50}
        ]
        result = pivot_table(records, "m", "c", "v")
        self.assertEqual(result["jan"]["food"], 100)

    def test_single_record(self):
        records = [{"a": "x", "b": "y", "c": 10}]
        result = pivot_table(records, "a", "b", "c")
        self.assertEqual(result["x"]["y"], 10)

    def test_empty(self):
        self.assertEqual(pivot_table([], "a", "b", "c"), {})


if __name__ == "__main__":
    unittest.main()
