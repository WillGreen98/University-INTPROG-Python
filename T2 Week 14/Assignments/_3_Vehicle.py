def clamp(val, low, high):
    if (val > high):
        return high
    if (val < low ):
         return low
    return val

class Vehicle:
    def __init__(numWheels, engineSize, manualTransition, currentMilage):
        self.numWheels = numWheels
        self.engineSize = engineSize
        self.manualTransition = manualTransition
        self.currentGear = 0
        self.currentMilage = currentMilage
        
        self.doorsLocked = True
        
    def drive(self):
        print("Car starts to drive")
        
    def changeGear(self, direction):
        self.currentGear += clamp(direction, low, high)
        self.currentGear = clamp(self.currentGear, 0, 5)
        
    def lockDoors(self):
        self.doorsLocked = True
        
    def unlockDoors(self):
        self.doorsLocked = False
        
class SportsCar(Vehicle):
    def __init__(self, turboEngine):
        self.roofOpen = False
        self.sportsMode = False 
        self.turboEngine = turboEngine
        
    def openRoof(self):
        self.roofOpen = True
        
    def closeRood(self):
        self.roofOpen = False
        
    def startSportsMode(self):
        self.sportsMode = True
        
    def stopSportsMode(self):
        self.sportsMode = False
        
class FourByFour(Vehicle):
    def __init__(self):
        self.offRoadMode = False
        
    def startOffRoad(self):
        self.offRoadMode = True 
        
    def stopOffRoad(self):
        self.offRoadMode = False 
        
class Tractor(Vehicle):
    def __init__(self, maxWeight):
        self.maximumWeight = maxWeight 
        self.trailerAttached = False
        
    def attachTrailer(self, mass):
        if (mass > self.maximumWeight):
            print("Unable to attach trailer, it is too heavy.")
        else:
            self.trailerAttached = True
        
    def detachTrailer(self, mass):
        self.trailerAttached = False
        
    
car = FourByFour()
car.drive()

tractor = Tractor(5000)