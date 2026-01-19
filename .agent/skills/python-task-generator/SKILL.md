---
name: python-task-generator
description: Use when creating Python learning tasks for a homemaker theme. Generates 25 tasks (5 per difficulty level) with Russian descriptions and English code templates.
---

# Python Task Generator

## Overview

Генерирует задачи по Python для изучения программирования. Все задачи тематически связаны с бытом домохозяйки, мамы троих детей.

**Персонажи для задач:**
- Глеб — 11 лет (старший сын)
- Алиса — 6 лет (средняя дочь)
- Майя — 4 года (младшая дочь)

## When to Use

- Нужно создать набор задач по конкретной теме Python
- Задачи должны быть понятны и интересны для изучающих Python
- Требуется градация сложности от очень лёгкой до очень сложной

## Output Structure

```
<Тема>/
  ├── difficulty_1/
  │   ├── task01.py
  │   ├── task02.py
  ├── difficulty_2/
  ...  
  └── difficulty_5/
```

Каждая задача состоит из одного файла:
- `taskNN.py` — файл с условием и шаблоном и с unittest тестами

## Task File Format

```python
"""
Задача: [Краткое название]

[Понятное описание на русском языке, что нужно сделать.
Упоминает персонажей: Глеб, Алиса или Майя в контексте домашнего быта.]

Пример:
    >>> function_name(input)
    expected_output
"""

def function_name(parameters):
    # Your code here
    pass

class TestFunctionName(unittest.TestCase):
    def test_gleb(self):
        self.assertEqual(function_name({"name": "Gleb", "age": 11}), "Gleb")

    def test_alisa(self):
        self.assertEqual(function_name({"name": "Alisa", "age": 6}), "Alisa")

    def test_maya(self):
        self.assertEqual(function_name({"name": "Maya", "age": 4}), "Maya")

    def test_with_extra_fields(self):
        self.assertEqual(function_name({"name": "Gleb", "age": 11, "grade": 5}), "Gleb")


if __name__ == "__main__":
    unittest.main()
```

## Difficulty Levels

| Level | Название | Концепции |
|-------|----------|-----------|
| 1 | Очень лёгкий | Базовый синтаксис, простые операции |
| 2 | Лёгкий | Условия, простые циклы |
| 3 | Средний | Вложенные структуры, функции |
| 4 | Сложный | Алгоритмы, сложные структуры данных |
| 5 | Очень сложный | Оптимизация, комбинированные задачи |

## Usage

При вызове укажите:
1. **Тема Python** — например: "Циклы while", "Словари", "Списки"
2. **Путь** — где создать папку с задачами

## Critical Rules

1. **Описания на русском** — понятные, ёмкие формулировки
2. **Код на английском** — имена функций, переменных, значения в словарях
3. **Тематика домохозяйки** — покупки, готовка, уборка, расписание детей
4. **Персонажи** — используйте имена: Gleb (11), Alisa (6), Maya (4) в коде
5. **Без решений** — только шаблон функции с `pass`
6. **Тесты для каждой задачи** — простые unittest проверки (3-5 тестов на задачу)

## Example Task (Difficulty 2 — Списки)

**task01.py:**
```python
import unittest
"""
Задача: Список покупок

Алиса помогает маме составить список покупок. Напиши функцию, 
которая принимает список продуктов и возвращает их количество.

Пример:
    >>> count_items(["milk", "bread", "eggs"])
    3
"""

def count_items(shopping_list):
    # Your code here
    pass


class TestCountItems(unittest.TestCase):
    def test_three_items(self):
        self.assertEqual(count_items(["milk", "bread", "eggs"]), 3)

    def test_empty_list(self):
        self.assertEqual(count_items([]), 0)

    def test_one_item(self):
        self.assertEqual(count_items(["apple"]), 1)

    def test_many_items(self):
        self.assertEqual(count_items(["a", "b", "c", "d", "e"]), 5)


if __name__ == "__main__":
    unittest.main()
```

## Example Task (Difficulty 4 — Словари)

**task01.py:**
```python
import unittest
"""
Задача: Расписание занятий

У Глеба разные кружки по дням недели. Напиши функцию, которая 
принимает словарь расписания и день недели, возвращает список 
занятий на этот день или пустой список, если занятий нет.

Пример:
    >>> schedule = {"monday": ["math", "swimming"], "wednesday": ["piano"]}
    >>> get_activities(schedule, "monday")
    ["math", "swimming"]
    >>> get_activities(schedule, "friday")
    []
"""

def get_activities(schedule, day):
    # Your code here
    pass


class TestGetActivities(unittest.TestCase):
    def setUp(self):
        self.schedule = {
            "monday": ["math", "swimming"],
            "wednesday": ["piano"],
            "friday": []
        }
    def test_day_with_activities(self):
        self.assertEqual(get_activities(self.schedule, "monday"), ["math", "swimming"])

    def test_day_with_one_activity(self):
        self.assertEqual(get_activities(self.schedule, "wednesday"), ["piano"])

    def test_day_not_in_schedule(self):
        self.assertEqual(get_activities(self.schedule, "sunday"), [])

    def test_empty_schedule(self):
        self.assertEqual(get_activities({}, "monday"), [])


if __name__ == "__main__":
    unittest.main()
```
