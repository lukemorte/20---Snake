from turtle import Screen
from snake import Snake
from food import Food
import time


# code


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


# snake object
snake = Snake()
food = Food()


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






screen.exitonclick()

# DONE 1: create snake body
# DONE 2: move the snake
# DONE 3: OOP
# TODO 4: detect collision with food
# TODO 5: create scoreboard
# TODO 6: detect collision with wall
# TODO 7: detect collision with tail
