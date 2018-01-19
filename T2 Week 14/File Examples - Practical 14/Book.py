class Book:
    
    def __init__(self, bTitle, bAuthor, bPages, bISBN, bCost, bSelling):
        self.title = bTitle
        self.author = bAuthor
        self.numPages = bPages
        self.isbn = bISBN
        self.costPrice = bCost
        self.numCopies = 0
        self.sellingPrice = bSelling
        
    def changePrice(self, newPrice):
        self.sellingPrice = newPrice
    
    def sellCopy(self):
        if self.numCopies == 0:
            print("There are no copies to sell")
        else:
            self.numCopies -= 1
        return self.sellingPrice
    
    def restockBook(self, numNewCopies):
        self.numCopies += numNewCopies
        return numNewCopies * self.costPrice
    
    def retrieveInformation(self):
        infoString = "Title: " + self.title
        infoString += "\nAuthor: " + self.author
        infoString += "\nNumber of Pages: " + str(self.numPages)
        infoString += "\nISBN: " + str(self.isbn)
        infoString += "\nCost Price: £" + str(self.costPrice)
        infoString += "\nSelling Price: £" + str(self.sellingPrice)
        infoString += "\nNumber of Copies: " + str(self.numCopies)
        
        return infoString
    