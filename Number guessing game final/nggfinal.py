from random import randint
from art import logo
EASY_TURNS = 10
HARD_TURNS = 5


def check_answer(guess, answer, turns):
    if guess < answer:
        print("Too low")
        return turns -1
    elif guess > answer:
        print("Too high")
        return turns -1
    else:
        print("You guessed it right")
def set_difficulty():
    turns_level = input("chose an difficulty level, easy or hard: ")
    if turns_level == "easy":
        return EASY_TURNS
    elif  turns_level == "hard":
        return HARD_TURNS





def game():
    print(logo)
    print("Welcome to the number guessing game")
    print("Im thinking of a number between 1 and 100")
    answer = randint(1,100)
    # print(f"psst, the number is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} turns remaining to guess the number")

        guess = int(input("Enter a number between 1 and 100: " ))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"You've ran out of turns, the answer is {answer}")
            return
        elif guess != answer:
            print("guess again: ")

game()





