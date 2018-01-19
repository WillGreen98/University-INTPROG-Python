import datetime

class LecturerDirectory:
    def __init__(self, name, tele_Num, office_Num, subject, start_Year):
        self.name = name
        self.tele = tele_Num
        self.office = office_Num
        self.subject = subject
        self.start_Y = start_Year

    def change_Name(self, newName):
        if newName == self.name:
            print("No change")
        else:
            self.fName = newName

    def change_Tele(self, newTele):
        self.tele = newTele

    def change_Office(self, newOffice):
        self.office = newOffice

    def change_Subject(self, newSub):
        self.subject = newSub

    def duration(self):
        date = datetime.date
        duration = date.today() - self.start_Y
        return duration

    def dis_Info(self):
        print(self.name, self.tele, self.office, self.subject)