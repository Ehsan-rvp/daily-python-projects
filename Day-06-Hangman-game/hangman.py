import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)

word_letter = []

for letter in chosen_word:
    word_letter.append(letter)

word_letter_with_space = " ".join(word_letter)
word_letter_list = []
for i in word_letter_with_space:
    word_letter_list.append(i)
chosen_word_space = "".join(word_letter_with_space)

for letter in range(0, len(word_letter)):
    word_letter[letter] = "_"

blank_word = " ".join(word_letter)
blank_word_list = []

for blank in blank_word:
    blank_word_list.append(blank)

print(logo)
lives = 6
while lives > 0:
    guess_letter = input("Guess a letter: ")
    print("\n"*3)

    if guess_letter in chosen_word:
        if guess_letter in blank_word_list:
            print(f"You've already guessed {guess_letter}")

        for i, v in enumerate(word_letter_list):
            if v == guess_letter:
                blank_word_list[i] = guess_letter

    else:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in word. You lose a life!")
        print(f"you have just {lives} lives.")
        print(stages[lives])

    if lives == 0:
        print("You lose!")
        break

    new_blank_word = "".join(blank_word_list)
    print(new_blank_word)

    if new_blank_word == chosen_word_space:
        print("You win!")
        break

