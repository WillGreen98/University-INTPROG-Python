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

    for i in range(0, 5):
        point = window.getMouse()
        points.append(point[i])

    poly = g.Polygon(points).draw(window).setFill("red")
    window.getMouse()


def testMarks():
    marks = []
    grades = [0, 1, 2, 3, 4, 5]

    marking = True
    while marking:
        grade = input("(Press Q to quit) Enter mark: ")
        marks.append(int(grade))

        if grade == '6' or grade == 'Q':
            for i in range(6):
                counter = marks.count(grades[i])
                print("{0} students got {1} marks".format(counter, grades[i]))
            break




# displayDate(14, 2, 2011)
# wordLength()
# drawHexagon()


testMarks()