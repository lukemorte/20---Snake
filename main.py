from turtle import Turtle, Screen
import time


# vars


TILE_SIZE = 20

directions = {'up': (0, 1), 'left': (-1, 0), 'down': (0, -1), 'right': (1, 0)}
active_dir = 'right'


# def


def turn_up():    
    segments[0].setheading(90)


def turn_left():
    segments[0].setheading(180)


def turn_down():
    segments[0].setheading(270)


def turn_right():
    segments[0].setheading(0)


# code


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()
screen.onkey(key="w", fun=turn_up)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=turn_down)
screen.onkey(key="d", fun=turn_right)

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
    screen.update()
    time.sleep(0.1)

    segments[0].forward(TILE_SIZE)

    previous_seg = segments[0]

    for i in range(1, len(segments)):
        coords = starting_positions[i - 1]
        segments[i].goto(coords)

    for i, segment in enumerate(segments):
        starting_positions[i] = segment.position()





# DONE 1: create snake body
# DONE 2: move the snake

# TODO 4: detect collision with food
# TODO 5: create scoreboard
# TODO 6: detect collision with wall
# TODO 7: detect collision with tail









screen.exitonclick()
