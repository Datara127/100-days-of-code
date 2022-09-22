import turtle as turtle_module
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("faster")
tim.penup()
number_of_dots = 100
for _ in range(20):
    tim.dot(20, random_color())
    tim.forward(50)

turtle_module.Screen().exitonclick()


