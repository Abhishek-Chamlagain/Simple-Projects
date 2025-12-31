import random

class Guess_game:
    def __init__(self, num, bot):
        self.num=num
        self.bot=bot

    def check(self):
        larger= self.bot+((self.bot*20)/100)
        smaller= self.bot-((self.bot*20)/100)

        if(self.num>self.bot):
            if(self.num>larger):
                print("Your number is too big! Take a smaller guess")
            else:
                print("Your number is big! Try again")
        
        elif(self.num<self.bot):
            if(self.num<smaller):
                print("Your number is too small! Take a bigger guess")
            else:
                print("Your number is small! Try again")
        
        else:
            print("You won the game!!!")
            return True



print("Welcome to guess number game!!!")
bot=random.randint(1, 100)
attempts = 0
while True:
    num=input("Enter guessed number (1 to 100) or Quit(Q): ").upper()

    if(num=="Q"):
        print("Thank you for playing game!!!")
        break

    try:
        num = int(num)
    except ValueError:
        print("Please enter a valid number")
        continue

    if (num<0 or num >100):
        print("Enter valid number between 1 to 100: ")
        continue

    game=Guess_game(num, bot)
    result=game.check()
    attempts += 1
    if result:
        print("Attempts:", attempts)
        print("----Game Over----")
        break