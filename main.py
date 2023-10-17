import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
level = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkeypress(player.move, "Up")

garage = []

game_is_on = True

level.update_scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    if player.ycor() >= 275:
        level.update_level()

    player.next_level()

screen.exitonclick()
