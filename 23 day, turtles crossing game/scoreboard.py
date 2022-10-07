from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.current_level = 1
        self.ht()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.current_level}", align="Left", font=FONT)

    def update_lvl(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="Left", font=FONT)

    def lvl_up(self):
        self.current_level += 1
