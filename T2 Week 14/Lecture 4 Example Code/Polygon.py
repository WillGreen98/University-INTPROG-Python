class Polygon:
    
    def __init__(self, pSides):
        self.sides = pSides
        
    def calculatePerimeter(self):
        
        perimeter = 0
        
        for i in self.sides:
            perimeter += i
        
        return perimeter