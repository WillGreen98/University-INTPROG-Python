import graphics as g

window = g.GraphWin("patch test")

def unwrap(func, *args):
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
    top_Left = g.Point(pos_X, pos_Y)
    top_Mid = g.Point(pos_X + 50, pos_Y)
    top_Right = g.Point(pos_X + 100, pos_Y)
    mid_Left = g.Point(pos_X, pos_Y + 50)
    mid_Mid = g.Point(pos_X + 50, pos_Y + 50)
    mid_Right = g.Point(pos_X + 100, pos_Y + 50)
    bottom_Left = g.Point(pos_X, pos_Y + 100)
    bottom_Mid = g.Point(pos_X + 50, pos_Y + 100)
    bottom_Right = g.Point(pos_X + 100, pos_Y + 100)

    colour = current_Colour
    pos_Increment = 0

    poly_List = {
        draw_Polygon(window, g.Point(top_Left.getX(), top_Left.getY() + pos_Increment),g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour),
        draw_Polygon(window, g.Point(top_Left.getX() + pos_Increment, top_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), top_Mid, colour),
        draw_Polygon(window, top_Mid, g.Point(top_Right.getX() - pos_Increment, top_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), colour),
        draw_Polygon(window, g.Point(top_Right.getX(), top_Right.getY() + pos_Increment), g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), mid_Right, colour),
        draw_Polygon(window, g.Point(bottom_Left.getX(), bottom_Left.getY() - pos_Increment), g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour),
        draw_Polygon(window, g.Point(bottom_Left.getX() + pos_Increment, bottom_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour),
        draw_Polygon(window, mid_Right, g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), g.Point(bottom_Right.getX(), bottom_Right.getY() - pos_Increment), colour),
        draw_Polygon(window, g.Point(bottom_Right.getX() - pos_Increment, bottom_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour)
    }

    # poly_List = [
    #     'section_one': draw_Polygon(window, g.Point(top_Left.getX(), top_Left.getY() + pos_Increment),g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour),
    #     'section_two': draw_Polygon(window, g.Point(top_Left.getX() + pos_Increment, top_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), top_Mid, colour),
    #     'section_three': draw_Polygon(window, top_Mid, g.Point(top_Right.getX() - pos_Increment, top_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), colour),
    #     'section_four': draw_Polygon(window, g.Point(top_Right.getX(), top_Right.getY() + pos_Increment), g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), mid_Right, colour),
    #     'section_five': draw_Polygon(window, g.Point(bottom_Left.getX(), bottom_Left.getY() - pos_Increment), g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour),
    #     'section_six': draw_Polygon(window, g.Point(bottom_Left.getX() + pos_Increment, bottom_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour),
    #     'section_seven': draw_Polygon(window, mid_Right, g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), g.Point(bottom_Right.getX(), bottom_Right.getY() - pos_Increment), colour),
    #     'section_eight': draw_Polygon(window, g.Point(bottom_Right.getX() - pos_Increment, bottom_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour)
    # ]
    #
    # poly_List = {
    #     unwrap.__call__(draw_Polygon, [window, g.Point(top_Left.getX(), top_Left.getY() + pos_Increment), g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour]),
    #     unwrap.__call__(draw_Polygon, [window, g.Point(top_Left.getX() + pos_Increment, top_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), top_Mid, colour]),
    #     unwrap.__call__(draw_Polygon, [window, top_Mid, g.Point(top_Right.getX() - pos_Increment, top_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() - pos_Increment), colour]),
    #     unwrap.__call__(draw_Polygon, [window, g.Point(top_Right.getX(), top_Right.getY() + pos_Increment), g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), mid_Right, colour]),
    #     unwrap.__call__(draw_Polygon, [window, g.Point(bottom_Left.getX(), bottom_Left.getY() - pos_Increment), g.Point(mid_Mid.getX() - pos_Increment, mid_Mid.getY()), mid_Left, colour]),
    #     unwrap.__call__(draw_Polygon, [window, g.Point(bottom_Left.getX() + pos_Increment, bottom_Left.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour]),
    #     unwrap.__call__(draw_Polygon, [window, mid_Right, g.Point(mid_Mid.getX() + pos_Increment, mid_Mid.getY()), g.Point(bottom_Right.getX(), bottom_Right.getY() - pos_Increment), colour]),
    #     unwrap.__call__(draw_Polygon, [window, g.Point(bottom_Right.getX() - pos_Increment, bottom_Right.getY()), g.Point(mid_Mid.getX(), mid_Mid.getY() + pos_Increment), bottom_Mid, colour])
    # }

    for quadrant in range(8):
        quadrant += 1
        for i in range(8):
            colour = colour_Picker(current_Colour, colour)
            if quadrant == 4:
                colour = "white"
            elif quadrant == 6:
                colour = current_Colour
            poly_List[0]()
            pos_Increment += 10

draw_Patch_Penultimate(window, 100, 100, "green")
window.getMouse()