from turtle import Turtle
from const import ALIGNMENT, FONT, FONT_GAME_OVER, SCREEN_HEIGHT, FILE_PATH


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore_from_file()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, (SCREEN_HEIGHT / 2) - 50)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} | high score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highsore_to_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def get_highscore_from_file(self):
        with open(FILE_PATH, "r") as file:
            high_score = file.read()
            return int(high_score)

    def save_highsore_to_file(self, p_highscore):
        with open(FILE_PATH, "w") as file:
            file.write(str(p_highscore))

    # def game_over(self):
    #     self.goto(0, 0)\
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT_GAME_OVER)
