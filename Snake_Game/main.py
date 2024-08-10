# Create snake body
# move the snake
# control the snake
# detect collision with food
# create a scoreboard
# detect collision with wall
# detect collision with tail
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

game_is_on = True
score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Eats food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect tail collision
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()