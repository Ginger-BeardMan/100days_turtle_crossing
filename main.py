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
screen.title('Turtle Crossing')

screen.onkeypress(player.move, "Up")

garage = []

game_is_on = True

level.update_scoreboard()

for i in range(40):
    new_car = CarManager()
    garage.append(new_car)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in garage:
        car.move_car()
        if car.xcor() <= -310:
            car.reset_position()

        if player.ycor() >= 275:
            car.increase_speed()

        if player.distance(car) <= 10:
            level.game_over()
            game_is_on = False

    if player.ycor() >= 275:
        level.update_level()

    player.level_start_position()

screen.exitonclick()
