import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("LimeGreen")
# tim.right(90)


def random_color():
    """ Give a random color (rbg values) """
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# -------------------- Draw a Square ------------------------------

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# -------------------- Draw a dashed line ----------------------------

# for i in range(15):
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()


# ------------------- Draw a triangle, square, pentagon upto decagon  --------------

for i in range(3, 11):
    angle = 360/i
    tim.color(random.choice(colors))
    for j in range(i):
        tim.forward(100)        # Sides should be 100 in length, mentioned in question
        tim.right(angle)

# --------------------- Draw a Random Walk ---------------------------------------

# heading = [0, 90, 180, 270]
#
# for i in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(heading))
#     tim.speed(10)
#     tim.pensize(10)
#     tim.forward(30)

# ----------------------Draw a Spirograph -------------------------------------

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for c in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(20)

# ------------------------------------------------------------------------------

screen = Screen()
screen.exitonclick()
