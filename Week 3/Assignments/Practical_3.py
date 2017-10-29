import graphics as g

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
    message = g.Text(g.Point(100,100), "Click on first point")
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

