from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from const import SCREEN_WIDTH, SCREEN_HEIGHT


# code


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


# snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# key listening
screen.listen()
screen.onkeypress(key="Up", fun=snake.turn_up)
screen.onkeypress(key="Left", fun=snake.turn_left)
screen.onkeypress(key="Down", fun=snake.turn_down)
screen.onkeypress(key="Right", fun=snake.turn_right)


# game logic
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.075)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()




screen.exitonclick()

# DONE 1: create snake body
# DONE 2: move the snake
# DONE 3: OOP
# DONE 4: detect collision with food
# DONE 5: create scoreboard

# TODO 6: detect collision with wall
# TODO 7: detect collision with tail
