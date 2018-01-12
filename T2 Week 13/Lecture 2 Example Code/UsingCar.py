from Car import Car

def main():
    
    car = Car("Honda", "Civic", "AB01 CDE", 1.6, "Petrol", "Left")
    
    print(car.getCarInformation())
    print()
    
    print("Old Registration: ", car.reg)
    car.changeReg("ZY99 XVU")
    print("New Registration: ", car.reg)
    print()
    
    print("Old Mileage: ", car.mileage)
    car.drive(25)
    print("New Mileage: ", car.mileage)
    print()
    
    print("Current Gear: ", car.currentGear)
    car.changeGear(False)
    print("Current Gear: ", car.currentGear)
    car.changeGear(True)
    car.changeGear(True)
    car.changeGear(True)
    car.changeGear(True)
    car.changeGear(True)
    print("Current Gear: ", car.currentGear)
    car.changeGear(False)
    print()
    
    print("Air Con On? ", car.aircon)
    car.turnOnAirCon()
    print("Air Con On? ", car.aircon)
    car.turnOnAirCon()
    print("Air Con On? ", car.aircon)
    car.turnOffAirCon()
    print("Air Con On? ", car.aircon)
    car.turnOffAirCon()
    print("Air Con On? ", car.aircon)
    car.turnOnAirCon()
    print()
    
    print("Lights On? ", car.aircon)
    car.turnOnLights()
    print("Lights On? ", car.aircon)
    car.turnOnLights()
    print("Lights On? ", car.aircon)
    car.turnOffLights()
    print("Lights On? ", car.aircon)
    car.turnOffLights()
    print("Lights On? ", car.aircon)
    print()
    
    print(car.getCarInformation())
    print()