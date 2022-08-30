import random
from art import logo
from clear import clear

def secret_number():
    """Generates the number the user is guessing."""
    return random.randint(1, 100)

def number_check(input, randnum, levelnum, times):
    """Checks to see if the player guessed the right number."""
    if input > randnum and times < levelnum:
        return "\nToo high, try again!"
    elif input < randnum and times < levelnum:
        return "\nToo low, try again!"
    elif input == randnum:
        return "\nYou guessed it!"
    elif times == levelnum:
        return "\nGame over!"

def difficulty_runner(cont, times, levelnum, randnum):
    """The repeating part of the game that changes the number of allowed itterations based on difficulty level."""
    while cont and times < levelnum:
        guess = int(input("Guess a number between 1 and 100: "))
        times += 1
        print(number_check(guess, randnum, levelnum, times))
        if number_check(guess, randnum, levelnum, times) == "\nYou guessed it!":
            cont = False    
        elif times == levelnum:
            print(f"The number was {randnum}.")
            cont = False
    
    
def guess_the_number():
    """Game of Guess the Number"""
    print(logo)
    keep_going = True
    times = 0
    num = secret_number()
    
    difficulty = input("Easy or hard? ").lower()
    
    if difficulty == "easy":
        difficulty_runner(keep_going, times, 10, num)
        
    elif difficulty == "hard":
        difficulty_runner(keep_going, times, 5, num)

    again = input("Did you want to play again? Yes/No\n").lower()
    
    if again == "yes":
        clear()
        guess_the_number()
    else:
        clear()
        print("Thanks for playing!")

guess_the_number()
