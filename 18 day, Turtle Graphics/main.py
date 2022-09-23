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
tim.speed("fastest")
tim.penup()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
tim.forward(-150)

number_of_dots = 120
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


turtle_module.Screen().exitonclick()


