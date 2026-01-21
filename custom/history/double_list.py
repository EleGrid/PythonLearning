# Задача 6: Удвоение элементов
# Создай новый список, где каждый элемент удвоен

def double_elements(numbers:list[int]):

    n = []
    for i in numbers:
        n.append(i * 2)
    print(n)
    # Ожидаемый результат: [2, 4, 6, 8, 10]

nu = [1, 2, 3, 4, 5]
double_elements(numbers=nu)
nu2 = [1,2,3,4,5,6,7,8,9]
double_elements(numbers=nu2)
double_elements(numbers=[5,6,7])