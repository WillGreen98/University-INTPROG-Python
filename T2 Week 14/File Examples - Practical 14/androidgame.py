from graphics import *
from android import Android
from BabyAndroid import BabyAndroid

import math

def main():
    playArea, and1, and2 = drawScene()
    playGame(playArea, and1, and2)

def drawScene():

    window = GraphWin("Android", 500, 500)
    window.setCoords(0, 0, 1, 1)
    androidNo1 = Android(window, "green", 0.25, 0.5, 1.2, 0.001)
    androidNo2 = BabyAndroid(window, "red", 0.75, 0.5)

    return window, androidNo1, androidNo2

def playGame(win, android1, android2):
    
    message = Text(Point(0.5, 0.5), "")
    message.setSize(20)

    
    lost = False

    while not lost:
        key = win.checkKey()
        if key == "Left":
            android1.moveAndroid("Left")
        elif key == "Right":
            android1.moveAndroid("Right")
        elif key == "Down":
            android1.moveAndroid("Down")
        elif key == "Up":
            android1.moveAndroid("Up")
        elif key == "d":
            android2.moveAndroid("Left")
        elif key == "f":
            android2.moveAndroid("Right")
        elif key == "c":
            android2.moveAndroid("Up")
        elif key == "r":
            android2.moveAndroid("Down")
            
        android1Centre = android1.getHeadCentre()
        android2Centre = android2.getHeadCentre()
        
        if distanceBetweenPoints(android1Centre, android2Centre) > 0.4:
            android2.cry()
        else:
            android2.stopCrying()
        
        if android1Centre.getX() < 0 or android1Centre.getX() > 1 or \
           android1Centre.getY() < 0 or android1Centre.getY() > 1:
            lost = True
            message.setText("Android 1 Hit the Wall!")
        elif android2Centre.getX() < 0 or android2Centre.getX() > 1 or \
           android2Centre.getY() < 0 or android2Centre.getY() > 1:
            lost = True
            message.setText("Android 2 Hit the Wall!")

    message.draw(win)

def distanceBetweenPoints(point1, point2):
    return math.sqrt(((point2.getX()-point1.getX())**2) + ((point2.getY()-point1.getY())**2))

main()

