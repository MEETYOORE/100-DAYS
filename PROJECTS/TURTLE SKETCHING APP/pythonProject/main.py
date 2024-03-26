from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    cur_heading = tim.heading()
    tim.setheading(cur_heading+10)

def turn_right():
    cur_heading = tim.heading()
    tim.setheading(cur_heading-10)

def north():
    tim.setheading(0)
    tim.forward(10)

def south():
    tim.setheading(90)
    tim.forward(10)

def east():
    tim.setheading(180)
    tim.forward(10)

def west():
    tim.setheading(270)
    tim.forward(10)

def clear():
    tim.setposition(0,0)
    tim.clear()


tim.speed(0)
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
