import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed(18)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_no):
    for _ in range(int(360/gap_no)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(10)


screen.exitonclick()


