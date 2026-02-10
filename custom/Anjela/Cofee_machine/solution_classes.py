from copy import deepcopy

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

default_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

class CoffeeMachine:
    def __init__(self, resources, menu):
        self._resources = deepcopy(resources)
        self._menu = deepcopy(menu)
        self._power_on = True
        self._profit = 0.0

    def _print_report(self):
        print(f"Water: {self._resources['water']} ml")
        print(f"Milk: {self._resources['milk']} ml")
        print(f"Coffee: {self._resources['coffee']} g")
        print(f"Money: {self._profit}$")

    def _check_ingredients(self, coffee_name: str) -> bool:
        """Check ingredients with resources to continiue"""
        ingredients = MENU[coffee_name]['ingredients']
        for key in ingredients:
            if ingredients[key] <= self._resources[key]:
                pass
            else:
                print(f"Sorry there is not enough {key}")
                return False
        return True

    def _insert_coins(self) -> float:
        print("Please insert coins.")
        q_quantity = int(input(f"How many quarters?: "))
        d_quantity = int(input(f"How many dimes?: "))
        n_quantity = int(input(f"How many nickles?: "))
        p_quantity = int(input(f"How many pennies?: "))
        return q_quantity * 0.25 + d_quantity * 0.1 + n_quantity * 0.05 + p_quantity * 0.01

    def _check_enough_money(self, coffee_name: str, user_money: float) -> bool:
        """Check cost and inserted money"""
        coffee_cost = self._menu[coffee_name]['cost']
        if user_money >= coffee_cost:
            return True
        else:
            return False

    def _count_change(self, coffee_name: str, user_money: float) -> float:
        """change"""
        coffee_cost = self._menu[coffee_name]['cost']
        return round(user_money - coffee_cost, 3)

    def _make_a_coffee(self, coffee_name: str):
        """Take ingredient"""
        ingredients = self._menu[coffee_name]['ingredients']
        for key in ingredients:
            required_ingredient = ingredients[key]
            self._resources[key] = self._resources[key] - required_ingredient
        print(f"Here is your {coffee_name}☕. Enjoy!!!")

    def start_coffee_machine(self):
        while self._power_on:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ")
            if user_choice == "off":
                self._power_on = False
            elif user_choice == "report":
                self._print_report()
            elif user_choice in ['espresso', 'latte', 'cappuccino']:
                enough_ing = self._check_ingredients(coffee_name=user_choice)
                if not enough_ing:
                    continue
                inserted_money = self._insert_coins()
                if not self._check_enough_money(coffee_name=user_choice, user_money=inserted_money):
                    print("Sorry not enough money. Here is your inserted money")
                    continue
                change = self._count_change(coffee_name=user_choice, user_money=inserted_money)
                if change != 0:
                    print(f"Here is your change {change} $")
                self._profit = self._profit + self._menu[user_choice]['cost']
                self._make_a_coffee(coffee_name=user_choice)

coffee_machine = CoffeeMachine(default_resources, MENU)
coffee_machine.start_coffee_machine()