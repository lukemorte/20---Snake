from turtle import Turtle


class Grid(Turtle):

    def __init__(self, screen_width, screen_height, tile_size, grid_color="green"):
        super().__init__()
        self.shape("circle")
        self.color(grid_color)
        self.hideturtle()

        for y in range(-screen_height // 2 - (tile_size // 2), screen_height // 2, tile_size):
            self.penup()
            self.goto(-screen_width // 2, y)
            self.pendown()
            self.goto(screen_width // 2, y)

        for x in range(-screen_width // 2 - (tile_size // 2), screen_width // 2, tile_size):
            self.penup()
            self.goto(x, -screen_height // 2)
            self.pendown()
            self.goto(x, screen_height // 2)
