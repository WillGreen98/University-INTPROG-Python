class Animal:
    def __init__(self, name, owner, noiseMade, furColour):
        self.name = name
        self.owner = owner 
        self.noiseMade = noiseMade
        self.furColour = furColour

    def changeOwner(self, newOwnerName):
        self.owner = newOwnerName 

    def changeName(self, newName):
        self.name = newName 
    
    def makeNoise(self):
        print(self.name, "says", self.noiseMade)


class Cat(Animal):
    def __init__(self, name, owner, furColour, favFood):
        Animal.__init__(self, name, owner, "meow", furColour)
        self.favFood = favFood

    def eatFavouriteFood(self):
        print(self.name, "eats", self.favFood)

    def changeFavouriteFood(self, newFavFood):
        self.favFood = newFavFood

    def scratchOwner(self):
        print(self.name, "scratches", self.owner)

    def purr(self):
        print(self.name, "says purrrr")


class Dog(Animal):
    def __init__(self, name, owner, furColour, favChewToy):
        Animal.__init__(self, name, owner, "woof", furColour)
        self.favChewToy = favChewToy

    def playWithFavouriteToy(self):
        print(self.name, "plays with", self.favChewToy)

    def wagTail(self):
        print(self.name, "wags their tail")
        
        
dog = Dog("Bob", "James", "Red", "Bone")
dog.makeNoise()

    