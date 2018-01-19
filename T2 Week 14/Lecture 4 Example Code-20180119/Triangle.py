from Polygon import Polygon
import math

class Triangle(Polygon):
    
    def __init__(self, side1, side2, side3):
        Polygon.__init__(self, [side1, side2, side3])
    
    def calculateTriangleArea(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        
        s = (a + b + c) / 2
        
        sa = s-a
        sb = s-b
        sc = s-c
        
        area = math.sqrt(s * sa * sb * sc)
        
        return area
    
    def calculateAngles(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        
        angleA = self.calculateSingleAngle(b, c, a)
        angleB = self.calculateSingleAngle(c, a, b)
        angleC = self.calculateSingleAngle(a, b, c)
        
        return [angleA, angleB, angleC]
        
    def calculateSingleAngle(self, s1, s2, s3):
        cosAngle = ((s1**2) + (s2**2) - (s3**2))/(2*s1*s2)
        angle = math.acos(cosAngle)
        return math.degrees(angle)
        
    def printTriangleInformation(self):
        print("Triangle Information")
        sideString = "Sides: "
        
        for i in self.sides:
            sideString += str(i)
            sideString += " "
        
        print(sideString)
        
        anglesString = "Angles: "
        
        anglesList = self.calculateAngles()
        
        for i in anglesList:
            anglesString += str(i)
            anglesString += " "
            
        print(anglesString)
        
        print("Area: ", self.calculateTriangleArea())
        print("Perimeter: ", self.calculatePerimeter())
        
        