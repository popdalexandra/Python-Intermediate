import random
from turtle import Screen, Turtle
import turtle

tim = Turtle()
tim.shape("arrow")
turtle.colormode(255)
tim.pensize(2)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spin(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spin(5)

#For the screen to exit on click
screen = Screen()
screen.exitonclick()