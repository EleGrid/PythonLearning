import random
from random import choice

from game_data import data
from art import logo, vs

def get_persons():
    famous_peoples = random.choices(data, k = 2)
    return famous_peoples

def right_answer(followers_1, followers_2):
    if followers_1 > followers_2:
        return 'a'
    else:
        return 'b'



def game():
    print(logo)
    score = 0
    while True:
        channels = get_persons()
        channel_1 = channels[0]
        channel_2 = channels[1]
        print(f"Compare A: {channel_1['name']}, a {channel_1['description']}, from {channel_1['country']}")
        print(vs)
        print(f"Against B: {channel_2['name']}, a {channel_2['description']}, from {channel_2['country']}")
        right_choice = right_answer(channel_1['follower_count'], channel_2['follower_count'])
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_answer == right_choice:
                score += 1
                print(f"You are right! Current score: {score}")
        else:
                print(f"Sorry, that's wrong. Final score: {score}")
                return



game()


