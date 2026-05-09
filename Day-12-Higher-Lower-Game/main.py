import random
import sys

from higher_data import data
from higher_art import logo, vs

# Store player's score
SCORES = 0


def get_random_celebrity():
    """Return a random celebrity from dataset"""
    return random.choice(data)


# Select initial celebrities
celebrity_a = get_random_celebrity()
celebrity_b = get_random_celebrity()

# Prevent duplicate comparison
if celebrity_a == celebrity_b:
    celebrity_b = get_random_celebrity()


def get_followers_count(person):
    """Return follower count of a celebrity"""
    return person["follower_count"]


followers_a = get_followers_count(celebrity_a)
followers_b = get_followers_count(celebrity_b)


def compare_followers():
    """Return which celebrity has more followers"""
    if followers_a > followers_b:
        return "A"

    elif followers_b > followers_a:
        return "B"

    else:
        return 0


def format_information(person, label, hint):
    """Return formatted celebrity information"""

    name = ""
    description = ""
    country = ""

    for k, v in person.items():

        if k == "name":
            name += v

        elif k == "description":
            description += v

        elif k == "country":
            country += v

    return f"{label} {hint}: {name}, {description}, from {country}."


def ask_user_choice():
    """Handle user guess and score system"""

    global SCORES

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Correct answer
    if user_choice == compare_followers():

        SCORES += 1

        print(logo)
        print(f"You're right! Current score: {SCORES}\n")

    # Wrong answer
    else:
        print("\n" * 10)
        print(f"Sorry, that's wrong. Final score: {SCORES}")
        return 1


# Generate formatted information text
info_a = format_information(celebrity_a, "Compare", "A")
info_b = format_information(celebrity_b, "Against", "B")


def show_first_round():
    """Display first comparison"""

    print(logo)

    print(info_a)
    print(vs)
    print(info_b)

    if ask_user_choice():
        sys.exit()


# Start first round
show_first_round()

# Main game loop
while True:

    # Swap celebrities
    celebrity_a = celebrity_b

    # Generate new celebrity
    celebrity_b = get_random_celebrity()

    # Prevent duplicates
    while celebrity_a == celebrity_b:
        celebrity_b = get_random_celebrity()

    # Update follower counts
    followers_a = get_followers_count(celebrity_a)
    followers_b = get_followers_count(celebrity_b)

    # Update display info
    info_a = format_information(celebrity_a, "Compare", "A")
    info_b = format_information(celebrity_b, "Against", "B")

    # Show comparison
    print(info_a)
    print(vs)
    print(info_b)

    # End game if player loses
    if ask_user_choice():
        break
