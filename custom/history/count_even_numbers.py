# Задача 3: Подсчёт чётных чисел
# Посчитай количество чётных чисел в списке

def count_even(numbers: list, text: str):
    count = 0
    for count_numbers in numbers:
        if count_numbers % 2 == 0:
            count += 1
    print(f"{text} {count}")
    # Ожидаемый результат: 5


hhh = "количество чётных чисел в списке: "
hhh2 = f"yyyy:{hhh}"
print()
numbers = [1, 4, 6, 7, 10, 15, 22, 33, 40]
count_even(numbers, hhh)
count_even(numbers, f"{hhh}")
