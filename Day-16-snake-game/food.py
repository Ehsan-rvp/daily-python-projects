import random as random_generator
from turtle import Turtle


class Food(Turtle):

    def __init__(self):

        # Initialize Turtle class
        super().__init__()

        # Food appearance
        self.shape("circle")

        # Set food size (10x10 pixels)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Disable drawing line
        self.up()

        # Food color
        self.color("DeepPink3")

        # Fastest turtle speed
        self.speed("fastest")

        # Random starting position
        random_x_position = random_generator.randint(-280, 280)
        random_y_position = random_generator.randint(-280, 280)

        self.goto(random_x_position, random_y_position)

    def refresh(self):
        """Move food to a new random position"""

        random_x_position = random_generator.randint(-280, 280)
        random_y_position = random_generator.randint(-280, 280)

        self.goto(random_x_position, random_y_position)
