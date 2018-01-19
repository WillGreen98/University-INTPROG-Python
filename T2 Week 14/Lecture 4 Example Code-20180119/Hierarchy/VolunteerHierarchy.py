from WorkerHierarchy import Worker

class Volunteer(Worker):
    
    def __init__(self, name, address, area):
        Worker.__init__(self, name, address)
        self.area = area
        
    def changeArea(self, newArea):
        self.area = newArea