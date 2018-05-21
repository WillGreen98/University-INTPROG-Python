import time

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

    def bork(self, d):
        if d == "quiet":
            print("Bork Bork Bork... My name is: {0}".format(self.name))
        elif d == "loud":
            print("BORK BORK BORK... MY NAME IS: {0}".format(self.name))
        elif d == "sassy":
            print("Bork Bork Boooork... My name is: {0}".format(self.name))
        else:
            print("Bork")

    def sit(self, duration):
        t = time.process_time()
        print("I am now sitting, I have been sitting for: {0}".format(time.process_time() - duration))

    def getTheFuckAwayFromMyPizza(self):
        return "DRIBBLES ON FLOOR"
        
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

Kewal = Person("Kewal", "Bitch-Boi", ["Maths"], True)
Will = Person("Will", "The Bald Bean", ["Comp Sci"], False)

Crumble = Dog("Crumble", "Wire-Haired Sausage")
Loki = Dog("Loki", "Samoyed")
Rollie = Dog("Rollie", "Sausage")
Thor = Dog("Thor", "Samoyed")

def main():
    print(subjects, "\n")

    print(Kewal.killMyself())
    print(Will.killMyself())


if __name__ == '__main__':
    main()