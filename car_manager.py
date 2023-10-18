from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POSITIONS = []

for i in range(25):
    starting_y = random.randint(-250, 255)
    STARTING_Y_POSITIONS.append(starting_y)

STARTING_X_POSITIONS = []

for i in range(25):
    starting_x = random.randint(310, 910)
    STARTING_X_POSITIONS.append(starting_x)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.create_car()
        self.movement_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=None, stretch_len=2)
        self.setheading(180)
        self.car_color()
        self.goto(random.choice(STARTING_X_POSITIONS), random.choice(STARTING_Y_POSITIONS))

    def move_car(self):
        self.fd(self.movement_speed)

    def car_color(self):
        car_color = random.choice(COLORS)
        self.color(car_color)

    def reset_position(self):
        self.goto(310, random.choice(STARTING_Y_POSITIONS))

    def increase_speed(self):
        self.movement_speed += MOVE_INCREMENT
