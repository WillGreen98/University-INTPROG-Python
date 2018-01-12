class Car:
    
    def __init__(self, cMake, cModel, cReg, cEngine, cFuel, cDriverSide):
        self.make = cMake
        self.model = cModel
        self.reg = cReg
        self.engine = cEngine
        self.fuel = cFuel
        self.driverSide = cDriverSide
        self.mileage = 0
        self.currentGear = 1
        self.aircon = False
        self.lightsOn = False
        
    def changeReg(self, newReg):
        if self.reg == newReg:
            print("That is the current registration number")
        else:
            self.reg = newReg
            print("The registration has been changed to ", self.reg)
    
    def drive(self, numMiles):
        print("Mileage before driving:", self.mileage)
        for i in range(numMiles):
            print("Driving mile ",(i+1))
            self.mileage += 1
        print("Mileage after driving:", self.mileage)
        
    def changeGear(self, increaseGear):
        if increaseGear:
            if self.currentGear == 5:
                print("You are already in the top gear!")
            else:
                self.currentGear += 1
                print("You are in gear: ", self.currentGear)
        else:
            if self.currentGear == 1:
                print("You are already in the lowest gear!")
            else:
                self.currentGear -= 1
                print("You are in gear: ", self.currentGear)
    
    def turnOnAirCon(self):
        if self.aircon:
            print("Air Con is already on")
        else:
            self.aircon = True
            print("Air Con is now on")
            
    def turnOffAirCon(self):
        if self.aircon:
            self.aircon = False
            print("Air Con is now off")
        else:
            print("Air Con is already off")
            
    def turnOnLights(self):
        if self.lightsOn:
            print("The lights are already on")
        else:
            self.lightsOn = True
            print("The lights are now on")
        
    def turnOffLights(self):
        if self.lightsOn:
            self.lightsOn = False
            print("The lights are now off")
        else:
            print("The lights are already off")
    
    def getCarInformation(self):
        infoString = "Car Information\n"
        
        infoString += "\nMake: "+self.make
        infoString += "\nModel: "+self.model
        infoString += "\nRegistration: "+self.reg
        infoString += "\nEngine: "+str(self.engine)
        infoString += "\nFuel: "+self.fuel
        infoString += "\nDriver Side: "+self.driverSide
        infoString += "\nCurrent Mileage: "+str(self.mileage)
        infoString += "\nCurrent Gear: "+str(self.currentGear)
        
        if self.aircon:
            infoString += "\nAir Con is On"
        else:
            infoString += "\nAir Con is Off"
        
        if self.lightsOn:
            infoString += "\nLights are On"
        else:
            infoString += "\nLights are Off"
            
        return infoString
    
    
    