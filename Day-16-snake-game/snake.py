from turtle import Turtle

# Movement distance
MOVE_DISTANCE = 20

# Starting snake positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Direction angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        # Store snake body segments
        self.segments = []

        # Create initial snake body
        self.create_snake()

        # Store snake head separately for easier access
        self.head = self.segments[0]

    def create_snake(self):
        """Create starting snake body"""

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create and add a new snake segment"""

        new_segment = Turtle("square")

        new_segment.color("white")

        # Disable drawing line
        new_segment.up()

        # Set segment position
        new_segment.goto(position)

        # Save segment
        self.segments.append(new_segment)

    def extend(self):
        """Add new segment to snake tail"""

        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake forward"""

        # Move body segments from tail to head
        for segment_number in range(len(self.segments) - 1, 0, -1):

            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(new_x, new_y)

        # Move head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move snake upward"""

        # Prevent reverse movement
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move snake downward"""

        # Prevent reverse movement
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move snake left"""

        # Prevent reverse movement
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move snake right"""

        # Prevent reverse movement
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


'''
In the first iterate of 'move()' method, start=2(lens of segments), stop=0(the head of segs), step=-1 (means just 2, 1).
Positon of the (last seg(2) - 1) means the seg's position of the one before last seg.
The last seg(2) will goto the seg's position of the one before itself(1).
'''
