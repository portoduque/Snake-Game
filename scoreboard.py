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
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}     High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

