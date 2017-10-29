import graphics as g

def personalGreeting():
    name = str(input("Hello there, what is your name? : "))
    print("Hello ",name, " nice to see you!")

def formalName():
    full_Name = str(input("Hello there, what is your name? : "))
    split_Name = full_Name.split()
    f_Name = split_Name[0]
    s_Name = split_Name[1]

    print(f_Name[:1], ".", s_Name)

def kilos2pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print(kilos, "Kilos is: ", pounds, "Lbs")

def emailFormatting():
    full_Name = str(input("Hello there, what is your name? : "))
    split_Name = full_Name.split()
    f_Name = split_Name[0]
    s_Name = split_Name[1]

    yr_Entered = print("What year did you start? (YYYY): ")

    print("Email: ", s_Name[:4], ".", f_Name[:1], ".", yr_Entered[-2], "@myport.ac.uk")

def gradeTest():
    grades = "AAABBCCFFFF"
    g_Flipped = grades[::-1]
    grade_Index = int(input("Enter mark: "))
    print(g_Flipped[grade_Index])

def graphicalLetters():
    graphical_Letters_Window = g.GraphWin("Letters", 400, 400)

    input_Letters = str(input("Enter letters: "))
    for letters in input_Letters:
        letters = g.Text(graphical_Letters_Window.getMouse(), letters).draw(graphical_Letters_Window)
        letters.setSize(22)

    graphical_Letters_Window.getMouse()

def singSong():
    word_Input = str(input("Enter sing song word: "))
    words_Per_Line = int(input("Enter number per line: "))
    lines = int(input("Enter number of lines: "))

    for i in range(lines):
        print(word_Input, " " * words_Per_Line)

def exchangeTable():
    for euros in range(21):
        pounds = euros / 1.09
        print("Euros: ", euros, " --- Pounds: ", pounds)

def makeAcronym():
    usr_In = str(input("Enter your input: ")).upper()

    for words in usr_In.split():
        print(words[:1], end="")

def nameToNumber():
    name = str(input("Enter yo name: "))

    ascii_Sum = 0
    for chars in name.title():
        ascii_Sum += ord(chars)
    print([ord(char) for char in name], " = ", ascii_Sum)