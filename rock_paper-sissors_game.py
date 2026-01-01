"""This program lets the user play a Rock-Paper-Scissors game against 
the computer, providing the result of each round and allowing the user 
to replay until they choose to quit. """

import random

def game_start():
    while True:
        bot=random.choice(["rock", "paper", "scissors"])
        print("Welcome to rock, paper, scissors game...")
        user=input(f"Enter your choice: ").lower()

        if(user==bot):
            print(f"Equal!!! Computer choice is {bot}")

        elif( user == "rock" and bot == "scissors" ) or \
        ( user == "paper" and bot == "rock" ) or \
        ( user == "scissors" and bot == "paper" ):
            print(f"You Win.... Computer choice is {bot}")

        elif user in ["rock", "paper", "scissors"]:
            print(f"You lose.... Computer choice is {bot}")

        else:
            print("Please enter valid input")
            continue

        replay=input("Do you want to play again ('Yes' or 'No'): ").lower()
        if replay != "yes":
            print("Thank you for playing!")
            break
        
game_start()


