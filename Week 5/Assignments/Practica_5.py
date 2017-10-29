import math
import graphics as g

def areaOfCircle(radius):
    return math.pi * radius ** 2

def circum_Of_Circle(radius):
    return 2 * math.pi * radius

def circle_Info():
    radius = int(input("Enter value for radius: "))
    print("Area = ", areaOfCircle(radius), " circumference = ", circum_Of_Circle(radius))

def drawCircle(window, centre, radius, color):
    circle = g.Circle(centre, radius)
    circle.setFill(color)
    circle.setWidth(2)
    circle.draw(window)

def drawBrownEyeInCentre(win, centre, radius):
    window = win



def drawBrownEye(win, centre, radius):
    pass