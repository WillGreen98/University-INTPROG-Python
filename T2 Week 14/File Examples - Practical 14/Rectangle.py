import math

class Rectangle:
    
    def __init__(self, rHeight, rWidth):
        self.height = rHeight
        self.width = rWidth
        
    def calculateArea(self):
        area = self.height * self.width
        return area
    
    def calculatePerimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter
        
    def calculateDiagonal(self):
        diagonal = math.sqrt((self.height)**2 + (self.width)**2)
        return diagonal
        
    def retrieveInformation(self):
        infoString = "The height is {0:0.2f}".format(self.height)
        infoString += "\nThe width is {0:0.2f}".format(self.width)
        infoString += "\nThe area is {0:0.2f}".format(self.calculateArea())
        infoString += "\nThe perimeter is {0:0.2f}".format(self.calculatePerimeter())
        infoString += "\nThe diagonal length is {0:0.2f}".format(self.calculateDiagonal())
        return infoString