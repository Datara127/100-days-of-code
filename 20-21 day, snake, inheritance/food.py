from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x, random_y = randint(-350, 350), randint(-350, 350)
        self.goto(random_x, random_y)