from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# starting speed
STARTING_MOVE_DISTANCE = 5

# every level the turtle speed increases by:
MOVE_INCREMENT = 10

STARTING_Y_POSITIONS = []

for i in range(25):
    starting_y = random.randint(-270, 270)
    STARTING_Y_POSITIONS.append(starting_y)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=None, stretch_len=2)
        self.setheading(180)
        # adjust xcor after everything is working so that the car starts off-screen
        self.goto(250, random.choice(STARTING_Y_POSITIONS))
        self.car_color()

    def car_color(self):
        car_color = random.choice(COLORS)
        self.color(car_color)

    def car_move(self):
        self.fd(5)
