from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self, color):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(color)
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align= ALIGNMENT, font=FONT)