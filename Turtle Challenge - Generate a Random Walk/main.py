import random
from turtle import Screen, Turtle
import turtle

tim = Turtle()
tim.shape("circle")
turtle.colormode(255)

#colours=["red", "blue", "green", "yellow", "purple",  "pink", "orange", "gray"]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


#For the screen to exit on click
screen = Screen()
screen.exitonclick()