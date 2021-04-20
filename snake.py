from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self, color):
        self.segments = []
        self.create_snake(color)
        self.head = self.segments[0]

    def create_snake(self, color):
        for position in STARTING_POSITION:
            self.add_segment(position, color)

    def add_segment(self, position, color):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color(color)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self, color):
        self.add_segment(self.segments[-1].position(), color)

    def reset_snake(self, color):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments = []
        self.create_snake(color)
        self.head = self.segments[0]

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[segment_number - 1].xcor()
            y_position = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(x_position, y_position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)