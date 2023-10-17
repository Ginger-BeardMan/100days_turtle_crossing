from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.level_score = 1
        # self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level_score}", align='center', font=FONT)

    def update_level(self):
        self.level_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
