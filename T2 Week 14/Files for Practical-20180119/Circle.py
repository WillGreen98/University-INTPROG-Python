import math

class Circle:
    
    def __init__(self, circleRadius):
        self.radius = circleRadius

    def calculateArea(self):
        area = math.pi * (self.radius ** 2)
        return area
    
    def calculateCircumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference
    
    def retrieveInformation(self):
        infoString = "A circle of radius {0:0.4f}".format(self.radius)
        infoString += "\nhas an area of {0:0.4f}".format(self.calculateArea())
        infoString += "\nand circumference of {0:0.4f}".format(self.calculateCircumference())
        return infoString
