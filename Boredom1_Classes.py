subjects = []

isAllowed2Die = True

class Animal:
    isAllowed2Die = False
    isPet = bool

    def __init__(self, genome, classes, bio_def, c_type):
        self.genome = genome
        self.a_class = classes
        self.bio_def = bio_def
        self.type = c_type


class Dog(Animal):
    isPet = True

    def __init__(self, breed):
        super().__init__(self, "Canis", "Carnivore", "Dog")
        self.breed = breed

class Person:
    def __init__(self, f_Name, s_Name, subject, isAwesome):
        self.fName = f_Name
        self.sName = s_Name
        self.subject = subject

        subjects.append(self.subject)
        self._isAwesome = bool(isAwesome)

    def killMyself(self):
        if self._isAwesome:
            ToBkilledOrNotToBKilledThatIsTheQuestion = " is awesome, not allowed to be killed."
        else:
            ToBkilledOrNotToBKilledThatIsTheQuestion = " is now dead."

        killed = print("{0}{1}".format(self.fName, ToBkilledOrNotToBKilledThatIsTheQuestion))
        return killed


Will = Person("Will", "Greatest", ["Comp Sci"], True)
Kewal = Person("Kewal", "Bitch-Boi", ["Maths"], True)
Bob = Person("Bob", "Smith", ["Turfgrass Science"], False)

Loki = Dog("Samoyed")
Thor = Dog("Samoyed")


'''
Is there a way to access all classes? E.g
If class name eqiuals animal isAllowed2Die is automatically False
'''

def main():
    print(subjects, "\n")

    Person.killMyself(Will)
    Person.killMyself(Kewal)

if __name__ == '__main__':
    main()