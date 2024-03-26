from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = ("center")

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("cyan")
        self.score = 0
        self.goto(0, 420)
        self.write(f"Score is: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score is: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over_message(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ☠️", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -25)
        self.write(f"Score is: {self.score}", align="center", font=("Arial", 24, "normal"))
