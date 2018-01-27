class Padlock:
    def __init__(self, code):
        self.code = code
        self.isLocked = True
         
    def open(self, code):
        if self.code == code:
            self.isLocked = False 
        else:
            print("Invalid password, padlock is still locked")
            
    def close(self):
        self.isLocked = False
        
    def changeCode(self, newCode):
        if (len(newCode) != len(newCode)):
            print("Invalid length for passcode")
        elif (self.isLocked):
            print ("Unable to change password when padlock is locked")
        else:
            self.code == code
            