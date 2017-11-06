import graphics as g
import math

def areaOfCircle(radius):
    return math.pi * (radius ** 2)

def circumferenceOfCircle(radius):
    return 2 * math.pi * radius

def areaOfCircle(radius):
    return math.pi * radius ** 2

def circleInfo():
    radius = float(input("Enter for radis: "))
    print("Area: ", areaOfCircle(radius), "\n"
          "Circumference: ", circumferenceOfCircle(radius))

def drawCircle(window, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(window)

def drawStars(height, width):
    for i in range(height):
        print("*" * width)

def drawLetter_E():
    drawStars(8, 3)
    drawStars(2, 3)
    drawStars(6, 3)
    drawStars(2, 3)
    drawStars(8, 3)

def drawBrownEye(window, centre, radius):
    drawBrownEye(window, g.Point(centre, 100), radius, "white")
    drawBrownEye(window, g.Point(centre, 100), radius / 2, "brown")
    drawBrownEye(window, g.Point(centre, 100), radius / 4, "black")


def drawPairBrownEyes(window, centre, radius):
    drawBrownEye(window, g.Point(90, 100))
    drawBrownEye(window, g.Point(100, 120))



