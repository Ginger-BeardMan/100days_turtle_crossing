import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()

level = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    player.next_level()

    # not working
    # if player.ycor() >= 280:
    #     level.update_level()
