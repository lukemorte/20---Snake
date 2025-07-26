from turtle import Turtle
from const import MOVE_DISTANCE, STARTING_POSITION, DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP


class Snake():

    def __init__(self):
        """
        Snake class constructor
        """
        self.segments: list[Turtle] = []
        self.reset()

    def create(self):
        """
        create basic snake from start_position
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(MOVE_DISTANCE / 20)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        if len(self.segments) > 0:
            [segment.hideturtle() for segment in self.segments]
            self.segments.clear()
        self.create()
        self.head = self.segments[0]
        self.head.color('red')

    def extend(self):
        """
        add new segment at the end of tail
        """
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        """
        move snake by one tile
        """
        # odzadu iteruje všechny segmenty a přemístí každý iterovaný segment na pozici předchozího segmentu
        for i in range(len(self.segments) - 1, 0, -1):
            coords = self.segments[i - 1].position()
            self.segments[i].goto(coords)

        # posune první (head - nultý segment) segment na novou pozici podle aktuálního směru
        self.head.forward(MOVE_DISTANCE)

    # movement methods

    def turn_up(self):
        if self.head.heading() != DIR_DOWN:
            self.head.setheading(DIR_UP)

    def turn_left(self):
        if self.head.heading() != DIR_RIGHT:
            self.head.setheading(DIR_LEFT)

    def turn_down(self):
        if self.head.heading() != DIR_UP:
            self.head.setheading(DIR_DOWN)

    def turn_right(self):
        if self.head.heading() != DIR_LEFT:
            self.head.setheading(DIR_RIGHT)
