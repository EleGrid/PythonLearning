import random


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return "Loose"
    elif user_score == 0:
        return "Win"
    elif user_score > 21:
        return "Loose"
    elif computer_score > 21:
        return  "Win"
    elif user_score > computer_score:
        return "Win"
    else:
        return "Loose"


def calc_score(card_list):
    """ Calculate score in your hand
    If you have 2 cards with ace and card qual 10, return 0 - its black jack combination

    :param card_list: player hand
    :return:
    """

    if len(card_list) == 2 and 10 in card_list and 11 in card_list:
        return 0

    elif sum(card_list) > 21:
        try:
            card_list.remove(11)
            card_list.append(1)
        except ValueError:
            pass
    return sum(card_list)

def deal_card():
    """Get 1 random card from deck

    :return:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def game():
    user_card = []
    comp_card = []
    user_card.append(deal_card())
    user_card.append(deal_card())
    user_score = calc_score(user_card)
    print(f"Your score {user_score}")


    comp_card.append(deal_card())
    comp_card.append(deal_card())
    comp_score = calc_score(comp_card)
    print(f"Computer score {comp_score}")

    while True:

        if comp_score == 0 or user_score > 21:
            return "Looose"
        else:
            answer_q = input("Do you want to draw another card. Type 'y' or 'n': ")
            if answer_q == 'y':
                user_card.append(deal_card())
                user_score = calc_score(user_card)
                print(user_score)
            else:
                break

    while comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calc_score(comp_card)

    game_result = compare(user_score, comp_score)
    return game_result

go_on = 'y'
while go_on == 'y':
    print("Start new game")
    final = game()
    print(f"You {final}")

    go_on = input("Do you want to restart the game? Type 'y' or 'no'")