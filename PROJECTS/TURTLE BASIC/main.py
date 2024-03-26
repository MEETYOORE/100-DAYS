import turtle
from turtle import Turtle, Screen
import random


def delay(time=1):
    for i in range(time * 10000000):
        pass


colors = ["red", "green", "blue", "black", "cyan", "purple", "CornflowerBlue", "DarkOrchid", "IndianRed", "SlateGray", "SeaGreen"]


def draw(x, y, side, points, t):
    pos = (x, y)

    t.penup()
    t.setposition(pos)
    t.pendown()
    t.color(random.choice(colors))
    for i in range(points):
        t.forward(side)
        t.right(360 / points)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

def random_walk(t):
    directions = (0, 90, 180, 270)
    turtle.colormode(255)  # color mode rgb values
    t.pensize(15)
    t.speed(0)

    while True:
        t.setheading(random.choice(directions))
        t.color(random_color())
        t.forward(30)


def draw_circle(t):
    turtle.colormode(255)
    t.speed(0)
    t.circle(150)

    t.right(5)
    while t.heading() != 0:
        t.color(random_color())
        t.circle(150)
        t.right(5)



my_turtle = Turtle()
draw_circle(my_turtle)

screen = Screen()
screen.exitonclick()