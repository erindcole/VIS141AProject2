# Erin Cole
# This File is the main driver for my VIS141A final project.

from tkinter import *
from Lib import random
import time
import sys
import Make


# This is the main function for the project.  It creates a narrative in a loop 
# with randomized function calls in order to hightlight the literal stupidity of
# computers and the frustration that often gets evoked while using them.
if __name__ == '__main__':
    shortPause = 2
    longPause = 5

    canvasWidth = 600
    canvasHeight = 600
    rad = 25
    side = 50

    main = Tk()
    w = Canvas(main, width = canvasWidth, height = canvasHeight)
    w.pack()

    
    circle = Make.circle(w, canvasWidth, canvasHeight, rad)
   
    square = Make.square(w, canvasWidth, canvasHeight, side)
    
    while True:
        time.sleep(.75)
        Make.move(w, canvasWidth, canvasHeight, circle, rad*2)
        w.update()
    
    w.mainloop()

    
