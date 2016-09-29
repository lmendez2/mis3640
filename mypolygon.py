import turtle
''''
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

''''

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


''''
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
''''
''''
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

''''
def polygon(t, length, n):  
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


lucky = turtle.Turtle()
polygon(lucky, 100, 12)

lauren = turtle.Turtle()
polygon(lauren, 200, 5)


turtle.mainloop()