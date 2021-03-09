import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
inc = 1
total = []
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
num = 0
screen.listen()
screen.onkey(key='Up', fun=player.move)
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car = CarManager()
    total.append(car)
    time.sleep(1)
    for i in total:
        i.move()
        if i.distance(player) < 20 or player.distance(i) < 30:
            game_is_on = False
            player.reset()

    if player.ycor() > 278:
        player.backtonormal()
        car.update()
        scoreboard.update()


screen.exitonclick()




