import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ['cyan', 'red']
HEADCOLOR = 'yellow'


class Snake:
    def __init__(self):
        self.segments = []
        self.segments: list[Turtle]  # specify that segments is a list of turtle objects to help autocomplete
        self.create_snake()
        self.head = self.segments[0]  # refers to first segment
        self.head.color(HEADCOLOR)

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move_forward(self):
        for index in range(len(self.segments) - 1, 0, -1):  # step -1 not including first segment
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()

            self.segments[index].goto(x, y)

        self.head.forward(20)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color(COLORS[len(self.segments) % 2])
        new_segment.penup()
        new_segment.setposition(pos)
        self.segments.append(new_segment)  # add to list of segments

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
