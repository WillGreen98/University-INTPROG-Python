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

def drawBrownEye_NoPoint(window, centre, radius):
    drawBrownEye(window, centre, radius, "white")
    drawBrownEye(window, centre, radius / 2, "brown")
    drawBrownEye(window, centre, radius / 4, "black")


def drawBrownEyes_Pair(window, centre, radius):
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

def drawBrownEyes_Two_Pairs():
    window = g.GraphWin("4 Eyes", 1000, 1000)

    for i in range(4):
        coord_Left = window.getMouse()
        coord_Right = coord_Left.getX() + radius

        radius = distBetweenPoints(coord_Left, window.getMouse())
        drawBrownEye_NoPoint(window, coord_Left, radius)
        drawBrownEye_NoPoint(window, g.Point(coord_Left.getY(), coord_Right),
                             radius)
        window.getMouse()

def displayTextWithSpaces(window, text, size, pos):
    text = text.replace("", " ")
    text_Display = g.Text(pos, text).draw(window).setSize(size)

def constructVisionChart():
    window = g.GraphWin("Chart", 400, 400)

    font_Sizes = [30, 25, 20, 15, 10, 5]
    dx = 100
    dy = 50

    for size in font_Sizes: