import random

def choose_dif():
    print("Welcome to the number guessing game!")
    print("I'm thiking about a number between 1 and 100")   
    dif = input("Choose the dificulty. Type 'hard' or 'easy': ").lower()
    if dif == 'hard':
        cant = 5
    elif dif == 'easy':
        cant = 10
    else: 
        print("Write correctly!")
        exit
    print(f"You have {cant} attemps remaining to guess\n")
    return cant

def make_guess(life, num):
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too high.")
        print("Guess again.")
        print(f"You have {life -1} attemps left.\n")
        return life - 1
    elif guess < num:
        print("Too low.")
        print("Guess again.")
        print(f"You have {life - 1 } attemps left.\n")
        return life - 1
    else:
        print(f"You got it! The answer was {num}\n")
        return 0

def game():
    lives = 0
    num = random.randint(1,100)
    lives = choose_dif()
    while(lives > 0):
        lives = make_guess(lives,num)

game()