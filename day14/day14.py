#HIGHER OR LOWER

import data14
import random
from os import system

def game():
    first_pick, second_pick = random.choices(data14.data,k=2)
    while (first_pick == second_pick): second_pick = random.choice(data14.data)
    score = 0
    game = True
    while game == True:
        print(f"Compare A: {first_pick["name"]}, a {first_pick["description"].lower()}, from {first_pick["country"]}")
        print(f"Against B: {second_pick["name"]}, a {second_pick["description"].lower()}, from {second_pick["country"]}\n")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if first_pick["follower_count"] > second_pick["follower_count"] and answer == 'a':
            score +=1
            system("clear")
            print(f"You're right! Current score: {score}")
            first_pick = second_pick
            while (first_pick == second_pick): second_pick = random.choice(data14.data)    
            score +=1
            system("clear")
            print(f"You're right! Current score: {score}")
            first_pick = second_pick
            while (first_pick == second_pick): second_pick = random.choice(data14.data)

        else:
            system("clear")
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False
game()