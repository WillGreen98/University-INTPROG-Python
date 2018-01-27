import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
        
    def getPerimeter(self):
        return self.width * 2 + self.height * 2
        
    def getDiagonalLength(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)
        
    def retrieveInformation(self):
        return  "Rectangle Summary: Width:" + str(self.width) +  \
                "\nHeight: "                 + str(self.height) + \
                "\nArea:   "                 + str(self.getArea()) + \
                "\nPerimeter: "              + str(self.getPerimeter()) + \
                "\nDiagonal Length: "        + str(self.getDiagonalLength())
        

'''
rect = Rectangle(5, 5)
rect.getSummary()
'''