import random

from guess_art import logo


def guess_number():
    # Display game logo and intro
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Select difficulty level
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Generate random number
    secret_number = random.randint(1, 100)

    # Set attempts based on difficulty
    attempts = 5 if level == "hard" else 10

    def show_attempts(attempts_amount):
        """Return remaining attempts message"""

        # Player loses if attempts reach zero
        if attempts_amount == 0:
            return "You've run out of guesses, you lose!"

        return f"You have {attempts_amount} remaining to guess the number."

    print(show_attempts(attempts))

    # Main game loop
    while attempts != 0:

        # Get player's guess
        user_guess = int(input("\nMake a guess: "))

        # Guess is too high
        if user_guess > secret_number:
            print("Too high!\nGuess again.")
            attempts -= 1
            print(show_attempts(attempts))

        # Guess is too low
        elif user_guess < secret_number:
            print("Too low!\nGuess again.")
            attempts -= 1
            print(show_attempts(attempts))

        # Correct guess
        elif user_guess == secret_number:
            print(f"\nYou got it! The answer was {secret_number}.")
            return


# Start the game
guess_number()
