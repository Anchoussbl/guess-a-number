"""
This is my game "Guess a number"
"""
import random


if __name__ == "__main__":
    your_number = input("Enter a number from 1 to 10: ")
    computer_number = random.randint(1, 10)
    if int(your_number) == computer_number:
        print("You guessed it!")
    else:
        print("You got it wrong!")
        print(f"The number is {computer_number}")
