from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 340)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 32, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Finall score: {self.score}", align="center", font=("Arial", 32, "normal"))
