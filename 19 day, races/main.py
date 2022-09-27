from turtle import Turtle, Screen
import random


def main():
    screen = Screen()
    screen.setup(width=800, height=600)

    turtles = []
    color = ["red", "yellow", "black", "blue", "green", "pink"]
    stavka = screen.textinput("Turtle races", "Chose color turtle:")
    is_race_on = False
    print(f"Your bet: {stavka}")
    if stavka.lower() in color:
        is_race_on = True
        for i in range(6):
            timik = Turtle(shape="turtle")
            timik.penup()
            timik.color(color[i])
            timik.setx(-350)
            timik.sety(-150 + 50 * i)
            timik.speed("fastest")
            turtles.append(timik)

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 350:
                winner_color = turtle.pencolor()
                if winner_color == stavka.lower():
                    print(f"You Win, the {winner_color} is the winner")
                else:
                    print(f"You lost, the {winner_color} is the winner")
                is_race_on = False
            turtle.forward(random.randint(0, 10))

    screen.exitonclick()


if __name__ == '__main__':
    main()


