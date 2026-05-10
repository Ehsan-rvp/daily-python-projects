from coffee_data import MENU, resources
from coffee_art import logo


def start():
    """Main coffee machine function"""

    should_continue = True

    # Display coffee machine logo
    print(logo)

    while should_continue:

        # Ask user for coffee choice
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino)"
            " Type 'ESP', 'LAT', 'CAP'.\n"
        ).lower()

        # Turn off machine
        if user_choice == "off":
            should_continue = False

        # Display current machine resources
        symbols = ["ml", "ml", "g", "$"]

        if user_choice == "report":

            for idx, ((resource, value), symbol) in enumerate(zip(resources.items(), symbols)):

                if idx == 3:
                    print(f"{resource.title()}: {symbol}{value}")

                else:
                    print(f"{resource.title()}: {value}{symbol}")

        def check_resources():
            """Check if enough resources exist for selected coffee"""

            # Required ingredients
            required_water = MENU[user_choice]["ingredients"]["water"]
            required_milk = MENU[user_choice]["ingredients"]["milk"]
            required_coffee = MENU[user_choice]["ingredients"]["coffee"]

            # Available machine resources
            available_water = resources["water"]
            available_milk = resources["milk"]
            available_coffee = resources["coffee"]

            # Resource validation
            if available_water >= required_water:

                if available_milk >= required_milk:

                    if available_coffee >= required_coffee:
                        return True

                    else:
                        return "Sorry there is not enough coffee."

                else:
                    return "Sorry there is not enough milk."

            else:
                return "Sorry there is not enough water."

        def process_coins():
            """Receive user's coins and calculate total"""

            print("Plz insert coins.")

            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total = quarters + dimes + nickles + pennies

            return total

        def update_resources():
            """Reduce ingredients after making coffee"""

            required_ingredients = []

            # Collect needed ingredient amounts
            for item in MENU[user_choice]["ingredients"].values():
                required_ingredients.append(item)

            # Reduce resources
            for amount, resource in zip(required_ingredients, resources):
                resources[resource] -= amount

        # Coffee selection validation
        if user_choice in ["esp", "lat", "cap"]:

            coffee_cost = MENU[user_choice]["cost"]

            # Check resources
            check_coffee = check_resources()

            if check_coffee:

                # Process payment
                total_money = process_coins()

                # Enough money
                if total_money > coffee_cost:

                    change = total_money - coffee_cost

                    print(f"Here is ${round(change, 2)} in change.")

                    update_resources()

                    resources["money"] += coffee_cost

                    print(f"\nHere is your {user_choice.upper()} ☕ Enjoy!\n")

                # Exact payment
                elif total_money == coffee_cost:

                    update_resources()

                    resources["money"] += coffee_cost

                    print(f"\nHere is your {user_choice.upper()} ☕ Enjoy!\n")

                # Not enough money
                else:
                    print("\nSorry, that's not enough money. Money refunded.\n")

            # Resource error
            else:
                print(check_coffee)

        # Invalid command
        elif user_choice not in ["off", "report"]:
            print("Error 505! try again.")


# Start coffee machine
start()
