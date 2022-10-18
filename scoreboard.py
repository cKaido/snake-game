from msilib.schema import Font
from turtle import Turtle
FONT = ('Times New Roman', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score} ', move=False, align='center',
                   font=('Times New Roman', 18, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(f'Score: {self.score} ', move=False, align='center',
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
