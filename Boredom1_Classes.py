subjects = []

isAllowed2Die = False

class animal:
    def __init__(self, genome, classes, bio_def, type, name):
        self.genome = genome
        self.a_class = classes
        self.bio_def = bio_def
        self.type = type
        self.name = name


class dog(animal):
    animal.__init__(self, canis, carnivore, dog, breed, input())


class person:
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


Will = person("Will", "Green", ["Comp Sci"], True)
Kewal = person("Kewal", "Rai", ["Maths"], True)
Bob = person("Bob", "Smith", ["Turfgrass Science"], False)

Samoyed = dog()


'''
if class eqiuals animal isAllowed2Die is automatically False
'''

def main():
    print(subjects, "\n")

    person.killMyself(Will)
    person.killMyself(Kewal)

if __name__ == '__main__':
    main()