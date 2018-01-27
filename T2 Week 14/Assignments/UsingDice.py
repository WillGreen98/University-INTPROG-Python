from   _3_dice      import *
from   _1_rectangle import *
from   Circle       import *
from   Triangle     import * 
import random       as     rand

def main():
    dice = Dice(["Circle", "Rectangle", "Triangle"] * 2)
    result = dice.throw()
    size   = rand.randint(1, 10)
    print("Creating", result, "with size", size)
    if (result == "Circle"):
        shape = Circle(size)
    elif(result == "Rectangle"):
        shape = Rectangle(size, size)
    elif(result == "Triangle"):
        shape = Triangle(size, size)
    print(shape.retrieveInformation())
    
main()