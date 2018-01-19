from PolygonOverriding import Polygon
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
    
    def printInformation(self):
        # this method uses the one in the superclass...
        super().printInformation()
        # then adds extra functionality
        print("Diagonal Length: ", self.calculateDiagonalLength())
        print("Area: ", self.calculateRectangleArea())
        