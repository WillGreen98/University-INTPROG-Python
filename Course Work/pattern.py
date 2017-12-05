__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g

DEBUG = False

valid_colours = ["red", "orange", "green", "blue", "magenta", "cyan", "brown", "pink"]  # Order of Freq

def getInput():
    val_Dimensions = [5, 7, 9, 11]
    colour_Choices = []

    while True:
        dimension = input("Enter dimension: ")

        if dimension.isnumeric(): #__contains__(filter(lambda i: isinstance(i, numbers.Number), val_Dimensions)):
            dimension = int(dimension)
            if dimension % 2 == 1:
                if dimension in val_Dimensions:
                    break
                else:
                    print("Value not a valid digit")
            else:
                print("Value not even, must be {0}".format(val_Dimensions))
        else:
            print("Only Numbers!")

    while True:
        colour = input("Enter colour: ")

        if colour in valid_colours:
            if colour not in colour_Choices:
                colour_Choices.append(colour)
            else:
                print("You cannot use the same colour twice")
        else:
            print("Invalid input your inputs must be one of {0}".format(valid_colours))
        if len(colour_Choices) >= 3:
            break

    return dimension, colour_Choices

def draw_Patch_Penultimate(window, pos_X, pos_Y, colour, reversed):
    colour = ""

    point_One = g.Point(0, 0)
    point_Two = g.Point(50, 0)
    point_Three = g.Point(50, 50)

    poly = g.Polygon(point_One, point_Two, point_Three)
    poly.setFill(colour)
    poly.setOutline(colour)
    poly.draw(window)

    if reversed == False:
        for i in range(5):
            if i % 2 == 0:
                colour = "Red"
            else:
                colour = "White"

            point_One = g.Point(pos_X + 10, pos_Y)
            point_Two = g.Point(pos_X, pos_Y)
            point_three = g.Point(pos_X, pos_Y - 10)
    elif reversed == True:
        for i in range(5):
            if i % 2 == 0:
                colour = "White"
            else:
                colour = "Red"
            point_One = g.Point(point_One.getX() - 10, point_One.getY())
            point_Two = g.Point(point_Two.getX(), point_Two.getY())
            point_three = g.Point(point_Three.getX(), point_Three.getY() + 10)


def drawLine(window, pos_X, pos_Y, colour):
    line = g.Line(pos_X, pos_Y).draw(window).setFill(colour)

def draw_Patch_Final(window, x, y, colour):
    for i in range(0, 100, 20):
        drawLine(window, g.Point(x + i, y), g.Point(x + 100, y + 100 - i), colour)
        drawLine(window, g.Point(x, y + i), g.Point(x + 100 - i, y + 100), colour)
        drawLine(window, g.Point(x + i, y + 100), g.Point(x + 100, y + i), colour)
        drawLine(window, g.Point(x, y + 100 - i), g.Point(x + 100 - i, y), colour)

def main():
    x = 0
    cols_Counter = 0
    rows_Counter = 0

    if DEBUG:
        window = g.GraphWin("Patch Work")
        #draw_Patch_Penultimate(window, 200, 200, "red", False)

        draw_Patch_Final(window, 50, 50, "red")
        draw_Patch_Final(window, 180, 180, "black")
        draw_Patch_Final(window, 300, 250, "blue")
    else:
        dim, col = getInput()
        window = g.GraphWin("Patch Work", dim * 100, dim * 100)

        for cols in range(0, window.getHeight(), 100):
            for rows in range(0, window.getWidth(), 100):
                # draw_Patch_Penultimate(window, rows + 100, cols + 100, col[x], False)
                draw_Patch_Final(window, rows, cols, col[x])

                x += 1
                if x == 3:
                    x = 0

    window.getMouse()

if __name__ == '__main__':
    main()
