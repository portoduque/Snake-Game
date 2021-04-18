from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from colors import random_color, colors_dictionary
import time

# Set Color
primary_color = random_color()
secondary_color = colors_dictionary[primary_color]

# Set screen
screen = Screen()
screen.bgcolor(primary_color)
screen.title("My Snake Game")
screen.setup(width=600, height=600)

# Turn off animation
screen.tracer(0)

# Create snake body
snake = Snake(secondary_color)


# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Create Food
food = Food(secondary_color)

# Create a scoreboard
score = Scoreboard(secondary_color)

game_is_on = True
while game_is_on:
    # Update Screen
    screen.update()
    time.sleep(0.1)

    # Move Snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend_snake(secondary_color)
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()


screen.exitonclick()
