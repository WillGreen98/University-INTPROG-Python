class Padlock:
    
    def __init__(self, pCode):
        self.code = pCode
        self.opened = False
        
    def openLock(self, combination):
        if combination == self.code:
            self.opened = True
        else:
            print("Incorrect code, try again!")
        return self.opened
    
    def closeLock(self):
        self.opened = False
    
    def changeCombination(self, newCombination):
        if self.opened:
            oldCodeLength = len(self.code)
            newCodeLength = len(newCombination)
            if oldCodeLength == newCodeLength:
                self.code = newCombination
            elif oldCodeLength > newCodeLength:
                print("Code too short")
            else:
                print("Code too long")
        else:
            print("Open the lock before changing the code")
                
                
                
                
                