__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g
import random as rand

DEBUG = True

colors = ["black", "blue", "green", "yellow", "orange", "red"]

def getInputs_Mercer():
    colours_array = []
    size_col = 0  # setup for colours inputs
    valid_colours = ["red", "green", "blue", "magenta", "cyan", "orange", "brown", "pink"]
    while True:  # Loops until done
        size = input("Please enter the size of the patchwork:")
        # checks if input is a number
        if size.isnumeric():
            if int(size) % 2 == 1:
                if size in ["5", "7", "9", "11"]:
                    size = int(size)
                    break
                else:
                    print("Your Input is not one of the valid options 5, 7, 9, 11")
            else:
                print("Your Input is an even number this is invalid")
        else:
            print("Your Input is not a  number")

    while True:
        colour = input("Please enter the {0} colour: ".format(size_col + 1))
        if hasNumbers(colour):  # checks fir digit in input
            print("Your colour contains number. Invalid Input")

        else:
            if colour in valid_colours:
                if colour not in colours_array:  # checks if colour is already added
                    colours_array.append(colour)
                else:
                    print("You cannot enter the same colour more than once")
            else:
                print("Your colour is not available please try a different one. The valid colours are {0}".format(
                    valid_colours))
        # does size of the colours array for breaking purposes
        size_col = len(colours_array)
        if size_col >= 3:  # checks if enough colours have been entered
            break

    return size, colours_array

def getInput():
    # 5x5 7x7 9x9 11x11
    dimensions = input("Enter grid (N N): ").split()
    di_X = int(dimensions[0])
    di_Y = int(dimensions[1])

    color = input("Enter colors (color 1 colour 1 color 3): ").split()
    col_One = color[0]
    col_Two = color[1]
    col_Three = color[2]

    if col_One and col_Two and col_Three not in colors:
        print("Colour not valid!")
        getInput()

    return dimensions, color

def draw_Patch_Penultimate(window):
    reversed = False

    point_One = g.Point(0, 0)
    point_Two = g.Point(50, 0)
    point_Three = g.Point(50, 50)

    colour = ""

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
    line = g.Line(g.Point(x1, y1), g.Point(x2, y2)).draw(window)
    line.setFill(colour)

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
    window = g.GraphWin("Patch Work", 500, 500)

    #getInput()

    #draw_Patch_Penultimate(window)

    draw_Patch_Final(window, 50, 50, "Red")
    draw_Patch_Final(window, 180, 180, "Black")
    draw_Patch_Final(window, 300, 250, "Green")

    # for rows in range(0, 600, 100):
    #     for cols in range(0, 600, 100):
    #         draw_Patch_Final(window, rows + 100, cols + 100, rand.choice(colors))


    window.getMouse()

if __name__ == '__main__':
    main()