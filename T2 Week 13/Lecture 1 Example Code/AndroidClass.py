class Android:
    
    def __init__(self, window, colour, xStart, yStart):
        self.win = window
        self.currColour = colour
        self.xPos = xStart  # centre of the head (x direction)
        self.yPos = yStart  # centre of the head (y direction)
        self.drawAndroid()
    
    def drawAndroid(self):
        head = Circle(Point(self.xPos, self.yPos), 0.03)
        body = Rectangle(Point(self.xPos - 0.03, self.yPos - 0.05), Point(self.xPos + 0.03, self.yPos))
        leg1 = Rectangle(Point(self.xPos - 0.02, self.yPos - 0.08), Point(self.xPos - 0.01, self.yPos - 0.05))
        leg2 = Rectangle(Point(self.xPos + 0.02, self.yPos - 0.08), Point(self.xPos + 0.01, self.yPos - 0.05))
        arm1 = Rectangle(Point(self.xPos + 0.03, self.yPos - 0.04), Point(self.xPos + 0.04, self.yPos))
        arm2 = Rectangle(Point(self.xPos - 0.04, self.yPos - 0.04), Point(self.xPos - 0.03, self.yPos))
        eye1 = Circle(Point(self.xPos - 0.01, self.yPos + 0.01), 0.005)
        eye2 = Circle(Point(self.xPos + 0.01, self.yPos + 0.01), 0.005)
        self.android = [head, body, leg1, leg2, 
                arm1, arm2, eye1, eye2]
        for part in self.android:
            if part in [eye1, eye2]:
                colour = "white"
            else:
                colour = self.currColour
            part.setFill(colour)
            part.setOutline(colour)
            part.draw(self.win)
    
    def moveAndroid(self, xChange, yChange):
        
        self.xPos += xChange
        self.yPos += yChange
        
        for part in self.android:
            part.move(xChange, yChange)
        
    def changeColour(self):
        newColour = input("What colour would you like to change it to?")
        
        self.currColour = newColour
        eye1 = self.android[6]
        eye2 = self.android[7]
        for part in self.android:
            if part in [eye1, eye2]:
                colour = "white"
            else:
                colour = self.currColour
            part.setFill(colour)
            part.setOutline(colour)
    