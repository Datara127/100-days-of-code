from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.dir_x = self.dir_y = -1

    def move(self):
        self.goto(self.xcor()+0.25*self.dir_x, self.ycor()+0.25*self.dir_y)

    def reset_pos(self):
        self.goto(0, 0)
        self.dir_x *= 1
        self.dir_y *= 1
