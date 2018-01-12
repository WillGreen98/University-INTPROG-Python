def drawAndroid(win, startX, startY, colourBody):
    head = Circle(Point(startX, startY), 0.03)
    body = Rectangle(Point(startX - 0.03, startY - 0.05), Point(startX + 0.03, startY))
    leg1 = Rectangle(Point(startX - 0.02, startY - 0.08), Point(startX - 0.01, startY - 0.05))
    leg2 = Rectangle(Point(startX + 0.02, startY - 0.08), Point(startX + 0.01, startY - 0.05))
    arm1 = Rectangle(Point(startX + 0.03, startY - 0.04), Point(startX + 0.04, startY))
    arm2 = Rectangle(Point(startX - 0.04, startY - 0.04), Point(startX - 0.03, startY))
    eye1 = Circle(Point(startX - 0.01, startY + 0.01), 0.005)
    eye2 = Circle(Point(startX + 0.01, startY + 0.01), 0.005)
    android = [head, body, leg1, leg2, 
               arm1, arm2, eye1, eye2]
    for part in android:
        if part in [eye1, eye2]:
            colour = "white"
        else:
            colour = colourBody
        part.setFill(colour)
        part.setOutline(colour)
        part.draw(win)
    return android

def moveAndroid(android, xChange, yChange):
    
    for part in android:
        part.move(xChange, yChange)
    
    return android
    
def changeColour(android):
    newColour = input("What colour would you like to change it to?")
    
    eye1 = android[6]
    eye2 = android[7]
    
    for part in android:
        if part in [eye1, eye2]:
            colour = "white"
        else:
            colour = newColour
        part.setFill(colour)
        part.setOutline(colour)
    
    return android