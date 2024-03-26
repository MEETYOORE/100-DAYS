import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import scoreBoard

WIDTH = 1000
HEIGHT = WIDTH

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)  # turn off the animations

snake = Snake()
food = Food()
scoreboard = scoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    screen.update()
    print(snake.head.pos())

    # detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > WIDTH / 2 - 10:
        game_is_on = False
    elif snake.head.ycor() > HEIGHT / 2 - 40:
        game_is_on = False
    elif snake.head.xcor() < -(WIDTH / 2):
        game_is_on = False
    elif snake.head.ycor() < -(HEIGHT / 2 - 40):
        game_is_on = False

    # detect collision with tail
    # if head collides with any segment in the tail then game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over_message()



scoreboard.game_over_message()
screen.exitonclick()
