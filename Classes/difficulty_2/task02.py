import unittest

"""
Задача: Уставший ребенок

У нас есть класс `Child` с именем, возрастом и уровнем энергии (`energy`, по умолчанию 100).
Метод `play` уменьшает энергию на 20.
Измените метод `play` так, чтобы ребенок играл, только если энергии больше 0.
Если энергии <= 0, метод должен возвращать строку "Tired...".
Иначе уменьшает энергию и возвращает "Playing!".

Пример:
    >>> gleb = Child("Gleb", 11)
    >>> gleb.energy = 10
    >>> gleb.play()
    'Playing!'
    >>> gleb.play() # Energy becomes -10 (virtually) or stays at 0 depending on logic, but next call handles check
    'Tired...'
"""

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def play(self):
        if self.energy <= 0:
            return "Tired..."
        else:
            self.energy -= 20
            return "Playing!"


class TestChildPlay(unittest.TestCase):
    def test_play_when_energetic(self):
        c = Child("Gleb", 11)
        self.assertEqual(c.play(), "Playing!")
        self.assertEqual(c.energy, 80)

    def test_play_until_tired(self):
        c = Child("Maya", 4)
        c.energy = 0
        self.assertEqual(c.play(), "Tired...")
        self.assertEqual(c.energy, 0) # Should not decrease below 0 if logically prevented, or just check return

    def test_play_boundary(self):
        c = Child("Alisa", 6)
        c.energy = 10
        self.assertEqual(c.play(), "Playing!")
        self.assertEqual(c.energy, -10)
        self.assertEqual(c.play(), "Tired...")

if __name__ == "__main__":
    unittest.main()
