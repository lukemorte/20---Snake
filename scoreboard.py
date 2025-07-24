from turtle import Turtle
from const import ALIGNMENT, FONT, FONT_GAME_OVER, SCREEN_HEIGHT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, (SCREEN_HEIGHT / 2) - 50)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT_GAME_OVER)
