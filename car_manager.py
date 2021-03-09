from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
cars = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.MOVE_INCREMENT = 30
        self.create()

    def create(self):
        self.speed(self.MOVE_INCREMENT)
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2.5)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-240, 240))

    def move(self):
        new_x = self.xcor()
        new_x -= self.MOVE_INCREMENT
        self.goto(new_x, self.ycor())

    def update(self):
        self.MOVE_INCREMENT *= 2



