from Book import Book

class Bookshop:
    
    def __init__(self, listOfBooks):
        self.bookList = listOfBooks
        self.valueSpentTotal = 0
        self.valueSoldTotal = 0
        self.valueSpentDay = 0
        self.valueSoldDay = 0

    def openBookshop(self):
        
        print("\nThe bookshop is open\n")
        
        bookShopOpen = True
        
        self.valueSpentDay = 0
        self.valueSoldDay = 0
        
        while bookShopOpen:
            bookAction = input("Please enter what you would like to do (c = close, p = purchase, s = sell): ")
            
            if bookAction == "c":
                bookShopOpen = False
            elif bookAction == "p":
                self.purchaseBook(self.getBookIndex())
            elif bookAction == "s":
                self.sellBook(self.getBookIndex())
            else:
                print("Not a valid action, try again")
                
        print("\nThe bookshop is closed\n")
                
    def sellBook(self, bookIndex):
        sellValue = self.bookList[bookIndex].sellCopy()
        self.valueSoldTotal += sellValue
        self.valueSoldDay += sellValue
        
    def purchaseBook(self, bookIndex):
        continueLoop = True
        while continueLoop:
            restockQty = input("Please enter the quantity of books required: ")
            if restockQty.isdigit():
                continueLoop = False
            else:
                print("Must be a number, try again")
        
        restockValue = self.bookList[bookIndex].restockBook(eval(restockQty))
        
        self.valueSpentTotal += restockValue
        self.valueSpentDay += restockValue
        
    def getBookIndex(self):
        noBooks = len(self.bookList)
        print("You have the following books in stock\n")
        
        for i in range(noBooks):
            print("[",i,"] - ",self.bookList[i].author,"; ",self.bookList[i].title)
            
        continueLoop = True
        while continueLoop:
            bookIndex = input("Please enter the item number for the book: ")
            if bookIndex.isdigit():
                bookIndex = eval(bookIndex)
                if bookIndex < noBooks and bookIndex >= 0:
                    continueLoop = False
                else:
                    print("Invalid reference number, try again")
            else:
                print("Must be a number, try again")
            
        return bookIndex
        
    def printEndOfDaySummary(self):
        print("\n\nDay Summary\n\n")
        print("Total Spent: ",self.valueSpentDay)
        print("Total Sold: ",self.valueSoldDay)
        print("Profit: ",self.valueSoldDay - self.valueSpentDay)
        
        print("\n\nLifetime Summary\n\n")
        print("Total Spent: ",self.valueSpentTotal)
        print("Total Sold: ",self.valueSoldTotal)
        print("Profit: ",self.valueSoldTotal - self.valueSpentTotal)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        