# Erin Cole
# This File is the main driver for my VIS141A final project.

from tkinter import *
from Lib import random
import time
import Make


# This is the main function for the project.  It creates a narrative in a loop 
# with randomized function calls in order to hightlight the literal stupidity of# computers and the frustration that often gets evoked while using them.
if __name__ == '__main__':
    shortPause = 2
    longPause = 5

    xCoord = 100
    yCoord = 100
    rad = 25

    points = [200, 200, 250, 200, 250, 250, 200, 250]

    #c = Canvas.make()
    #c.mainloop()

    main = Tk()
    w = Canvas(main, width = 750, height = 750)
    w.pack()

    Make.circle(w, xCoord, yCoord, rad)
    
    Make.square(w, points)
    #while 1:

    
    w.mainloop()
