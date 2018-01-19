from Polygon import Polygon
import math

class Hexagon(Polygon):
    
    def __init__(self, side):
        Polygon.__init__(self, [side] * 6)
        
    def calculateHexagonArea(self):
        a = self.sides[0]
        
        area = ((3 * math.sqrt(3))/2)* (a**2)
        
        return area
    
    def calculateLongDiagonalLength(self):
        a = self.sides[0]
        
        return 2 * a
        
    def printHexagonInformation(self):
        print("Hexagon Information")
        sideString = "Sides: "
        
        for i in self.sides:
            sideString += str(i)
            sideString += " "
        
        print(sideString)
        
        print("Long Diagonal Length: ", self.calculateLongDiagonalLength())
        print("Area: ", self.calculateHexagonArea())
        print("Perimeter: ", self.calculatePerimeter())