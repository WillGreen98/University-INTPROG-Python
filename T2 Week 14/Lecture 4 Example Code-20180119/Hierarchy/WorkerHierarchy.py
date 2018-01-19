class Worker:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def changeAddress(self, newAddress):
        self.address = newAddress