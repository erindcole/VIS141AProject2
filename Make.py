# Erin Cole
# This file creates all the needed components and containers for the project.

from tkinter import *

def mainWindow(h = 750, w = 750):

    main = Tk()
    w = Canvas(main, width = w, height = h)
    w.pack()

    w.mainloop()

def circle(canvas, x, y, r):
    c = canvas.create_oval(x-r, y-r, x+r, y+r)
    return c

def square(canvas, points):
    s = canvas.create_polygon(points)
    return s
