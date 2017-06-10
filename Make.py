# Erin Cole
# This file creates all the needed components and containers for the project.

from tkinter import *
from Lib import random



def circle(canvas, canvasWidth, canvasHeight, r):
    x = random.randint(r+1, canvasWidth-r-1)
    y = random.randint(r+1, canvasHeight-r-1)
    c = canvas.create_oval(x-r, y-r, x+r, y+r)
    return c

def square(canvas, canvasWidth, canvasHeight, side):
    x = random.randint(side+1, canvasWidth-side-1)
    y = random.randint(side+1, canvasHeight-side-1)
    points = [x, y, x+side, y, x+side, y+side, x, y+side]
    s = canvas.create_polygon(points)
    return s

def move(item, canvas, x, y):
    if x%2 == 0:
        canvas.coords(item, x-rad, y-rad, x+rad, y+rad)
    else:
        canvas.coords(item, x+rad, y+rad, x-rad, y-rad)

