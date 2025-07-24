from turtle import Turtle, Screen
import time

TILE_SIZE = 20

directions = {'up': (0, 1), 'left': (-1, 0), 'down': (0, -1), 'right': (1, 0)}
active_dir = 'right'



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

starting_positions = [(0, 0), (-TILE_SIZE, 0), (-TILE_SIZE * 2, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

segments[0].color('red')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
    screen.update()



# DONE 1: create snake body



# TODO 2: move the snake
# TODO 4: detect collision with food
# TODO 5: create scoreboard
# TODO 6: detect collision with wall
# TODO 7: detect collision with tail










screen.exitonclick()
