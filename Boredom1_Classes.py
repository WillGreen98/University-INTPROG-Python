subjects = []

isAllowed2Die = True

class Animal:
    isAllowed2Die = True
    isPet = bool

    def __init__(self, genome, classes, bio_def, c_type):
        self.genome = genome
        self.a_class = classes
        self.bio_def = bio_def
        self.type = c_type

class Dog(Animal):
    isPet = True

    def __init__(self, name, breed):
        super().__init__(self, "Canis", "Carnivore", "Dog")
        self.name = name
        self.breed = breed

    def bork(d):
        if d == "quiet":
            print("Bork Bork Bork... My name is: {0}".format(name))
        elif d == "loud":
            print("BORK BORK BORK... MY NAME IS: {0}".format(name))
        elif d == "sassy":
            print("Bork Bork Boooork... My name is: {0}".format(name))
        else:
            print("Bork")

    def sit(duration):
        import time
        t = time.process_time()
        print("I am now sitting, I have been sitting for: {0}".format(elapsed_time))

        elapsed_time = time.process_time() - t
        
    def roll_Over():
        print("My belly is showing")
        
    def bundle():
        print("CUDDLES")
        
    def fetch():
        print("Did you throw something?")

    def zoomies():
        y = 6
        for x in range(0, y, 1):
            print("Z")
        for x in range(0, y*2, 1):
            print("O")
        for x in range(0, y/2, 1):
            print("M")
        for x in range(0, y-1, 1):
            print("I")
        for x in range(0, y*(2/3), 1):
            print("E")
        for x in range(0, y, 1):
            print("S")
    
    def getTheFuckAwayFromMyPizza():
        print("*DRIBBLES ON FLOOR*")
        
class Person:
    def __init__(self, f_Name, nickName, subject, isAwesome):
        self.fName = f_Name
        self.sName = nickName
        self.subject = subject

        subjects.append(self.subject)
        self._isAwesome = bool(isAwesome)

    def killMyself(self):
        if self._isAwesome:
            ToBkilledOrNotToBKilledThatIsTheQuestion = " is awesome, they are not allowed to be killed."
        else:
            ToBkilledOrNotToBKilledThatIsTheQuestion = " is now dead."

        killed = "{0}{1}".format(self.fName, ToBkilledOrNotToBKilledThatIsTheQuestion)
        return killed

Albert = Person("Albert", "Hung like a Moose, Hanging from a Noose", ["Comp Sci & AI"], True)
Kewal = Person("Kewal", "Bitch-Boi", ["Maths"], True)
Will = Person("Will", "The Bald Bean", ["Comp Sci"], False)
Xho = Person("Xho", "Squidward", ["Sociology & Pysch"], True)

Crumble = Dog("Crumble", "Wire-Haired Sausage")
Loki = Dog("Loki", "Samoyed")
Rollie = Dog("Rollie", "Sausage")
Thor = Dog("Thor", "Samoyed")

def main():
    print(subjects, "\n")

    Person.killMyself

if __name__ == '__main__':
    main()