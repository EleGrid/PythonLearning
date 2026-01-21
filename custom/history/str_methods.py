
def get_letter_by_index(stroka, index):
    print(stroka[index])
    # return stroka[index]

a = get_letter_by_index("1234567890", 7)
print()
# a = str("86678")
# b = 86678
# print(int(a) == b)
# print(name[2])
# print(a.find("7"))

def ffff():
    return "gfgjhfhg"

b = ffff()
print()

#перевести в стринг, пробел вместо с
letters = ['a', 'b', 'c', 'd', 'e', 'f']
final_word = ""

for letter in letters:

    if letter == "c":
        final_word += " "
    else:
        final_word += letter
print(final_word)