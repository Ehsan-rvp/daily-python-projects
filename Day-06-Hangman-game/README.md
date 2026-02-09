#  Hangman 💀 (Day 06)

A classic text-based Hangman game implemented in Python. The player guesses letters to uncover a hidden word, with a limited number of incorrect guesses before the "hangman" is complete. This project demonstrates modular programming by separating game logic, ASCII art, and word lists into different Python files.

---

### ❓ What does this project do?
This project is an interactive console game that:
*   Randomly selects a secret word from an extensive list.
*   Displays the current state of the word with underscores for unguessed letters.
*   Takes letter guesses from the player.
*   Provides visual feedback (ASCII art of the gallows) for incorrect guesses.
*   Tracks the number of remaining lives.
*   Checks for win/loss conditions and announces the game's outcome.
*   Handles already guessed letters to prevent penalizing the player twice.

---

### Technologies Used
*   **`random` module**: For selecting a random word and shuffling.
*   **Modular Design**: Utilizes separate Python files (`hangman_art.py`, `hangman_words.py`) for better code organization and reusability.

---

### 📘 Learning Outcomes
In this project, I practiced:
*   **String and List Manipulation**: Working with characters, joining/splitting strings, and modifying lists.
*   **`import` Statements**: Learning how to import specific variables and lists from other Python files.
*   **`while` Loops**: Implementing a game loop that continues until win/loss conditions are met.
*   **Conditional Logic (`if-elif-else`)**: Handling various game states, guess validations, and outcome determinations.
*   **Randomness**: Using `random.choice()` for word selection.
*   **User Input**: Taking and processing single-letter guesses.
*   **Game State Management**: Tracking lives, guessed letters, and the progress of the hidden word.
*   **Code Organization**: Structuring a project across multiple Python modules.
