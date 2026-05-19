import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Food collision size
FOOD_SHAPESIZE = 10  # 10x10 pixels

# Create game screen
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Disable automatic screen updates for smoother animation
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Keyboard controls
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Main game loop controller
is_game_running = True

while is_game_running:

    # Refresh screen manually
    screen.update()

    # Control game speed
    time.sleep(0.1)

    # Move snake forward
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= (FOOD_SHAPESIZE + 5):

        # Generate new food position
        food.refresh()

        # Increase snake size
        snake.extend()

        # Update score
        scoreboard.update_score()

    # Detect collision with wall
    if (
        snake.head.xcor() >= 285
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() <= -285
    ):

        is_game_running = False

        scoreboard.game_over()

        # Save high score
        with open("data.txt", mode="w") as score_file:
            score_file.write(f"High Score: {scoreboard.score}")

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Ignore head

        if snake.head.distance(segment) < 10:

            is_game_running = False

            scoreboard.game_over()

            # Save high score
            with open("data.txt", mode="w") as score_file:
                score_file.write(f"High Score: {scoreboard.high_score}")

# Keep screen open
screen.exitonclick()
