import unittest

"""
Задача: Планировщик праздника (Complex Logic)

Класс `HolidayPlanner` помогает рассадить гостей.
Есть столы с вместимостью `{"Table1": 4, "Table2": 6}`.
Метод `seat_guests(guest_list)` должен распределить гостей по столам так,
чтобы задействовать минимум столов.
Возвращает словарь `{"TableName": [guests_at_this_table]}`.
Если гостей слишком много, возбуждает ошибку `ValueError`.

Пример:
    >>> tables = {"T1": 2, "T2": 2}
    >>> hp = HolidayPlanner(tables)
    >>> dist = hp.seat_guests(["A", "B", "C"])
    >>> # Оптимально: заполнить T1 (2 чел) и T2 (1 чел) или наоборот.
"""

class HolidayPlanner:
    def __init__(self, tables):
        self.tables = tables # {"Table1": 4, "Table2": 6}

    def seat_guests(self, guests):
        # Logic to distribute guests
        pass


class TestHolidayPlanner(unittest.TestCase):
    def test_fit_guests(self):
        hp = HolidayPlanner({"T1": 5})
        res = hp.seat_guests(["A", "B", "C"])
        self.assertEqual(len(res), 1)
        self.assertEqual(len(res["T1"]), 3)

    def test_overflow(self):
        hp = HolidayPlanner({"T1": 1})
        with self.assertRaises(ValueError):
            hp.seat_guests(["A", "B"])

    def test_distribution(self):
        # Greedy fit or simple fit
        hp = HolidayPlanner({"T1": 2, "T2": 2})
        res = hp.seat_guests(["A", "B", "C"])
        total_seated = sum(len(v) for v in res.values())
        self.assertEqual(total_seated, 3)

if __name__ == "__main__":
    unittest.main()
