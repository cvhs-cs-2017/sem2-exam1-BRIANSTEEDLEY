"""Create a Turtle Program that will draw a 3-dimensional cube"""





"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
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
