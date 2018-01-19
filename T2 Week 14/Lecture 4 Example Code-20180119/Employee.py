class Employee:
    
    def __init__(self, name, address, jobTitle, lineManager, dept):
        self.name = name
        self.address = address
        self.jobTitle = jobTitle
        self.lineManager = lineManager
        self.department = dept
    
    def changeAddress(self, newAddress):
        self.address = newAddress
    
    def changeLineManager(self, newLineManager):
        self.lineManager = newLineManager
    