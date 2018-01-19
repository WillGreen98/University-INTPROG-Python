from EmployeeHierarchy import Employee

class TemporaryEmployee(Employee):
    
    def __init__(self, name, address, jobTitle, lineManager, dept, hourlyRate, contractEnd):
        Employee.__init__(self, name, address, jobTitle, lineManager, dept)
        self.hourlyRate = hourlyRate
        self.contractEnd = contractEnd
    
    def extendContract(self, newEnd):
        self.contractEnd = newEnd