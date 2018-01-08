from graphics import *

WIDTH, HEIGHT = 500, 500
RAD = 50

def drawCircle():
    window = GraphWin("Test", WIDTH, HEIGHT)

    circle = Circle(Point(100, 100), RAD).draw(window).setFill("Green")
    rectangle = Rectangle(Point(160, 160), Point(400, 400)).draw(window).setFill("Blue")

    string = "Will G G G G G G Green"

    for i in range(5):
        text = Text(window.getMouse(), string[i]).draw(window).setSize(22)
        print(string[:i])
        window.getMouse()

    window.getMouse()
    window.close()

def main():
    drawCircle()

if __name__ == '__main__':
    main()