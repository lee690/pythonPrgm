# Import the 'random' module
import random

# Display a welcome message for the Guess the Number game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Initialize a variable to track if the user has guessed the correct number
isGuessRight = False

# Loop until the user guesses the correct number
while isGuessRight != True:
    # Ask the user to input their guess
    guess = input("Guess a number between 1 and 10:")

    # Check if the user's guess matches the randomly generated number
    if int(guess) == number:
        # If the guess is correct, congratulate the user and end the game
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        # If the guess is incorrect, provide feedback and allow the user to try again
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
