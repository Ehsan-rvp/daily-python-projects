import random
from turtle import Turtle, Screen
import turtle

# Color palette for the painting
color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165),
    (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208),
    (168, 99, 102)
]

# Enable RGB color mode
turtle.colormode(255)

# Create turtle object
painting_turtle = Turtle()

# Set drawing speed
painting_turtle.speed(10)

# Hide turtle cursor
painting_turtle.hideturtle()

# Starting vertical position
y_position = -250

# Move turtle to starting position
painting_turtle.up()
painting_turtle.goto(-250, y_position)

# Draw painting dots
for _ in range(90):

    # Draw first dot
    painting_turtle.down()
    painting_turtle.dot(30, random.choice(color_list))

    # Move forward
    painting_turtle.up()
    painting_turtle.fd(50)

    # Draw next dot
    painting_turtle.down()
    painting_turtle.dot(30, random.choice(color_list))

    # Move to next row if edge reached
    if painting_turtle.xcor() >= 200:

        painting_turtle.up()

        y_position += 50

        painting_turtle.goto(-250, y_position)

# Create screen object
screen = Screen()

# Keep window open until click
screen.exitonclick()
