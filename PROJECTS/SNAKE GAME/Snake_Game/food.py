from turtle import Turtle
import random

colors = ['red', 'yellow', 'green', 'cyan']
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()  # Initialize the Turtle base class
        # Additional initialization code for the Food class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("black")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)