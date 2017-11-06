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
    window = g.GraphWin()

    drawBrownEye(window, g.Point(90, 100))
    drawBrownEye(window, g.Point(100, 120))

    window.getMouse()

def distBetweenPoints(a, b):
    return math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2)

def drawStars_Gap(gap_One, star_One, gap_Two, star_Two, row):
    for i in range(row):
        print(" " * gap_One, end= "")
        print("*" * star_One, end="")
        print(" " * gap_Two, end="")
        print("*" * star_Two, end="")

def drawLetter_A():
    drawStars_Gap(1, 8, 0, 0, 2)
    drawStars_Gap(0, 2, 6, 2, 2)
    drawStars_Gap(0, 10, 0, 0, 2)
    drawStars_Gap(0, 2, 6, 2, 3)

