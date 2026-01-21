# Задача 11: Преобразование регистра
# Преобразуй все слова в нижний регистр

def change_case():
    words = ["Hello", "WORLD", "PyThOn", "code"]
    under = []
    for reg in words:
      w = reg.lower()
      under.append(w)
    print(under)

    # Ожидаемый результат: ["hello", "world", "python", "code"]


change_case()