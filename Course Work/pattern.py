__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g

val_Dimensions = [5, 7, 9, 11]

valid_colours = ["red", "orange", "green", "blue", "magenta", "cyan", "brown", "pink"]  # PINK ISN'T A COLOUR!!!
colour_Choices = []

def getInput():
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
            print("Invalid input, your inputs must be one of {0}".format(valid_colours))
        if len(colour_Choices) >= 3:
            break

    return dimension, colour_Choices

def draw_Polygon(window, point_One, point_Two, point_Three, colour):
    # Faster render time than: poly = g.Polygon(point_One, point_Two, point_Three).draw(window).setFill(colour)
    poly = g.Polygon(point_One, point_Two, point_Three)
    poly.setFill(colour)
    poly.setOutline(colour)
    poly.draw(window)

def colour_Picker(current_Colour, colour):
    if colour == current_Colour:
        colour = "white"
    else:
        colour = current_Colour

    return colour

def draw_Patch_Penultimate(window, pos_X, pos_Y, current_Colour):
    mid = g.Point(pos_X + 50, pos_Y + 50)
    mid_Bottom = g.Point(pos_X + 50, pos_Y + 100)
    bottom_Left = g.Point(pos_X, pos_Y + 100)
    mid_Left = g.Point(pos_X, pos_Y + 50)
    top_Left = g.Point(pos_X, pos_Y)
    mid_Top = g.Point(pos_X + 50, pos_Y)
    top_Right = g.Point(pos_X + 100, pos_Y)
    mid_Right = g.Point(pos_X + 100, pos_Y + 50)
    bottom_Right = g.Point(pos_X + 100, pos_Y + 100)

    colour = current_Colour
    for quadrant in range(8):
        pos_Increment = 0
        if quadrant == 0:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(top_Left.getX(), top_Left.getY() + pos_Increment), g.Point(mid.getX() - pos_Increment, mid.getY()), mid_Left, colour)
                pos_Increment += 10
        elif quadrant == 1:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(top_Left.getX() + pos_Increment, top_Left.getY()), g.Point(mid.getX(), mid.getY() - pos_Increment), mid_Top, colour)
                pos_Increment += 10
        elif quadrant == 2:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, mid_Top, g.Point(top_Right.getX() - pos_Increment, top_Right.getY()), g.Point(mid.getX(), mid.getY() - pos_Increment), colour)
                pos_Increment += 10
        elif quadrant == 3:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(top_Right.getX(), top_Right.getY() + pos_Increment), g.Point(mid.getX() + pos_Increment, mid.getY()), mid_Right, colour)
                pos_Increment += 10
        elif quadrant == 4:
            colour = "white"
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(bottom_Left.getX(), bottom_Left.getY() - pos_Increment), g.Point(mid.getX() - pos_Increment, mid.getY()), mid_Left, colour)
                pos_Increment += 10
        elif quadrant == 5:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(bottom_Left.getX() + pos_Increment, bottom_Left.getY()), g.Point(mid.getX(), mid.getY() + pos_Increment), mid_Bottom, colour)
                pos_Increment += 10
        elif quadrant == 6:
            colour = current_Colour
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, mid_Right, g.Point(mid.getX() + pos_Increment, mid.getY()), g.Point(bottom_Right.getX(), bottom_Right.getY() - pos_Increment), colour)
                pos_Increment += 10
        elif quadrant == 7:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                draw_Polygon(window, g.Point(bottom_Right.getX() - pos_Increment, bottom_Right.getY()), g.Point(mid.getX(), mid.getY() + pos_Increment), mid_Bottom, colour)
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
                draw_Patch_Penultimate(window, rows, columns, col_Array[x])
            x += 1
            if x == 3:
                x = 0

    window.getMouse()

if __name__ == '__main__':
    main()
