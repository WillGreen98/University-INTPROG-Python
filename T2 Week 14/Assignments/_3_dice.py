import random

class Dice:
    def __init__(self, labels):
        self.labels = labels
        self.numSides = len(labels)
        
    def throw(self):
        return self.labels[random.randint(0, self.numSides - 1)]
        
'''
dice = Dice([1, 2, 3, 4, 5, 6])

for i in range(10):
    print(dice.throw())
'''