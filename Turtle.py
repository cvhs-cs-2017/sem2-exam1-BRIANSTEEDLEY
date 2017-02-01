"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
turtle = turtle.Turtle()
m = 90
n = 90
def square(m,n):
    turtle.forward(m)
    turtle.left(n)
    turtle.forward(m)
    turtle.left(n)
    turtle.forward(m)
    turtle.left(n)
    turtle.forward(m)
    turtle.left(n)
square(m,n)
import turtle

o = 90
p = 90
def square(o,p):
    turtle.pu()
    turtle.goto(-100,20)
    turtle.pd()
    turtle.forward(o)
    turtle.left(p)
    turtle.forward(o)
    turtle.left(p)
    turtle.forward(o)
    turtle.left(p)
    turtle.forward(o)
    turtle.left(p)
square(o,p)








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
