from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-210, 250)
        self.show_score()

    def show_score(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.show_score()
