from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.start_pos()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def start_pos(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

