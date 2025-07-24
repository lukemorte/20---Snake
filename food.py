from turtle import Turtle
import random
from const import FOOD_SIZE_KOEF, MOVE_DISTANCE, PADDING, SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(FOOD_SIZE_KOEF)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_tiles = int(((SCREEN_WIDTH / 2) / MOVE_DISTANCE) - PADDING)
        y_tiles = int(((SCREEN_HEIGHT / 2) / MOVE_DISTANCE) - PADDING)
        random_x = random.randint(-x_tiles, x_tiles)
        random_y = random.randint(-y_tiles, y_tiles)
        self.goto(random_x * MOVE_DISTANCE, random_y * MOVE_DISTANCE)
