from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make ur bet", prompt="Bet on a turtle color")

tim = Turtle(shape="turtle")
tim.penup()
tim.setposition(x=-230, y=100)

screen.exitonclick()