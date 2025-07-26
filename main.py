from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from grid import Grid
import time
from const import SCREEN_WIDTH, SCREEN_HEIGHT, MOVE_DISTANCE, GRID_COLOR


# screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# snake objects

snake = Snake()
food = Food()
grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, MOVE_DISTANCE, GRID_COLOR)
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
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    w = float((SCREEN_WIDTH - (MOVE_DISTANCE * 2)) / 2)
    h = float((SCREEN_HEIGHT - (MOVE_DISTANCE * 2)) / 2)
    if snake.head.xcor() > w or snake.head.xcor() < -w or snake.head.ycor() > h or snake.head.ycor() < -h:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
