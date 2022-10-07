from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.current_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(300, randint(-280, 280))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.current_speed)

    def speed_up(self):
        self.current_speed += MOVE_INCREMENT
