#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

import graphics as g
import math

def distBetweenPoints(a, b):
    return math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2)

def drawCircle(window, center, radius, colour):
    circle = g.Circle(center, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(window)

def drawColouredEye(window, center, radius, colour):
    drawCircle(window, center, radius, "")
    drawCircle(window, center, radius / 2, "brown")
    drawCircle(window, center, radius / 3, "black")

def fastFoodOrderPrice():
    price = float(input("Price of pizza: "))

    if price < 10.00:
        price += 1.50
    print("Cost of pizza is £", price)

def whatToDoToday():
    temp = int(input("What is the temp outside: "))

    if temp < 10:
        print("stay in")
    elif temp > 10 and temp < 25:
        print("Go GunWharf")
    elif temp > 25:
        print("Get Nekid and sun bathe")
    else:
        print("What is even happening?")

def squareRoot(num1, num2):
    for i in range(num1, num2):
        print("square root of ", i, " = ", math.sqrt(i))

def calculateGrade():
    grade = int(input("Enter grade: "))

    if grade >= 16:
        print("a".upper())
    elif grade >= 12:
        print("b".upper())
    elif grade >= 8:
        print("c".upper())
    elif grade >= 7:
        print("f".upper())
    else:
        print("You majorly fucked up")

def peasInAPod():
    peas = int(input("Number of peas? : "))

    window = g.GraphWin("Peas in pod", peas * 100, 100)

    for i in range(peas):
        pea = g.Circle(g.Point(i * 100 + 50, 50), 50).draw(window).setFill("green")

    window.getMouse()

def ticketPrice(age, distance):
    discount = 0
    if age <= 15 or age >= 60:
        discount = 0.60
    else:
        discount = 1.00

    return discount * (3.00 + (0.15 * distance))

def numberedSquare(n):
    a = 5
