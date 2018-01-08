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
    drawBrownEye(window, g.Point(centre, 100), radius, "White")
    drawBrownEye(window, g.Point(centre, 100), radius / 2, "Brown")
    drawBrownEye(window, g.Point(centre, 100), radius / 4, "Black")

def drawBrownEye_NoPoint(window, centre, radius):
    drawBrownEye(window, centre, radius, "White")
    drawBrownEye(window, centre, radius / 2, "Brown")
    drawBrownEye(window, centre, radius / 4, "Black")


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
        usr_In = g.Entry(g.Point(40, 40), 10).draw(window)

        window.getMouse()

        displayTextWithSpaces(window, usr_In.getText(), size,
                              g.Point(dx, dy))

        dx -= 10
        dy += 30
    window.getMouse()

def drawStickFigure(window, size, pos):

    coord_X = pos.getX()
    coord_Y = pos.getY()

    head = g.Circle(g.Point(100, 60), 20).draw(window)
    body = g.Line(g.Point(100, 80), g.Point(100, 120)).draw(window)

    left_Arm = g.Line(g.Point(80, 80), g.Point(100, 90)).draw(window)
    right_Arm = g.Line(g.Point(120, 80), g.Point(100, 90)).draw(window)

    left_Leg = g.Line(g.Point(100, 120), g.Point(80, 140)).draw(window)
    right_Leg = g.Line(g.Point(100, 120), g.Point(120, 140)).draw(window)

    window.getMouse()

def drawStickFigure_Family():
    window = g.GraphWin("It da Peeeps", 400, 400)
    drawStickFigure(window, 40, g.Point(100, 100))