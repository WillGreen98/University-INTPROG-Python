# in-class demo illustrating the use of functions

from graphics import *

def drawRectangle(win, p1, p2, colour):
    rect = Rectangle(p1, p2)
    rect.setOutline(colour)
    rect.setFill(colour)
    rect.draw(win)
    
def makeFlagWindow(title, width, col1, col2, col3):
    win = GraphWin(title, width, 2 * width / 3)
    win.setCoords(0,0,3,1)
    drawRectangle(win, Point(0,0), Point(1,1), col1)
    drawRectangle(win, Point(1,0), Point(2,1), col2)
    drawRectangle(win, Point(2,0), Point(3,1), col3)
    
def main():
    makeFlagWindow("France", 300, "blue", "white", "red")
    makeFlagWindow("Italy", 400, "green", "white", "red")
    makeFlagWindow("Belgium", 250, "black", "yellow", "red")
    makeFlagWindow("Ireland", 300, "green", "white", "orange")
    
main()
