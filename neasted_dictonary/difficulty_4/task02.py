"""
Задача: Слияние словарей покупок

Мама объединяет два списка покупок по категориям. Напиши функцию, которая
принимает два словаря покупок с вложенными категориями и объединяет их,
суммируя количество одинаковых продуктов.

Пример:
    >>> list1 = {"dairy": {"milk": 2}, "bakery": {"bread": 1}}
    >>> list2 = {"dairy": {"milk": 1, "cheese": 2}, "fruits": {"apples": 5}}
    >>> merge_shopping(list1, list2)
    {'dairy': {'milk': 3, 'cheese': 2}, 'bakery': {'bread': 1}, 'fruits': {'apples': 5}}
"""


def merge_shopping(list1, list2):
    # Your code here
    pass


# === Тесты ===
import unittest


class TestMergeShopping(unittest.TestCase):
    def test_merge_with_overlap(self):
        list1 = {"dairy": {"milk": 2}, "bakery": {"bread": 1}}
        list2 = {"dairy": {"milk": 1, "cheese": 2}, "fruits": {"apples": 5}}
        result = merge_shopping(list1, list2)
        self.assertEqual(result["dairy"]["milk"], 3)
        self.assertEqual(result["dairy"]["cheese"], 2)
        self.assertEqual(result["bakery"]["bread"], 1)
        self.assertEqual(result["fruits"]["apples"], 5)

    def test_no_overlap(self):
        list1 = {"a": {"x": 1}}
        list2 = {"b": {"y": 2}}
        result = merge_shopping(list1, list2)
        self.assertEqual(result, {"a": {"x": 1}, "b": {"y": 2}})

    def test_empty_first(self):
        result = merge_shopping({}, {"dairy": {"milk": 1}})
        self.assertEqual(result, {"dairy": {"milk": 1}})

    def test_empty_second(self):
        result = merge_shopping({"dairy": {"milk": 1}}, {})
        self.assertEqual(result, {"dairy": {"milk": 1}})


if __name__ == "__main__":
    unittest.main()
