# import colorgram

# colors = colorgram.extract('Turtle Hirst Painting/OIP.jpg', 20)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import random
import turtle 

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(165, 156, 25), (162, 17, 60), (27, 115, 189), (241, 209, 64), (226, 137, 61), (97, 152, 217), (206, 69, 148), (4, 63, 153), (7, 128, 61), (91, 82, 181), (228, 101, 51)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










#For the screen to exit on click
screen = turtle.Screen()
screen.exitonclick()