__auther__ = "Will"
__project__ = "Prac 2"

import math
import numpy as np
import matplotlib.pyplot as mpl

def getRadius():
    return int(input("Enter radius of circle: "))

def getCircleArea(r):
    return math.pi * (r ** 2)

def circumOfCircle():
    radius = getRadius()
    print("Circumfrence of circle is: ", 2 * math.pi * radius)

def areaOfCircle():
    r = getRadius()
    print("Circumfrence of circle is: ", getCircleArea(r))

def costOfPizza():
    d = int(input("Enter value for d: "))
    print(((d/2) ** 2) * math.pi * 1.5)

def slopeOfLineWithDistance():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))

    coor_One = [x1, y1]
    coor_Two = [x2, y2]

    #Graphing Line
    mpl.xlabel('X \n', print("The distance axial points is: ", (y2-y1)/(x2-x1)), "\n The Disctance between the two points is: "
               ,math.sqrt((math.pow((x2-x1), 2)) + (math.pow((y2-y1), 2))))
    mpl.ylabel('Y')
    mpl.plot(coor_One, coor_Two)
    mpl.show()

def travelStat():
    time = int(input("Enter the time: "))
    speed = int(input("Enter the (average) speed: "))

    distance = speed * time
    print("Distance: ", distance, " Fuel used: ", (distance / 5), " Liters")

def sumOfNumbers():
    seq = int(input("Enter values: "))
    sig_Sum = 0
    for i in range(seq):
        sig_Sum += (i + 1)
    print(sig_Sum)

def averageOfNumbers():
    index = int(input("Enter how many numbers: "))

    total = 0
    for i in range(index):
        total += int(input("Enter value: "))
    print(total/index)


def selectCoins():
    coins = int(input("Enter amount: "))

    for change in [200, 100, 50, 20, 10, 5, 2, 1]:
        total = int(coins / change)
        print(str(total), " of ", str(change), " ps")
        coins -= total * change

def menu():
    print("0. Exit\n"
          "1. circumOfCircle()\n"
          "2. areaOfCircle()\n"
          "3. costOfPizza()\n"
          "4. slopeOfLineWithDistance()\n"
          "5. travelStat()\n"
          "6. averageOfNumbers()\n"
          "7. sumOfNumbers()\n"
          "8. averageOfNumbers()\n"
          "9. selectCoins()\n")

    usr_In = int(input("Enter menu choice: "))

    while usr_In != 0:
        menu_List = {
            1: circumOfCircle,
            2: areaOfCircle,
            3: costOfPizza,
            4: slopeOfLineWithDistance,
            5: travelStat,
            6: sumOfNumbers,
            7: averageOfNumbers,
            8: selectCoins
        }[usr_In]()

        print("----------------")
        menu()

        print("Thanks for using.")
        break

def main():
    menu()

if __name__ == '__main__':
    main()