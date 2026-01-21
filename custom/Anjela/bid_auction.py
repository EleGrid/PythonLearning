logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
# Ask user and loop
question = 'yes'
while question == 'yes':
    name = input("What is your name?")
    bid = int(input("What is your bid?:  $"))
    question = input("Are there any other bidders? Type 'yes' or 'no'")

# сравниваем ставки
    if name not in bids:
        bids[name] = bid
    elif bids[name] < bid:
        bids[name] = bid

# Выводим победителя
def print_winner(bids: dict):
    w_name = ""
    w_bid = 0
    for name_b, bid_b in bids.items():
        if bid_b > w_bid:
            w_bid = bid_b
            w_name = name_b

    print(f"The winner is {w_name} with a bid of ${w_bid}. ")


print_winner(bids)