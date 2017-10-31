import graphics as g


def drawCircle(win, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawColouredEye(win, centre, radius, colour):
    pass

