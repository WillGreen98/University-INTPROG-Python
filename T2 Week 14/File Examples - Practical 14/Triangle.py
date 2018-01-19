import math

class Triangle:
    
    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2
        
    def calculateSide3(self):
        
        side3 = math.sqrt((self.side1**2) + (self.side2**2))
        
        return side3
        
    def calculateArea(self):
        area = self.side1 * self.side2 * 0.5
        
        return area
        
    def calculatePerimeter(self):
        perimeter = self.side1 + self.side2 + self.calculateSide3()
        
        return perimeter
        
    def calculateAngles(self):
        angle1 = math.atan(self.side1 / self.side2)
        angle1 = math.degrees(angle1)
        
        angle2 = 180 - (90 + angle1)
        
        return [90, angle1, angle2]
        
    def changeSide1(self, newS1):
        self.side1 = newS1
        
    def changeSide2(self, newS2):
        self.side2 = newS2
        
    def retrieveInformation(self):
        infoString = "Side 1 is {0:0.2f}".format(self.side1)
        infoString += "\nSide 2 is {0:0.2f}".format(self.side2)
        infoString += "\nSide 3 is {0:0.2f}".format(self.calculateSide3())
        infoString += "\nThe area is {0:0.2f}".format(self.calculateArea())
        infoString += "\nThe perimeter is {0:0.2f}".format(self.calculatePerimeter())
        infoString += "\nThe angles are: ".format(self.calculateAngles())

        return infoString
        
        
        
        