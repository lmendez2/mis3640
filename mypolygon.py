import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)



def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)



def square(t, length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    #print(t)

def polygon(t, length, n):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    #print(t)


def polygon(t, length, n):  
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

import math
def circle (t, r):
    circumference = 2 * math.pi *r
    n = 50 
    length = circumference / n
    polygon(t, length, n)

lucky = turtle.Turtle()
#polygon(lucky, 100, 12)
print(lucky.position())
lucky.setx(-200)
lucky.sety(-200)
print(lucky.position())
circle(lucky, 80)

lauren = turtle.Turtle()
polygon(lauren, 200, 5)


turtle.mainloop()