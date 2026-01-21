# Задача 7: Фильтрация отрицательных чисел
# Создай новый список только с положительными числами

def filter_negative(numbers:list[int]):

    positive_num = []
    for pos_num in numbers:
        if pos_num >= 0:
            positive_num.append(pos_num)
    print(positive_num)

    # Ожидаемый результат: [3, 7, 12]
num = [-5, 3, -1, 7, -8, 12, -2]

filter_negative(num)