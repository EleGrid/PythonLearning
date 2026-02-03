import unittest

"""
Задача: Робот-помощник (Composition)

Создайте класс `RobotHelper`.
Он может выполнять разные задачи, но не сам, а используя инструменты.
У него есть метод `add_tool(tool_name, tool_obj)`.
И метод `do_task(task_name)`, который ищет подходящий инструмент.
Инструменты - это классы, у которых есть метод `execute()`.
- `VacuumCleaner` -> execute() returns "Vacuuming..."
- `Dishwasher` -> execute() returns "Washing dishes..."

Если инструмента для задачи нет, вернуть "I cannot do this".
Маппинг задачи на инструмент: "clean" -> "VacuumCleaner", "wash" -> "Dishwasher".

Пример:
    >>> bot = RobotHelper()
    >>> bot.add_tool(VacuumCleaner())
    >>> bot.do_task("clean")
    'Vacuuming...'
"""

class RobotHelper:
    def __init__(self):
        self.tools = [] # List of tool objects

    # Your code here
    pass

class VacuumCleaner:
    name = "VacuumCleaner"
    def execute(self): return "Vacuuming..."

class Dishwasher:
    name = "Dishwasher"
    def execute(self): return "Washing dishes..."

class TestRobot(unittest.TestCase):
    def test_clean_task(self):
        r = RobotHelper()
        r.add_tool(VacuumCleaner())
        self.assertEqual(r.do_task("clean"), "Vacuuming...")

    def test_unknown_task(self):
        r = RobotHelper()
        self.assertEqual(r.do_task("fly"), "I cannot do this")

    def test_missing_tool(self):
        r = RobotHelper()
        # "clean" needs VacuumCleaner, but we don't have it
        self.assertEqual(r.do_task("clean"), "I cannot do this")

if __name__ == "__main__":
    unittest.main()
