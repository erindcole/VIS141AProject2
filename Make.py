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

def move(canvas, canvasWidth, canvasHeight, item, x, y):
    randVal = random.random() 
    print(canvas.coord(item)
    #if canvas.coords(item)[1] > canvasWidth or canvas.coords(item)[1] < 25:
    #    canvas.move(item, canvasWidth/2, canvasHeight/2) 
    
    #if canvas.coords(item)[2] > canvasHeight or canvas.coords(item)[2] < 25:
    #    canvas.move(item, canvasWidth/2, canvasHeight/2) 
    
    
    #if canvas.coords(item)[3] > canvasWidth or canvas.coords(item)[3] < 25:
    #    canvas.move(item, canvasWidth/2, canvasHeight/2) 
    
    #if canvas.coords(item)[0] > canvasHeight or canvas.coords(item)[0] < 25:
     #   canvas.move(item, canvasWidth/2, canvasHeight/2) 
 
    
    
    #if randVal > .75:
    #    canvas.move(item, x, y)
    #elif randVal > .5:
    #    canvas.move(item, x, -y)
    #elif randVal > .25:
    #    canvas.move(item, -x, y)
    #else:
    #    canvas.move(item, -x, -y)
    
    sys.stdout.flush()
    
