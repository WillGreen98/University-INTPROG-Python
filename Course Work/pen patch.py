import graphics as g

window = g.GraphWin("Test Pen Patch")

test_colour = input("enter colour: ")

def draw_Patch_Penultimate(window, pos_X, pos_Y, colour, reversed):
    point_One = g.Point(0, 0)
    point_Two = g.Point(50, 0)
    point_Three = g.Point(50, 50)

    if reversed == False:
        for i in range(5):
            if i % 2 == 0:
                colour = test_colour
            else:
                colour = "white"

            point_One = g.Point(pos_X + 10, pos_Y)
            point_Two = g.Point(pos_X, pos_Y)
            point_three = g.Point(pos_X, pos_Y - 10)

            poly = g.Polygon(point_One, point_Two, point_Three).draw(window).setFill(test_colour)
    elif reversed == True:
        for i in range(5):
            if i % 2 == 1:
                colour = "white"
            else:
                colour = test_colour

            point_One = g.Point(pos_X - 10, pos_Y)
            point_Two = g.Point(pos_X, pos_Y)
            point_three = g.Point(pos_X, pos_Y + 10)

            poly = g.Polygon(point_One, point_Two, point_Three).draw(window).setFill(test_colour)

draw_Patch_Penultimate(window, 0, 0, test_colour, True)

window.getMouse()