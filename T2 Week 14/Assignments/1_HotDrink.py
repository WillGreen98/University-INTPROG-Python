class HotDrink:
    def __init__(self, servingTempreture, numSugars):
        self.servingTempreture = 0
        self.numSugars = 0

    def changeServingTempreture(self, newTemp):
        self.servingTempreture = newTemp 

    def changeNumberSugars(self, numSugars):
        self.numSugars = numSugars

class Tea(HotDrink):
    def __init__(self):
        HotDrink.__init__(self, 38, 2)
        