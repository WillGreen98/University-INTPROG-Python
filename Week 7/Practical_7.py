import graphics as g
import time
import math, random as rand

#--------------- Week 6 ----------------------#
def drawCircle(window, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(window)


def distanceBetweenPoints(a, b):
    return (math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2))


def drawColouredEye(window, center, radius, colour):
    drawCircle(window, center, radius, "")
    drawCircle(window, center, radius / 2, colour)
    drawCircle(window, center, radius / 4, "black")


def calculateGrade(mark):
    if mark >= 16:
        print('A')
    elif mark >= 12:
        print('B')
    elif mark >= 8:
        print('C')
    elif mark < 8:
        print('F')
    else:
        print('Invalid Input')
#--------------- Week 6 ----------------------#

def trafficLights():
    window = g.GraphWin()

    light_Red = g.Circle(g.Point(100, 50), 20)
    light_Red.setFill("red")
    light_Red.draw(window)

    light_Amber = g.Circle(g.Point(100, 100), 20)
    light_Amber.setFill("black")
    light_Amber.draw(window)

    light_Green = g.Circle(g.Point(100, 150), 20)
    light_Green.setFill("black")
    light_Green.draw(window)

    while True:
        light_Green.setFill("black")
        light_Red.setFill("red")

        time.sleep(1)

        light_Amber.setFill("yellow")
        light_Red.setFill("black")

        time.sleep(1)

        light_Amber.setFill("black")
        light_Green.setFill("green")

        time.sleep(1)

def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def askaName():
    while True:
        name = input("What is your name: ")

        if name.isnumeric():
            print("Invalid input")
        else:
            break

def calculateCourseWork():