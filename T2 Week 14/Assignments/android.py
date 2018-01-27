from graphics import *

class Android:

    def __init__(self, win, colour, headCentreX, headCentreY, scale, speedChange):
        head = Circle(Point(headCentreX, headCentreY), scale*0.03)
        body = Rectangle(Point(headCentreX-0.03*scale, headCentreY-0.05*scale), Point(headCentreX+0.03*scale, headCentreY))
        
        leg1 = Rectangle(Point(headCentreX-0.02*scale, headCentreY-0.08*scale), Point(headCentreX-0.01*scale, headCentreY-0.05*scale))
        leg2 = Rectangle(Point(headCentreX+0.02*scale, headCentreY-0.08*scale), Point(headCentreX+0.01*scale, headCentreY-0.05*scale))
        
        arm1 = Rectangle(Point(headCentreX+0.03*scale, headCentreY-0.04*scale), Point(headCentreX+0.04*scale, headCentreY))
        arm2 = Rectangle(Point(headCentreX-0.04*scale, headCentreY-0.04*scale), Point(headCentreX-0.03*scale, headCentreY))
        
        eye1 = Circle(Point(headCentreX-0.01*scale, headCentreY+0.01*scale), scale*0.005)
        eye2 = Circle(Point(headCentreX+0.01*scale, headCentreY+0.01*scale), scale*0.005)
        
        self.android = [head, body, leg1, leg2, arm1, arm2, eye1, eye2]
        
        for part in self.android:
            if part == eye1 or part == eye2:
                mainColour = "white"
            else:
                mainColour = colour
            part.setFill(mainColour)
            part.setOutline(mainColour)
            part.draw(win)
            
        self.currentXSpeed = 0
        self.currentYSpeed = 0
        
        self.speedChange = speedChange

    def moveAndroid(self, direction):
        
        if direction == "Left":
            self.currentXSpeed -= self.speedChange
        elif direction == "Right":
            self.currentXSpeed += self.speedChange
        elif direction == "Down":
            self.currentYSpeed -= self.speedChange
        elif direction == "Up":
            self.currentYSpeed += self.speedChange
        
        for part in self.android:
            part.move(self.currentXSpeed, self.currentYSpeed)
            
    def getHeadCentre(self):
        return self.android[0].getCenter()
