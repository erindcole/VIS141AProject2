# Erin Cole
# This file creates all the needed components and containers for the project.

from tkinter import *
from Lib import random
import sys


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

def move(canvas, canvasWidth, canvasHeight, item, itemLength):
    dx = random.randint(1, canvasWidth/2)
    dy = random.randint(1, canvasHeight/2)
    new_dx = 0.0
    new_dy = 0.0
    offset = itemLength + 1
    print(canvas.coords(item))
    coordsList = canvas.coords(item)
    for i in range(len(coordsList)):
        if i % 2 == 0:
            if dx + coordsList[i] > canvasWidth - offset: 
                new_dx = dx * -1  
                print('here')
            elif coordsList[i] - dy < offset:
                new_dx = dx
        else:
            if dy + coordsList[i] > canvasHeight - offset:
                new_dy = dy * -1    
            elif coordsList[i] - dy < offset:
                new_dy = dy
    if new_dx == 0.0:
        new_dx = dx
    if new_dy == 0.0:
        new_dy = dy
    
    canvas.move(item, new_dx, new_dy) 
    sys.stdout.flush()
    
