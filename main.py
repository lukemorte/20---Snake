from turtle import Screen
from snake import Snake
import time


# code


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


# snake object
snake = Snake()


# key listening
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)


# game logic
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.075)
    snake.move()






screen.exitonclick()

# DONE 1: create snake body
# DONE 2: move the snake

# TODO 4: detect collision with food
# TODO 5: create scoreboard
# TODO 6: detect collision with wall
# TODO 7: detect collision with tail
