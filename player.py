from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.hideturtle()
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=("Arial", 50, "normal"))

    def backtonormal(self):
        self.goto(STARTING_POSITION)