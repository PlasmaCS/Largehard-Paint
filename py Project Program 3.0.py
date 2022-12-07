"""
Project Program
Name: Andrew Barbarini, Eric Davis, Bradyn Weatherwax
Date: 11/29/2022
"""

import turtle
from turtle import Turtle, Screen
from tkinter.colorchooser import askcolor
from tkinter import *

screen = Screen()
canvas = screen.getcanvas()
canvas.create_window(-200, -200)
t = Turtle()
b = "black"

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

def sFill():
	t.fillcolor(b)
	t.begin_fill()

def eFill():
	t.end_fill()
	t.fillcolor("black")
	t.pencolor(b)

def clear():
	t.clear()
	
def undo():
	for i in range(10):
		t.undo()
		
def drawing(x, y):
	t.ondrag(None)
	t.setheading(t.towards(x, y))
	t.goto(x, y)
	t.ondrag(drawing)

def clickMove(x, y):
	t.pu()
	t.goto(x, y)
	t.pd()

def buttonMaker(text, cmd):
	Button(canvas.master, text = text, background = "white", command = cmd).pack(side=LEFT)

def main():
	turtle.listen()

	t.speed(-1)
	t.pensize(10)

	t.ondrag(drawing)
	turtle.onscreenclick(clickMove)

	Label(canvas.master).pack(side=LEFT, padx=125)
	buttonMaker("Pick Color", changeColor)
	buttonMaker("Clear", clear)
	buttonMaker("Undo", undo)
	buttonMaker("Erase", erase)
	buttonMaker("Triangle", triangle)
	buttonMaker("Rectangle", rect)
	buttonMaker("Start Fill", sFill)
	buttonMaker("End Fill", eFill)

	screen.mainloop()

if __name__ == "__main__":
	main()
