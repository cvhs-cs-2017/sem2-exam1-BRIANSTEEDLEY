"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""

import turtle

turtle = turtle.Turtle()
turtle.speed(0)
x = 100
y = 100
theta = 100
def triangle(x,y,theta):
    for i in range(1):
        turtle.pu()
        turtle.goto(-100,100)
        turtle.pd()
        turtle.forward(x)
        turtle.right(y)
        turtle.forward(theta)
        turtle.goto(-100,100)


triangle(x,y,theta)


"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
