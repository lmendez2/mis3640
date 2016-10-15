import turtle
from turtle_shape import arc, circle, move, polygon
import math

# 3.1.1

lucky = turtle.Turtle()
lucky.speed(0)

# large circle
circle(lucky, 100)

# 4 triangles here we are printing the four triangles in the assigned different angles
move(lucky, 0, 100)
lucky.setheading(60)
polygon(lucky, 3, 100)
lucky.setheading(150)
polygon(lucky, 3, 100)
lucky.setheading(240)
polygon(lucky, 3, 100)
lucky.setheading(330)
polygon(lucky, 3, 100)


# 4 small circles same thing except with the four different circles 
moving_step = 50 * math.sqrt(3)
small_radius = 50 * math.sqrt(3) / 3

move(lucky, 0, 100 - moving_step)
lucky.setheading(0)
circle(lucky, small_radius)

move(lucky, moving_step, 100)
lucky.setheading(90)
circle(lucky, small_radius)

move(lucky, 0, 100 + moving_step)
lucky.setheading(180)
circle(lucky, small_radius)

move(lucky, -moving_step, 100)
lucky.setheading(270)
circle(lucky, small_radius)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100, 0) # the petals are just connected arcs
flower(bob, 7, 60.0, 60.0)

move(bob, 0, 0)
flower(bob, 10, 40.0, 80.0)




lucky = turtle.Turtle()
lucky.speed(0)

# large circle
circle(lucky, 100)

# two arcs
move(lucky, 0, 100)
lucky.setheading(180)
arc(lucky, 50, 180)

move(lucky, 0, 100)
lucky.setheading(0)
arc(lucky, 50, 180)

# small circles
move(lucky, 0, 50 + 100 / 6)
circle(lucky, 100 / 6)

move(lucky, 0, 150 + 100 / 6)
circle(lucky, 100 / 6)

ef draw_spiral(t, n, length=3, a=0.1, b=0.0002):

    for i in range(n):
        t.fd(length)

bob.hideturtle()



turtle.mainloop()