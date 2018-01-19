from Polygon import Polygon
import math

class Rectangle(Polygon):
    
    def __init__(self, height, width):
        Polygon.__init__(self, [height, width, height, width])
    
    def calculateRectangleArea(self):
        a = self.sides[0]
        b = self.sides[1]
        
        return a * b
    
    def calculateDiagonalLength(self):
        a = self.sides[0]
        b = self.sides[1]
        
        return math.sqrt((a**2) + (b**2))
    
    def printRectangleInformation(self):
        print("Rectangle Information")
        sideString = "Sides: "
        
        for i in self.sides:
            sideString += str(i)
            sideString += " "
        
        print(sideString)
        
        print("Diagonal Length: ", self.calculateDiagonalLength())
        print("Area: ", self.calculateRectangleArea())
        print("Perimeter: ", self.calculatePerimeter())