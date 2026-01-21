def add(n1, n2):
    return n1 + n2


def substruct(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

keys = {
    "+":add,
    "-":substruct,
    "*":multiply,
    "/":divide
}
pick = ""
result = 0.0


while True:

    if pick == 'y':
        first_number = result
    else:
        first_number = float(input("What's the first number?"))


    for key in keys:
        print(key)
    operations = input(f"Pick an operation: ")


    second_number = float(input("What's the next number?"))


    selected_func = keys[operations]
    result = selected_func(first_number,second_number)


    print(f"{first_number} + {second_number} = {result}")

    pick = input(f"Type 'y' to continue calculating with {result}, "
                 f"or type 'n' to start a new calculation: ")

