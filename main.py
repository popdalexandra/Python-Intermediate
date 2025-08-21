import random
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("pink")

colours=["red", "blue", "green", "yellow", "purple",  "pink", "orange", "gray"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


#For the screen to exit on click
screen = Screen()
screen.exitonclick()
