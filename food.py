from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape("turtle")
        self.refresh()

    def refresh(self):
        x_position = random.randint(-270, 275)
        y_position = random.randint(-275, 270)
        self.goto(x_position, y_position)
