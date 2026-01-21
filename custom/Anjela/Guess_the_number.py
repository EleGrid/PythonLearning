import random


def print_logo():
    logo = r"""
      ___________                        _________                      __  .__    .__                 
    \__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
      |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
      |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
      |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
              \/     |__|        \/          \/             \/     \/          \/        \//_____/   

    """
    print(logo)

def choice_level() -> int:
    easy_level = 10
    hard_level = 5
    answer = input("Choose difficulty. Type 'easy' or 'hard': ")
    if answer == 'easy':
        return easy_level
    elif answer == 'hard':
        return hard_level
    else:
        raise ValueError("Wrong answer!")

def make_a_guess() -> int:
    chosen_number = int(input("Make a guess: " ))
    return chosen_number

def compare(secret_n, user_n):
    if user_n < secret_n:
        print("Too low.")
        return False
    elif user_n >secret_n:
        print("Too high.")
        return False
    else:
        return True

def game():
    print_logo()
    print("Welcome to the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = choice_level()
    secret_number = random.randint(1, 100)


    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        user_number = make_a_guess()
        result = compare(secret_number, user_number)
        if result == True:
            print(f"You got it! The answer was {user_number}")
            return
        else:
            print("Guess again!")
            attempts -= 1

    print("You lose!")

ask_user = "y"

while ask_user == 'y':
    game()
    ask_user = input("Do you want to restart the game? Type y\\n ")