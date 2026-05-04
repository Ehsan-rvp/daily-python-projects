from caesar_cipher_art import logo

# List of lowercase alphabet letters
alphabet = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

# Display ASCII art logo
print(logo)


def cipher_ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    max_alpha = len(alphabet)  # Total number of letters (26)

    # Characters that should NOT be changed
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               ' ', '@', '!', '.', '#', '-',
               '_', '(', ')']

    # Normalize shift to stay within alphabet range
    shift_amount %= 26

    # Reverse shift for decoding
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        # Keep symbols, spaces, and numbers unchanged
        if char in symbols:
            end_text += char
            continue

        # Find new position after shifting
        find_index_char = (alphabet.index(char)) + shift_amount

        # Handle wrap-around (e.g., z -> a)
        if find_index_char >= max_alpha:
            find_index_char -= max_alpha

        # Get shifted character
        shifted_char = alphabet[find_index_char]
        end_text += shifted_char

    # Output result
    print(f"The {cipher_direction}d text is: {end_text}")


# Control loop to keep program running
should_continue = True
while should_continue:
    # Ask user for operation type
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Get user message and convert to lowercase
    text = input("Type your message:\n").lower()

    # Get shift value
    shift = int(input("Type the shift number:\n"))

    # Call cipher function
    cipher_ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask user if they want to run again
    restart = input("Type 'yes' if you want go again. Otherwise type 'no'.\n").lower()

    if restart == "no" or restart == 'n':
        should_continue = False
        print("Goodbye!")
