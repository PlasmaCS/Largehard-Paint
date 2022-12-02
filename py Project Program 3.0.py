
"""
Project Program
Name: Andrew Barbarini, Eric Davis, Bradyn Weatherwax
Date: 11/29/2022
"""

import turtle, tkinter
from turtle import Turtle, Screen
from tkinter.colorchooser import askcolor
from tkinter import *

screen = Screen()
canvas = screen.getcanvas()
canvas.create_window(-200, -200)
t = Turtle()

def changeColor():
    global b
    a,b = askcolor(title = "Choose Color")
    t.pencolor(b)
    t.pensize(10)

def triangle():
    for i in range(3):
        t.fd(100)
        t.rt(120)
def rect():
    for i in range(4):
        t.fd(100)
        t.rt(90)

def erase():
    t.pencolor("white")
    t.pensize(50)
    
def undo():
    t.undo()

def sFill():
    t.fillcolor(b)
    t.begin_fill()

def eFill():
    t.end_fill()
    t.fillcolor("black")
    t.pencolor(b)

def clear():
    t.clear()

def drawing(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(drawing)

def clickRight(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def buttonMaker(text, cmd):
    tkinter.Button(canvas.master, text = text, bg = "white", command = cmd).pack()

def main():
    turtle.listen()

    t.speed(-1)
    t.pensize(10)
    b = "black"

    t.ondrag(drawing)
    turtle.onscreenclick(clickRight)

    buttonMaker("Pick Color", changeColor)
    buttonMaker("Undo", undo)
    buttonMaker("Clear", clear)
    buttonMaker("Erase", erase)
    buttonMaker("Triangle", triangle)
    buttonMaker("Rectangle", rect)
    buttonMaker("Start Fill", sFill)
    buttonMaker("End Fill", eFill)

    screen.mainloop()

if __name__ == "__main__":
    main()