import random
from blackjack_art import logo

# Create deck (4 sets of cards)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
random.shuffle(cards)


def get_user_choice():
    # Ask player to hit or stand
    return input("\nType 'y' to get another card, type 'n' to pass: ")


def deal_random_cards(card_amount):
    """Return random cards as a list"""
    return random.sample(cards, card_amount)


def calculate_score(person_cards):
    """Calculate total score, handle Ace (11 → 1 if needed)"""
    sum_scores = sum(person_cards)

    # Adjust Ace value if bust
    if 11 in person_cards and sum_scores > 21:
        for card in person_cards:
            if card == 11:
                sum_scores -= 10

    return sum_scores


def is_blackjack(person_scores):
    # Check if score is exactly 21
    if person_scores == 21:
        return True


def display_result(u_cards, u_scores, c_cards, c_scores, final):
    # Show cards and scores (partial or final)
    if final:
        print(f"Your final hand: {u_cards}, final score: {u_scores}"
              f"\nComputer's final hand: {c_cards}, final score: {c_scores}")
    else:
        print(f"Your cards: {u_cards}, current score: {u_scores}"
              f"\nComputer's first card: {c_cards[0]}")


def start_blackjack():
    print(logo)

    # Initial deal
    should_continue = True
    user_cards = deal_random_cards(2)
    computer_cards = deal_random_cards(2)

    # Calculate scores
    user_scores = calculate_score(user_cards)
    computer_scores = calculate_score(computer_cards)

    # Check blackjack
    user_21 = is_blackjack(user_scores)
    computer_21 = is_blackjack(computer_scores)

    def check_initial_blackjack():
        # Handle instant blackjack cases
        if user_21 and computer_21:
            print("\nPush! it's draw.")
            return True

        elif user_21:
            display_result(user_cards, user_scores, computer_cards, computer_scores, True)
            print("\nWin with Blackjack! 😎")
            return True

        elif computer_21:
            display_result(user_cards, user_scores, computer_cards, computer_scores, True)
            print("\nYou lose with Blackjack! 🥲")
            return True

    first_result = check_initial_blackjack()
    if first_result:
        return

    def add_card_to_hand(person_cards):
        # Add one random card
        person_cards.extend(deal_random_cards(1))

    def handle_game_logic(flag):
        if flag == "hit":
            add_card_to_hand(user_cards)
            print(f"\nUser's cards: {user_cards}, current score: {calculate_score(user_cards)}")

            if calculate_score(user_cards) == 21:
                print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}\n")

                # Computer draws until 17
                while calculate_score(computer_cards) < 17:
                    add_card_to_hand(computer_cards)

                display_result(user_cards, calculate_score(user_cards), computer_cards, calculate_score(computer_cards), True)
                print("\nWin with Blackjack! 😎")
                return True

            elif calculate_score(user_cards) > 21:
                display_result(user_cards, calculate_score(user_cards), computer_cards, calculate_score(computer_cards), True)
                print("\nYou went over. You lose. 🥲")
                return True

        elif flag == "stand":
            print(f"\nComputer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}\n")

            while calculate_score(computer_cards) < 17:
                add_card_to_hand(computer_cards)

            display_result(user_cards, calculate_score(user_cards), computer_cards, calculate_score(computer_cards), True)

            # Compare scores
            if calculate_score(computer_cards) > 21:
                print("\nOpponent went over. You win. 😉")
            elif calculate_score(computer_cards) == 21:
                print("\nYou lose with Blackjack! 🥲")
            elif calculate_score(computer_cards) == calculate_score(user_cards):
                print("\nPush! it's draw.")
            elif calculate_score(user_cards) > calculate_score(computer_cards):
                print("\nYou win. 😉")
            else:
                print("\nYou lose. 🥲")

    # Show initial cards
    display_result(user_cards, calculate_score(user_cards), computer_cards, calculate_score(computer_cards), False)

    # Game loop
    while should_continue:
        user_choice = get_user_choice()

        if user_choice == 'y':
            win = handle_game_logic("hit")
            if win:
                should_continue = False

        elif user_choice == 'n':
            handle_game_logic("stand")
            break


# Main loop
start = True
while start:
    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if again == "y":
        start_blackjack()
    elif again == "n":
        print("\nGoodbye!")
        start = False
    else:
        print("\nError 404. Not found!")
        start = False
