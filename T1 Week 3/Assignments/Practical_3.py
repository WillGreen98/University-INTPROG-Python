import graphics as g
import random as rand

def drawStickFigure():
    window = g.GraphWin("Stick MAAAAAN", 200, 200)

    head = g.Circle(g.Point(100, 60), 20).draw(window)
    body = g.Line(g.Point(100, 80), g.Point(100, 120)).draw(window)

    left_Arm = g.Line(g.Point(80, 80), g.Point(100, 90)).draw(window)
    right_Arm = g.Line(g.Point(120, 80), g.Point(100, 90)).draw(window)

    left_Leg = g.Line(g.Point(100, 120), g.Point(80, 140)).draw(window)
    right_Leg = g.Line(g.Point(100, 120), g.Point(120, 140)).draw(window)

    window.getMouse()
    window.close()

def drawACircle():
    window = g.GraphWin("Draw Circle", 200, 200)

    radius = int(input("Radius: "))
    g.Circle(g.Point(100, 100), radius).draw(window)

    window.getMouse()
    window.close()

def bowAndArrow():
    window = g.GraphWin("Archery Target", 300, 300)

    radius = int(input("Radius: "))
    outer_Circle = g.Circle(g.Point(150, 150), radius).draw(window).setFill("Blue")
    mid_Circle = g.Circle(g.Point(150, 150), radius - 30).draw(window).setFill("Yellow")
    inner_Circle = g.Circle(g.Point(150, 150), radius - 60).draw(window).setFill("Red")

    window.getMouse()
    window.close()

def drawRectangle():
    window = g.GraphWin("Long Square", 300, 300)

    height = int(input("Enter height: "))
    width = int(input("Enter Width: "))

    rectangle = g.Rectangle(g.Point(150 - height / 3, 150 - width / 3),
                            g.Point(150 + height / 3, 150 + width / 3)).draw(window).setFill("Green")

    window.getMouse()
    window.close()

def click_BlueCircle():
    window = g.GraphWin("Blue Circle")
    usr_Click = window.getMouse()

    circle = g.Circle(g.Point(usr_Click.getX(), usr_Click.getY()), 50).draw(window).setFill("Blue")

    window.getMouse()
    window.close()

def drawLine():
    window = g.GraphWin("Line drawer")
    message = g.Text(g.Point(100, 100), "Click on first point")
    message.draw(window)
    p1 = window.getMouse()
    message.setText("Click on second point")
    p2 = window.getMouse()
    line = g.Line(p1, p2)
    line.draw(window)
    message.setText("")

    window.getMouse()
    window.close()

def drawLine_Ten():
    for i in range(10):
        drawLine()

def tenStrings():
    window = g.GraphWin("Ten Strings", 500, 500)

    for i in range(10):
        usr_Click = window.getMouse()
        usr_In_Box = g.Entry(g.Point(200, 50), 20).draw(window)
        usr_In = g.Text(g.Point(usr_Click.getX(), usr_Click.getX()), usr_In_Box.getText()).draw(window)

    window.getMouse()
    window.close()

def tenfilledRects():
    window = g.GraphWin("Ten Strings", 500, 500)

    for i in range(10):
        # inputBox = g.Entry(g.Point(50, 30), 10)
        # inputBox.draw(window)

        r = rand.randrange(256)
        b = rand.randrange(256)
        g = rand.randrange(256)
        rand_Color = g.color_rgb(r, g, b)

        coord_One = window.getMouse()
        coord_Two = window.getMouse()

        rectangle = g.Rectangle(g.Point(coord_One.getX(), coord_One.getY()), g.Point(coord_Two.getX(),
                                                                                     coord_Two.getY())).draw(
            window).setFill(rand_Color)

    window.getMouse()
    window.close

def click_stickFigure():
    window = g.GraphWin("Click Stick Figure", 500, 500)

    coord_One_Head = window.getMouse()
    coord_Two_Head = window.getMouse()
    coord_Three_Body = window.getMouse()
    coord_Four_Body = window.getMouse()
    coord_Five_Leg = window.getMouse()

    # Radius = distance between two points becuase it is a click
    radius = (((coord_Two_Head.getX() - coord_One_Head.getX()) ** 2) + (coord_Two_Head.getY() - coord_Two_Head.getY()) ** 2) ** 0.5

    body_Head = g.Circle(coord_One_Head, radius).draw(window)
    body_Line = g.Line(g.Point(coord_Two_Head.getX(), coord_Two_Head.getX()), coord_Three_Body).draw(window)

    dist_Arms = coord_Four_Body.getX() - coord_Three_Body.getX()

    body_Arms = g.Line(g.Point(coord_Four_Body.getX(), coord_Four_Body.getY()),
                       g.Point(coord_Four_Body.getY() - dist_Arms, coord_Four_Body.getY())).draw(window)

    dist_Legs = coord_Five_Leg.getX() - coord_Three_Body.getX()

    leg_Left = g.Line(coord_Five_Leg, coord_Three_Body).draw(window)
    leg_Right = g.Line(g.Point(coord_Five_Leg.getX() - dist_Legs), coord_Three_Body).draw(window)

def rainFall_Graph():
    window = g.GraphWin("RainFall", 400, 400)

    usr_In = g.Entry(g.Point(40, 40), 10).draw(window)

    for i in range(7):
        window.getMouse()
        dim = int(usr_In.getText())
        rectangle = g.Rectangle(g.Point(), g.Point()).draw(window).setFill(rand.choice(
                                            ["Black", "Blue", "Green", "Yellow", "Orange", "Red"]))
        window.getMouse()

rainFall_Graph()