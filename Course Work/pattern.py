__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g
import numbers

DEBUG = False

valid_colours = ["red", "orange", "green", "blue", "magenta", "cyan", "brown", "pink"]  # Order of Freq

def getInput():
    val_Dimensions = [5, 7, 9, 11]
    colour_Choices = []

    while True:
        dimension = input("Enter dimension: ")

        # Or boring .isnumeric()
        if dimension.__contains__(filter(lambda i: isinstance(i, numbers.Number), val_Dimensions)):
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
        colour = input("Enter colours: ")
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

def draw_Patch_Penultimate(window, pos_x, pos_Y, colour, reversed):
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

            point_One = g.Point(point_One.getX() + 10, point_One.getY())
            point_Two = g.Point(point_Two.getX(), point_Two.getY())
            point_three = g.Point(point_Three.getX(), point_Three.getY() - 10)
    elif reversed == True:
        for i in range(5):
            if i % 2 == 0:
                colour = "White"
            else:
                colour = "Red"
            point_One = g.Point(point_One.getX() - 10, point_One.getY())
            point_Two = g.Point(point_Two.getX(), point_Two.getY())
            point_three = g.Point(point_Three.getX(), point_Three.getY() + 10)


def drawLine(window, x1, y1, x2, y2, colour):
    line = g.Line(g.Point(x1, y1), g.Point(x2, y2)).draw(window).setFill(colour)

def draw_Patch_Final(window, pos_x, pos_y, colour):
    x = pos_x
    y = pos_y

    while x < pos_x + 100 and y < pos_y + 100:
        # TODO Flip Coordinates for reverted pattern
        # If X and Y are different values, pattern diverges
        #Top Left to Bottom Right
        drawLine(window, pos_y, x, (2 * pos_y) + 100 - x, pos_x + 100, colour) # Problem line
        drawLine(window, y, pos_x, pos_y + 100, (2 * pos_x) + 100 - x, colour)

        #Top Right to Bottom Left
        drawLine(window, y, pos_x, pos_y, x, colour)
        drawLine(window, pos_y + 100, x, y, pos_x + 100, colour)

        x += 20
        y += 20

        if DEBUG:
            print("x1: ", pos_y, " y1: ", x, " x2: ", ((2 * pos_y) + 100 - x), " y2: ", (pos_x + 100))

def main():
    x = 0

    if DEBUG:
        window = g.GraphWin("Patch Work", 600, 600)
        # draw_Patch_Penultimate(window, False)

        draw_Patch_Final(window, 50, 50, "red")
        draw_Patch_Final(window, 180, 180, "black")
        draw_Patch_Final(window, 300, 250, "blue")
    else:
        dim, col = getInput()
        window = g.GraphWin("Patch Work", dim * 100, dim * 100)

        for rows in range(0, 600, 100):
            for cols in range(0, 600, 100):
                # draw_Patch_Penultimate(window, rows + 100, cols + 100, col[x], False)
                draw_Patch_Final(window, rows + 100, cols + 100, col[x])
                x += 1
                if x == 3:
                    x = 0

    window.getMouse()

if __name__ == '__main__':
    main()