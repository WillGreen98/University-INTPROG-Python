import math

def circumOfCircle():
    r = int(input("Enter value for r: "))
    print(2 * math.pi * r)

def areaOfCircle():
    r = int(input("Enter value for r: "))
    print(math.pi * (r ** 2))

def costOfPizza():
    d = int(input("Enter value for d: "))
    print(((d/2) ** 2) * math.pi * 1.5)

def slopeOfLine():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))

    print((y2-y1)/(x2-x1))

def distanceBetweenPoints():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))

    print(math.sqrt((math.pow((x2-x1), 2)) + (math.pow((y2-y1), 2))))

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
    change = int(input("Enter amount in ps: "))

    two_Pound = change // 200
    change -= two_Pound * 200

    one_Pound = change // 100
    change -= one_Pound * 100

    fifty_P = change // 50
    change -= fifty_P * 50

    twenty_P = change // 20
    change -= twenty_P * 20

    ten_P = change // 10
    change -= ten_P * 10

    five_P = change // 5
    change -= five_P * 5

    two_P = change // 2
    change -= two_P * 2

    one_P = change

    print("1p: ", one_P,
          "2p: ", two_P,
          "5p: ", five_P,
          "10p: ", ten_P,
          "20p: ", twenty_P,
          "50p: ", fifty_P,
          "£1: ", one_Pound,
          "£2: ", two_Pound)

selectCoins()
