import random
from hangman_art import stages, logo  # Imports ASCII art stages and logo from hangman_art.py
from hangman_words import word_list    # Imports the list of words from hangman_words.py


# 1. Game Setup
# Select a random word from the word_list for the player to guess.
secret_word = random.choice(word_list)

# Create a list of individual letters from the chosen secret_word.
# This list is used for character-by-character comparison.
secret_word_letters_list = []
for char in secret_word:
    secret_word_letters_list.append(char)

# Create a string representation of the secret word with spaces between letters (e.g., "h a n g m a n").
# This specific format is used for checking the win condition later.
spaced_secret_word_string = " ".join(secret_word_letters_list)

# Convert the spaced secret word string into a list of its characters (e.g., ['h', ' ', 'a', ' ', 'n', ' ', ...]).
# This list is used for indexed access and comparison with the display list.
spaced_secret_word_char_list = []
for char_with_space in spaced_secret_word_string:
    spaced_secret_word_char_list.append(char_with_space)

# Initialize the display for the word with underscores, one for each letter.
# This list will be updated as the player makes correct guesses.
display_word_underscores = []
for char in secret_word: # Populate with underscores corresponding to the length of the secret word.
    display_word_underscores.append("_")

# Convert the list of underscores into a space-separated string (e.g., "_ _ _ _ _ _ _").
# This string is what is initially shown to the player.
current_display_string = " ".join(display_word_underscores)

# Convert the current display string into a list of characters (e.g., ['_', ' ', '_', ' ', ...]).
# This list is directly manipulated to replace underscores with correctly guessed letters.
current_display_char_list = []
for char_in_display in current_display_string:
    current_display_char_list.append(char_in_display)


# 2. Game Start
print(logo) # Display the game's ASCII art logo.
remaining_lives = 6 # Initialize the number of lives the player has.

# Main game loop: Continues as long as the player has lives and the game is not won.
while remaining_lives > 0:
    # Prompt the player to guess a letter.
    # It's recommended to convert the input to lowercase here (e.g., input().lower())
    # to handle both uppercase and lowercase guesses consistently.
    guessed_letter = input("Guess a letter: ")
    print("\n"*3) # Clears the console output for better readability between turns.

    # Check if the guessed letter is present in the secret word.
    if guessed_letter in secret_word:
        # If the letter has already been correctly guessed (and is visible in the display).
        if guessed_letter in current_display_char_list:
            print(f"You've already guessed {guessed_letter}")

        # If the guess is correct and new, update the display list.
        # Iterate through the spaced_secret_word_char_list to find all occurrences of the guessed letter.
        for index, char_in_secret_list in enumerate(spaced_secret_word_char_list):
            if char_in_secret_list == guessed_letter:
                current_display_char_list[index] = guessed_letter # Replace underscore with the correct letter.

    else:
        # If the guess is incorrect, deduct a life.
        remaining_lives -= 1
        print(f"You guessed {guessed_letter}, which is not in the word. You lose a life!")
        print(f"You have just {remaining_lives} lives.")
        # Display the hangman ASCII art corresponding to the current number of remaining lives.
        print(stages[remaining_lives])

    # Check for loss condition: if no lives are left.
    if remaining_lives == 0:
        print("You lose! The word was:", secret_word)
        break # Exit the game loop immediately.

    # Display the current state of the word (correctly guessed letters and underscores).
    # Join the list of characters back into a string for printing.
    updated_display_string = "".join(current_display_char_list)
    print(updated_display_string)

    # Check for win condition: if all underscores have been replaced by letters.
    # This is checked by comparing the updated display string (with spaces) to the original spaced secret word string.
    if updated_display_string == spaced_secret_word_string:
        print("You win! You guessed the word!")
        break # Exit the game loop immediately.
