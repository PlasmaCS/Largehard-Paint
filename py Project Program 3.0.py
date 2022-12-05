"""
Project Program
Name: Andrew Barbarini, Eric Davis, Bradyn Weatherwax
Date: 11/29/2022
"""

import turtle
from tkinter import *
from turtle import Turtle, Screen
from tkinter import ttk
from tkinter.colorchooser import askcolor

screen = Screen()
canvas = screen.getcanvas()
canvas.create_window(-200, -200)
t = Turtle()
t.speed(-1)
t.pensize(10)
b = "black"
f = DISABLED

def changeColor():
    global b
    a,b = askcolor(title = "Choose Your Fighter")
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

def sFill():
    global f
    f = NORMAL
    t.fillcolor(b)
    t.begin_fill()

def eFill():
    global f
    f = DISABLED
    t.end_fill()
    t.fillcolor("black")
    t.pencolor(b)

def undo():
    for i in range(10):
        t.undo()
    t.pensize(10)

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

def buttonMaker(text, cmd, dis):
    return ttk.Button(canvas.master, text = text, state = dis, command = cmd)
    
def main():
    turtle.listen()

    t.ondrag(drawing)
    turtle.onscreenclick(clickRight)

    changeColor()

    buttonMaker("Pick Color", changeColor, NORMAL).pack()
    buttonMaker("Undo", undo, NORMAL).pack()
    buttonMaker("Clear", clear, NORMAL).pack()
    buttonMaker("Erase", erase, NORMAL).pack()
    buttonMaker("Triangle", triangle, NORMAL).pack()
    buttonMaker("Rectangle", rect, NORMAL).pack()
    buttonMaker("Start Fill", sFill, NORMAL).pack()
    buttonMaker("End Fill", eFill, DISABLED).pack

    screen.mainloop()

if __name__ == "__main__":
    main()
