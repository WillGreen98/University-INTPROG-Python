def sayName():
    print("Will")

def sayHelloWorld():
    print("Hello...")
    print("... World!")

def euros2pounds():
    euro = float(input("Please enter value: "))
    print("Converted = £", euro * 1.09)

def addNum():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))

    sum = num1 + num2
    print(sum)

def changeCounter():
    one_p = 0.01
    two_p = 0.02
    five_p = 0.05

    one_p_v = int(input("Enter amount of 1p coins:"))
    two_p_v = int(input("Enter amount of 2p coins:"))
    five_p_v = int(input("Enter amount of 5 couns:"))

    print("You have: ", one_p_v * one_p, " in 1ps\n "
          "You have: ", two_p_v * two_p, " in 2ps\n "
          "You have: ", five_p_v * five_p, " in 2ps")

def hhhhhhhhhh():
    for x in range(0, 10):
        print("Hello World!")

def weightsTable():
    print("KG - LBS")
    for kg in range(0+10, 110, 10):
        for lb in range(1):
            print(kg, " ", kg * 2.2)

def futureValue():
    value = int(input("Enter investment: "))
    year = int(input("Enter duration: "))

    print("Compound interest value: ", value * (5.5 ** year))

sayName()
sayHelloWorld()
euros2pounds()
addNum()
changeCounter()
hhhhhhhhhh()
weightsTable()
futureValue()