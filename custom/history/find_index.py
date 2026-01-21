# Задача 10: Индексы элементов
# Найди все индексы, где встречается буква 'a'

def find_indices():
    letters = ['a', 'b', 'a', 'c', 'a', 'd', 'a']
    l_l = []

    for index in range(len(letters)):
        v = letters[index]
        if v == 'a':
            l_l.append(index)
    print(l_l)


    # Ожидаемый результат: [0, 2, 4, 6]


find_indices()