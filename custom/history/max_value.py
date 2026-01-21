# Задача 5: Поиск максимального элемента
# Найди максимальный элемент в списке

def find_max():
    numbers = [12, 45, 7, 89, 23, 56]
    max_value = 0
    for i in numbers:
        if i > max_value:
            max_value = i
    print(max_value)
    # Ожидаемый результат: 89


find_max()