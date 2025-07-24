from turtle import Turtle


class Snake():

    def __init__(self, tile_size):
        """
        Snake class constructor
        """
        self.TILE_SIZE = tile_size
        self.segments = []
        starting_positions = [(0, 0), (-self.TILE_SIZE, 0), (-self.TILE_SIZE * 2, 0)]        

        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

        self.segments[0].color('red')

    def move(self):
        """
        move snake by one tile
        """
        # odzadu iteruje všechny segmenty a přemístí každý iterovaný segment na pozici předchozího segmentu
        for i in range(len(self.segments) - 1, 0, -1):
            coords = self.segments[i - 1].position()
            self.segments[i].goto(coords)

        # posune první (head - nultý segment) segment na novou pozici podle aktuálního směru
        self.segments[0].forward(self.TILE_SIZE)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_down(self):
        self.segments[0].setheading(270)

    def turn_right(self):
        self.segments[0].setheading(0)
