from Employee import Employee

class PermanentEmployee(Employee):
    
    def __init__(self, name, address, jobTitle, lineManager, dept, salary):
        Employee.__init__(self, name, address, jobTitle, lineManager, dept)
        self.salary = salary
    
    def givePayRise(self, payChangePercentage):
        self.salary = self.salary * (1 + (payChangePercentage/100))
    
    def changeJobTitle(self, newTitle):
        self.jobTitle = newTitle
        
    def changeDepartment(self, newDepartment):
        self.department = newDepartment