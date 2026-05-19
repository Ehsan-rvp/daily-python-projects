from turtle import Turtle

# Text alignment
ALIGNMENT = "center"

# Font style
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):

        # Initialize Turtle class
        super().__init__()

        # Current game score
        self.score = 0

        # Read saved high score
        with open("data.txt") as score_file:
            self.high_score = int(score_file.read().split()[-1])

        # Hide turtle cursor
        self.hideturtle()

        # Lift pen
        self.up()

        # Set text color
        self.color("white")

        # Set scoreboard position
        self.goto(0, 260)

        # Display score
        self.update_scoreboard()

    def update_scoreboard(self):
        """Display current score and high score"""

        self.clear()

        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def update_score(self):
        """Increase score after eating food"""

        self.score += 1

        # Update high score if needed
        if self.score > self.high_score:
            self.high_score = self.score

        self.update_scoreboard()

    def game_over(self):
        """Display game over message"""

        self.goto(0, 0)

        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=FONT
        )
