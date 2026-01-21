# Задача 8: Подсчёт длины слов
# Создай список с длинами каждого слова

def count_word_lengths(words:list):
    l_w = []
    for wc in words:
        len_wc = len(wc)
        l_w.append(len_wc)
    print(l_w)

    # Ожидаемый результат: [3, 6, 4, 7]

words = ["кот", "собака", "слон", "муравей"]
count_word_lengths(words)