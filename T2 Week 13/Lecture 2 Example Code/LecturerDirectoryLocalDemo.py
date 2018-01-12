class LecturerDirectory:
    
    def __init__(self, lecName, lecPhone, lecOffice, lecSubjects, lecStart):
        self.name = lecName
        self.phone = lecPhone
        self.office = lecOffice
        self.subjects = lecSubjects
        self.startYear = lecStart
        
    def changeName(self, newName):
        self.name = newName
        
    def changePhone(self, newPhone):
        self.phone = newPhone
        
    def changeOffice(self, newOffice):
        self.office = newOffice
        
    def addSubject(self, newSubject):
        self.subjects.append(newSubject)
        
    def calculateService(self):
        currentYear = 2018
        service = currentYear - self.startYear
        return service
        
    def printSubjects(self):
        print(self.name, " teaches ", len(self.subjects), " subjects:")
        for subject in self.subjects:
            print(subject)
        
    def printLecturerInformation(self):
        print("Lecturer Information")
        print("Name = ", self.name)
        print("Phone Number = ", self.phone)
        print("Office = ", self.office)
        self.printSubjects()
  