import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main_func():
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.delay(0)

    game_is_on = True
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            scoreboard.score += 1
            scoreboard.refresh()
            food.refresh()
            snake.extend()

        if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
            game_is_on = False

        for segment in snake.snake:
            if snake.head.distance(segment) < 10 and segment != snake.head:
                game_is_on = False

    else:
        screen.clearscreen()
        screen.bgcolor("black")
        scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main_func()