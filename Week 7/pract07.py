#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import time

# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        pass
	# remove the pass and add your code here

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
