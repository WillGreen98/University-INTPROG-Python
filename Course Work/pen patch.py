import graphics as g

window = g.GraphWin("patch test")

def unwrapper(func, args):
    func(*args)

def draw_Polygon(window, point_One, point_Two, point_Three, colour):
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
    pos_Increment = 0

    poly_List = {
        draw_Polygon(window, g.Point(top_Left.getX(), top_Left.getY() + pos_Increment), g.Point(mid.getX() - pos_Increment, mid.getY()), mid_Left, colour),
        draw_Polygon(window, g.Point(top_Left.getX() + pos_Increment, top_Left.getY()), g.Point(mid.getX(), mid.getY() - pos_Increment), mid_Top, colour),
        draw_Polygon(window, mid_Top, g.Point(top_Right.getX() - pos_Increment, top_Right.getY()), g.Point(mid.getX(), mid.getY() - pos_Increment), colour),
        draw_Polygon(window, g.Point(top_Right.getX(), top_Right.getY() + pos_Increment), g.Point(mid.getX() + pos_Increment, mid.getY()), mid_Right, colour),
        draw_Polygon(window, g.Point(bottom_Left.getX(), bottom_Left.getY() - pos_Increment), g.Point(mid.getX() - pos_Increment, mid.getY()), mid_Left, colour),
        draw_Polygon(window, g.Point(bottom_Left.getX() + pos_Increment, bottom_Left.getY()), g.Point(mid.getX(), mid.getY() + pos_Increment), mid_Bottom, colour),
        draw_Polygon(window, mid_Right, g.Point(mid.getX() + pos_Increment, mid.getY()), g.Point(bottom_Right.getX(), bottom_Right.getY() - pos_Increment), colour),
        draw_Polygon(window, g.Point(bottom_Right.getX() - pos_Increment, bottom_Right.getY()), g.Point(mid.getX(), mid.getY() + pos_Increment), mid_Bottom, colour)
    }

    for quadrant in range(8):
        quadrant += 1
        for i in range(8):
            colour = colour_Picker(current_Colour, colour)

            # TODO Find how to call function from list
            poly_List[i]()

            if quadrant == 4:
                colour = "white"
            elif quadrant == 6:
                colour = current_Colour

            pos_Increment += 10

    for quadrant in range(8):
        pos_Increment = 0
        if quadrant == 0:
            for i in range(5):
                colour = colour_Picker(current_Colour, colour)
                poly_List[1]()
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

draw_Patch_Penultimate(window, 100, 100, "green")

window.getMouse()