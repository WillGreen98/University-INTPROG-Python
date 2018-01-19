from WorkerHierarchy import Worker

class Employee(Worker):
    
    def __init__(self, name, address, jobTitle, lineManager, dept):
        Worker.__init__(self, name, address)
        self.jobTitle = jobTitle
        self.lineManager = lineManager
        self.department = dept
    
    def changeLineManager(self, newLineManager):
        self.lineManager = newLineManager
    