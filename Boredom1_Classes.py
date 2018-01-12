subjects = []

isAllowed2Die = False

class Animal:
    def __init__(self, genome, classes, bio_def, type):
        self.genome = genome
        self.a_class = classes
        self.bio_def = bio_def
        self.type = type


class Dog(Animal):
    Animal.__init__(self, canis, carnivore, dog, breed="Unknown")


class Person:
    def __init__(self, f_Name, s_Name, subject, isAwesome):
        self.fName = f_Name
        self.sName = s_Name
        self.subject = subject
        subjects.append(self.subject)
        self._isAwesome = bool(isAwesome)

    def killMyself(self):
        if self._isAwesome:
            mystr = " is awesome, not allowed to be killed."
        else:
            mystr = " is now dead."

        killed = print("{0}{1}".format(self.fName, mystr))
        return killed


Will = Person("Will", "Greatest", ["Comp Sci"], True)
Kewal = Person("Kewal", "Bitch-Boi", ["Maths"], True)
Bob = Person("Bob", "Smith", ["Turfgrass Science"], False)

Loki = Dog()
Thor = Dog()


'''
Is there a way to access all classes? E.g
if class name eqiuals animal isAllowed2Die is automatically False
'''

def main():
    print(subjects, "\n")

    Person.killMyself(Will)
    Person.killMyself(Kewal)

if __name__ == '__main__':
    main()