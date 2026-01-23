from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report(coffee_money: float):
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {coffee_money}$")


def check_ingredients(coffee_name: str) -> bool:
    """Check ingredients with resources to continiue"""
    ingredients = MENU[coffee_name]['ingredients']
    for key in ingredients:
        if ingredients[key] <= resources[key]:
            pass
        else:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def insert_coins() -> float:
    print("Please insert coins.")
    q_quantity =int(input(f"How many quarters?: "))
    d_quantity =int(input(f"How many dimes?: "))
    n_quantity =int(input(f"How many nickles?: "))
    p_quantity =int(input(f"How many pennies?: "))
    return q_quantity * 0.25 + d_quantity * 0.1 + n_quantity * 0.05 + p_quantity * 0.01

def check_enough_money(coffee_name: str, user_money: float) -> bool:
    """Check cost and inserted money"""
    coffee_cost = MENU[coffee_name]['cost']
    if user_money >= coffee_cost:
        return True
    else:
        return False

def count_change(coffee_name: str, user_money: float) -> float:
    """change"""
    coffee_cost = MENU[coffee_name]['cost']
    return round(user_money - coffee_cost, 3)

def make_a_coffee(coffee_name: str):
    """Take ingredient"""
    ingredients = MENU[coffee_name]['ingredients']
    for key in ingredients:
        required_ingredient = ingredients[key]
        resources[key] = resources[key] - required_ingredient
    print(f"Here is your {coffee_name}☕. Enjoy!!!")



def start_coffee_machine():
    power_on = True
    profit = 0.0
    while power_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            power_on = False
        elif user_choice == "report":
            print_report(coffee_money=profit)
        elif user_choice in ['espresso','latte', 'cappuccino']:
            enough_ing = check_ingredients(coffee_name=user_choice)
            if not enough_ing:
                continue
            inserted_money = insert_coins()
            if not check_enough_money(coffee_name=user_choice, user_money=inserted_money):
                print("Sorry not enough money. Here is your inserted money")
                continue
            change = count_change(coffee_name=user_choice, user_money=inserted_money)
            if change != 0:
                print(f"Here is your {change} $")
            make_a_coffee(coffee_name=user_choice)



start_coffee_machine()
