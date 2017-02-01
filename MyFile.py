def bob(n):
    n = n + 10
    return(n)

import turtle
turtle = turtle.Turtle()
Anyturtle = 100
l = 90
w = 150
def DrawRectangle(Anyturtle,l,w):
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
    turtle.left(l)
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
DrawRectangle(Anyturtle,l,w)
