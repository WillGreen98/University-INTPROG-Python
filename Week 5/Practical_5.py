from graphics import *
import math

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    window = GraphWin()
    # Add your code here

# For exercise 5
def drawBrownEye(win, centre, radius):
    pass
    # Remove pass and add your code her
