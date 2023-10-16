from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# starting speed
STARTING_MOVE_DISTANCE = 5

# every level the turtle speed increases by:
MOVE_INCREMENT = 10

starting_y = random.randint(-270, 270)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=None, stretch_len=2)
        self.goto(250, starting_y)

    def car_color(self):
        pass

    def car_move(self):
        pass
