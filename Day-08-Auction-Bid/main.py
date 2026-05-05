from bid_art import logo

# Display program logo
print(logo)
print("Welcome to the secret auction program.")

should_continue = True

# Track highest bid and winner name
max_bid = 0
max_name = ""

while should_continue:
    # Get bidder information
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    # Store current bid in a dictionary
    auction_bid = dict(name=name, bid=bid)

    # Check if current bid is the highest so far
    if auction_bid["bid"] > max_bid:
        max_bid = auction_bid["bid"]
        max_name = auction_bid["name"]

    # Ask if there are more bidders
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if bidders == "yes" or bidders == 'y':
        # Clear screen simulation (hide previous bids)
        print('\n'*10)
        continue
    else:
        break

# Final result display
print('\n'*6)
print(f"The winner is {max_name} with a bid of ${max_bid}.")
