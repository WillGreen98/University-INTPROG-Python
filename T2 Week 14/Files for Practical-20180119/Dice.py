from random import *

class Dice:
    
    def __init__(self, dSides):
        self.sides = dSides
        
    def rollDice(self):
        numSides = len(self.sides)
        sideLanded = randint(0, numSides-1)
        return self.sides[sideLanded]