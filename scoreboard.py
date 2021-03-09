from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.create()

    def create(self):
        self.clear()
        self.write(f'Level: {self.score}', align='left', font=FONT)

    def update(self):
        self.score += 1
        self.create()
