__auther__ = "Will"
__project__ = "Patterns Course Word"

# TODO patch window task: ID Number 9
# Based on X and Y axis
def drawPatchWindow():
    window = g.GraphWin("ID Num 9", 100, 100)

    for x in range(0, 100, 20):
        g.Line(g.Point(x, 0), g.Point(100, 100 - x)).draw(window)
        g.Line(g.Point(100 - x, 0), g.Point(0, 100 - x)).draw(window)

        g.Line(g.Point(0, x), g.Point(100 - x, 100)).draw(window)
        g.Line(g.Point(100, 100 - x), g.Point(100 - x, 100)).draw(window)


    window.getMouse()

# TODO patch window task, draw window by x and y
# Based on parameters
def drawPatch(window, pos_X, pos_Y):
    for x in range(pos_X, pos_X + 100, 10):
        g.Line(g.Point(pos_X, pos_Y), g.Point(pos_X + 100,  (pos_Y + 100) - x)).draw(window)
        g.Line(g.Point((pos_X + 100) - pos_X, pos_Y), g.Point(pos_X, (pos_Y + 100) - x)).draw(window)
        g.Line(g.Point(pos_X, pos_Y + pos_X), g.Point((pos_X + 100) - pos_X, pos_Y + 100)).draw(window)
        g.Line(g.Point(pos_X + 100,(pos_Y + 100) - x), g.Point((pos_X + 100) - x, pos_Y + 100)).draw(window)

    window.getMouse()

if __name__ == '__main__':
    a = 5