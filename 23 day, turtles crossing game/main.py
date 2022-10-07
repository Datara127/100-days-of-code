import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

speedik = Player()
score = Scoreboard()
car_manager = CarManager()
screen.onkeypress(speedik.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if speedik.is_at_finish_line():
        score.lvl_up()
        score.update_lvl()
        car_manager.speed_up()

    for car in car_manager.cars:
        if speedik.distance(car) < 20:
            game_is_on = False

screen.exitonclick()