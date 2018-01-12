from Triangle import Triangle

def main():
    
    triangle = Triangle(3, 4)
    
    print("side 3: ", triangle.calculateSide3())
    
    print("area: ", triangle.calculateArea())
        
    print("perimeter: ", triangle.calculatePerimeter())
        
    print("angles: ", triangle.calculateAngles())
    
    print()
    print()
    print()
    
    triangle.printTriangleInformation()

    triangle.changeSide2(2)
    
    print()
    print("side 2 changed")
    print()
    
        
    triangle.printTriangleInformation()
    
    triangle.changeSide1(2)
    
    print()
    print("side 1 changed")
    print()
    
    
    
    triangle.printTriangleInformation()
    