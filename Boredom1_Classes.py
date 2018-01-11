subjects = []

class person:
    def __init__(self, f_Name, s_Name, subject, _isAwesome):
        self.fName = f_Name
        self.sName = s_Name
        self.subject = subject
        subjects.append(self.subject)
        self.isAwesome = bool(_isAwesome)

    def killMyself(person):
        isAllowed2Die = False
        if person.isAwesome == "False":
            isAllowed2Die = True
            if isAllowed2Die == True:
                mystr = " is now dead"
            else:
                mystr = " is awesome, not allowed to be killed."

            killed = print("{0}{1}".format(person.fName, mystr))

        return killed

Will = person("Will", "Green", ["Comp Sci"], False)
Bob = person("Bob", "Smith", ["Turfgrass Science"], True)

def main():
    person.killMyself(Will)
    person.killMyself(Bob)

    print(subjects)

if __name__ == '__main__':
    main()