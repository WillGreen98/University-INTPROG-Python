#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

import graphics as g
import math

def distBetweenPoints(a, b):
    return math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2)

def drawCircle(win, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawColouredEye(win, centre, radius, colour):
    pass

