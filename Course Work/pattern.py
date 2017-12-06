__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g

valid_colours = ["red", "orange", "green", "blue", "magenta", "cyan", "brown", "pink"]  # PINK ISN'T A COLOUR!!!

def getInput():
    val_Dimensions = [5, 7, 9, 11]
    colour_Choices = []

    while True:
        dimension = input("Enter dimension: ")

        if dimension.isnumeric():
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

def drawPolygon(window, colour, p1, p2, p3):
    poly = g.Polygon(p1, p2, p3)
    poly.setOutline(colour)
    poly.setFill(colour)
    poly.draw(window)

def colour_Picker(colour_In, colour):
    if colour == colour_In:
        colour = "white"
    else:
        colour = colour_In

    return colour

def draw_Patch_Penultimate(window, pos, colour_In):
    p1 = g.Point(pos.getX() + 50, pos.getY() + 50)
    p2 = g.Point(pos.getX() + 50, pos.getY() + 100)
    p3 = g.Point(pos.getX(), pos.getY() + 100)
    p4 = g.Point(pos.getX(), pos.getY() + 50)
    p5 = g.Point(pos.getX(), pos.getY())
    p6 = g.Point(pos.getX() + 50, pos.getY())
    p7 = g.Point(pos.getX() + 100, pos.getY())
    p8 = g.Point(pos.getX() + 100, pos.getY() + 50)
    p9 = g.Point(pos.getX() + 100, pos.getY() + 100)

    colour = colour_In
    for i in range(8):
        pos_Increment = 0
        if i == 0:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p5.getX(), p5.getY() + pos_Increment), g.Point(p1.getX() - pos_Increment, p1.getY()), p4)
                pos_Increment += 10
        elif i == 1:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p5.getX() + pos_Increment, p5.getY()), g.Point(p1.getX(), p1.getY() - pos_Increment), p6)
                pos_Increment += 10
        elif i == 2:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, p6, g.Point(p7.getX() - pos_Increment, p7.getY()), g.Point(p1.getX(), p1.getY() - pos_Increment))
                pos_Increment += 10
        elif i == 3:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p7.getX(), p7.getY() + pos_Increment), g.Point(p1.getX() + pos_Increment, p1.getY()), p8)
                pos_Increment += 10
        elif i == 4:
            colour = "white"
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p3.getX(), p3.getY() - pos_Increment), g.Point(p1.getX() - pos_Increment, p1.getY()), p4)
                pos_Increment += 10
        elif i == 5:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p3.getX() + pos_Increment, p3.getY()), g.Point(p1.getX(), p1.getY() + pos_Increment), p2)
                pos_Increment += 10
        elif i == 6:
            colour = colour_In
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, p8, g.Point(p1.getX() + pos_Increment, p1.getY()), g.Point(p9.getX(), p9.getY() - pos_Increment))
                pos_Increment += 10
        elif i == 7:
            for j in range(5):
                colour = colour_Picker(colour_In, colour)
                drawPolygon(window, colour, g.Point(p9.getX() - pos_Increment, p9.getY()), g.Point(p1.getX(), p1.getY() + pos_Increment), p2)
                pos_Increment += 10


def drawLine(window, pos_X, pos_Y, colour):
    line = g.Line(pos_X, pos_Y).draw(window).setFill(colour)

def draw_Patch_Final(window, pos_X, pos_Y, colour):
    for i in range(0, 100, 20):
        drawLine(window, g.Point(pos_X + i, pos_Y), g.Point(pos_X + 100, pos_Y + 100 - i), colour)
        drawLine(window, g.Point(pos_X, pos_Y + i), g.Point(pos_X + 100 - i, pos_Y + 100), colour)
        drawLine(window, g.Point(pos_X + i, pos_Y + 100), g.Point(pos_X + 100, pos_Y + i), colour)
        drawLine(window, g.Point(pos_X, pos_Y + 100 - i), g.Point(pos_X + 100 - i, pos_Y), colour)

def main():
    x = 0

    dim, col_Array = getInput()
    window = g.GraphWin("Patch Work", dim * 100, dim * 100)

    for columns in range(0, window.getHeight(), 100):
        for rows in range(0, window.getWidth(), 100):
            if rows <= 299 and columns >= window.getWidth() - 300:
                draw_Patch_Final(window, rows, columns, col_Array[x])
            else:
                draw_Patch_Penultimate(window, g.Point(rows, columns), col_Array[x])
            x += 1
            if x == 3:
                x = 0

    window.getMouse()

if __name__ == '__main__':
    main()
