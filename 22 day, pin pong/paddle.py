from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.goto(position)
        self.turtlesize(5, 1)
        self.color("white")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)