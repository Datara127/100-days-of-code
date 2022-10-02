from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


def main_func():
    screen = Screen()
    screen.tracer(0)
    paddle_1, paddle_2 = Paddle((350, 0)), Paddle((-350, 0))
    ball = Ball()
    score = Scoreboard()

    screen.setup(800, 600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.listen()
    screen.onkeypress(paddle_2.go_up, "Up")
    screen.onkeypress(paddle_2.go_down, "Down")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()

        if ball.ycor() >= 287 or ball.ycor() <= -280:
            ball.dir_y *= -1
        if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
            ball.dir_x *= -1
        if ball.xcor() >= 387:
            ball.reset_pos()
            score.l_point()
            time.sleep(0.25)
        if ball.xcor() <= -380:
            ball.reset_pos()
            score.r_point()
            time.sleep(0.25)

    screen.exitonclick()


if __name__ == '__main__':
    main_func()

