import random

def printl(result):
    print(result)
    print(f"Your choice: {choices[choice_1]}")
    print(f"Computer choice: {choices[choice_2]}")

choices = ["rock","paper","scissors"]
choice_1 = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
choice_2 = random.randint(0,2)

if choice_1 == choice_2:
    printl("Draw!")
elif choice_1 == (choice_2 + 1):
    printl("You won!")
elif choice_1 > 2:
    print("Out of range, you lost!")
else: 
    printl("You lost!")





