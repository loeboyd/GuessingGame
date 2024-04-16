#Lois Daniels
#CIS261
#GuessingGame
#16APR24

import random

def display_title():
    print("Guess the Number!")
    print()
    
def play_game(limit):
    number = random.randint(1, 10)
    print(f"I am thinking of a number from 1 to {limit}\n.")
    count = 1
    guess = int(input("Your guess?:  "))
    
    while(guess != number):
        if guess < number:
            print("Too low")
            count += 1
        elif guess > number:
            print("Too High")
            count += 1
        guess = int(input("Your Guess?:  "))
    print(f"You guessed it in {count} tries. \n")
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit:"))
        play_game(limit)
        again = input("Would you like to play again? Enter (yes/no)")
        print()
    print("Later!")
    
if __name__ == "__main__":
    main()
    