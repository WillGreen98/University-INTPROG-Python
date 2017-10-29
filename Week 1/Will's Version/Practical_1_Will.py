__auther__ = "Will"
__project__ = "Prac 1"

import requests
import math
import curses #Key Presses

def sayName():
    name = input("Please enter your name: ")
    if name == "Will":
        print("Hello Master!")
    else:
        print("Hello ", name, "!")

def sayHelloWorld():
    print("Hello... \n ...World!")

def curCon():
    inputCurr = input("First currency: ").upper()
    con = float(input("Enter value to convert: "))
    convertCurr = input("Second Currency: ").upper()

    currency_URL = f"https://currency-api.appspot.com/api/%s/%s.json" % (inputCurr, convertCurr)
    r = requests.get(currency_URL)
    print(r.json()['rate'])
    print(con * float(r.json()['rate']))

def addNum():
    end_loop = False
    total  = 0
    while not end_loop:
        usr_Input = input("Enter a number: ")
        #isInstace(usr_In, int)
        if usr_Input.isdigit():
            sum += int(usr_Input)
        elif type(usr_Input) is str:
            if usr_Input == "Q" or usr_Input == "q":
                print(total)
                end_loop = True

class CoinType:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.num = 0

    def get_count(self):
        self.num = int(input("How many " + self.name + " coins do you have? "))

    def get_val(self):
        return self.num * self.value

def changeCounter():
    coins = [CoinType(1, "1p"), CoinType(2, "2p"), CoinType(5, "5p")]
    sum = 0
    for c in coins:
        c.get_count()
        sum += c.get_val()
    print("You have:", sum, "p")

def hhhhhhhhhh():
    for x in range(0, 10):
        print("Hello World!")

def weightsTable():
    print("KG - LBS")
    for kg in range(0+10, 110, 10):
        for lb in range(1):
            print(kg, " : ", kg * 2.2)

def futureValue():
    investment = int(input("Enter investment: "))
    years = int(input("Enter duration: "))
    comp_Value = investment * math.pow((1+1/years), (1*years))

    print(comp_Value)

def menu():
    print("0. Exit\n"
          "1. SayName()\n"
          "2. sayHelloWorld()\n"
          "3. curCon()\n"
          "4. addNum()\n"
          "5. changeCounter()\n"
          "6. hhhhhhhhhh()\n"
          "7. weightsTable()\n"
          "8. futureValue()\n")

    usr_In = int(input("Enter menu choice: "))

    while usr_In != 0:
        menu_List = {
            1: sayName,
            2: sayHelloWorld,
            3: curCon,
            4: addNum,
            5: changeCounter,
            6: hhhhhhhhhh,
            7: weightsTable,
            8: futureValue
        }[usr_In]()

        print("Thanks For using")
        break

        print("----------------")
        menu()

def main():
    menu()

if __name__ == '__main__':
    main()
