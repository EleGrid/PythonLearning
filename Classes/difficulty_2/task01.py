import unittest

"""
Задача: Кошелек

Мама дала Глебу карманные деньги. Создайте класс `Wallet` (Кошелек), 
который хранит текущий баланс (`balance`).
При создании кошелька баланс равен 0.
Добавьте методы:
1. `add_money(amount)` — добавляет деньги в кошелек.
2. `spend_money(amount)` — тратит деньги, если их достаточно. 
   Если денег хватает, уменьшает баланс и возвращает True.
   Если денег не хватает, баланс не меняется, возвращает False.

Пример:
    >>> my_wallet = Wallet()
    >>> my_wallet.add_money(100)
    >>> my_wallet.spend_money(50)
    True
    >>> my_wallet.balance
    50
    >>> my_wallet.spend_money(1000)
    False
"""

class Wallet:
    def __init__(self):
        self.balance = 0

    # Your code here
    pass


class TestWallet(unittest.TestCase):
    def test_initial_balance(self):
        w = Wallet()
        self.assertEqual(w.balance, 0)

    def test_add_money(self):
        w = Wallet()
        w.add_money(100)
        self.assertEqual(w.balance, 100)

    def test_spend_success(self):
        w = Wallet()
        w.add_money(100)
        result = w.spend_money(30)
        self.assertTrue(result)
        self.assertEqual(w.balance, 70)

    def test_spend_fail(self):
        w = Wallet()
        w.add_money(50)
        result = w.spend_money(100)
        self.assertFalse(result)
        self.assertEqual(w.balance, 50) # Balance should not change

if __name__ == "__main__":
    unittest.main()
