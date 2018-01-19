class Polygon:
    
    def __init__(self, pSides):
        self.sides = pSides
        
    def calculatePerimeter(self):
        
        perimeter = 0
        
        for i in self.sides:
            perimeter += i
        
        return perimeter
        
    def printInformation(self):
        print("Shape Information")
        sideString = "Sides: "
        
        for i in self.sides:
            sideString += str(i)
            sideString += " "
        
        print(sideString)
        
        print("Perimeter: ", self.calculatePerimeter())