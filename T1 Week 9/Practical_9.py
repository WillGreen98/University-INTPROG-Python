import graphics as g

def displayDate(day, month, year):
    months = {
        1: "Janurary",
        2: "Feburay",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    print(day, months[month], year)

def wordLength(words = []):
    while len(words) <= 2:
        word = input("Enter word: ")
        words.append(word)

    for i in range(len(words)):
        print("word: {0} len: {1}".format(words[i], len(words[i])))

# TODO doesn't work
def drawHexagon():
    points = []

    window = g.GraphWin("Hexagon", 400, 400)

    point1 = window.getMouse()
    point2 = window.getMouse()
    point3 = window.getMouse()
    point4 = window.getMouse()
    point5 = window.getMouse()
    point6 = window.getMouse()

    poly = g.Polygon(point1, point2, point3, point4, point5, point6).draw(window).setFill("red")
    window.getMouse()

def testMarks():
    marks = []
    grades = [0, 1, 2, 3, 4, 5]

    marking = True
    while marking:
        usr_In = input("(Press 6 to quit) Enter mark: ")
        marks.append(int(usr_In))

        if usr_In == '6':
            for i in range(6):
                counter = marks.count(grades[i])
                print("{0} students got {1} marks".format(counter, grades[i]))
            break

# TODO doesn't work
def drawBarChart(*args):
    for i in range(max(args)):  # iterate on even numbered indexes (to get the *'s)
        for column in args:  # iterate over the list of strings
            if i < len(column):
                print(column[i]),  # the comma means no newline will be printed
            else:
                print(" "),  # put spaces in for missing values
        print()

    # displayDate(14, 2, 2011)
# wordLength()
# drawHexagon()
# testMarks()

drawBarChart(3, 5, 7)