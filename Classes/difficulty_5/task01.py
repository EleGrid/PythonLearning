import unittest

"""
Задача: Умный дом (System of Objects)

Создайте класс `SmartHome`.
В нем есть метод `add_device(device)`, который принимает объект устройства.
У каждого устройства есть метод `consume_power()` который возвращает потребление энергии.
У `SmartHome` должен быть метод `get_total_consumption()`, который суммирует потребление всех добавленных устройств.

Нужно также создать фиктивные классы устройств для проверки (или использовать моки, но лучше простые классы `Lamp`, `TV`).

Пример:
    >>> home = SmartHome()
    >>> home.add_device(Lamp(10)) # 10 Watt
    >>> home.add_device(TV(100))  # 100 Watt
    >>> home.get_total_consumption()
    110
"""

class SmartHome:
    def __init__(self):
        self.devices = []
    
    # Your code here
    pass

# Mock classes for devices
class Lamp:
    def __init__(self, power):
        self.power = power
    def consume_power(self):
        return self.power

class TV:
    def __init__(self, power):
        self.power = power
    def consume_power(self):
        return self.power


class TestSmartHome(unittest.TestCase):
    def test_total_consumption(self):
        home = SmartHome()
        home.add_device(Lamp(50))
        home.add_device(TV(150))
        self.assertEqual(home.get_total_consumption(), 200)

    def test_empty_home(self):
        home = SmartHome()
        self.assertEqual(home.get_total_consumption(), 0)

if __name__ == "__main__":
    unittest.main()
