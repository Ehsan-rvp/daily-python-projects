import random
from turtle import Turtle, Screen

# Control race state
is_race_on = False

# Create screen object
screen = Screen()

# Set screen size
screen.setup(width=500, height=400)

# Ask user for bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# Available turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Store all turtle objects
all_turtles = []

# Starting vertical position
y_position = -100

# Create turtles
for index in range(6):

    # Create turtle object
    new_turtle = Turtle(shape="turtle")

    # Set turtle color
    new_turtle.color(colors[index])

    # Lift pen
    new_turtle.up()

    # Set starting position
    new_turtle.goto(x=-230, y=y_position)

    # Save turtle object in list
    all_turtles.append(new_turtle)

    # Move next turtle downward
    y_position += 35

# Start race if user entered a bet
if user_bet:
    is_race_on = True

# Store winner color
winner_color = ""

# Main race loop
while is_race_on:

    # Move each turtle randomly
    for turtle in all_turtles:

        # Random forward movement
        random_distance = random.randint(0, 10)

        turtle.forward(random_distance)

        # Check finish line
        if turtle.xcor() >= 230:

            # Get winner color
            winner_color += turtle.color()[0]

            # Stop race
            is_race_on = False

# Check user's result
if user_bet == winner_color:
    print(f"You've won! The '{winner_color}' turtle is the winner!")

else:
    print(f"You've lost! The '{winner_color}' turtle is the winner!")

# Keep screen open
screen.exitonclick()
