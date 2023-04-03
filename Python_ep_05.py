from random import randint
import os

LIFE_HARD = 5
LIFE_EASY = 10
number = randint(1,100)

def life():
    if input("Choose difficulty. Type 'easy' or 'hard' : ") == 'easy':
        return LIFE_EASY
    else:
        return LIFE_HARD

def check(lifes):
    ask = int(input("Guess number : "))
    if ask > number:
        print("Too high")
        return lifes - 1
    elif ask < number:
        print("Too low")
        return lifes - 1
    else:
        print(f"That's right, The anwer is {number}")
        return lifes - 1000

def game():
    os.system('cls')
    game_over = False
    lifes = life()
    while not game_over:
        if lifes <= 0:
            game_over = True
        else:
            print('==========')
            print(f"Your life is {lifes}.")
            lifes = check(lifes)

game()