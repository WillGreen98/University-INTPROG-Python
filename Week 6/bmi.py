# Demo of the use of range and nested for loops
# Draws a body-mass index chart similar to that found at
# https://www.diabetes.co.uk/bmi.html
# Heights are in cm, weights in kg.

def calculateBmi(cm, kg):
    return 10000 * kg / cm ** 2

def bodyMassIndexTable():
    print("    ", end="")
    for kg in range(50, 100, 2):
            print(kg, end=" ")
    print()        
    for cm in range(200, 149, -2):
        print(cm, end=" ")
        for kg in range(50, 100, 2):
            bmi = calculateBmi(cm, kg)
            if bmi >= 30:
                # obese
                code = "*"
            elif bmi >= 25:
                # overweight
                code = "+"   
            elif bmi >= 18.5:
                # normal
                code = "."
            else:
                #underweight
                code = "-"
            print(" " + code + " ", end="")
        print()












